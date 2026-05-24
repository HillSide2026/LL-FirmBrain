---
id: PRO-015
title: Marketing Stage Classification and Handoff
owner: ML1
status: approved
approved_by: ML1
approved_date: 2026-04-18
version: 0.2
effective_date: 2026-04-18
supersedes:
provenance:
  decided_by: ML1
  decided_on: 2026-04-18
  context: Metadata normalized by system admin cleanup on 2026-05-24
created_date: 2026-03-08
last_updated: 2026-03-09
tags: [protocol, marketing, lifecycle, handoff]
---

# PRO-015 — Marketing Stage Classification and Handoff

Enforces Policies: POL-032, POL-033

Trigger condition:
- A marketing run, campaign, asset, or report is created, updated, or promoted.
- A stage transition is requested.

Required stage taxonomy:
- `discovery`
- `interest`
- `consideration`
- `inquiry` (alias: `intake`)
- `conversion` (marketing term)

Terminology rule:
- `conversion` is the marketing-stage label.
- `onboarding` is the fulfillment-stage label for the handoff event.

Protocol steps:
1. Classify each governed marketing artifact/run with exactly one lifecycle stage from the required taxonomy.
2. Normalize aliases (`intake -> inquiry`) in canonical structured fields for marketing artifacts.
3. If `onboarding` appears in a marketing artifact, treat it as a legacy/non-canonical label, normalize to `conversion`, and record a terminology warning in the run artifact.
4. If stage is `conversion`, validate objective evidence exists (`engagement agreement signed`, `retainer received`, or `invoice paid`) and attach evidence reference(s).
5. If conversion evidence is valid, mark marketing lifecycle as complete and initiate handoff into fulfillment as `onboarding`.
6. Route post-conversion artifacts to non-marketing classes (`client_service`, `delivery`, `retention`, `expansion`) under their governing doctrine.

Block condition:
- Stage value not in required taxonomy.
- `onboarding` persisted as canonical marketing-stage value after normalization.
- Conversion asserted without required evidence.
- Post-conversion artifact retained in marketing stage classification.

Escalation path:
- Escalate ambiguous stage assignment, missing evidence, or handoff conflicts to ML1.

Logging requirement:
- Record stage classification, normalized alias handling, evidence references, transition decision, and handoff target in run artifacts.

Version: 0.2
Status: Draft
