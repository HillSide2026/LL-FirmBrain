---
id: POL-070
title: Backlog Routing Policy
version: '1.0'
status: approved
owner: ML1
created_date: 2026-05-17
last_updated: 2026-05-17
tags: [backlog, routing, system, personal]
---

# POL-070 — Backlog Routing Policy

## Purpose

Define which backlog file receives a given candidate item, so that system-level
work and personal to-do items do not accumulate in the wrong location.

## Backlog and Action Files

| Artifact | Path | Receives |
|----------|------|----------|
| System Portfolio Backlog | `04_INITIATIVES/SYSTEM_PORTFOLIO/BACKLOG.md` | System-level work items |
| Personal Actions Backlog | `04_INITIATIVES/HillSide_PORTFOLIO/PERSONAL_PROJECTS/PERSONAL_ACTIONS/BACKLOG.md` | ML1 personal action items |
| LL Actions Hub | `05_MATTERS/LL_ACTIONS/README.md` | Index only — routes to `LL_TASK_TRACKER.md` and content backlogs |

## Routing Rules

### System Portfolio Backlog
An item belongs here if it concerns the architecture, configuration, or operation
of the ML2 system itself — including:
- MCP server setup or changes
- Agent deployment or configuration
- Integration surface changes (Gmail, SharePoint, etc.)
- Repo structure, doctrine, or governance changes
- Automation, scripts, or tooling that operates on the system

### Personal To-Do Backlog
An item belongs here if it is a personal obligation or action for ML1 that is
not a Levine Law task — including:
- Advisor follow-ups
- Personal appointments or commitments
- HillSide / personal project next steps
- Items with no system execution component

### LL Actions Hub
An item belongs in the LL Actions layer if it is Levine Law work. Classify it as:
- `LL Legal Task` for client or matter work involving legal judgment, legal
  delivery, matter strategy, drafting, review, negotiation, filing, or
  client-facing legal advice
- `LL Admin Task` for matter administration, file closing, collections, client
  authorization, document chasing, internal follow-up, or other non-substantive
  matter support
- `LL Firm Management Task` for Levine Law management work not tied to a single
  client matter, including operations, finance, marketing, staffing, systems,
  and strategy

Classify LL work by task type, not by professional role.

## Routing Decision

If an item could plausibly go in either backlog, ask: **does this require a
change to the system or its configuration?** If yes → System Portfolio Backlog.
If it is purely an ML1 action with no system component → Personal To-Do Backlog.

## Agent Capture Rule

When capturing items during a session:
1. Classify first using the routing rules above.
2. Add to the correct backlog file without waiting for ML1 instruction.
3. Do not add the same item to both files.
