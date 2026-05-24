---
id: POL-063
title: Project Risk Artifact Lifecycle Policy
owner: ML1
status: approved
approved_by: ML1
approved_date: 2026-04-18
version: 1.0
effective_date: 2026-04-18
supersedes:
provenance:
  decided_by: ML1
  decided_on: 2026-04-18
  context: Metadata normalized by system admin cleanup on 2026-05-24
created_date: 2026-03-08
last_updated: 2026-03-23
tags: [policy, risk]
---

# POL-063 - PROJECT RISK ARTIFACT LIFECYCLE POLICY

## 1. Scope

This policy governs required risk artifacts across project lifecycle stages and gate-review requirements for project work.

This policy applies to:
- Strategic projects
- Management projects
- Operational projects
- Decision projects

This policy does not apply to legal matters.

## 2. Required Lifecycle Artifacts

### Stage 1 - Initiating: `RISK_SCAN.md`

Purpose: Capture top risks and key assumptions before committing to the project.

Required schema:
```md
## Top 5 Risks
1. <Risk description>
2.
3.
4.
5.

## Key Assumptions
- <Assumption underpinning the project>

## Go / No-Go Judgment
Decision: [Proceed | Do Not Proceed | Proceed with Conditions]
Rationale: <ML1 judgment - must be explicit, not inferred>
```

Category rule:
- `RISK_SCAN.md` may remain plain-language.
- Each listed risk must still be classifiable under an allowed canonical category for that project type.
- Operational projects: each risk must classify as `Scope`, `Schedule`, or `Budget`.
- Strategic, management, and decision projects: each risk must classify as `Scope`, `Schedule`, `Budget`, `Financial`, or `Strategic`.

### Stage 2 - Planning: `RISK_REGISTER.md`

Purpose: Decompose risks by category with likelihood, impact, and mitigation.

Required schema:
```md
| Risk | Category | Likelihood | Impact | Mitigation |
|------|----------|------------|--------|------------|
| <description> | Scope / Schedule / Budget | H / M / L | H / M / L | <action> |
```

Category rule:
- `RISK_REGISTER.md` must contain an explicit `Category` field.
- Each risk row must be assigned exactly one canonical category.
- Multi-axis risks must be decomposed into separate rows.

### Stage 3 - Executing: `ISSUE_LOG.md`

Purpose: Track risks that materialized as issues during active execution, including intensified monitoring while work is underway.

Required schema:
```md
| Risk | Issue | Cause | Action |
|------|-------|-------|--------|
| <original risk from RISK_SCAN or RISK_REGISTER> | <what materialized> | <root cause> | <resolution step> |
```

### Stage 4 - Closing: `LESSONS_LEARNED.md`

Purpose: Capture durable risk and control learning for future projects.

Required schema:
```md
## What Worked
- <bullet>

## What Failed
- <bullet>

## What Should Change Next Time
- <bullet>
```

## 3. Stage-Gate Review Requirement

All four artifacts require ML1 review before a stage gate is closed.

ML2 may draft and structure artifacts; ML1 decides gate closure.

## 4. Artifact Obligations by Work Type

| Artifact | Strategic Project | Management Project | Operational Project | Decision Project | Legal Matter |
|---|:---:|:---:|:---:|:---:|:---:|
| `RISK_SCAN.md` (Initiating) | ✓ | ✓ | ✓ | ✓ | - |
| `RISK_REGISTER.md` (Planning) | ✓ | ✓ | ✓ | ✓ | - |
| `ISSUE_LOG.md` (Executing) | ✓ | ✓ | ✓ | ✓ | - |
| `LESSONS_LEARNED.md` (Closing) | ✓ | ✓ | ✓ | ✓ | - |

Legal matters carry no project risk artifacts under this policy.

## 5. Category Axis Requirement by Work Type

`RISK_REGISTER.md` must use:
- Strategic, management, and decision projects: Scope / Schedule / Budget / Financial / Strategic
- Operational projects: Scope / Schedule / Budget

## 6. Deprecated Risk Artifacts

- `RISKS_INITIAL.md` is non-canonical and deprecated.
- Existing `RISKS_INITIAL.md` files must be reconciled into canonical lifecycle artifacts.
- Legacy labels such as `Primary`, `Control`, `Execution`, `Governance`, and `Residual` must not be used as substitute category systems going forward.

## 7. Related Doctrine

- `01_DOCTRINE/01_INVARIANTS/INV-0013-risk-model.md`
- `01_DOCTRINE/01_INVARIANTS/INV-0014-risk-classification-invariants.md`
- `01_DOCTRINE/02_PRINCIPLES/PRN-013_Risk_Lifecycle_Governance.md`
- `01_DOCTRINE/03_POLICIES/POL-064_Levine_Law_Initiative_Risk_Policy.md`
- `01_DOCTRINE/03_POLICIES/POL-065_Matthew_Holdings_Initiative_Risk_Policy.md`
