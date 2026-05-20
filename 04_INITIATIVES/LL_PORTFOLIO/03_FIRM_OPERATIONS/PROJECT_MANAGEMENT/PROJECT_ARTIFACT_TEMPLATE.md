---
id: 04_initiatives__ll_portfolio__03_firm_operations__project_management__project_artifact_template_md
title: Project Artifact Template
owner: ML1
status: draft
created_date: 2026-03-08
last_updated: 2026-03-19
tags: [project-management, stage-gates, artifacts, template]
---

# Project Artifact Template

Governing Project ID: `LLP-043`
Project Path: `03_FIRM_OPERATIONS/PROJECT_MANAGEMENT`

## Purpose

Local LL implementation guide for the doctrine-defined project artifact set.

This template is subordinate to
`01_DOCTRINE/03_POLICIES/POL-055_Repository_Project_Policy.md`,
`01_DOCTRINE/03_POLICIES/POL-056_Firm_Project_Policy.md`, and
`01_DOCTRINE/03_POLICIES/POL-073_Project_Management_Control_Policy.md`.

Planning-stage artifacts are execution-readiness controls used to authorize execution and achievement of project goals.

## Project Types

This template acknowledges five LL work types:
- Strategic projects
- Management projects
- Operational projects
- Decision projects
- Client matters (aka client projects)

Applicability:
- The staged project artifact lifecycle in this template applies to strategic,
  management, operational, and decision projects.
- Client matters/client projects are governed by matter doctrine and matter-stage artifacts, not this project-stage lifecycle template.

## Stage 1 - Initiating

Required (all projects):
- `PROJECT_CHARTER.md`
- `PROBLEM_STATEMENT.md`
- `SUCCESS_CRITERIA.md`
- `STAKEHOLDERS.md`
- `RISK_SCAN.md`
- `APPROVAL_RECORD.md`

Required (strategic projects only):
- `BUSINESS_CASE.md`

Notes:
- `RISK_SCAN.md` must include: Top 5 Risks, Key Assumptions, Go/No-Go Judgment.
- `PROJECT_CHARTER.md` must include:
  - `Project ID` (canonical globally unique identifier, e.g., `LLP-024`)
  - `Project Path` (repository path key, e.g., `08_MARKETING/LLP-024`)
  - `Project Type` (`Strategic`, `Management`, `Operational`, or `Decision`)
- Stage advancement requires ML1 approval in `APPROVAL_RECORD.md`.

Identity Rule:
- Project ID is the folder name.
- New LL project folders use plain `LLP-NNN` (e.g. `LLP-024`).
- Project ID and folder name are identical. They are the same thing.
- The folder number is globally unique across the entire LL Portfolio — not per-area.
- The deprecated LLP-26-XX registry format (year-prefixed) must not be used in any new or existing project artifact.
- New `LLP-NNN_NAME` folders must not be created.
- Existing `LLP-NNN_NAME` folders are migration residue and should be
  normalized under `POL-073`.
- When a new project is created, check the full portfolio folder list to confirm the chosen number is unused before creating the folder.

## Stage 2 - Planning (Execution Readiness)

Purpose:
- Lock the execution-ready shape of the specific project.
- Reduce uncertainty before execution.
- Prepare a clean ML1 gate decision.

Anti-Bloat Rule:
- Planning artifacts exist to support execution authorization, not planning for the sake of planning.
- If an artifact does not help lock scope, confirm dependencies, reduce risk, define controls, or support the gate decision, merge it or remove it.
- Planning artifacts must use project-specific language. Avoid generic PM boilerplate that could apply to any project.

### Core Planning
Required for strategic and management projects:
- `SCOPE_STATEMENT.md`
- `PROJECT_PLAN.md` (must include workstreams, execution sequence, milestones, resource plan, completion condition; legacy `WORKPLAN.md` remains acceptable during transition)
- `ASSUMPTIONS_CONSTRAINTS.md`
- `DEPENDENCIES.md`
- `RISK_REGISTER.md`
- `COMMUNICATION_PLAN.md`

Required for operational projects:
- `SCOPE_STATEMENT.md`
- `PROJECT_PLAN.md` (must include workstreams, execution sequence, milestones, resource plan, completion condition; legacy `WORKPLAN.md` remains acceptable during transition)
- `DEPENDENCIES.md`
- `RISK_REGISTER.md`

Optional for operational projects, when the project actually needs them:
- `ASSUMPTIONS_CONSTRAINTS.md`
- `COMMUNICATION_PLAN.md`

Required for decision projects:
- `DECISION_FRAME.md`
- `PROJECT_PLAN.md`
- `ASSUMPTIONS_CONSTRAINTS.md`
- `DEPENDENCIES.md`
- `RISK_REGISTER.md`

### Measurement Architecture
Required:
- `METRICS.md`

**DEPRECATED — do not create these files:**
- `METRIC_DEFINITION.md` — non-compliant; content belongs in `METRICS.md`
- `MEASUREMENT_METHOD.md` — non-compliant; content belongs in `METRICS.md`
- `BASELINE_CAPTURE_PERIOD.md` — non-compliant; content belongs in `METRICS.md`
- `VALIDATION_REVIEW.md` — non-compliant; content belongs in `METRICS.md`
- `ML1_METRIC_APPROVAL.md` — non-compliant; ML1 threshold approval is recorded inside `METRICS.md`, not in a separate file

Any project that has these files must consolidate them into `METRICS.md` before the Planning→Executing gate is closed. Any agent, playbook, or process that scaffolds these files for a new project is in violation of this template.

Notes:
- `METRICS.md` is the single canonical measurement document. It must contain: metric definitions, measurement method, baseline capture period, validation review criteria, and ML1 threshold approval.
- Executing must not begin until ML1 approves Planning→Executing in `APPROVAL_RECORD.md` and threshold approval is recorded in `METRICS.md`.

Best-Practice Rules:
- `SCOPE_STATEMENT.md`
  Must define the real execution boundary for the project, including explicit exclusions.
- `PROJECT_PLAN.md`
  Must focus on the project decisions that still need to be locked for execution. It must not become a generic project-management report.
- `ASSUMPTIONS_CONSTRAINTS.md`
  Must state the assumptions the project is relying on and the hard limits it cannot cross.
- `DEPENDENCIES.md`
  Must list only dependencies that could block or materially change execution.
- `RISK_REGISTER.md`
  Must focus on risks that threaten the actual project thesis, including scope,
  schedule, budget, operating control, authorization readiness, or other
  doctrine-aligned project risks.
- `COMMUNICATION_PLAN.md`
  Must be limited to decision loops, coordination points, and escalation triggers that the project actually needs. It is expected by default for strategic and management projects and optional for operational projects unless coordination complexity warrants it.
- `METRICS.md`
  Must be the single source for metric definitions, calculation method, baseline logic, validation rules, and ML1 threshold approval.
- Decision projects should use the lightest planning packet that still supports
  the specific ML1 decision at issue.
## Stage 3 - Executing

Required:
- `EXECUTION_LOG.md`
- `DECISION_LOG.md`
- `CHANGE_LOG.md`
- `ISSUE_LOG.md`
- `DELIVERABLES_TRACKER.md`
- `QA_CHECKLIST.md`
- `STATUS_REPORT.md`
- `KPI_DASHBOARD.md`
- `VARIANCE_REPORT.md`
- `RISK_UPDATES.md`
- `STAKEHOLDER_UPDATES.md`

Notes:
- `ISSUE_LOG.md` tracks materialized risks and corrective actions.
- Executing includes active implementation plus increased monitoring while the work is live.

## Stage 4 - Closing

Required:
- `DELIVERABLE_ACCEPTANCE.md`
- `LESSONS_LEARNED.md`
- `POST_EXECUTION_REVIEW.md`
- `FINAL_STATUS_REPORT.md`
- `ARCHIVE_INDEX.md`

## Stage-Gate Rule

No stage advancement is valid without explicit ML1 approval recorded in project artifacts.

## Control-Layer Rule

This template is a local LL implementation guide. It is not itself canonical
doctrine. If it conflicts with doctrine, doctrine governs.
