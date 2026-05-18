---
id: 04_initiatives__system_portfolio__sys_004_word_onedrive_integration__planning__risk_register_md
title: SYS-004 Word / OneDrive Integration - Risk Register
status: planning
owner: ML2
last_updated: 2026-03-28
tags:
  - system-portfolio
  - sys-004
  - word
  - onedrive
  - planning
doc_type: risk_register
created_date: 2026-05-18
---

# SYS-004 Word / OneDrive Integration - Risk Register

## Canonical Categories
Per [POL-063](../../../../../01_DOCTRINE/03_POLICIES/POL-063_Project_Risk_Artifact_Lifecycle_Policy.md), this operational project uses:
- `Scope`
- `Schedule`
- `Budget`

## Scope Risks
| Risk | Category | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| The lane duplicates SharePoint or Drive without solving a distinct problem | Scope | `medium` | `high` | Require an explicit use-case and overlap review before any implementation decision |
| Expectations drift toward editing or publishing authority before the lane is justified | Scope | `medium` | `high` | Keep the packet explicit that planning does not admit document mutation or publish authority |
| Microsoft auth and document-surface complexity outweigh the value of the lane | Scope | `medium` | `medium` | Treat auth and dependency analysis as gating work before any build decision |

## Schedule Risks
| Risk | Category | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| Planning is mistaken for approval to implement | Schedule | `medium` | `high` | Keep all planning artifacts explicit that `SYS-004` remains exploratory and execution is not approved |
