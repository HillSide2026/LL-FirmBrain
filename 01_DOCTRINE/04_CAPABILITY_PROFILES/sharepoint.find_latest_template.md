---
id: 01_doctrine__03_capability_profiles__sharepoint_find_latest_template_md
title: Capability Profile: SharePoint.FindLatestTemplate
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
# Capability Profile: SharePoint.FindLatestTemplate (v0.2)

## Purpose
Find the latest template in an allowlisted Templates library.

## Allowed Actions
- Search templates by key/name
- Read metadata (name, modified time, version, URL)

## Disallowed Actions
- Writing or copying documents
- Reading outside allowlisted template sites/libraries

## Inputs (Typed)
- template_key: string
- template_library_id: string
- max_results: integer (default 10; max 20)

## Outputs (Typed)
- templates: array of
  - doc_id: string
  - name: string
  - version: string (optional)
  - last_modified_ts: string (ISO-8601)
  - url: string

## Required Logs
- template_key
- template_library_id
- result_count
- selected_doc_id (if any)

## Approval Mode
- Auto when the read satisfies `POL-059_Integration_Control_Policy.md` Section 2 read controls and remains within the approved template scope.

## Boundary Rules
- Read and search are permitted only within allowlisted template sites or libraries from `00_SYSTEM/security/sharepoint_allowlist.json`.
- Read authority remains bounded by the active site-class and read-control rules in `POL-059_Integration_Control_Policy.md`.
- No write, publish, or permission-changing behavior is authorized by this capability.
