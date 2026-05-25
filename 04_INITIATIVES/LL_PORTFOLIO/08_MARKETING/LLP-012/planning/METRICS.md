---
id: llp_012_funnel2_management__planning__metrics_md
title: LLP-012 Funnel 2 - Metrics
owner: ML1
status: draft
created_date: 2026-03-15
last_updated: 2026-04-07
tags: [llp-012, funnel-02, planning, metrics]
---

# Metrics

Project ID: LLP-012
Project Path: 08_MARKETING/LLP-012
Stage: Planning

Approval Status: Provisional. Project execution was authorized by ML1 on
2026-04-01, but numeric thresholds remain provisional until the baseline-lock
rule below is satisfied and ML1 records the final lock decision inside this
file.

---

## KPI Definitions

### Intake Stage

| KPI | Process Step | SLA | Formula | Target |
| --- | --- | --- | --- | --- |
| `leads_worked_within_24h_rate` | 3.3 Intake — Welcoming | Call out within 24h of opt-in | `(opt-in leads with first contact ≤ 24h) / (opt-in leads) × 100` | `≥ 90%` |
| `leads_scheduled_rate` | 3.4 Intake — Scheduling | N/A | `(opt-in leads with consult scheduled) / (opt-in leads) × 100` | `≥ 30%` |
| `qualification_call_completion_rate` | 3.4 Intake — Qualification | Mandatory qualification call completed before paid path or ML1 allocation | `(opt-in leads with completed qualification call and full evidence record) / (opt-in leads) × 100` | `100%` |

### Conversion Stage

| KPI | Process Step | SLA | Formula | Target |
| --- | --- | --- | --- | --- |
| `consulting_stage_tracking` | 3.5 Conversion — Consulting | N/A | Instrumentation complete and reportable | Instrumentation required |
| `paid_lead_to_engaged_conversion_rate` | 3.6 Conversion — Closing/Engaging | N/A | `(paid leads reaching closing/engaged) / (paid leads) × 100` | `≥ 10%` |

Intake targets and conversion target provided by ML1.
`consulting_stage_tracking` is instrumentation-only until ML1 sets a numeric threshold.

## Qualification-Call Evidence Requirement

`qualification_call_completion_rate` is satisfied only if the record includes:

- lead source
- referring accountant or referral source, if any
- buyer role
- buyer authority level
- annual revenue band
- employee band
- accountant relationship confirmed
- maturity trigger
- practice-area fit
- projected remediation value band
- willingness to pay for a Health Check tier
- timeframe / urgency
- document readiness
- disposition
- disqualification reason, if applicable
- recommended next path

Canonical disposition values are:

- `qualified`
- `declined`
- `no_response`
- `deferred`
- `out_of_scope`

## Measurement Method

- Capture intake-stage and conversion-stage events from governed funnel artifacts.
- Normalize stage aliases: `intake → inquiry`. Treat `conversion` as canonical marketing terminal stage; `onboarding` as downstream fulfillment handoff label.
- Record stage transitions with timestamped evidence references.
- Measure against ML1-approved thresholds.

### Calculation Rules
- `leads_worked_within_24h_rate`: numerator = opt-in leads with first outbound call/contact timestamp ≤ 24h of opt-in; denominator = opt-in leads in window.
- `leads_scheduled_rate`: numerator = opt-in leads with scheduled consult/meeting event; denominator = opt-in leads in window.
- `qualification_call_completion_rate`: numerator = opt-in leads with a completed qualification call and full evidence record; denominator = opt-in leads in window.
- `consulting_stage_tracking`: consulting-stage events must be captured for conversion-qualified leads and handoff records.
- `paid_lead_to_engaged_conversion_rate`: numerator = paid leads reaching closing/engaged conversion; denominator = paid leads in window.

### Window and Reporting
- Default window: rolling 7 days for operational management.
- Governance rollup: monthly.
- Any metric below target for 2 consecutive weekly windows requires escalation review.

### Data Sources
- Website and landing-page conversion instrumentation (`levine-law.ca`)
- Funnel intake forms / booking events
- Conversion evidence artifacts (engagement signed, retainer received, or invoice paid), with handoff reference to fulfillment onboarding
- Governed run artifacts and signal reports

## Baseline Capture Period

Status: Defined but not yet active
Notes: The F02 baseline window opens only after all conditions below are true:

- one canonical qualification-call schema is deployed without bypass
- one canonical Health Check price ladder is live
- one canonical payment / routing path is live
- no material pricing, routing, or qualification-schema change occurs during
  the measurement window

### Formal Lock Rule

ML1 may lock F02 thresholds only at the later of:

- `60` days of clean live operation, or
- `8` completed paid Corporate Health Checks

The lock window must also include at least `2` downstream conversions into
remediation or recurring counsel before final threshold approval.

## Validation

Status: Proposed with lock rule recorded
Notes: Operating targets are useful now. Numeric threshold lock remains
pending until the baseline conditions and formal lock rule above are
satisfied and approved by ML1.

## Retired Metric Artifact Consolidation

- Consolidated on: 2026-05-25
- Retired source artifacts moved to: `10_ARCHIVE/LL_PORTFOLIO_PM_CONFORMANCE_2026-05-25/04_INITIATIVES/LL_PORTFOLIO/08_MARKETING/LLP-012/planning`
- Retired artifact names: ML1_METRIC_APPROVAL.md
- Threshold approval and measurement details now belong in this `METRICS.md` file.

