---
id: 02_playbooks__readme_md
title: Playbooks
owner: ML1
status: draft
version: 1.0
supersedes:
created_date: 2026-01-25
last_updated: 2026-03-09
tags: []
---

## Playbook Header
Playbook ID: 02_playbooks__readme_md
Version: 1.0
Status: draft

Principles Referenced: PRN-001, PRN-002, PRN-003, PRN-004, PRN-005, PRN-006, PRN-008, PRN-009
Policies Applied: POL-003, POL-004, POL-006, POL-007, POL-009, POL-011
Protocols Enforced: PRO-003, PRO-004, PRO-006, PRO-007, PRO-009, PRO-011
Doctrine Invoked: 00_SYSTEM/constitution.md, 01_DOCTRINE/index.yaml

Inputs: TBD
Outputs: TBD
Acceptance Criteria: TBD


# Playbooks

Repeatable workflows and SOPs derived from doctrine.

## Module Architecture (Canonical)

Top-level structure:

```
02_PLAYBOOKS/
├── LL_OPERATIONS/              # Firm operations playbooks
├── CONTRACTS/                  # Contract practice area
├── CORPORATE/                  # Corporate practice area
├── FINANCIAL_SERVICES/         # Financial services practice area
├── TRADE_REMEDIES_MARKET_ACCESS/  # Trade remedies and market access practice area (draft)
├── _ASSETS/                    # Reusable non-workflow assets
└── _REGISTRY/                  # Indexes, policy, and structure controls
```

Practice area playbooks are organized under:

```
02_PLAYBOOKS/<PRACTICE_AREA>/WORKFLOWS/
```

Financial Services exception (approved structure target):

```
02_PLAYBOOKS/FINANCIAL_SERVICES/SOLUTIONS/[SPECIFIC_SOLUTION]/
  MODULES/
    [MODULE_ID]/
      WORKFLOWS/
      TEMPLATES/
      CHECKLISTS/
```

Hierarchy semantics for this exception:
- `Practice Area`: legal domain boundary
- `Solution`: productized offering
- `Module`: deliverable unit of work under a solution
- `Workflow`: procedural production path for a module deliverable

Strategies require ML1 approval to create. Each strategy folder must include:

- STRATEGY_SCOPE.md
- STRATEGY_ARCHITECTURE.md
- COMPONENT_SOLUTIONS.md
- RISK_SURFACE.md
- VERSION.md

Strategies are not playbooks. Playbooks remain the execution layer.

## Metadata Taxonomy

`CORE`, `SUBSTANTIVE`, `EXECUTION`, and `SYSTEM` are metadata categories, not directories.

Each workflow should encode taxonomy in metadata (for example `category` in `metadata.yaml`):
- `core`: lifecycle backbone workflows (intake/triage/scaffold/extract/update)
- `substantive`: legal-work workflows (review/draft/file/analyze)
- `execution`: deliverable-generation workflows (emails, memos, escalation packets)
- `system`: meta-workflows that modify ML2 itself

Operational workflows live under:
- `02_PLAYBOOKS/LL_OPERATIONS/`

Practice workflows live under:
- `02_PLAYBOOKS/CONTRACTS/WORKFLOWS/`
- `02_PLAYBOOKS/CORPORATE/WORKFLOWS/`
- `02_PLAYBOOKS/FINANCIAL_SERVICES/SOLUTIONS/[SPECIFIC_SOLUTION]/MODULES/[MODULE_ID]/WORKFLOWS/`

Legacy migration folders retained under `LL_OPERATIONS/`:
- `INBOX_TRIAGE_LEGACY/`
- `MATTER_DASHBOARD_LEGACY/`
- `STAGE3_LEGACY/`

Rules:
- Must include YAML frontmatter per `/00_SYSTEM/schemas/SCHEMAS.md`
- `version` and `supersedes` live in YAML frontmatter; Playbook Header `Version` must match `version`
- May reference doctrine IDs
- If a playbook conflicts with doctrine, doctrine wins
- Workflow folders should include `README.md`, `metadata.yaml`, `steps.yaml`, and `acceptance.md`.
- Non-workflow material belongs in `02_PLAYBOOKS/_ASSETS/`.
- `02_PLAYBOOKS/_REGISTRY/` contains policy, index, and migration records; no runnable workflows.

Registry: `02_PLAYBOOKS/_REGISTRY/README.md`
Playbook index: `02_PLAYBOOKS/_REGISTRY/PLAYBOOK_INDEX.md`
Status manifests (derived views): `02_PLAYBOOKS/_REGISTRY/ACTIVE_INDEX.md`, `02_PLAYBOOKS/_REGISTRY/DRAFT_INDEX.md`
Structure policy: `02_PLAYBOOKS/_REGISTRY/STRUCTURE_POLICY.md`
