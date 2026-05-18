---
id: 04_initiatives_ll_portfolio_03_firm_operations_llp_005_opening_planning_measurement_method_md
title: Measurement Method
owner: ML1
status: draft
created_date: 2026-05-18
last_updated: 2026-05-18
tags: []
---

# Measurement Method

Project ID: LLP-005
Project Path: 03_FIRM_OPERATIONS/LLP-005_OPENING
Stage: Planning

## Method
- Use opening run artifacts as primary measurement source.
- Require evidence pointers for Gate 2 intake and Gate 3 completion events.
- Compute cycle timing from observed timestamps only.
- Track exceptions by age, type, and owner.

## Rules
- `gate2_packets_received` includes only LLP-004 handoff packets entering opening intake.
- `gate2_packets_accepted` requires packet completeness against approved intake checklist.
- `gate2_authorized_matters` includes only signed-engagement authorized entries.
- `financial_ready_within_2d` counts records with complete financial readiness evidence within 48 hours of Gate 2 intake.
- `gate3_date` is valid only when Gate 3 completion evidence and approval state exist.
- `premature_handoffs` includes any LLP-006 handoff before Gate 3 completion.

## Reporting Window
- Weekly trailing 7 days.
- Monthly rollup for trend analysis.
