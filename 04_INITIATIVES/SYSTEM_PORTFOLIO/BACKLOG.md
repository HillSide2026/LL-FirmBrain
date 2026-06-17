---
id: 04_initiatives__system_portfolio__backlog_md
title: System Portfolio Backlog
owner: ML1
status: draft
created_date: 2026-02-08
last_updated: 2026-06-17
tags: []
---

# System Portfolio Backlog

## Purpose
Centralized backlog for System Portfolio initiatives. Items here are candidates for
inclusion in active roadmaps but do not authorize execution by themselves.

## Backlog Rules
- Items must include: description, owner (or TBD), and dependencies (if any)
- Items are prioritized by ML1; agents may propose but not reorder
- Promoted items move to active roadmap stages; completed items are removed or archived
- Backlog does not create doctrine or authorize execution

---

## Candidate Items

| ID | Description | Owner | Dependencies | Priority | Status |
|----|-------------|-------|--------------|----------|--------|
| SYS-001 | Choose and implement agent runtime (Claude Code agents, MCP servers, or custom SDK) | ML1 | Stage 3 agent roster | P0 | candidate |
| SYS-002 | Formalize and govern the active Gmail integration surface (read plus controlled label writes) | Integration Steward | Stage 2 specs; active Gmail runtime | P1 | planning |
| SYS-003 | Formalize and govern the active SharePoint integration surface (LegalMatters read-only plus managed Documentation / Clients surfaces) | Integration Steward | Stage 2 specs; active SharePoint runtime | P1 | planning |
| SYS-004 | Define and stand up the Word/OneDrive document-access integration surface | Integration Steward | Stage 2 specs; scope clarification from Gmail and SharePoint lessons | P1 | planning |
| SMA-001 | Deploy and configure System Governance Agent | Runbook & QA | SYS-001 | P1 | candidate |
| SMA-002 | Deploy and configure Portfolio Planning Agent | Runbook & QA | SYS-001 | P1 | candidate |
| SMA-003 | Deploy and configure Integration Steward Agent | Runbook & QA | SYS-001 | P1 | candidate |
| SMA-004 | Deploy and configure Knowledge Curation Agent | Runbook & QA | SYS-001 | P1 | candidate |
| SMA-005 | Deploy and configure Runbook & QA Agent | Runbook & QA | SYS-001 | P1 | candidate |
| SYS-010 | Execute first operating cycle (weekly cadence test) | All Agents | SMA-001 to SMA-005 | P2 | candidate |
| SYS-011 | Archive completed Stage 3 + Stage 4 artifacts | Knowledge Curation | Stage closures approved | P2 | candidate |
| SYS-012 | Standardize per-solution module taxonomy in `02_PLAYBOOKS/FINANCIAL_SERVICES/SOLUTIONS` (define canonical module sets/names and replace placeholder `MODULE_001_PRIMARY`) | Playbook Governance | ML1 module architecture approval; existing solution packets | P1 | candidate |
| SYS-013 | Configure local Gmail MCP server on ML1 laptop so Gmail inbox is accessible via Claude Code CLI / VS Code (not just the claude.ai desktop app) | Integration Steward | Must be executed on the laptop to test credentials and config; reference `00_SYSTEM/integrations/gmail/README.md` | P2 | candidate |
| SYS-014 | Adapt upstream matter-control, onboarding, setup-doctor, command, and context-pack assets into local ML2 structures without importing the upstream `memory/` and `tasks/` model | ML1 | Existing local matter-control surfaces; `00_SYSTEM/retrieval/bundles.yaml`; explicit ML1 promotion from backlog before execution; draft plan at `04_INITIATIVES/SYSTEM_PORTFOLIO/00_DRAFT_ROADMAPS/SYS-014_UPSTREAM_ENABLEMENT_ADOPTION_PLAN.md` | P2 | candidate |

---

## Priority Legend
- **P0**: Blocking — must resolve before other work proceeds
- **P1**: High — core functionality, schedule ASAP
- **P2**: Medium — important but not blocking
- **P3**: Low — nice to have, schedule when capacity allows

---

## Recently Completed (for reference)
- **Stage 1**: System Discovery & Readiness Baseline — archived
- **Stage 2**: Read-Only Integration Foundation — archived
- **Stage 3**: System-Level Agent Orchestration — READY_FOR_CLOSURE
- **Stage 4**: Portfolio Operating Rhythm — OUTSTANDING

## How to Add Items
1. Add a row to the Candidate Items table
2. Assign an ID (sequential: SYS-001, SYS-002, etc.)
3. Leave Status as `candidate` until promoted to a roadmap stage
