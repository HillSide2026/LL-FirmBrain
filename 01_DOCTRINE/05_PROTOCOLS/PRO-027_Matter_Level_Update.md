---
id: PRO-027
title: Matter Level Update
owner: ML1
status: draft
version: 0.1
created_date: 2026-05-20
last_updated: 2026-05-20
tags: [protocol, matters, updates, scope, change-control]
---

# PRO-027 — Matter Level Update

> **DRAFT — PENDING ML1 APPROVAL.**
> This protocol has not been approved and is not yet in effect.

---

## 1. Purpose

This protocol defines a five-level scale for changes made within an existing
matter.

It exists to prevent overreach, under-description, and scope confusion when a
matter is updated.

The governing assumption is fixed:

- the matter structure does not change

For this protocol, "matter structure does not change" means:

- no new `matter_id`
- no split, merge, or retirement of matters
- no reclassification of one matter into multiple matters
- no change to the matter container itself

This protocol therefore governs only within-matter update scope.

---

## 2. Scope

This protocol applies whenever an agent or operator updates artifacts inside a
matter folder, including:

- `MATTER.yaml`
- `README.md`
- `MATTER_BRIEF.md`
- `ISSUES_AND_POSITIONS.md`
- `NOTES_TO_FILE.md`
- `SALES_PIPELINE.md`
- matter-local tracking files, watchlists, and summaries
- derived indexes or dashboards that reflect matter-local canonical state

It does not govern:

- creation of a new matter
- deletion, merger, or supersession of a matter
- changing the number of matters used to represent a client relationship

Those are structural changes and are outside this protocol.

For clarity, a change is not structural if it only changes matter-internal
artifacts such as:

- summaries
- notes
- briefs

---

## 3. Classification Rule

Before making a matter update, classify the intended change at one of the five
levels below.

If the change includes elements from multiple levels, classify it at the
highest level reached.

If uncertain between two levels, use the higher level.

---

## 4. The Five Levels

### Level 1 — Sync

Least extensive.

Purpose:
- typo, date, wording only

Typical changes:
- typo fixes
- formatting cleanup
- stale dates or `last_updated` fields
- broken links
- wording cleanups that do not alter substance

What does not happen at Level 1:
- no change to the matter thesis
- no change to current priorities
- no change to service inventory
- no new substantive facts introduced

### Level 2 — Refresh

Low-extensiveness update.

Purpose:
- sync current-facing matter files to an already-accepted posture

Typical changes:
- refresh `README.md`, `MATTER_BRIEF.md`, or `MATTER.yaml` to reflect current
  posture already established elsewhere
- sync fulfillment labels, service labels, or track labels across matter files
- add a dated note recording the current posture where the facts are already
  known
- update matter-local summaries to point to the current active track, issue, or
  service

What does not happen at Level 2:
- no change to the core problem the matter is for
- no redefinition of scope
- no new service-line thesis
- no structural change to the matter container

### Level 3 — Update

Moderate update within the same matter.

Purpose:
- record a real new development in the matter, without changing the matter's
  scope or purpose

Typical changes:
- a new current development is added to the matter record
- an old development is no longer current
- deadlines, counterparties, or current posture change in a way that must be
  recorded
- the matter files are updated because the facts changed, not just because the
  summaries were stale

What does not happen at Level 3:
- the matter's scope does not change
- the matter's purpose does not change

### Level 4 — Rewrite

High-extensiveness update within a fixed matter structure.

Purpose:
- substantially revise multiple files within a matter to reflect accumulated
  developments, but without changing the matter's scope or purpose

Typical changes:
- multiple matter files require substantial revision
- the revisions reflect accumulated developments rather than a single new fact
- the write-up of the matter is being broadly refreshed while the matter remains
  the same matter for the same purpose

What does not happen at Level 4:
- still no new `matter_id`
- still no split or merger
- still no change to the matter's scope or purpose

### Level 5 — Reframing

Most extensive update permitted under this protocol.

Purpose:
- materially reframe how the matter is described, without changing the matter's
  scope or purpose

Typical changes:
- the matter description is materially reframed
- the governing explanation of the matter changes
- current-facing matter artifacts are rewritten to reflect the new framing
- the matter remains the same matter for the same scope and purpose

Boundary note:
- if the update truly requires a new matter, a split, a merger, or a change to
  the matter map, it is not a Level 5 matter-level update
- it is a structural matter change and falls outside this protocol

---

## 5. Operational Use

When describing or proposing a matter update, state:

1. the target matter
2. the intended level
3. the reason for that level
4. the artifacts expected to change

Suggested format:

```text
Matter: [matter_id]
Update level: [1-5]
Why: [short reason]
Artifacts: [file list]
```

---

## 6. Interpretation Notes

- Level 1 fixes wording.
- Level 2 catches the files up.
- Level 3 records a real new development.
- Level 4 substantially rewrites multiple files.
- Level 5 changes the framing, but not the matter's scope or purpose.

The scale is cumulative in significance, not in word count. A short edit may
still be Level 4 or Level 5 if it changes the matter's governing understanding.

---

## 7. Related Doctrine

- `01_DOCTRINE/01_INVARIANTS/INV-0003-matter-model-structural-invariants.md`
- `01_DOCTRINE/01_INVARIANTS/INV-0017-matter-identity-authority-and-lifecycle.md`
- `01_DOCTRINE/03_POLICIES/POL-054_Matter_Summary.md`
- `01_DOCTRINE/05_PROTOCOLS/PRO-019_Matter_Summary_and_Task_Governance.md`
- `01_DOCTRINE/05_PROTOCOLS/PRO-025_Matter_Update_Context_Hydration.md`

---

## 8. Change Log

| Version | Date | Change |
|---|---|---|
| 0.1 | 2026-05-20 | Initial draft. Creates a five-level scale for within-matter updates while holding matter structure constant. |
