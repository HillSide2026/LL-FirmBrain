---
id: 04_initiatives__ll_portfolio__05_matter_docketing__readme_md
title: Matter Docketing Portfolio
owner: ML1
status: draft
created_date: 2026-02-08
last_updated: 2026-02-08
tags: []
---

# Matter Docketing Portfolio

**Location:** `04_INITIATIVES/LL_PORTFOLIO/05_MATTER_DOCKETING/`

**Status:** Draft — Requires ML1 Approval

---

## 1. Purpose

The Matter Docketing portfolio defines the **delivery and docketing overlay** for matters that exist in the system of record (Clio).

It provides a real-time, delivery-focused view of:

* Which matters are consuming delivery capacity
* What delivery work is currently happening
* What legal-delivery actions should happen next

This portfolio does **not** represent the client relationship, financial lifecycle, or administrative handling of a matter.

---

## 2. Authority & System Boundaries

* **System of Record:** Clio
* **ML1:** Sole authority for judgment, prioritization, and acceptance of matters
* **ML2:** Observes, tags, suggests, and records delivery signals

The Matter Docketing portfolio:

* Does not replace Clio fields
* Does not create authoritative status
* Does not make or enforce decisions

---

## 3. Scope (Inclusions)

This portfolio includes **delivery-only artifacts** tied to an existing matter:

* Delivery-facing views that consume fulfillment readiness and queue signals
* Legal-delivery views that may consume derivative command-layer visibility from
  `LLP-023 Matter Command and Control`
* Activity Periods (what is happening now in delivery)
* LL Legal Task Lists (delivery actions)
* Delivery-relevant dependencies and blockers
* Read-only matter metadata required for delivery context

All artifacts must reference a valid `matter_id`.

---

## 4. Explicit Exclusions (Hard)

The following are explicitly **out of scope** and must not appear in this portfolio:

* Billing, invoicing, or payments
* Time tracking or productivity metrics
* Accounting or trust activity
* Client intake, leads, or sales processes
* Marketing or relationship management
* Strategic planning or pricing decisions

Admin and accounting workflows exist as **parallel systems** and may create dependencies, but are not modeled here.

---

## 5. Core Components

### 5.1 Fulfillment Matter Queue Relationship

The Fulfillment Matter Queue is a **fulfillment-side reporting mechanism**
defined under `03_FIRM_OPERATIONS/FULFILLMENT_MATTER_QUEUE/`.

It is not owned by the Matter Docketing portfolio.

Matter Docketing **consumes** queue outputs where relevant, especially:

* where the matter sits in onboarding, opening, maintenance, or closing
* whether fulfillment-side work is complete enough for docketing readiness
* whether the matter is ready for legal-delivery docketing attention

Queue states and queue readiness logic remain fulfillment constructs.
The Matter Docketing portfolio must not redefine them.

---

### 5.2 Activity Periods

Repeatable, descriptive periods that capture what is happening in delivery at a given time.

Activity Periods:

* Exist only within Initiating, Backlog, or Docketing Active states
* May repeat or recur
* Carry no evaluative or performance meaning

---

### 5.3 LL Legal Task Lists

A delivery-scoped list of actionable legal tasks for a matter.

To-dos:

* Are derived from the current delivery context
* Do not advance states automatically
* Do not represent billing or time obligations

---

### 5.4 Delivery Dependencies

Explicit delivery blockers or prerequisites, such as:

* Awaiting inputs
* External dependencies
* Internal sequencing constraints

Dependencies are **facts**, not tasks.

---

## 6. Interaction With Other Portfolios

* **Practice Areas:** Provide reusable execution knowledge; do not own matter state
* **Firm Operations:** Own fulfillment mechanics and the Fulfillment Matter Queue; Matter Docketing consumes those readiness signals but does not define them
* **LLP-023 Matter Command and Control:** Provides the derivative,
  cross-system matter-visibility layer for lawyers; Matter Docketing may
  consume those visibility outputs but does not own the command layer
* **Financial Portfolio:** May analyze delivery patterns; may not control them
* **Risk & Compliance:** May impose checks; may not advance delivery

---

## 7. Operating Principles

* Delivery reality over linear progress
* Capacity awareness without enforcement
* Signals, not judgments
* Observability without control

If scope or authority is unclear:

> Stop. Label. Escalate to ML1.

---

## ML1 Authority Statement

ML1 is the sole authority for:
- Judgment, prioritization, and acceptance of matters
- Approving State transitions
- Defining new States or Activity Periods
- Authorizing any automated Fulfillment Matter Queue changes

## Explicit Prohibitions

The System must NOT:
- Replace or modify Clio source-of-truth fields
- Create authoritative status
- Make or enforce decisions
- Track billing, accounting, or admin work
- Model intake, leads, sales, or marketing
- Redefine Fulfillment Matter Queue states or fulfillment readiness rules

## Approval State

**Draft** — Requires ML1 Approval

## Last ML1 Review Date

*Pending initial review*
