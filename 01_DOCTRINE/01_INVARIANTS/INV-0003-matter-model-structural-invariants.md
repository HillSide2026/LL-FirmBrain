---
id: INV-0003
title: Matter Model Structural Invariants
owner: ML1
status: approved
approved_by: ML1
approved_date: 2026-04-26
version: 1.2
created_date: 2026-03-08
last_updated: 2026-04-26
tags: [invariant, matters, model]
---

# Matter Model Structural Invariants (Binding Invariant)

## Invariant
The matter domain model is a structural contract. The following properties must remain true.

## Structural Rules
1. Matter is the economic/control container.
2. Solution is a child monetizable unit of a Matter.
3. Strategy is a child monetizable unit of a Matter.
4. Solution and Strategy are both Service types.
5. Service is an open-ended supertype; Solution and Strategy are required subtypes but do not exhaust all possible service forms.
6. `matter_id` is globally unique and immutable.
7. Every Solution must belong to exactly one valid `matter_id` (no orphan solutions).
8. Every Strategy must belong to exactly one valid `matter_id` (no orphan strategies).
9. A Matter has exactly one top-level `status`, with allowed values: `open`, `pending`, `closed`.
10. A Matter has exactly one `delivery_status`. `delivery_status` is the priority/importance tier of the matter. Allowed values: `essential`, `strategic`, `standard`, `normal`. Tier order (highest to lowest): `essential` → `strategic` → `standard` → `normal`. (Note: `parked` was a prior vocabulary variant; it is now a `delivery_stage` value, not a `delivery_status` value.)
11. A Matter has exactly one `fulfillment_status`.
11a. A Matter with top-level `status: open` or `status: pending` has exactly one `delivery_stage`. `delivery_stage` is the current activity state of the matter. Allowed values: `backlog`, `activated`, `active`, `parked`, `finished`. `delivery_stage` is an independent axis from `delivery_status`. Governed by POL-071.
12. Canonical structured fields are source of truth; summaries, dashboards, digests, and action queues are derived views and must not override canonical fields.
13. Derived command-layer outputs may append ML1-action fields and operational-signal overlays, but may not collapse, recode, or substitute for canonical `delivery_status` or `fulfillment_status`.
14. Matter File mappings and external artifacts may enrich or evidence a Matter, but may not redefine `matter_id`, `status`, `delivery_status`, or `fulfillment_status`.
15. **Taxonomy Separation Rule:** `delivery_status` (matter-level) and `service_type` (service-level) are independent classification axes. `delivery_status` must not be used to infer `service_type`. `service_type` must not be used to infer `delivery_status`. A matter with `delivery_status: strategic` may contain services of `service_type: strategy` or `service_type: solution` or both.
16. Every Matter must contain at least one Service.
17. Service streams (also called service workstreams) are sub-units of a specific Service. They are described within the service entry and must not be listed as separate top-level Service entries in MATTER.yaml.

## Boundary
This invariant defines structure and cardinality only. Policy documents define operational status vocabularies, transitions, and thresholds.
