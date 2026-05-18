---
id: 04_initiatives__system_portfolio__sys_003_sharepoint_integration__planning__scope_statement_md
title: SYS-003 SharePoint Integration - Scope Statement
status: planning
owner: ML2
last_updated: 2026-03-28
tags:
  - system-portfolio
  - sys-003
  - sharepoint
  - planning
doc_type: scope_statement
created_date: 2026-05-18
---

# SYS-003 SharePoint Integration - Scope Statement

## Project Context
- Project ID: `SYS-003`
- Project Path: `04_INITIATIVES/SYSTEM_PORTFOLIO/SYS-003_SHAREPOINT_INTEGRATION`
- Current Stage: `Planning`
- Planning Approval: `ML1 approved move to planning on 2026-03-28`

## Planning Purpose
This planning packet normalizes the currently active SharePoint integration surface so doctrine, control matrices, allowlists, and runtime behavior stay aligned. The planning goal is to describe the active admitted surface clearly, not to widen authority by implication.

## In Scope
- `LegalMatters` as a read-only governed workspace
- `Documentation` as a managed workspace
- `Clients` as a managed workspace
- Admitted helper tools and managed-site wrappers
- The boundary between doctrine, control matrix, allowlist, and runtime implementation

## Out of Scope
- Treating abstract doctrine language as already-implemented runtime
- Tenant-wide SharePoint authority
- Canonical ML2 storage inside SharePoint
- Unapproved cross-site mutation

## Boundary Condition
Planning for `SYS-003` freezes and normalizes the active SharePoint surface. It does not authorize wider site authority than the admitted runtime and control layer support.

## Gate Criteria
- Site-class and site-boundary rules are explicitly frozen
- Runtime-versus-doctrine distinctions are explicit
- Wrapper rules are explicit
- Authentication dependencies and gaps are explicit
- ML1 can judge the current surface and any later expansion from a coherent packet
