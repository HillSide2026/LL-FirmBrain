---
id: 01_doctrine__03_capability_profiles__sharepoint_update_site_page_content_md
title: Capability Profile: SharePoint.UpdateSitePageContent
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
created_date: 2026-03-28
last_updated: 2026-03-28
tags: [capability, sharepoint, mcp, sitepages]
---
# Capability Profile: SharePoint.UpdateSitePageContent (v0.2)

## Purpose
Apply page updates through the current Clients helper slice. This profile describes
the current helper implementation, not the full breadth of Clients site authority.

## Allowed Actions
- Update page title
- Update page description
- Update `innerHtml` for existing text web parts on existing `SitePages/*.aspx` pages
- Execute only when invoked by an approved workflow, runbook, or capability and run evidence is emitted into ML2

## Disallowed Actions
- This capability itself does not create, delete, rename, move, publish, or demote pages
- This capability itself does not alter layout, canvas structure, title area structure, navigation, permissions, sharing, retention, or site settings
- This capability itself does not create, delete, or reposition web parts
- This capability itself does not update standard web part configuration
- This capability does not define the full extent of authority over the broader `Clients` site

## Inputs (Typed)
- page_path: string (`SitePages/<name>.aspx`)
- expected_e_tag: string
- title: string (optional)
- description: string (optional)
- text_webparts: array of `{webpart_id: string, inner_html: string}` (optional)

## Outputs (Typed)
- page_id: string
- page_path: string
- updated_fields: array
- updated_webparts: array
- previous_e_tag: string
- new_e_tag: string
- web_url: string

## Required Logs
- page_path
- page_id
- updated field list
- updated webpart ids
- run identifier
- acting tool or agent
- artifact version reference
- provenance label
- reason code
- upstream artifact reference
- approval_reference when provided by the workflow governance layer

## Approval Mode
- Auto when the request stays within the current helper implementation, uses an approved workflow, runbook, or capability, and satisfies the active SharePoint write invariants.

## Boundary Rules
- The request MUST target an existing `SitePages/*.aspx` page in `/sites/Clients`.
- The request MUST include an expected page eTag for version-safe execution.
- The request MUST include artifact version reference and `Derived from ML2 vX.Y` provenance labeling or equivalent governed marker.
- The capability profile does not limit the broader Clients site authority.
