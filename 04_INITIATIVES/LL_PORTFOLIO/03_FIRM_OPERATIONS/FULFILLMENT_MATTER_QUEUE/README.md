---
id: 04_initiatives__ll_portfolio__03_firm_operations__fulfillment_matter_queue__readme_md
title: Fulfillment Matter Queue
owner: ML1
status: draft
created_date: 2026-02-08
last_updated: 2026-02-08
tags: []
---

# Fulfillment Matter Queue

**Location:** `LL_PORTFOLIO/03_FIRM_OPERATIONS/FULFILLMENT_MATTER_QUEUE/`

**Status:** Draft — Requires ML1 Approval

---

## 1. Purpose

The Fulfillment Matter Queue defines **fulfillment-stage visibility and
docketing flow** for matters across the governed fulfillment lifecycle.

It covers matters at all fulfillment stages:

* Onboarding
* Opening
* Maintenance
* Closing

Its practical purpose is to make salient to fee earners which matters are in
onboarding, opening, maintenance, or closing, and which are ready for
docketing, actively delivering, blocked, paused, or moving toward closure.

Administrative and accounts work still exists as a **parallel workstream** for
many purposes, but fulfillment-stage visibility across onboarding, opening,
maintenance, and closing is in scope for the queue.

The Fulfillment Matter Queue is therefore optimized to answer:

* Which matters are docketing-ready?
* Which matters are actively being delivered?
* How much delivery capacity is currently in use?
* Where is each matter in the fulfillment lifecycle right now?

It is **not a linear workflow**. Legal delivery is episodic, cyclical, and frequently dormant. The Fulfillment Matter Queue therefore models matters as:

* **States** — stable, low-cardinality delivery conditions describing what a matter *is*
* **Activity Periods** — repeatable, high-cardinality descriptions of what is *happening (or not happening)* in delivery over time

### Relationship to Matter Maintenance

The Fulfillment Matter Queue sits downstream of Matter Maintenance.

Matter Maintenance is a specific scope of work assigned to a teammate within
LL. The governed fulfillment system monitors that maintenance work and keeps a
reconciled view of whether the open-matter base is actually being maintained.

The Fulfillment Matter Queue builds on that monitored maintenance substrate to
make fulfillment-stage visibility salient to fee earners, especially by
answering which matters are in onboarding, opening, maintenance, or closing,
which are docketing-ready, and where current delivery load sits.

The Fulfillment Matter Queue is therefore an extension of Matter Maintenance, not a
replacement for it. It must not be used to compensate for unresolved
maintenance gaps in the underlying matter substrate.

The Fulfillment Matter Queue has not yet been assigned inside LL. For now, its
operating owner is ML2.

---

## 2. Hard Scope Boundary

The Fulfillment Matter Queue applies **only to matters**.

It explicitly excludes:

* Leads
* Prospects
* Pre-engagement evaluation before a governed matter record exists
* Sales funnels or CRM stages

The queue enters scope once a governed matter record exists within fulfillment.
That includes pending matters in onboarding and matters progressing through
opening, maintenance, and closing. Leads and pre-matter opportunities remain
out of scope.

### Relationship to System of Record

The Fulfillment Matter Queue **does not replace or modify** existing matter status fields in the system of record.

Matters already carry authoritative tags such as:

| Field | Source | Authority |
|-------|--------|-----------|
| Status (e.g., Pending / Open / Closed) | Clio | Source of truth |
| Fulfillment Status | Clio | Source of truth |
| Delivery Status | Clio | Source of truth |

**These remain the source-of-truth fields.**

The Fulfillment Matter Queue introduces **additional, real-time operational tags**:

| Field | Source | Purpose |
|-------|--------|---------|
| State | Fulfillment Matter Queue | Delivery posture |
| Activity Period(s) | Fulfillment Matter Queue | What is happening now |

The Fulfillment Matter Queue tags are **supplementary** — they do not override or conflict with system of record fields.

---

## 3. Matter States (Fulfillment-Focused)

Matter States describe the **operational posture** of a matter across the
fulfillment lifecycle, with special emphasis on stage visibility, delivery
readiness, and docketing salience for fee earners.

They are:

* Mutually exclusive
* Few in number
* Infrequently changed
* Oriented around fulfillment-stage visibility and docketing readiness

> **Scope note:** This taxonomy applies to matters in fulfillment scope,
> including matters in onboarding, opening, maintenance, and closing. Closed
> matters are out of scope once closure is complete.

### Minimal, Neutral State Set

1. **Initiating**

   * Matter exists in governed fulfillment scope
   * Onboarding or opening activity may still be underway
   * Docketing readiness may still be developing
   * No assumption of substantive legal work yet

2. **Backlog**

   * Matter is open and valid
   * Not currently selected for delivery
   * Awaiting prioritization, triggering event, or delivery capacity
   * Explicitly *not* a failure or delay signal

3. **Docketing Active**

   * Matter is actively occupying delivery capacity
   * Legal work is currently expected or underway
   * Activity periods may start, stop, and repeat

4. **Paused**

   * Matter is temporarily removed from delivery flow
   * Pause may be client-driven, external, regulatory, or strategic
   * Distinct from Backlog (which implies not yet selected or re-selected for delivery)

5. **Closing**

   * Substantive delivery work largely complete
   * Final delivery wrap-up in progress

> **Rule:** A matter must always be in exactly one delivery state while it remains open in the system of record.

---

## 4. Activity Periods (Delivery-Salience Layer)

Activity Periods describe **what is happening in legal delivery** during a
span of time.

They:

* May occur when a matter is in **Initiating**, **Backlog**, **Docketing Active**, or **Closing**
* Are repeatable
* Are descriptive, not evaluative

Not every fulfillment stage requires an activity period. Matters in onboarding
or opening may be in scope for the queue before substantive legal delivery
activity begins.

They explicitly **exclude**:

* Billing activity
* Accounting work
* Administrative processing

A matter may cycle through the same period type multiple times.

### Core Period Taxonomy (Extensible)

#### Delivery Work Periods

* Drafting
* Review
* Analysis
* Negotiation
* Filing / Submission
* Implementation

#### Waiting / Dormancy Periods

* Waiting on Client
* Waiting on Counterparty
* Waiting on Regulator / Court
* External Hold

#### Internal Delivery Periods

* Internal Review
* Partner Review
* Quality Control

> **Rule:** Waiting and inactivity are normal delivery conditions, not signals of inefficiency.

---

## 5. Relationship Between States and Periods

* Activity Periods may only exist **within Initiating, Backlog, or Docketing Active**
* Activity Periods do not advance or regress states
* Entering or exiting a state is a separate, explicit action

Example:

* State: Active

  * Period: Drafting
  * Period: Waiting on Client
  * Period: Drafting

The matter remains **Active** throughout.

---

## 6. What the Fulfillment Matter Queue Does NOT Do

The Fulfillment Matter Queue does not:

* Evaluate performance
* Judge efficiency
* Predict outcomes
* Rank matters
* Imply sales velocity or success

It records **conditions**, not opinions.

---

## 7. Interaction With Other Portfolios

* **Matter Docketing (`05_MATTER_DOCKETING`)**

  * Overlay for tracking delivery states and activity periods
  * Houses lawyer to-do protocol

* **Risk (`04_RISK`)**

  * May require checks at certain states
  * Cannot change states

* **Financial Portfolio (`01_FINANCIAL_MANAGEMENT`)**

  * May analyze time-in-state or period patterns
  * May not define, modify, or advance states or periods

---

## 8. Capacity Intent (Non-Prescriptive)

The firm's operational intent is to maintain approximately **6–10 matters** in a **Docketing Active** state at any given time.

This is:

* A **target**
* A planning reference for delivery capacity
* Explicitly non-binding

The System may **observe and report** against this intent but must not:

* Enforce it
* Automatically move matters between states
* Treat deviations as errors or failures

---

## 9. Enforcement Rules

* The Fulfillment Matter Queue governs **matter visibility across onboarding, opening, maintenance, and closing**
* Billing and accounting remain parallel workstreams and must not be modeled as queue states or activity periods
* No linear progression assumptions are permitted
* No lead, funnel, or sales concepts may be introduced
* States must remain minimal and stable
* Period taxonomy may expand but must remain delivery-descriptive

If uncertainty exists:
**STOP. FLAG. ESCALATE TO ML1.**

---

## ML1 Authority Statement

ML1 is the sole authority for:
- Approving state transitions
- Defining new states or periods
- Setting capacity targets
- Interpreting Fulfillment Matter Queue conditions

## Explicit Prohibitions

The System must NOT:
- Evaluate matter performance
- Judge delivery efficiency
- Predict outcomes
- Automatically advance states
- Enforce capacity targets
- Model leads, prospects, or sales funnels

## Approval State

**Draft** — Requires ML1 Approval

## Last ML1 Review Date

*Pending initial review*
