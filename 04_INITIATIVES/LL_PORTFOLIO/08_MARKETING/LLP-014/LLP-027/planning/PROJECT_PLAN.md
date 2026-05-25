---
id: llp-027__planning__workplan
title: LLP-027 Inquiries — Workplan
owner: ML1
status: draft — pending LLP-014 stage gate definitions and LLP-026 inquiry format
created_date: 2026-04-01
last_updated: 2026-04-01
tags: [inquiries, intake, planning, workplan]
---

# Workplan

Project ID: LLP-027
Project Path: 04_INITIATIVES/LL_PORTFOLIO/08_MARKETING/LLP-014/LLP-027
Stage: Planning

> **Draft — cannot be finalized until:**
> - LLP-014 WS-1 M1.4: Inquiry stage gate definitions ML1-approved
> - LLP-014 WS-2 M2.4: Inquiry → Consultation handoff protocol ML1-approved
> - LLP-026 WS-3: Inquiry attribution format and routing logic confirmed
>
> Milestones marked TBD-GATE are blocked pending the above. Other milestones
> can proceed in parallel.

---

## Workstreams

### WS-1: Inquiry Receipt System

**Goal:** Design and configure the system that logs all incoming inquiries
from all channels and generates acknowledgment.

**Milestones:**

| ID | Milestone | Owner | Target | Gate |
|----|-----------|-------|--------|------|
| M1.1 | Channel inventory: map all current inquiry entry points (web, email, phone, referral) | System | 2026-04-08 | — |
| M1.2 | Receipt logging mechanism designed (aligned with LLP-026 routing format) | System | TBD-GATE | Requires LLP-026 WS-3 inquiry format |
| M1.3 | Acknowledgment SLA and workflow drafted | System | 2026-04-08 | ML1 review required |
| M1.4 | Acknowledgment SLA ML1-approved | ML1 | TBD-GATE | SLA must align with LLP-014 metric schema |
| M1.5 | Receipt system design ML1-approved | ML1 | TBD-GATE | Requires LLP-026 routing format confirmed |

---

### WS-2: Triage Logic

**Goal:** Define and get ML1 approval on the classification system applied
to each logged inquiry.

**Milestones:**

| ID | Milestone | Owner | Target | Gate |
|----|-----------|-------|--------|------|
| M2.1 | Practice area classification criteria drafted | System | 2026-04-08 | ML1 review and approval required |
| M2.2 | Urgency tier classification criteria drafted | System | 2026-04-08 | ML1 review required |
| M2.3 | Matter type classification drafted | System | 2026-04-08 | ML1 review required |
| M2.4 | Out-of-scope / decline criteria drafted | System | 2026-04-08 | ML1 review required |
| M2.5 | All triage criteria ML1-approved | ML1 | TBD-GATE | Must align with LLP-014 stage gate entry criteria (M1.1) |
| M2.6 | Triage category mapping to funnel source (F01/F02/F03) confirmed | System | TBD-GATE | Requires LLP-026 attribution schema and funnel metric approvals |

---

### WS-3: Initial Response Workflow

**Goal:** Draft and get ML1 approval on response templates and SLA targets.

**Milestones:**

| ID | Milestone | Owner | Target | Gate |
|----|-----------|-------|--------|------|
| M3.1 | Response template drafts by triage category | System | 2026-04-15 | ML1 review required; SE-01 review for outward-facing copy |
| M3.2 | SLA targets by urgency tier proposed | System | 2026-04-08 | ML1 approval required |
| M3.3 | SLA targets ML1-approved | ML1 | TBD-GATE | Must align with LLP-014 metric schema |
| M3.4 | Response templates ML1-approved | ML1 | TBD-GATE | — |
| M3.5 | Declined inquiry response protocol ML1-approved | ML1 | TBD-GATE | — |

---

### WS-4: Handoff Protocol (LLP-027 Side)

**Goal:** Implement the LLP-027 side of the Inquiry → Consultation handoff
protocol as defined by LLP-014 WS-2 M2.1.

**Milestones:**

| ID | Milestone | Owner | Target | Gate |
|----|-----------|-------|--------|------|
| M4.1 | Handoff data package defined (what fields are passed to LLP-028) | System | TBD-GATE | Requires LLP-014 WS-2 M2.1 (handoff spec) |
| M4.2 | Handoff trigger mechanism designed | System | TBD-GATE | Requires LLP-014 WS-2 M2.1 and LLP-028 to have initiated |
| M4.3 | LLP-028 confirmation protocol aligned with LLP-028 intake spec | System | TBD-GATE | Requires LLP-028 initiation and Planning start |
| M4.4 | Handoff protocol (LLP-027 side) ML1-approved | ML1 | TBD-GATE | — |

---

### WS-5: Disposition Tracking

**Goal:** Define the disposition schema and implement recording for all
inquiry outcomes.

**Milestones:**

| ID | Milestone | Owner | Target | Gate |
|----|-----------|-------|--------|------|
| M5.1 | Disposition category set defined (aligned with LLP-014 metric schema) | System | TBD-GATE | Requires LLP-014 WS-3 M3.1 (disposition categories) |
| M5.2 | Disposition recording mechanism designed | System | TBD-GATE | — |
| M5.3 | Disposition schema ML1-approved | ML1 | TBD-GATE | — |

---

## Resource Plan

| Resource | Allocation | Notes |
|----------|-----------|-------|
| ML1 | ~1 hr/week approval decisions | Triage criteria, SLA targets, and template approvals require ML1 |
| System | On-demand | Drafts all artifacts; coordinates with LLP-014, LLP-026, LLP-028 |

---

## Dependencies

- **LLP-014 (Intake Management)** — WS-1, WS-2, WS-4, WS-5 all depend on
  LLP-014 WS-1/WS-2/WS-3 outputs; this workplan cannot be finalized until
  LLP-014 Planning produces stage gate definitions and handoff protocol
- **LLP-026 (Lead Capture)** — WS-1 receipt system design requires LLP-026
  WS-3 attribution and routing format; WS-2 triage mapping requires LLP-026
  attribution schema
- **LLP-028 (Consults)** — WS-4 handoff protocol requires LLP-028 to be
  initiated and to have defined its intake requirements; LLP-028 must be
  initiated before M4.2 can proceed
- **LLP-011/012/013 (Funnels)** — WS-2 M2.6 triage mapping and WS-3 SLA
  thresholds require funnel metric approvals to be confirmed

---

## Completion Condition

Planning stage complete when:

- All WS-1 through WS-5 milestones are ML1-approved
- LLP-014 stage gate and handoff protocol outputs are incorporated
- LLP-026 attribution format is reflected in the receipt system design
- LLP-028 has initiated and confirmed its handoff intake requirements

Executing stage begins when Planning → Executing gate is ML1-approved.
