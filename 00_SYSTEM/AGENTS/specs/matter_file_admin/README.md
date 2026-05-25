---
id: 00_system__agents__specs__matter_file_admin__readme_md
title: Matter File Administration Agents
owner: ML1
status: draft
created_date: 2026-03-28
last_updated: 2026-03-28
tags: []
---

# Matter File Administration Agents

This folder defines Matter File Administration Agent (MFA) charters used by
the Matter File Administration layer of Matter Command and Control.

Matter File Administration is distinct from Matter Administration. It governs
the federated Matter File across external systems, with emphasis on:

- matter-to-system mapping
- SharePoint folder protocol assessment
- authoritative-source verification
- document inventory and delta tracking

## Governing Doctrine
- `01_DOCTRINE/05_PROTOCOLS/PRO-029_Matter_Management_Protocol.md`
- `01_DOCTRINE/05_PROTOCOLS/PRO-031_Matter_File_Administration_Protocol.md`
- `01_DOCTRINE/05_PROTOCOLS/PRO-020_LL_Matters_SharePoint_Protocol.md`
- `01_DOCTRINE/05_PROTOCOLS/PRO-021_LL_Matters_Folder_Protocol.md`
- `01_DOCTRINE/05_PROTOCOLS/PRO-022_LL_Matters_File_Protocol.md`
- `01_DOCTRINE/03_POLICIES/POL-067_Matter_Authoritative_Source_Verification_Requirement.md`

## Run Graphs
- `00_SYSTEM/orchestration/run_graphs/matter_file_admin_daily.yaml`
- `00_SYSTEM/orchestration/run_graphs/matter_file_admin_one.yaml`

## Transitional Execution Note
- The doctrinal split is defined here now.
- Runtime execution is still partially bundled inside
  `scripts/run_matter_admin.py`.
- The active `agent_document_delta` step remains live during that transition.

## Agents In Scope
- `MFA_MATTER_FILE_MAP`
- `MFA_FOLDER_PROTOCOL`
- `MFA_DOCUMENT_DELTA`
- `MFA_AUTHORITY_VERIFIER`

## Relationship to Matter Administration
- Matter Administration answers: what matter is this, what is its status, what
  inbox traffic belongs to it, and what needs attention today.
- Matter File Administration answers: where does the Matter File live across
  systems, which SharePoint folders belong, how should protocol compliance be
  described, and what source claims remain unresolved.
- Matter File Administration may inform but may not rewrite canonical
  matter-record fields.
