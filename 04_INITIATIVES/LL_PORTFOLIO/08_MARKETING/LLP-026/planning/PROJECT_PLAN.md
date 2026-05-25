---
id: llp-026__planning__workplan
title: LLP-026 Lead Capture — Workplan
owner: ML1
status: draft
created_date: 2026-04-01
last_updated: 2026-04-01
tags: [lead-capture, marketing, planning, workplan]
---

# Workplan

Project ID: LLP-026
Project Path: 04_INITIATIVES/LL_PORTFOLIO/08_MARKETING/LLP-026
Stage: Planning

---

## Workstreams

### WS-1: Capture Architecture Design

**Goal:** Define the CTA placement, form configuration, and capture mechanism
for each active funnel. F01 is executing — its capture architecture is the
first priority. F02 and F03 depend on funnel Planning maturity.

**Milestones:**

| ID | Milestone | Owner | Target | Gate |
|----|-----------|-------|--------|------|
| M1.1 | F01 CTA audit — identify all current funnel pages and capture points | System | 2026-04-08 | — |
| M1.2 | F01 capture architecture (CTA placement, form fields, confirmation) defined | System | 2026-04-08 | ML1 review required |
| M1.3 | F01 capture architecture ML1-approved | ML1 | 2026-04-15 | — |
| M1.4 | F02 capture architecture defined (pending LLP-012 CTA specifications) | System | TBD | Blocked until LLP-012 Planning produces CTA specs |
| M1.5 | F03 capture architecture defined (pending LLP-013 metric approval) | System | TBD | Blocked until LLP-013 ML1_METRIC_APPROVAL.md confirmed |
| M1.6 | All active funnel capture architectures ML1-approved | ML1 | TBD | Funnel-level dependencies must be met |

---

### WS-2: Lead Magnet and Offer Definition

**Goal:** Get ML1 approval on the opt-in offer for each active funnel before
any opt-in asset is designed or built.

**Milestones:**

| ID | Milestone | Owner | Target | Gate |
|----|-----------|-------|--------|------|
| M2.1 | F01 lead magnet options identified and presented to ML1 | System | 2026-04-08 | ML1 decision required |
| M2.2 | F01 lead magnet offer ML1-approved (scope and format) | ML1 | 2026-04-15 | — |
| M2.3 | F02 lead magnet offer defined (Health Check adjacent) | System | TBD | Requires LLP-012 offer definition; coordinate with LLP-012 |
| M2.4 | F03 lead magnet offer defined (regulatory triage) | System | TBD | Must align with LLP-013 entry offer (SCOPE_STATEMENT.md) |
| M2.5 | All active funnel offers ML1-approved | ML1 | TBD | — |

---

### WS-3: Attribution and Routing Design

**Goal:** Define the attribution schema and routing logic that connects
captured leads to the intake pipeline. Must align with LLP-014 metric schema
(running in parallel) and LLP-027 inquiry receipt format.

**Dependency:** Attribution schema must use the same event naming and
conversion definitions as F01/F02/F03 funnel metrics. Cannot be finalized
until LLP-011/012/013 metric approvals are confirmed.

**Milestones:**

| ID | Milestone | Owner | Target | Gate |
|----|-----------|-------|--------|------|
| M3.1 | Source attribution tag schema drafted (funnel, page type, CTA type) | System | 2026-04-08 | Must align with LLP-014 WS-3 metric schema |
| M3.2 | Routing logic defined: how form submissions reach LLP-027 inquiry receipt | System | 2026-04-15 | Requires LLP-027 inquiry format (coordinate with LLP-027 Planning) |
| M3.3 | Attribution schema reviewed against LLP-014 metric schema | System | 2026-04-15 | LLP-014 WS-3 must be sufficiently advanced |
| M3.4 | Attribution schema and routing logic ML1-approved | ML1 | 2026-04-22 | Funnel metric approvals (LLP-011/012/013) must be confirmed |

---

### WS-4: Platform and Delivery Configuration

**Goal:** Confirm or select the platform stack, define delivery mechanics,
and specify the integration with the intake pipeline before asset build begins.

**Milestones:**

| ID | Milestone | Owner | Target | Gate |
|----|-----------|-------|--------|------|
| M4.1 | Platform assessment: GHL vs. alternate for form capture and delivery | System | 2026-04-08 | ML1 decision on platform |
| M4.2 | Platform selection ML1-approved | ML1 | 2026-04-15 | — |
| M4.3 | Intake pipeline integration spec defined: how captured lead data reaches LLP-027 | System | 2026-04-15 | Requires LLP-027 inquiry receipt format |
| M4.4 | Integration spec ML1-approved | ML1 | 2026-04-22 | — |

---

## Resource Plan

| Resource | Allocation | Notes |
|----------|-----------|-------|
| ML1 | ~1 hr/week approval decisions | Offer definition, platform selection, and architecture approvals require ML1 |
| System | On-demand | Audits, drafts, and coordinates with LLP-012/013/014/027 |

---

## Dependencies

- **LLP-014 (Intake Management)** — WS-3 attribution schema must align with
  LLP-014 metric schema (WS-3). Run in parallel; coordinate before schemas are
  finalized.
- **LLP-027 (Inquiries)** — routing logic (WS-3 M3.2) and integration spec
  (WS-4 M4.3) both require LLP-027 inquiry receipt format; coordinate during
  LLP-027 Planning.
- **LLP-011 (F01 Funnel)** — F01 capture architecture can proceed now; F01
  metric thresholds need to be locked before attribution schema is finalized.
- **LLP-012 (F02 Funnel)** — F02 capture architecture (M1.4) blocked until
  LLP-012 Planning produces CTA specifications. LLP-012 Planning has zero
  artifacts currently — this is a hard dependency.
- **LLP-013 (F03 Funnel)** — F03 capture architecture (M1.5) blocked until
  LLP-013 metric approval gate closes (single ML1 decision outstanding).

---

## Completion Condition

Planning stage complete when:

- WS-1: all active funnel capture architectures ML1-approved
- WS-2: all active funnel lead magnet offers ML1-approved
- WS-3 M3.4: attribution schema and routing logic ML1-approved
- WS-4 M4.4: platform configuration and integration spec ML1-approved

Executing stage begins when Planning → Executing gate is ML1-approved.
