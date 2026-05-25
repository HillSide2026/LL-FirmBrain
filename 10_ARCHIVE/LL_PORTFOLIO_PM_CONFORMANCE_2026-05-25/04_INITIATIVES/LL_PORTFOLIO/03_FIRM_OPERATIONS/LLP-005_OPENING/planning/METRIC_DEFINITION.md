---
id: 04_initiatives_ll_portfolio_03_firm_operations_llp_005_opening_planning_metric_definition_md
title: Metric Definition
owner: ML1
status: draft
created_date: 2026-05-18
last_updated: 2026-05-18
tags: []
---

# Metric Definition

Project ID: LLP-005
Project Path: 03_FIRM_OPERATIONS/LLP-005
Stage: Planning

## LLP-005 Core Metrics

| KPI | Definition | Formula | Decision Use |
| --- | --- | --- | --- |
| `gate2_intake_accept_rate` | Share of Gate 2 packets accepted as complete at opening intake | `(gate2_packets_accepted / gate2_packets_received) * 100` | Intake quality and rework pressure |
| `opening_checklist_completion_rate` | Share of Gate 2-authorized matters with complete opening checklist before Gate 3 | `(checklist_complete / gate2_authorized_matters) * 100` | Execution completeness control |
| `financial_readiness_within_2d_rate` | Share of Gate 2-authorized matters reaching financial readiness within 2 days | `(financial_ready_within_2d / gate2_authorized_matters) * 100` | Accounts-speed control |
| `opening_cycle_time_days` | Median days from Gate 2 to Gate 3 | `median(gate3_date - gate2_date)` | End-to-end opening speed |
| `opening_exception_backlog` | Count of unresolved opening exceptions | `open_opening_exceptions` | Operational risk pressure |
| `premature_handoff_count` | Count of matters handed to LLP-006 before Gate 3 completion | `premature_handoffs` | Boundary-control integrity |

## Context Metric (Non-KPI)
- `gate2_authorized_matters`: `count(gate2_authorized)` for denominator context.

## Target Status
- Anticipated thresholds (draft for gate review):
  - `gate2_intake_accept_rate` >= `95%`
  - `opening_checklist_completion_rate` >= `95%`
  - `financial_readiness_within_2d_rate` >= `85%`
  - `opening_cycle_time_days` <= `3`
  - `opening_exception_backlog` <= `3`
  - `premature_handoff_count` = `0`
- These remain draft targets until explicitly approved in `ML1_METRIC_APPROVAL.md`.

## Measurement Cadence
- Weekly operational review
- Monthly governance summary
