---
id: 01_doctrine__03_capability_profiles__sharepoint_list_folder_md
title: Capability Profile: SharePoint.ListFolder
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
tags: [capability, sharepoint, mcp]
---
# Capability Profile: SharePoint.ListFolder (v0.1)

## Purpose
Enumerate the children of a folder path within an approved SharePoint drive alias
without reading file contents.

## Allowed Actions
- List files and folders within an approved drive/path boundary
- Read metadata needed to identify names, types, sizes, modification times, and child counts
- Read the root of full-library Clients aliases when the runtime explicitly permits an empty path

## Disallowed Actions
- Reading file content
- Writing, moving, copying, deleting, or renaming items
- Enumerating outside the approved drive aliases and read prefixes

## Inputs (Typed)
- drive: string
- path: string

## Outputs (Typed)
- status: string
- operation_id: string
- target_ref: object
- result_payload:
  - entries: array<object>
- warnings: array
- errors: array
- executed_at: string

## Required Logs
- drive alias
- normalized path
- operation_id
- authorized scope
- result count
- output status

## Approval Mode
- Auto when the request stays within the approved read boundary for the selected drive alias.

## Boundary Rules
- The request MUST target an approved drive alias admitted by the active SharePoint MCP contract.
- The request MUST remain metadata-only.
- The request MUST respect the configured read prefixes for `legalmatters`, `documentation`, and `clients_*` aliases.
