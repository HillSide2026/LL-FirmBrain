---
id: 04_initiatives__system_portfolio__sys_002_gmail_integration__planning__risk_register_md
title: SYS-002 Gmail Integration - Risk Register
status: planning
owner: ML2
last_updated: 2026-03-28
tags:
  - system-portfolio
  - sys-002
  - gmail
  - planning
doc_type: risk_register
created_date: 2026-05-18
---

# SYS-002 Gmail Integration - Risk Register

## Canonical Categories
Per [POL-063](../../../../../01_DOCTRINE/03_POLICIES/POL-063_Project_Risk_Artifact_Lifecycle_Policy.md), this operational project uses:
- `Scope`
- `Schedule`
- `Budget`

## Scope Risks
| Risk | Category | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| Label behavior drifts from Matter Admin routing expectations | Scope | `medium` | `high` | Freeze admitted label semantics and keep routing logic aligned with actual label behavior |
| Send, archive, delete, or other mailbox mutation creeps in informally | Scope | `medium` | `high` | Keep Gmail authority explicit as read plus controlled label writes only; require separate ML1 approval for any new write class |
