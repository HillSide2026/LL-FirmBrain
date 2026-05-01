---
id: llp-037_project_charter
title: LLP-037 Project Charter — LL System Design
owner: ML1
status: draft
created_date: 2026-05-01
last_updated: 2026-05-01
tags: [llp-037, system-design, charter]
---

# Project Charter

Project ID: LLP-037  
Project Path: `07_GROWTH_PROJECTS/LLP-037_LL_SYSTEM_DESIGN`  
Stage: Initiating

## Problem Statement Summary

Levine Law's technology stack has no authoritative system design document. Systems have been built, partially built, and planned in isolation. A repo analysis conducted in May 2026 revealed that:

- ll-task-tracker (Camunda-based matter platform) was built as a system of record but has now been superseded by Lexora as the authoritative matter SOR — the mirror architecture is not yet defined
- ll-corporate (client portal) has no document access path and no payment processing
- ll-corporate-records (Mayan EDMS) is an unintegrated 4-file stub with no API connections
- No Legal Work System exists — the layer between matter creation and document delivery is entirely absent
- The accounts lifecycle (billing, retainer, collections) is a 900-line backlog spec in ll-task-tracker but has not been built

Without a governed system design, these gaps cannot be prioritized or sequenced. Individual system builds proceed without a coherent target architecture.

See `PROBLEM_STATEMENT.md` for full analysis.

## Project Objectives

| ID | Objective |
|---|---|
| OBJ-01 | Produce and maintain an accurate current system map (`LL_CURRENT_SYSTEM.md`) |
| OBJ-02 | Produce and maintain an approved future system architecture (`LL_FUTURE_SYSTEM.md`) |
| OBJ-03 | Document and resolve all architectural open items via ML1-approved ADRs |
| OBJ-04 | Define requirements for the missing Legal Work System |
| OBJ-05 | Establish integration contracts between all future systems |

## Scope

### In Scope

- Current system map (all systems, roles, boundaries, integration state)
- Approved future system architecture (v0.1 approved 2026-05-01)
- Architectural decision records for all open items
- Requirements definition for missing Legal Work System
- Integration contract specifications

### Out of Scope

- Execution of individual system builds (separate LLP projects)
- Legal practice content
- Marketing architecture (LLP-025, LLP-011, LLP-012)

## Constraints

- All architectural decisions require ML1 approval
- No system integration or build work may commence without an approved design decision in this project
- ll-corporate must not evolve into a workflow engine or system of record (self-declared in its own README)
- Mayan EDMS must not be directly coupled to any system other than ll-corporate-records

## Stakeholders

| Role | Name / Agent | Involvement |
|---|---|---|
| Owner / Decision Authority | ML1 | All approvals, all decisions |
| Portfolio PM | LLM-004 | Stage gate compliance |

## Success Criteria

See `SUCCESS_CRITERIA.md`.

## Go Decision

**Go** — opening initiation stage. Current and future system documents drafted as first artifacts.
