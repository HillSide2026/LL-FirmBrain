---
id: 04_initiatives__ll_portfolio__07_strategic_projects__llp_031_corporate_entity_management__first_run_corporate_solutions_artifact_opinion_md
title: First-Run Corporate Solutions — Stage Artifact Opinion
owner: ML1
status: draft
created_date: 2026-02-28
last_updated: 2026-02-28
tags: [corporate, solutions, first-run, stage-gates, artifacts]
---

# First-Run Corporate Solutions — Stage Artifact Opinion

## Purpose

Joint review and opinion using:
- Corporate Practice-Area Master lens (substantive completeness, decision discipline, artifact quality)
- LLM-004 Project Management lens (stage-gate completeness, approval discipline, measurement architecture)

This is a non-authoritative working artifact for ML1 review.

## Sources Applied

- `02_PLAYBOOKS/CORPORATE/AGENTS/CORPORATE_LAW_MASTER_AGENT.md`
- `02_PLAYBOOKS/CORPORATE/SOLUTIONS/`
- `00_SYSTEM/AGENTS/LLM-004_LLP-043_AGENT.md`
- `01_DOCTRINE/03_POLICIES/POL-056_Firm_Project_Policy.md`
- `01_DOCTRINE/03_POLICIES/POL-053_Matter_Solutions.md`
- `00_SYSTEM/schemas/SCHEMAS_SOLUTIONS.md`

## High-Confidence Findings

1. Stage-gate required artifact sets are explicit and complete at the project doctrine level (Stages 1-5).
2. Corporate solution tiering for Run 1 is:
- Tier 1: `INCORPORATION`, `SHAREHOLDER_AGREEMENT`, `SHAREHOLDER_CHANGE`
- Tier 2: `BUSINESS_ACQUISITION`, `SHAREHOLDER_CONFLICT`
3. Naming/governance mismatch to resolve:
- `CRISIS_ADVISORY` should remain a Solution
- `CORPORATE_ADVISORY` and `FRACTIONAL_COUNSEL` should be Strategies (not Solutions)
4. First run should be executed as a controlled pilot with Tier 1 only.

## First-Run Scope Opinion

### Include in Run 1
- Tier 1 only: `INCORPORATION`, `SHAREHOLDER_AGREEMENT`, `SHAREHOLDER_CHANGE`

### Exclude from Run 1 (until upgraded)
- Tier 2: `BUSINESS_ACQUISITION`, `SHAREHOLDER_CONFLICT`

### Hold Pending Naming/Authority Decision
- Reclassify `CORPORATE_ADVISORY` and `FRACTIONAL_COUNSEL` as Strategies
- Keep `CRISIS_ADVISORY` as Solution

## Stage Artifact Matrix (Project Stages 1-5)

## Stage 1 — Initiation

### Doctrine-mandatory
- `PROJECT_CHARTER.md`
- `PROBLEM_STATEMENT.md`
- `SUCCESS_CRITERIA.md`
- `STAKEHOLDERS.md`
- `RISK_SCAN.md`
- `APPROVAL_RECORD.md`

### Corporate first-run additions (recommended)
- `FIRST_RUN_SOLUTION_SCOPE.md` (explicit include/exclude list above)
- `SOLUTION_NAMING_ALIGNMENT_DECISION.md` (resolve advisory naming mismatch)
- `SOLUTION_MATURITY_BASELINE.md` (per-solution readiness score and blockers)

## Stage 2 — Planning

### Doctrine-mandatory planning
- `SCOPE_STATEMENT.md`
- `WORKPLAN.md` (includes milestone schedule and resource plan sections)
- `ASSUMPTIONS_CONSTRAINTS.md`
- `DEPENDENCIES.md`
- `RISK_REGISTER.md`
- `COMMUNICATION_PLAN.md`

### Doctrine-mandatory measurement architecture
- `METRICS.md`

### Corporate first-run additions (recommended)
- `SOLUTION_PACKET_COMPLETENESS_MATRIX.md` (README/SCOPE/ASSEMBLY/ARTIFACTS/RISK completeness)
- `DECISION_REGISTRY_COVERAGE_MAP.md` (D01-D07 mapped to each in-scope solution)
- `INTAKE_MINIMUM_FACT_SET.md` (fact minimums before drafting)
- `STAGE_GATE_DEFINITION_BY_SOLUTION.md` (what done looks like per solution packet)

## Stage 3 — Implementation

### Doctrine-mandatory
- `EXECUTION_LOG.md`
- `DECISION_LOG.md`
- `CHANGE_LOG.md`
- `ISSUE_LOG.md`
- `DELIVERABLES_TRACKER.md`
- `QA_CHECKLIST.md`

### Corporate first-run additions (recommended)
- `ARTIFACT_REQUEST_LISTS.md` (required client/internal documents by solution)
- `OUTPUT_SCHEMA_COMPLIANCE_CHECKLIST.md` (Matter Classification, Decisions, Assumptions, Plan, Risks, Escalations, Artifacts)
- `ESCALATION_CASEBOOK.md` (all triggered escalations with disposition status)
- `SOLUTION_COLLISION_CASES.md` (if multi-solution sequencing appears)

## Stage 4 — Monitoring

### Doctrine-mandatory
- `STATUS_REPORT.md`
- `KPI_DASHBOARD.md`
- `VARIANCE_REPORT.md`
- `RISK_UPDATES.md`
- `STAKEHOLDER_UPDATES.md`

### Corporate first-run additions (recommended)
- `QUALITY_DRIFT_REPORT.md` (template drift, missing sections, incomplete artifact packets)
- `ESCALATION_METRICS.md` (trigger frequency, resolution time, reopened decisions)
- `REWORK_METRICS.md` (redraft cycles and root causes)

## Stage 5 — Closing

### Doctrine-mandatory
- `DELIVERABLE_ACCEPTANCE.md`
- `LESSONS_LEARNED.md`
- `POST_IMPLEMENTATION_REVIEW.md`
- `FINAL_STATUS_REPORT.md`
- `ARCHIVE_INDEX.md`

### Corporate first-run additions (recommended)
- `SOLUTION_READINESS_VERDICT.md` (Ready / Hold / Refactor per corporate solution)
- `PROMOTION_CANDIDATE_PACKET.md` (what can migrate to authoritative layers)
- `RESIDUAL_RISK_REGISTER.md` (known unresolved risks and owners)

## Operational Overlay: Matter-Solution Lifecycle Artifacts (9 Stages)

The project stages above govern initiative delivery. In parallel, matter execution should track minimum artifacts for each `solution_stage`.

1. `identified`:
- `SOLUTION_INTAKE_SNAPSHOT.md`
- `PRELIM_CLASSIFICATION.md`

2. `scoped`:
- `SOLUTION_SCOPE_MEMO.md`
- `FEE_MODEL_AND_ESTIMATE.md`
- `ASSUMPTION_LOG.md`

3. `approved`:
- `CLIENT_AUTHORIZATION_RECORD.md`
- `SOLUTION_STAGE_CHANGE_LOG.md`

4. `in_production`:
- `WORKING_DRAFT_PACKET_INDEX.md`
- `OPEN_QUESTIONS_AND_GAPS.md`

5. `client_review`:
- `CLIENT_REVIEW_PACKET.md`
- `FEEDBACK_LOG.md`

6. `awaiting_external`:
- `EXTERNAL_DEPENDENCY_LOG.md`
- `DEADLINE_AND_BLOCKER_TRACKER.md`

7. `delivered`:
- `DELIVERY_CONFIRMATION.md`
- `FINAL_ARTIFACT_INDEX.md`

8. `billed`:
- `INVOICE_RECORD.md`
- `BILLING_RECONCILIATION_NOTE.md`

9. `collected`:
- `PAYMENT_CONFIRMATION.md`
- `SOLUTION_CLOSEOUT_NOTE.md`

## ML1 Decisions Needed Before Run 1

1. Approve tier model: Tier 1 (`INCORPORATION`, `SHAREHOLDER_AGREEMENT`, `SHAREHOLDER_CHANGE`); Tier 2 (`BUSINESS_ACQUISITION`, `SHAREHOLDER_CONFLICT`).
2. Approve first-run scope as Tier 1 only.
3. Approve naming alignment: `CRISIS_ADVISORY` stays Solution; `CORPORATE_ADVISORY` and `FRACTIONAL_COUNSEL` are Strategies.
4. Approve Stage 2 planning expansion artifacts listed above.
5. Approve measurement set for first-run quality and throughput.
