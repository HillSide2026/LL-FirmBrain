---
id: POL-071
title: Matter Delivery Stage Policy
owner: ML1
status: approved
approved_by: ML1
approved_date: 2026-05-18
version: '1.1'
created_date: 2026-05-18
last_updated: 2026-05-18
tags: [policy, matters, delivery-stage, backlog, parked]
---

# POL-071 — Matter Delivery Stage Policy

## 1. Purpose

Define `delivery_stage` as an independent classification axis on a matter, orthogonal to `delivery_status`.

This policy separates two concepts that were previously conflated under `delivery_status`:

| Field | Meaning | Vocabulary |
|---|---|---|
| `delivery_status` | Priority or importance tier of the matter | `essential`, `strategic`, `standard`, `normal` |
| `delivery_stage` | Current activity state of the matter | `backlog`, `activated`, `active`, `parked`, `finished` |

`delivery_status` answers: how important is this matter to the firm?
`delivery_stage` answers: where is this matter in its activity lifecycle?

## 2. Delivery Stage Vocabulary

| Stage | Meaning |
|---|---|
| `backlog` | Matter is registered but not yet opened; queued for future activation |
| `activated` | Matter has been formally opened; engagement begun but not yet in active working delivery |
| `active` | Matter is currently being worked |
| `parked` | Matter was active or activated; now dormant; may be re-engaged |
| `finished` | Delivery is complete; matter is pending formal closure and archive |

## 3. Canonical Lifecycle

The normal progression is:

```
backlog → activated → active → finished
                   ↕
                parked
```

- A matter moves from `backlog` to `activated` when ML1 decides to open the engagement.
- A matter moves from `activated` or `active` to `parked` when work stops but the matter remains open.
- A matter moves from `parked` back to `active` or `activated` when work resumes.
- A matter moves to `finished` when delivery is complete and the matter is ready for closure.

## 4. Orthogonality

`delivery_stage` and `delivery_status` are independent. Any combination is valid:

| Example | Meaning |
|---|---|
| `essential` + `active` | High-priority matter, currently being worked |
| `essential` + `parked` | High-priority matter, currently dormant |
| `standard` + `backlog` | Standard matter, registered but not yet opened |
| `strategic` + `activated` | Strategic matter formally opened, engagement begun |
| `standard` + `finished` | Standard matter, delivery complete, pending closure |

## 5. Relationship to `status`

`delivery_stage` applies to matters with top-level `status: open` or `status: pending`.

Matters with `status: closed` do not carry an active `delivery_stage`.

## 6. Filing Locations

Matter folders are organized by `delivery_status` tier. `delivery_stage` is recorded in the matter record (MATTER.yaml), not by folder.

| Delivery Status | Physical Filing Location |
|---|---|
| `essential` | `05_MATTERS/ESSENTIAL/` |
| `strategic` | `05_MATTERS/STRATEGIC/` |
| `standard` | `05_MATTERS/STANDARD/` |
| `normal` | `05_MATTERS/NORMAL/` |

`delivery_stage: backlog` matters are additionally indexed in `05_MATTERS/LL_ACTIONS/MATTER_BACKLOG.md`.

Note: `05_MATTERS/PARKED/` was the prior filing location when `parked` was a `delivery_status` value. It is now deprecated. All formerly-parked matters have been moved to `05_MATTERS/NORMAL/` with `delivery_stage: parked`.

## 7. Authority and Transitions

- ML1 is the authority for all `delivery_stage` transitions.
- System agents may signal that a stage transition is warranted but may not self-authorize it.
- `delivery_stage` transitions are recorded in the matter record.

## 8. Related Artifacts

| Artifact | Purpose |
|---|---|
| INV-0003 | Matter Model Structural Invariants — defines delivery_stage as a required field |
| POL-052 | Client Engagement Stage Policy — delivery_status vocabulary (tier only) |
| PRO-013 | Matter Filing Protocol |
| `05_MATTERS/LL_ACTIONS/MATTER_BACKLOG.md` | Unified index of open matters with delivery_stage: active, activated, or backlog — organized by delivery_status then delivery_stage |
