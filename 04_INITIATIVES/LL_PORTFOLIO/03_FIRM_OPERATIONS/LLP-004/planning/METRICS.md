---
id: llp_004_onboarding__planning__metrics_md
title: LLP-004 Onboarding - Metrics
owner: ML1
status: approved
created_date: 2026-04-07
last_updated: 2026-04-07
tags: [llp-004, onboarding, planning, metrics]
---

# Metrics

Project ID: LLP-004
Project Path: 03_FIRM_OPERATIONS/LLP-004
Stage: Planning

Approval Status: Approved (ML1 threshold approval recorded 2026-03-16)
Threshold Status: Active for execution governance. This file is the canonical
wrapper for the legacy split measurement packet retained in this folder for
provenance.

## Metric Definition

| KPI | Definition | Formula | Decision Use |
| --- | --- | --- | --- |
| `onboarding_engagement_rate` | Share of qualified leads that reach signed engagement (Gate 2) | `(engagements_signed / qualified_leads) * 100` | Core onboarding performance |
| `agreement_sent_within_24h_rate` | Share of qualified leads with engagement agreement sent within 24h of Gate 1 | `(agreements_sent_within_24h / qualified_leads) * 100` | 24-hour responsiveness SLA control |
| `onboarding_cycle_time_days` | Median days from Gate 1 validation to signed engagement | `median(agreement_signed_at - gate1_at)` | Speed from qualified lead to engagement |
| `onboarding_exception_backlog` | Count of unresolved onboarding exceptions | `open_onboarding_exceptions` | Operational risk pressure |

## Context Metric

- `qualified_leads`: `count(gate1_validated)` for denominator context.

## Thresholds

| KPI | Direction | Approved Threshold |
| --- | --- | --- |
| `onboarding_engagement_rate` | Higher is better | `>= 60%` |
| `agreement_sent_within_24h_rate` | Higher is better | `>= 90%` |
| `onboarding_cycle_time_days` | Lower is better | `<= 5 days` |
| `onboarding_exception_backlog` | Lower is better | `<= 3 open` |

## Measurement Method

### Method

- Use onboarding run artifacts as the primary measurement source.
- Require source evidence pointers for Gate 1 and Gate 2 transitions.
- Measure cycle timing from observed timestamps only.
- Track exception lifecycle by age and severity.
- Compute SLA using elapsed time from Gate 1 validation to the agreement-send event.

### Calculation Rules

- `qualified_leads` includes only records with Gate 1 validation evidence.
- `engagements_signed` requires explicit signed-agreement evidence.
- `agreements_sent_within_24h` counts only records where `agreement_sent_at - gate1_at <= 24h`.
- `onboarding_cycle_time_days` includes only records with both `gate1_at` and `agreement_signed_at`.
- `open_onboarding_exceptions` includes unresolved exceptions at the reporting cut-off.

### Window and Reporting

- Weekly trailing 7 days.
- Monthly rollup for trend analysis.

## Baseline Capture Period

- Start: 2026-03-10
- End: 2026-03-30

### Purpose

Capture the initial onboarding performance baseline before implementation hardening.

### Inclusion Rules

- Include only Gate 1-validated onboarding records.
- Include only records with traceable agreement and pending-matter events.

## Validation Review

### Review Criteria

- Engagement and 24-hour agreement SLA metrics are reproducible from source artifacts.
- Denominators and inclusion rules are unambiguous.
- Cycle-time and exception tracking support corrective-action prioritization.
- KPI package is sufficient for execution governance.

### Review Outcome

Status: Normalized from approved legacy packet.
Notes: Thresholds were approved by ML1 on 2026-03-16. Separate legacy measurement
files remain in the folder for provenance only.

## Retired Metric Artifact Consolidation

- Consolidated on: 2026-05-25
- Retired source artifacts moved to: `10_ARCHIVE/LL_PORTFOLIO_PM_CONFORMANCE_2026-05-25/04_INITIATIVES/LL_PORTFOLIO/03_FIRM_OPERATIONS/LLP-004/planning`
- Retired artifact names: BASELINE_CAPTURE_PERIOD.md, MEASUREMENT_METHOD.md, METRIC_DEFINITION.md, ML1_METRIC_APPROVAL.md, VALIDATION_REVIEW.md
- Threshold approval and measurement details now belong in this `METRICS.md` file.

