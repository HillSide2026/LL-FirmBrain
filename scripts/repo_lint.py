#!/usr/bin/env python3
"""
repo_lint.py - governed repo structure and metadata lint checks.

Exit codes:
  0 = no errors or warnings
  1 = one or more errors
  2 = warnings only
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote


REPO_ROOT = Path(__file__).resolve().parent.parent
GOVERNED_ROOTS = [
    "00_SYSTEM",
    "01_DOCTRINE",
    "02_PLAYBOOKS",
    "03_TEMPLATES",
    "04_INITIATIVES",
    "05_MATTERS",
    "06_RUNS",
    "07_REFERENCE",
    "08_RESEARCH",
    "09_INBOX",
    "10_ARCHIVE",
]
IGNORED_DIRS = {
    ".git",
    ".venv",
    "__pycache__",
    "node_modules",
}
DEFAULT_MAX_FINDINGS = 100

# Per-matter generated files that don't require frontmatter
MATTER_GENERATED_FILENAMES = {"DOC_DELTAS.md", "DOC_INDEX.md", "MATTER_STATUS.md"}

# Portfolio management agent output filenames (internal working material per CLAUDE.md)
PORTFOLIO_MGMT_OUTPUT_FILENAMES = {
    "BOTTLENECK_ANALYSIS.md",
    "CAPACITY_ALLOCATION_MODEL.md",
    "PORTFOLIO_STATUS_DASHBOARD.md",
    "PROJECT_PRIORITY_MATRIX.md",
    "RESOURCE_COLLISION_REPORT.md",
    "SEQUENCING_RECOMMENDATIONS.md",
    "STAGE_DISTRIBUTION_REPORT.md",
    "WIP_LOAD_ANALYSIS.md",
    "PROJECT_HEALTH_ROLLUP.md",
    "APPROVAL_GAP_REPORT.md",
    "CONTRADICTION_ALERTS.md",
    "DOCTRINE_DRIFT_REPORT.md",
    "GOVERNANCE_COMPLIANCE_AUDIT.md",
    "METRIC_SCHEMA_INTEGRITY_REPORT.md",
    "MIGRATION_VALIDATION_REPORT.md",
    "PM_CONFORMANCE_REPORT.md",
    "STAGE_GATE_VIOLATION_REPORT.md",
    "COS_BRIEF.md",
    "CROSS_AGENT_CONFLICTS.md",
    "ML1_DECISION_QUEUE.md",
}
REQUIRED_FRONTMATTER_FIELDS = [
    "id",
    "title",
    "owner",
    "status",
    "created_date",
    "last_updated",
    "tags",
]
LINK_PATTERN = re.compile(r"(?<!!)\[[^\]\n]+\]\(([^)\n]+)\)")
REFERENCE_LINK_PATTERN = re.compile(r"^\[[^\]]+\]:\s+(\S+)", re.MULTILINE)
FRONTMATTER_PATTERN = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
FIELD_PATTERN = re.compile(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--fail-on-warn",
        action="store_true",
        help="Return exit code 1 when warnings are present.",
    )
    parser.add_argument(
        "--max-findings",
        type=int,
        default=DEFAULT_MAX_FINDINGS,
        help="Maximum number of errors and warnings to print per group.",
    )
    return parser.parse_args()


def iter_repo_paths() -> list[Path]:
    paths: list[Path] = []
    for root, dirs, files in os.walk(REPO_ROOT):
        dirs[:] = [d for d in dirs if d not in IGNORED_DIRS]
        root_path = Path(root)
        for name in files:
            path = root_path / name
            if not is_lint_excluded(path):
                paths.append(path)
    return paths


def iter_governed_markdown() -> list[Path]:
    files: list[Path] = []
    for root_name in GOVERNED_ROOTS:
        root = REPO_ROOT / root_name
        if not root.exists():
            continue
        for path in root.rglob("*.md"):
            if any(part in IGNORED_DIRS for part in path.parts):
                continue
            if is_lint_excluded(path):
                continue
            files.append(path)
    return sorted(files)


def rel(path: Path) -> str:
    return str(path.relative_to(REPO_ROOT))


def is_lint_excluded(path: Path) -> bool:
    """Exclude raw/generated runtime material from governed-source linting."""
    relative_parts = path.relative_to(REPO_ROOT).parts
    if len(relative_parts) >= 2 and relative_parts[0] == "06_RUNS":
        if relative_parts[1].startswith("RUN-") or relative_parts[1] in {"ops", "state"}:
            return True
    if len(relative_parts) >= 3 and relative_parts[:2] == ("09_INBOX", "_sources"):
        return True
    if len(relative_parts) >= 2 and relative_parts[0] in {"cache", "screenshots"}:
        return True
    # Per-matter generated operational files
    if relative_parts[0] == "05_MATTERS" and path.name in MATTER_GENERATED_FILENAMES:
        return True
    # Operational matter dashboards
    if len(relative_parts) >= 2 and relative_parts[:2] == ("05_MATTERS", "DASHBOARDS"):
        return True
    # Portfolio management agent outputs (classified as internal working material)
    if relative_parts[0] == "04_INITIATIVES" and len(relative_parts) >= 3:
        if relative_parts[1:3] == ("LL_PORTFOLIO", "CHIEF_OF_STAFF"):
            return True
        if (
            len(relative_parts) >= 4
            and relative_parts[1:4] == ("LL_PORTFOLIO", "03_FIRM_OPERATIONS", "PORTFOLIO_GOVERNANCE")
        ):
            return True
    if relative_parts[0] == "04_INITIATIVES" and path.name in PORTFOLIO_MGMT_OUTPUT_FILENAMES:
        return True
    return False


def parse_frontmatter(path: Path) -> tuple[dict[str, str], bool]:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return {}, False

    match = FRONTMATTER_PATTERN.match(text)
    if not match:
        return {}, False

    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        field_match = FIELD_PATTERN.match(line)
        if field_match:
            fields[field_match.group(1)] = field_match.group(2).strip()
    return fields, True


def is_external_link(target: str) -> bool:
    lowered = target.lower()
    return (
        lowered.startswith("http://")
        or lowered.startswith("https://")
        or lowered.startswith("mailto:")
        or lowered.startswith("tel:")
        or lowered.startswith("app://")
    )


def normalize_link_target(target: str) -> str:
    target = target.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    target = target.split("#", 1)[0]
    return unquote(target.strip())


def is_repo_absolute_path(target: str) -> bool:
    if not target.startswith("/"):
        return False
    first_part = target.lstrip("/").split("/", 1)[0]
    return first_part in GOVERNED_ROOTS or first_part in {"scripts", "gmail_governance"}


def check_frontmatter(markdown_files: list[Path]) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    ids: dict[str, list[Path]] = defaultdict(list)

    for path in markdown_files:
        fields, has_frontmatter = parse_frontmatter(path)
        if not has_frontmatter:
            warnings.append(f"missing frontmatter: {rel(path)}")
            continue

        missing_fields = [field for field in REQUIRED_FRONTMATTER_FIELDS if field not in fields]
        if missing_fields:
            warnings.append(
                f"incomplete frontmatter: {rel(path)} missing {', '.join(missing_fields)}"
            )

        artifact_id = fields.get("id")
        if artifact_id:
            ids[artifact_id].append(path)

    for artifact_id, paths in sorted(ids.items()):
        if len(paths) > 1:
            locations = ", ".join(rel(path) for path in paths)
            errors.append(f"duplicate frontmatter id '{artifact_id}': {locations}")

    return errors, warnings


def check_root_runtime_dirs() -> list[str]:
    errors: list[str] = []
    for dirname in ("logs", "state"):
        if (REPO_ROOT / dirname).exists():
            errors.append(f"invalid root runtime dir: {dirname}/")
    return errors


def check_non_ascii_filenames(paths: list[Path]) -> list[str]:
    warnings: list[str] = []
    for path in paths:
        relative = rel(path)
        try:
            relative.encode("ascii")
        except UnicodeEncodeError:
            warnings.append(f"non-ASCII filename: {relative}")
    return warnings


def extract_link_targets(text: str) -> list[str]:
    targets = [match.group(1) for match in LINK_PATTERN.finditer(text)]
    targets.extend(match.group(1) for match in REFERENCE_LINK_PATTERN.finditer(text))
    return targets


def check_broken_relative_links(markdown_files: list[Path]) -> list[str]:
    warnings: list[str] = []
    for path in markdown_files:
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            warnings.append(f"cannot read markdown as UTF-8 for link scan: {rel(path)}")
            continue

        for raw_target in extract_link_targets(text):
            target = normalize_link_target(raw_target)
            if not target or target.startswith("#") or is_external_link(target):
                continue
            if target.startswith("/") and not is_repo_absolute_path(target):
                continue

            candidate = (path.parent / target).resolve() if not target.startswith("/") else (
                REPO_ROOT / target.lstrip("/")
            ).resolve()

            try:
                candidate.relative_to(REPO_ROOT)
            except ValueError:
                warnings.append(f"relative link escapes repo: {rel(path)} -> {raw_target}")
                continue

            if not candidate.exists():
                warnings.append(f"broken relative link: {rel(path)} -> {raw_target}")

    return warnings


DOCTRINE_ROOTS = {"01_DOCTRINE", "02_PLAYBOOKS", "03_TEMPLATES"}
DEPRECATED_STATUS_PATTERN = re.compile(r"^status:\s+active\s*$", re.MULTILINE)


def check_deprecated_status(markdown_files: list[Path]) -> list[str]:
    """Warn on 'status: active' in doctrine/playbook/template layers (should be 'approved')."""
    warnings: list[str] = []
    for path in markdown_files:
        if path.relative_to(REPO_ROOT).parts[0] not in DOCTRINE_ROOTS:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if DEPRECATED_STATUS_PATTERN.search(text):
            warnings.append(
                f"deprecated status 'active' (use 'approved'): {rel(path)}"
            )
    return warnings


def print_group(title: str, items: list[str], label: str, max_findings: int) -> None:
    if not items:
        return
    print(title)
    print("-" * 40)
    for item in items[:max_findings]:
        print(f"  {label}: {item}")
    omitted = len(items) - max_findings
    if omitted > 0:
        print(f"  ... {omitted} more {label.lower()} entries omitted; rerun with --max-findings 0 for all")
    print()


def main() -> int:
    args = parse_args()
    repo_paths = iter_repo_paths()
    markdown_files = iter_governed_markdown()

    errors: list[str] = []
    warnings: list[str] = []

    fm_errors, fm_warnings = check_frontmatter(markdown_files)
    errors.extend(fm_errors)
    warnings.extend(fm_warnings)
    errors.extend(check_root_runtime_dirs())
    warnings.extend(check_non_ascii_filenames(repo_paths))
    warnings.extend(check_broken_relative_links(markdown_files))
    warnings.extend(check_deprecated_status(markdown_files))

    print("=" * 60)
    print("Repo Lint Check")
    print("=" * 60)
    print()
    print(f"Governed markdown files scanned: {len(markdown_files)}")
    print(f"Repo paths scanned:              {len(repo_paths)}")
    print(f"Errors:                          {len(errors)}")
    print(f"Warnings:                        {len(warnings)}")
    print()

    max_findings = len(errors) + len(warnings) if args.max_findings == 0 else args.max_findings
    print_group("ERRORS", errors, "ERROR", max_findings)
    print_group("WARNINGS", warnings, "WARN", max_findings)

    print("=" * 60)
    if errors:
        print("STATUS: FAIL")
        return 1
    if warnings:
        print("STATUS: WARN")
        return 1 if args.fail_on_warn else 2
    print("STATUS: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
