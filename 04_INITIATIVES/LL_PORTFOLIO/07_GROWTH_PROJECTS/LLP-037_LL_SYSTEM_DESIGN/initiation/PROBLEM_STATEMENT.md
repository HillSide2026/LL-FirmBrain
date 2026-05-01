---
id: llp-037_problem_statement
title: LLP-037 Problem Statement — LL System Design
owner: ML1
status: draft
created_date: 2026-05-01
last_updated: 2026-05-01
tags: [llp-037, system-design, problem-statement]
---

# Problem Statement

## Background

A direct analysis of three repositories (ll-corporate, ll-corporate-records, LL-task-tracker) was conducted in May 2026. The following findings are based on actual file and code inspection, not assumptions.

## Finding 1: No Legal Work Execution Layer Exists

The full end-to-end flow for a corporate legal service is:

```
Lead → Matter → Legal Work → Documents → Client Delivery
```

The following layers exist in some form:
- Lead capture (GHL)
- Matter creation and admin lifecycle (ll-task-tracker)
- Client portal (ll-corporate)
- Document storage stub (ll-corporate-records)

The layer between matter activation and document delivery — legal work execution — does not exist anywhere. No system tracks what work needs to be done for a given matter type, who is doing it, what documents have been produced, or when delivery is complete.

Evidence: The LL-task-tracker accounts backlog (`docs/backlog/accounts-lifecycle-system.md`, Section 23) names a "Delivery system" with a `markReadyToDeliver` transition as a planned cross-system coordination point. No such system has been built.

## Finding 2: ll-corporate-records Is an Unintegrated Stub

ll-corporate-records contains 4 tracked files. Its `docker-compose.yml` references `mayanedms/mayanedms:latest` as an external Docker Hub image — Mayan EDMS is not embedded. There is:
- No API client code
- No integration with ll-task-tracker
- No integration with ll-corporate
- No document type definitions or workflow configurations tracked in git

Documents cannot flow in or out of this system.

## Finding 3: ll-task-tracker Is Built as a System of Record, Not a Mirror

The ML1-approved future architecture designates Lexora as the authoritative system of record for matter state, with ll-task-tracker operating as a mirror for admin and accounts workflows. However, ll-task-tracker was built as a primary system — it runs a live Camunda 7 workflow engine, has its own authorization policy (OPA), and the authority map (`contracts/domain/AUTHORITY-MAP.md`) declares ll-task-tracker as the canonical owner of the Matter domain.

Rearchitecting ll-task-tracker as a mirror requires specifying the Lexora sync model (event shape, direction, consistency guarantees). This has not been done.

## Finding 4: Accounts Lifecycle Is Planned but Not Built

A 900-line specification for the accounts lifecycle (`docs/backlog/accounts-lifecycle-system.md`) exists in ll-task-tracker. It defines 6 matter types, 14 states, 16 transitions, and cross-lifecycle coordination rules. None of it has been implemented. Under the new architecture, it is also unclear whether the accounts lifecycle is owned by ll-task-tracker or Lexora.

## Finding 5: ll-corporate Has No Payment or Document Capability

ll-corporate displays a service catalog with prices (`src/lib/services/catalog.ts`) but has no payment processor integration, no retainer setup flow, and no document retrieval path. The future architecture assigns retainer signup to ll-corporate. This requires building capability that does not currently exist.

## Impact of These Gaps

Without a governed system design:
- Legal work cannot be tracked or delivered systematically
- Documents cannot be stored or retrieved
- The conversion funnel cannot be completed (no retainer signup)
- The accounts lifecycle cannot be built without knowing which system owns it
- ll-task-tracker cannot be rearchitected as a mirror without a defined Lexora sync model
- Individual system builds proceed without a coherent target architecture, increasing the risk of further integration debt
