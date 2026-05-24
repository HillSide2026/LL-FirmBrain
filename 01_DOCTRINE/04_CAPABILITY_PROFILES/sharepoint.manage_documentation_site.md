---
id: 01_doctrine__03_capability_profiles__sharepoint_manage_documentation_site_md
title: Capability Profile: SharePoint.ManageDocumentationSite
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
tags: [capability, sharepoint, documentation, management]
---
# Capability Profile: SharePoint.ManageDocumentationSite (v0.1)

## Purpose
Formalize the broad-wrapper pattern for the `/sites/Documentation` SharePoint
managed workspace.

## Allowed Actions
- Get page, navigation, permission, site-structure, and site-settings metadata within `/sites/Documentation`
- Create, update, publish, unpublish, set-home, and delete pages within `/sites/Documentation`
- Create, update, and delete libraries within `/sites/Documentation`
- Create, move, rename, and delete folders within `/sites/Documentation`
- Get, upsert, reorder, and delete navigation nodes within `/sites/Documentation`
- Get, grant, revoke, break inheritance, and restore inheritance for SharePoint principals within `/sites/Documentation`
- Alter page layout, canvas structure, title area structure, and supported web-part configuration only through an admitted structured wrapper contract
- Execute only when invoked by an approved workflow, runbook, or capability and when run evidence is emitted into ML2

## Disallowed Actions
- Modifying ML2 canonical artifacts in place through SharePoint
- Expanding authority to any non-Documentation SharePoint site by implication
- Altering tenant-wide identity management, retention, or compliance settings
- Enabling anonymous sharing, performing owner escalation, or mutating cross-site surfaces
- Treating this profile as proof that a dedicated Documentation broad-wrapper tool is already exposed

## Inputs (Typed)
- site_path: string (`/sites/Documentation`)
- operation: string
- target: object
- options: object
  - may include `approval_token` for ML1-gated operations in a future admitted wrapper
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
- executed_at: string

## Required Logs
- site_path
- target_ref
- operation
- structured target/options input record
- run identifier
- acting tool or agent
- success/failure state

## Approval Mode
- Draft formalization only. This profile describes the intended broad-wrapper pattern for Documentation.
- Until a dedicated `manage_documentation_site` wrapper is admitted into the active MCP runtime, current Documentation MCP exposure remains bounded to the narrower documented tools.

## Boundary Rules
- The request MUST remain within `/sites/Documentation`.
- This profile MUST not be read as authority over `LegalMatters`, `Clients`, or any non-Documentation SharePoint surface.
- If a dedicated wrapper is later admitted, destructive and permission-bearing operations should follow the same explicit token-gated pattern used by the governed Clients wrapper.
