---
id: 01_doctrine__03_capability_profiles__sharepoint_upload_draft_md
title: Capability Profile: SharePoint.UploadDraft
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
# Capability Profile: SharePoint.UploadDraft (v0.1)

## Purpose
Upload one draft file into the allowlisted Documentation `SB Execution/DRAFTS`
zone.

## Allowed Actions
- Upload one file into the hardcoded Documentation DRAFTS zone
- Execute only on the SharePoint site classified as `managed_workspace`
- Execute only when invoked by an approved workflow, runbook, or capability
- Record provenance, run identifiers, and write-context evidence for the upload

## Disallowed Actions
- Writing to any non-Documentation site
- Writing to any path outside the hardcoded allowlisted DRAFTS zone
- Publishing, finalizing, or moving the uploaded file outside the draft zone
- Omitting required write-context and provenance fields

## Inputs (Typed)
- filename: string
- content: string
- encoding: string (`utf-8` or `base64`)
- run_id: string
- workflow_ref: string (optional; one of workflow_ref, runbook_ref, or capability_ref is required)
- runbook_ref: string (optional; one of workflow_ref, runbook_ref, or capability_ref is required)
- capability_ref: string (optional; one of workflow_ref, runbook_ref, or capability_ref is required)
- artifact_version_ref: string
- provenance_label: string
- reason_code: string
- upstream_artifact_ref: string
- actor_id: string (optional)
- human_operator_id: string (optional)

## Outputs (Typed)
- status: string
- operation_id: string
- target_ref: object
- result_payload:
  - item: object
  - artifact_version_ref: string
  - provenance_label: string
  - run_id: string
- warnings: array
- errors: array
- executed_at: string

## Required Logs
- filename
- content length
- target site, library, and path
- run identifier
- workflow/runbook/capability reference
- artifact version reference
- provenance label
- reason code
- upstream artifact reference
- human operator id when present
- output status

## Approval Mode
- Auto when the request stays within the allowlisted Documentation DRAFTS zone, the target site class is `managed_workspace`, and the required write-context evidence is provided.

## Boundary Rules
- The target path is hardcoded to the allowlisted Documentation `SB Execution/DRAFTS` zone.
- `filename` MUST be a plain filename with no path separators or traversal sequences.
- The request MUST include artifact version reference and a provenance label beginning with `Derived from ML2 v`.
- This capability validates provenance inputs but does not itself persist them as SharePoint metadata.
