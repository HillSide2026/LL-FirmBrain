---
id: PRO-003
title: Novel Policy Gate
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
created_date: 2026-02-13
last_updated: 2026-02-13
tags: [protocol]
---

# PRO-003 — Novel Policy Gate

Enforces Policy: POL-003

Trigger condition: Output contains policy language or prescriptive rule changes.
Enforcement rule: If novel policy content is detected, then block and escalate.
Block condition: policy_novelty == true.
Escalation path: Escalate to ML1 with highlighted policy deltas and rationale.
Logging requirement: Record detected policy content and escalation in run log.
Version: 1.0
Status: Active
