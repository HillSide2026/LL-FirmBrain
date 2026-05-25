---
id: 04_initiatives_ll_portfolio_03_firm_operations_llp_004_onboarding_planning_metric_definition_md
title: Metric Definition
owner: ML1
status: draft
created_date: 2026-05-18
last_updated: 2026-05-18
tags: []
---

# Metric Definition

Project ID: LLP-004
Project Path: 03_FIRM_OPERATIONS/LLP-004
Stage: Planning

## LLP-004 Core Metrics

| KPI | Definition | Formula | Decision Use |
| --- | --- | --- | --- |
| `onboarding_engagement_rate` | Share of qualified leads that reach signed engagement (Gate 2) | `(engagements_signed / qualified_leads) * 100` | Core onboarding performance |
| `agreement_sent_within_24h_rate` | Share of qualified leads with engagement agreement sent within 24h of Gate 1 | `(agreements_sent_within_24h / qualified_leads) * 100` | 24-hour responsiveness SLA control |
| `onboarding_cycle_time_days` | Median days from Gate 1 validation to signed engagement | `median(agreement_signed_at - gate1_at)` | Speed from qualified lead to engagement |
| `onboarding_exception_backlog` | Count of unresolved onboarding exceptions | `open_onboarding_exceptions` | Operational risk pressure |

## Context Metric (Non-KPI)
- `qualified_leads`: `count(gate1_validated)` for denominator context.

## Target Status
- Penciled thresholds (draft for gate review):
  - `onboarding_engagement_rate` >= `60%`
  - `agreement_sent_within_24h_rate` >= `90%`
  - `onboarding_cycle_time_days` <= `5`
  - `onboarding_exception_backlog` <= `3`
- These remain draft targets until explicitly approved in `ML1_METRIC_APPROVAL.md`.

## Measurement Cadence
- Weekly operational review
- Monthly governance summary
