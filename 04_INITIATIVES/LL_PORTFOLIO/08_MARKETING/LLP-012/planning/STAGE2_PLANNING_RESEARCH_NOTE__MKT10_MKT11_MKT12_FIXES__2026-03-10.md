---
id: llp_012__stage2_planning_research_note__mkt10_mkt11_mkt12_fixes__2026_03_10
title: Stage 2 Planning Research Note — Funnel 02 Agent Review Fixes
owner: ML1
status: draft
project_stage: planning
created_date: 2026-03-10
last_updated: 2026-03-10
tags: [llp-012, planning, funnel-02, mkt-10, mkt-11, mkt-12]
---

# Stage 2 Planning Research Note — Funnel 02

## Purpose
Record planning-stage corrections from the MKT-10/MKT-11/MKT-12 review for Funnel 02.

## Planning-Scope Changes Applied

1. Metadata and naming normalization
- Updated `funnel.yaml` canonical name from legacy Funnel 01 labeling to `Funnel 02 Future State`.
- Updated version and history to reflect normalization.

2. Pipeline lifecycle ownership boundaries
- Added explicit `stage_ownership` mapping in `pipeline.yaml`:
  - marketing
  - shared_handoff
  - fulfillment
- Added `lifecycle_boundary` block clarifying:
  - marketing terminal event
  - handoff stage
  - fulfillment entry stage
  - terminology note: conversion (marketing) vs onboarding (fulfillment).

2A. Canonical lifecycle normalization
- Expanded awareness into explicit sequential checkpoints:
  - `awareness_discovery`
  - `awareness_interest`
- Preserved canonical sequence to match doctrine:
  - `lead_magnet_downloaded` -> consideration
  - `inquiry_submitted` -> inquiry (alias: intake)
  - `intake_completed` -> inquiry readiness checkpoint
  - `health_check_purchased` -> conversion (marketing terminal event)
- Set `health_check_purchased` as fulfillment handoff state in `lifecycle_boundary`.

3. Competitive differentiation codification
- Added `COMPETITIVE_DIFFERENTIATION_MATRIX.md` to define:
  - key alternatives
  - structural weaknesses of alternatives at Stage 3-4
  - Funnel 02 differentiators
  - stage-based category messaging guardrails.

## Updated Planning Artifacts
- `04_FUNNELS/funnel-02/funnel.yaml`
- `04_FUNNELS/funnel-02/pipeline.yaml`
- `04_FUNNELS/funnel-02/FUNNEL_SPEC.md`
- `04_FUNNELS/funnel-02/COMPETITIVE_DIFFERENTIATION_MATRIX.md`
- `04_FUNNELS/funnel-02/AGENT_REVIEW_MKT10_MKT11_MKT12_2026-03-10.md`

## Planning Outcome
Funnel 02 now has:
- canonical naming consistency,
- explicit lifecycle boundaries,
- codified competitive framing for message discipline,
- canonical lifecycle mapping without discovery/interest/consideration/inquiry/conversion ambiguity,
- explicit conversion-as-handoff state aligned to project stage semantics.

These are planning-stage governance updates and do not authorize launch without ML1 approval.
