---
id: llp-037_ll_system_design
title: LLP-037 LL System Design
owner: ML1
status: planning
project_stage: planning
created_date: 2026-05-01
last_updated: 2026-05-01
tags: [system-design, architecture, technology, infrastructure, phase-1, deployment]
---

# LLP-037 LL System Design

## Purpose

Establish and maintain the authoritative system design for Levine Law's technology stack. This project governs the current system map, the approved future system architecture, and all open design decisions required to close the gap between the two.

The immediate trigger is the identification of a missing Legal Work System — the layer between matter creation (Lexora) and document delivery (ll-corporate-records) — and the need to make a governed architectural decision about how to fill it.

## Scope

### In Scope

- Documented current system map (all systems, roles, boundaries, and integration points as they exist today)
- Approved future system architecture (Lead → Matter → Documents → Client Delivery)
- Identification and prioritization of missing system capabilities
- Architectural decision records (ADRs) for all ML1-level design decisions
- System boundary specifications for each component
- Integration contracts between systems (to be defined)

### Out of Scope

- Execution of individual system builds (each system build is a separate LLP project)
- Legal practice content or matter strategy
- Marketing and acquisition architecture (governed by LLP-025 and funnel projects)

## Planning Artifacts

- `planning/README.md` — planning packet index
- `planning/PHASE_1_DEPLOYMENT.md` — **Phase 1 scope: internal testing deployment at firm.levinellp.ca + engine.levinellp.ca**
- `planning/SCOPE_STATEMENT.md` — phase structure and planning stage scope

## Substantive Artifacts

| Artifact | Purpose |
|---|---|
| `LL_CURRENT_SYSTEM.md` | Map of all systems as they exist today — roles, boundaries, integration state |
| `LL_FUTURE_SYSTEM.md` | Approved v0.1 future architecture — Lead → Matter → Documents → Client Delivery |

## Initiation Artifacts

- `initiation/PROJECT_CHARTER.md`
- `initiation/PROBLEM_STATEMENT.md`
- `initiation/SUCCESS_CRITERIA.md`
- `initiation/STAKEHOLDERS.md`
- `initiation/RISK_SCAN.md`
- `initiation/APPROVAL_RECORD.md`

## Key Open Items

| Item | Blocking |
|---|---|
| Lexora sync model (push/pull, event shape) | ll-task-tracker rearchitecting |
| Accounts lifecycle ownership under Lexora model | Accounts backlog implementation |
| Legal Work System evaluation (Harvey / Legora candidates) | Document generation and delivery lifecycle |
| Retainer signup surface in ll-corporate | Conversion and onboarding flow |
| ll-corporate-records → Mayan API contract | Document ingestion from Legal Work System |

## ML1 Authority Statement

ML1 is the sole authority for all system design decisions, boundary changes, and architectural approvals. No system integration or build work may proceed without an approved design decision in this project.

## Approval State

**PLANNING** — Initiation complete. Phase 1 internal testing deployment scoped and ML1-approved 2026-05-01. Planning packet open.

## Last ML1 Review Date

`2026-05-01`
