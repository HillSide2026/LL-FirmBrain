---
id: llp_012__stage2_planning_research_note__target_segment_comparison_existing_owners_vs_new_entrants__2026_03_10
title: Stage 2 Planning Research Note — Target Segment Comparison (Existing Owners vs New Entrants)
owner: ML1
status: draft
project_stage: planning
created_date: 2026-03-10
last_updated: 2026-03-10
tags: [llp-012, planning, funnel-02, targeting, segmentation]
---

# Stage 2 Planning Research Note — Target Segment Comparison

## Planning Comment Added
Funnel 2 has a second potential target:
- operators acquiring an existing operating business (independently or with backing).

This cohort is now designated as a planning-stage research target and is not yet a canonical ICP replacement.

## Cohorts to Compare
1. Existing owners/operators (current primary hypothesis)
2. New entrants via acquisition (secondary hypothesis)

## Comparison Questions
1. Which cohort shows higher paid diagnostic conversion rate?
2. Which cohort shows stronger remediation and retainer attach rates?
3. Which cohort has faster time-to-conversion?
4. Which cohort has lower qualification fallout at `inquiry` and `intake_completed`?
5. Which cohort yields better unit economics (CAC to paid diagnostic and downstream value)?

## Data Model Requirement
For each qualified inquiry and conversion event, capture:
- `operator_cohort`: `existing_owner` or `new_entrant_acquisition`
- `acquisition_mode`: `independent` or `backed` (for new entrants only)
- `sdr_fit_decision`
- `paid_diagnostic_purchase`
- `remediation_conversion`
- `retainer_conversion`

## Decision Gate
No ICP change is permitted until ML1 reviews cohort comparison output and approves:
- maintain current ICP focus,
- broaden to dual-cohort strategy,
- or re-segment Funnel 2 by cohort.

## Planning Outcome
This research track is now in-scope for Stage 2 planning and must be evaluated before implementation-scale allocation decisions.

