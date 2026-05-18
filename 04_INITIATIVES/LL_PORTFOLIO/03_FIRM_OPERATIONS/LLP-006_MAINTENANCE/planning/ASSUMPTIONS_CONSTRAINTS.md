---
id: 04_initiatives_ll_portfolio_03_firm_operations_llp_006_maintenance_planning_assumptions_constraints_md
title: Assumptions and Constraints
owner: ML1
status: draft
created_date: 2026-05-18
last_updated: 2026-05-18
tags: []
---

# Assumptions and Constraints

Project ID: LLP-006
Project Path: 03_FIRM_OPERATIONS/LLP-006_MAINTENANCE
Stage: Planning

## Assumptions
- `matter_id` remains the canonical cross-system identity key.
- Clio active-matter records are accessible each Sunday.
- SharePoint folder metadata is readable and mappable to matter IDs.
- Asana tasks can be filtered or tagged by matter context for reconciliation use.
- Prior-cycle artifacts remain available for deterministic diffing.
- ML1 review cadence supports weekly exception decisioning.

## Constraints
- Reconciliation must be bounded to SB, Clio, SharePoint, and Asana.
- No autonomous source-of-record writes are permitted.
- Ambiguous matches must be flagged as exceptions, not force-matched.
- Reconciliation cannot reinterpret doctrine or policy boundaries.
- Legal-delivery conclusions are out of scope.
- Missing data is handled by explicit exception output; no hidden inference.
