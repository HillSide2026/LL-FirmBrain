---
id: 04_initiatives__ll_portfolio__07_growth_projects__llp_023_matter_command_control__planning__assumptions_constraints_md
title: Matter Command and Control - Assumptions and Constraints
owner: ML1
status: draft
created_date: 2026-03-23
last_updated: 2026-03-23
tags: [matter-command-control, planning, assumptions, constraints]
---

# Assumptions and Constraints

Project ID: `LLP-023`
Stage: `Planning`

## Assumptions

- Clio matter number remains the primary join key for the command layer
- Gmail label structure and SharePoint naming can become stable enough to
  support bounded deterministic routing
- a daily derivative command layer is valuable even if it does not replace any
  existing source system
- a `25`-thread daily Gmail review pass is operationally manageable for ML1
  oversight and controlled execution
- ambiguous cases should be surfaced as exceptions, not force-fit into false
  certainty
- the right next step is prioritization discipline, not broader feature
  expansion

## Constraints

- Clio, Gmail, and SharePoint remain authoritative
- no broad or unapproved write-back to source systems is permitted
- Gmail state or matter labeling is allowed only as a narrow, approval-gated,
  audit-logged label write
- no shadow source-of-truth database is permitted
- every generated assertion must include a source pointer
- approved persisted state is limited to caches and run state needed for
  normalized execution
- later slices may not outrun the trust and stability of earlier slices
- heuristic fallbacks must remain review-aware rather than silently authoritative
- each reviewed Gmail thread must end in exactly one canonical state label

## Locked Planning Direction

Currently locked:

- Slice 1 is the current priority
- slice prioritization is the main job of Planning
- `IMPLEMENTATION_SPEC.md` and `MILESTONE_PLAN.md` are support inputs, not the
  canonical planning packet
- the command layer remains a derivative control layer, not a new operating
  system of record

## Still Not Locked

- exact promotion threshold from Slice 1 to Slice 2
- exact review sampling method for routing confidence
- exact treatment of SharePoint override mappings
- whether Slice 3 or Slice 4 is the higher-value post-Slice-2 step
- whether the current thin Slice 1 implementation is already close enough to
  the minimum viable daily run
