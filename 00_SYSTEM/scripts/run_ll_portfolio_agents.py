#!/usr/bin/env python3
"""
LL Portfolio Agent Runner

Runs the restored LLM-004/005/006 agent logic in a deterministic, local form and
materializes outputs in both:
1) Canonical LL folders under 04_INITIATIVES/LL_PORTFOLIO/03_FIRM_OPERATIONS/
2) A timestamped run folder under 06_RUNS/
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

PROJECT_MGMT_DIR = REPO_ROOT / "04_INITIATIVES" / "LL_PORTFOLIO" / "03_FIRM_OPERATIONS" / "PROJECT_MANAGEMENT"
PORTFOLIO_MGMT_DIR = REPO_ROOT / "04_INITIATIVES" / "LL_PORTFOLIO" / "03_FIRM_OPERATIONS" / "PORTFOLIO_MANAGEMENT"
PORTFOLIO_GOVERNANCE_DIR = REPO_ROOT / "04_INITIATIVES" / "LL_PORTFOLIO" / "03_FIRM_OPERATIONS" / "PORTFOLIO_GOVERNANCE"

GOVERNED_PROJECT_TYPES = {"Strategic Project", "Management Project", "Operational Project", "Decision Project"}
PROJECT_TYPE_PATTERN = re.compile(r"(?im)^(?:\*\*Project Type:\*\*|Project Type:)\s*(.+?)\s*$")
APPROVAL_STAGE_PATTERN = re.compile(r"(?im)^Stage:\s*(.+?)\s*$")
PROJECT_ID_PATTERN = re.compile(r"(?im)^Project ID:\s*(LLP-\d+)\s*$")
STAGE_DIR_NAMES = {"initiation", "planning", "implementation", "monitoring", "closing"}

COMMON_STAGE1 = [
    "PROJECT_CHARTER.md",
    "PROBLEM_STATEMENT.md",
    "SUCCESS_CRITERIA.md",
    "STAKEHOLDERS.md",
    "RISK_SCAN.md",
    "APPROVAL_RECORD.md",
]

STRATEGIC_STAGE1_EXTRA = [
    "BUSINESS_CASE.md",
]

DECISION_STAGE1 = [
    "PROJECT_CHARTER.md",
    "PROBLEM_STATEMENT.md",
    "RISK_SCAN.md",
    "APPROVAL_RECORD.md",
]

REQUIRED_STAGE2_MEASUREMENT = [
    # METRICS.md is the single canonical measurement artifact per
    # POL-055_Repository_Project_Policy.md §8.
    # The four-file split schema (METRIC_DEFINITION.md, MEASUREMENT_METHOD.md,
    # BASELINE_CAPTURE_PERIOD.md, VALIDATION_REVIEW.md) is deprecated and non-compliant.
    # ML1 threshold approval is recorded inside METRICS.md, not in a separate
    # ML1_METRIC_APPROVAL.md file.
    "METRICS.md",
]

SCOPE_ARTIFACT = "SCOPE_STATEMENT.md"
SCOPE_ARTIFACT_ALIASES = {SCOPE_ARTIFACT, "SCOPE_DEFINITION.md"}

PLANNING_PLAN_ARTIFACT = "PROJECT_PLAN.md"
PLANNING_PLAN_ALIASES = {PLANNING_PLAN_ARTIFACT, "WORKPLAN.md"}

STRATEGIC_MANAGEMENT_STAGE2_PLANNING = [
    SCOPE_ARTIFACT,
    # PROJECT_PLAN.md is preferred. Legacy WORKPLAN.md remains accepted for compatibility.
    PLANNING_PLAN_ARTIFACT,
    "ASSUMPTIONS_CONSTRAINTS.md",
    "DEPENDENCIES.md",
    "RISK_REGISTER.md",
    "COMMUNICATION_PLAN.md",
]

OPERATIONAL_STAGE2_PLANNING = [
    SCOPE_ARTIFACT,
    # PROJECT_PLAN.md is preferred. Legacy WORKPLAN.md remains accepted for compatibility.
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

REQUIRED_STAGE3 = [
    "EXECUTION_LOG.md",
    "DECISION_LOG.md",
    "CHANGE_LOG.md",
    "ISSUE_LOG.md",
    "DELIVERABLES_TRACKER.md",
    "QA_CHECKLIST.md",
]

REQUIRED_STAGE4 = [
    "STATUS_REPORT.md",
    "KPI_DASHBOARD.md",
    "VARIANCE_REPORT.md",
    "RISK_UPDATES.md",
    "STAKEHOLDER_UPDATES.md",
]

REQUIRED_STAGE5 = [
    "DELIVERABLE_ACCEPTANCE.md",
    "LESSONS_LEARNED.md",
    "POST_IMPLEMENTATION_REVIEW.md",
    "FINAL_STATUS_REPORT.md",
    "ARCHIVE_INDEX.md",
]


@dataclass
class ProjectSnapshot:
    project_id: str
    project_path: str
    project_type: str
    files: set[str]
    inferred_stage: int
    stage_label: str
    stage_source: str
    missing_stage1: List[str]
    missing_stage2_measurement: List[str]
    missing_stage2_planning: List[str]
    missing_stage3: List[str]
    missing_stage4: List[str]
    missing_stage5: List[str]

    @property
    def approvals_present(self) -> bool:
        return has_requirement(self.files, "APPROVAL_RECORD.md")

    @property
    def stage1_complete(self) -> bool:
        return not self.missing_stage1

    @property
    def stage2_measurement_complete(self) -> bool:
        return not self.missing_stage2_measurement

    @property
    def project_health(self) -> str:
        if self.inferred_stage == 0:
            return "at-risk"
        if not self.stage1_complete:
            return "at-risk"
        if not self.approvals_present:
            return "at-risk"
        if self.inferred_stage >= 2 and (self.missing_stage2_measurement or self.missing_stage2_planning):
            return "watch"
        if self.inferred_stage >= 3 and self.missing_stage3:
            return "watch"
        if self.inferred_stage >= 4 and self.missing_stage4:
            return "watch"
        if self.inferred_stage >= 5 and self.missing_stage5:
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
        return f"{self.project_id} ({self.project_path})"

    @property
    def missing_for_current_stage(self) -> List[str]:
        if self.inferred_stage <= 0:
            return stage1_requirements(self.project_type)
        required = stage_requirements(self.project_type, self.inferred_stage)
        return missing_requirements(self.files, required)


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def utc_date() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


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
        return stage1 + stage2 + REQUIRED_STAGE3
    if stage_index == 4:
        return stage1 + stage2 + REQUIRED_STAGE3 + REQUIRED_STAGE4
    return stage1 + stage2 + REQUIRED_STAGE3 + REQUIRED_STAGE4 + REQUIRED_STAGE5


def infer_stage(files: set[str], project_type: str) -> int:
    if any(has_requirement(files, name) for name in REQUIRED_STAGE5):
        return 5
    if any(has_requirement(files, name) for name in REQUIRED_STAGE4):
        return 4
    if any(has_requirement(files, name) for name in REQUIRED_STAGE3):
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
    if index in {3, 4}:
        return "Executing"
    return "Closing"


def normalize_stage(raw_value: str) -> Tuple[str, int] | None:
    value = raw_value.strip().strip("*").strip()
    key = value.lower()
    aliases = {
        "initiating": ("Initiating", 1),
        "initiation": ("Initiating", 1),
        "planning": ("Planning", 2),
        "executing": ("Executing", 3),
        "execution": ("Executing", 3),
        "monitoring": ("Executing", 4),
        "implementation": ("Executing", 3),
        "closing": ("Closing", 5),
        "closed": ("Closing", 5),
        "stage 1": ("Initiating", 1),
        "stage 2": ("Planning", 2),
        "stage 3": ("Executing", 3),
        "stage 4": ("Executing", 4),
        "stage 5": ("Closing", 5),
        "1": ("Initiating", 1),
        "2": ("Planning", 2),
        "3": ("Executing", 3),
        "4": ("Executing", 4),
        "5": ("Closing", 5),
    }
    return aliases.get(key)


def extract_recorded_stage(approval_text: str) -> Tuple[str, int] | None:
    match = APPROVAL_STAGE_PATTERN.search(approval_text)
    if not match:
        return None
    return normalize_stage(match.group(1))


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


def canonical_id_from_dirname(path: Path) -> str | None:
    if path.name.startswith("LLP-"):
        return path.name.split("_", 1)[0]
    return None


def extract_project_id_from_text(text: str) -> str | None:
    match = PROJECT_ID_PATTERN.search(text)
    if not match:
        return None
    return match.group(1)


def extract_canonical_id_from_readme(text: str) -> str | None:
    marker = "## Canonical Project ID"
    if marker not in text:
        return None
    tail = text.split(marker, 1)[1]
    match = re.search(r"`?(LLP-\d+)`?", tail)
    if not match:
        return None
    return match.group(1)


def infer_project_type_from_path(relative_path: str) -> str | None:
    if relative_path.startswith("07_GROWTH_PROJECTS/") or relative_path.startswith("02_PRACTICE_AREAS/"):
        return "Strategic Project"
    if (
        relative_path.startswith("04_RISK/")
        or relative_path.startswith("06_FINANCIAL_PORTFOLIO/")
        or relative_path.startswith("01_FINANCIAL_MANAGEMENT/LLP-002_BUDGETING")
        or relative_path.startswith("01_FINANCIAL_MANAGEMENT/LLP-044_FINANCE")
        or relative_path.startswith("08_MARKETING/")
        or relative_path.startswith("09_SERVICE_MANAGEMENT")
        or relative_path == "03_FIRM_OPERATIONS/PORTFOLIO_MANAGEMENT"
        or relative_path == "03_FIRM_OPERATIONS/PROJECT_MANAGEMENT"
    ):
        return "Management Project"
    if (
        relative_path.startswith("01_ACCOUNTING/")
        or relative_path.startswith("01_FINANCIAL_MANAGEMENT/LLP-001_ACCOUNTING")
        or relative_path.startswith("03_FIRM_OPERATIONS/")
        or relative_path.startswith("05_MATTER_DOCKETING/")
    ):
        return "Operational Project"
    return None


def is_project_root(path: Path) -> bool:
    if not path.is_dir():
        return False
    if path.name in STAGE_DIR_NAMES:
        return False
    if path == LL_PORTFOLIO_DIR:
        return False
    if canonical_id_from_dirname(path):
        return True
    if (path / "PROJECT_CHARTER.md").exists() or (path / "initiation" / "PROJECT_CHARTER.md").exists():
        return True
    readme_path = path / "README.md"
    if readme_path.exists():
        return extract_canonical_id_from_readme(safe_read_text(readme_path)) is not None
    return False


def discover_project_roots() -> List[Path]:
    roots: List[Path] = []
    for path in sorted(
        (p for p in LL_PORTFOLIO_DIR.rglob("*") if p.is_dir()),
        key=lambda p: (len(p.relative_to(LL_PORTFOLIO_DIR).parts), p.as_posix()),
    ):
        if is_project_root(path):
            roots.append(path)
    return roots


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
    dirname_id = canonical_id_from_dirname(project_root)
    if dirname_id:
        return dirname_id
    return project_root.relative_to(LL_PORTFOLIO_DIR).as_posix()


def extract_project_type_for_root(project_root: Path, markdown_paths: List[Path]) -> str | None:
    for md_path in markdown_paths:
        if md_path.name != "PROJECT_CHARTER.md":
            continue
        project_type = extract_project_type(safe_read_text(md_path))
        if project_type in GOVERNED_PROJECT_TYPES:
            return project_type
    return infer_project_type_from_path(project_root.relative_to(LL_PORTFOLIO_DIR).as_posix())


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

        file_set = {p.name for p in markdown_paths}
        recorded_stage = None
        approval_candidates = [p for p in markdown_paths if p.name == "APPROVAL_RECORD.md"]
        if approval_candidates:
            approval_path = sorted(
                approval_candidates,
                key=lambda p: (0 if p.parent == project_root else 1, len(p.relative_to(project_root).parts), p.as_posix()),
            )[0]
            approval_text = safe_read_text(approval_path)
            recorded_stage = extract_recorded_stage(approval_text) if approval_text else None
        if recorded_stage:
            stage_label, stage_index = recorded_stage
            stage_source = "approval_record"
        else:
            stage_index = infer_stage(file_set, project_type)
            stage_label = stage_label_from_index(stage_index)
            stage_source = "artifacts"
        project_id = extract_project_id_for_root(project_root, markdown_paths)
        required_stage1 = stage1_requirements(project_type)
        required_stage2_planning = stage2_planning_requirements(project_type)
        projects.append(
            ProjectSnapshot(
                project_id=project_id,
                project_path=project_root.relative_to(LL_PORTFOLIO_DIR).as_posix(),
                project_type=project_type,
                files=file_set,
                inferred_stage=stage_index,
                stage_label=stage_label,
                stage_source=stage_source,
                missing_stage1=missing_requirements(file_set, required_stage1),
                missing_stage2_measurement=missing_requirements(file_set, REQUIRED_STAGE2_MEASUREMENT),
                missing_stage2_planning=missing_requirements(file_set, required_stage2_planning),
                missing_stage3=missing_requirements(file_set, REQUIRED_STAGE3),
                missing_stage4=missing_requirements(file_set, REQUIRED_STAGE4),
                missing_stage5=missing_requirements(file_set, REQUIRED_STAGE5),
            )
        )
    return sorted(projects, key=lambda p: (p.project_path, p.project_id))


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


def project_priority_score(project: ProjectSnapshot) -> int:
    return (
        (10 if project.project_health == "at-risk" else 0)
        + (5 if project.project_health == "watch" else 0)
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


def llm_004_outputs(projects: List[ProjectSnapshot], run_id: str) -> Dict[str, str]:
    stage_rows: List[List[str]] = []
    health_rows: List[List[str]] = []
    blocker_lines: List[str] = []
    action_rows: List[List[str]] = []

    ranked = sorted(projects, key=lambda p: (-project_priority_score(p), p.project_id))

    for p in projects:
        blocker_types = []
        if p.missing_stage1:
            blocker_types.append("stage1")
        if p.inferred_stage >= 2 and p.missing_stage2_measurement:
            blocker_types.append("measurement")
        if p.inferred_stage >= 2 and p.missing_stage2_planning:
            blocker_types.append("planning")
        if not p.approvals_present:
            blocker_types.append("approval")

        stage_rows.append(
            [
                p.project_id,
                p.stage_label,
                p.project_health,
                str(p.open_gate_count),
                f"{p.stage2_completion_pct}%" if p.inferred_stage >= 2 else "n/a",
                "yes" if p.approvals_present else "no",
                join_or_none(blocker_types),
            ]
        )

        health_rows.append(
            [
                p.project_id,
                p.project_health,
                str(p.open_gate_count),
                str(len(p.relevant_stage2_planning_gaps)),
                str(len(p.relevant_stage2_measurement_gaps)),
            ]
        )

        current_stage_missing = p.missing_for_current_stage
        blocker_lines.append(
            f"- `{p.project_id}`: stage={p.inferred_stage}, health={p.project_health}, "
            f"relevant gaps={len(current_stage_missing)} ({join_or_none(current_stage_missing)})"
        )

    for p in ranked:
        if p.inferred_stage < 2 and p.missing_stage1:
            action = "Complete the initiation packet before ML1 initiation review."
        elif p.inferred_stage < 2:
            action = "Keep the project in Initiating until ML1 authorizes Planning; draft planning artifacts remain non-authoritative."
        elif p.missing_stage2_measurement:
            action = "Complete METRICS.md and record ML1 threshold approval inside it."
        elif p.missing_stage2_planning:
            action = "Close stage-2 planning artifacts before any stage advancement."
        else:
            action = "Maintain current stage controls and prepare the next gated packet."
        if not p.approvals_present:
            action = "Record the missing ML1 approval in APPROVAL_RECORD.md."
        action_rows.append([p.project_id, str(project_priority_score(p)), action])

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
                    "Stage 2 Readiness",
                    "Approvals Present",
                    "Blocker Types",
                ],
                stage_rows or [["none", "-", "-", "-", "-", "-", "-"]],
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
        ]
    )

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
                ],
                health_rows or [["none", "-", "-", "-", "-"]],
            ),
            "",
            "## Summary",
            "",
            f"- Projects reviewed: {len(projects)}",
            f"- On-track: {sum(1 for p in projects if p.project_health == 'on-track')}",
            f"- Watch: {sum(1 for p in projects if p.project_health == 'watch')}",
            f"- At-risk: {sum(1 for p in projects if p.project_health == 'at-risk')}",
            f"- Average stage-2 readiness: "
            f"{int(round(sum((p.stage2_completion_pct for p in projects), 0) / max(len(projects), 1)))}%",
        ]
    )

    write_markdown(
        PROJECT_MGMT_DIR / "PROJECT_HEALTH_ROLLUP.md",
        run_id=run_id,
        title="Project Health Rollup",
        body=rollup_body,
    )

    top_actions = [f"- {row[0]}: {row[2]}" for row in action_rows[:3]] or ["- None."]
    report = "\n".join(
        [
            "## LLM-004 Result",
            "",
            f"- Projects reviewed: {len(projects)}",
            f"- Watch/at-risk projects: {sum(1 for p in projects if p.project_health != 'on-track')}",
            f"- Stage-2 planning gaps: {sum(len(p.missing_stage2_planning) for p in projects if p.inferred_stage >= 2)}",
            f"- Stage-2 measurement gaps: {sum(len(p.missing_stage2_measurement) for p in projects if p.inferred_stage >= 2)}",
            "",
            "## Top ML1 Actions",
            "",
            *top_actions,
            "",
            "## Outputs",
            "",
            f"- {PROJECT_MGMT_DIR / 'PROJECT_ARTIFACT_TEMPLATE.md'}",
            f"- {PROJECT_MGMT_DIR / 'PROJECT_HEALTH_ROLLUP.md'}",
        ]
    )
    return {"report": report}


def llm_005_outputs(projects: List[ProjectSnapshot], run_id: str) -> Dict[str, str]:
    stage_counts = Counter(p.inferred_stage for p in projects)
    health_counts = Counter(p.project_health for p in projects)
    stage2_projects = [p for p in projects if p.inferred_stage >= 2]
    planning_freq = missing_frequency(stage2_projects, "missing_stage2_planning")
    measurement_freq = missing_frequency(stage2_projects, "missing_stage2_measurement")

    ranked = sorted(
        projects,
        key=lambda p: (-project_priority_score(p), p.project_id),
    )

    dashboard_rows = [
        [
            p.project_id,
            p.stage_label,
            p.project_health,
            str(p.open_gate_count),
            f"{p.stage2_completion_pct}%" if p.inferred_stage >= 2 else "n/a",
        ]
        for p in projects
    ] or [["none", "-", "-", "-", "-"]]

    priority_rows = [
        [
            str(i),
            p.project_id,
            str(project_priority_score(p)),
            p.project_health,
            str(p.open_gate_count),
            (
                "Complete initiation packet"
                if p.inferred_stage < 2 and p.missing_stage1
                else "Hold in Initiating until ML1 review"
                if p.inferred_stage < 2
                else "Complete stage-2 planning packet"
                if p.missing_stage2_planning
                else "Advance to next gated artifact set"
            ),
        ]
        for i, p in enumerate(ranked, start=1)
    ] or [["-", "none", "-", "-", "-", "-"]]

    sequencing_lines: List[str] = []
    if not ranked:
        sequencing_lines.append("1. No active projects detected.")
    else:
        for i, project in enumerate(ranked[:4], start=1):
            if project.inferred_stage < 2:
                sequencing_lines.append(
                    f"{i}. `{project.project_id}` first focus: close {len(project.missing_stage1)} initiation gaps and keep planning drafts non-authoritative pending ML1 review."
                )
            else:
                sequencing_lines.append(
                    f"{i}. `{project.project_id}` first focus: close {len(project.missing_stage2_planning)} planning and "
                    f"{len(project.missing_stage2_measurement)} measurement gaps."
                )

    collisions = [p.project_id for p in projects if p.inferred_stage == 2]
    collision_artifacts = sorted(
        [name for name, count in planning_freq.items() if count >= 2],
        key=lambda n: (-planning_freq[n], n),
    )
    collision_body = "\n".join(
        [
            "## Resource Collision Signals",
            "",
            f"- Projects in planning/measurement stage: {len(collisions)}",
            f"- Potential coordination set: {', '.join(collisions) if collisions else 'none'}",
            f"- Shared missing planning artifacts (portfolio-wide): {join_or_none(collision_artifacts)}",
        ]
    )

    capacity_rows: List[List[str]] = []
    total_capacity_units = 0
    for p in projects:
        if p.inferred_stage >= 2:
            planning_gap_count = len(p.missing_stage2_planning)
            measurement_gap_count = len(p.missing_stage2_measurement)
            load_units = (planning_gap_count * 2) + (measurement_gap_count * 3)
        else:
            planning_gap_count = 0
            measurement_gap_count = 0
            load_units = len(p.missing_stage1)
        total_capacity_units += load_units
        capacity_rows.append([p.project_id, str(load_units), str(planning_gap_count), str(measurement_gap_count)])

    top_bottlenecks = planning_freq.most_common(3) + measurement_freq.most_common(2)
    bottleneck_lines = [f"- `{name}` missing in {count} project(s)." for name, count in top_bottlenecks]

    files_to_body = {
        "PORTFOLIO_STATUS_DASHBOARD.md": "\n".join(
            [
                "## Portfolio Status",
                "",
                render_table(["Project", "Stage", "Health", "Relevant Open Gates", "Stage 2 Readiness"], dashboard_rows),
                "",
                f"- Total projects: {len(projects)}",
                f"- Health mix: on-track={health_counts.get('on-track', 0)}, "
                f"watch={health_counts.get('watch', 0)}, at-risk={health_counts.get('at-risk', 0)}",
            ]
        ),
        "CAPACITY_ALLOCATION_MODEL.md": "\n".join(
            [
                "## Capacity Allocation Model (Advisory)",
                "",
                render_table(
                    ["Project", "Estimated Capacity Units", "Planning Gaps", "Measurement Gaps"],
                    capacity_rows or [["none", "-", "-", "-"]],
                ),
                "",
                f"- Stage 1 load: {stage_counts.get(1, 0)}",
                f"- Stage 2 load: {stage_counts.get(2, 0)}",
                f"- Stage 3+ load: {stage_counts.get(3, 0) + stage_counts.get(4, 0) + stage_counts.get(5, 0)}",
                f"- Total estimated capacity units to close current stage-2 gaps: {total_capacity_units}",
                "",
                "- Recommendation: prioritize Stage 2 closure to reduce planning backlog.",
            ]
        ),
        "BOTTLENECK_ANALYSIS.md": "\n".join(
            [
                "## Bottleneck Analysis",
                "",
                f"- Planning bottleneck candidates: {sum(1 for p in projects if p.missing_stage2_planning)}",
                f"- Measurement bottleneck candidates: {sum(1 for p in projects if p.missing_stage2_measurement)}",
                "",
                "## Top Portfolio Bottlenecks",
                "",
                *(bottleneck_lines or ["- None."]),
            ]
        ),
        "PROJECT_PRIORITY_MATRIX.md": "\n".join(
            [
                "## Priority Matrix",
                "",
                render_table(["Rank", "Project", "Priority Score", "Health", "Relevant Open Gates", "Next Focus"], priority_rows),
            ]
        ),
        "STAGE_DISTRIBUTION_REPORT.md": "\n".join(
            [
                "## Stage Distribution",
                "",
                render_table(
                    ["Stage", "Count"],
                    [[str(stage), str(stage_counts.get(stage, 0))] for stage in [0, 1, 2, 3, 4, 5]],
                ),
            ]
        ),
        "SEQUENCING_RECOMMENDATIONS.md": "\n".join(
            [
                "## Sequencing Recommendations",
                "",
                *sequencing_lines,
            ]
        ),
        "WIP_LOAD_ANALYSIS.md": "\n".join(
            [
                "## WIP Load Analysis",
                "",
                f"- Active projects (stage >=1): {sum(1 for p in projects if p.inferred_stage >= 1)}",
                f"- At-risk active projects: {sum(1 for p in projects if p.inferred_stage >= 1 and p.project_health == 'at-risk')}",
                f"- Watch projects: {sum(1 for p in projects if p.project_health == 'watch')}",
                f"- Portfolio planning gap total: {sum(len(p.missing_stage2_planning) for p in projects)}",
            ]
        ),
        "RESOURCE_COLLISION_REPORT.md": collision_body,
    }

    for filename, body in files_to_body.items():
        write_markdown(PORTFOLIO_MGMT_DIR / filename, filename.replace("_", " ").replace(".md", ""), run_id, body)

    report = "\n".join(
        [
            "## LLM-005 Result",
            "",
            f"- Projects reviewed: {len(projects)}",
            f"- Stage 2 concentration: {stage_counts.get(2, 0)}",
            f"- At-risk projects: {health_counts.get('at-risk', 0)}",
            f"- Planning backlog volume: {sum(len(p.missing_stage2_planning) for p in stage2_projects)}",
            f"- Measurement backlog volume: {sum(len(p.missing_stage2_measurement) for p in stage2_projects)}",
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


def llm_006_outputs(projects: List[ProjectSnapshot], run_id: str) -> Dict[str, str]:
    approval_gaps = [p for p in projects if not p.approvals_present]
    stage_violations = [p for p in projects if p.missing_for_current_stage]
    metric_schema_gaps = [p for p in projects if p.inferred_stage >= 2 and p.missing_stage2_measurement]
    planning_gaps = [p for p in projects if p.inferred_stage >= 2 and p.missing_stage2_planning]
    contradiction_alerts: List[str] = []

    seen = set()
    for p in projects:
        if p.project_id in seen:
            contradiction_alerts.append(f"Duplicate project identifier: {p.project_id}")
        seen.add(p.project_id)

    severity_counts = {"critical": 0, "high": 0, "medium": 0}
    for project in projects:
        if project.missing_stage1 or not project.approvals_present:
            severity_counts["critical"] += 1
        elif project.missing_stage2_measurement:
            severity_counts["high"] += 1
        elif project.missing_stage2_planning:
            severity_counts["medium"] += 1

    stage2_projects = [p for p in projects if p.inferred_stage >= 2]
    planning_drift_freq = missing_frequency(stage2_projects, "missing_stage2_planning")
    measurement_drift_freq = missing_frequency(stage2_projects, "missing_stage2_measurement")

    files_to_body = {
        "GOVERNANCE_COMPLIANCE_AUDIT.md": "\n".join(
            [
                "## Governance Compliance Audit",
                "",
                f"- Projects audited: {len(projects)}",
                f"- Stage violations: {len(stage_violations)}",
                f"- Approval gaps: {len(approval_gaps)}",
                f"- Metric schema gaps: {len(metric_schema_gaps)}",
                f"- Planning schema gaps: {len(planning_gaps)}",
                "",
                "## Severity Mix",
                "",
                f"- Critical: {severity_counts['critical']}",
                f"- High: {severity_counts['high']}",
                f"- Medium: {severity_counts['medium']}",
            ]
        ),
        "STAGE_GATE_VIOLATION_REPORT.md": "\n".join(
            [
                "## Stage Gate Violations",
                "",
                *(
                    [
                        f"- `{p.project_id}`: relevant missing artifacts={len(p.missing_for_current_stage)} "
                        f"({join_or_none(p.missing_for_current_stage)})"
                        for p in stage_violations
                    ]
                    or ["- None."]
                ),
            ]
        ),
        "METRIC_SCHEMA_INTEGRITY_REPORT.md": "\n".join(
            [
                "## Metric Schema Integrity",
                "",
                *(
                    [
                        f"- `{p.project_id}` missing measurement artifacts: {join_or_none(p.missing_stage2_measurement)}"
                        for p in metric_schema_gaps
                    ]
                    or ["- All projects contain required measurement artifacts."]
                ),
            ]
        ),
        "CONTRADICTION_ALERTS.md": "\n".join(
            [
                "## Contradiction Alerts",
                "",
                *(contradiction_alerts or ["- No cross-project contradictions detected by deterministic checks."]),
            ]
        ),
        "MIGRATION_VALIDATION_REPORT.md": "\n".join(
            [
                "## Migration Validation",
                "",
                "- No stage 5 project migrations detected in this run.",
                "- No migration packets found to validate in project folders.",
            ]
        ),
        "APPROVAL_GAP_REPORT.md": "\n".join(
            [
                "## Approval Gap Report",
                "",
                *(
                    [
                        f"- `{p.project_id}` missing `APPROVAL_RECORD.md`."
                        for p in approval_gaps
                    ]
                    or ["- None."]
                ),
            ]
        ),
        "DOCTRINE_DRIFT_REPORT.md": "\n".join(
            [
                "## Doctrine Drift Report",
                "",
                "- Structural drift patterns detected from repeated missing artifacts:",
                *(
                    [
                        f"- Planning drift: `{name}` missing in {count} project(s)."
                        for name, count in planning_drift_freq.most_common(5)
                    ]
                    or ["- No repeated planning drift pattern detected."]
                ),
                *(
                    [
                        f"- Measurement drift: `{name}` missing in {count} project(s)."
                        for name, count in measurement_drift_freq.most_common(3)
                    ]
                    or ["- No repeated measurement drift pattern detected."]
                ),
                "- Doctrine interpretation remains ML1 authority.",
            ]
        ),
    }

    for filename, body in files_to_body.items():
        write_markdown(
            PORTFOLIO_GOVERNANCE_DIR / filename,
            filename.replace("_", " ").replace(".md", ""),
            run_id,
            body,
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
    return {"report": report}


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

    write_markdown(run_root / "LLM-004_PROJECT_MANAGEMENT_REPORT.md", "LLM-004 Project Management Report", run_id, llm_004_report)
    write_markdown(run_root / "LLM-005_PORTFOLIO_MANAGEMENT_REPORT.md", "LLM-005 Portfolio Management Report", run_id, llm_005_report)
    write_markdown(run_root / "LLM-006_PORTFOLIO_GOVERNANCE_REPORT.md", "LLM-006 Portfolio Governance Report", run_id, llm_006_report)


def main() -> int:
    run_id = generate_run_id()
    run_root = REPO_ROOT / "06_RUNS" / run_id / "ll_portfolio_agents"

    projects = discover_projects()

    llm_004 = llm_004_outputs(projects, run_id)
    llm_005 = llm_005_outputs(projects, run_id)
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
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
