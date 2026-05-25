---
id: 04_initiatives__ll_portfolio__07_growth_projects__llp_023_matter_command_control__planning__scope_statement_md
title: Matter Command and Control - Scope Statement
owner: ML1
status: draft
created_date: 2026-03-23
last_updated: 2026-03-28
tags: [matter-command-control, planning, scope]
---

# Scope Statement

Project ID: `LLP-023`
Project Path: `04_INITIATIVES/LL_PORTFOLIO/07_GROWTH_PROJECTS/LLP-023`
Stage: `Planning`

## Planning Use

Use this file to lock what LLP-023 is actually building first, what is
explicitly deferred, and what boundaries cannot be crossed while the command
layer is being prioritized.

## Governing Design Rule

LLP-023 succeeds only if uncertain cases stay visibly uncertain.

## In Scope

- a deterministic, derivative command layer for matter visibility
- a narrower derivative ML1-action layer inside that command layer
- explicit slice prioritization across:
  - Slice 1: matter index, Gmail routing, digest, unmapped exceptions
  - Slice 2: SharePoint document index and delta visibility
  - Slice 3: deadline extraction and radar
  - Slice 4: communications draft packets
- refinement of Matter Summary and digest outputs so they distinguish:
  - persistent ML1 visibility
  - ML1 action required now
  - delegated fulfillment handling
  - fulfillment escalation
- source-of-truth boundaries across Clio, Gmail, and SharePoint
- citation-backed output rules
- approved cache and run-state limits
- promotion criteria for moving from one slice to the next
- daily run and single-matter run modes
- a bounded Gmail review pass of up to `25` threads per daily run
- moving each reviewed Gmail thread into exactly one canonical state label
  through the governed Gmail label-write path

## Out of Scope

- replacing Clio, Gmail, or SharePoint as systems of record
- replacing durable matter attributes such as `delivery_status` or
  `fulfillment_status`
- broad or unapproved source-system mutation
- maintaining a shadow source-of-truth database
- silently assigning ambiguous threads instead of surfacing them
- expanding into later slices before earlier slices have passed their gates
- autonomous client or matter communication
- production governance activation without ML1 approval

## Write-Back Definition

For LLP-023, `write-back` means any mutation applied to an external source
system.

- controlled Gmail state or matter labeling counts as a narrow write-back
- that narrow write-back is permitted only when it uses canonical labels, has an
  explicit ML1 approval artifact, and produces an audit trail
- broader source mutation remains out of scope, including message-content
  changes, send/archive/delete behavior, or operational-truth updates

## Prioritization Boundary

Current planning direction is:

1. **Priority 1 — Slice 1**
   Minimal daily command layer: matter index, label-first Gmail routing,
   `MATTER_DIGEST.md`, `INBOX_UNMAPPED.md`, routed matter status files, and a
   clean distinction between ML1 visibility and ML1 action.

2. **Priority 2 — Slice 2**
   Document visibility only after Slice 1 is stable enough to trust the command
   layer's core routing and exception handling.

3. **Priority 3 — Slice 3**
   Deadline extraction only after the project can show that the daily command
   layer is stable and that deadline visibility is the next highest-value gap.

4. **Priority 4 — Slice 4**
   Communications drafts last, after the project has already proven command
   value without creating false confidence or authority drift.

## Explicit Deferrals

Not part of the current initial execution-readiness target:

- broad or unapproved source-system mutation beyond governed Gmail label writes
- broad comms automation
- advanced heuristic routing beyond bounded review-required fallbacks
- downstream operational adoption beyond the derivative command layer

## Visibility vs Action Rule

- `delivery_status` remains the durable matter attribute for ML1 relevance and
  economic/delivery importance.
- `fulfillment_status` remains the durable matter attribute for delegated
  fulfillment operating posture.
- The daily command outputs must separately answer:
  - what ML1 should continue to see
  - what actually requires ML1 action now
- Ordinary fulfillment handling should stay delegated.
- Only fulfillment escalation belongs in the ML1-action layer.

## Ambiguity Rule

When routing, mapping, or source confidence is weak, the system must surface
that weakness explicitly through review-required or exception paths rather than
quietly converting uncertainty into apparent confidence.

## Required Planning Outputs

- frozen slice order and deferral logic
- frozen source-boundary rules
- frozen promotion criteria between slices
- explicit dependency and risk packet
- explicit metric and threshold logic for slice promotion

## Gate Criteria for Executing Authorization

- Slice 1 is clearly defined as the minimum viable command layer
- later slices are explicitly deferred until gate conditions are met
- derivative-output boundaries are explicit enough to avoid shadow-system drift
- routing, citation, and exception logic are measurable
- reviewed Gmail threads are bounded to `25` per daily pass and end in exactly
  one canonical state label through the governed write path
- command outputs distinguish ML1 visibility from ML1 action without creating a
  shadow state model that conflicts with durable matter attributes
- ML1 can decide whether to continue, narrow, pause, or promote the next slice
