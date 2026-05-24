#!/usr/bin/env python3
"""
System Admin Sweep runner.

Writes required artifacts to:
  06_RUNS/${run_id}/system_admin/

Scope:
- Builds an inventory of governed artifacts.
- Runs deterministic checks for each System Admin Agent (SAA).
- Produces canonical findings and per-agent appendices.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple
from urllib.parse import unquote


REPO_ROOT = Path(__file__).resolve().parents[2]
FOLDER_MAP_PATH = REPO_ROOT / "00_SYSTEM" / "architecture" / "FOLDER_MAP.md"
SCHEMAS_PATH = REPO_ROOT / "00_SYSTEM" / "schemas" / "SCHEMAS.md"
PLAYBOOK_INDEX_PATH = REPO_ROOT / "02_PLAYBOOKS" / "_REGISTRY" / "PLAYBOOK_INDEX.md"

SAA_AGENTS = [
    "SAA_REPO_LINTER",
    "SAA_FOLDER_MAP_DRIFT",
    "SAA_METADATA_ENFORCER",
    "SAA_REFERENCE_INTEGRITY",
    "SAA_REGISTRY_SYNC",
]

SEVERITY_ORDER = {"BLOCKER": 0, "MAJOR": 1, "MINOR": 2, "INFO": 3}

EXCLUDE_DIR_NAMES = {
    ".git",
    ".github",
    ".idea",
    ".vscode",
    "__pycache__",
    "node_modules",
    ".venv",
    "venv",
    "dist",
    "build",
}

INVENTORY_ROOTS_WITHOUT_RUNS = [
    "00_SYSTEM",
    "01_DOCTRINE",
    "02_PLAYBOOKS",
    "03_TEMPLATES",
    "04_INITIATIVES",
    "05_MATTERS",
    "07_REFERENCE",
    "08_RESEARCH",
    "09_INBOX",
    "10_ARCHIVE",
]

METADATA_SCOPE_ROOTS = {"00_SYSTEM", "01_DOCTRINE", "02_PLAYBOOKS", "04_INITIATIVES"}
REFERENCE_SCOPE_ROOTS = {
    "00_SYSTEM",
    "01_DOCTRINE",
    "02_PLAYBOOKS",
    "03_TEMPLATES",
    "04_INITIATIVES",
    "07_REFERENCE",
    "08_RESEARCH",
    "09_INBOX",
    "10_ARCHIVE",
}

REQUIRED_FRONTMATTER_KEYS = [
    "id",
    "title",
    "owner",
    "status",
    "created_date",
    "last_updated",
]

CORE_STATUS_VALUES = {
    "draft",
    "proposed",
    "approved",
    "deprecated",
    "active",
    "superseded",
}
INITIATIVE_STATUS_VALUES = CORE_STATUS_VALUES | {
    "on track",
    "at risk",
    "blocked",
    "complete",
    "closed",
    "parked",
    "executing",
    "open",
    "ready",
    "backlog",
    "shortlisted",
    "working",
    "working-draft",
    "working-notes",
    "audience-draft",
    "locked",
    "advisory",
    "implemented",
    "planned",
    "planning",
    "initiating",
    "in_progress",
    "stable",
}
AGENT_STATUS_VALUES = CORE_STATUS_VALUES | {"planned", "stub"}

PLAYBOOK_TOP_LEVEL_DIRS = {
    "LL_OPERATIONS",
    "CONTRACTS",
    "CORPORATE",
    "FINANCIAL_SERVICES",
    "TRADE_REMEDIES_MARKET_ACCESS",
    "_ASSETS",
    "_REGISTRY",
}
PLAYBOOK_TOP_LEVEL_FILES = {"README.md"}
PLAYBOOK_REQUIRED_COMPANION_FILES = {"README.md", "metadata.yaml", "steps.yaml", "acceptance.md"}
ASSET_EXTENSIONS = {
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".svg",
    ".webp",
    ".pdf",
    ".csv",
    ".json",
    ".yaml",
    ".yml",
    ".docx",
    ".xlsx",
    ".pptx",
}

MARKDOWN_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


@dataclass
class MarkdownRecord:
    path: Path
    rel_path: str
    text: str
    body: str
    has_frontmatter: bool
    frontmatter: Dict[str, str]


@dataclass
class YamlRecord:
    path: Path
    rel_path: str
    data: Dict[str, str]


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def slugify(text: str) -> str:
    cleaned = re.sub(r"[^a-zA-Z0-9]+", "-", text.strip().lower()).strip("-")
    return cleaned or "finding"


def generate_run_id() -> str:
    stamp = datetime.now(timezone.utc).strftime("%H%M%SZ")
    date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    return f"RUN-{date}-SYSTEM-ADMIN-SWEEP-{stamp}"


def normalize_scalar(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def parse_simple_mapping(lines: Sequence[str]) -> Dict[str, str]:
    data: Dict[str, str] = {}
    for raw in lines:
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if raw[:1].isspace():
            continue
        if ":" not in raw:
            continue
        key, value = raw.split(":", 1)
        data[key.strip()] = normalize_scalar(value.strip())
    return data


def parse_markdown_frontmatter(text: str) -> Tuple[bool, Dict[str, str], str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return False, {}, text
    end_index = None
    for idx in range(1, len(lines)):
        if lines[idx].strip() == "---":
            end_index = idx
            break
    if end_index is None:
        return False, {}, text
    frontmatter = parse_simple_mapping(lines[1:end_index])
    body = "\n".join(lines[end_index + 1 :])
    if text.endswith("\n"):
        body += "\n"
    return True, frontmatter, body


def parse_yaml_file(path: Path) -> Dict[str, str]:
    return parse_simple_mapping(path.read_text(encoding="utf-8", errors="ignore").splitlines())


def load_folder_map_roots() -> List[str]:
    if not FOLDER_MAP_PATH.exists():
        return []
    roots: List[str] = []
    numbered_pattern = re.compile(r"^-\s+([0-9]{2}_[A-Z0-9_]+)\b")
    section: str | None = None
    for line in FOLDER_MAP_PATH.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped.startswith("## "):
            header = stripped[3:].strip().lower()
            if header.startswith("ml2 governed roots"):
                section = "numbered"
            elif header.startswith("non-ml2 root folders"):
                section = "non_numbered"
            else:
                section = None
            continue
        if not line.startswith("- "):
            continue
        if section == "numbered":
            match = numbered_pattern.match(stripped)
            if match:
                roots.append(match.group(1))
        elif section == "non_numbered":
            name = stripped[2:]
            name = name.split("—", 1)[0].strip()
            if name and not name.startswith("."):
                roots.append(name)
    return roots


def governed_roots() -> List[str]:
    roots = load_folder_map_roots()
    if roots:
        return roots
    return [d.name for d in REPO_ROOT.iterdir() if d.is_dir() and re.match(r"^[0-9]{2}_", d.name)]


def is_excluded_dir(path: Path) -> bool:
    return any(part in EXCLUDE_DIR_NAMES for part in path.parts) or "scripts" in path.parts


def type_guess(path: Path) -> str:
    ext = path.suffix.lower()
    if ext == ".md":
        return "markdown"
    if ext == ".json":
        return "json"
    if ext in {".yaml", ".yml"}:
        return "yaml"
    if ext == ".txt":
        return "text"
    if ext == ".csv":
        return "csv"
    if ext == ".pdf":
        return "pdf"
    return "file"


def category_guess(rel_path: Path) -> str:
    if not rel_path.parts:
        return "other"
    top = rel_path.parts[0]
    mapping = {
        "00_SYSTEM": "system",
        "01_DOCTRINE": "doctrine",
        "02_PLAYBOOKS": "playbook",
        "03_TEMPLATES": "template",
        "04_INITIATIVES": "initiative",
        "05_MATTERS": "matter",
        "06_RUNS": "runs",
        "07_REFERENCE": "reference",
        "08_RESEARCH": "research",
        "09_INBOX": "inbox",
        "10_ARCHIVE": "archive",
    }
    return mapping.get(top, "other")


def build_inventory(roots: Iterable[str]) -> List[Dict]:
    inventory: List[Dict] = []
    for root in roots:
        root_path = REPO_ROOT / root
        if not root_path.exists() or not root_path.is_dir():
            continue
        for path in root_path.rglob("*"):
            if path.is_dir():
                continue
            if is_excluded_dir(path):
                continue
            rel = path.relative_to(REPO_ROOT)
            stat = path.stat()
            inventory.append(
                {
                    "path": rel.as_posix(),
                    "type_guess": type_guess(path),
                    "category_guess": category_guess(rel),
                    "exists": True,
                    "size_bytes": stat.st_size,
                    "last_modified": datetime.fromtimestamp(
                        stat.st_mtime, timezone.utc
                    ).isoformat(timespec="seconds"),
                }
            )
    inventory.sort(key=lambda item: item["path"])
    return inventory


def scan_markdown_records(root_names: Sequence[str]) -> List[MarkdownRecord]:
    records: List[MarkdownRecord] = []
    for root in root_names:
        root_path = REPO_ROOT / root
        if not root_path.exists() or not root_path.is_dir():
            continue
        for path in root_path.rglob("*.md"):
            if is_excluded_dir(path):
                continue
            text = path.read_text(encoding="utf-8", errors="ignore")
            has_frontmatter, frontmatter, body = parse_markdown_frontmatter(text)
            records.append(
                MarkdownRecord(
                    path=path,
                    rel_path=path.relative_to(REPO_ROOT).as_posix(),
                    text=text,
                    body=body,
                    has_frontmatter=has_frontmatter,
                    frontmatter=frontmatter,
                )
            )
    records.sort(key=lambda record: record.rel_path)
    return records


def scan_yaml_records(root: Path, filename: str) -> List[YamlRecord]:
    records: List[YamlRecord] = []
    if not root.exists():
        return records
    for path in root.rglob(filename):
        if is_excluded_dir(path):
            continue
        records.append(
            YamlRecord(
                path=path,
                rel_path=path.relative_to(REPO_ROOT).as_posix(),
                data=parse_yaml_file(path),
            )
        )
    records.sort(key=lambda record: record.rel_path)
    return records


def clip_paths(paths: Sequence[str], limit: int = 50) -> Tuple[List[str], int]:
    unique = sorted(dict.fromkeys(paths))
    return unique[:limit], max(0, len(unique) - limit)


def make_finding(
    agent: str,
    severity: str,
    category: str,
    title: str,
    description: str,
    affected_paths: Sequence[str],
    suggested_fix: str = "",
    references: Sequence[Dict[str, str]] | None = None,
    slug_hint: str = "",
) -> Dict:
    listed_paths, omitted = clip_paths(affected_paths)
    if omitted:
        description = f"{description} ({omitted} additional paths omitted from listing.)"
    finding = {
        "id": f"{agent}-{slugify(category)}-{slugify(title + '-' + slug_hint)}",
        "agent": agent,
        "severity": severity,
        "category": category,
        "title": title,
        "description": description,
        "affected_paths": listed_paths,
        "created_at": utc_now(),
    }
    if suggested_fix:
        finding["suggested_fix"] = suggested_fix
    if references:
        finding["references"] = list(references)
    return finding


def load_markdown_lookup(records: Sequence[MarkdownRecord]) -> Dict[str, MarkdownRecord]:
    return {record.rel_path: record for record in records}


def parse_playbook_index() -> Tuple[List[Dict[str, str]], str | None]:
    if not PLAYBOOK_INDEX_PATH.exists():
        return [], "PLAYBOOK_INDEX.md is missing."
    entries: List[Dict[str, str]] = []
    for line in PLAYBOOK_INDEX_PATH.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != 5:
            continue
        if cells[0].lower() == "category" or all(set(cell) <= {"-"} for cell in cells):
            continue
        path_value = cells[4]
        link_match = re.match(r"\[[^\]]+\]\(([^)]+)\)", path_value)
        if link_match:
            path_value = link_match.group(1).strip()
        entries.append(
            {
                "category": cells[0],
                "playbook": cells[1],
                "status": cells[2],
                "owner": cells[3],
                "path": path_value,
            }
        )
    return entries, None


def normalize_status(value: str) -> str:
    normalized = " ".join(value.strip().lower().split())
    for separator in (" — ", " – "):
        if separator in normalized:
            normalized = normalized.split(separator, 1)[0].strip()
    return normalized


def allowed_statuses_for_path(path: Path) -> set[str]:
    rel = path.relative_to(REPO_ROOT)
    if rel.parts and rel.parts[0] == "04_INITIATIVES":
        return INITIATIVE_STATUS_VALUES
    if rel.parts[:2] == ("00_SYSTEM", "AGENTS"):
        return AGENT_STATUS_VALUES
    return CORE_STATUS_VALUES


def value_is_empty(value: str) -> bool:
    return normalize_scalar(value) in {"", "[]", "{}", "null", "None"}


def doctrine_record(record: MarkdownRecord) -> bool:
    return record.path.relative_to(REPO_ROOT).parts[0] == "01_DOCTRINE"


def playbook_metadata_folder_allowed(rel_to_playbooks: Path) -> bool:
    parts = rel_to_playbooks.parts
    if not parts:
        return True
    if parts[0] in {"_ASSETS", "_REGISTRY", "LL_OPERATIONS"}:
        return True
    if len(parts) >= 2 and parts[1] == "WORKFLOWS":
        return True
    if len(parts) >= 2 and parts[:2] == ("FINANCIAL_SERVICES", "SOLUTIONS"):
        return True
    return False


def duplicate_markdown_ids(records: Sequence[MarkdownRecord]) -> Dict[str, List[str]]:
    id_map: Dict[str, List[str]] = defaultdict(list)
    for record in records:
        if not record.has_frontmatter:
            continue
        identifier = record.frontmatter.get("id", "").strip()
        if not identifier:
            continue
        id_map[identifier].append(record.rel_path)
    return {
        identifier: sorted(paths)
        for identifier, paths in id_map.items()
        if len(paths) > 1
    }


def schema_location_targets() -> List[str]:
    if not SCHEMAS_PATH.exists():
        return []
    targets: List[str] = []
    for match in re.finditer(r"Location:\s*`([^`]+)`", SCHEMAS_PATH.read_text(encoding="utf-8")):
        candidate = match.group(1).strip()
        if "{" in candidate or "}" in candidate:
            continue
        targets.append(candidate)
    return targets


def repo_linter_findings(
    inventory: Sequence[Dict],
    markdown_records: Sequence[MarkdownRecord],
    metadata_records: Sequence[YamlRecord],
    registry_entries: Sequence[Dict[str, str]],
) -> List[Dict]:
    findings: List[Dict] = []

    runtime_dirs = [name for name in ("logs", "state") if (REPO_ROOT / name).is_dir()]
    if runtime_dirs:
        findings.append(
            make_finding(
                "SAA_REPO_LINTER",
                "MAJOR",
                "structure",
                "Root runtime directories present at repo root",
                "Runtime directories that should live under 06_RUNS/ or outside the repo are present at the root.",
                [f"{name}/" for name in runtime_dirs],
                "Relocate runtime directories out of the repo root or document an explicit exception.",
            )
        )

    playbooks_root = REPO_ROOT / "02_PLAYBOOKS"
    if playbooks_root.exists():
        top_level_drift: List[str] = []
        for entry in playbooks_root.iterdir():
            if entry.name.startswith("."):
                continue
            if entry.is_dir() and entry.name not in PLAYBOOK_TOP_LEVEL_DIRS:
                top_level_drift.append(entry.name + "/")
            elif entry.is_file() and entry.name not in PLAYBOOK_TOP_LEVEL_FILES:
                top_level_drift.append(entry.name)
        if top_level_drift:
            findings.append(
                make_finding(
                    "SAA_REPO_LINTER",
                    "MINOR",
                    "structure",
                    "Unexpected top-level entries under 02_PLAYBOOKS",
                    "Top-level playbook contents drift from the documented module architecture in 02_PLAYBOOKS/README.md.",
                    top_level_drift,
                    "Move these entries into documented subfolders or update the module architecture if the change is intentional.",
                )
            )

    invalid_metadata_folders: List[str] = []
    missing_companion_files: List[str] = []
    for record in metadata_records:
        rel_to_playbooks = record.path.relative_to(REPO_ROOT / "02_PLAYBOOKS")
        if not playbook_metadata_folder_allowed(rel_to_playbooks.parent):
            invalid_metadata_folders.append(record.rel_path)
        folder = record.path.parent
        missing = [name for name in PLAYBOOK_REQUIRED_COMPANION_FILES if not (folder / name).exists()]
        if missing:
            missing_companion_files.append(f"{folder.relative_to(REPO_ROOT).as_posix()} -> missing {', '.join(sorted(missing))}")

    if invalid_metadata_folders:
        findings.append(
            make_finding(
                "SAA_REPO_LINTER",
                "MAJOR",
                "structure",
                "Playbook metadata folders outside approved placement",
                "Metadata-bearing playbook folders exist outside the approved playbook structure.",
                invalid_metadata_folders,
                "Move these folders under approved playbook branches or retire the metadata if the folder is not a canonical playbook.",
            )
        )

    if missing_companion_files:
        findings.append(
            make_finding(
                "SAA_REPO_LINTER",
                "MAJOR",
                "structure",
                "Playbook folders missing required companion files",
                "Metadata-bearing playbook folders must include README.md, metadata.yaml, steps.yaml, and acceptance.md.",
                missing_companion_files,
                "Add the missing companion files so the playbook folder is structurally complete.",
            )
        )

    duplicates = duplicate_markdown_ids(markdown_records)
    if duplicates:
        affected_paths = [path for paths in duplicates.values() for path in paths]
        sample = ", ".join(
            f"{identifier} ({len(paths)} files)"
            for identifier, paths in list(sorted(duplicates.items()))[:8]
        )
        findings.append(
            make_finding(
                "SAA_REPO_LINTER",
                "MAJOR",
                "naming",
                "Duplicate frontmatter ids across governed markdown",
                f"{len(duplicates)} duplicate id values were found across governed markdown files. Sample groups: {sample}.",
                affected_paths,
                "Make ids globally unique or archive/remove obsolete duplicates.",
            )
        )

    missing_schema_locations = [target for target in schema_location_targets() if not (REPO_ROOT / target).exists()]
    if missing_schema_locations:
        findings.append(
            make_finding(
                "SAA_REPO_LINTER",
                "MAJOR",
                "structure",
                "Schema locations referenced in SCHEMAS.md are missing",
                "One or more schema location references point to files that do not exist.",
                missing_schema_locations,
                "Create the missing schema files or update SCHEMAS.md to match the actual file locations.",
                references=[{"path": SCHEMAS_PATH.relative_to(REPO_ROOT).as_posix(), "anchor": "Artifact Schemas"}],
            )
        )

    non_ascii_paths: List[str] = []
    whitespace_paths: List[str] = []
    for item in inventory:
        if item["type_guess"] not in {"markdown", "yaml", "json", "csv", "text"}:
            continue
        name = Path(item["path"]).name
        if any(ord(char) > 127 for char in name):
            non_ascii_paths.append(item["path"])
        if " " in name:
            whitespace_paths.append(item["path"])

    if non_ascii_paths:
        findings.append(
            make_finding(
                "SAA_REPO_LINTER",
                "MINOR",
                "naming",
                "Non-ASCII filenames detected",
                "Governed artifacts should avoid non-ASCII filenames unless there is an explicit exception.",
                non_ascii_paths,
                "Rename files to ASCII-safe names or document the exception.",
            )
        )

    if whitespace_paths:
        findings.append(
            make_finding(
                "SAA_REPO_LINTER",
                "MINOR",
                "naming",
                "Filenames with spaces detected",
                "Whitespace in filenames increases link fragility and makes repo references less deterministic.",
                whitespace_paths,
                "Rename files to use underscores or hyphens instead of spaces.",
            )
        )

    return findings


def folder_map_drift_findings() -> List[Dict]:
    mapped_roots = set(load_folder_map_roots())
    actual_roots = {
        path.name
        for path in REPO_ROOT.iterdir()
        if path.is_dir() and not path.name.startswith(".") and path.name not in EXCLUDE_DIR_NAMES
    }
    extras = sorted(actual_roots - mapped_roots)
    missing = sorted(mapped_roots - actual_roots)

    findings: List[Dict] = []

    if extras:
        findings.append(
            make_finding(
                "SAA_FOLDER_MAP_DRIFT",
                "MAJOR",
                "drift",
                "Root directories not documented in FOLDER_MAP.md",
                "Root directories exist on disk that are not listed in the folder map.",
                [f"{name}/" for name in extras],
                "Update FOLDER_MAP.md or relocate these directories into documented locations.",
            )
        )

    if missing:
        findings.append(
            make_finding(
                "SAA_FOLDER_MAP_DRIFT",
                "MINOR",
                "drift",
                "Folder map entries missing on disk",
                "FOLDER_MAP.md lists root directories that do not exist in the repo.",
                [f"{name}/" for name in missing],
                "Remove stale entries from FOLDER_MAP.md or recreate the expected directories.",
            )
        )

    return findings


def metadata_enforcer_findings(records: Sequence[MarkdownRecord]) -> List[Dict]:
    findings: List[Dict] = []
    scoped = [record for record in records if record.path.relative_to(REPO_ROOT).parts[0] in METADATA_SCOPE_ROOTS]

    missing_frontmatter = [record.rel_path for record in scoped if not record.has_frontmatter]
    missing_required_keys: List[str] = []
    empty_required_values: List[str] = []
    invalid_statuses: List[str] = []
    doctrine_missing_effective_date: List[str] = []
    doctrine_missing_provenance: List[str] = []

    for record in scoped:
        if not record.has_frontmatter:
            continue
        frontmatter = record.frontmatter
        missing = [key for key in REQUIRED_FRONTMATTER_KEYS if key not in frontmatter]
        if missing:
            missing_required_keys.append(f"{record.rel_path} -> missing {', '.join(missing)}")
        empty = [
            key
            for key in REQUIRED_FRONTMATTER_KEYS
            if key in frontmatter and value_is_empty(frontmatter[key])
        ]
        if empty:
            empty_required_values.append(f"{record.rel_path} -> empty {', '.join(empty)}")

        status_value = frontmatter.get("status", "")
        if status_value:
            allowed = allowed_statuses_for_path(record.path)
            if normalize_status(status_value) not in allowed:
                invalid_statuses.append(f"{record.rel_path} -> {status_value}")

        if doctrine_record(record):
            if "effective_date" not in frontmatter:
                doctrine_missing_effective_date.append(record.rel_path)
            if "provenance" not in frontmatter:
                doctrine_missing_provenance.append(record.rel_path)

    if missing_frontmatter:
        findings.append(
            make_finding(
                "SAA_METADATA_ENFORCER",
                "MAJOR",
                "metadata",
                "Governed markdown missing YAML frontmatter",
                "Governed markdown files in scope must start with YAML frontmatter.",
                missing_frontmatter,
                "Add YAML frontmatter with the required fields defined in 00_SYSTEM/schemas/SCHEMAS.md.",
                references=[{"path": SCHEMAS_PATH.relative_to(REPO_ROOT).as_posix(), "anchor": "Required Fields (All Artifacts)"}],
            )
        )

    if missing_required_keys:
        findings.append(
            make_finding(
                "SAA_METADATA_ENFORCER",
                "MAJOR",
                "metadata",
                "Governed markdown missing required frontmatter keys",
                "One or more governed markdown files are missing required frontmatter keys.",
                missing_required_keys,
                "Add the required keys: id, title, owner, status, created_date, and last_updated.",
                references=[{"path": SCHEMAS_PATH.relative_to(REPO_ROOT).as_posix(), "anchor": "Required Fields (All Artifacts)"}],
            )
        )

    if empty_required_values:
        findings.append(
            make_finding(
                "SAA_METADATA_ENFORCER",
                "MINOR",
                "metadata",
                "Required frontmatter values are empty",
                "Required metadata keys should be present and non-empty.",
                empty_required_values,
                "Populate the empty required metadata values.",
            )
        )

    if invalid_statuses:
        findings.append(
            make_finding(
                "SAA_METADATA_ENFORCER",
                "MINOR",
                "metadata",
                "Statuses outside the current allowlists",
                "Some status values fall outside the current path-specific lifecycle allowlists used by the metadata enforcer.",
                invalid_statuses,
                "Normalize status values or expand the allowlists if the current lifecycle vocabulary is intentional.",
            )
        )

    if doctrine_missing_effective_date:
        findings.append(
            make_finding(
                "SAA_METADATA_ENFORCER",
                "MINOR",
                "metadata",
                "Doctrine files missing effective_date",
                "Doctrine files should include effective_date under the doctrine-specific schema extension.",
                doctrine_missing_effective_date,
                "Add effective_date to doctrine files or document why the extension should not apply.",
                references=[{"path": SCHEMAS_PATH.relative_to(REPO_ROOT).as_posix(), "anchor": "Additional Fields (Doctrine)"}],
            )
        )

    if doctrine_missing_provenance:
        findings.append(
            make_finding(
                "SAA_METADATA_ENFORCER",
                "MINOR",
                "metadata",
                "Doctrine files missing provenance block",
                "Doctrine files should include provenance metadata under the doctrine-specific schema extension.",
                doctrine_missing_provenance,
                "Add provenance metadata or document why the extension should not apply.",
                references=[{"path": SCHEMAS_PATH.relative_to(REPO_ROOT).as_posix(), "anchor": "Additional Fields (Doctrine)"}],
            )
        )

    return findings


def strip_fenced_code_blocks(text: str) -> str:
    lines: List[str] = []
    in_fence = False
    for line in text.splitlines():
        if line.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if not in_fence:
            lines.append(line)
    return "\n".join(lines)


def extract_markdown_link_targets(text: str) -> List[str]:
    cleaned = strip_fenced_code_blocks(text)
    return [match.group(1).strip() for match in MARKDOWN_LINK_RE.finditer(cleaned)]


def normalize_link_target(raw_target: str) -> str:
    target = raw_target.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1].strip()
    if " " in target and not target.startswith("http"):
        target = target.split(" ", 1)[0]
    target = unquote(target)
    return target


def path_within_repo(path: Path) -> bool:
    try:
        path.resolve(strict=False).relative_to(REPO_ROOT)
        return True
    except ValueError:
        return False


def resolve_repo_target(source_path: Path, target: str) -> Tuple[Path | None, str]:
    normalized = normalize_link_target(target)
    if not normalized or normalized.startswith("#"):
        return None, "anchor"
    if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", normalized):
        return None, "external"
    if normalized.startswith("/"):
        first_segment = normalized.lstrip("/").split("/", 1)[0]
        known_roots = set(INVENTORY_ROOTS_WITHOUT_RUNS) | PLAYBOOK_TOP_LEVEL_DIRS | {
            "06_RUNS",
            "scripts",
            "agents",
            "cache",
            "gmail_governance",
            "screenshots",
        }
        if first_segment not in known_roots and first_segment != "Users":
            return None, "external"
        if first_segment == "Users":
            base = Path(normalized).resolve(strict=False)
        else:
            base = (REPO_ROOT / normalized.lstrip("/")).resolve(strict=False)
        mode = "absolute"
    else:
        base = (source_path.parent / normalized).resolve(strict=False)
        mode = "relative"
    if not path_within_repo(base):
        return base, mode
    candidates = [base]
    if not base.suffix:
        candidates.append(base.with_suffix(".md"))
        candidates.append(base / "README.md")
    for candidate in candidates:
        if candidate.exists():
            return candidate, mode
    return base, mode


def reference_integrity_findings(
    records: Sequence[MarkdownRecord],
    metadata_records: Sequence[YamlRecord],
    registry_entries: Sequence[Dict[str, str]],
) -> List[Dict]:
    findings: List[Dict] = []
    scoped = [record for record in records if record.path.relative_to(REPO_ROOT).parts[0] in REFERENCE_SCOPE_ROOTS]
    inbound_refs: Dict[str, set[str]] = defaultdict(set)
    broken_refs: List[str] = []
    missing_assets: List[str] = []

    for record in scoped:
        for raw_target in extract_markdown_link_targets(record.body):
            target_path, mode = resolve_repo_target(record.path, raw_target)
            normalized_target = normalize_link_target(raw_target).split("#", 1)[0]
            if mode in {"anchor", "external"} or not target_path:
                continue
            if path_within_repo(target_path) and target_path.exists():
                resolved = target_path
                if resolved.is_dir():
                    readme = resolved / "README.md"
                    if readme.exists():
                        inbound_refs[readme.relative_to(REPO_ROOT).as_posix()].add(record.rel_path)
                elif resolved.suffix.lower() == ".md":
                    inbound_refs[resolved.relative_to(REPO_ROOT).as_posix()].add(record.rel_path)
                continue

            entry = f"{record.rel_path} -> {normalized_target}"
            suffix = Path(normalized_target).suffix.lower()
            if suffix in ASSET_EXTENSIONS:
                missing_assets.append(entry)
            else:
                broken_refs.append(entry)

    if broken_refs:
        findings.append(
            make_finding(
                "SAA_REFERENCE_INTEGRITY",
                "MAJOR",
                "reference",
                "Broken internal markdown links",
                "Markdown links resolve to missing paths or escape the repo boundary.",
                broken_refs,
                "Repair or remove broken links so governed docs point to valid internal targets.",
            )
        )

    if missing_assets:
        findings.append(
            make_finding(
                "SAA_REFERENCE_INTEGRITY",
                "MAJOR",
                "reference",
                "Missing linked assets or attachments",
                "Linked assets or attachments are referenced by markdown but do not exist at the target path.",
                missing_assets,
                "Add the missing asset files or update the links to valid targets.",
            )
        )

    registry_paths = {entry["path"] for entry in registry_entries}
    orphaned_docs: List[str] = []
    for record in metadata_records:
        if record.path.parts[-3:-1] == ("_REGISTRY", "LEGACY_BUCKET_METADATA"):
            continue
        rel_to_playbooks = record.path.relative_to(REPO_ROOT / "02_PLAYBOOKS")
        if rel_to_playbooks.parts and rel_to_playbooks.parts[0] in {"_ASSETS", "_REGISTRY"}:
            continue
        readme = record.path.parent / "README.md"
        if not readme.exists():
            continue
        rel_readme = readme.relative_to(REPO_ROOT).as_posix()
        if rel_readme in registry_paths:
            continue
        if inbound_refs.get(rel_readme):
            continue
        orphaned_docs.append(rel_readme)

    if orphaned_docs:
        findings.append(
            make_finding(
                "SAA_REFERENCE_INTEGRITY",
                "MINOR",
                "reference",
                "Playbook docs with no inbound references",
                "Metadata-bearing playbook README files are not referenced by the registry or any other markdown link in scope.",
                orphaned_docs,
                "Add registry/index references for these docs or archive them if they are no longer canonical.",
            )
        )

    return findings


def registry_candidate_map(metadata_records: Sequence[YamlRecord]) -> Dict[str, YamlRecord]:
    candidates: Dict[str, YamlRecord] = {}
    for record in metadata_records:
        rel_to_playbooks = record.path.relative_to(REPO_ROOT / "02_PLAYBOOKS")
        if rel_to_playbooks.parts and rel_to_playbooks.parts[0] in {"_ASSETS", "_REGISTRY"}:
            continue
        readme = record.path.parent / "README.md"
        if not readme.exists():
            continue
        candidates[readme.relative_to(REPO_ROOT).as_posix()] = record
    return candidates


def registry_sync_findings(
    metadata_records: Sequence[YamlRecord],
    registry_entries: Sequence[Dict[str, str]],
    registry_error: str | None,
) -> List[Dict]:
    findings: List[Dict] = []

    if registry_error:
        return [
            make_finding(
                "SAA_REGISTRY_SYNC",
                "BLOCKER",
                "registry",
                "Playbook registry unavailable",
                registry_error,
                [PLAYBOOK_INDEX_PATH.relative_to(REPO_ROOT).as_posix()],
                "Restore PLAYBOOK_INDEX.md before running registry reconciliation.",
            )
        ]

    candidate_map = registry_candidate_map(metadata_records)
    registry_paths = {entry["path"] for entry in registry_entries}

    missing_entries = sorted(path for path in candidate_map if path not in registry_paths)
    if missing_entries:
        findings.append(
            make_finding(
                "SAA_REGISTRY_SYNC",
                "MAJOR",
                "registry",
                "Metadata-bearing playbooks missing from PLAYBOOK_INDEX.md",
                "Canonical playbook folders with metadata and README files are not listed in the registry.",
                missing_entries,
                "Add these playbooks to PLAYBOOK_INDEX.md so the registry matches the filesystem.",
            )
        )

    ghost_entries = sorted(path for path in registry_paths if not (REPO_ROOT / path).exists())
    if ghost_entries:
        findings.append(
            make_finding(
                "SAA_REGISTRY_SYNC",
                "MAJOR",
                "registry",
                "Registry paths missing on disk",
                "PLAYBOOK_INDEX.md contains entries whose target paths do not exist.",
                ghost_entries,
                "Remove stale registry entries or recreate the missing playbook targets.",
            )
        )

    status_mismatches: List[str] = []
    for entry in registry_entries:
        metadata_record = candidate_map.get(entry["path"])
        if not metadata_record:
            continue
        registry_status = normalize_status(entry["status"])
        metadata_status = normalize_status(metadata_record.data.get("status", ""))
        if metadata_status and registry_status != metadata_status:
            status_mismatches.append(
                f"{entry['path']} -> registry={entry['status']}, metadata={metadata_record.data.get('status', '')}"
            )

    if status_mismatches:
        findings.append(
            make_finding(
                "SAA_REGISTRY_SYNC",
                "MINOR",
                "registry",
                "Registry status mismatches",
                "Registry status values differ from the paired playbook metadata.yaml status values.",
                status_mismatches,
                "Normalize registry and metadata statuses so playbook state is represented consistently.",
            )
        )

    return findings


def merge_findings(findings_by_agent: Dict[str, List[Dict]]) -> List[Dict]:
    merged: List[Dict] = []
    seen: set[Tuple[str, str, Tuple[str, ...]]] = set()
    for findings in findings_by_agent.values():
        for finding in findings:
            key = (
                finding.get("category", ""),
                finding.get("title", ""),
                tuple(finding.get("affected_paths", [])),
            )
            if key in seen:
                continue
            seen.add(key)
            merged.append(finding)
    merged.sort(
        key=lambda finding: (
            SEVERITY_ORDER.get(finding.get("severity", "INFO"), 3),
            finding.get("category", ""),
            finding.get("title", ""),
            finding.get("agent", ""),
        )
    )
    return merged


def summarize_counts(findings: List[Dict]) -> Dict[str, int]:
    counts = {"BLOCKER": 0, "MAJOR": 0, "MINOR": 0, "INFO": 0}
    for finding in findings:
        severity = finding.get("severity", "INFO")
        counts[severity] = counts.get(severity, 0) + 1
    return counts


def render_findings_md(findings: List[Dict]) -> str:
    counts = summarize_counts(findings)
    lines = [
        "# System Admin Findings",
        "",
        "## Summary",
        f"- BLOCKER: {counts['BLOCKER']}",
        f"- MAJOR: {counts['MAJOR']}",
        f"- MINOR: {counts['MINOR']}",
        f"- INFO: {counts['INFO']}",
        "",
    ]
    if not findings:
        lines.append("No findings.")
        return "\n".join(lines) + "\n"

    for finding in findings:
        lines.extend(
            [
                f"## {finding['severity']} — {finding['title']}",
                f"Agent: {finding['agent']}",
                "",
                finding["description"],
                "",
                "Affected paths:",
            ]
        )
        for path in finding.get("affected_paths", []):
            lines.append(f"- {path}")
        if finding.get("suggested_fix"):
            lines.extend(["", f"Suggested fix: {finding['suggested_fix']}"])
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def render_system_admin_report(run_id: str, run_root: Path, findings: List[Dict]) -> str:
    counts = summarize_counts(findings)
    categories: Dict[str, int] = {}
    for finding in findings:
        category = finding.get("category", "unknown")
        categories[category] = categories.get(category, 0) + 1
    status = "FAILED" if counts["BLOCKER"] else "COMPLETED"

    lines = [
        "# SYSTEM ADMIN REPORT",
        "",
        f"Run ID: {run_id}",
        f"Run Root: {run_root.as_posix()}",
        "",
        "## Summary",
        f"- BLOCKER: {counts['BLOCKER']}",
        f"- MAJOR: {counts['MAJOR']}",
        f"- MINOR: {counts['MINOR']}",
        f"- INFO: {counts['INFO']}",
        "",
        f"Status: {status}",
        "",
        "## Category Totals",
    ]
    if categories:
        for category in sorted(categories):
            lines.append(f"- {category}: {categories[category]}")
    else:
        lines.append("- none")
    lines.extend(
        [
            "",
            "## Next Actions",
            "- Review appendices for agent-specific detail.",
            "- Triage BLOCKER/MAJOR findings first.",
            "",
        ]
    )
    return "\n".join(lines)


def render_appendix(agent: str, findings: List[Dict]) -> str:
    lines = [f"# Appendix — {agent}", ""]
    if not findings:
        lines.append("No findings.")
        return "\n".join(lines) + "\n"
    lines.append(f"Findings: {len(findings)}")
    lines.append("")
    for finding in findings:
        lines.extend(
            [
                f"## {finding['severity']} — {finding['title']}",
                "",
                finding["description"],
                "",
                "Affected paths:",
            ]
        )
        for path in finding.get("affected_paths", []):
            lines.append(f"- {path}")
        if finding.get("suggested_fix"):
            lines.extend(["", f"Suggested fix: {finding['suggested_fix']}"])
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def write_json(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Run System Admin Sweep locally.")
    parser.add_argument("--run-id", help="Override run ID (default: auto)")
    args = parser.parse_args()

    run_id = args.run_id or generate_run_id()
    run_root = REPO_ROOT / "06_RUNS" / run_id / "system_admin"
    run_root.mkdir(parents=True, exist_ok=True)

    start_time = utc_now()

    roots = governed_roots()
    inventory = build_inventory(roots)
    markdown_records = scan_markdown_records(INVENTORY_ROOTS_WITHOUT_RUNS)
    metadata_records = scan_yaml_records(REPO_ROOT / "02_PLAYBOOKS", "metadata.yaml")
    registry_entries, registry_error = parse_playbook_index()

    findings_by_agent: Dict[str, List[Dict]] = {agent: [] for agent in SAA_AGENTS}
    findings_by_agent["SAA_REPO_LINTER"] = repo_linter_findings(
        inventory=inventory,
        markdown_records=markdown_records,
        metadata_records=metadata_records,
        registry_entries=registry_entries,
    )
    findings_by_agent["SAA_FOLDER_MAP_DRIFT"] = folder_map_drift_findings()
    findings_by_agent["SAA_METADATA_ENFORCER"] = metadata_enforcer_findings(markdown_records)
    findings_by_agent["SAA_REFERENCE_INTEGRITY"] = reference_integrity_findings(
        records=markdown_records,
        metadata_records=metadata_records,
        registry_entries=registry_entries,
    )
    findings_by_agent["SAA_REGISTRY_SYNC"] = registry_sync_findings(
        metadata_records=metadata_records,
        registry_entries=registry_entries,
        registry_error=registry_error,
    )

    merged_findings = merge_findings(findings_by_agent)

    write_json(run_root / "inventory.json", inventory)
    for agent in SAA_AGENTS:
        write_json(run_root / f"findings_{agent}.json", findings_by_agent.get(agent, []))
    write_json(run_root / "findings.json", merged_findings)

    (run_root / "findings.md").write_text(render_findings_md(merged_findings), encoding="utf-8")
    (run_root / "SYSTEM_ADMIN_REPORT.md").write_text(
        render_system_admin_report(run_id, run_root, merged_findings),
        encoding="utf-8",
    )

    appendix_map = {
        "SAA_REPO_LINTER": "appendix_repo_linter.md",
        "SAA_FOLDER_MAP_DRIFT": "appendix_folder_map_drift.md",
        "SAA_METADATA_ENFORCER": "appendix_metadata_enforcer.md",
        "SAA_REFERENCE_INTEGRITY": "appendix_reference_integrity.md",
        "SAA_REGISTRY_SYNC": "appendix_registry_sync.md",
    }
    for agent, filename in appendix_map.items():
        (run_root / filename).write_text(
            render_appendix(agent, findings_by_agent.get(agent, [])),
            encoding="utf-8",
        )

    counts = summarize_counts(merged_findings)
    run_status = "FAILED" if counts["BLOCKER"] else "COMPLETED"
    runlog = "\n".join(
        [
            "# System Admin Sweep Run Log",
            "",
            f"Run ID: {run_id}",
            f"Start: {start_time}",
            f"End: {utc_now()}",
            "",
            f"Inventory entries: {len(inventory)}",
            f"Markdown files scanned: {len(markdown_records)}",
            f"Playbook metadata files scanned: {len(metadata_records)}",
            f"Total findings: {len(merged_findings)}",
            f"Run status: {run_status}",
            "",
            "Outputs:",
            f"- {run_root / 'inventory.json'}",
            f"- {run_root / 'findings.json'}",
            f"- {run_root / 'findings.md'}",
            f"- {run_root / 'SYSTEM_ADMIN_REPORT.md'}",
            "",
        ]
    )
    (run_root / "runlog.md").write_text(runlog, encoding="utf-8")
    write_json(
        run_root / "provenance.json",
        {
            "run_id": run_id,
            "started_at": start_time,
            "ended_at": utc_now(),
            "runner": "00_SYSTEM/scripts/run_system_admin_sweep.py",
            "notes": "Deterministic multi-agent system admin sweep.",
        },
    )

    print(f"System admin sweep complete: {run_root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
