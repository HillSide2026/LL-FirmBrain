---
id: 01_doctrine__rules__readme_md
title: Atomic Rules
owner: ML1
status: approved
approved_by: ML1
approved_date: 2026-04-18
version: 1.0
effective_date: 2026-04-18
supersedes:
provenance:
  decided_by: ML1
  decided_on: 2026-04-18
  context: Metadata normalized by system admin cleanup on 2026-05-24
created_date: 2026-02-13
last_updated: 2026-03-08
tags: [doctrine, rules]
---

# Atomic Rules

Definition: Executable rule fragments used by protocols to enforce policy checks.
Rules are direct instructions and should be machine-checkable wherever possible.
Boundary: Do not define policy intent or interpretive guidance; they implement checks.

Typical examples:
- All LL outputs must include required provenance metadata.
- Doctrine files must include required metadata fields.
- Playbooks must reference governing doctrine.
