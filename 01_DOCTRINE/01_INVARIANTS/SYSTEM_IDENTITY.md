---
id: 00_system__system_identity_md
title: System Identity — LL Second Brain (ML2)
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
created_date: 2026-01-25
last_updated: 2026-03-21
tags: []
---

# System Identity — LL Second Brain (ML2)

## What This Repository Is
This repository is the **Second Brain system-of-record (ML2)** for Matthew Levine and Levine Law.

It contains:
- binding system doctrine
- approved playbooks and templates
- governed structures for initiatives, matters, and execution
- auditable outputs derived from approved artifacts
- automation configuration in `.claude/` that governs execution (version-controlled, non-canon)

ML2 exists to preserve and govern ML1's decisions consistently over time; the System applies them during runtime.

## What This Repository Is Not
This repository is **not**:
- a client matter workspace
- a project scratchpad
- a place for ad hoc notes or drafts
- an execution environment for live legal work

Project- or matter-specific materials belong only in their designated directories and never originate doctrine by default.

## Authority and Control
- **ML1 (Matthew Levine)** is the sole authority for doctrine, structure, and exceptions.
- Changes to doctrine, templates, or system rules require explicit approval.
- Levine Law (LL) consumes only approved outputs generated from this system.

## Change Discipline
- `main` is protected.
- All changes are made via pull request.
- Structural or governance changes are classified as **System / Governance** artifacts.

This file defines the identity boundary of the system.
