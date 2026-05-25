---
id: 04_initiatives__ll_portfolio__07_growth_projects__llp_030_firm_strategy__planning__metrics_md
title: LLP-030 Firm Strategy - Metrics
owner: ML1
status: draft
created_date: 2026-04-03
last_updated: 2026-04-03
tags: [llp-030, planning, metrics]
---

# Metrics

Project ID: `LLP-030`
Project Path: `04_INITIATIVES/LL_PORTFOLIO/07_GROWTH_PROJECTS/LLP-030`
Stage: `Planning`

## Metric Purpose

These are planning-stage control metrics for LLP-030 itself.

They do not replace the firm's operating KPIs. They measure whether LLP-030 is
becoming a decision-useful strategic control packet rather than remaining a set
of useful but loosely governed documents.

## Metric Definitions

| Metric | Definition | Source | Review Cadence | Proposed Threshold |
| --- | --- | --- | --- | --- |
| `planning_packet_completion_pct` | required canonical planning artifacts complete ÷ required planning artifacts total | `planning/` file inventory | on edit; weekly while planning open | `100%` before planning-gate review |
| `material_contradiction_count` | count of open material contradictions across `FIRM_STRATEGY.md`, `BUSINESS_PLAN.md`, `FINANCIAL_MODEL.md`, and linked governing packets | ML1 review plus dependency check | weekly | `0` before executing authorization is considered |
| `linked_packet_alignment_reviews_complete` | number of required linked packets explicitly reviewed against LLP-030 assumptions | `DEPENDENCIES.md` alignment review | weekly | `6/6` required set completed |
| `financial_model_readiness` | qualitative state of the financial model: `stub`, `draft`, `decision-useful`, `approved` | `../FINANCIAL_MODEL.md` | weekly | at least `decision-useful` before LLP-030 can be treated as execution-ready |
| `critical_open_strategy_questions` | count of unresolved strategy questions that materially affect channel sequencing, profitability, staffing sequence, or entity treatment | ML1 review log | weekly | `0` material unresolved items at planning-gate review |
| `profitability_visibility_status` | binary check whether LLP-030 explicitly states the profitability logic for `F01`, leverage, and Andersen cross-entity treatment | `BUSINESS_PLAN.md`, `FINANCIAL_MODEL.md` | weekly | `yes` before planning is treated as mature |

## Measurement Method

| Metric | Method |
| --- | --- |
| `planning_packet_completion_pct` | count the seven required Stage 2 files in `planning/` and divide completed files by seven |
| `material_contradiction_count` | count only contradictions that would change ML1 judgment, not minor wording differences |
| `linked_packet_alignment_reviews_complete` | required set is `LLP-002`, `LLP-025`, `LLP-011`, `LLP-012`, `LLP-013`, and `LLP-033` |
| `financial_model_readiness` | classify manually based on whether the document can answer margin / profitability questions without major guesswork |
| `critical_open_strategy_questions` | count unresolved items affecting operating target, ICP floor, staffing sequence, profitability model, or Andersen treatment |
| `profitability_visibility_status` | mark `yes` only if the relevant documents explicitly address profitability rather than only revenue |

## Baseline Capture Period

Baseline opens on `2026-04-03`, the date the canonical Stage 2 packet is first
normalized for LLP-030.

This baseline is not a revenue baseline. It is a planning-readiness baseline.

## Validation Review

Validation occurs at the next ML1 planning review for LLP-030 and asks:

- is the Stage 2 packet complete
- are the root docs materially aligned
- is the financial model still only narrative, or actually decision-useful
- are the linked packets aligned enough that LLP-030 can govern them credibly

## ML1 Threshold Approval

Approval Status: Proposed

Submitted By: ML2  
Date: 2026-04-03

| Item | Status | Date | Notes |
| --- | --- | --- | --- |
| metric definitions | drafted | 2026-04-03 | planning-stage control metrics defined |
| measurement method | drafted | 2026-04-03 | manual review rules defined |
| baseline logic | drafted | 2026-04-03 | planning-readiness baseline opened |
| validation review criteria | drafted | 2026-04-03 | ML1 review questions defined |
| threshold approval | pending | — | no ML1 threshold approval recorded yet |

Notes:

- Executing is not authorized by this file.
- This file becomes binding for LLP-030 only when ML1 approves the thresholds.
