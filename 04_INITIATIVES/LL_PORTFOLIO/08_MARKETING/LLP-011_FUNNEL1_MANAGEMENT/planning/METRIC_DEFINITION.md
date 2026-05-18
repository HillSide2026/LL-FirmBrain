---
id: 04_initiatives_ll_portfolio_08_marketing_llp_011_funnel1_management_planning_metric_definition_md
title: Metric Definition
owner: ML1
status: draft
created_date: 2026-05-18
last_updated: 2026-05-18
tags: []
---

# Metric Definition

Project ID: LLP-011
Project Path: 08_MARKETING/LLP-011_FUNNEL1_MANAGEMENT
Stage: Planning

## Funnel 01 Core Metrics

| KPI | Definition | Formula |
| --- | --- | --- |
| `cost_per_qualified_lead` | Average paid acquisition cost per lead | `ad_spend / leads` |
| `lead_to_booked_rate` | Share of captured leads that progress to booked consult | `(booked / lead_captured) * 100` |
| `lead_to_retained_rate` | Share of captured leads that become retained | `(retained / lead) * 100` |
| `consult_show_rate` | Share of booked consults completed | `(consult_complete / booked) * 100` |
| `consult_to_retained_rate` | Share of completed consults that become retained | `(retained / consult_complete) * 100` |

## Goal Alignment
- `cost_per_qualified_lead` supports acquisition efficiency goal.
- `lead_to_booked_rate` and `consult_show_rate` support execution-throughput goal.
- `lead_to_retained_rate` and `consult_to_retained_rate` support conversion achievement goal.

## Stage Mapping
- Canonical progression: `lead_captured -> screened -> booked -> consult_complete -> retained`
- Formula token `lead` corresponds to count of `lead_captured` events in the measurement window.
- Lifecycle normalization alignment: `intake -> inquiry`; `conversion` remains the marketing terminal stage label; downstream fulfillment handoff is labeled `onboarding`.

## Target Status
- Target thresholds are `TBD` pending ML1 metric approval for Planning -> Executing gate authorization.

## ROAS Threshold Hypothesis

| Metric | Hypothesis | Status | Source |
|--------|------------|--------|--------|
| ROAS (all-in) | Must exceed **2.0x** to justify continued F1 spend | ML1 hypothesis — not yet validated | ML1 2026-03-30 |

**Context:** 2025 all-in ROAS was ~1.47x (Jan–Oct, $36,654 revenue / $25,000 cost). Below the hypothesized threshold.
This hypothesis is not yet a formal target — it requires ML1 approval to become a governance threshold.
Until validated, it serves as the working benchmark for F1 investment decisions.

## Measurement Cadence
- Weekly operational review
- Monthly governance summary
