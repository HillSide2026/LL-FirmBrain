---
id: llp_011_funnel1_management__planning__metrics_md
title: LLP-011 Funnel 1 - Metrics
owner: ML1
status: approved
created_date: 2026-04-07
last_updated: 2026-04-09
tags: [llp-011, funnel-01, planning, metrics]
---

# Metrics

Project ID: LLP-011
Project Path: 08_MARKETING/LLP-011
Stage: Planning

Approval Status: Approved (framework and methods approved by ML1 on 2026-03-16)
Threshold Status: Numeric thresholds remain provisional pending the first
4-week operational baseline. The F01 wind-down control is now defined via the
governing LLP-025 strategy packet. This file is the canonical wrapper for the
legacy split measurement packet retained in this folder for provenance.

## Metric Definition

| KPI | Definition | Formula | Decision Use |
| --- | --- | --- | --- |
| `cost_per_qualified_lead` | Average paid acquisition cost per lead | `ad_spend / leads` | Acquisition-efficiency control |
| `lead_to_booked_rate` | Share of captured leads that progress to booked consult | `(booked / lead_captured) * 100` | Top-of-funnel progression quality |
| `lead_to_retained_rate` | Share of captured leads that become retained | `(retained / lead) * 100` | End-to-end acquisition quality |
| `consult_show_rate` | Share of booked consults completed | `(consult_complete / booked) * 100` | Booking-flow and show-rate control |
| `consult_to_retained_rate` | Share of completed consults that become retained | `(retained / consult_complete) * 100` | Consult close-rate quality |

## Context Metrics

- `lead_volume`: count of `lead_captured` events in the measurement window.
- `all_in_roas_hypothesis`: `> 2.0x` remains a working ML1 investment
  hypothesis, not yet an approved threshold.
- `cash_flow_working_premise`: `CAD 500,000+` annual business cash flow remains
  the current F01 fit heuristic for reactive SMB matters. This is a working
  premise, not doctrine.

## Thresholds

| KPI | Threshold Status | Notes |
| --- | --- | --- |
| `cost_per_qualified_lead` | TBD | Lock after first 4-week operational baseline |
| `lead_to_booked_rate` | TBD | Lock after first 4-week operational baseline |
| `lead_to_retained_rate` | TBD | Lock after first 4-week operational baseline |
| `consult_show_rate` | TBD | Lock after first 4-week operational baseline |
| `consult_to_retained_rate` | TBD | Lock after first 4-week operational baseline |

## Working-Premise Review Metrics

These review metrics test whether the F01 cash-flow working premise is useful
for filtering reactive, lower-value demand. They are review tools, not
governed KPI thresholds.

| Review Metric | Definition | Use |
| --- | --- | --- |
| `share_of_retained_matters_below_cash_flow_premise` | Share of retained F01 matters where the business appears below the `CAD 500,000` annual cash-flow premise | Tests whether low-fit retained work is clustering below the premise |
| `revenue_from_below_premise_matters` | Collected revenue from retained F01 matters assessed below the `CAD 500,000` cash-flow premise | Measures economic drag from below-premise matters |
| `roas_above_vs_below_cash_flow_premise` | Compare attributable F01 ROAS for matters assessed above vs below the premise | Tests whether the premise improves channel economics |

### Review Rule

- Where exact cash-flow data is unavailable, use screening evidence and business-size proxies to place matters into practical bands for review.
- Recommended review bands: `< CAD 250,000`, `CAD 250,000-CAD 500,000`, `CAD 500,000-CAD 1,000,000`, `CAD 1,000,000+`.
- The `CAD 500,000` line is a working premise for analysis and screening judgment. It does not create an automatic rejection rule.

## F01 Wind-Down Control

F01 remains a bridge acquisition channel until F02 demonstrates replacement
capacity with enough consistency to protect both revenue and ML1 capacity.

### Adopted Trigger

Begin F01 wind-down only when all conditions below hold for `2` consecutive
rolling `30`-day windows:

- F02 produces at least `3` paid Corporate Health Checks in each window.
- F02 converts at least `1` Health Check client in each window into
  remediation work or a monthly retainer.
- F02 Health Check -> retained/remediation conversion rate is `>=` F01
  consult -> retained conversion rate over the same window.
- F02 generates at least `CAD 8,000` in combined collected Health Check
  revenue plus first-month value of signed downstream engagements in each
  window.
- Total firm active matters remain below `15`.

### Required Action

- Reduce F01 Google Ads spend by `50%` for the next `30` days.
- If the same conditions hold during that reduced-spend month and firm monthly
  revenue remains `>= CAD 22,000`, pause F01 entirely.

## Measurement Method

### Method

- Capture stage transitions from governed funnel artifacts and platform records.
- Enforce canonical stage sequence for KPI calculations.
- Use only observed event timestamps and attributable spend data.
- Maintain evidence references for each aggregated metric report.
- Use KPI outputs to guide execution-control decisions and goal-attainment review.

### Calculation Rules

- `lead` in KPI formulas is the count of `lead_captured` events in the measurement window.
- `cost_per_qualified_lead`: numerator is paid spend attributable to Funnel 01 during the window; denominator is the count of leads during the same window.
- `lead_to_booked_rate`: numerator is count of leads that reach `booked`; denominator is count of `lead_captured`.
- `lead_to_retained_rate`: numerator is count of `retained` events; denominator is count of captured leads.
- `consult_show_rate`: numerator is count of `consult_complete`; denominator is count of `booked`.
- `consult_to_retained_rate`: numerator is count of `retained` events sourced from `consult_complete`; denominator is count of `consult_complete`.

### Window and Reporting

- Default operational window: rolling 7 days.
- Governance rollup: monthly.
- Any KPI below an ML1-approved threshold for 2 consecutive weekly windows triggers corrective-action escalation.

### Data Sources

- Google Ads spend and campaign-level performance exports.
- Go High Level intake, booking, and consult progression records.
- Governed run artifacts and stage-classification evidence.

## Baseline Capture Period

- Start: 2026-03-09
- End: 2026-03-29

### Purpose

Establish the pre-change execution baseline for Funnel 01 so implementation
effects and goal achievement can be measured after go-live adjustments.

### Inclusion Rules

- Include only records attributable to Funnel 01 campaigns and intake path.
- Include only leads with valid stage-progression evidence.
- Exclude test traffic and incomplete records lacking minimum stage or timestamp data.

## Validation Review

### Review Criteria

- Metric formulas and denominators are unambiguous.
- Stage-event evidence is sufficient to reproduce KPI outputs.
- Baseline inclusion/exclusion rules are consistently applied.
- No metric requires inferred data outside governed sources.
- Escalation conditions are defined for under-threshold execution performance.
- KPI package is sufficient to judge implementation success against defined goals.

### Review Outcome

Status: Normalized from approved legacy packet.
Notes: Metric definitions and measurement method were approved by ML1 on
2026-03-16. Numeric thresholds remain intentionally open pending baseline review.

## Working Investment Note

- 2025 all-in ROAS was approximately `1.47x` based on the current packet.
- ML1's current working hypothesis is that F01 should exceed `2.0x` all-in ROAS
  to justify continued spend.
- That hypothesis is decision-useful now, but it is not yet a formal governed
  threshold until ML1 records it explicitly.
- The governed spend-reduction rule for F01 is the transition control above,
  not the ROAS hypothesis on its own.

## Retired Metric Artifact Consolidation

- Consolidated on: 2026-05-25
- Retired source artifacts moved to: `10_ARCHIVE/LL_PORTFOLIO_PM_CONFORMANCE_2026-05-25/04_INITIATIVES/LL_PORTFOLIO/08_MARKETING/LLP-011/planning`
- Retired artifact names: BASELINE_CAPTURE_PERIOD.md, MEASUREMENT_METHOD.md, METRIC_DEFINITION.md, ML1_METRIC_APPROVAL.md, VALIDATION_REVIEW.md
- Threshold approval and measurement details now belong in this `METRICS.md` file.

