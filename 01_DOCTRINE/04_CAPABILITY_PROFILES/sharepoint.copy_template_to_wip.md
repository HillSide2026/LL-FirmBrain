---
id: 01_doctrine__03_capability_profiles__sharepoint_copy_template_to_wip_md
title: Capability Profile: SharePoint.CopyTemplateToWIP
owner: ML1
status: approved
approved_by: ML1
approved_date: 2026-04-18
version: 0.2
effective_date: 2026-04-18
supersedes:
provenance:
  decided_by: ML1
  decided_on: 2026-04-18
  context: Metadata normalized by system admin cleanup on 2026-05-24
created_date: 2026-02-26
last_updated: 2026-03-28
tags: [capability, sharepoint, mcp]
---
# Capability Profile: SharePoint.CopyTemplateToWIP (v0.2)

## Purpose
Copy a selected template document into an allowlisted WIP destination for drafting.

## Allowed Actions
- Copy a document into a WIP folder allowlisted in `00_SYSTEM/security/sharepoint_allowlist.json`
- Execute only on a SharePoint site classified as `managed_workspace`
- Execute only when invoked by an approved workflow, runbook, or capability

## Disallowed Actions
- Writing outside allowlisted WIP destinations
- Publishing to final libraries
- Overwrite by default
- Copying into `read_only_authority` sites or unapproved destinations
- Modifying canonical ML2 artifacts or paths externally

## Inputs (Typed)
- source_doc_id: string
- dest_site_id: string
- dest_library_id: string
- dest_folder_path: string
- new_name: string
- overwrite: boolean (default false)

## Outputs (Typed)
- new_doc_id: string
- new_url: string

## Required Logs
- source_doc_id
- destination triple: dest_site_id, dest_library_id, dest_folder_path
- allowlist_check: pass/fail
- overwrite flag
- source_doc_id -> new_doc_id mapping
- run identifier
- acting tool or agent
- artifact version reference
- approval_reference when execution depends on an ML1-scoped exception

## Approval Mode
- Auto when destination scope is allowlisted, the target site class is `managed_workspace`, the call is part of an approved workflow/runbook/capability, and run evidence is emitted into ML2.

## Boundary Rules
- Destination MUST match an allowlisted WIP destination.
- The request MUST include artifact version reference and `Derived from ML2 vX.Y` provenance labeling or equivalent governed marker.
- Canonical ML2 artifacts must not be modified externally.
- If overwrite=true, require ML1 approval recorded through an `approval_reference`.
