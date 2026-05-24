---
id: INV-0004
title: Worker Boundary and Final Output Issuance
owner: ML1
status: approved
approved_by: ML1
approved_date: 2026-04-18
version: 1.0
effective_date: 2026-04-18
supersedes:
provenance:
  decided_by: ML1
  decided_on: 2026-04-18
  context: Metadata normalized by system admin cleanup on 2026-05-24
created_date: 2026-03-08
last_updated: 2026-03-23
tags: [invariant, workers, agents, outputs, authority]
---

# Worker Boundary and Final Output Issuance (Binding Invariant)

## Invariant
1. `Worker` is the canonical term for scoped task executors invoked by an orchestrating agent.
2. `Subagent` is a synonym of `Worker` and does not define a separate authority class.
3. Workers may perform only bounded tasks such as classification, extraction, drafting, QA checks, formatting, and structured analysis.
4. Workers may not orchestrate runs.
5. Workers may not issue final outputs.

## Implication
Workers cannot issue the terminal output of a governed run. They may contribute intermediate artifacts only; final-output issuance belongs to the run's orchestrating agent.

## Boundary
This invariant defines role identity and authority boundaries.
Policies and protocols define enforcement mechanics, validation checks, and escalation handling.
