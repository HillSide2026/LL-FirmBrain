---
id: PRO-019
title: Matter Summary and Task Governance
owner: ML1
status: approved
approval: ML1
approved_by: ML1
approved_date: 2026-04-18
version: 0.1
created_date: 2026-03-22
last_updated: 2026-03-22
tags: [protocol, matters, tasks, matter-brief, task-tracker]
---

# PRO-019 — Matter Summary and Task Governance

> **DRAFT — PENDING ML1 APPROVAL.**
> This protocol has not been approved and is not in effect.

---

## 1. Purpose

This protocol governs:

1. The per-matter summary file (`MATTER_BRIEF.md`) — its required content, creation, and currency rules
2. The firm-wide task surface (`LL_TASK_TRACKER.md`) — how tasks are identified, added, updated, and closed
3. The three canonical matter fields (Clio Status, Delivery Status, Fulfillment Status) — their definitions, source of truth, and permitted values

---

## 2. Matter Status Fields

Three canonical fields describe every matter. They are independent axes.

| Field | Level | Source of truth | Permitted values | Who sets it |
|-------|-------|----------------|-----------------|-------------|
| **Clio Status** | Matter | Clio (hardwired) | `Open`, `Closed`, `Pending` | Clio only |
| **Delivery Status** | Matter | Matter folder location in repo | `Essential`, `Strategic`, `Standard`, `Parked` | ML1 only |
| **Fulfillment Status** | Matter | MATTER.yaml in repo | `urgent`, `active`, `keep in view`, `dormant`, `closing` | ML1 only |

Note: `engagement_stage` is a client-level field (not a matter field) governed by POL-052. It does not appear in MATTER.yaml or any matter-level artifact.

### Secondary Operational Field

`Fulfillment Stage` is a secondary operational field, not a core canonical
matter field.

It is useful for guiding team workflow and handoffs and is governed by
`POL-034`, but it should not be presented as a peer to the three canonical
matter fields.

**Definitions:**

- **Delivery Status** reflects the business importance of the docketable work to the firm.
  - `Essential` — highest priority; active, revenue-critical, or relationship-critical work
  - `Strategic` — important but not immediately revenue-critical; relationship or positioning value
  - `Standard` — ordinary active matters; billable but not disproportionately important
  - `Parked` — not currently active; monitoring only

- **Fulfillment Status** reflects the operational priority state of the matter within its current stage.
  - `urgent` — immediate action required; delivery or deadline pressure
  - `active` — normal active state; work proceeding
  - `keep in view` — low or no immediate action; monitoring
  - `dormant` — presently inactive from an admin / ops perspective but not necessarily closed
  - `closing` — matter winding down toward Pending Close

- **Fulfillment Stage** is the secondary operational workflow guide for the
  matter (governed by `POL-034`).
  - `onboarding` — consult scheduled; engagement letter being prepared; `status = pending`
  - `opening` — engagement signed; matter setup underway; `status = open`
  - `maintenance` — necessary administration of matter; `status = open`
  - `pending_close` — work complete; administrative file closure; `status = pending`
  - `closed` — terminal; requires `close_reason` (`completed` / `declined` / `terminated`); `status = closed`

**Rules:**
- ML2 must never change any of these fields without explicit ML1 instruction.
- Delivery Status is encoded in the matter's folder path (e.g., `05_MATTERS/ESSENTIAL/`). The folder is the source of truth — if MATTER.yaml disagrees with the folder, flag to ML1.
- Fulfillment Stage is secondary and operational; it must not be treated as a fourth canonical field.
- Fulfillment Stage and Fulfillment Status are independent — any combination is valid (e.g., `maintenance` / `urgent`).

---

## 3. MATTER_BRIEF.md — Per-Matter Authoritative Summary

### 3.1 What it is

`MATTER_BRIEF.md` is the authoritative narrative summary of a matter. It is the primary reference for ML2 when reasoning about matter state, open questions, and current posture. It is maintained by the system, subject to ML1 override.

### 3.2 Required for

All **Essential**, **Strategic**, and **Standard** matters must have a `MATTER_BRIEF.md`. Parked matters may have one but are not required to.

### 3.3 Required structure

```markdown
## One-paragraph gist
[Single paragraph: client identity, matter type, current primary activity]

## Parties
[Client, counterparties, key contacts]

## What's happened so far
[Completed milestones in chronological order]

## Current posture
[State, primary activity, active work items]

## Near-term milestones
[What must happen next, in order]

## Open questions
[Unresolved items that may affect direction or scope]

## Change log
[Date — description of what changed and why]
```

### 3.4 Currency rules

A MATTER_BRIEF must be updated when:
- A task in `LL_TASK_TRACKER.md` moves to Completed for this matter
- ML1 confirms new scope, a new party, or a changed posture
- A new matter is created with Essential or Strategic delivery status
- An existing item in "Current posture" is resolved

ML2 must not update a MATTER_BRIEF based solely on SharePoint file activity or Gmail inference. Updates require ML1 confirmation of the underlying fact.

### 3.5 Creation rule

When a new Essential, Strategic, or Standard matter is created in the repo (new folder + MATTER.yaml), a stub MATTER_BRIEF.md must be created with the gist, parties, and current posture populated from available context. Stubs must not be left with placeholder text (`[TBD]`, `[list]`) indefinitely — ML2 should flag them for ML1 input at the next session.

---

## 4. LL_TASK_TRACKER.md — Firm-Wide Task Surface

### 4.1 What it is

`LL_TASK_TRACKER.md` is the system-maintained record of open matter-linked LL
Tasks owned by ML1. It is the primary task surface for ML2 to surface pending
matter work to ML1.

Location: `05_MATTERS/LL_TASK_TRACKER.md`

### 4.2 Required fields

| Field | Description |
|-------|-------------|
| Matter ID | Clio matter ID |
| Client | Client name |
| LL Task Type | LL Legal Task / LL Admin Task / LL Firm Management Task |
| Delivery Status | Essential / Strategic / Standard / Parked |
| Service | Service type (CAMLO, Counsel, Corporate, Regulatory, etc.) |
| Task | Specific, actionable description |
| Status | Open / In Progress / Waiting |
| Due | Due date if known |

### 4.3 Task status definitions

| Status | Meaning |
|--------|---------|
| `Open` | Not yet started |
| `In Progress` | Work underway |
| `Waiting` | Blocked — waiting on client, counterparty, or third party |

### 4.4 Governance rules

- **Only ML1 may confirm a task is open.** ML2 may propose tasks based on Gmail or SharePoint evidence but must not add them to the tracker without ML1 confirmation.
- **Completed tasks move to the Completed section** — never deleted. The Completed section is a permanent record.
- **Before adding any task, check the Completed section.** If the same task has already been completed on this matter, do not recreate it. A follow-up task is a new task with a distinct description.
- **Delivery Status must appear on every row.** It is not optional.
- **Tasks are classified.** Use `LL Legal Task`, `LL Admin Task`, or `LL Firm Management Task`; classify work by task type, not by professional role.
- **This tracker is matter-linked.** General firm tasks or project tasks belong in the LL Actions layer unless ML1 creates a dedicated artifact for them.

### 4.5 Task identification from Gmail

When ML2 is asked to scan Gmail for open tasks on a matter:

1. Search using Gmail MCP (`list_threads` or `list_messages`) with matter-relevant query terms (client name, counterparty name, matter keywords).
2. Identify threads where: (a) the most recent message is from a counterparty or client awaiting a response, or (b) ML1 has sent a message committing to a follow-up action.
3. Present findings to ML1 as **proposed tasks** — do not add to tracker without confirmation.
4. Record ML1's confirmation or rejection.

### 4.6 Task identification from SharePoint

SharePoint MCP provides folder/item metadata only — it cannot read file content. Task inference from SharePoint file names alone is unreliable and must not be used as the sole basis for a task proposal. Use file names to prompt ML1 for clarification, not to auto-generate tasks.

---

## 5. Matter Index

`05_MATTERS/INDEX.md` is updated on explicit ML1 instruction only. It is not an ML2-maintained artifact. See CLAUDE.md.

---

## 6. Scope

This protocol covers all matters tracked in `05_MATTERS/` (Essential, Strategic, Standard, Parked). It does not govern marketing matters, portfolio projects, or internal firm projects tracked elsewhere.

---

## 7. Approval Gate

This protocol becomes active only after ML1 review and explicit approval. Upon approval:
- Change `status` from `draft` to `active`
- Change `version` from `0.1` to `1.0`
- Update `last_updated`

---

## 8. Change Log

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-03-22 | Initial draft. Based on session work: Essential/Strategic MATTER_BRIEFs created, task tracker populated, status field semantics confirmed with ML1, CLAUDE.md governance rules added. |
