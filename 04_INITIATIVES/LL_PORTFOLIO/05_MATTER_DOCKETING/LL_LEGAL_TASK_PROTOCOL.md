---
id: 04_initiatives__ll_portfolio__05_matter_docketing__ll_legal_task_protocol_md
title: LL Legal Task Protocol
owner: ML1
status: draft
created_date: 2026-02-08
last_updated: 2026-05-17
tags: [ll, legal-tasks, matter-docketing]
---

# LL Legal Task Protocol

**Location:** `LL_PORTFOLIO/05_MATTER_DOCKETING/`

**Status:** Draft — Requires ML1 Approval

---

## 1. Purpose

This protocol defines how **LL Legal Tasks** are created, updated, and consumed
within a matter's delivery workflow.

The goal is to provide:

* A clear view of client and matter legal work that requires action
* Tight alignment with the **Fulfillment Matter Queue** for delivery/docketing
* Clear separation from LL Admin Tasks and LL Firm Management Tasks

The task list is an operational aid, not a task manager of record and not a
system of judgment.

---

## 2. Scope & Non-Scope

### In Scope

* LL Legal Tasks tied to an existing matter
* Tasks that advance, unblock, or close delivery Activity Periods
* Tasks that require legal judgment, drafting, review, negotiation, filing,
  coordination, or client-facing legal advice

### Explicitly Out of Scope

* Billing, invoicing, collections, trust accounting
* Internal admin or HR tasks
* Marketing, intake, or pre-engagement work
* Strategic planning or pricing decisions

LL Admin Tasks and accounts tasks live in parallel workstreams and must not be
categorized as LL Legal Tasks.

---

## 3. Relationship to Other Systems

### Fulfillment Matter Queue

* LL Legal Tasks are derived from:
  * Matter State
  * Current Activity Period(s)
* LL Legal Tasks do not define or change State or Periods
* Completing an LL Legal Task may suggest a Period change but never applies it
  automatically

### Clio

* Clio Status / Fulfillment Status / Delivery Status remain authoritative
* LL Legal Tasks are overlay artifacts only

### Email-to-Fulfillment Matter Queue Workflow

* Emails may generate suggested LL Legal Tasks
* No LL Legal Task is created without a valid `matter_id`

---

## 4. What an LL Legal Task Is

An LL Legal Task is:

* A discrete, actionable delivery task
* Assigned to ML1, another legal service owner, or a role
* Time-bounded or event-triggered
* Explicitly tied to one matter

An LL Legal Task must answer:

> What legal delivery action needs to happen next on this matter?

---

## 5. Required Fields

Each LL Legal Task MUST include:

| Field | Description |
|-------|-------------|
| `matter_id` | Required — links to exactly one matter |
| `task_title` | Clear action verb, e.g. "Review draft agreement" |
| `description / context` | Why this task exists |
| `linked_activity_period` | One of the approved delivery periods |
| `assigned_to` | ML1, legal service owner, or role |
| `priority` | Low / Normal / High / Urgent |
| `due_trigger` | Date or event-based |
| `source` | manual / email / fulfillment matter queue-derived |
| `created_at` | Timestamp |
| `status` | Open / In Progress / Blocked / Completed |

Optional but recommended:

* dependencies
* reference links to documents, emails, or filings

---

## 6. Creation Rules

LL Legal Tasks may be created by:

* ML1 or another legal service owner
* ML2, as a suggestion based on Fulfillment Matter Queue state or email events

Creation constraints:

* Must be tied to an existing matter
* Must map to a valid delivery Activity Period
* Must not duplicate an existing open LL Task

If ambiguity exists:

* Create as **Suggested LL Legal Task** and flag for ML1 confirmation

---

## 7. Update & Completion Rules

### Allowed Updates

* Change status: Open -> In Progress -> Completed / Blocked
* Update description or due trigger
* Reassign to another legal service owner or role, with visibility

### Completion Effects

Completing an LL Legal Task does NOT automatically:

* Change Matter State
* Change Activity Period
* Close the matter

Completion MAY:

* Trigger a suggested Activity Period change
* Trigger creation of follow-on LL Tasks

---

## 8. Prohibited Uses

The LL Legal Task list MUST NOT be used to:

* Track billing or time entries
* Hide LL Admin Tasks inside legal-delivery work
* Hide LL Firm Management Tasks inside legal-delivery work
* Enforce productivity metrics
* Replace legal judgment
* Act as a project plan or Gantt chart
* Auto-advance Fulfillment Matter Queue states

---

## 9. ML2 Automation Guardrails

The System may:

* Suggest LL Legal Tasks based on Fulfillment Matter Queue state and email events
* De-duplicate similar tasks
* Surface overdue or blocked items

The System must NOT:

* Create LL Legal Tasks without a valid `matter_id`
* Assign priorities beyond explicit signals
* Close or complete LL Tasks autonomously
* Penalize inactivity or waiting

---

## 10. Enforcement & Escalation

If a proposed LL Legal Task:

* Is admin/accounting in nature
* Lacks a clear delivery Activity Period
* Attempts to substitute for judgment

Then:

* Reject creation as an LL Legal Task
* Route it to the correct LL Task class if appropriate
* Escalate to ML1 if unclear

---

## ML1 Authority Statement

ML1 is the sole authority for:

* Approving LL Task creation rules and constraints
* Defining valid delivery Activity Periods for LL Legal Task linkage
* Authorizing any System automation beyond suggestion
* Interpreting ambiguous LL Task categorization

## Explicit Prohibitions

The System must NOT:

* Create LL Legal Tasks without a valid `matter_id`
* Complete or close LL Tasks autonomously
* Use LL Legal Tasks to track billing, admin, or accounting work
* Auto-advance Fulfillment Matter Queue states based on LL Task completion
* Enforce productivity or efficiency metrics

## Approval State

**Draft** — Requires ML1 Approval

## Last ML1 Review Date

*Pending initial review*
