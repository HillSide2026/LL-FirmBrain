---
id: llp-027_inquiries__readme_md
title: LLP-027 INQUIRIES
owner: ML1
status: initiating
project_stage: initiating
created_date: 2026-03-17
last_updated: 2026-04-01
tags: [intake, inquiries, triage, response]
parent_project: LLP-014
---

# LLP-027 INQUIRIES

## Purpose

Manages the first stage of the client intake pipeline — receipt, triage, and
initial response to incoming client inquiries across all channels (web form,
email, referral). Hands off qualified inquiries to the consultation stage
(LLP-028).

## Scope

### In Scope

- Inquiry receipt: logging all incoming contacts regardless of channel
- Triage logic: routing by practice area, urgency, and matter type
- Initial response: response templates, SLA targets, and acknowledgment
  workflow
- Handoff protocol to consultation stage (LLP-028)
- Channel coverage: web form submissions, email inquiries, phone and referral
  inquiries

### Out of Scope

- Lead capture infrastructure (LLP-026)
- Consultation scheduling and conduct (LLP-028)
- Client onboarding — marketing or operational side (LLP-029, LLP-004)
- Matter setup in Clio

## Funnel References

Inquiries sourced from funnel traffic arrive via LLP-026 (Lead Capture), which
aggregates CTA and form submissions from all three funnels:

| Funnel | Source | Inquiry Type |
|--------|--------|--------------|
| F01 | LLP-011 | Personal injury and tort inquiries |
| F02 | LLP-012 | Corporate and commercial inquiries |
| F03 | LLP-013 | Financial services inquiries |

Triage logic must classify inquiries by source funnel as well as practice
area and urgency.

## Related Projects

- LLP-014 — Intake Management (parent)
- LLP-026 — Lead Capture (upstream)
- LLP-028 — Consults (downstream)

## Initiation Artifacts

| Artifact | Status |
|----------|--------|
| `initiation/PROJECT_CHARTER.md` | complete |
| `initiation/PROBLEM_STATEMENT.md` | complete |
| `initiation/SUCCESS_CRITERIA.md` | complete |
| `initiation/STAKEHOLDERS.md` | complete |
| `initiation/RISK_SCAN.md` | complete |
| `initiation/APPROVAL_RECORD.md` | complete |

## ML1 Authority Statement

ML1 approval is required for scope, changes, and any execution commitments.
Triage logic, SLA targets, and response content require ML1 approval before
implementation.

## Approval State

`initiating — approved, advance to Planning`

## Last ML1 Review Date

`2026-04-01`
