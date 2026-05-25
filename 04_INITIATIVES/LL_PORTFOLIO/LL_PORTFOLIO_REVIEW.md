---
id: 04_initiatives__ll_portfolio__ll_portfolio_review_md
title: LL Portfolio Review
owner: ML1
status: draft
created_date: 2026-04-03
last_updated: 2026-05-15
tags: [ll-portfolio, review, governance]
---

# LL Portfolio Review

## Purpose

Provide one obvious front door for reviewing the Levine Law portfolio.

This file does not replace the underlying artifacts. It tells ML1 where to
start, what order to read in, and which agent outputs are authoritative for
which review question.

## Operating Posture

LL review is program-led and matter-aware.

The top-level organizing structure is the numbered `LL_PORTFOLIO` program
structure. Individual matters do not organize LL at the top level.

The matter portfolio is the fast drill-down layer for delivery and fulfillment
visibility. ML1 shifts into the matter portfolio when the review question is
about client-service urgency, matter handling, WIP conversion, LL task
load, document-delivery status, or matter-level bottlenecks.

## Fastest Path

### If a current Chief of Staff packet exists

Start here:

1. `CHIEF_OF_STAFF/COS_BRIEF.md`
2. `CHIEF_OF_STAFF/ML1_DECISION_QUEUE.md`
3. `CHIEF_OF_STAFF/CROSS_AGENT_CONFLICTS.md` only if conflict review is needed

Treat the Chief of Staff packet as current only if its `Input freshness` line
is at least as recent as the latest `Generated` timestamp in the current
`LLM-004`, `LLM-005`, and `LLM-006` management outputs.

### If the Chief of Staff packet is stale or absent

Use this review order:

1. `LL_PROGRAM_SUMMARY_REPORT.md`
2. `03_FIRM_OPERATIONS/LLP-042/PORTFOLIO_STATUS_DASHBOARD.md`
3. `03_FIRM_OPERATIONS/PORTFOLIO_GOVERNANCE/GOVERNANCE_COMPLIANCE_AUDIT.md`
4. `03_FIRM_OPERATIONS/LLP-043/PROJECT_HEALTH_ROLLUP.md`
5. `../../05_MATTERS/DASHBOARDS/MATTER_DIGEST.md`
6. `../../05_MATTERS/LL_TASK_TRACKER.md`

This sequence gives:

- program-level posture first
- portfolio flow and capacity second
- structural integrity third
- project-by-project drill-down fourth
- matter-control visibility fifth

## Fast Shift To Matter Portfolio

Use this shift when the top-level LL review raises a delivery or fulfillment
question:

1. `LL_PORTFOLIO_REVIEW.md` identifies the relevant program-level concern.
2. `03_FIRM_OPERATIONS/LLP-042/PORTFOLIO_STATUS_DASHBOARD.md`
   shows whether the concern is portfolio flow, sequencing, or capacity.
3. `../../05_MATTERS/DASHBOARDS/MATTER_DIGEST.md` shows what matters ML1 should
   consider checking based on email, calendar, SharePoint, Clio, and Lexaro
   signals.
4. `../../05_MATTERS/DASHBOARDS/MATTER_INDEX.md` provides the full roster and
   matter-folder pointers for drill-down.

The matter digest and matter index are system tracking and visibility artifacts
for ML1. They help ML1 decide where to look next; they do not decide the exact
legal step, evaluate draft quality, or determine whether ML1 has failed to act.

## Canonical Review Stack

| Layer | Canonical File | Primary Use | Agent |
| --- | --- | --- | --- |
| Portfolio synthesis | `CHIEF_OF_STAFF/COS_BRIEF.md` | fastest narrative read for ML1 | `LLM-001` |
| Decision queue | `CHIEF_OF_STAFF/ML1_DECISION_QUEUE.md` | ranked ML1 decisions | `LLM-001` |
| Conflict check | `CHIEF_OF_STAFF/CROSS_AGENT_CONFLICTS.md` | identify flow-vs-governance conflict | `LLM-001` |
| Program summary | `LL_PROGRAM_SUMMARY_REPORT.md` | understand the 9 numbered programs | derived summary |
| Portfolio flow | `03_FIRM_OPERATIONS/LLP-042/PORTFOLIO_STATUS_DASHBOARD.md` | on-track / watch / at-risk, bottlenecks, sequencing | `LLM-005` |
| Structural integrity | `03_FIRM_OPERATIONS/PORTFOLIO_GOVERNANCE/GOVERNANCE_COMPLIANCE_AUDIT.md` | stage-gate, approval, metric, and schema gaps | `LLM-006` |
| Project drill-down | `03_FIRM_OPERATIONS/LLP-043/PROJECT_HEALTH_ROLLUP.md` | project-by-project review | `LLM-004` |
| Matter visibility | `../../05_MATTERS/DASHBOARDS/MATTER_DIGEST.md` | active / watch / urgent / stalled matter control read | matter command-and-control layer |
| Matter index | `../../05_MATTERS/DASHBOARDS/MATTER_INDEX.md` | full matter roster and current category/delivery posture | matter command-and-control layer |
| LL Tasks | `../../05_MATTERS/LL_TASK_TRACKER.md` | current LL task load and immediate action concentration | matter layer |

## Drill-Down Files

Open these after the four main review artifacts above when the question is more
specific:

- `03_FIRM_OPERATIONS/LLP-042/PROJECT_PRIORITY_MATRIX.md`
- `03_FIRM_OPERATIONS/LLP-042/SEQUENCING_RECOMMENDATIONS.md`
- `03_FIRM_OPERATIONS/LLP-042/BOTTLENECK_ANALYSIS.md`
- `03_FIRM_OPERATIONS/LLP-042/RESOURCE_COLLISION_REPORT.md`
- `03_FIRM_OPERATIONS/LLP-042/WIP_LOAD_ANALYSIS.md`
- `03_FIRM_OPERATIONS/PORTFOLIO_GOVERNANCE/STAGE_GATE_VIOLATION_REPORT.md`
- `03_FIRM_OPERATIONS/PORTFOLIO_GOVERNANCE/APPROVAL_GAP_REPORT.md`
- `03_FIRM_OPERATIONS/PORTFOLIO_GOVERNANCE/METRIC_SCHEMA_INTEGRITY_REPORT.md`
- `03_FIRM_OPERATIONS/PORTFOLIO_GOVERNANCE/DOCTRINE_DRIFT_REPORT.md`
- `../../05_MATTERS/DASHBOARDS/MATTER_INDEX.md`
- `../../05_MATTERS/LL_TASK_TRACKER.md`

## Agent Logic

The intended agent stack is:

1. `LLM-004` for project health and stage-gate review
2. `LLM-005` for flow, capacity, sequencing, and bottleneck review
3. `LLM-006` for structural and governance review
4. `LLM-001` for ML1-facing synthesis

Canonical agent specs:

- `00_SYSTEM/AGENTS/LLM-004_LLP-043_AGENT.md`
- `00_SYSTEM/AGENTS/LLM-005_LLP-042_AGENT.md`
- `00_SYSTEM/AGENTS/LLM-006_PORTFOLIO_GOVERNANCE_AGENT.md`
- `00_SYSTEM/AGENTS/LLM-001_CHIEF_OF_STAFF.md`

## Refresh Path

The deterministic management-agent refresh path is:

`python3 00_SYSTEM/scripts/run_ll_portfolio_agents.py`

That script refreshes the `LLM-004`, `LLM-005`, and `LLM-006` outputs. A fresh
`LLM-001` run should then read those refreshed outputs and update the canonical
files under `CHIEF_OF_STAFF/`.

## Canonical vs Legacy Chief of Staff Paths

Canonical Chief of Staff outputs live at:

- `04_INITIATIVES/LL_PORTFOLIO/CHIEF_OF_STAFF/`

Legacy duplicate pointer files still exist at:

- `04_INITIATIVES/LL_PORTFOLIO/03_FIRM_OPERATIONS/CHIEF_OF_STAFF/`

Those legacy duplicates are not authoritative and should not be used for ML1
review.
