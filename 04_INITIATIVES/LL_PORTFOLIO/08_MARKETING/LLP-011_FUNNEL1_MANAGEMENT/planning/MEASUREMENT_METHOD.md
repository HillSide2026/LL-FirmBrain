---
id: 04_initiatives_ll_portfolio_08_marketing_llp_011_funnel1_management_planning_measurement_method_md
title: Measurement Method
owner: ML1
status: draft
created_date: 2026-05-18
last_updated: 2026-05-18
tags: []
---

# Measurement Method

Project ID: LLP-011
Project Path: 08_MARKETING/LLP-011_FUNNEL1_MANAGEMENT
Stage: Planning

## Method
- Capture stage transitions from governed funnel artifacts and platform records.
- Enforce canonical stage sequence for KPI calculations.
- Use only observed event timestamps and attributable spend data.
- Maintain evidence references for each aggregated metric report.
- Use KPI outputs to guide implementation control decisions and goal-attainment review.

## Calculation Rules
- `lead` in KPI formulas is the count of `lead_captured` events in the measurement window.
- `cost_per_qualified_lead`
  Numerator: paid spend attributable to Funnel 01 during window.
  Denominator: count of leads during window.
- `lead_to_booked_rate`
  Numerator: count of leads that reach `booked` stage.
  Denominator: count of `lead_captured` in window.
- `lead_to_retained_rate`
  Numerator: count of `retained` events.
  Denominator: count of captured leads (`lead`) in window.
- `consult_show_rate`
  Numerator: count of `consult_complete` events.
  Denominator: count of `booked` events.
- `consult_to_retained_rate`
  Numerator: count of `retained` events sourced from `consult_complete`.
  Denominator: count of `consult_complete` events.

## Window and Reporting
- Default operational window: rolling 7 days.
- Governance rollup: monthly.
- Any KPI below ML1-approved threshold for 2 consecutive weekly windows triggers corrective-action escalation.

## Data Sources
- Google Ads spend and campaign-level performance exports.
- GHL intake, booking, and consult progression records.
- Governed run artifacts and stage-classification evidence.
