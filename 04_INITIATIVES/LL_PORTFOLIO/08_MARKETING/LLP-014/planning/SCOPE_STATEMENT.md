---
id: llp-014__planning__scope_statement
title: LLP-014 Intake Management — Scope Statement
owner: ML1
status: draft
created_date: 2026-04-01
last_updated: 2026-04-01
tags: [intake, pipeline, planning, scope]
---

# Scope Statement

Project ID: LLP-014
Project Path: 04_INITIATIVES/LL_PORTFOLIO/08_MARKETING/LLP-014
Stage: Planning

---

## In Scope

### 1. Stage Gate Definitions

Define the entry and exit criteria for each of the three intake stages:

- Inquiry stage (LLP-027): what constitutes a received inquiry; what conditions
  must be met for an inquiry to advance to consultation
- Consultation stage (LLP-028): what constitutes a qualified consultation
  booking; what conditions must be met for a consultation to advance to
  onboarding
- Onboarding stage (LLP-029): what constitutes a completed onboarding; what
  signals transfer to LLP-004 (operational onboarding) and LLP-005 (Opening)

Stage gate definitions are the primary output of Planning. They are the
governing artifact that LLP-027, LLP-028, and LLP-029 Planning depends on.

### 2. Handoff Protocol Design

Define the handoff protocol between each adjacent stage:

- Inquiry → Consultation handoff: what data is passed, what trigger initiates
  the handoff, what confirmation LLP-028 requires to accept the handoff
- Consultation → Onboarding handoff: same structure
- Onboarding → LLP-004 (Operational Onboarding) handoff: scope boundary
  between marketing-side and operational-side onboarding; requires coordination
  with LLP-004

Handoff protocols must be defined at the parent level before subprojects
design their own intake and output logic.

### 3. Cross-Stage Metric Framework

Define the metric schema for the pipeline as a whole:

- Conversion rate definitions: inquiry-to-consult, consult-to-client
- Disposition categories: what outcomes are tracked at each stage (qualified,
  declined, no-response, deferred, out-of-scope)
- Reporting cadence and format: how pipeline health is reported to ML1

Metric thresholds are not set in this stage — they are set once baseline
data is available. Schema only.

Dependency: metric schema must use event and conversion definitions that are
compatible with F01 (LLP-011), F02 (LLP-012), and F03 (LLP-013) funnel
metric definitions. Schema cannot be finalized until funnel-level metric
approvals are confirmed by ML1.

### 4. Subproject Coordination Protocol

Define the operational coordination layer between LLP-027, LLP-028, and
LLP-029:

- Decision escalation path: what decisions stay within a subproject vs. what
  escalates to LLP-014 governance
- Scope boundary enforcement: how conflicts between adjacent subprojects are
  resolved
- Reporting integration: how subproject status reports roll up into the
  pipeline health view

---

## Out of Scope

- Triage logic, SLA targets, and response workflows — owned by LLP-027
- Consultation scheduling, conduct protocols, and conversion criteria —
  owned by LLP-028
- Welcome communications and onboarding materials — owned by LLP-029
- Operational matter setup and Clio provisioning — owned by LLP-004
- Lead capture infrastructure and CTA configuration — owned by LLP-026
- Funnel content and SEO — owned by LLP-011, LLP-012, LLP-013

---

## Completion Condition

Planning stage complete when:

1. Stage gate definitions for all three intake stages are ML1-approved.
2. Handoff protocol design for all three inter-stage transitions is
   ML1-approved, including the LLP-029 / LLP-004 boundary.
3. Cross-stage metric schema is documented (thresholds deferred to execution
   baseline).
4. Subproject coordination protocol is documented.
5. LLP-027, LLP-028, and LLP-029 have each received the stage gate and
   handoff definitions they need to finalize their own Planning artifacts.

Executing stage begins when Planning → Executing gate is ML1-approved.
