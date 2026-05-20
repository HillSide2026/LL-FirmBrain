---
id: INV-0018
title: 'INV-0018: Canonical Project Types'
owner: ML1
status: approved
approved_by: ML1
approved_date: 2026-05-19
version: '1.0'
created_date: 2026-05-19
last_updated: 2026-05-19
tags: [doctrine, invariants, projects, typing]
---

# INV-0018 — Canonical Project Types

## Purpose

Define the canonical project types used across the repository so project
governance is driven by a stable and explicit classification model.

## Structural Rule

Every governed project must carry exactly one canonical project type.

The canonical type set is:

- `Strategic`
- `Management`
- `Operational`
- `Decision`

These are governance types, not marketing labels or effort estimates.

## Canonical Type Definitions

### 1. Strategic

A strategic project is a change initiative that defines or materially changes
long-horizon direction, capability, ownership posture, or structural operating
position.

Use `Strategic` when the main question is how the enterprise, portfolio, or
capability should be positioned over time.

### 2. Management

A management project is a change initiative focused on governance, control,
coordination, monitoring, or optimization of existing systems or operating
domains.

Use `Management` when the main objective is to improve control, visibility,
coordination, or operating discipline rather than to build a new capability.

### 3. Operational

An operational project is a bounded execution-focused initiative that improves,
implements, or stabilizes how defined work is carried out.

Use `Operational` when the main objective is a concrete implementation,
stabilization, or improvement outcome within an already-defined operating scope.

### 4. Decision

A decision project is a bounded option-framing initiative used to structure,
compare, and decide whether a proposed build, partnership, divestiture, or new
venture path should advance, be reclassified, or be closed.

A decision project:

- is evaluation-first, not execution-first
- exists to produce a clear ML1 go / hold / no-go or reclassification decision
- may conclude by closing or by being reclassified into another project type

Use `Decision` when the main objective is disciplined choice, not material
execution.

## Type Selection Rules

### One Type Only

Each project must use exactly one canonical project type for governance
purposes.

Dual typing such as `Strategic + Operational` or `Management / Decision` is not
allowed.

### Primary Objective Controls

Project type is determined by the project's primary governance objective, not
by:

- project importance
- project size
- current enthusiasm level
- artifact count
- current delivery stage
- which portfolio contains it

### Explicit Reclassification

If a project's primary objective changes, the project may be reclassified only
through explicit ML1 approval recorded in the relevant project artifacts and
registers.

### Rendered Labels

The canonical stored values are:

- `Strategic`
- `Management`
- `Operational`
- `Decision`

Prose may render these as `Strategic Project`, `Management Project`,
`Operational Project`, or `Decision Project`, but the underlying type remains
one of the four canonical values above.

## Related Doctrine

- `01_DOCTRINE/01_INVARIANTS/INV-0012-project-structural-boundaries.md`
- `01_DOCTRINE/03_POLICIES/POL-055_Repository_Project_Policy.md`
- `01_DOCTRINE/03_POLICIES/POL-056_Firm_Project_Policy.md`
- `01_DOCTRINE/03_POLICIES/POL-063_Project_Risk_Artifact_Lifecycle_Policy.md`
