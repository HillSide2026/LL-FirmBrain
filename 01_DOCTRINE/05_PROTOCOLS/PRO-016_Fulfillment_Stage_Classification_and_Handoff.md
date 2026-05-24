---
id: PRO-016
title: Fulfillment Stage Classification and Handoff
owner: ML1
status: approved
approved_by: ML1
approved_date: 2026-04-18
version: 0.3
effective_date: 2026-04-18
supersedes:
provenance:
  decided_by: ML1
  decided_on: 2026-04-18
  context: Metadata normalized by system admin cleanup on 2026-05-24
created_date: 2026-03-09
last_updated: 2026-03-22
tags: [protocol, fulfillment, lifecycle, handoff, gates]
---

# PRO-016 — Fulfillment Stage Classification and Handoff

Enforces Policies: POL-034, POL-032, POL-033

Trigger condition:
- A fulfillment run, workflow, checklist, or artifact is created, updated, or promoted.
- A fulfillment stage transition is requested.
- A marketing conversion handoff is requested into fulfillment.

Required stage taxonomy:
- `onboarding`
- `opening`
- `maintenance`
- `pending_close`
- `closed`

Normalization rules:
- Canonical fulfillment stages must use the taxonomy above.
- `conversion` is a marketing-stage label; it may be accepted only as an inbound handoff alias and must be normalized to `onboarding` in canonical structured fields.
- `inquiry` is a client engagement stage (client level, not matter level) and is not a valid fulfillment stage.
- `closing` is a deprecated label; normalize to `pending_close`.
- `intake` is not a valid fulfillment stage.
- `accounts` and `admin` are cross-cutting functions and must not be used as fulfillment stage values.

Protocol steps:
1. Classify each governed fulfillment artifact/run with exactly one fulfillment stage from the required taxonomy.
2. Validate stage sequence and prohibit skipping: `onboarding -> opening -> maintenance -> pending_close -> closed`.
3. For entry to `onboarding`, verify Gate 1 evidence exists (consult scheduled, client intent to proceed); enforce matter status = `pending`.
4. For transition to `opening`, verify Gate 2 evidence exists (engagement agreement signed); confirm matter status transitions to `open`.
5. For transition to `maintenance`, verify Gate 3 evidence exists (opening controls complete and internally approved).
6. For transition to `pending_close`, verify Gate 4 evidence exists (substantive work complete); matter status returns to `pending`.
7. For transition to `closed`, verify Gate 5 evidence exists (ML1 explicit close authorization); set `close_reason` (`completed` / `declined` / `terminated`); matter status transitions to `closed`.
8. Execute handoff controls:
   - Marketing `conversion` handoff enters fulfillment as `onboarding`.
   - Post-`closed` records are routed to archive handling under governing doctrine.

Block condition:
- Stage value not in required fulfillment taxonomy.
- More than one fulfillment stage assigned to the same governed artifact/run.
- Stage skip or out-of-order transition.
- `onboarding` asserted without Gate 1 evidence.
- Matter status is `open` before engagement agreement signature.
- `opening` asserted without Gate 2 evidence and status transition proof.
- `maintenance` asserted without Gate 3 completion evidence.
- `pending_close` asserted without Gate 4 completion evidence.
- `closed` asserted without Gate 5 ML1 authorization and `close_reason`.
- `accounts` or `admin` used as stage values rather than cross-cutting functions.

Escalation path:
- Escalate ambiguous stage assignment, missing gate evidence, status-transition conflict, or handoff conflict to ML1.

Logging requirement:
- Record stage classification, normalization behavior, gate evidence references, matter status checks, transition decision, handoff target, `close_reason` (if applicable), and any block/escalation event in run artifacts.

Version: 0.3
Status: Draft
