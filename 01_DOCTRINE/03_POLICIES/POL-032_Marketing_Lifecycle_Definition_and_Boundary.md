---
id: POL-032
title: Marketing Lifecycle Definition and Boundary
owner: ML1
status: approved
approved_by: ML1
approved_date: 2026-04-18
version: 0.2
effective_date: 2026-04-18
supersedes:
provenance:
  decided_by: ML1
  decided_on: 2026-04-18
  context: Metadata normalized by system admin cleanup on 2026-05-24
created_date: 2026-03-08
last_updated: 2026-03-09
tags: [policy, marketing, lifecycle, boundary]
---

# POL-032 — Marketing Lifecycle Definition and Boundary

Policy Statement: For Levine Law, marketing is the process that begins when a potential client first becomes aware of the firm and ends when that person becomes a paying client.

Canonical marketing lifecycle:
1. Discovery
2. Interest
3. Consideration
4. Inquiry (also known as Intake)
5. Conversion (marketing term)

Terminology rule:
- `conversion` is the canonical marketing-stage label.
- `onboarding` is the fulfillment-stage label for the downstream handoff event.

Boundary rule: Marketing ends at the end of Conversion.
Handoff rule: The completed Conversion event is handed off into fulfillment as `onboarding`.

Post-conversion activities are not marketing and must be classified outside the marketing lifecycle, including:
- Client Service
- Delivery
- Client Retention
- Client Expansion

Authority (Principles referenced): PRN-020, PRN-021, PRN-027
Enforcement expectation: Artifacts, runs, or workflows that classify non-marketing stages as marketing are non-compliant and must be reclassified with governance review.
Supersedes: None
Version: 0.2
Status: Draft
