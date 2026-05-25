#!/usr/bin/env python3
"""
LL Portfolio Agent Runner

Runs the active LLM-004/005/006 portfolio management stack in deterministic
local form. The runner writes advisory outputs to the canonical LL folders and
to a timestamped run folder under 06_RUNS.

Per POL-073, the runner may still materialize advisory outputs when PM
conformance fails, but the run itself must exit non-zero.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
import re
from typing import Dict, List, Tuple


REPO_ROOT = Path(__file__).resolve().parents[2]
LL_PORTFOLIO_DIR = REPO_ROOT / "04_INITIATIVES" / "LL_PORTFOLIO"
MATTERS_DIR = REPO_ROOT / "05_MATTERS"

PROJECT_MGMT_DIR = LL_PORTFOLIO_DIR / "03_FIRM_OPERATIONS" / "LLP-043"
PORTFOLIO_MGMT_DIR = LL_PORTFOLIO_DIR / "03_FIRM_OPERATIONS" / "LLP-042"
PORTFOLIO_GOVERNANCE_DIR = LL_PORTFOLIO_DIR / "03_FIRM_OPERATIONS" / "PORTFOLIO_GOVERNANCE"

GOVERNED_PROJECT_TYPES = {
    "Strategic Project",
    "Management Project",
    "Operational Project",
    "Decision Project",
}
PROJECT_TYPE_PATTERN = re.compile(r"(?im)^(?:\*\*Project Type:\*\*|Project Type:)\s*(.+?)\s*$")
APPROVAL_STAGE_PATTERN = re.compile(r"(?im)^Stage:\s*(.+?)\s*$")
PROJECT_ID_PATTERN = re.compile(r"(?im)^Project ID:\s*`?([^`\n]+?)`?\s*$")

CANONICAL_STAGE_DIR_NAMES = {"initiation", "planning", "executing", "closing"}
LEGACY_STAGE_DIR_NAMES = {"implementation", "monitoring"}
STAGE_DIR_NAMES = CANONICAL_STAGE_DIR_NAMES | LEGACY_STAGE_DIR_NAMES

CANONICAL_NUMBERED_ID_PATTERN = re.compile(r"^(?:LLP|HBP|SYS)-\d+$")
LEGACY_SUFFIXED_ID_PATTERN = re.compile(r"^(?:LLP|HBP|SYS)-\d+_.+$")
NUMBERED_PROJECT_DIR_PATTERN = re.compile(r"^(?:LLP|HBP|SYS)-\d+(?:_.+)?$")

ROOT_AUTHORITY_MARKERS = (
    ("READ-ONLY", "Root README is marked READ-ONLY."),
    ("Not yet reviewed", "Root README says the packet is not yet reviewed."),
    ("Awaiting ML1 population", "Root README says the packet is awaiting ML1 population."),
    ("Awaiting ML1 definition", "Root README says the packet is awaiting ML1 definition."),
)

COMMON_STAGE1 = [
    "PROJECT_CHARTER.md",
    "PROBLEM_STATEMENT.md",
    "SUCCESS_CRITERIA.md",
    "STAKEHOLDERS.md",
    "RISK_SCAN.md",
    "APPROVAL_RECORD.md",
]
STRATEGIC_STAGE1_EXTRA = ["BUSINESS_CASE.md"]
DECISION_STAGE1 = [
    "PROJECT_CHARTER.md",
    "PROBLEM_STATEMENT.md",
    "RISK_SCAN.md",
    "APPROVAL_RECORD.md",
]

SCOPE_ARTIFACT = "SCOPE_STATEMENT.md"
SCOPE_ARTIFACT_ALIASES = {SCOPE_ARTIFACT, "SCOPE_DEFINITION.md"}
PLANNING_PLAN_ARTIFACT = "PROJECT_PLAN.md"
PLANNING_PLAN_ALIASES = {PLANNING_PLAN_ARTIFACT, "WORKPLAN.md"}
REQUIRED_STAGE2_MEASUREMENT = ["METRICS.md"]

STRATEGIC_MANAGEMENT_STAGE2_PLANNING = [
    SCOPE_ARTIFACT,
    PLANNING_PLAN_ARTIFACT,
    "ASSUMPTIONS_CONSTRAINTS.md",
    "DEPENDENCIES.md",
    "RISK_REGISTER.md",
    "COMMUNICATION_PLAN.md",
]
OPERATIONAL_STAGE2_PLANNING = [
    SCOPE_ARTIFACT,
    PLANNING_PLAN_ARTIFACT,
    "DEPENDENCIES.md",
    "RISK_REGISTER.md",
]
DECISION_STAGE2_PLANNING = [
    "DECISION_FRAME.md",
    PLANNING_PLAN_ARTIFACT,
    "ASSUMPTIONS_CONSTRAINTS.md",
    "DEPENDENCIES.md",
    "RISK_REGISTER.md",
]

REQUIRED_EXECUTING = [
    "EXECUTION_LOG.md",
    "DECISION_LOG.md",
    "CHANGE_LOG.md",
    "ISSUE_LOG.md",
    "DELIVERABLES_TRACKER.md",
    "QA_CHECKLIST.md",
    "STATUS_REPORT.md",
    "KPI_DASHBOARD.md",
    "VARIANCE_REPORT.md",
    "RISK_UPDATES.md",
    "STAKEHOLDER_UPDATES.md",
]
REQUIRED_CLOSING = [
    "DELIVERABLE_ACCEPTANCE.md",
    "LESSONS_LEARNED.md",
    "POST_EXECUTION_REVIEW.md",
    "FINAL_STATUS_REPORT.md",
    "ARCHIVE_INDEX.md",
]

LEGACY_ARTIFACT_MESSAGES = {
    "WORKPLAN.md": "Legacy `WORKPLAN.md` present; normalize to `PROJECT_PLAN.md`.",
    "SCOPE_DEFINITION.md": "Legacy `SCOPE_DEFINITION.md` present; normalize to `SCOPE_STATEMENT.md`.",
    "METRIC_DEFINITION.md": "Retired split metric file `METRIC_DEFINITION.md` present; consolidate into `METRICS.md`.",
    "MEASUREMENT_METHOD.md": "Retired split metric file `MEASUREMENT_METHOD.md` present; consolidate into `METRICS.md`.",
    "BASELINE_CAPTURE_PERIOD.md": "Retired split metric file `BASELINE_CAPTURE_PERIOD.md` present; consolidate into `METRICS.md`.",
    "VALIDATION_REVIEW.md": "Retired split metric file `VALIDATION_REVIEW.md` present; consolidate into `METRICS.md`.",
    "ML1_METRIC_APPROVAL.md": "Retired `ML1_METRIC_APPROVAL.md` present; threshold approval belongs inside `METRICS.md`.",
    "POST_IMPLEMENTATION_REVIEW.md": "Legacy `POST_IMPLEMENTATION_REVIEW.md` present; normalize to `POST_EXECUTION_REVIEW.md`.",
}


@dataclass
class MatterLoad:
    essential_active: int
    strategic_active: int
    standard_active: int
    normal_active: int

    @property
    def priority_pressure(self) -> int:
        return self.essential_active + self.strategic_active


@dataclass
class ProjectSnapshot:
    project_id: str
    declared_project_id: str
    folder_name: str
    project_path: str
    project_type: str
    files: set[str]
    inferred_stage: int
    stage_label: str
    stage_source: str
    missing_stage1: List[str]
    missing_stage2_measurement: List[str]
    missing_stage2_planning: List[str]
    missing_executing: List[str]
    missing_closing: List[str]
    identity_issues: List[str]
    legacy_stage_issues: List[str]
    retired_artifact_issues: List[str]
    authority_issues: List[str]
    duplicate_declared_id: bool = False

    @property
    def approvals_present(self) -> bool:
        return has_requirement(self.files, "APPROVAL_RECORD.md")

    @property
    def stage1_complete(self) -> bool:
        return not self.missing_stage1

    @property
    def conformance_failures(self) -> List[str]:
        failures = list(self.identity_issues)
        if self.duplicate_declared_id and self.declared_project_id:
            failures.append(f"Declared Project ID `{self.declared_project_id}` is duplicated across the portfolio.")
        failures.extend(self.legacy_stage_issues)
        failures.extend(self.retired_artifact_issues)
        failures.extend(self.authority_issues)
        return failures

    @property
    def project_health(self) -> str:
        if self.conformance_failures:
            return "non-conformant"
        if self.inferred_stage == 0:
            return "at-risk"
        if not self.stage1_complete or not self.approvals_present:
            return "at-risk"
        if self.inferred_stage >= 2 and (self.missing_stage2_measurement or self.missing_stage2_planning):
            return "watch"
        if self.inferred_stage >= 3 and self.missing_executing:
            return "watch"
        if self.inferred_stage >= 4 and self.missing_closing:
            return "watch"
        return "on-track"

    @property
    def open_gate_count(self) -> int:
        return len(self.missing_for_current_stage)

    @property
    def stage2_completion_pct(self) -> int:
        if self.inferred_stage < 2:
            return 0
        required = stage2_planning_requirements(self.project_type) + REQUIRED_STAGE2_MEASUREMENT
        present = sum(1 for name in required if has_requirement(self.files, name))
        return int(round((present / len(required)) * 100))

    @property
    def relevant_stage2_measurement_gaps(self) -> List[str]:
        return self.missing_stage2_measurement if self.inferred_stage >= 2 else []

    @property
    def relevant_stage2_planning_gaps(self) -> List[str]:
        return self.missing_stage2_planning if self.inferred_stage >= 2 else []

    @property
    def display_name(self) -> str:
        if self.project_id == self.folder_name:
            return self.project_id
        return f"{self.project_id} [{self.folder_name}]"

    @property
    def missing_for_current_stage(self) -> List[str]:
        if self.inferred_stage <= 0:
            return stage1_requirements(self.project_type)
        required = stage_requirements(self.project_type, self.inferred_stage)
        return missing_requirements(self.files, required)


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def generate_run_id() -> str:
    stamp = datetime.now(timezone.utc).strftime("%H%M%SZ")
    date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    return f"RUN-{date}-LL-PORTFOLIO-AGENTS-{stamp}"


def requirement_aliases(name: str) -> set[str]:
    if name == SCOPE_ARTIFACT:
        return set(SCOPE_ARTIFACT_ALIASES)
    if name == PLANNING_PLAN_ARTIFACT:
        return set(PLANNING_PLAN_ALIASES)
    return {name}


def has_requirement(files: set[str], name: str) -> bool:
    return any(alias in files for alias in requirement_aliases(name))


def missing_requirements(files: set[str], required: List[str]) -> List[str]:
    return [name for name in required if not has_requirement(files, name)]


def stage1_requirements(project_type: str) -> List[str]:
    if project_type == "Strategic Project":
        return COMMON_STAGE1 + STRATEGIC_STAGE1_EXTRA
    if project_type == "Decision Project":
        return list(DECISION_STAGE1)
    return list(COMMON_STAGE1)


def stage2_planning_requirements(project_type: str) -> List[str]:
    if project_type == "Decision Project":
        return list(DECISION_STAGE2_PLANNING)
    if project_type == "Operational Project":
        return list(OPERATIONAL_STAGE2_PLANNING)
    return list(STRATEGIC_MANAGEMENT_STAGE2_PLANNING)


def stage_requirements(project_type: str, stage_index: int) -> List[str]:
    stage1 = stage1_requirements(project_type)
    stage2 = stage2_planning_requirements(project_type) + REQUIRED_STAGE2_MEASUREMENT
    if stage_index <= 1:
        return stage1
    if stage_index == 2:
        return stage1 + stage2
    if stage_index == 3:
        return stage1 + stage2 + REQUIRED_EXECUTING
    return stage1 + stage2 + REQUIRED_EXECUTING + REQUIRED_CLOSING


def infer_stage(files: set[str], project_type: str) -> int:
    if any(has_requirement(files, name) for name in REQUIRED_CLOSING):
        return 4
    if any(has_requirement(files, name) for name in REQUIRED_EXECUTING):
        return 3
    if any(has_requirement(files, name) for name in (REQUIRED_STAGE2_MEASUREMENT + stage2_planning_requirements(project_type))):
        return 2
    if any(has_requirement(files, name) for name in stage1_requirements(project_type)):
        return 1
    return 0


def stage_label_from_index(index: int) -> str:
    if index <= 0:
        return "Unstaged"
    if index == 1:
        return "Initiating"
    if index == 2:
        return "Planning"
    if index == 3:
        return "Executing"
    return "Closing"


def normalize_stage(raw_value: str) -> Tuple[str, int, str | None] | None:
    value = raw_value.strip().strip("*").strip()
    key = value.lower()
    aliases = {
        "initiating": ("Initiating", 1, None),
        "initiation": ("Initiating", 1, None),
        "planning": ("Planning", 2, None),
        "executing": ("Executing", 3, None),
        "execution": ("Executing", 3, None),
        "implementation": ("Executing", 3, "Deprecated stage label `Implementation` used; canonical label is `Executing`."),
        "monitoring": ("Executing", 3, "Deprecated stage label `Monitoring` used; canonical label is `Executing`."),
        "closing": ("Closing", 4, None),
        "closed": ("Closing", 4, None),
        "stage 1": ("Initiating", 1, None),
        "stage 2": ("Planning", 2, None),
        "stage 3": ("Executing", 3, None),
        "stage 4": ("Closing", 4, None),
        "1": ("Initiating", 1, None),
        "2": ("Planning", 2, None),
        "3": ("Executing", 3, None),
        "4": ("Closing", 4, None),
    }
    return aliases.get(key)


def extract_recorded_stage(approval_text: str) -> Tuple[str, int, List[str]] | None:
    match = APPROVAL_STAGE_PATTERN.search(approval_text)
    if not match:
        return None
    normalized = normalize_stage(match.group(1))
    if not normalized:
        return None
    stage_label, stage_index, warning = normalized
    warnings = [warning] if warning else []
    return stage_label, stage_index, warnings


def normalize_project_type(raw_value: str) -> str:
    value = raw_value.strip().strip("*").strip()
    key = value.lower()
    aliases = {
        "strategic": "Strategic Project",
        "strategic project": "Strategic Project",
        "management": "Management Project",
        "management project": "Management Project",
        "operational": "Operational Project",
        "operational project": "Operational Project",
        "decision": "Decision Project",
        "decision project": "Decision Project",
        "client matter": "Client Matter",
        "client project": "Client Matter",
        "client matters": "Client Matter",
        "client projects": "Client Matter",
    }
    return aliases.get(key, value)


def extract_project_type(charter_text: str) -> str | None:
    match = PROJECT_TYPE_PATTERN.search(charter_text)
    if not match:
        return None
    return normalize_project_type(match.group(1))


def safe_read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return ""


def is_relative_to(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
        return True
    except ValueError:
        return False


def extract_project_id_from_text(text: str) -> str | None:
    match = PROJECT_ID_PATTERN.search(text)
    if not match:
        return None
    return match.group(1).strip()


def extract_canonical_id_from_readme(text: str) -> str | None:
    marker = "## Canonical Project ID"
    if marker not in text:
        return None
    tail = text.split(marker, 1)[1]
    match = re.search(r"`?([A-Za-z0-9._-]+)`?", tail)
    if not match:
        return None
    return match.group(1)


def infer_project_type_from_path(relative_path: str) -> str | None:
    if relative_path.startswith("07_GROWTH_PROJECTS/") or relative_path.startswith("02_PRACTICE_AREAS/"):
        return "Strategic Project"
    if (
        relative_path.startswith("04_RISK/")
        or relative_path.startswith("06_FINANCIAL_PORTFOLIO/")
        or relative_path.startswith("01_FINANCIAL_MANAGEMENT/LLP-002")
        or relative_path.startswith("01_FINANCIAL_MANAGEMENT/LLP-044")
        or relative_path.startswith("08_MARKETING/")
        or relative_path.startswith("LLP-046")
        or relative_path == "03_FIRM_OPERATIONS/LLP-042"
        or relative_path == "03_FIRM_OPERATIONS/LLP-043"
        or relative_path == "03_FIRM_OPERATIONS/PORTFOLIO_GOVERNANCE"
    ):
        return "Management Project"
    if (
        relative_path.startswith("01_ACCOUNTING/")
        or relative_path.startswith("01_FINANCIAL_MANAGEMENT/LLP-001")
        or relative_path.startswith("03_FIRM_OPERATIONS/")
        or relative_path.startswith("05_MATTER_DOCKETING/")
    ):
        return "Operational Project"
    return None


def root_from_charter(charter_path: Path) -> Path:
    parent = charter_path.parent
    if parent.name in STAGE_DIR_NAMES:
        return parent.parent
    return parent


def is_project_root(path: Path) -> bool:
    if not path.is_dir():
        return False
    if path.name in STAGE_DIR_NAMES:
        return False
    if path == LL_PORTFOLIO_DIR:
        return False
    if NUMBERED_PROJECT_DIR_PATTERN.match(path.name):
        return True
    if (path / "PROJECT_CHARTER.md").exists() or (path / "initiation" / "PROJECT_CHARTER.md").exists():
        return True
    readme_path = path / "README.md"
    if readme_path.exists():
        return extract_canonical_id_from_readme(safe_read_text(readme_path)) is not None
    return False


def discover_project_roots() -> List[Path]:
    roots = {root_from_charter(path) for path in LL_PORTFOLIO_DIR.rglob("PROJECT_CHARTER.md")}
    ordered = sorted(roots, key=lambda p: (len(p.relative_to(LL_PORTFOLIO_DIR).parts), p.as_posix()))
    return [path for path in ordered if is_project_root(path)]


def collect_project_markdown_paths(project_root: Path, project_roots: List[Path]) -> List[Path]:
    nested_roots = [root for root in project_roots if root != project_root and is_relative_to(root, project_root)]
    markdown_paths: List[Path] = []
    for md_path in sorted(project_root.rglob("*.md"), key=lambda p: p.as_posix()):
        if any(is_relative_to(md_path, nested_root) for nested_root in nested_roots):
            continue
        markdown_paths.append(md_path)
    return markdown_paths


def extract_project_id_for_root(project_root: Path, markdown_paths: List[Path]) -> str:
    for name in ("APPROVAL_RECORD.md", "PROJECT_CHARTER.md"):
        for md_path in markdown_paths:
            if md_path.name != name:
                continue
            project_id = extract_project_id_from_text(safe_read_text(md_path))
            if project_id:
                return project_id
    readme_path = project_root / "README.md"
    if readme_path.exists():
        project_id = extract_canonical_id_from_readme(safe_read_text(readme_path))
        if project_id:
            return project_id
    return project_root.name


def extract_project_type_for_root(project_root: Path, markdown_paths: List[Path]) -> str | None:
    for md_path in markdown_paths:
        if md_path.name != "PROJECT_CHARTER.md":
            continue
        project_type = extract_project_type(safe_read_text(md_path))
        if project_type in GOVERNED_PROJECT_TYPES:
            return project_type
    return infer_project_type_from_path(project_root.relative_to(LL_PORTFOLIO_DIR).as_posix())


def detect_identity_issues(folder_name: str, declared_project_id: str) -> List[str]:
    issues: List[str] = []
    if declared_project_id and declared_project_id != folder_name:
        issues.append(f"Declared Project ID `{declared_project_id}` does not match folder name `{folder_name}`.")
    if LEGACY_SUFFIXED_ID_PATTERN.match(folder_name):
        issues.append(f"Legacy suffixed folder `{folder_name}` must be normalized to a plain Project ID.")
    if declared_project_id and LEGACY_SUFFIXED_ID_PATTERN.match(declared_project_id):
        issues.append(f"Declared Project ID `{declared_project_id}` uses a legacy suffixed pattern.")
    return issues


def detect_legacy_stage_issues(project_root: Path, recorded_stage_warnings: List[str]) -> List[str]:
    issues = list(recorded_stage_warnings)
    for name in sorted(LEGACY_STAGE_DIR_NAMES):
        if (project_root / name).exists():
            issues.append(f"Legacy stage directory `{name}/` present; normalize to the canonical four-stage model.")
    return issues


def detect_retired_artifact_issues(file_names: set[str]) -> List[str]:
    issues: List[str] = []
    for artifact, message in LEGACY_ARTIFACT_MESSAGES.items():
        if artifact in file_names:
            issues.append(message)
    return issues


def detect_authority_issues(project_root: Path) -> List[str]:
    readme_path = project_root / "README.md"
    if not readme_path.exists():
        return []
    text = safe_read_text(readme_path)
    issues: List[str] = []
    for marker, message in ROOT_AUTHORITY_MARKERS:
        if marker in text:
            issues.append(message)
    return issues


def discover_projects() -> List[ProjectSnapshot]:
    projects: List[ProjectSnapshot] = []
    if not LL_PORTFOLIO_DIR.exists():
        return projects

    project_roots = discover_project_roots()
    for project_root in project_roots:
        markdown_paths = collect_project_markdown_paths(project_root, project_roots)
        project_type = extract_project_type_for_root(project_root, markdown_paths)
        if project_type not in GOVERNED_PROJECT_TYPES:
            continue

        file_set = {path.name for path in markdown_paths}
        recorded_stage = None
        recorded_stage_warnings: List[str] = []
        approval_candidates = [path for path in markdown_paths if path.name == "APPROVAL_RECORD.md"]
        if approval_candidates:
            approval_path = sorted(
                approval_candidates,
                key=lambda p: (0 if p.parent == project_root else 1, len(p.relative_to(project_root).parts), p.as_posix()),
            )[0]
            approval_text = safe_read_text(approval_path)
            recorded_stage = extract_recorded_stage(approval_text) if approval_text else None
        if recorded_stage:
            stage_label, stage_index, recorded_stage_warnings = recorded_stage
            stage_source = "approval_record"
        else:
            stage_index = infer_stage(file_set, project_type)
            stage_label = stage_label_from_index(stage_index)
            stage_source = "artifacts"

        declared_project_id = extract_project_id_for_root(project_root, markdown_paths)
        folder_name = project_root.name
        project_id = declared_project_id or folder_name

        projects.append(
            ProjectSnapshot(
                project_id=project_id,
                declared_project_id=declared_project_id,
                folder_name=folder_name,
                project_path=project_root.relative_to(LL_PORTFOLIO_DIR).as_posix(),
                project_type=project_type,
                files=file_set,
                inferred_stage=stage_index,
                stage_label=stage_label,
                stage_source=stage_source,
                missing_stage1=missing_requirements(file_set, stage1_requirements(project_type)),
                missing_stage2_measurement=missing_requirements(file_set, REQUIRED_STAGE2_MEASUREMENT),
                missing_stage2_planning=missing_requirements(file_set, stage2_planning_requirements(project_type)),
                missing_executing=missing_requirements(file_set, REQUIRED_EXECUTING),
                missing_closing=missing_requirements(file_set, REQUIRED_CLOSING),
                identity_issues=detect_identity_issues(folder_name, declared_project_id),
                legacy_stage_issues=detect_legacy_stage_issues(project_root, recorded_stage_warnings),
                retired_artifact_issues=detect_retired_artifact_issues(file_set),
                authority_issues=detect_authority_issues(project_root),
            )
        )

    duplicate_counts = Counter(
        project.declared_project_id for project in projects if project.declared_project_id
    )
    for project in projects:
        if project.declared_project_id and duplicate_counts[project.declared_project_id] > 1:
            project.duplicate_declared_id = True

    return sorted(projects, key=lambda p: (p.project_path, p.project_id))


def extract_yaml_scalar(text: str, field: str) -> str | None:
    pattern = re.compile(rf"(?im)^{re.escape(field)}:\s*\"?([^\"\n]+?)\"?\s*$")
    match = pattern.search(text)
    if not match:
        return None
    return match.group(1).strip()


def discover_active_matter_load() -> MatterLoad:
    counts = Counter()
    if not MATTERS_DIR.exists():
        return MatterLoad(0, 0, 0, 0)

    for matter_path in MATTERS_DIR.rglob("MATTER.yaml"):
        text = safe_read_text(matter_path)
        status = (extract_yaml_scalar(text, "status") or "").lower()
        if status not in {"open", "pending"}:
            continue
        priority = (extract_yaml_scalar(text, "delivery_status") or "").lower()
        activity = (
            extract_yaml_scalar(text, "delivery_stage")
            or extract_yaml_scalar(text, "fulfillment_status")
            or ""
        ).lower()
        if activity and activity not in {"active", "activated"}:
            continue
        if priority in {"essential", "strategic", "standard", "normal"}:
            counts[priority] += 1

    return MatterLoad(
        essential_active=counts.get("essential", 0),
        strategic_active=counts.get("strategic", 0),
        standard_active=counts.get("standard", 0),
        normal_active=counts.get("normal", 0),
    )


def write_markdown(path: Path, title: str, run_id: str, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    header = "\n".join(
        [
            f"# {title}",
            "",
            f"- Generated: {utc_now()}",
            f"- Run ID: {run_id}",
            "",
            "> Advisory output. ML1 approval remains required for decisions.",
            "",
        ]
    )
    path.write_text(header + body.strip() + "\n", encoding="utf-8")


def render_table(headers: List[str], rows: List[List[str]]) -> str:
    out = []
    out.append("| " + " | ".join(headers) + " |")
    out.append("| " + " | ".join(["---"] * len(headers)) + " |")
    for row in rows:
        out.append("| " + " | ".join(row) + " |")
    return "\n".join(out)


def health_sort_key(health: str) -> int:
    order = {
        "non-conformant": 0,
        "at-risk": 1,
        "watch": 2,
        "on-track": 3,
    }
    return order.get(health, 9)


def project_priority_score(project: ProjectSnapshot) -> int:
    base = {
        "non-conformant": 20,
        "at-risk": 14,
        "watch": 7,
        "on-track": 0,
    }.get(project.project_health, 0)
    return (
        base
        + (3 * len(project.conformance_failures))
        + (3 * len(project.relevant_stage2_measurement_gaps))
        + (2 * len(project.relevant_stage2_planning_gaps))
        + len(project.missing_for_current_stage)
    )


def missing_frequency(projects: List[ProjectSnapshot], selector: str) -> Counter:
    counts: Counter = Counter()
    for project in projects:
        missing = getattr(project, selector)
        for name in missing:
            counts[name] += 1
    return counts


def join_or_none(items: List[str]) -> str:
    return ", ".join(items) if items else "none"


def llm_004_outputs(projects: List[ProjectSnapshot], run_id: str) -> Dict[str, object]:
    stage_rows: List[List[str]] = []
    health_rows: List[List[str]] = []
    blocker_lines: List[str] = []
    action_rows: List[List[str]] = []

    ranked = sorted(projects, key=lambda p: (-project_priority_score(p), p.project_id, p.project_path))
    health_counts = Counter(project.project_health for project in projects)

    for project in projects:
        blocker_types = []
        if project.conformance_failures:
            blocker_types.append("conformance")
        if project.missing_stage1:
            blocker_types.append("stage1")
        if project.inferred_stage >= 2 and project.missing_stage2_measurement:
            blocker_types.append("measurement")
        if project.inferred_stage >= 2 and project.missing_stage2_planning:
            blocker_types.append("planning")
        if not project.approvals_present:
            blocker_types.append("approval")

        stage_rows.append(
            [
                project.display_name,
                project.stage_label,
                project.project_health,
                str(project.open_gate_count),
                str(len(project.conformance_failures)),
                f"{project.stage2_completion_pct}%" if project.inferred_stage >= 2 else "n/a",
                "yes" if project.approvals_present else "no",
                join_or_none(blocker_types),
            ]
        )

        health_rows.append(
            [
                project.display_name,
                project.project_health,
                str(project.open_gate_count),
                str(len(project.relevant_stage2_planning_gaps)),
                str(len(project.relevant_stage2_measurement_gaps)),
                str(len(project.conformance_failures)),
            ]
        )

        current_stage_missing = project.missing_for_current_stage
        blocker_lines.append(
            f"- `{project.display_name}`: stage={project.stage_label}, health={project.project_health}, "
            f"gaps={len(current_stage_missing)} ({join_or_none(current_stage_missing)}), "
            f"conformance={len(project.conformance_failures)} ({join_or_none(project.conformance_failures)})"
        )

    for project in ranked:
        if project.conformance_failures:
            action = "Resolve PM conformance failures before relying on the packet as an authoritative control surface."
        elif project.inferred_stage < 2 and project.missing_stage1:
            action = "Complete the initiation packet before ML1 initiation review."
        elif project.inferred_stage < 2:
            action = "Keep the project in Initiating until ML1 authorizes Planning; planning drafts remain non-authoritative."
        elif project.relevant_stage2_measurement_gaps:
            action = "Complete METRICS.md and record ML1 threshold approval inside it."
        elif project.relevant_stage2_planning_gaps:
            action = "Close Stage 2 planning gaps before any stage advancement."
        else:
            action = "Maintain current controls and prepare the next gated packet."
        if not project.approvals_present:
            action = "Record the missing ML1 approval in APPROVAL_RECORD.md."
        action_rows.append([project.display_name, str(project_priority_score(project)), action])

    rollup_body = "\n".join(
        [
            "## Project Health Rollup",
            "",
            render_table(
                [
                    "Project",
                    "Health",
                    "Relevant Gate Gaps",
                    "Planning Gaps",
                    "Measurement Gaps",
                    "Conformance Failures",
                ],
                health_rows or [["none", "-", "-", "-", "-", "-"]],
            ),
            "",
            "## Summary",
            "",
            f"- Projects reviewed: {len(projects)}",
            f"- On-track: {health_counts.get('on-track', 0)}",
            f"- Watch: {health_counts.get('watch', 0)}",
            f"- At-risk: {health_counts.get('at-risk', 0)}",
            f"- Non-conformant: {health_counts.get('non-conformant', 0)}",
            f"- Average Stage 2 readiness: {int(round(sum((p.stage2_completion_pct for p in projects), 0) / max(len(projects), 1)))}%",
        ]
    )
    write_markdown(PROJECT_MGMT_DIR / "PROJECT_HEALTH_ROLLUP.md", "Project Health Rollup", run_id, rollup_body)

    checklist_body = "\n".join(
        [
            "## Stage Gate Snapshot",
            "",
            render_table(
                [
                    "Project",
                    "Stage",
                    "Health",
                    "Relevant Gate Gaps",
                    "Conformance Failures",
                    "Stage 2 Readiness",
                    "Approvals Present",
                    "Blocker Types",
                ],
                stage_rows or [["none", "-", "-", "-", "-", "-", "-", "-"]],
            ),
            "",
            "## Project-Specific Blockers",
            "",
            *(blocker_lines or ["- None."]),
            "",
            "## ML1 Action Queue",
            "",
            render_table(
                ["Project", "Priority Score", "Recommended Next Action"],
                action_rows or [["none", "-", "-"]],
            ),
            "",
            "## Rule",
            "",
            "- Do not advance a project gate without explicit ML1 approval.",
            "- Do not treat non-conformant packets as on-track PM controls.",
        ]
    )

    report = "\n".join(
        [
            "## LLM-004 Result",
            "",
            f"- Projects reviewed: {len(projects)}",
            f"- Non-conformant projects: {health_counts.get('non-conformant', 0)}",
            f"- Watch/at-risk projects: {health_counts.get('watch', 0) + health_counts.get('at-risk', 0)}",
            f"- Stage 2 planning gaps: {sum(len(project.missing_stage2_planning) for project in projects if project.inferred_stage >= 2)}",
            f"- Stage 2 measurement gaps: {sum(len(project.missing_stage2_measurement) for project in projects if project.inferred_stage >= 2)}",
            "",
            "## Top ML1 Actions",
            "",
            *([f"- {row[0]}: {row[2]}" for row in action_rows[:3]] or ["- None."]),
            "",
            "## Outputs",
            "",
            f"- {PROJECT_MGMT_DIR / 'PROJECT_HEALTH_ROLLUP.md'}",
        ]
    )

    return {"report": report, "body": checklist_body}


def llm_005_outputs(projects: List[ProjectSnapshot], run_id: str, matter_load: MatterLoad) -> Dict[str, object]:
    stage_counts = Counter(project.inferred_stage for project in projects)
    health_counts = Counter(project.project_health for project in projects)
    stage2_projects = [project for project in projects if project.inferred_stage >= 2]
    planning_freq = missing_frequency(stage2_projects, "relevant_stage2_planning_gaps")
    measurement_freq = missing_frequency(stage2_projects, "relevant_stage2_measurement_gaps")

    ranked = sorted(projects, key=lambda p: (-project_priority_score(p), p.project_id, p.project_path))

    dashboard_rows = [
        [
            project.display_name,
            project.stage_label,
            project.project_health,
            str(project.open_gate_count),
            "fail" if project.conformance_failures else "pass",
            f"{project.stage2_completion_pct}%" if project.inferred_stage >= 2 else "n/a",
        ]
        for project in projects
    ] or [["none", "-", "-", "-", "-", "-"]]

    priority_rows = []
    for rank, project in enumerate(ranked, start=1):
        if project.conformance_failures:
            basis = "PM conformance failure"
            focus = "Resolve identity, stage-vocabulary, or retired-artifact drift first."
        elif project.inferred_stage < 2 and project.missing_stage1:
            basis = "Initiation packet incomplete"
            focus = "Complete the initiation packet."
        elif project.relevant_stage2_measurement_gaps:
            basis = "Stage 2 measurement gap"
            focus = "Complete METRICS.md and threshold approval."
        elif project.relevant_stage2_planning_gaps:
            basis = "Stage 2 planning gap"
            focus = "Close planning artifacts before advancement."
        elif project.project_health == "at-risk":
            basis = "At-risk packet"
            focus = "Stabilize controls before expansion."
        else:
            basis = "Control-closed packet"
            focus = "Maintain current stage controls."
        priority_rows.append(
            [
                str(rank),
                project.display_name,
                project.project_health,
                basis,
                focus,
            ]
        )

    sequencing_lines: List[str] = []
    if matter_load.priority_pressure:
        sequencing_lines.append(
            f"1. Matter pressure gate: active essential matters={matter_load.essential_active}, "
            f"strategic matters={matter_load.strategic_active}; defer discretionary project starts unless they directly unblock delivery."
        )
    for index, project in enumerate(ranked[:3], start=len(sequencing_lines) + 1):
        if project.conformance_failures:
            sequencing_lines.append(
                f"{index}. `{project.display_name}` first focus: clear {len(project.conformance_failures)} PM conformance failures before treating this packet as reliable."
            )
        elif project.inferred_stage < 2:
            sequencing_lines.append(
                f"{index}. `{project.display_name}` first focus: close {len(project.missing_stage1)} initiation gaps and avoid opening new downstream work."
            )
        else:
            sequencing_lines.append(
                f"{index}. `{project.display_name}` first focus: close {len(project.missing_stage2_planning)} planning and "
                f"{len(project.missing_stage2_measurement)} measurement gaps."
            )
    if not sequencing_lines:
        sequencing_lines.append("1. No active projects detected.")

    planning_projects = [project.display_name for project in projects if project.inferred_stage == 2]
    executing_projects = [project.display_name for project in projects if project.inferred_stage == 3]
    collision_artifacts = sorted(
        [name for name, count in planning_freq.items() if count >= 2],
        key=lambda name: (-planning_freq[name], name),
    )

    capacity_rows: List[List[str]] = []
    total_capacity_units = 0
    for project in projects:
        if project.conformance_failures:
            planning_gap_count = len(project.relevant_stage2_planning_gaps)
            measurement_gap_count = len(project.relevant_stage2_measurement_gaps)
            load_units = len(project.conformance_failures) * 3 + planning_gap_count * 2 + measurement_gap_count * 3
        elif project.inferred_stage >= 2:
            planning_gap_count = len(project.relevant_stage2_planning_gaps)
            measurement_gap_count = len(project.relevant_stage2_measurement_gaps)
            load_units = (planning_gap_count * 2) + (measurement_gap_count * 3)
        else:
            planning_gap_count = 0
            measurement_gap_count = 0
            load_units = len(project.missing_stage1)
        total_capacity_units += load_units
        notes = "conformance residue" if project.conformance_failures else "current stage"
        capacity_rows.append(
            [
                project.display_name,
                str(load_units),
                str(planning_gap_count),
                str(measurement_gap_count),
                notes,
            ]
        )

    planning_bottleneck_count = sum(1 for project in projects if project.relevant_stage2_planning_gaps)
    measurement_bottleneck_count = sum(1 for project in projects if project.relevant_stage2_measurement_gaps)
    conformance_bottleneck_count = sum(1 for project in projects if project.conformance_failures)
    bottleneck_total = planning_bottleneck_count + measurement_bottleneck_count + conformance_bottleneck_count
    top_bottlenecks = planning_freq.most_common(3) + measurement_freq.most_common(2)
    bottleneck_rows = [
        [name, str(count), "shared planning/control gap"]
        for name, count in top_bottlenecks
    ] or [["none", "0", "none"]]
    bottleneck_assessment = (
        [
            "- No current-stage planning, measurement, or PM conformance bottlenecks were detected.",
            "- Continue monitoring stage concentration and matter pressure before adding discretionary project WIP.",
        ]
        if bottleneck_total == 0
        else [
            "- The portfolio should close conformance residue before adding new discretionary project WIP.",
            "- Shared planning and measurement gaps indicate migration work is still active, not complete.",
        ]
    )

    write_markdown(
        PORTFOLIO_MGMT_DIR / "PORTFOLIO_STATUS_DASHBOARD.md",
        "Portfolio Status Dashboard",
        run_id,
        "\n".join(
            [
                "## Portfolio Status",
                "",
                render_table(
                    ["Project", "Stage", "Health", "Relevant Open Gates", "Conformance", "Stage 2 Readiness"],
                    dashboard_rows,
                ),
                "",
                "## Summary",
                "",
                f"- Total projects: {len(projects)}",
                f"- On-track: {health_counts.get('on-track', 0)}",
                f"- Watch: {health_counts.get('watch', 0)}",
                f"- At-risk: {health_counts.get('at-risk', 0)}",
                f"- Non-conformant: {health_counts.get('non-conformant', 0)}",
                f"- Stage 2 concentration: {stage_counts.get(2, 0)} projects in Planning simultaneously",
                f"- Matter pressure: essential active={matter_load.essential_active}, strategic active={matter_load.strategic_active}",
            ]
        ),
    )

    write_markdown(
        PORTFOLIO_MGMT_DIR / "PROJECT_PRIORITY_MATRIX.md",
        "Project Priority Matrix",
        run_id,
        "\n".join(
            [
                "## Priority Rankings",
                "",
                render_table(
                    ["Rank", "Project", "Health", "Priority Basis", "Recommended Focus"],
                    priority_rows or [["-", "none", "-", "-", "-"]],
                ),
            ]
        ),
    )

    write_markdown(
        PORTFOLIO_MGMT_DIR / "SEQUENCING_RECOMMENDATIONS.md",
        "Sequencing Recommendations",
        run_id,
        "\n".join(
            [
                "## Recommended ML1 Attention Sequence",
                "",
                *sequencing_lines,
                "",
                "## Dependency-Driven Sequencing Constraints",
                "",
                "- No deterministic cross-project dependency parsing is implemented beyond declared dependency file presence.",
                "- Matter pressure remains a first-order sequencing input under POL-073.",
            ]
        ),
    )

    write_markdown(
        PORTFOLIO_MGMT_DIR / "BOTTLENECK_ANALYSIS.md",
        "Bottleneck Analysis",
        run_id,
        "\n".join(
            [
                "## Portfolio Bottlenecks",
                "",
                f"- Planning bottleneck candidates: {planning_bottleneck_count}",
                f"- Measurement bottleneck candidates: {measurement_bottleneck_count}",
                f"- PM conformance bottleneck candidates: {conformance_bottleneck_count}",
                "",
                "## Top Bottlenecks",
                "",
                render_table(["Artifact", "Missing In N Projects", "Impact"], bottleneck_rows),
                "",
                "## Assessment",
                "",
                *bottleneck_assessment,
            ]
        ),
    )

    write_markdown(
        PORTFOLIO_MGMT_DIR / "RESOURCE_COLLISION_REPORT.md",
        "Resource Collision Report",
        run_id,
        "\n".join(
            [
                "## Simultaneous Stage Concentrations",
                "",
                f"- Projects in Stage 2 (Planning) simultaneously: {len(planning_projects)} — {', '.join(planning_projects) if planning_projects else 'none'}",
                f"- Projects in Stage 3 (Executing) simultaneously: {len(executing_projects)} — {', '.join(executing_projects) if executing_projects else 'none'}",
                "",
                "## Collision Risk Assessment",
                "",
                f"- Shared missing planning artifacts: {join_or_none(collision_artifacts)}",
                f"- ML1 approval load is elevated when Planning concentration and matter pressure coexist: {matter_load.priority_pressure > 0 and bool(planning_projects)}",
            ]
        ),
    )

    write_markdown(
        PORTFOLIO_MGMT_DIR / "WIP_LOAD_ANALYSIS.md",
        "WIP Load Analysis",
        run_id,
        "\n".join(
            [
                "## WIP Summary",
                "",
                f"- Active projects (Stage >= 1): {sum(1 for project in projects if project.inferred_stage >= 1)}",
                f"- At-risk active: {sum(1 for project in projects if project.inferred_stage >= 1 and project.project_health == 'at-risk')}",
                f"- Watch: {health_counts.get('watch', 0)}",
                f"- Non-conformant: {health_counts.get('non-conformant', 0)}",
                f"- Portfolio planning gap total: {sum(len(project.missing_stage2_planning) for project in projects)}",
                "",
                "## ML1 Approval Load",
                "",
                f"- Projects missing approvals: {sum(1 for project in projects if not project.approvals_present)}",
                f"- Projects carrying PM conformance failures: {sum(1 for project in projects if project.conformance_failures)}",
                f"- Active essential matters: {matter_load.essential_active}",
                f"- Active strategic matters: {matter_load.strategic_active}",
                "",
                "## Assessment",
                "",
                "- When essential or strategic matter pressure is active, discretionary project expansion should slow unless the project directly unblocks delivery.",
            ]
        ),
    )

    write_markdown(
        PORTFOLIO_MGMT_DIR / "CAPACITY_ALLOCATION_MODEL.md",
        "Capacity Allocation Model",
        run_id,
        "\n".join(
            [
                "## Per-Project Capacity Demand",
                "",
                render_table(
                    ["Project", "Estimated Units", "Planning Gaps", "Measurement Gaps", "Notes"],
                    capacity_rows or [["none", "-", "-", "-", "-"]],
                ),
                "",
                "## Summary",
                "",
                f"- Stage 1 load: {stage_counts.get(1, 0)}",
                f"- Stage 2 load: {stage_counts.get(2, 0)}",
                f"- Stage 3 load: {stage_counts.get(3, 0)}",
                f"- Stage 4 load: {stage_counts.get(4, 0)}",
                f"- Total estimated capacity units: {total_capacity_units}",
            ]
        ),
    )

    write_markdown(
        PORTFOLIO_MGMT_DIR / "STAGE_DISTRIBUTION_REPORT.md",
        "Stage Distribution Report",
        run_id,
        "\n".join(
            [
                "## Stage Distribution",
                "",
                render_table(
                    ["Stage", "Count"],
                    [
                        ["Unstaged", str(stage_counts.get(0, 0))],
                        ["Initiating", str(stage_counts.get(1, 0))],
                        ["Planning", str(stage_counts.get(2, 0))],
                        ["Executing", str(stage_counts.get(3, 0))],
                        ["Closing", str(stage_counts.get(4, 0))],
                    ],
                ),
            ]
        ),
    )

    report = "\n".join(
        [
            "## LLM-005 Result",
            "",
            f"- Projects reviewed: {len(projects)}",
            f"- Stage 2 concentration: {stage_counts.get(2, 0)}",
            f"- Non-conformant projects: {health_counts.get('non-conformant', 0)}",
            f"- Matter pressure signal: essential active={matter_load.essential_active}, strategic active={matter_load.strategic_active}",
            "",
            "## Top Sequencing Moves",
            "",
            *(f"- {line}" for line in sequencing_lines[:3]),
            "",
            "## Outputs",
            "",
            f"- {PORTFOLIO_MGMT_DIR}",
        ]
    )
    return {"report": report}


def llm_006_outputs(projects: List[ProjectSnapshot], run_id: str) -> Dict[str, object]:
    approval_gaps = [project for project in projects if not project.approvals_present]
    stage_violations = [project for project in projects if project.missing_for_current_stage]
    metric_schema_gaps = [project for project in projects if project.inferred_stage >= 2 and project.missing_stage2_measurement]
    planning_gaps = [project for project in projects if project.inferred_stage >= 2 and project.missing_stage2_planning]
    conformance_projects = [project for project in projects if project.conformance_failures]

    contradiction_alerts: List[str] = []
    seen_declared_ids = set()
    for project in projects:
        if project.declared_project_id and project.declared_project_id in seen_declared_ids:
            contradiction_alerts.append(f"Duplicate declared Project ID: {project.declared_project_id}")
        seen_declared_ids.add(project.declared_project_id)

    severity_counts = {"critical": 0, "high": 0, "medium": 0, "low": 0}
    for project in projects:
        if project.conformance_failures or project.missing_stage1 or not project.approvals_present:
            severity_counts["critical"] += 1
        elif project.missing_stage2_measurement:
            severity_counts["high"] += 1
        elif project.missing_stage2_planning:
            severity_counts["medium"] += 1
        else:
            severity_counts["low"] += 1

    stage2_projects = [project for project in projects if project.inferred_stage >= 2]
    planning_drift_freq = missing_frequency(stage2_projects, "missing_stage2_planning")
    measurement_drift_freq = missing_frequency(stage2_projects, "missing_stage2_measurement")
    retired_artifact_freq: Counter = Counter()
    for project in projects:
        for issue in project.retired_artifact_issues:
            retired_artifact_freq[issue] += 1

    write_markdown(
        PORTFOLIO_GOVERNANCE_DIR / "GOVERNANCE_COMPLIANCE_AUDIT.md",
        "Governance Compliance Audit",
        run_id,
        "\n".join(
            [
                "## Governance Compliance Audit",
                "",
                f"- Projects audited: {len(projects)}",
                f"- Stage violations: {len(stage_violations)}",
                f"- Approval gaps: {len(approval_gaps)}",
                f"- Metric schema gaps: {len(metric_schema_gaps)}",
                f"- Planning schema gaps: {len(planning_gaps)}",
                f"- PM conformance failures: {len(conformance_projects)}",
                "",
                "## Severity Mix",
                "",
                f"- Critical: {severity_counts['critical']}",
                f"- High: {severity_counts['high']}",
                f"- Medium: {severity_counts['medium']}",
                f"- Low: {severity_counts['low']}",
            ]
        ),
    )

    write_markdown(
        PORTFOLIO_GOVERNANCE_DIR / "STAGE_GATE_VIOLATION_REPORT.md",
        "Stage Gate Violation Report",
        run_id,
        "\n".join(
            [
                "## Stage Gate Violations",
                "",
                *(
                    [
                        f"- `{project.display_name}`: relevant missing artifacts={len(project.missing_for_current_stage)} "
                        f"({join_or_none(project.missing_for_current_stage)})"
                        for project in stage_violations
                    ]
                    or ["- None."]
                ),
            ]
        ),
    )

    write_markdown(
        PORTFOLIO_GOVERNANCE_DIR / "METRIC_SCHEMA_INTEGRITY_REPORT.md",
        "Metric Schema Integrity Report",
        run_id,
        "\n".join(
            [
                "## Metric Schema Integrity",
                "",
                *(
                    [
                        f"- `{project.display_name}` missing measurement artifacts: {join_or_none(project.missing_stage2_measurement)}"
                        for project in metric_schema_gaps
                    ]
                    or ["- All Stage 2+ projects contain required measurement artifacts."]
                ),
            ]
        ),
    )

    write_markdown(
        PORTFOLIO_GOVERNANCE_DIR / "CONTRADICTION_ALERTS.md",
        "Contradiction Alerts",
        run_id,
        "\n".join(
            [
                "## Contradiction Alerts",
                "",
                *(contradiction_alerts or ["- No duplicate declared project IDs detected by deterministic checks."]),
            ]
        ),
    )

    write_markdown(
        PORTFOLIO_GOVERNANCE_DIR / "MIGRATION_VALIDATION_REPORT.md",
        "Migration Validation Report",
        run_id,
        "\n".join(
            [
                "## Migration Validation",
                "",
                *(
                    [
                        f"- `{project.display_name}` migration residue: {join_or_none(project.retired_artifact_issues + project.legacy_stage_issues + project.identity_issues)}"
                        for project in conformance_projects
                    ]
                    or ["- No migration residue detected in this run."]
                ),
            ]
        ),
    )

    write_markdown(
        PORTFOLIO_GOVERNANCE_DIR / "APPROVAL_GAP_REPORT.md",
        "Approval Gap Report",
        run_id,
        "\n".join(
            [
                "## Approval Gaps",
                "",
                *(
                    [
                        f"- `{project.display_name}` missing `APPROVAL_RECORD.md`."
                        for project in approval_gaps
                    ]
                    or ["- None."]
                ),
            ]
        ),
    )

    write_markdown(
        PORTFOLIO_GOVERNANCE_DIR / "DOCTRINE_DRIFT_REPORT.md",
        "Doctrine Drift Report",
        run_id,
        "\n".join(
            [
                "## Structural Drift Patterns",
                "",
                "- Planning drift:",
                *(
                    [
                        f"- `{name}` missing in {count} project(s)."
                        for name, count in planning_drift_freq.most_common(5)
                    ]
                    or ["- No repeated planning drift pattern detected."]
                ),
                "- Measurement drift:",
                *(
                    [
                        f"- `{name}` missing in {count} project(s)."
                        for name, count in measurement_drift_freq.most_common(3)
                    ]
                    or ["- No repeated measurement drift pattern detected."]
                ),
                "- Retired artifact residue:",
                *(
                    [
                        f"- {message} Seen in {count} project(s)."
                        for message, count in retired_artifact_freq.most_common(5)
                    ]
                    or ["- No repeated retired-artifact residue detected."]
                ),
            ]
        ),
    )

    write_markdown(
        PORTFOLIO_GOVERNANCE_DIR / "PM_CONFORMANCE_REPORT.md",
        "PM Conformance Report",
        run_id,
        "\n".join(
            [
                "## PM Conformance Failures",
                "",
                *(
                    [
                        f"- `{project.display_name}`: {join_or_none(project.conformance_failures)}"
                        for project in conformance_projects
                    ]
                    or ["- None."]
                ),
            ]
        ),
    )

    report = "\n".join(
        [
            "## LLM-006 Result",
            "",
            f"- Projects audited: {len(projects)}",
            f"- Approval gaps: {len(approval_gaps)}",
            f"- Stage gate violations: {len(stage_violations)}",
            f"- Metric schema gaps: {len(metric_schema_gaps)}",
            f"- Planning schema gaps: {len(planning_gaps)}",
            f"- PM conformance failures: {len(conformance_projects)}",
            "",
            "## Governance Risk View",
            "",
            f"- Critical risk projects: {severity_counts['critical']}",
            f"- High risk projects: {severity_counts['high']}",
            f"- Medium risk projects: {severity_counts['medium']}",
            "",
            "## Outputs",
            "",
            f"- {PORTFOLIO_GOVERNANCE_DIR}",
        ]
    )
    return {"report": report, "conformance_failures": len(conformance_projects)}


def write_run_outputs(
    run_root: Path,
    run_id: str,
    project_count: int,
    llm_004_report: str,
    llm_005_report: str,
    llm_006_report: str,
) -> None:
    run_root.mkdir(parents=True, exist_ok=True)

    run_log = "\n".join(
        [
            "# RUN LOG — LL Portfolio Agents",
            "",
            f"Run ID: {run_id}",
            f"Generated: {utc_now()}",
            "",
            "Agents:",
            "- LLM-004 Project Management Agent",
            "- LLM-005 Portfolio Management Agent",
            "- LLM-006 Portfolio Governance Agent",
            "",
            f"Projects reviewed: {project_count}",
            "",
            "Outputs written to:",
            f"- {PROJECT_MGMT_DIR}",
            f"- {PORTFOLIO_MGMT_DIR}",
            f"- {PORTFOLIO_GOVERNANCE_DIR}",
            "",
        ]
    )
    (run_root / "RUN_LOG.md").write_text(run_log, encoding="utf-8")

    write_markdown(run_root / "LLM-004_LLP-043_REPORT.md", "LLM-004 Project Management Report", run_id, llm_004_report)
    write_markdown(run_root / "LLM-005_LLP-042_REPORT.md", "LLM-005 Portfolio Management Report", run_id, llm_005_report)
    write_markdown(run_root / "LLM-006_PORTFOLIO_GOVERNANCE_REPORT.md", "LLM-006 Portfolio Governance Report", run_id, llm_006_report)


def main() -> int:
    run_id = generate_run_id()
    run_root = REPO_ROOT / "06_RUNS" / run_id / "ll_portfolio_agents"

    projects = discover_projects()
    matter_load = discover_active_matter_load()

    llm_004 = llm_004_outputs(projects, run_id)
    llm_005 = llm_005_outputs(projects, run_id, matter_load)
    llm_006 = llm_006_outputs(projects, run_id)

    write_run_outputs(
        run_root=run_root,
        run_id=run_id,
        project_count=len(projects),
        llm_004_report=llm_004["report"],
        llm_005_report=llm_005["report"],
        llm_006_report=llm_006["report"],
    )

    print(f"LL portfolio agents run complete: {run_root}")
    if llm_006["conformance_failures"]:
        print(f"PM conformance failed in {llm_006['conformance_failures']} project(s).")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
