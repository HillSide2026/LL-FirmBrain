---
id: llp-006__project_charter
title: LLP-006 Project Charter
owner: ML1
status: active
project_type: operational
created_date: 2026-03-07
last_updated: 2026-03-19
tags: []
---

# Project Charter

> **ML1-approved project packet. Current stage: Executing.**

**Project:** LLP-006 — Matter Maintenance
**Project ID:** LLP-006
**Project Type:** Operational
**Stage:** Executing

## 1. Purpose

Establish a repeatable, bounded matter maintenance function that keeps open matter records accurate, consistent, and action-ready across Clio, SharePoint, and Gmail. Produce a structured exception list for ML1 review on each maintenance cycle. Includes inbox governance and filing protocol.

This function is a specific scope of work assigned to a teammate within LL.
The governed system exists in part to monitor that teammate's maintenance work
so ML1 can see whether the open-matter base is actually being kept
reconciled and action-ready.

Downstream visibility overlays may build on this maintained base. In
particular, the Fulfillment Matter Queue depends on Matter Maintenance to keep
the open-matter base sufficiently reconciled that matters across onboarding,
opening, maintenance, and closing can be surfaced reliably to fee earners,
including which matters are docketing-ready.

## 2. Nature of Project

Operational — this is ongoing hygiene work, not a capability build. It has a bounded implementation phase (standing up the process) followed by a steady-state operating phase. It does not carry financial or strategic risk — only operational risk (scope, schedule, budget).

## 3. Deliverable

A running maintenance cycle that produces, on each execution:
- A matter exception list (stale records, missing folder links, unmapped Gmail threads, overdue items)
- A diff from the prior cycle (new exceptions, resolved exceptions)
- An ML1 action queue (items requiring judgment or authorization)
- Real filing (documents placed into correct SharePoint matter folders per filing protocol)
- Inbox governance (Gmail threads triaged, labeled, and linked to Clio matter IDs)

These outputs are administrative and reconciliation outputs first. They may be
be consumed by downstream layers such as the Fulfillment Matter Queue, but they
do not themselves determine delivery posture for fee earners.

## 4. Authority

Final approval authority: ML1. No maintenance action that modifies source-of-truth records (Clio, SharePoint, Gmail) may be taken without explicit ML1 authorization.

## 5. Promotion Path

Upon successful completion of the initiation, planning, and implementation stages, LLP-006 transitions to a standing operational function under `03_FIRM_OPERATIONS`. It does not close — it is promoted into operations.
