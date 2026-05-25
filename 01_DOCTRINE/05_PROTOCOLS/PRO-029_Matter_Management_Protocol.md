---
id: PRO-029
title: Matter Management Protocol
owner: ML1
status: draft
version: 0.1
created_date: 2026-05-25
last_updated: 2026-05-25
tags: [protocol, matters, matter-management, canonical-fields, authority-boundary]
---

# PRO-029 — Matter Management Protocol

> **DRAFT — PENDING ML1 APPROVAL.**
> This protocol has not been approved and is not yet in effect.

---

## 1. Purpose

This protocol defines the Matter Management layer.

It answers:

1. what the canonical matter record is,
2. which fields belong to matter-level canon,
3. when matter-level canon changes,
4. which artifacts are not canonical matter record artifacts, and
5. when a development should be routed to Matter Administration or Matter File
   Administration instead of changing matter canon.

The controlling rule is:

- matter-level canon changes only when a canonical matter-record field changes

If a development does not change a canonical matter-record field, it does not
justify a matter-canon update under this protocol.

---

## 2. Scope

This protocol governs the canonical matter record for LL matters.

It applies to:

- `05_MATTERS/*/{matter_id}/MATTER.yaml`
- `05_MATTERS/MATTER_REGISTRY.md`
- any other artifact explicitly designated by ML1 as part of the canonical
  matter record

It does not govern:

- operational summaries, queues, and dashboards
- Gmail / SharePoint / Clio mapping and verification outputs
- notes, timelines, briefs, issue summaries, or other non-canonical matter
  artifacts

Those belong to other layers unless separately elevated by doctrine.

---

## 3. Layer Distinction

Three layers are distinct:

| Layer | Core question | Canon authority |
|---|---|---|
| Matter Management | Did the matter record itself change? | Yes |
| Matter Administration | What needs operational attention around this matter? | No |
| Matter File Administration | What belongs to this matter file across systems, and what does the source evidence show? | No |

Matter Administration and Matter File Administration may inform Matter
Management, but neither may silently rewrite matter canon.

---

## 4. Canonical Matter Record

### 4.1 Preferred canonical record

The preferred matter-local canonical record is `MATTER.yaml`.

`05_MATTERS/MATTER_REGISTRY.md` may duplicate a subset of canonical fields for
registry/indexing purposes, but does not by itself authorize canon changes that
are absent from the matter-local record.

### 4.2 Conflict rule

If duplicate representations of canonical fields conflict:

1. treat the matter as having a canonical-state conflict,
2. do not silently choose a winner based on convenience,
3. escalate for Matter Management reconciliation.

Derived artifacts never override canonical matter-record fields.

---

## 5. Canonical Matter-Record Metadata

The canonical matter-record metadata fields under this protocol are:

1. `matter_id`
2. `clio_matter_id`
3. `status`
4. `delivery_status`
5. `fulfillment_status`
6. `services`
7. `client_name`
8. `instructing_officer_name`
9. `matter_description`
10. `engagement_date`
11. `closed_date` once set

### 5.1 Field semantics

| Field | Meaning | Notes |
|---|---|---|
| `matter_id` | Canonical matter identifier | Must match `clio_matter_id` if both are present |
| `clio_matter_id` | Clio identifier for the same matter | No separate identity from `matter_id` |
| `status` | Top-level matter state | Allowed values: `Pending`, `Open`, `Closed` |
| `delivery_status` | Matter importance tier | Matter-level priority / importance |
| `fulfillment_status` | Matter operational priority state | Matter-level fulfillment posture |
| `services` | Canonical service umbrella | Each entry must use `service_type` and `service_name` |
| `client_name` | Client identity for the matter | Canonical client field |
| `instructing_officer_name` | Canonical instructing officer for the matter | If absent in older matters, absence is a data gap, not permission to infer |
| `matter_description` | Canonical description of the engagement | Short matter-definition field |
| `engagement_date` | Canonical engagement/opening date | Matter-level date |
| `closed_date` | Canonical closure date | Immutable once validly set |

### 5.2 Open-matter service presumption

Every matter with `status: Open` is presumed to have at least one service
entry.

If an open matter has no service entry recorded, treat that as a canonical data
gap requiring Matter Management correction.

### 5.3 Congruence rule

If both `matter_id` and `clio_matter_id` are present, they must contain the
same value.

A mismatch is non-compliant and must be escalated as a canonical identity
conflict.

---

## 6. Not Canonical Under This Protocol

The following are not canonical matter-record metadata under this protocol:

- `README.md`
- `MATTER_BRIEF.md`
- `MATTER_STATUS.md`
- `FACTS_TIMELINE.md`
- `ISSUES_AND_POSITIONS.md`
- `NOTES_TO_FILE.md`
- `SALES_PIPELINE.md`
- dashboards, digests, queues, and tracker entries
- file maps, gap reports, folder assessments, and document-delta outputs
- Gmail threads, SharePoint folders, Clio notes, and other external artifacts

They may summarize, support, evidence, or route matter work, but they do not
constitute the canonical matter record.

### 6.1 Legacy-field note

This draft does not include `delivery_stage` in the canonical matter-record
metadata set.

If other doctrine or legacy artifacts still treat `delivery_stage` as
matter-canonical, that doctrine remains unreconciled and should be treated as a
formal reconciliation issue rather than silently blended into this protocol.

`engagement_stage` is expressly excluded from matter-level artifacts by
existing doctrine and remains non-canonical at the matter level.

---

## 7. Change Gate

A matter-level canon update is warranted only when one or more canonical
matter-record fields in Section 5 changes.

Examples that do justify Matter Management updates:

- a matter opens, closes, or reopens
- `delivery_status` changes
- `fulfillment_status` changes
- a service is added, removed, renamed, or reclassified
- the canonical client or instructing officer changes
- the matter description changes
- `closed_date` is set

Examples that do not by themselves justify Matter Management updates:

- a new email arrives
- a lawyer sends follow-up instructions
- a deadline is mentioned in correspondence
- a SharePoint folder receives new documents
- a matter summary becomes stale
- a file-mapping gap is discovered

Those developments may justify another layer's update, but not a matter-canon
update unless they change a canonical field.

---

## 8. Routing Rule

When a new development occurs, route it as follows:

1. **Canonical field changed** -> Matter Management
2. **Operational posture, queue, task, deadline, or ML1-attention changed, but
   no canonical field changed** -> Matter Administration
3. **Cross-system membership, source verification, folder compliance, or
   document inventory changed, but no canonical field changed** -> Matter File
   Administration
4. **No governed artifact needs updating** -> no matter-layer write

If uncertain whether a canonical field changed, escalate rather than infer.

---

## 9. Operational Consequences

1. Matter canon must be sparse and stable.
2. Non-canonical matter artifacts may be updated more freely, but must not
   present themselves as changing canon.
3. Matter summaries and notes may report developments inside the matter without
   automatically causing Matter Management changes.
4. A development inside the matter is not the same thing as a change to the
   matter record.

---

## 10. Relationship to Other Doctrine

- `INV-0003` defines Matter as the economic/control container and prevents
  derived artifacts from overriding canonical fields.
- `INV-0006` places the Matter File subordinate to Matter identity.
- `INV-0017` defines matter identity authority and lifecycle.
- `POL-043` confirms the Clio matter ID as canonical identifier structure.
- `POL-067` governs authoritative-source verification.
- `PRO-027` applies only after this protocol determines that a write to
  matter-level canon is actually warranted.

---

## 11. Change Log

| Version | Date | Change |
|---|---|---|
| 0.1 | 2026-05-25 | Initial draft. Defines Matter Management as the sole layer for canonical matter-record changes and formalizes the canonical field set confirmed by ML1. |
