---
id: 02_playbooks_financial_services_workflows_payments_readme_md
title: Financial Services — Payments
owner: ML1
status: draft
version: 1.0
supersedes:
created_date: 2026-02-08
last_updated: 2026-03-09
tags: []
---

## Playbook Header
Playbook ID: 02_playbooks__financial_services__payments__readme_md
Version: 1.0
Status: draft

Principles Referenced: PRN-001, PRN-002, PRN-003, PRN-004, PRN-006, PRN-009
Policies Applied: POL-004, POL-006, POL-009, POL-011
Protocols Enforced: PRO-004, PRO-006, PRO-009, PRO-011
Doctrine Invoked: 00_SYSTEM/constitution.md, 01_DOCTRINE/index.yaml

Inputs: TBD
Outputs: TBD
Acceptance Criteria: TBD


# Financial Services — Payments

Canonical location notice:
Canonical solution packets are maintained under:
`02_PLAYBOOKS/FINANCIAL_SERVICES/SOLUTIONS/[SPECIFIC_SOLUTION]/MODULES/[MODULE_ID]/{WORKFLOWS,TEMPLATES,CHECKLISTS}`.
This payments workflow container does not store canonical solution packets.

Architecture for payments advisory matters. This module defines solution frames, overlays, decision support, and agent infrastructure for the Payments practice area. It contains no legal or compliance analysis and no substantive requirements, thresholds, or procedures.

---

## Primary Solutions

| # | Solution | Folder |
|---|----------|--------|
| 1 | MSB_INTAKE_AND_REGISTRATION | [../../SOLUTIONS/MSB_INTAKE_AND_REGISTRATION/MODULES/MODULE_001_PRIMARY/WORKFLOWS/](../../SOLUTIONS/MSB_INTAKE_AND_REGISTRATION/MODULES/MODULE_001_PRIMARY/WORKFLOWS/) |
| 2 | MSB_REVIEW | [../../SOLUTIONS/MSB_REVIEW/MODULES/MODULE_001_PRIMARY/WORKFLOWS/](../../SOLUTIONS/MSB_REVIEW/MODULES/MODULE_001_PRIMARY/WORKFLOWS/) |
| 3 | FINTRAC_RESPONSE | [../../SOLUTIONS/FINTRAC_RESPONSE/MODULES/MODULE_001_PRIMARY/WORKFLOWS/](../../SOLUTIONS/FINTRAC_RESPONSE/MODULES/MODULE_001_PRIMARY/WORKFLOWS/) |
| 4 | RPAA_REGISTRATION | [../../SOLUTIONS/RPAA_REGISTRATION/MODULES/MODULE_001_PRIMARY/WORKFLOWS/](../../SOLUTIONS/RPAA_REGISTRATION/MODULES/MODULE_001_PRIMARY/WORKFLOWS/) |
| 5 | RPAA_THREE_YEAR_REVIEW | [../../SOLUTIONS/RPAA_THREE_YEAR_REVIEW/MODULES/MODULE_001_PRIMARY/WORKFLOWS/](../../SOLUTIONS/RPAA_THREE_YEAR_REVIEW/MODULES/MODULE_001_PRIMARY/WORKFLOWS/) |

---

## Overlays

Overlays are shared modules invoked by solutions. They are not solutions themselves.

| Overlay | Folder |
|---------|--------|
| AML/KYC Program | [overlays/aml_kyc_program/](overlays/aml_kyc_program/) |
| Rails | [overlays/rails/](overlays/rails/) |
| Crypto | [overlays/crypto/](overlays/crypto/) |

---

## Provider Agreements

Drafting and review of provider agreements lives in `02_PLAYBOOKS/CONTRACTS/WORKFLOWS` (not here). This practice area may reference provider agreement terms but does not produce or review them.

---

## Structure

| Directory / File | Purpose |
|------------------|---------|
| [../../SOLUTIONS/](../../SOLUTIONS/) | Canonical solution packet structure |
| [overlays/](overlays/) | Shared overlay modules (AML/KYC, Rails, Crypto) |
| [agents/](agents/) | Agent catalog, permissions, handoffs |
| [decision_lenses/](decision_lenses/) | Analytical frameworks |
| [failure_modes/](failure_modes/) | Known failure patterns |
| [initial_screening/](initial_screening/) | Internal front-door screening workflow for hybrid token/payment matters |
| [issue_maps/](issue_maps/) | Structured issue taxonomies |
| [question_banks/](question_banks/) | Intake and scoping questions |
| [regulatory_surfaces/](regulatory_surfaces/) | Statutory/regulatory touchpoints |
| [DECISION_REGISTRY.md](DECISION_REGISTRY.md) | Named decision points |
| [INTAKE_QUESTION_PACKS.md](INTAKE_QUESTION_PACKS.md) | Minimum viable fact sets per solution |
| [KNOWN_SAFE_DEFAULTS.md](KNOWN_SAFE_DEFAULTS.md) | Rebuttable default positions |
| [SOLUTION_COLLISION_MATRIX.md](SOLUTION_COLLISION_MATRIX.md) | Multi-solution routing |

---

## Operating Posture

Containment over completeness; explicit exit states; no assumed ongoing representation.
