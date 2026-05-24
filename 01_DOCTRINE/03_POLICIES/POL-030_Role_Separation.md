---
id: POL-030
title: Role Separation
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
last_updated: 2026-03-08
tags: [policy, roles, separation]
---

# POL-030 — Role Separation

Policy Statement: Agents, workers, and integration adapters must not be configured or used in ways that collapse orchestration, bounded execution, and external I/O into a single uncontrolled component.
Authority (Principles referenced): PRN-021, PRN-027
Enforcement expectation: Runtime configurations that collapse these roles are non-compliant and must be rejected or corrected before execution.
Supersedes: None
Version: 1.0
Status: Active
