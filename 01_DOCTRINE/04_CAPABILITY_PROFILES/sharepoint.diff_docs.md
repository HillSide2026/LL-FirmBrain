---
id: 01_doctrine__03_capability_profiles__sharepoint_diff_docs_md
title: Capability Profile: SharePoint.DiffDocs
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
# Capability Profile: SharePoint.DiffDocs (v0.2)

## Purpose
Generate a read-only diff summary between two SharePoint documents.

## Allowed Actions
- Read doc A and doc B
- Produce diff summary markdown artifact

## Disallowed Actions
- Writing changes back to either document
- Publishing

## Inputs (Typed)
- doc_a_id: string
- doc_b_id: string

## Outputs (Typed)
- diff_summary_md: string
- change_counts:
  - additions: integer
  - deletions: integer
  - edits: integer

## Required Logs
- doc_a_id, doc_b_id
- size estimates
- method identifier (e.g., "text-diff-v1")

## Approval Mode
- Auto when the underlying reads satisfy `POL-059_Integration_Control_Policy.md` Section 2 read controls.

## Boundary Rules
- Read-only.
- Reads are permitted only for documents inside the approved allowlisted comparison scope exposed by the active SharePoint integration contract.
- This capability does not authorize publish, overwrite, move, or metadata updates.
