---
id: 01_doctrine__03_capability_profiles__sharepoint_manage_clients_site_md
title: Capability Profile: SharePoint.ManageClientsSite
owner: ML1
status: approved
approved_by: ML1
approved_date: 2026-04-18
version: 0.1
effective_date: 2026-04-18
supersedes:
provenance:
  decided_by: ML1
  decided_on: 2026-04-18
  context: Metadata normalized by system admin cleanup on 2026-05-24
created_date: 2026-03-28
last_updated: 2026-03-28
tags: [capability, sharepoint, clients, management]
---

# Capability Profile: SharePoint.ManageClientsSite (v0.1)

## Purpose
Provide broad site-wide authority for the `/sites/Clients` SharePoint workspace.

## Allowed Actions
- Get page, navigation, permission, site-structure, and site-settings metadata within `/sites/Clients`
- Create, update, publish, unpublish, set-home, and delete pages within `/sites/Clients`
- Create, update, and delete libraries within `/sites/Clients`
- Create, move, rename, and delete folders within `/sites/Clients`
- Get, upsert, reorder, and delete navigation nodes within `/sites/Clients`
- Get, grant, revoke, break inheritance, and restore inheritance for SharePoint principals within `/sites/Clients`
- Alter page layout, canvas structure, title area structure, and supported web-part configuration only through the admitted structured page operations in the wrapper
- Maintain shared portal pages, client-specific workspace pages, and client routing surfaces
- Execute only when invoked by an approved workflow, runbook, or capability and when run evidence is emitted into ML2

## Disallowed Actions
- Modifying ML2 canonical artifacts in place through SharePoint
- Expanding authority to other SharePoint sites by implication
- Writing to `LegalMatters` or any unapproved SharePoint site under this authority
- Altering tenant-wide identity management, retention, or compliance settings
- Enabling anonymous sharing, performing owner escalation, or mutating cross-site surfaces
- Performing operations outside the admitted `manage_clients_site` wrapper contract

## Inputs (Typed)
- site_path: string (`/sites/Clients`)
- operation: string
- target: object
- options: object
  - may include `approval_token` for ML1-gated operations
  - may include `dry_run`, `create_if_missing`, `overwrite`, `publish_after_update`, `expected_version`, and `reason`

## Outputs (Typed)
- status: string
- operation_id: string
- site_path: string
- operation: string
- target_ref: object
- changes_applied: array
- warnings: array
- errors: array
- approval_used: boolean

## Required Logs
- site_path
- target_ref
- operation
- structured target/options input record
- run identifier
- acting tool or agent
- success/failure state

## Approval Mode
- Auto for the wrapper operations admitted without ML1 token in the active Clients control matrix.
- `approval_token` required for the wrapper operations that the active Clients control matrix marks as ML1-gated.

## Boundary Rules
- The request MUST remain within `/sites/Clients`.
- The capability MUST not infer authority over any non-`Clients` SharePoint surface.
- `site.get_settings` is inspection-only under the admitted wrapper and does not authorize arbitrary site-settings mutation.
- The capability MUST satisfy the active SharePoint write invariants.
