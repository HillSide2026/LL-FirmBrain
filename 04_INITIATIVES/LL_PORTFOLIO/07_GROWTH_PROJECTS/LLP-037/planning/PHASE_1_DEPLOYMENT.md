---
id: llp-037_phase_1_deployment
title: LLP-037 Phase 1 — Internal Testing Deployment
owner: ML1
status: approved
approved_by: ML1
approved_date: 2026-05-01
created_date: 2026-05-01
last_updated: 2026-05-01
tags: [llp-037, planning, phase-1, deployment, testing]
---

# Phase 1 — Internal Testing Deployment

## Purpose

Deploy `firm.levinellp.ca` and `engine.levinellp.ca` in a limited testing state so ML1 and selected users can interact with the future LL system before full integration. This phase is about observation and feedback, not production operation.

## Status

**Testing / non-production.**

## Deployments in Scope

| URL | System | Role in Phase 1 |
|---|---|---|
| `engine.levinellp.ca` | LL-WrkEngine (Mike) | Test deployment — workflow navigation, document upload, AI chat, matter views |
| `firm.levinellp.ca` | LL-task-tracker | Internal testing / control surface or landing page |

## Scope

- `engine.levinellp.ca` — test deployment of LL-WrkEngine. Users can create test projects, upload documents, run workflows, and interact with AI chat.
- `firm.levinellp.ca` — internal testing or control surface. Navigation, matter views, and admin lifecycle UI accessible for review.
- Users may test workflows, navigation, matter views, and usability.
- Data may be fake, seeded, or manually entered. No requirement for live Lexora or Clio sync in Phase 1.

## Explicit Exclusions

The following are **explicitly out of scope** for Phase 1. Any use of these deployments for excluded purposes is non-compliant.

| Exclusion | Reason |
|---|---|
| Client-facing access | Phase 1 is internal testing only |
| Production legal work | No reliance on outputs for real matters |
| Authoritative matter record | Lexora / Clio remain authoritative |
| Authoritative document record | ll-corporate-records is not yet integrated |
| Billing, deadlines, filings, or client delivery | Non-production environment; no legal reliance |

## Required Label

All pages on both deployments must clearly display:

> **Testing Environment — Not for Production Use**

This label must be persistent and visible on every page, not only on login. Implementation is a Phase 1 acceptance requirement.

## Phase 1 Success Criteria

| Criterion | Description |
|---|---|
| Login | Users can authenticate and access the testing environment |
| Matter / project views | Users can view test matters (projects) in LL-WrkEngine and firm.levinellp.ca |
| Workflow navigation | Users can open, navigate, and step through basic workflows in LL-WrkEngine |
| Observation | ML1 can observe what works and what breaks in a real interaction |
| Feedback capture | Feedback from testing can be captured and fed into ML2 / planning backlog |

## Phase 1 Does Not Gate

Phase 1 completion does not require Lexora integration, ll-corporate-records integration, or any production workflow to be functional. It is a usability and orientation phase.

## Phase 2 Dependencies (Not in Scope Here)

The following are Phase 2 concerns and must not be conflated with Phase 1:

- Lexora sync model and matter state integration
- LL-WrkEngine workflow templates for corporate services
- ll-corporate-records document ingestion integration
- Client portal activation (ll-corporate)
- Accounts lifecycle implementation

## Deployment Infrastructure

Per DC-001 (`ASSUMPTIONS_CONSTRAINTS.md`):

| Component | Platform | Notes |
|---|---|---|
| LL-WrkEngine frontend | Vercel | Next.js — Vercel-native |
| LL-WrkEngine backend | Render or Railway (TBD) | Full Node — required for LibreOffice, long-running processes |
| firm.levinellp.ca | TBD | LL-task-tracker deployment — separate from LL-WrkEngine infrastructure |

Platform selection between Render and Railway is an open constraint (OC-01). Verify LibreOffice availability on the chosen platform before Phase 1 deployment proceeds (OC-02).

## Notes

- `engine.levinellp.ca` maps to LL-WrkEngine repo (`LL-WrkEngine`)
- `firm.levinellp.ca` maps to LL-task-tracker repo (`LL-task-tracker`)
- Both deployments are independent; Phase 1 does not require them to be integrated with each other
