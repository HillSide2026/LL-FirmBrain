---
id: POL-052
title: Client Engagement Stage Policy
owner: ML1
status: approved
approved_by: ML1
approved_date: 2026-04-18
version: 0.1
created_date: 2026-02-24
last_updated: 2026-03-23
tags: [policy, matters, client, engagement]

effective_date:
supersedes:

provenance:
  decided_by: ML1
  decided_on:
  context:
---

# Client Engagement Stage Policy

**Document ID:** POL-052
**Status:** DRAFT
**Effective:** TBD
**Authority:** ML1

---

## 1. Purpose

This policy defines `engagement_stage` as the lifecycle state of the **client relationship** — not the individual matter.

`engagement_stage` operates at the **client/contact level**, spanning the full relationship across all matters. It is analogous to deal stages in a CRM (e.g. HubSpot).

`engagement_stage` is distinct from:
- `fulfillment_status` — the administrative lifecycle of a specific matter (matter level), governed by POL-034
- `delivery_status` — the priority/importance tier of a matter (`essential` / `strategic` / `standard` / `normal`, highest to lowest), governed by PRO-019. Note: `parked` is no longer a `delivery_status` value; it is a `delivery_stage` value, governed by POL-071.
- `delivery_stage` — the current activity state of a matter (`active` / `parked` / `backlog`), governed by POL-071
- matter `status` — the top-level Clio state (`open` / `pending` / `closed`)

`engagement_stage` is a field on the **client/contact record**, not on the matter.

---

## 2. Canonical Engagement Stages

| Stage | Description | Matter Status |
|-------|-------------|---------------|
| Inquiry | Pre-consult; not yet qualified | `pending` |
| Onboarding | Consult scheduled; engagement letter being prepared | `pending` |
| Active | At least one matter in Opening or Maintenance | `open` |
| Lapsed | No open matters; relationship exists but dormant | — |
| Closed | All matters closed; relationship ended | `closed` |

Notes:
- **Inquiry** belongs to the client record, not to marketing. It is the entry point for all new clients regardless of how they were acquired.
- **Onboarding** is a shared boundary: marketing ends here; fulfillment begins here. It appears in both the client engagement stage model and the matter fulfillment lifecycle (POL-034).
- A returning client opening a new matter enters at **Active** — they do not repeat Inquiry or Onboarding.
- A client may be Active across multiple concurrent matters at different fulfillment stages.

---

## 3. Relationship to Fulfillment

Fulfillment (POL-034) operates at the matter level. The client engagement stage reflects the aggregate relationship state across all matters:

- Client moves from Inquiry → Onboarding when the first consult is scheduled.
- Client moves from Onboarding → Active when the first engagement is signed (Opening begins on the matter).
- Client remains Active while any matter is in Opening, Maintenance, or Pending Close.
- Client moves to Lapsed when all matters are Closed and no active engagement exists.
- Client moves to Closed when the relationship is formally ended.

---

## 4. Authority Rules

- ML1 is the sole authority for advancing or overriding engagement_stage.
- System/agent layers may report and flag but may not self-authorize stage transitions.

---

## 5. Governance Rules

- `engagement_stage` must not be used as a field on MATTER.yaml or any matter-level artifact.
- Any reference to engagement_stage in matter-level schemas is non-compliant and must be removed.
- The source of truth for engagement_stage is the client/contact record (Clio or designated CRM).
