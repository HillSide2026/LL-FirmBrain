---
id: 04_initiatives__system_portfolio__sys_003_sharepoint_integration__planning__dependencies_md
title: SYS-003 SharePoint Integration - Dependencies
status: planning
owner: ML2
last_updated: 2026-03-28
tags:
  - system-portfolio
  - sys-003
  - sharepoint
  - planning
doc_type: dependencies
created_date: 2026-05-18
---

# SYS-003 SharePoint Integration - Dependencies

| Dependency | Type | Why It Matters | Current State |
|---|---|---|---|
| Azure app credentials | Runtime auth | Required for all admitted access | `active` |
| Microsoft Graph access | Runtime auth | Required for most active runtime operations | `active` |
| SharePoint REST authorization | Runtime auth | Required for some structural site operations | `partial / site-dependent` |
| Allowlist and control matrix | Governance | Defines admitted authority boundary | `active` |
| SharePoint MCP server and integration scripts | Runtime | Defines actual implemented surface | `active` |
| Live verification discipline | Governance | Required to keep doctrine and runtime aligned | `active` |
