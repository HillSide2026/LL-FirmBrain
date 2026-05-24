#!/usr/bin/env python3
"""
Minimal local runner for System Management Agents (SMA-001..SMA-007).

Writes artifacts to:
  06_RUNS/${run_id}/system_management/
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Tuple


REPO_ROOT = Path(__file__).resolve().parents[2]
FOLDER_MAP_PATH = REPO_ROOT / "00_SYSTEM" / "architecture" / "FOLDER_MAP.md"
BACKLOG_PATH = REPO_ROOT / "04_INITIATIVES" / "SYSTEM_PORTFOLIO" / "BACKLOG.md"
AGENT_TYPOLOGY_PATH = REPO_ROOT / "00_SYSTEM" / "AGENTS" / "specs" / "AGENT_TYPOLOGY.md"
INTEGRATIONS_DIR = REPO_ROOT / "00_SYSTEM" / "integrations"
AGENTS_DIR = REPO_ROOT / "00_SYSTEM" / "AGENTS"
MCP_CONFIG_PATH = REPO_ROOT / ".mcp.json"
CLAUDE_DIR = REPO_ROOT / ".claude"
RUN_GRAPHS_DIR = REPO_ROOT / "00_SYSTEM" / "orchestration" / "run_graphs"

REQUIRED_SECTIONS = [
    "## Summary",
    "## Findings",
    "## Recommendations",
    "## Actions",
    "## Escalations Required (if any)",
    "## Evidence",
    "## Assumptions / Confidence",
]

REQUIRED_FRONTMATTER_FIELDS = [
    "id",
    "title",
    "owner",
    "status",
    "created_date",
    "last_updated",
    "tags",
]

AGENT_LIFECYCLE_STATES = {
    "Draft",
    "Planned",
    "Active",
    "Deprecated",
    "Archived",
}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def generate_run_id() -> str:
    stamp = datetime.now(timezone.utc).strftime("%H%M%SZ")
    date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    return f"RUN-{date}-SYSTEM-MANAGEMENT-SWEEP-{stamp}"


def top_level_root(path: str) -> str:
    return path.split("/", 1)[0]


def load_folder_map_roots() -> List[str]:
    if not FOLDER_MAP_PATH.exists():
        return []
    roots: List[str] = []
    pattern = re.compile(r"^-\s+([0-9]{2}_[A-Z0-9_]+)\b")
    for line in FOLDER_MAP_PATH.read_text(encoding="utf-8").splitlines():
        match = pattern.match(line.strip())
        if match:
            roots.append(match.group(1))
    return roots


def fallback_roots() -> List[str]:
    return [p.name for p in REPO_ROOT.iterdir() if p.is_dir() and re.match(r"^[0-9]{2}_", p.name)]


def governed_roots() -> List[str]:
    roots = load_folder_map_roots()
    return roots if roots else fallback_roots()


def extract_frontmatter_block(content: str) -> Optional[List[str]]:
    lines = content.splitlines()
    idx = 0
    while idx < len(lines) and not lines[idx].strip():
        idx += 1
    if idx >= len(lines) or lines[idx].strip() != "---":
        return None
    block: List[str] = []
    for line in lines[idx + 1 :]:
        if line.strip() == "---":
            return block
        block.append(line)
    return None


def parse_frontmatter_fields(path: Path) -> Optional[Dict[str, str]]:
    try:
        content = path.read_text(encoding="utf-8")
    except Exception:
        return None
    block = extract_frontmatter_block(content)
    if block is None:
        return None
    fields: Dict[str, str] = {}
    for raw_line in block:
        line = raw_line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        if re.fullmatch(r"[A-Za-z0-9_]+", key.strip()):
            fields[key.strip()] = value.strip()
    return fields


def missing_frontmatter_fields(fields: Dict[str, str]) -> List[str]:
    missing: List[str] = []
    for key in REQUIRED_FRONTMATTER_FIELDS:
        if key not in fields:
            missing.append(key)
            continue
        if key != "tags" and not fields[key]:
            missing.append(key)
    return missing


def split_markdown_row(line: str) -> List[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def is_markdown_separator_row(line: str) -> bool:
    cells = split_markdown_row(line)
    if not cells:
        return False
    normalized = [cell.replace(" ", "") for cell in cells]
    return all(re.fullmatch(r":?-{3,}:?", cell) for cell in normalized)


def parse_markdown_tables(content: str) -> List[Tuple[List[str], List[Dict[str, str]]]]:
    tables: List[Tuple[List[str], List[Dict[str, str]]]] = []
    lines = content.splitlines()
    idx = 0
    while idx < len(lines) - 1:
        if (
            lines[idx].strip().startswith("|")
            and lines[idx + 1].strip().startswith("|")
            and is_markdown_separator_row(lines[idx + 1])
        ):
            headers = split_markdown_row(lines[idx])
            idx += 2
            rows: List[Dict[str, str]] = []
            while idx < len(lines) and lines[idx].strip().startswith("|"):
                cells = split_markdown_row(lines[idx])
                if len(cells) < len(headers):
                    cells.extend([""] * (len(headers) - len(cells)))
                row = {headers[pos]: cells[pos] for pos in range(len(headers))}
                rows.append(row)
                idx += 1
            tables.append((headers, rows))
            continue
        idx += 1
    return tables


def parse_table_by_header(path: Path, required_headers: List[str]) -> List[Dict[str, str]]:
    if not path.exists():
        return []
    content = path.read_text(encoding="utf-8")
    for headers, rows in parse_markdown_tables(content):
        if all(header in headers for header in required_headers):
            return rows
    return []


def extract_backlog_dependency_ids(text: str) -> List[str]:
    return re.findall(r"\b(?:SYS|SMA)-\d{3}\b", text or "")


def active_stage_dirs() -> List[Path]:
    active_root = REPO_ROOT / "04_INITIATIVES" / "SYSTEM_PORTFOLIO" / "01_ACTIVE_ROADMAPS"
    if not active_root.exists():
        return []
    return sorted(
        [
            path
            for path in active_root.iterdir()
            if path.is_dir() and re.fullmatch(r"STAGE\d+", path.name)
        ],
        key=lambda path: path.name,
    )


def stage_artifact_flags(stage_dir: Path) -> Dict[str, bool]:
    file_names = {path.name for path in stage_dir.iterdir() if path.is_file()}
    prefix = stage_dir.name
    return {
        "kickoff": any(name.startswith(f"{prefix}_AUTHORIZATION_KICKOFF") for name in file_names),
        "action_plan": any(name.startswith(f"{prefix}_ACTION_PLAN") for name in file_names),
        "readme": "README.md" in file_names,
    }


def split_html_break_paths(cell: str) -> List[str]:
    if not cell:
        return []
    parts = re.split(r"<br\s*/?>", cell)
    return [part.strip().strip("`").rstrip(".,;") for part in parts if part.strip()]


def resolve_repo_path(path_text: str) -> Optional[Path]:
    cleaned = path_text.strip().strip("`").rstrip(".,;")
    if not cleaned or "/" not in cleaned:
        return None
    candidate = cleaned.split(":", 1)[0].rstrip("/")
    if not candidate:
        return None
    if candidate.startswith("/"):
        return Path(candidate)
    return REPO_ROOT / candidate


def inbox_artifacts() -> List[Tuple[str, int]]:
    inbox_root = REPO_ROOT / "09_INBOX"
    if not inbox_root.exists():
        return []
    now = datetime.now(timezone.utc)
    artifacts: List[Tuple[str, int]] = []
    for path in inbox_root.rglob("*"):
        if not path.is_file():
            continue
        if path.name == ".gitkeep":
            continue
        rel = path.relative_to(REPO_ROOT).as_posix()
        if rel == "09_INBOX/README.md":
            continue
        parts = rel.split("/")
        if len(parts) > 1 and parts[1] in {"_sources", "_AGENT_OUTPUT"}:
            continue
        age_days = int((now - datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc)).days)
        artifacts.append((rel, age_days))
    return sorted(artifacts, key=lambda item: (-item[1], item[0]))


def governed_markdown_files() -> List[Path]:
    files: List[Path] = []
    for root in governed_roots():
        if root == "06_RUNS":
            continue
        root_path = REPO_ROOT / root
        if not root_path.exists():
            continue
        files.extend(sorted(root_path.rglob("*.md")))
    return files


def markdown_links(content: str) -> List[str]:
    links: List[str] = []
    for match in re.finditer(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", content):
        target = match.group(1).strip()
        if not target or target.startswith(("#", "http://", "https://", "mailto:")):
            continue
        links.append(target.split("#", 1)[0])
    return links


def relative_link_exists(source: Path, target: str) -> bool:
    cleaned = target.strip().strip("<>").replace("%20", " ")
    if not cleaned:
        return True
    if cleaned.startswith("/"):
        return (REPO_ROOT / cleaned.lstrip("/")).exists()
    return (source.parent / cleaned).resolve().exists()


def typology_entries() -> List[Dict[str, str]]:
    rows: List[Dict[str, str]] = []
    if not AGENT_TYPOLOGY_PATH.exists():
        return rows
    content = AGENT_TYPOLOGY_PATH.read_text(encoding="utf-8")
    for headers, table_rows in parse_markdown_tables(content):
        if {"Agent", "Class", "Status", "Path"}.issubset(headers):
            rows.extend(table_rows)
    return rows


def extract_section_lines(content: str, heading: str) -> Optional[List[str]]:
    lines = content.splitlines()
    for idx, line in enumerate(lines):
        if line.strip() != heading:
            continue
        section: List[str] = []
        for follow in lines[idx + 1 :]:
            if follow.startswith("## "):
                break
            section.append(follow)
        return section
    return None


def git_changed_paths() -> List[str]:
    try:
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=REPO_ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
    except FileNotFoundError:
        return []
    if result.returncode != 0:
        return []
    paths: List[str] = []
    for line in result.stdout.splitlines():
        if not line:
            continue
        status = line[:2]
        path = line[3:].strip()
        if " -> " in path:
            path = path.split(" -> ", 1)[1].strip()
        if "D" in status:
            continue
        if path:
            paths.append(path)
    return sorted(set(paths))


def has_frontmatter(md_path: Path) -> bool:
    try:
        content = md_path.read_text(encoding="utf-8")
    except Exception:
        return False
    lines = content.splitlines()
    # Skip leading blank lines
    idx = 0
    while idx < len(lines) and not lines[idx].strip():
        idx += 1
    if idx >= len(lines) or lines[idx].strip() != "---":
        return False
    for j in range(idx + 1, min(len(lines), idx + 100)):
        if lines[j].strip() == "---":
            return True
    return False


def render_report(
    title: str,
    summary: List[str],
    findings: List[str],
    recommendations: List[str],
    actions: List[str],
    escalations: List[str],
    evidence: List[str],
    assumptions: List[str],
) -> str:
    lines: List[str] = []
    lines.append("## Summary")
    for item in summary:
        lines.append(f"- {item}")
    lines.append("")

    lines.append("## Findings")
    if findings:
        for i, item in enumerate(findings, start=1):
            lines.append(f"{i}. {item}")
    else:
        lines.append("1. None.")
    lines.append("")

    lines.append("## Recommendations")
    if recommendations:
        for i, item in enumerate(recommendations, start=1):
            lines.append(f"{i}. {item}")
    else:
        lines.append("1. None.")
    lines.append("")

    lines.append("## Actions")
    if actions:
        for item in actions:
            lines.append(f"- [ ] {item}")
    else:
        lines.append("- [ ] None.")
    lines.append("")

    lines.append("## Escalations Required (if any)")
    if escalations:
        for item in escalations:
            lines.append(f"- {item}")
    else:
        lines.append("- None.")
    lines.append("")

    lines.append("## Evidence")
    if evidence:
        for item in evidence:
            lines.append(f"- {item}")
    else:
        lines.append("- None.")
    lines.append("")

    lines.append("## Assumptions / Confidence")
    if assumptions:
        for item in assumptions:
            lines.append(f"- {item}")
    else:
        lines.append("- None.")
    lines.append("")

    return "\n".join(lines)


def write_report(path: Path, title: str, body: str) -> None:
    frontmatter = "\n".join(
        [
            "---",
            f"id: {slugify(path.stem)}",
            f"title: {title}",
            "owner: ML1",
            "status: draft",
            f"created_date: {datetime.now(timezone.utc).strftime('%Y-%m-%d')}",
            f"last_updated: {datetime.now(timezone.utc).strftime('%Y-%m-%d')}",
            "tags: [system-management, run]",
            "---",
            "",
        ]
    )
    path.write_text(frontmatter + body, encoding="utf-8")


def slugify(text: str) -> str:
    return re.sub(r"[^a-zA-Z0-9]+", "_", text.strip().lower()).strip("_")


def sma_001_report(changed_paths: List[str], roots: List[str]) -> Tuple[str, List[str]]:
    governed = []
    off_map_numbered_roots = []
    for p in changed_paths:
        root = top_level_root(p)
        if root in roots:
            governed.append(p)
        elif re.match(r"^[0-9]{2}_", root):
            off_map_numbered_roots.append(p)
    md_paths = [p for p in governed if p.lower().endswith(".md")]
    missing_frontmatter = []
    invalid_frontmatter = []
    for p in md_paths:
        full_path = REPO_ROOT / p
        if not full_path.exists():
            continue
        if not has_frontmatter(full_path):
            missing_frontmatter.append(p)
            continue
        fields = parse_frontmatter_fields(full_path) or {}
        missing_fields = missing_frontmatter_fields(fields)
        if missing_fields:
            invalid_frontmatter.append(f"{p} -> missing fields: {', '.join(missing_fields)}")

    summary = [
        f"Scope: working tree changes ({len(changed_paths)} files).",
        f"Governed changes reviewed: {len(governed)}.",
        f"Folder placement: {'PASS' if not off_map_numbered_roots else 'FAIL'} (numbered-root changes checked against FOLDER_MAP).",
        (
            f"Frontmatter compliance: {'PASS' if not missing_frontmatter and not invalid_frontmatter else 'FAIL'} "
            f"(checked {len(md_paths)} markdown files)."
        ),
    ]

    findings = []
    recommendations = []
    actions = []
    if off_map_numbered_roots:
        findings.append(
            "Changed files under numbered roots not declared in FOLDER_MAP: "
            + ", ".join(off_map_numbered_roots)
        )
        recommendations.append("Register new numbered roots in FOLDER_MAP or relocate the files.")
        actions.append("Resolve off-map numbered-root placement before relying on governed automation.")
    if missing_frontmatter:
        findings.append(f"Missing YAML frontmatter in {len(missing_frontmatter)} file(s): {', '.join(missing_frontmatter)}")
        recommendations.append("Add required YAML frontmatter to missing files.")
        actions.append("Add frontmatter to flagged files and re-run compliance review.")
    if invalid_frontmatter:
        findings.append(
            f"Frontmatter missing required fields in {len(invalid_frontmatter)} file(s): "
            + "; ".join(invalid_frontmatter)
        )
        recommendations.append("Populate the standard frontmatter contract fields in governed markdown files.")
        actions.append("Repair incomplete frontmatter fields in flagged files.")

    evidence = [
        "00_SYSTEM/architecture/FOLDER_MAP.md:1",
        "00_SYSTEM/schemas/SCHEMAS.md:1",
    ]
    if governed:
        evidence.append("Working tree diff (git status).")

    assumptions = [
        "Doctrine alignment not evaluated in this minimal run.",
        "Scope limited to working tree changes.",
    ]

    body = render_report(
        "System Governance Compliance Report",
        summary,
        findings,
        recommendations,
        actions,
        [],
        evidence,
        assumptions,
    )
    return body, missing_frontmatter


def parse_backlog_rows() -> List[Dict[str, str]]:
    rows = parse_table_by_header(
        BACKLOG_PATH,
        ["ID", "Description", "Owner", "Dependencies", "Priority", "Status"],
    )
    normalized: List[Dict[str, str]] = []
    for row in rows:
        normalized.append(
            {
                "id": row.get("ID", ""),
                "description": row.get("Description", ""),
                "owner": row.get("Owner", ""),
                "dependencies": row.get("Dependencies", ""),
                "priority": row.get("Priority", ""),
                "status": row.get("Status", ""),
            }
        )
    return normalized


def sma_002_report() -> str:
    rows = parse_backlog_rows()
    status_counts: Dict[str, int] = {}
    missing_fields: List[str] = []
    ids = [row.get("id", "") for row in rows if row.get("id")]
    duplicate_ids = sorted({item for item in ids if ids.count(item) > 1})
    id_set = set(ids)
    missing_dependency_refs: Dict[str, List[str]] = {}
    for row in rows:
        status_counts[row["status"]] = status_counts.get(row["status"], 0) + 1
        for key in ("id", "description", "owner", "priority", "status"):
            if not row.get(key):
                missing_fields.append(row.get("id") or "(missing-id)")
        refs = [ref for ref in extract_backlog_dependency_ids(row.get("dependencies", "")) if ref not in id_set]
        if refs:
            missing_dependency_refs[row.get("id") or "(missing-id)"] = refs

    stage_summaries: List[str] = []
    stage_structure_gaps: List[str] = []
    for stage_dir in active_stage_dirs():
        flags = stage_artifact_flags(stage_dir)
        stage_summaries.append(
            f"{stage_dir.name}(kickoff={'Y' if flags['kickoff'] else 'N'}, action={'Y' if flags['action_plan'] else 'N'}, readme={'Y' if flags['readme'] else 'N'})"
        )
        if not any(flags.values()):
            stage_structure_gaps.append(stage_dir.name)

    summary = [
        f"Backlog items reviewed: {len(rows)}.",
        "No backlog updates applied in this run.",
    ]
    if status_counts:
        summary.append("Status counts: " + ", ".join(f"{k}={v}" for k, v in sorted(status_counts.items())))
    if stage_summaries:
        summary.append("Active stage artifact coverage: " + ", ".join(stage_summaries))

    findings = []
    recommendations = []
    actions = []
    if missing_fields:
        findings.append(f"Missing required fields in backlog rows: {', '.join(sorted(set(missing_fields)))}")
        recommendations.append("Fill missing backlog fields (description/owner/priority/status).")
        actions.append("Update backlog rows with missing required fields.")
    if duplicate_ids:
        findings.append(f"Duplicate backlog IDs detected: {', '.join(duplicate_ids)}")
        recommendations.append("Assign unique backlog IDs before further backlog expansion.")
        actions.append("Resolve duplicate backlog IDs.")
    if missing_dependency_refs:
        rendered = ", ".join(
            f"{item} -> {', '.join(refs)}" for item, refs in sorted(missing_dependency_refs.items())
        )
        findings.append(f"Backlog dependency references point to undefined IDs: {rendered}")
        recommendations.append("Repair dependency references so all SYS/SMA IDs resolve inside the backlog.")
        actions.append("Update backlog dependency fields with valid item IDs.")
    if stage_structure_gaps:
        findings.append(
            "Active stage directories missing kickoff/action-plan/readme coverage: "
            + ", ".join(stage_structure_gaps)
        )
        recommendations.append("Add at least one stage control artifact (kickoff, action plan, or README) per active stage.")
        actions.append("Backfill stage control artifacts for the flagged stage directories.")

    evidence = [
        "04_INITIATIVES/SYSTEM_PORTFOLIO/BACKLOG.md:1",
        "04_INITIATIVES/SYSTEM_PORTFOLIO/01_ACTIVE_ROADMAPS/:1",
    ]
    assumptions = [
        "No stage DoD review performed (scope not provided).",
        "No backlog prioritization changes applied.",
    ]

    return render_report(
        "Portfolio Planning Report",
        summary,
        findings,
        recommendations,
        actions,
        [],
        evidence,
        assumptions,
    )


def sma_003_report(changed_paths: List[str]) -> str:
    integrations = []
    missing_sources = []
    missing_readmes = []
    invalid_source_counts = []
    if INTEGRATIONS_DIR.exists():
        for child in sorted(INTEGRATIONS_DIR.iterdir(), key=lambda p: p.name):
            if not child.is_dir():
                continue
            sources = list(child.glob("*_sources.yaml")) + list(child.glob("*_sources.yml"))
            integrations.append((child.name, sources))
            if not sources:
                missing_sources.append(child.name)
            elif len(sources) != 1:
                invalid_source_counts.append(f"{child.name}({len(sources)})")
            if not (child / "README.md").exists():
                missing_readmes.append(child.name)

    changed_integrations = [p for p in changed_paths if p.startswith("00_SYSTEM/integrations/")]
    index_rows = parse_table_by_header(
        INTEGRATIONS_DIR / "INTEGRATIONS_INDEX.md",
        ["Integration ID", "Name", "Status", "Owner", "Contract Path", "Evidence (paths)", "Consumers (paths)", "Notes / Gaps"],
    )
    row_by_id = {row.get("Integration ID", ""): row for row in index_rows if row.get("Integration ID")}
    integration_ids = {name for name, _ in integrations}
    missing_index_rows = sorted(integration_ids - set(row_by_id))
    orphan_index_rows = sorted(set(row_by_id) - integration_ids)
    missing_contract_paths = []
    broken_index_paths = []
    for integration_id, row in row_by_id.items():
        contract_path = row.get("Contract Path", "").strip().strip("`")
        if not contract_path:
            missing_contract_paths.append(integration_id)
        else:
            resolved = resolve_repo_path(contract_path)
            if resolved is None or not resolved.exists():
                broken_index_paths.append(f"{integration_id} contract -> {contract_path}")
        for label in ("Evidence (paths)", "Consumers (paths)"):
            for path_text in split_html_break_paths(row.get(label, "")):
                resolved = resolve_repo_path(path_text)
                if resolved is None or resolved.exists():
                    continue
                broken_index_paths.append(f"{integration_id} {label.lower()} -> {path_text}")

    summary = [
        f"Integrations reviewed: {len(integrations)}.",
        f"Integration files changed in working tree: {len(changed_integrations)}.",
        f"Integration index rows reviewed: {len(index_rows)}.",
    ]
    if integrations:
        summary.append(
            "Sources files present: "
            + ", ".join(f"{name}({len(sources)})" for name, sources in integrations)
        )

    findings = []
    recommendations = []
    actions = []
    if missing_sources:
        findings.append(f"Missing *_sources.yaml in integration folders: {', '.join(missing_sources)}")
        recommendations.append("Add *_sources.yaml for each integration folder missing a source spec.")
        actions.append("Create missing integration source specs.")
    if invalid_source_counts:
        findings.append(f"Integration folders with unexpected source-spec count: {', '.join(invalid_source_counts)}")
        recommendations.append("Keep exactly one canonical *_sources.yaml file per integration folder.")
        actions.append("Resolve duplicate or ambiguous integration source-spec files.")
    if missing_readmes:
        findings.append(f"Integration folders missing README.md: {', '.join(missing_readmes)}")
        recommendations.append("Add README.md documentation for each integration folder.")
        actions.append("Create missing integration READMEs.")
    if missing_index_rows:
        findings.append(f"Integration folders missing index rows: {', '.join(missing_index_rows)}")
        recommendations.append("Add each integration folder to INTEGRATIONS_INDEX.md.")
        actions.append("Update the integrations index for missing folders.")
    if orphan_index_rows:
        findings.append(f"Integration index rows without matching folders: {', '.join(orphan_index_rows)}")
        recommendations.append("Remove or reconcile index rows that no longer map to real integration folders.")
        actions.append("Reconcile orphaned integration index rows.")
    if missing_contract_paths:
        findings.append(f"Integration index rows missing contract paths: {', '.join(missing_contract_paths)}")
        recommendations.append("Populate the Contract Path column for each integration row.")
        actions.append("Add missing contract paths to the integrations index.")
    if broken_index_paths:
        findings.append(
            f"Broken integration index references detected ({len(broken_index_paths)}): "
            + "; ".join(sorted(set(broken_index_paths)))
        )
        recommendations.append("Repair broken contract, evidence, or consumer path references in INTEGRATIONS_INDEX.md.")
        actions.append("Update invalid integration index paths and rerun steward review.")

    evidence = ["00_SYSTEM/integrations/:1", "00_SYSTEM/integrations/INTEGRATIONS_INDEX.md:1"]
    assumptions = [
        "No external integration validation performed.",
        "Scope limited to repo inventory.",
    ]

    return render_report(
        "Integration Steward Review",
        summary,
        findings,
        recommendations,
        actions,
        [],
        evidence,
        assumptions,
    )


def sma_004_report() -> str:
    typology_content = AGENT_TYPOLOGY_PATH.read_text(encoding="utf-8") if AGENT_TYPOLOGY_PATH.exists() else ""
    required_entries = [
        "00_SYSTEM/AGENTS/SMA-001_SYSTEM_GOVERNANCE.md",
        "00_SYSTEM/AGENTS/SMA-002_PORTFOLIO_PLANNING.md",
        "00_SYSTEM/AGENTS/SMA-003_INTEGRATION_STEWARD.md",
        "00_SYSTEM/AGENTS/SMA-004_KNOWLEDGE_CURATION.md",
        "00_SYSTEM/AGENTS/SMA-005_RUNBOOK_QA.md",
        "00_SYSTEM/AGENTS/SMA-006_SYSTEM_LIBRARIAN.md",
        "00_SYSTEM/AGENTS/SMA-007_SYSTEM_CAPABILITY_AUDITOR.md",
    ]
    missing_entries = [entry for entry in required_entries if entry not in typology_content]
    invalid_status_entries = []
    missing_entry_paths = []
    for row in typology_entries():
        status = row.get("Status", "").strip()
        path_text = row.get("Path", "").strip().strip("`")
        agent_name = row.get("Agent", "(unnamed agent)")
        if status and status not in AGENT_LIFECYCLE_STATES:
            invalid_status_entries.append(f"{agent_name} -> {status}")
        if path_text.endswith(".md"):
            resolved = resolve_repo_path(path_text)
            if resolved is None or not resolved.exists():
                missing_entry_paths.append(f"{agent_name} -> {path_text}")

    stub_files = []
    for path in list((REPO_ROOT / "00_SYSTEM" / "AGENTS").glob("*.md")) + list(
        (REPO_ROOT / "00_SYSTEM" / "AGENTS" / "specs").glob("*.md")
    ):
        try:
            content = path.read_text(encoding="utf-8")
        except Exception:
            continue
        if "status: stub" in content:
            stub_files.append(path.relative_to(REPO_ROOT).as_posix())

    inbox_items = inbox_artifacts()
    stale_inbox_items = [f"{path} ({age}d)" for path, age in inbox_items if age > 7]
    archive_candidates = [f"{path} ({age}d)" for path, age in inbox_items if age > 30]

    summary = [
        "Agent index sanity check completed.",
        f"SMA entries present in typology: {len(required_entries) - len(missing_entries)}/{len(required_entries)}.",
        f"Stub specs detected: {len(stub_files)}.",
        f"INBOX artifacts reviewed: {len(inbox_items)}.",
        f"INBOX artifacts overdue for triage/history review (>7d): {len(stale_inbox_items)}.",
    ]

    findings = []
    recommendations = []
    actions = []
    if missing_entries:
        findings.append(f"Missing SMA entries in Agent Typology: {', '.join(missing_entries)}")
        recommendations.append("Add missing SMA paths to the Agent Typology index.")
        actions.append("Update Agent Typology to include missing SMA entries.")
    if invalid_status_entries:
        findings.append(
            f"Agent Typology rows use invalid lifecycle status values ({len(invalid_status_entries)}): "
            + "; ".join(invalid_status_entries)
        )
        recommendations.append("Normalize Agent Typology statuses to Draft/Planned/Active/Deprecated/Archived.")
        actions.append("Correct non-canonical status values in Agent Typology.")
    if missing_entry_paths:
        findings.append(
            f"Agent Typology paths do not resolve to real files ({len(missing_entry_paths)}): "
            + "; ".join(missing_entry_paths)
        )
        recommendations.append("Repair or remove broken path references in Agent Typology.")
        actions.append("Fix missing Agent Typology path references.")
    if stale_inbox_items:
        findings.append(
            f"INBOX artifacts older than 7 days require triage/history review ({len(stale_inbox_items)}): "
            + "; ".join(stale_inbox_items[:8])
        )
        recommendations.append("Review aged INBOX artifacts for promotion, archival, or history placement.")
        actions.append("Triage aged INBOX artifacts and move resolved items out of active INBOX holding areas.")
    if archive_candidates:
        recommendations.append(
            "Consider moving long-stale INBOX artifacts (>30d) into an explicit history/archive state after review."
        )

    evidence = ["00_SYSTEM/AGENTS/specs/AGENT_TYPOLOGY.md:1", "09_INBOX/:1"]
    assumptions = [
        "Stub files are informational only unless ML1 requests removal.",
    ]

    return render_report(
        "Knowledge Curation Report",
        summary,
        findings,
        recommendations,
        actions,
        [],
        evidence,
        assumptions,
    )


def sma_005_report(target_reports: List[Path]) -> str:
    missing_sections: Dict[str, List[str]] = {}
    empty_sections: Dict[str, List[str]] = {}
    missing_frontmatter_map: Dict[str, List[str]] = {}
    broken_evidence: Dict[str, List[str]] = {}
    placeholders: Dict[str, List[str]] = {}
    required_non_empty_sections = {
        "## Summary",
        "## Evidence",
        "## Assumptions / Confidence",
    }
    for report in target_reports:
        content = report.read_text(encoding="utf-8")
        fields = parse_frontmatter_fields(report)
        if not fields:
            missing_frontmatter_map[report.name] = REQUIRED_FRONTMATTER_FIELDS[:]
        else:
            missing_fields = missing_frontmatter_fields(fields)
            if missing_fields:
                missing_frontmatter_map[report.name] = missing_fields
        missing = [section for section in REQUIRED_SECTIONS if section not in content]
        if missing:
            missing_sections[report.name] = missing
        for section in REQUIRED_SECTIONS:
            section_lines = extract_section_lines(content, section)
            if section_lines is None:
                continue
            if section not in required_non_empty_sections:
                continue
            meaningful = [
                line.strip()
                for line in section_lines
                if line.strip()
                and line.strip() not in {"1. None.", "- None.", "- [ ] None."}
            ]
            if not meaningful:
                empty_sections.setdefault(report.name, []).append(section)
        if re.search(r"\b(?:TODO|TBD)\b", content):
            matches = sorted(set(re.findall(r"\b(?:TODO|TBD)\b", content)))
            placeholders[report.name] = matches
        evidence_lines = extract_section_lines(content, "## Evidence") or []
        for line in evidence_lines:
            if not line.strip().startswith("- "):
                continue
            resolved = resolve_repo_path(line.strip()[2:])
            if resolved is None:
                continue
            if not resolved.exists():
                broken_evidence.setdefault(report.name, []).append(line.strip()[2:])

    summary = [
        f"QA validation run against {len(target_reports)} report(s).",
        f"Reports missing required sections: {len(missing_sections)}.",
        f"Reports with incomplete frontmatter: {len(missing_frontmatter_map)}.",
        f"Reports with empty standard sections: {len(empty_sections)}.",
        f"Reports with broken evidence references: {len(broken_evidence)}.",
    ]

    findings = []
    recommendations = []
    actions = []
    if missing_frontmatter_map:
        for report, fields in missing_frontmatter_map.items():
            findings.append(f"{report} missing frontmatter fields: {', '.join(fields)}")
        recommendations.append("Ensure every report includes the standard frontmatter contract.")
        actions.append("Repair report frontmatter before relying on QA outputs.")
    if missing_sections:
        for report, sections in missing_sections.items():
            findings.append(f"{report} missing sections: {', '.join(sections)}")
        recommendations.append("Ensure all reports include the standard output format sections.")
        actions.append("Amend reports to include missing sections and re-run QA.")
    if empty_sections:
        for report, sections in empty_sections.items():
            findings.append(f"{report} contains empty standard sections: {', '.join(sections)}")
        recommendations.append("Populate empty standard sections with concrete observations or explicit rationale.")
        actions.append("Fill empty report sections and re-run QA validation.")
    if broken_evidence:
        for report, refs in broken_evidence.items():
            findings.append(f"{report} has broken evidence references: {', '.join(refs)}")
        recommendations.append("Repair or remove broken evidence paths in reports.")
        actions.append("Update report evidence references and rerun QA.")
    if placeholders:
        for report, tokens in placeholders.items():
            findings.append(f"{report} still contains placeholders: {', '.join(tokens)}")
        recommendations.append("Resolve TODO/TBD placeholders in reports before treating them as complete.")
        actions.append("Replace outstanding report placeholders with final content.")

    evidence = [f"{report.relative_to(REPO_ROOT).as_posix()}:1" for report in target_reports]
    assumptions = [
        "QA checks are deterministic and repo-local; they do not validate substantive correctness of recommendations.",
    ]

    return render_report(
        "Runbook & QA Validation Report",
        summary,
        findings,
        recommendations,
        actions,
        [],
        evidence,
        assumptions,
    )


def sma_006_report(changed_paths: List[str]) -> str:
    all_markdown = governed_markdown_files()
    id_to_paths: Dict[str, List[str]] = {}
    missing_ids: List[str] = []
    missing_metadata: List[str] = []
    non_ascii_names: List[str] = []
    broken_links: List[str] = []

    for path in all_markdown:
        rel = path.relative_to(REPO_ROOT).as_posix()
        if any(ord(ch) > 127 for ch in rel):
            non_ascii_names.append(rel)
        fields = parse_frontmatter_fields(path)
        if fields is None:
            continue
        artifact_id = fields.get("id", "").strip()
        if artifact_id:
            id_to_paths.setdefault(artifact_id, []).append(rel)
        else:
            missing_ids.append(rel)

    changed_markdown = [
        REPO_ROOT / p
        for p in changed_paths
        if p.lower().endswith(".md") and top_level_root(p) in governed_roots() and (REPO_ROOT / p).exists()
        and top_level_root(p) != "06_RUNS"
    ]
    for path in changed_markdown:
        rel = path.relative_to(REPO_ROOT).as_posix()
        fields = parse_frontmatter_fields(path)
        if fields is None:
            missing_metadata.append(f"{rel} -> missing frontmatter")
            continue
        missing = missing_frontmatter_fields(fields)
        if missing:
            missing_metadata.append(f"{rel} -> missing fields: {', '.join(missing)}")
        try:
            content = path.read_text(encoding="utf-8")
        except Exception:
            continue
        for target in markdown_links(content):
            if not relative_link_exists(path, target):
                broken_links.append(f"{rel} -> {target}")

    duplicate_ids = {
        artifact_id: paths
        for artifact_id, paths in id_to_paths.items()
        if len(paths) > 1
    }
    typology_content = AGENT_TYPOLOGY_PATH.read_text(encoding="utf-8") if AGENT_TYPOLOGY_PATH.exists() else ""
    unregistered_sma_specs = []
    for spec in sorted(AGENTS_DIR.glob("SMA-*.md")):
        rel = spec.relative_to(REPO_ROOT).as_posix()
        if rel not in typology_content:
            unregistered_sma_specs.append(rel)

    summary = [
        f"Governed markdown files inventoried: {len(all_markdown)}.",
        f"Changed governed markdown files checked for registration hygiene: {len(changed_markdown)}.",
        f"Unique frontmatter IDs inventoried: {len(id_to_paths)}.",
        f"Duplicate frontmatter IDs detected: {len(duplicate_ids)}.",
        f"Non-ASCII governed filenames detected: {len(non_ascii_names)}.",
    ]

    findings = []
    recommendations = []
    actions = []
    if duplicate_ids:
        rendered = "; ".join(
            f"{artifact_id} -> {', '.join(paths[:3])}" for artifact_id, paths in sorted(duplicate_ids.items())[:10]
        )
        findings.append(f"Duplicate frontmatter IDs require librarian resolution ({len(duplicate_ids)}): {rendered}")
        recommendations.append("Assign stable unique IDs to duplicated artifacts before depending on automated indexing.")
        actions.append("Resolve duplicate frontmatter IDs and re-run the librarian pass.")
    if missing_ids:
        findings.append(f"Governed markdown with frontmatter but no id field: {len(missing_ids)} file(s).")
        recommendations.append("Populate missing artifact IDs in governed markdown frontmatter.")
        actions.append("Backfill id fields for governed markdown files missing IDs.")
    if missing_metadata:
        findings.append(
            f"Changed governed markdown with incomplete metadata ({len(missing_metadata)}): "
            + "; ".join(missing_metadata[:10])
        )
        recommendations.append("Repair metadata on changed governed artifacts before registration.")
        actions.append("Add required frontmatter fields to changed governed artifacts.")
    if non_ascii_names:
        findings.append(
            f"Non-ASCII governed filenames detected ({len(non_ascii_names)}): "
            + "; ".join(non_ascii_names[:10])
        )
        recommendations.append("Rename governed files to ASCII filenames unless a specific exception is approved.")
        actions.append("Normalize non-ASCII governed filenames.")
    if broken_links:
        findings.append(
            f"Broken relative links in changed governed markdown ({len(broken_links)}): "
            + "; ".join(broken_links[:10])
        )
        recommendations.append("Repair broken local links before promoting changed artifacts.")
        actions.append("Fix broken relative links in changed governed artifacts.")
    if unregistered_sma_specs:
        findings.append(f"SMA specs missing from Agent Typology: {', '.join(unregistered_sma_specs)}")
        recommendations.append("Register every SMA spec in the Agent Typology index.")
        actions.append("Update Agent Typology with missing SMA specs.")

    evidence = [
        "00_SYSTEM/architecture/FOLDER_MAP.md:1",
        "00_SYSTEM/AGENTS/specs/AGENT_TYPOLOGY.md:1",
    ]
    assumptions = [
        "SMA-006 performed validation only; it did not relocate artifacts or infer artifact ownership.",
        "Broken-link checks are scoped to changed governed markdown files.",
    ]

    return render_report(
        "System Librarian Report",
        summary,
        findings,
        recommendations,
        actions,
        [],
        evidence,
        assumptions,
    )


def sma_007_report() -> str:
    findings = []
    recommendations = []
    actions = []
    evidence = [
        ".mcp.json:1",
        ".claude/:1",
        "00_SYSTEM/orchestration/run_graphs/:1",
        "scripts/:1",
    ]

    mcp_servers: Dict[str, Dict[str, object]] = {}
    missing_mcp_commands: List[str] = []
    missing_integration_specs: List[str] = []
    if MCP_CONFIG_PATH.exists():
        try:
            mcp_config = json.loads(MCP_CONFIG_PATH.read_text(encoding="utf-8"))
            raw_servers = mcp_config.get("mcpServers", {})
            if isinstance(raw_servers, dict):
                mcp_servers = {
                    name: config
                    for name, config in raw_servers.items()
                    if isinstance(config, dict)
                }
        except json.JSONDecodeError:
            findings.append(".mcp.json is not valid JSON.")
            recommendations.append("Repair MCP configuration JSON before relying on connector automation.")
            actions.append("Fix .mcp.json syntax and rerun capability audit.")
    else:
        findings.append("No .mcp.json file found for MCP server registration.")
        recommendations.append("Create an MCP registry if MCP-backed capability is expected.")
        actions.append("Add or document the MCP registry location.")

    for server_name, config in sorted(mcp_servers.items()):
        args = config.get("args", [])
        if isinstance(args, list):
            for arg in args:
                if isinstance(arg, str) and arg.endswith(".py"):
                    if not (REPO_ROOT / arg).exists():
                        missing_mcp_commands.append(f"{server_name} -> {arg}")
        integration_dir = INTEGRATIONS_DIR / server_name
        if integration_dir.exists() and not list(integration_dir.glob("*_sources.y*ml")):
            missing_integration_specs.append(server_name)

    claude_agent_count = len(list((CLAUDE_DIR / "agents").glob("*.md"))) if (CLAUDE_DIR / "agents").exists() else 0
    claude_command_count = len(list((CLAUDE_DIR / "commands").glob("*.md"))) if (CLAUDE_DIR / "commands").exists() else 0
    missing_capability_dirs = []
    for required in ("agents", "commands", "hooks"):
        if not (CLAUDE_DIR / required).exists():
            missing_capability_dirs.append(f".claude/{required}")
    missing_capability_files = []
    for required in (CLAUDE_DIR / "settings.json", AGENT_TYPOLOGY_PATH, RUN_GRAPHS_DIR / "weekly_sma_sweep.yaml"):
        if not required.exists():
            missing_capability_files.append(required.relative_to(REPO_ROOT).as_posix())

    run_graph_count = len(list(RUN_GRAPHS_DIR.glob("*.yaml"))) if RUN_GRAPHS_DIR.exists() else 0
    management_runner = REPO_ROOT / "00_SYSTEM" / "scripts" / "run_system_management_sweep.py"
    admin_runner = REPO_ROOT / "00_SYSTEM" / "scripts" / "run_system_admin_sweep.py"
    missing_runners = [
        path.relative_to(REPO_ROOT).as_posix()
        for path in (management_runner, admin_runner)
        if not path.exists()
    ]

    if missing_mcp_commands:
        findings.append(f"MCP server command targets are missing: {', '.join(missing_mcp_commands)}")
        recommendations.append("Repair MCP server command paths or remove stale server registrations.")
        actions.append("Reconcile missing MCP command targets.")
    if missing_integration_specs:
        findings.append(f"MCP-backed integrations missing source specs: {', '.join(missing_integration_specs)}")
        recommendations.append("Add source contracts for MCP-backed integrations.")
        actions.append("Create missing MCP integration source specs.")
    if missing_capability_dirs:
        findings.append(f"Capability directories missing: {', '.join(missing_capability_dirs)}")
        recommendations.append("Restore expected .claude capability directories or document replacement locations.")
        actions.append("Create missing capability directories or update the audit contract.")
    if missing_capability_files:
        findings.append(f"Capability control files missing: {', '.join(missing_capability_files)}")
        recommendations.append("Restore required capability control files.")
        actions.append("Create missing capability control files.")
    if missing_runners:
        findings.append(f"System sweep runners missing: {', '.join(missing_runners)}")
        recommendations.append("Restore missing deterministic sweep runners.")
        actions.append("Create or recover missing sweep runner scripts.")

    summary = [
        f"MCP servers registered: {len(mcp_servers)} ({', '.join(sorted(mcp_servers)) if mcp_servers else 'none'}).",
        f"Claude-style local agent specs: {claude_agent_count}.",
        f"Claude-style local commands: {claude_command_count}.",
        f"Run graphs available: {run_graph_count}.",
        "Capability audit scope: repo-local configuration, scripts, run graphs, and agent inventory.",
    ]

    assumptions = [
        "SMA-007 did not test external services or network connectivity.",
        "Connector quality is evaluated from repo-local declarations only.",
    ]

    return render_report(
        "System Capability Audit Report",
        summary,
        findings,
        recommendations,
        actions,
        [],
        evidence,
        assumptions,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Run minimal System Management sweep.")
    parser.add_argument("--run-id", help="Override run ID (default: auto)")
    args = parser.parse_args()

    run_id = args.run_id or generate_run_id()
    run_root = REPO_ROOT / "06_RUNS" / run_id / "system_management"
    run_root.mkdir(parents=True, exist_ok=True)

    roots = governed_roots()
    changed_paths = git_changed_paths()

    sma_001_body, _ = sma_001_report(changed_paths, roots)
    sma_002_body = sma_002_report()
    sma_003_body = sma_003_report(changed_paths)
    sma_004_body = sma_004_report()
    sma_006_body = sma_006_report(changed_paths)
    sma_007_body = sma_007_report()

    report_map = {
        "SMA-001_SYSTEM_GOVERNANCE_REPORT.md": ("System Governance Report", sma_001_body),
        "SMA-002_PORTFOLIO_PLANNING_REPORT.md": ("Portfolio Planning Report", sma_002_body),
        "SMA-003_INTEGRATION_STEWARD_REPORT.md": ("Integration Steward Report", sma_003_body),
        "SMA-004_KNOWLEDGE_CURATION_REPORT.md": ("Knowledge Curation Report", sma_004_body),
        "SMA-006_SYSTEM_LIBRARIAN_REPORT.md": ("System Librarian Report", sma_006_body),
        "SMA-007_SYSTEM_CAPABILITY_AUDITOR_REPORT.md": ("System Capability Auditor Report", sma_007_body),
    }

    for filename, (title, body) in report_map.items():
        write_report(run_root / filename, title, body)

    qa_body = sma_005_report([run_root / name for name in report_map.keys()])
    write_report(run_root / "SMA-005_RUNBOOK_QA_REPORT.md", "Runbook & QA Report", qa_body)

    run_log = "\n".join(
        [
            "# RUN LOG — System Management Sweep",
            "",
            f"Run ID: {run_id}",
            f"Start: {utc_now()}",
            "",
            "Outputs:",
            f"- {run_root / 'SMA-001_SYSTEM_GOVERNANCE_REPORT.md'}",
            f"- {run_root / 'SMA-002_PORTFOLIO_PLANNING_REPORT.md'}",
            f"- {run_root / 'SMA-003_INTEGRATION_STEWARD_REPORT.md'}",
            f"- {run_root / 'SMA-004_KNOWLEDGE_CURATION_REPORT.md'}",
            f"- {run_root / 'SMA-005_RUNBOOK_QA_REPORT.md'}",
            f"- {run_root / 'SMA-006_SYSTEM_LIBRARIAN_REPORT.md'}",
            f"- {run_root / 'SMA-007_SYSTEM_CAPABILITY_AUDITOR_REPORT.md'}",
            "",
        ]
    )
    (run_root / "RUN_LOG.md").write_text(run_log, encoding="utf-8")

    print(f"System management sweep complete: {run_root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
