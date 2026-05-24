---
id: POL-026
title: Orchestrating Agent Final Output Issuance
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
tags: [policy, agents, outputs, authority]
---

# POL-026 — Orchestrating Agent Final Output Issuance

Policy Statement: Only the orchestrating agent for a governed run may issue the run's final output. Participating non-orchestrating agents may contribute artifacts, checks, or recommendations, but may not issue the final output unless they are explicitly assigned as the orchestrating agent for that run.
Authority (Principles referenced): PRN-020, PRN-025
Enforcement expectation: Final-output issuance outside the run's orchestrating agent is non-compliant and must be rejected or escalated. Final-output issuance is distinct from ML1 approval, publication, and external distribution permission.
Supersedes: None
Version: 1.0
Status: Active
