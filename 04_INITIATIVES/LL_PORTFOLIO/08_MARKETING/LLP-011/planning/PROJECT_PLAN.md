---
id: llp-011_funnel1_management__planning__workplan
title: LLP-011 Planning Workplan
owner: ML1
status: draft
created_date: 2026-03-08
last_updated: 2026-03-14
tags: [llp-011, marketing, funnel1, planning, workplan]
---

# Workplan

Project ID: LLP-011
Project Path: 08_MARKETING/LLP-011
Stage: Planning

## Execution Objective
Use the Planning stage to mobilize immediate execution of Funnel 01 across the full lifecycle:
`lead_captured -> screened -> booked -> consult_complete -> retained`.

## Execution Workstreams

| Workstream | Scope | Primary Owner | Outputs |
| --- | --- | --- | --- |
| WS-01 Lifecycle Controls | Lock execution boundaries and stage-entry/exit controls for the full funnel lifecycle | ML1 + CMO Agent | `SCOPE_STATEMENT.md`, `ASSUMPTIONS_CONSTRAINTS.md` |
| WS-02 Channel and Intake Operations | Confirm Google Ads -> GHL pathway, qualification controls, and dependency safeguards | CMO Agent | `DEPENDENCIES.md`, `RISK_REGISTER.md` |
| WS-03 Conversion Operations | Define execution controls for booked -> consult_complete -> retained progression | Marketing Strategy Agent + CMO Agent | `COMMUNICATION_PLAN.md`, updated conversion controls in execution-readiness artifacts |
| WS-04 KPI Activation | Finalize KPI formulas, baseline method, and validation logic for execution monitoring | Market Signal Agent + CMO Agent | `METRIC_DEFINITION.md`, `MEASUREMENT_METHOD.md`, `BASELINE_CAPTURE_PERIOD.md`, `VALIDATION_REVIEW.md` |
| WS-05 Execution Gate | Prepare and submit the Planning -> Executing authorization packet | CMO Agent | `ML1_METRIC_APPROVAL.md`, updated `APPROVAL_RECORD.md` |

## Execution Sequence
1. Freeze lifecycle controls and execution boundaries.
2. Confirm channel/intake dependencies and risk controls.
3. Finalize KPI activation package (formulas, baseline, validation).
4. Submit Planning -> Executing gate packet for ML1 decision.
5. On ML1 approval, start execution under approved controls.

## Milestones

| Milestone | Target Date | Status | Evidence |
| --- | --- | --- | --- |
| M1 - Initiating stage approved and project advanced to Planning | 2026-03-08 | complete | `APPROVAL_RECORD.md` |
| M2 - Planning scope package completed | 2026-03-10 | planned | `SCOPE_STATEMENT.md`, `ASSUMPTIONS_CONSTRAINTS.md` |
| M3 - Risk/dependency package completed | 2026-03-11 | planned | `RISK_REGISTER.md`, `DEPENDENCIES.md` |
| M4 - Measurement package completed | 2026-03-12 | planned | `METRIC_DEFINITION.md`, `MEASUREMENT_METHOD.md`, `VALIDATION_REVIEW.md` |
| M5 - Baseline period approved for execution | 2026-03-13 | planned | `BASELINE_CAPTURE_PERIOD.md`, `ML1_METRIC_APPROVAL.md` |
| M6 - Planning gate packet submitted to ML1 | 2026-03-14 | planned | Updated `APPROVAL_RECORD.md` |

Notes:
- Dates are execution-mobilization targets and can be adjusted only through ML1-approved changes.

## Resource Plan

### Human / Agent Roles

| Role | Responsibility |
| --- | --- |
| ML1 | Final authority for approvals, thresholds, and stage advancement |
| CMO Agent | Execution mobilization orchestration and gate packet assembly |
| Marketing Strategy Agent | Lifecycle execution alignment and conversion-control design |
| Content Production Agent | Execution asset readiness for approved messaging |
| Editorial QA Agent | Execution QA controls for publishable assets |
| Distribution Orchestration Agent | Channel execution sequencing for approved assets |
| Market Signal Agent | KPI activation and execution monitoring design |
| Repository / Asset Governance Agent | Artifact state/provenance controls during execution rollout |

### Systems / Tools
- Google Ads (acquisition channel)
- Go High Level (intake and scheduling flow)
- ML2-governed repository artifacts for doctrine and funnel specifications

### Capacity Notes
- Execution may proceed only after explicit ML1 Planning -> Executing approval.
- No expanded channel spend or material funnel reconfiguration is authorized without ML1 approval.
- If lifecycle execution cannot stay within defined boundaries, escalate instead of broadening scope.

## Completion Condition
Workplan is complete when execution mobilization artifacts are complete, internally aligned, and approved for Planning -> Executing gate decision by ML1.

---

## Stage 2 — Funnel 1 Future State (Planning Horizon, Not Yet Authorized)

These items represent the planned evolution of Funnel 01 beyond the current execution scope. They are in-scope for planning-stage design but require a separate ML1 authorization before execution begins. They do not modify the current Stage 1 execution scope.

### S2-WS-01 — Intake Gate Hardwiring

**Problem**: The GHL qualification questionnaire exists but is not being sent consistently. Leads are entering the funnel without passing the ICP-01 filter.

**Task**: Hardwire the qualification questions directly into the opt-in / booking button on the F01 landing page so the gate cannot be bypassed. Questions:
1. Business annual revenue (disqualify < $1M)
2. Number of employees (disqualify < 5)
3. Whether they work with an accountant (disqualify if no)

**Why Stage 2**: Configuration change to live GHL flow. Requires ML1 sign-off on disqualification thresholds before implementation.

### S2-WS-02 — Lead Magnet for All Leads

**Scope**: All F01 leads receive a lead magnet at intake — prior to or concurrent with consult booking. The lead magnet serves two purposes: (1) filters for ICP-01 by topic specificity (operators who download a governance or structuring guide self-select as the right audience), and (2) warms leads who don't immediately book.

**Requirements**:
- Lead magnet topic must align with Structuring keyword cluster (e.g., shareholder governance checklist, executive compensation overview, corporate structure review guide) — not a generic legal resource
- Delivered automatically via GHL on opt-in
- ML1 must approve content before deployment

**Why Stage 2**: Lead magnet must be created and approved before GHL automation can be configured.

### S2-WS-03 — Structuring Keywords Added to Google Ads

**Scope**: Add Structuring keyword cluster to the F01 Google Ads campaign alongside existing reactive keywords. Target keywords to include candidates from the LLP-025 SEO research (e.g., "shareholder agreement review Ontario," "executive compensation lawyer Toronto," "corporate governance review Ontario").

**Rationale**: Current F01 keyword "toronto corporate lawyer" attracts reactive, crisis-driven leads. Structuring keywords attract operators building governance systems — closer to ICP-01. This does not replace the current campaign; it supplements it with higher-fit traffic.

**Requirements**:
- Keyword shortlist approved by ML1 (delegated to SEO Metrics Master Agent for research; ML1 approves final list)
- Separate ad group or campaign to isolate Structuring traffic for measurement
- Conversion tracking for Structuring keywords must be confirmed before spend is allocated

**Why Stage 2**: Requires keyword research output from LLP-025 WS-05 / IMP-05 before implementation.

### S2-WS-04 — Setter Role

**Scope**: Add a setter to the F01 intake and booking flow. The setter handles:
- Initial lead qualification follow-up
- Consult booking and confirmation
- Pre-consult screening and no-show reduction
- Handoff to ML1 for consult

**Rationale**: Currently ML1 handles all intake operations. A setter frees ML1 capacity for legal work and improves contact rates at the Lead → Consult stage (currently the primary drop-off point at 70–75% of leads not booking).

**Requirements**:
- Setter role definition: scope, script, qualification authority, escalation triggers
- Compensation model (ML1 to define)
- GHL workflow updated for setter hand-off
- ML1 retains decision authority on all retentions

**Why Stage 2**: Staffing decision requiring ML1 approval. Cannot be activated without role definition and compensation model.

### S2-WS-05 — Senior Lawyer Delivery

**Scope**: Add a senior lawyer to handle matter delivery for F01 retained clients. ML1 retains client relationship and strategic oversight; senior lawyer handles execution.

**Rationale**: As F01 volume grows (and as F02 and F03 add intake), ML1 delivery capacity becomes the constraint. A senior lawyer on delivery extends capacity without compromising relationship or oversight quality.

**Requirements**:
- Role definition: matter types in scope, supervision model, ML1 handoff protocol
- Compensation and engagement model (ML1 to define)
- Matter type eligibility list (which F01 matters are appropriate for delegation)
- QA and oversight process

**Why Stage 2**: Staffing decision requiring ML1 approval and matter-type eligibility scoping before any delegation occurs.

### Stage 2 Gate Criteria

Stage 2 work may not begin until:
- Stage 1 (current execution) is authorized and operational
- ML1 provides explicit Stage 2 authorization
- Each workstream above has a separate ML1-approved scope before execution
