---
id: llp-014__planning__workplan
title: LLP-014 Intake Management — Workplan
owner: ML1
status: draft
created_date: 2026-04-01
last_updated: 2026-04-01
tags: [intake, pipeline, planning, workplan]
---

# Workplan

Project ID: LLP-014
Project Path: 04_INITIATIVES/LL_PORTFOLIO/08_MARKETING/LLP-014
Stage: Planning

---

## Workstreams

### WS-1: Stage Gate Definitions

**Goal:** Produce and get ML1 approval on the entry and exit criteria for
each of the three intake stages (Inquiry, Consultation, Onboarding). These
are the governing artifacts that unblock LLP-027, LLP-028, and LLP-029
Planning finalization.

**Milestones:**

| ID | Milestone | Owner | Target | Gate |
|----|-----------|-------|--------|------|
| M1.1 | Inquiry stage gate (entry + exit criteria) drafted | System | 2026-04-08 | ML1 review required |
| M1.2 | Consultation stage gate drafted | System | 2026-04-08 | ML1 review required |
| M1.3 | Onboarding stage gate drafted (incl. LLP-004 boundary) | System | 2026-04-08 | Requires LLP-004 coordination |
| M1.4 | All three stage gates ML1-approved | ML1 | 2026-04-15 | Unlocks LLP-027/028/029 Planning finalization |

---

### WS-2: Handoff Protocol Design

**Goal:** Define the data, trigger, and confirmation requirements for each
inter-stage handoff. LLP-027, LLP-028, and LLP-029 cannot finalize their
intake and output logic until these are locked.

**Milestones:**

| ID | Milestone | Owner | Target | Gate |
|----|-----------|-------|--------|------|
| M2.1 | Inquiry → Consultation handoff spec drafted | System | 2026-04-08 | Requires M1.1 and M1.2 |
| M2.2 | Consultation → Onboarding handoff spec drafted | System | 2026-04-08 | Requires M1.2 and M1.3 |
| M2.3 | Onboarding → LLP-004 boundary defined (coordination with LLP-004) | ML1 + System | 2026-04-15 | ML1 scope decision required |
| M2.4 | All handoff protocols ML1-approved | ML1 | 2026-04-15 | Required before LLP-027/028/029 Planning can finalize |

---

### WS-3: Cross-Stage Metric Schema

**Goal:** Define the metric schema (event definitions, disposition categories,
conversion rate structure) for the pipeline as a whole. Thresholds deferred
until execution baseline.

**Dependency:** Schema must align with F01/F02/F03 funnel metric definitions.
Cannot be finalized until LLP-011, LLP-012, and LLP-013 metric approvals
are confirmed.

**Milestones:**

| ID | Milestone | Owner | Target | Gate |
|----|-----------|-------|--------|------|
| M3.1 | Disposition category set defined (qualified, declined, no-response, deferred, out-of-scope) | System | 2026-04-08 | ML1 review required |
| M3.2 | Conversion rate schema defined (inquiry-to-consult, consult-to-client definitions) | System | 2026-04-08 | Must align with funnel metric schemas |
| M3.3 | Pipeline health reporting format defined | System | 2026-04-15 | ML1 review required |
| M3.4 | Metric schema ML1-approved | ML1 | 2026-04-22 | Funnel metric approvals (LLP-011/012/013) must be confirmed first |

---

### WS-4: Subproject Coordination Protocol

**Goal:** Define decision escalation, scope boundary enforcement, and
reporting integration so LLP-027/028/029 can operate autonomously within
governed boundaries.

**Milestones:**

| ID | Milestone | Owner | Target | Gate |
|----|-----------|-------|--------|------|
| M4.1 | Decision escalation path documented | System | 2026-04-15 | Requires WS-1 and WS-2 complete |
| M4.2 | Subproject scope boundary rules documented | System | 2026-04-15 | Requires stage gates (M1.4) |
| M4.3 | Coordination protocol ML1-approved | ML1 | 2026-04-22 | — |

---

## Resource Plan

| Resource | Allocation | Notes |
|----------|-----------|-------|
| ML1 | ~1 hr/week approval decisions | Stage gate and handoff protocol decisions require ML1 |
| System | On-demand | Drafts all artifacts; coordinates with LLP-004 for onboarding boundary |

---

## Dependencies

- **LLP-026 (Lead Capture)** — runs in parallel; LLP-026 routing decisions
  feed into inquiry format requirements for LLP-027
- **LLP-004 (Operational Onboarding)** — M2.3 requires coordination to
  define the LLP-029 / LLP-004 scope boundary
- **LLP-011, LLP-012, LLP-013 (Funnels)** — metric schema (WS-3) cannot be
  finalized until funnel-level metric approvals are confirmed by ML1

---

## Completion Condition

Planning stage complete when:

- WS-1 M1.4: all stage gates ML1-approved
- WS-2 M2.4: all handoff protocols ML1-approved
- WS-3 M3.4: metric schema ML1-approved (funnel metrics confirmed first)
- WS-4 M4.3: coordination protocol ML1-approved

Executing stage begins when Planning → Executing gate is ML1-approved.
