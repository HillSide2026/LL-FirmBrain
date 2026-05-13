# Project Plan

Project ID: LLP-001
Project Path: 01_ACCOUNTING/LLP-001_ACCOUNTING
Stage: Planning

## Planning Objective

Turn the newly clarified accounting scope into an execution-ready control packet
for historical fact maintenance, reconciliation, exception review, and bounded
handoff to LLP-002.

## Core Planning Questions

1. Which source systems and record classes are in the governed accounting fact packet?
2. What reconciliation cadence is realistic and sufficient for ML1 review?
3. Which exceptions must stop the packet, and which may remain open with explicit disclosure?
4. What facts may be handed into LLP-002, and under what freshness warnings?
5. What minimum metrics are needed before execution is authorized?
6. How will acquisition spend be tagged from 2026-07-01 onward so LLP-002 can budget one combined marketing + sales envelope without losing source detail?

## Planning Workstreams

| Workstream | Objective | Primary Output |
| --- | --- | --- |
| WS-01 Scope Lock | Freeze the fact-layer boundary and explicit exclusions | `SCOPE_STATEMENT.md`, this file |
| WS-02 Source and Cadence Design | Identify governed evidence sources and lock the reconciliation / close rhythm | `DEPENDENCIES.md`, `RISK_REGISTER.md` |
| WS-03 Exception Control | Define unresolved-item treatment, ML1 escalation points, and downstream warnings | `RISK_REGISTER.md`, `METRICS.md` |
| WS-04 Handoff and Gate Readiness | Define what LLP-002 may consume, including acquisition-spend actuals from 2026-07-01 onward, and what evidence supports execution approval | `METRICS.md`, updated `../initiation/APPROVAL_RECORD.md` |

## Execution Sequence

| Order | Step | Why It Comes Now |
| --- | --- | --- |
| 1 | Freeze the accounting fact boundary | Prevent planning drift into modeling or strategy |
| 2 | Identify the source systems and support package | Execution cannot be approved without evidence discipline |
| 3 | Lock the reconciliation and exception rhythm | Cadence determines whether the packet stays current enough to matter |
| 4 | Define acquisition-spend tagging for July onward | Budgeting should receive one combined acquisition actuals feed without losing source-level support |
| 5 | Define downstream handoff warnings and metrics | LLP-002 should consume facts only under explicit freshness and completeness rules |

## Planning Milestones

| Milestone | Target Date | Evidence |
| --- | --- | --- |
| Scope boundary frozen | 2026-05-16 | `SCOPE_STATEMENT.md` |
| Dependency and evidence map frozen | 2026-05-20 | `DEPENDENCIES.md` |
| Risk and exception model frozen | 2026-05-23 | `RISK_REGISTER.md` |
| Acquisition-spend classification rule frozen | 2026-05-24 | `SCOPE_STATEMENT.md`, `DEPENDENCIES.md`, `METRICS.md` |
| Metric package submitted for ML1 review | 2026-05-27 | `METRICS.md` |
| Planning gate packet assembled | 2026-05-30 | full `planning/` folder and updated `../initiation/APPROVAL_RECORD.md` |

## Resource Plan

| Role | Responsibility |
| --- | --- |
| ML1 | Final approval authority for boundaries, cadence, exceptions, and promotion decisions |
| Accounting / bookkeeping support | Provide source-record reality, reconciliation mechanics, and evidence availability constraints |
| ML2 | Draft artifacts, normalize structure, and maintain packet coherence under ML1 direction |

## Immediate Planning Sprint

- freeze the precise list of fact sources and evidence classes that belong in LLP-001
- define the minimum recurring reconciliation cycle worth governing
- define what constitutes an exception versus an acceptable timing lag
- define how acquisition spend is tagged beginning 2026-07-01, including the
  rollup rule that combines marketing + sales under one acquisition program
- define the warning model for incomplete or stale facts
- define the minimum fact packet LLP-002 may consume
- propose the first operating metrics for control and gate review

## Deferred Backlog

The following follow-on item is acknowledged as backlog for LLP-001 after the
current planning packet is locked:

1. Pull January-June 2026 actual acquisition spend from the LLP-001 fact layer,
   then document whether the LLP-001 `acquisition program` actuals category
   does or does not align exactly with the `acquisition` / `growth` line item
   used in the firm-level budget.

Backlog intent:

- LLP-001 should provide the historical actuals and the classification / bridge
  logic.
- LLP-002 should use that actuals feed and bridge logic to set the
  July-December 2026 acquisition budget for combined marketing + sales.
- If the categories do not align exactly, the backlog output should make the
  variance explicit rather than forcing a false one-to-one match.

## Completion Condition

Planning is complete when ML1 can answer one question cleanly:

Is there one defensible, bounded accounting control model that keeps LLP-001 in
historical fact, keeps exceptions visible, and gives LLP-002 only the facts it
may safely consume, including a clean acquisition-spend actuals feed beginning
2026-07-01?
