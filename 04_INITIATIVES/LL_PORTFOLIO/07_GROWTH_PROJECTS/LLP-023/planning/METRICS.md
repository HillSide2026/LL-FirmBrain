---
id: 04_initiatives__ll_portfolio__07_growth_projects__llp_023_matter_command_control__planning__metrics_md
title: Matter Command and Control - Metrics
owner: ML1
status: draft
created_date: 2026-03-23
last_updated: 2026-03-23
tags: [matter-command-control, planning, metrics]
---

# Metrics

Project ID: `LLP-023`
Stage: `Planning`

## Planning Metric Rule

Metrics in LLP-023 exist to support slice prioritization and slice promotion.
They are not vanity instrumentation.

## Governing Design Rule

LLP-023 succeeds only if uncertain cases stay visibly uncertain.

## Locked Prioritization Logic

- Slice 1 is the current minimum viable command layer
- Slice 2, Slice 3, and Slice 4 are deferred until Slice 1 passes its trust and
  reliability gates
- promotion to later slices should happen only when the current slice is useful
  enough to justify more complexity

## Operating Rules

- each controlled daily pass reviews at most `25` Gmail threads
- each reviewed Gmail thread should end in exactly one canonical state label
- unreviewed threads remain outside the current pass rather than being silently
  force-processed

## Planning Exit Metrics

| Metric | Definition | Target | Evidence |
| --- | --- | --- | --- |
| Prioritization readiness | Slice order and explicit deferrals are documented | one coherent slice order | `SCOPE_STATEMENT.md`, `PROJECT_PLAN.md` |
| Boundary readiness | Source-of-truth, citation, cache, and ambiguity rules are explicit | one defensible control model | `ASSUMPTIONS_CONSTRAINTS.md`, `RISK_REGISTER.md` |
| Dependency readiness | Source, config, and orchestration dependencies are explicit | one dependency packet | `DEPENDENCIES.md` |
| Gate readiness | ML1 can decide continue / narrow / pause / promote | full planning packet coherent | planning folder |

## Operating Metrics for Controlled Slice Runs

| Metric | Definition | Source | Cadence |
| --- | --- | --- | --- |
| Daily run completion rate | Controlled daily runs that produce the minimum Slice 1 output set ÷ attempted controlled runs | run state and output files | per run / 10-run review |
| Citation coverage rate | Generated assertions sampled with source pointers ÷ generated assertions sampled | output audit sample | per review window |
| Routed matter coverage | Active matters appearing in command outputs ÷ active matters in scope for the run | Clio + generated outputs | per review window |
| Ambiguous-thread surfacing rate | Ambiguous Gmail threads surfaced to `INBOX_UNMAPPED.md` or review-required path ÷ ambiguous threads sampled | Gmail routing sample + exceptions | per review window |
| Reviewed-thread state disposition rate | Reviewed Gmail threads ending in exactly one canonical state label ÷ reviewed Gmail threads in the pass | Gmail audit + thread label inspection | per run / review window |
| False-authority incidents | Count of cases where outputs read as authoritative beyond source boundaries | audit review | per review window |

## Measurement Method

### Method

- use controlled run outputs, run-state files, and sampled artifact review
- compare generated outputs against source-system references, not memory
- sample ambiguous cases explicitly rather than relying only on successful
  routed cases
- measure Slice 1 first before treating later slices as promotion candidates

### Calculation Rules

- `daily_run_completion_rate`
  Rule: count runs that emit the minimum Slice 1 output set divided by
  attempted controlled runs in the review window
- `citation_coverage_rate`
  Rule: sampled assertions with source pointers divided by sampled assertions
- `routed_matter_coverage`
  Rule: in-scope matters appearing in command outputs divided by in-scope
  active matters for the run
- `ambiguous-thread-surfacing-rate`
  Rule: sampled ambiguous threads that are surfaced explicitly rather than
  silently assigned
- `reviewed-thread-state-disposition-rate`
  Rule: reviewed threads in the pass that end with exactly one canonical state
  label divided by total reviewed threads in the pass
- `false-authority-incidents`
  Rule: count every detected case where output wording or behavior implies
  source authority beyond the approved boundary

### Review Window

- controlled baseline window: next 10 controlled daily runs after the planning
  packet is frozen
- promotion review: at the close of that baseline window, or earlier only if
  ML1 pauses the project

## Baseline Capture Period

### Baseline Window

- Start: first controlled daily run after planning packet freeze
- End: tenth controlled daily run after planning packet freeze

### Purpose

This baseline exists to answer one question: does Slice 1 produce a trustworthy
minimum daily command layer before the project spends more time on later slices.

## Validation Review

### Review Criteria

- Slice 1 output set is explicit and reproducible
- citation coverage is measurable
- ambiguity is surfaced rather than hidden
- source boundaries remain intact
- slice-promotion decision can be made from observed evidence

### Review Owner

- ML1
- ML2

### Review Outcome

Status: Proposed
Notes: Planning packet drafted; slice-promotion thresholds still need ML1
review.

## ML1 Metric Approval

Approval Status: Proposed

Approved By: ______________________
Date: ______________________

### Metrics Submitted for Approval

- `daily_run_completion_rate`
- `citation_coverage_rate`
- `routed_matter_coverage`
- `ambiguous-thread-surfacing-rate`
- `reviewed-thread-state-disposition-rate`
- `false-authority-incidents`

### Proposed Thresholds

| Metric | Direction | Proposed Threshold |
| --- | --- | --- |
| `daily_run_completion_rate` | Higher is better | `>= 80%` across the 10-run baseline |
| `citation_coverage_rate` | Higher is better | `= 100%` in sampled asserted outputs |
| `routed_matter_coverage` | Higher is better | `>= 90%` of in-scope active matters represented in generated command outputs |
| `ambiguous-thread-surfacing-rate` | Higher is better | `= 100%` of sampled ambiguous threads surfaced explicitly |
| `reviewed-thread-state-disposition-rate` | Higher is better | `= 100%` of reviewed threads end in exactly one canonical state label |
| `false-authority-incidents` | Lower is better | `= 0` in the review window |

### Threshold Use

- promotion to Slice 2 should not be recommended unless the baseline window
  shows that Slice 1 is both useful and boundary-safe
- failing thresholds should default to narrowing, fixing, or pausing rather
  than automatic expansion

## Approval Note

This file is the authoritative source for LLP-023 metric logic. Existing
technical planning files in `planning/` may support implementation detail but
do not override this file.
