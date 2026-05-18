---
id: 04_initiatives_ll_portfolio_01_financial_management_llp_001_accounting_planning_metrics_md
title: Metrics
owner: ML1
status: draft
created_date: 2026-05-18
last_updated: 2026-05-18
tags: []
---

# Metrics

Project ID: LLP-001
Project Path: 01_FINANCIAL_MANAGEMENT/LLP-001_ACCOUNTING
Stage: Planning

Approval Status: Proposed
Threshold Status: Proposed. These thresholds are planning-stage gate inputs
only and are not yet active for execution governance.

## Metric Definition

| KPI | Definition | Formula | Decision Use |
| --- | --- | --- | --- |
| `reconciliation_coverage_rate` | Share of in-scope reconciliations completed for the review window | `(completed_reconciliations / due_reconciliations) * 100` | Determines whether the packet is complete enough to rely on |
| `reconciliation_timeliness_rate` | Share of due reconciliations completed by the approved cut-off | `(on_time_reconciliations / due_reconciliations) * 100` | Tests whether cadence is operationally realistic |
| `evidence_traceability_rate` | Share of sampled balances or transactions with source support pointers | `(sampled_items_with_support / sampled_items_reviewed) * 100` | Tests whether the fact layer is reviewable |
| `acquisition_spend_tagging_coverage_rate` | Share of in-scope acquisition spend items from 2026-07-01 onward that are tagged to the governed `acquisition` project / program classification | `(tagged_acquisition_items / in_scope_acquisition_items) * 100` | Tests whether LLP-002 can rely on one combined acquisition actuals feed |
| `open_exception_backlog` | Count of unresolved accounting exceptions past the agreed review window | `count(open_exceptions_past_window)` | Measures control pressure and unresolved risk |
| `downstream_handoff_freshness_days` | Age in days of the latest approved fact packet provided to LLP-002 | `date(consumer_packet) - date(last_approved_fact_packet)` | Prevents stale facts from being treated as current |

## Context Metric

- `due_reconciliations`: count of in-scope reconciliations scheduled for the
  review window.

## Proposed Thresholds

| KPI | Direction | Proposed Threshold |
| --- | --- | --- |
| `reconciliation_coverage_rate` | Higher is better | `= 100%` of due reconciliations completed |
| `reconciliation_timeliness_rate` | Higher is better | `>= 90%` completed by cut-off |
| `evidence_traceability_rate` | Higher is better | `= 100%` in sampled reviewed items |
| `acquisition_spend_tagging_coverage_rate` | Higher is better | `= 100%` for in-scope items dated 2026-07-01 onward |
| `open_exception_backlog` | Lower is better | `<= 5` open beyond the agreed review window |
| `downstream_handoff_freshness_days` | Lower is better | `<= 10 days` from the last approved fact packet |

## Measurement Method

### Method

- measure from governed reconciliation packs, supporting schedules, and source
  pointers rather than memory or narrative summaries
- sample evidence traceability explicitly instead of assuming booked records are
  self-proving
- review fact freshness at the point of LLP-002 consumption, not only inside
  LLP-001

### Calculation Rules

- `completed_reconciliations` counts only reconciliations with an explicit
  support package
- `on_time_reconciliations` counts only completed reconciliations delivered by
  the approved cut-off
- `sampled_items_reviewed` must include both routine items and exception items
- `in_scope_acquisition_items` includes only marketing or sales spend items
  dated 2026-07-01 or later that should roll into the governed acquisition
  category
- `tagged_acquisition_items` counts only items explicitly mapped to the
  `acquisition` project / program classification
- `open_exceptions_past_window` excludes items formally paused by ML1 with a
  recorded rationale
- `downstream_handoff_freshness_days` is measured only when an LLP-002 handoff
  actually occurs

### Review Window

- first baseline window: the first full governed reconciliation cycle after the
  planning packet is frozen
- review cadence: per close cycle and at each planning-to-executing gate review

## Baseline Capture Period

Start: first full governed reconciliation cycle after planning packet freeze
End: completion of that cycle and its downstream handoff review

Purpose: confirm that the proposed control model is measurable before execution
is authorized.

## Validation Review

### Review Criteria

- each KPI can be computed from observed accounting evidence
- thresholds support ML1 gate judgment rather than vanity reporting
- sampled traceability is reproducible
- acquisition-tagging coverage is auditable from source records dated
  2026-07-01 onward
- downstream freshness warnings are visible when facts are incomplete or stale

### Review Outcome

Status: Proposed
Notes: Metrics are now present for planning-stage review. ML1 threshold approval
remains pending.

## ML1 Metric Approval

Approval Status: Proposed

Approved By: ______________________
Date: ______________________
