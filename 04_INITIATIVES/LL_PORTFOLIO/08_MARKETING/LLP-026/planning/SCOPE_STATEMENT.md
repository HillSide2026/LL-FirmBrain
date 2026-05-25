---
id: llp-026__planning__scope_statement
title: LLP-026 Lead Capture — Scope Statement
owner: ML1
status: draft
created_date: 2026-04-01
last_updated: 2026-04-01
tags: [lead-capture, marketing, planning, scope]
---

# Scope Statement

Project ID: LLP-026
Project Path: 04_INITIATIVES/LL_PORTFOLIO/08_MARKETING/LLP-026
Stage: Planning

---

## In Scope

### 1. Capture Architecture

Define the capture architecture for each active funnel:

- F01 (LLP-011): capture mechanism for organic search traffic already
  executing; define CTA placement and form configuration for existing pages
- F02 (LLP-012): capture mechanism for Health Check funnel; define CTA and
  lead magnet opt-in design aligned with Health Check offer; dependent on F02
  Planning reaching sufficient maturity to specify CTAs
- F03 (LLP-013): capture mechanism for payments/fintech regulatory funnel;
  define CTA placement aligned with regulatory triage consultation offer;
  dependent on F03 metric approval gate closing

For each funnel: define form fields, CTA copy direction, placement logic
(which page types carry which CTA), and confirmation workflow.

### 2. Lead Magnet and Offer Definition

Define the opt-in offer for each funnel:

- F01 entry offer: to be determined in Planning based on F01 content audit
  and ML1 approval
- F02 entry offer: Health Check diagnostic or adjacent download — must be
  coordinated with LLP-012 offer definition
- F03 entry offer: regulatory triage consultation or AML/MSB resource —
  must be coordinated with LLP-013 entry offer definition (SCOPE_STATEMENT.md
  WS entry offer section)

Offer definitions are ML1-approval decisions. No opt-in asset is built until
offer and scope are approved.

### 3. Attribution and Routing Design

Define the attribution and routing layer:

- Source attribution schema: what tags are applied at point of capture to
  identify source funnel (F01/F02/F03), page type, and CTA type
- Routing logic: how each form submission is routed into the intake pipeline
  (LLP-014); must align with LLP-014 handoff protocol and LLP-027 inquiry
  receipt format
- Attribution schema must be designed in coordination with LLP-014 Planning
  (WS-3 metric schema) and must be compatible with the funnel-level metric
  definitions from LLP-011, LLP-012, and LLP-013

### 4. Platform and Delivery Configuration

Define the platform configuration for capture mechanics:

- Form platform selection or confirmation (existing GHL or alternate)
- Lead magnet delivery mechanism
- Confirmation email / acknowledgment workflow
- Integration with intake pipeline (how captured lead data reaches LLP-027)

Platform decisions require ML1 approval before implementation.

---

## Out of Scope

- Funnel content production, SEO, and page publishing — owned by LLP-011,
  LLP-012, LLP-013
- Intake pipeline management and inquiry triage — owned by LLP-014 and
  LLP-027
- CRM provisioning and Clio setup — owned by LLP-004
- Paid advertising management
- Lead magnet content production (asset creation is an Executing-stage task;
  offer definition only is in scope for Planning)

---

## Metric Dependency

Specific conversion rate thresholds, opt-in rate benchmarks, and attribution
schema definitions cannot be finalized until:

1. F01 metric thresholds are locked by ML1 (LLP-011 Planning gate)
2. F02 Planning artifacts are produced and metric definitions are approved
   by ML1 (LLP-012)
3. F03 metric threshold approval is confirmed by ML1 (LLP-013 ML1_METRIC_APPROVAL.md)

The attribution schema design (WS-3) must use the same event naming and
conversion definitions as the funnel metrics it sits inside.

---

## Completion Condition

Planning stage complete when:

1. Capture architecture is defined for each active funnel with ML1 approval.
2. Lead magnet / opt-in offer is ML1-approved for each active funnel.
3. Attribution schema and routing logic are defined and aligned with LLP-014
   metric schema and LLP-027 inquiry receipt format.
4. Platform configuration decisions are ML1-approved.
5. Metric schema and thresholds are deferred to Executing baseline — this
   does not block Planning gate closure.

Executing stage begins when Planning → Executing gate is ML1-approved.
