---
id: llp_005_opening__planning__metrics_md
title: LLP-005 Opening - Metrics
owner: ML1
status: approved
created_date: 2026-04-07
last_updated: 2026-04-07
tags: [llp-005, opening, planning, metrics]
---

# Metrics

Project ID: LLP-005
Project Path: 03_FIRM_OPERATIONS/LLP-005
Stage: Planning

Approval Status: Approved (ML1 threshold approval recorded 2026-03-16)
Threshold Status: Active for execution governance. This file is the canonical
wrapper for the legacy split measurement packet retained in this folder for
provenance.

## Metric Definition

| KPI | Definition | Formula | Decision Use |
| --- | --- | --- | --- |
| `gate2_intake_accept_rate` | Share of Gate 2 packets accepted as complete at opening intake | `(gate2_packets_accepted / gate2_packets_received) * 100` | Intake quality and rework pressure |
| `opening_checklist_completion_rate` | Share of Gate 2-authorized matters with complete opening checklist before Gate 3 | `(checklist_complete / gate2_authorized_matters) * 100` | Execution completeness control |
| `financial_readiness_within_2d_rate` | Share of Gate 2-authorized matters reaching financial readiness within 2 days | `(financial_ready_within_2d / gate2_authorized_matters) * 100` | Accounts-speed control |
| `opening_cycle_time_days` | Median days from Gate 2 to Gate 3 | `median(gate3_date - gate2_date)` | End-to-end opening speed |
| `opening_exception_backlog` | Count of unresolved opening exceptions | `open_opening_exceptions` | Operational risk pressure |
| `premature_handoff_count` | Count of matters handed to LLP-006 before Gate 3 completion | `premature_handoffs` | Boundary-control integrity |

## Context Metric

- `gate2_authorized_matters`: `count(gate2_authorized)` for denominator context.

## Thresholds

| KPI | Direction | Approved Threshold |
| --- | --- | --- |
| `gate2_intake_accept_rate` | Higher is better | `>= 95%` |
| `opening_checklist_completion_rate` | Higher is better | `>= 95%` |
| `financial_readiness_within_2d_rate` | Higher is better | `>= 85%` |
| `opening_cycle_time_days` | Lower is better | `<= 3 days` |
| `opening_exception_backlog` | Lower is better | `<= 3 open` |
| `premature_handoff_count` | Lower is better | `= 0` |

## Measurement Method

### Method

- Use opening run artifacts as the primary measurement source.
- Require evidence pointers for Gate 2 intake and Gate 3 completion events.
- Compute cycle timing from observed timestamps only.
- Track exceptions by age, type, and owner.

### Calculation Rules

- `gate2_packets_received` includes only LLP-004 handoff packets entering opening intake.
- `gate2_packets_accepted` requires packet completeness against the approved intake checklist.
- `gate2_authorized_matters` includes only signed-engagement-authorized entries.
- `financial_ready_within_2d` counts records with complete financial-readiness evidence within 48 hours of Gate 2 intake.
- `gate3_date` is valid only when Gate 3 completion evidence and approval state exist.
- `premature_handoffs` includes any LLP-006 handoff before Gate 3 completion.

### Window and Reporting

- Weekly trailing 7 days.
- Monthly rollup for trend analysis.

## Baseline Capture Period

- Start: 2026-03-10
- End: 2026-03-30

### Purpose

Capture opening-stage performance baseline before implementation hardening.

### Inclusion Rules

- Include only Gate 2-authorized opening records.
- Include only records with traceable intake, readiness, and Gate 3 events.

## Validation Review

### Review Criteria

- Intake, readiness, and Gate 3 metrics are reproducible from source artifacts.
- Denominators and inclusion rules are unambiguous.
- Exception tracking supports corrective-action prioritization.
- KPI package is sufficient for execution governance.

### Review Outcome

Status: Normalized from approved legacy packet.
Notes: Thresholds were approved by ML1 on 2026-03-16. Separate legacy measurement
files remain in the folder for provenance only.

## Retired Metric Artifact Consolidation

- Consolidated on: 2026-05-25
- Retired source artifacts moved to: `10_ARCHIVE/LL_PORTFOLIO_PM_CONFORMANCE_2026-05-25/04_INITIATIVES/LL_PORTFOLIO/03_FIRM_OPERATIONS/LLP-005/planning`
- Retired artifact names: BASELINE_CAPTURE_PERIOD.md, MEASUREMENT_METHOD.md, METRIC_DEFINITION.md, ML1_METRIC_APPROVAL.md, VALIDATION_REVIEW.md
- Threshold approval and measurement details now belong in this `METRICS.md` file.

