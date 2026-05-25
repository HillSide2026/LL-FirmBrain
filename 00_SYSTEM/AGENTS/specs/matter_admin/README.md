---
id: 00_system__agents__specs__matter_admin__readme_md
title: Matter Administration Agents
owner: ML1
status: draft
created_date: 2026-03-05
last_updated: 2026-03-28
tags: []
---

# Matter Administration Agents

This folder defines Matter Administration Agent (MAA) charters used by
the matter-identity and matter-state layer of the Matter Command and Control
pipeline.

## Governing Doctrine
- `01_DOCTRINE/05_PROTOCOLS/PRO-029_Matter_Management_Protocol.md`
- `01_DOCTRINE/05_PROTOCOLS/PRO-030_Matter_Administration_Protocol.md`
- `01_DOCTRINE/01_INVARIANTS/INV-0017-matter-identity-authority-and-lifecycle.md`

## Run Graphs
- `00_SYSTEM/orchestration/run_graphs/matter_admin_daily.yaml`
- `00_SYSTEM/orchestration/run_graphs/matter_admin_one.yaml`

## Runner
- `scripts/run_matter_admin.py`

## Agents In Scope
- `MAA_MATTER_INDEX`
- `MAA_INBOX_ROUTER`
- `MAA_DEADLINE_EXTRACTOR`
- `MAA_COMMS_DRAFTER`
- `MAA_MATTER_DIGEST_COMPILER`

## Relationship to Matter File Administration
- Matter Administration governs matter identity, routing, status, deadlines,
  digesting, and other matter-level administrative signals.
- Matter Administration does not own canonical matter-record field changes;
  those are reserved to Matter Management.
- Matter File Administration governs the federated Matter File across
  SharePoint, Gmail, Clio, and other approved systems.
- The authoritative Matter File Admin charters live under
  `00_SYSTEM/AGENTS/specs/matter_file_admin/`.
- During the current transition, `scripts/run_matter_admin.py` still executes
  the active `agent_document_delta` step inside the bundled daily pipeline.

## System-of-Record Doctrine
- Clio = matter registry authority
- Gmail = communications authority
- SharePoint = document authority
- ML2 stores derived/admin artifacts plus source pointers only
