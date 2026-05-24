---
id: PRN-021
title: Layer Separation by Design
owner: ML1
status: approved
approved_by: ML1
approved_date: 2026-04-18
version: 1.1
effective_date: 2026-04-18
supersedes:
provenance:
  decided_by: ML1
  decided_on: 2026-04-18
  context: Metadata normalized by system admin cleanup on 2026-05-24
created_date: 2026-03-08
last_updated: 2026-03-28
tags: [principle, architecture, layering]
applies_to: [ML2, System, LL, HillSide]
---

# PRN-021 - Layer Separation by Design

Title: Layer Separation by Design

Statement:
Design workflows so governance decisions, enforcement logic, execution tasks, and integration transport remain separable and auditable. A change in one layer should not silently rewrite obligations in another.
Where Matter Administration and Matter File Administration both operate, they must remain distinct but linked layers; one may inform the other, but neither should silently absorb the other's role.

Rationale:
Separated layers improve auditability, reduce unintended coupling, preserve governance integrity during change, and prevent matter-state logic from being mistaken for Matter File authority.

Supersedes: None
Version: 1.1
Status: Active
