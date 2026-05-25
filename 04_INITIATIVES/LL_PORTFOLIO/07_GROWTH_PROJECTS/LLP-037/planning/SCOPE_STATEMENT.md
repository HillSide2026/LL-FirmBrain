---
id: llp-037_planning_scope_statement
title: LLP-037 Scope Statement
owner: ML1
status: draft
created_date: 2026-05-01
last_updated: 2026-05-01
tags: [llp-037, planning, scope]
---

# Scope Statement

Project ID: `LLP-037`  
Project Path: `04_INITIATIVES/LL_PORTFOLIO/07_GROWTH_PROJECTS/LLP-037`  
Stage: `Planning`

## Planning Use

This project governs the system design for Levine Law's technology stack across two horizons:

1. **Current system documentation** — accurate record of the operational stack (Clio + SharePoint + Gmail + GHL + Asana + ll-secondbrain) for use as a baseline
2. **Future system architecture** — approved v0.1 design (Lead → Matter → Documents → Client Delivery) with open items tracked to resolution

The planning stage is organized by phases of implementation. Each phase is a discrete, scoped deployment or build effort. Phases do not need to be sequential in time but must have explicit scope boundaries and exclusions.

## In Scope — Planning Stage

- Phase 1 internal testing deployment (firm.levinellp.ca + engine.levinellp.ca) — see `PHASE_1_DEPLOYMENT.md`
- Resolution of open items OI-01 through OI-06 from `LL_FUTURE_SYSTEM.md` via ML1 decisions
- Integration contract specifications for LL-WrkEngine ↔ Lexora, LL-WrkEngine ↔ ll-corporate-records, ll-task-tracker ↔ Lexora
- LL-WrkEngine corporate service workflow template backlog (Phase 2 prep)
- AGPL-3.0 compliance assessment for LL-WrkEngine (OI-03b)

## Out of Scope — Planning Stage

- Execution of individual system builds (each has its own LLP project)
- Legal practice content or matter strategy
- Marketing architecture

## Phase Structure

| Phase | Name | Status |
|---|---|---|
| Phase 1 | Internal Testing Deployment | Scoped — see `PHASE_1_DEPLOYMENT.md` |
| Phase 2 | Integration and Workflow Build | Not yet scoped |
| Phase 3 | Client Portal Activation | Not yet scoped |
