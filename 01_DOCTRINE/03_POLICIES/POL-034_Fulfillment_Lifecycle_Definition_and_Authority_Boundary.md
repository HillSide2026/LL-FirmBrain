---
id: POL-034
title: Fulfillment Lifecycle Definition and Authority Boundary
owner: ML1
status: approved
approved_by: ML1
approved_date: 2026-04-18
version: 0.3
effective_date: 2026-04-18
supersedes:
provenance:
  decided_by: ML1
  decided_on: 2026-04-18
  context: Metadata normalized by system admin cleanup on 2026-05-24
created_date: 2026-03-09
last_updated: 2026-03-22
tags: [policy, fulfillment, lifecycle, authority, gates]
---

# POL-034 — Fulfillment Lifecycle Definition and Authority Boundary

Policy Statement: Fulfillment is the governed administrative system that begins at Onboarding and ends at Closed. Fulfillment is not legal delivery and must operate within explicit gate, scope, and authority boundaries.

Scope: Fulfillment operates at the **matter level** — one fulfillment lifecycle
instance per matter.

`fulfillment_status` is the canonical fulfillment-side matter field. It
captures the operational posture of the matter for admin / ops purposes.

`fulfillment_stage` is a secondary operational field. It is useful for guiding
team workflow, sequencing, handoffs, and readiness logic, but it is not one of
the core canonical matter fields.

The two fulfillment concepts are independent:
- `fulfillment_status` — the canonical operational priority state (`urgent` /
  `active` / `keep in view` / `dormant` / `closing`)
- `fulfillment_stage` — the sequential lifecycle position defined in this
  policy

Terminology rules:
- `onboarding` is the canonical fulfillment-stage label for the first stage.
- `conversion` is a marketing-stage label and is not a fulfillment stage.
- Onboarding is a shared boundary: marketing ends here; fulfillment begins here.

Canonical fulfillment lifecycle:

| Stage | Description | Matter Status |
|-------|-------------|---------------|
| Onboarding | Consult scheduled; engagement letter being prepared | `pending` |
| Opening | Engagement signed; matter setup underway | `open` |
| Maintenance | Necessary administration of matter | `open` |
| Pending Close | Work complete; administrative file closure | `pending` |
| Closed | Terminal | `closed` |

`Closed` requires a `close_reason` value: `completed` / `declined` / `terminated`

Cross-cutting fulfillment functions:
- Accounts (cross-cutting across Onboarding / Opening / Maintenance): money setup, billing controls, collections, trust/retainer controls
- Admin: fulfillment risk-management controls

Gate and status transition rules:
- Gate 1 (Onboarding Entry): consult scheduled and client intent to proceed confirmed; matter status = `pending`.
- Gate 2 (Engagement Signed): authorizes transition from Onboarding to Opening; matter status transitions to `open`.
- Gate 3 (Opening Complete): opening controls complete and internally approved; authorizes transition to Maintenance.
- Gate 4 (Work Complete): substantive work complete; authorizes transition to Pending Close; matter status returns to `pending`.
- Gate 5 (Close Authorized): ML1 explicit approval; matter status transitions to `closed`; `close_reason` must be set.
- No stage skipping is allowed.

Boundary rules:
- Fulfillment governs administrative execution only; it must not perform legal judgment, legal strategy, or substantive delivery decisions.
- Marketing ends at Onboarding per `POL-032` and `POL-033`; fulfillment begins at Onboarding.
- Maintenance outputs do not authorize doctrine changes or gate overrides.
- Closed may occur only after fulfillment closure preconditions are satisfied and explicitly approved under ML1 authority.

Authority rules:
- ML1 is the sole authority for gate advancement, exceptions, and boundary overrides.
- System/agent layers may enforce controls and produce diagnostics but may not self-authorize stage promotion.

Authority (Principles referenced): PRN-020, PRN-021, PRN-027, PRN-028
Enforcement expectation: Any run, artifact, or workflow that misclassifies fulfillment stages, skips gates, or performs out-of-scope legal-delivery actions is non-compliant and must be blocked or escalated to ML1.
Supersedes: None
Version: 0.3
Status: Draft
