---
id: POL-073
title: Project Management Control Policy
owner: ML1
status: approved
approved_by: ML1
approved_date: 2026-05-19
version: '1.0'
created_date: 2026-05-19
last_updated: 2026-05-19
tags: [doctrine, policy, project-management, controls, conformance]
---

# Project Management Control Policy

## 1. Purpose

This policy defines the doctrine-side project-management control suite for the
repository.

It operationalizes the repo-level project policy by making the PM control layer
explicit for:

- identity
- stage vocabulary
- planning baselines
- metric governance
- portfolio health states
- sequencing logic
- work-in-progress discipline
- matter-to-project prioritization
- automation conformance

## 2. Scope

This policy applies to all governed project-management structures that monitor,
report on, sequence, or audit repo-governed projects, including:

- LL project-management artifacts and agent outputs
- HillSide project-management artifacts and agent outputs
- PM templates, rollups, dashboards, and audit packets outside doctrine
- deterministic runners or agents that assess project state

This policy does not replace project-stage artifact requirements defined in
`POL-055`. It governs the control layer that interprets and enforces them.

## 3. Policy Hierarchy

This policy is subordinate to:

- `01_DOCTRINE/01_INVARIANTS/INV-0012-project-structural-boundaries.md`
- `01_DOCTRINE/01_INVARIANTS/INV-0018-canonical-project-types.md`
- `01_DOCTRINE/03_POLICIES/POL-055_Repository_Project_Policy.md`

Subsidiary project policies such as `POL-056` and `POL-072` must apply this
control policy where they define local PM behavior.

## 4. Authoritative Control Surfaces

Doctrine-level PM controls must live in `01_DOCTRINE/`.

Rules:

- Project-management doctrine may not be made canonical by a README, template,
  register, or agent file outside `01_DOCTRINE/`.
- Operational files outside `01_DOCTRINE/` may explain, mirror, or implement
  doctrine, but they are subordinate working surfaces only.
- If an operational PM artifact outside doctrine conflicts with doctrine, the
  doctrine artifact governs.
- Local PM files outside doctrine should prefer pointing to doctrine over
  restating a parallel local rulebook.

## 5. Identity Control Rule

Project identity is controlled as follows:

- `Project ID` equals the project folder name.
- The folder name is therefore the canonical identity string used in rollups,
  approvals, cross-references, and dependency declarations.
- A project may not carry one declared `Project ID` while residing in a
  differently named project folder.
- Project-identity uniqueness is repository-wide, not portfolio-local.

### 5a. LL Application

For Levine Law, the canonical target format is `LLP-NNN`.

Rules:

- New LL project folders must be created as `LLP-NNN`, not `LLP-NNN_NAME`.
- Existing folders using the legacy suffixed pattern `LLP-NNN_NAME` are
  non-canonical migration residue.
- A legacy suffixed folder may remain readable during transition, but it fails
  PM conformance until normalized.

### 5b. Legacy Folder Migration Rule

When normalizing an existing `LLP-NNN_NAME` folder:

1. Rename the project folder to the canonical target ID (for example
   `LLP-037_LL_SYSTEM_DESIGN` -> `LLP-037`).
2. Update `PROJECT_CHARTER.md`, `APPROVAL_RECORD.md`, and any other project
   packet artifacts so `Project ID` exactly matches the new folder name.
3. Update references in registers, dependency files, dashboards, READMEs, and
   automation outputs that mention the prior folder slug.
4. Record the migration in the relevant change or migration validation surface.

No new suffixed project folder may be created after adoption of this policy.

## 6. Stage Vocabulary Control Rule

The canonical delivery stages remain:

1. `Initiating`
2. `Planning`
3. `Executing`
4. `Closing`

Rules:

- `Implementation` is a deprecated stage label.
- `Monitoring` is a deprecated stage label.
- `Executing` is the only canonical stage that covers both active
  implementation and live monitoring/reporting activity.
- New PM dashboards, templates, and automation must not present
  `Implementation` or `Monitoring` as canonical stage names.
- Legacy `implementation/` and `monitoring/` folders may remain readable during
  migration, but they are conformance failures until normalized.

## 7. Planning Baseline Control Rule

Planning control is governed as follows:

- The required planning baseline by project type is defined in `POL-055`.
- `PROJECT_PLAN.md` is the canonical planning-sequence artifact.
- `WORKPLAN.md` is legacy residue and must not be created for new work.
- `METRICS.md` is the single canonical measurement artifact.
- The split measurement schema
  (`METRIC_DEFINITION.md`, `MEASUREMENT_METHOD.md`,
  `BASELINE_CAPTURE_PERIOD.md`, `VALIDATION_REVIEW.md`) is retired.
- `ML1_METRIC_APPROVAL.md` is retired. Threshold approval belongs inside
  `METRICS.md`.
- `POST_EXECUTION_REVIEW.md` is the canonical closing review artifact name.

Legacy filenames may remain readable during migration, but they fail PM
conformance until normalized.

## 8. Portfolio Health State Rule

The PM control layer uses four health states:

- `on-track`
- `watch`
- `at-risk`
- `non-conformant`

Rules:

- `on-track` may be used only when the current stage requirements are satisfied,
  required approvals are present, and there are no PM conformance failures.
- `watch` may be used when the packet is structurally valid but has non-fatal
  current-stage gaps.
- `at-risk` may be used when Stage 1 integrity, approvals, or critical control
  artifacts are missing.
- `non-conformant` must be used when the project or control surface violates
  identity, stage-vocabulary, retired-artifact, or authority-surface rules.

A packet or control surface must not be reported as `on-track` if it is still
explicitly marked `READ-ONLY`, `Not yet reviewed`, or otherwise not yet fit to
serve as an authoritative PM control surface.

## 9. Sequencing and WIP Control Rule

Portfolio sequencing must prefer control closure over uncontrolled expansion.

Rules:

- Closing open gate requirements outranks opening new discretionary internal
  project work.
- Dependency-unlocking projects may be prioritized ahead of lower-leverage
  projects.
- Stage-2 concentration is a portfolio risk signal and should be actively
  managed, not ignored.
- WIP should be constrained when ML1 approval load, planning backlog, or
  governance drift is already elevated.
- A PM system should prefer fewer governed projects with cleaner packets over a
  larger volume of partially governed work.

## 10. Matter-to-Project Prioritization Rule

LL matter pressure is a first-order sequencing input.

Rules:

- Active `essential` and `strategic` matters outrank discretionary internal
  project acceleration unless ML1 decides otherwise.
- Internal projects that directly unblock active matter delivery may be
  prioritized ahead of other internal work.
- In the absence of an explicit matter-support linkage, assume matter delivery
  has priority over discretionary project expansion.
- Matter-aware PM outputs should at minimum surface the current active
  essential/strategic matter load when making sequencing recommendations.

Related matter doctrine remains governed by:

- `01_DOCTRINE/03_POLICIES/POL-070_Backlog_Routing_Policy.md`
- `01_DOCTRINE/03_POLICIES/POL-071_Matter_Delivery_Stage_Policy.md`

## 11. Automation Conformance Rule

Project-management automation must perform explicit conformance checks.

The conformance layer must fail when it detects:

- duplicate declared project IDs in governed rollups
- a declared `Project ID` that does not match the project folder name
- deprecated stage labels presented as canonical state
- legacy PM artifact names being used as current authoritative controls
- draft or read-only PM control surfaces being treated as authoritative
- `on-track` status assigned to packets or control surfaces that are still
  explicitly not reviewed or otherwise non-authoritative

Automation may still write advisory outputs after detecting these failures, but
the run itself must be marked failed.

## 12. Related Artifacts

- `01_DOCTRINE/03_POLICIES/POL-055_Repository_Project_Policy.md`
- `01_DOCTRINE/03_POLICIES/POL-056_Firm_Project_Policy.md`
- `01_DOCTRINE/03_POLICIES/POL-072_HillSide_Business_Project_Policy.md`
- `01_DOCTRINE/03_POLICIES/POL-070_Backlog_Routing_Policy.md`
- `01_DOCTRINE/03_POLICIES/POL-071_Matter_Delivery_Stage_Policy.md`
