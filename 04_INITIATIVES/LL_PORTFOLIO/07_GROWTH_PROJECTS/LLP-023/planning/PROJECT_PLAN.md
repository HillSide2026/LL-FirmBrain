---
id: 04_initiatives__ll_portfolio__07_growth_projects__llp_023_matter_command_control__planning__project_plan_md
title: Matter Command and Control - Project Plan
owner: ML1
status: draft
created_date: 2026-03-23
last_updated: 2026-03-28
tags: [matter-command-control, planning, project-plan]
---

# Project Plan

Project ID: `LLP-023`
Project Path: `04_INITIATIVES/LL_PORTFOLIO/07_GROWTH_PROJECTS/LLP-023`
Stage: `Planning`

## Planning Objective

Turn thin-slice experimentation into a governed, prioritized execution path for
the matter command layer.

## Core Planning Questions

1. What is the smallest command layer worth running daily?
2. What must be built first, and what must explicitly wait?
3. What evidence justifies moving from one slice to the next?
4. What controls prevent the command layer from becoming a shadow system?
5. How should the command layer distinguish ML1 visibility from ML1 action?
6. How should fulfillment escalation surface without pulling ordinary
   fulfillment handling back onto ML1?

## Planning Workstreams

| Workstream | Objective | Primary Output |
| --- | --- | --- |
| WS-01 Slice Prioritization | Freeze slice order, define deferrals, and decide what is not built yet | `SCOPE_STATEMENT.md`, this file |
| WS-02 Boundary Control | Freeze read-only, citation, cache, ambiguity-handling, and ML1-visibility-versus-action rules | `ASSUMPTIONS_CONSTRAINTS.md`, `RISK_REGISTER.md` |
| WS-03 Dependency Normalization | Identify what the command layer depends on across systems, config, and ML1 review | `DEPENDENCIES.md` |
| WS-04 Metrics and Gates | Define slice-promotion thresholds, ML1-action thresholds, and the evidence needed for ML1 review | `METRICS.md` |

## Priority Stack

| Priority | Slice | Why It Goes First / Later | What Is Explicitly Deferred |
| --- | --- | --- | --- |
| P1 | Slice 1 | Establish whether a daily derivative command layer plus a governed `25`-thread Gmail review pass is useful at all, while separating ML1 visibility from ML1 action | document deltas, deadline radar, comms drafts |
| P2 | Slice 2 | Add document visibility only after routing and daily packet logic are stable | deadlines and comms drafts |
| P3 | Slice 3 | Add deadline intelligence only if it is the next highest-value blind spot | comms drafts |
| P4 | Slice 4 | Drafting support is valuable only after trust, routing, and source discipline are proven | any autonomous communication behavior |

## Current Execution-Readiness Position

Planning is centered on proving that **Slice 1** is the minimum viable daily
command layer. In the current direction, each controlled daily pass reviews at
most `25` Gmail threads and each reviewed thread should end in exactly one
canonical state label through the governed Gmail label-write path. The current
packet uses a proposal-first pattern: the review pass writes a batch proposal to
`06_RUNS/batch/proposals/`, and any Gmail label execution happens only against
that bounded batch with an ML1 approval artifact and audit trail. Later slices
should not be built immediately simply because they are already conceptually
defined.

Slice 1 also needs to stop treating coarse rollups such as `ML Active` and
`ML Watch` as sufficient ML1 triage logic. The command layer should show:

- which matters remain visible to ML1
- which matters actually require ML1 action now
- which matters remain delegated to fulfillment
- which fulfillment issues have escalated back into the ML1-action layer

## Planning Milestones

| Milestone | Target Date | Evidence |
| --- | --- | --- |
| Slice order frozen | 2026-03-25 | `SCOPE_STATEMENT.md`, this file |
| Source-boundary rules frozen | 2026-03-26 | `ASSUMPTIONS_CONSTRAINTS.md`, `RISK_REGISTER.md` |
| Dependency packet frozen | 2026-03-27 | `DEPENDENCIES.md` |
| Metric and promotion logic frozen | 2026-03-28 | `METRICS.md` |
| ML1 prioritization packet assembled | 2026-03-29 | planning folder and updated `../initiation/APPROVAL_RECORD.md` |

## Resource Plan

| Role | Responsibility |
| --- | --- |
| ML1 | Final approval authority for slice order, boundaries, and promotion decisions |
| ML2 | Draft planning artifacts, implement bounded slice work only within approved limits |

## Immediate Planning Sprint

- freeze Slice 1 as the current minimum daily command layer
- freeze what will not be built yet
- define exactly what promotes Slice 2
- define the control tests that block shadow-system drift
- define how ambiguous routing is surfaced instead of hidden
- lock the `25`-thread daily review cap and the one-state-label-per-reviewed-thread rule
- define the ML1-decision fields that drive `Needs ML1 Review Today`
- define how fulfillment escalation is separated from ordinary fulfillment work

## Deferred Cleanup Backlog

The following doctrinal cleanup items are acknowledged and deferred for a
separate follow-on pass after the current terminology and boundary work:

1. Fulfillment Matter Queue README:
   replace the invalid `Active` example with `Docketing Active`.
2. Matter Docketing README:
   narrow authority language around `States` so it does not read as reclaiming
   Fulfillment Matter Queue state ownership.
3. Fulfillment Matter Queue tracker specs:
   replace phrases such as `source-of-truth files` and `Operations Queue Update Draft`
   so they align with the derivative, supplementary nature of the queue.

## Completion Condition

Planning is complete when ML1 can answer one question cleanly:

**Is the slice order correct, are the boundaries defensible, and is Slice 1
worth continuing under explicit promotion rules and clean ML1 triage logic?**
