---
id: llp-027__planning__scope_statement
title: LLP-027 Inquiries — Scope Statement
owner: ML1
status: draft — pending LLP-014 stage gate definitions and LLP-026 inquiry format
created_date: 2026-04-01
last_updated: 2026-04-01
tags: [inquiries, intake, planning, scope]
---

# Scope Statement

Project ID: LLP-027
Project Path: 04_INITIATIVES/LL_PORTFOLIO/08_MARKETING/LLP-014/LLP-027
Stage: Planning

> **Draft — cannot be finalized until:**
> 1. LLP-014 Planning (WS-1, WS-2) has produced and ML1-approved the Inquiry
>    stage gate definitions and the Inquiry → Consultation handoff protocol.
> 2. LLP-026 Planning (WS-3) has defined the inquiry format arriving from
>    lead capture (attribution tags, form fields, routing trigger).
>
> This document may be drafted and worked in parallel but must be reviewed
> against LLP-014 outputs before Planning gate can close.

---

## In Scope

### 1. Inquiry Receipt

Define the logging and acknowledgment system for all incoming inquiries:

- Web form submissions arriving from LLP-026 (lead capture)
- Email inquiries arriving directly (not via capture form)
- Phone and referral inquiries — channel coverage and logging protocol
- Acknowledgment workflow: what confirmation does an inquirer receive and
  when; what is the acknowledgment SLA

Entry criteria for the inquiry stage are defined by LLP-014 (WS-1 M1.1).
This scope section implements the receipt mechanism that satisfies those
criteria.

### 2. Triage Logic

Define the classification system applied to each logged inquiry:

- Practice area classification: which Levine Law practice area does this
  inquiry concern (corporate, contracts, financial services, other)
- Urgency classification: urgency tier assignment criteria
- Matter type classification: type of matter or service being sought
- Out-of-scope classification: what inquiry types are declined and how

Triage categories must be compatible with the source funnel attribution
tags arriving from LLP-026. Classification should map to funnel source where
possible (F01 → likely personal injury / general; F02 → likely corporate /
commercial; F03 → likely financial services / payments).

Triage criteria are ML1-approval decisions and cannot be implemented until
approved.

### 3. Initial Response Workflow

Define the initial response system:

- Response templates by triage category and urgency tier
- SLA targets by urgency tier (time-to-first-response)
- Escalation path when ML1 review is required before response
- Declined inquiry response protocol

SLA targets are ML1-approval decisions. Metric dependency: SLA tiers and
urgency definitions must be compatible with the metric schema defined by
LLP-014 (WS-3) and must align with F01/F02/F03 funnel metric definitions.

### 4. Handoff Protocol to LLP-028

Define the handoff mechanism to the consultation stage:

- Exit criteria for the inquiry stage (defined by LLP-014 WS-1 M1.1 —
  this scope section implements the mechanism, not the criteria)
- Handoff data package: what information is passed to LLP-028
- Handoff trigger: what action initiates the handoff
- Confirmation protocol: what LLP-028 must confirm to accept the handoff

Handoff protocol design is governed by LLP-014 (WS-2 M2.1). This section
implements the LLP-027 side of that protocol.

### 5. Disposition Tracking

Define the disposition recording system:

- A recorded outcome for every inquiry that enters the stage
- Disposition categories aligned with LLP-014 metric schema
- No inquiry exits the stage without a recorded disposition

---

## Out of Scope

- Lead capture infrastructure and form configuration — owned by LLP-026
- Consultation scheduling and conduct — owned by LLP-028
- Client onboarding — owned by LLP-029 and LLP-004
- Stage gate definitions and handoff protocol design — owned by LLP-014;
  this project implements, not designs, those protocols

---

## Metric Dependency

SLA targets, urgency tier thresholds, and inquiry volume benchmarks are
Planning deliverables subject to ML1 approval. These cannot be finalized
until:

1. LLP-014 metric schema (WS-3) is approved by ML1
2. F01/F02/F03 funnel metric definitions are approved by ML1

Triage category definitions must use event and conversion naming compatible
with the funnel metric schemas.

---

## Completion Condition

Planning stage complete when:

1. LLP-014 stage gate definitions (M1.4) and handoff protocol (M2.4) are
   ML1-approved and this scope is reconciled against them.
2. LLP-026 inquiry format (WS-3) is confirmed and receipt system is designed
   to accept that format.
3. Triage logic and classification criteria are ML1-approved.
4. SLA targets by urgency tier are ML1-approved.
5. Initial response templates are drafted and ML1-approved.
6. Handoff protocol (LLP-027 side) is defined and aligned with LLP-028.
7. Disposition tracking schema is defined and compatible with LLP-014
   metric schema.

Executing stage begins when Planning → Executing gate is ML1-approved.
