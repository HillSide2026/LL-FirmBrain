---
id: 04_initiatives_ll_portfolio_07_growth_projects_llp_023_matter_command_control_initiation_problem_statement_md
title: Problem Statement
owner: ML1
status: draft
created_date: 2026-05-18
last_updated: 2026-05-18
tags: []
---

# Problem Statement

Matter signals currently arrive across multiple systems with inconsistent
routing confidence and uneven daily visibility.

The current command layer also over-relies on coarse summary buckets such as
`ML Active` and `ML Watch`. Those rollups are useful as background context, but
they do not cleanly distinguish:

- matters ML1 should continue to see
- matters that actually require ML1 action now
- delegated fulfillment handling versus fulfillment escalation

Observed operational gaps:

1. Inbox threads are not always deterministically linked to matter numbers.
2. Daily matter briefing does not yet separate ML1 visibility from ML1 action.
3. Delegated fulfillment handling and fulfillment escalation are not yet
   surfaced consistently.
4. Matter movement vs. stall state is difficult to assess in one morning view.
5. Document truth and communication truth are distributed across systems.
6. Admin assertions are not always emitted with explicit source pointers.

Failure mode to avoid:
- A shadow database that drifts from Clio, SharePoint, and Gmail.
- A daily command surface that shows too many relevant matters without
  distinguishing actual ML1 decision pressure from ordinary delegated work.

Design requirement:
- ML2 stores only derived/admin artifacts and pointer-based citations to source
  systems.
- The command layer must preserve durable matter attributes such as
  `delivery_status` and `fulfillment_status`.
- The command layer must separately surface:
  - what remains visible to ML1
  - what requires ML1 action now
  - what remains delegated to fulfillment unless escalated
