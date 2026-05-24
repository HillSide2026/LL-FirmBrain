---
id: 01_doctrine__03_capability_profiles__sharepoint_review_site_page_md
title: Capability Profile: SharePoint.ReviewSitePage
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
# Capability Profile: SharePoint.ReviewSitePage (v0.2)

## Purpose
Review an existing SharePoint site page through the current Clients helper slice.

## Allowed Actions
- Read metadata for existing `SitePages/*.aspx` pages in `/sites/Clients`
- Read text web part content and supported web part inventory for review
- Review page links and plain-text page content for QC, ML1-requested review, or drift checks

## Disallowed Actions
- Editing page content
- Creating, deleting, moving, renaming, publishing, or demoting pages
- Altering page layout, navigation, permissions, sharing, retention, or site settings
- Inferring authority outside the current helper slice

## Inputs (Typed)
- page_path: string (`SitePages/<name>.aspx`)

## Outputs (Typed)
- page_id: string
- page_path: string
- title: string
- description: string
- e_tag: string
- page_text: string
- text_webparts: array
- standard_webparts: array
- web_url: string

## Required Logs
- page_path
- page_id
- read_scope
- operation_id
- acting tool or agent
- output status

## Approval Mode
- Auto when the request satisfies `POL-059_Integration_Control_Policy.md` read controls and remains within the current helper slice.

## Boundary Rules
- The request MUST target an existing `SitePages/*.aspx` page in `/sites/Clients`.
- The tool MUST remain read-only.
- The tool MUST NOT expose or infer authority for any non-`SitePages` Clients surface.
