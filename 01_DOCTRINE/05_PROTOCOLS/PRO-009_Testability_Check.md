---
id: PRO-009
title: Testability Check
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

# PRO-009 — Testability Check

Enforces Policy: POL-009

Trigger condition: Playbook or protocol is created, updated, or proposed for Active status.
Enforcement rule: If acceptance criteria or checks are missing, flag and block Active status.
Block condition: acceptance_criteria_missing == true OR verification_checks_missing == true.
Escalation path: Escalate to ML1 with required acceptance criteria or checks.
Logging requirement: Record missing testability elements and status in the audit log.
Version: 1.0
Status: Active
