---
id: 04_initiatives__system_portfolio__sys_003_sharepoint_integration__planning__risk_register_md
title: SYS-003 SharePoint Integration - Risk Register
status: planning
owner: ML2
last_updated: 2026-03-28
tags:
  - system-portfolio
  - sys-003
  - sharepoint
  - planning
doc_type: risk_register
created_date: 2026-05-18
---

# SYS-003 SharePoint Integration - Risk Register

## Canonical Categories
Per [POL-063](../../../../../01_DOCTRINE/03_POLICIES/POL-063_Project_Risk_Artifact_Lifecycle_Policy.md), this operational project uses:
- `Scope`
- `Schedule`
- `Budget`

## Scope Risks
| Risk | Category | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| Doctrine and runtime drift apart | Scope | `medium` | `high` | Keep doctrine, control matrix, allowlist, and runtime contract aligned through explicit live verification; monitor this risk |
| SharePoint REST authorization fails where Graph succeeds, blocking structural operations unexpectedly | Scope | `high` | `high` | Treat REST authorization as a separate dependency and verify it explicitly per admitted site; monitor this risk |
| Managed-site wrappers overstate authority if profiles, allowlists, and runtime do not match | Scope | `medium` | `high` | Freeze wrapper contracts and check them against active runtime implementation before operational use; monitor this risk |
| Site-boundary confusion causes `LegalMatters`, `Clients`, and `Documentation` to be treated as if they share one control model | Scope | `medium` | `high` | Keep site-specific governance explicit and forbid cross-site reasoning by analogy; monitor this risk |
