---
id: llp_012_funnel2_management__planning__project_plan_md
title: LLP-012 Funnel 2 - Project Plan
owner: ML1
status: draft
created_date: 2026-04-07
last_updated: 2026-05-10
tags: [llp-012, funnel-02, planning, project-plan]
---

# Project Plan

Project ID: LLP-012
Project Path: 08_MARKETING/LLP-012_FUNNEL2_MANAGEMENT
Stage: Planning

## Planning Objective

Normalize Funnel 02 into a coherent governed packet that supports the already
authorized execution surface: a paid Corporate Health Check for mature Ontario
operators in approved strategic industry lanes, distributed primarily through
referrals and screened for fit before ML1 time is committed.

## Current Planning Focus

1. preserve the referral-first acquisition path, with priority on fintech-
   adjacent, trade-impacted, and Rousseau Mazzuca-referable construction
   operators
2. preserve the entry offer as a defined paid diagnostic rather than a premium
   consult variant
3. freeze the mandatory human qualification call and evidence schema as the
   required gate before ML1 time is committed
4. align website, GHL, pricing, and downstream retainer logic to one adopted
   pricing model
5. record the baseline-lock rule so F02 thresholds stop drifting as the packet
   evolves

## Approved Industry Lanes

F02 Health Check targeting is narrowed to:

- fintech-adjacent operators, including fintech, payments, MSB, PSP, embedded
  finance, and platform businesses with regulated payment flows;
- trade-impacted operators, including lumber, steel, plastics, import/export-
  exposed manufacturers, distributors, and supply-chain businesses;
- construction and construction-adjacent mid-market operators, especially where
  a Health Check may surface lien, holdback, payment, subcontracting, or project
  dispute issues referable to Rousseau Mazzuca.

## Planning Workstreams

| Workstream | Objective | Primary Output |
| --- | --- | --- |
| WS-01 Channel and ICP lock | Freeze the primary acquisition path and the operator profile F02 is designed to attract | `ASSUMPTIONS_CONSTRAINTS.md`, `DEPENDENCIES.md` |
| WS-02 Entry-offer definition | Freeze Health Check scope, pricing posture, delivery expectations, and handoff logic | this file, `SCOPE_STATEMENT.md`, implementation pricing notes |
| WS-03 Intake and qualification control | Define the mandatory qualification call, minimum fit fields, and non-bypass gate logic | `ASSUMPTIONS_CONSTRAINTS.md`, `RISK_REGISTER.md`, `COMMUNICATION_PLAN.md` |
| WS-04 Surface activation alignment | Align website page, intake form, content, and referral surfaces to one F02 path | `DEPENDENCIES.md`, `RISK_REGISTER.md` |
| WS-05 Measurement and control normalization | Make the active metrics, escalation triggers, and packet-review cadence explicit | `METRICS.md`, `COMMUNICATION_PLAN.md` |
| WS-06 Packet normalization | Bring the planning packet into canonical shape so portfolio governance reflects the real project state | full `planning/` packet and `initiation/APPROVAL_RECORD.md` |

## Planning Sequence

1. confirm acquisition path and ICP boundary
2. confirm entry-offer scope and pricing posture
3. freeze qualification-call and evidence requirements
4. align website, GHL, and referral surfaces to the same path
5. lock metrics and escalation rules
6. record the normalized packet state for future portfolio reviews

## Adopted Operating Decisions

### Mandatory Qualification-Call Schema

F02 does not treat an inquiry as `intake_completed` until a human
qualification call has occurred and the resulting evidence record is complete.

#### Pre-Call Hard Filters

The existing pre-booking gate remains in force:

- annual cash flow below `CAD 5M` is disqualifying for the Health Check service
  path unless ML1 grants an exception; route toward information products where
  possible
- fewer than `5` employees is disqualifying
- no accountant relationship is disqualifying

#### Required Call Outputs

Every completed qualification call must record all fields below:

- lead source
- industry lane
- referring accountant or referral source, if any
- buyer role
- buyer authority level
- annual revenue band
- annual cash-flow band
- employee band
- accountant relationship confirmed (`yes` / `no`)
- maturity trigger
- practice-area fit
- Rousseau Mazzuca referral potential, if construction/lien-risk facts are present
- projected remediation value band
- willingness to pay for a Health Check tier
- timeframe / urgency
- document readiness
- disposition
- disqualification reason, if not qualified
- recommended next path

#### Canonical Dispositions

Disposition values must align with LLP-014 intake governance:

- `qualified`
- `declined`
- `no_response`
- `deferred`
- `out_of_scope`

#### Recommended Next Path Values

- `f02_v1`
- `f02_v2`
- `f02_v3`
- `reroute_f01`
- `reroute_f03`
- `reroute_info_product`
- `decline_no_offer`

#### Information Product Routing

Where the recommended next path is `reroute_info_product`, the default product
map is:

| Product | Lane | Use |
|---|---|---|
| Corporate Starter Kit | General below-threshold operators | General corporate, contracts, governance, NDA, contractor, invoice, or payment-terms needs |
| Corporate Assessment | Cross-F02 | Screening and routing before ML1 attention is committed |
| Fintech White Paper | Fintech-adjacent | Education on payments, MSB, RPAA, AML, and banking-partner readiness; high-fit leads route to F03 |
| Trade-Impacted Contract Risk Kit | Lumber, steel, plastics, manufacturing, distribution | Tariff and supply-chain contract risk education |
| Construction Payment / Lien Triage Kit | Construction / Rousseau Mazzuca referral lane | Holdback, payment dispute, lien-deadline, and referral issue-spotting |
| Subcontractor Contract Risk Pack | Construction operators | Scope, extras, delay, payment, backcharges, and lien-preservation issue-spotting |

### Pricing Posture

The packet adopts the business-plan pricing model as the live F02 pricing
baseline.

#### Corporate Health Check Pricing

- `V1 Entry Level` = `CAD 2,000`
- `V2 Growth Health Check` = `CAD 3,500`
- `V3 Pre-Event Health Check` = `CAD 6,000`

Accountant-referral traffic should default to `V1` unless qualification-call
evidence supports escalation to `V2` or `V3`.

#### Downstream Fractional Counsel Pricing

- `V1 Foundations` = `CAD 1,500/month`
- `V2 Active` = `CAD 2,750/month`
- `V3 Growth` = `CAD 4,500/month`

Immediate post-Health-Check conversion should prefer remediation work first.
Fractional counsel remains a downstream relationship offer after trust is
established through findings and follow-on work.

### Threshold Lock Rule

F02 thresholds remain provisional until a clean live baseline exists.

The threshold-lock review opens only after all conditions below are true:

- the qualification-call schema above is deployed without bypass
- one canonical Health Check price ladder is live
- one canonical payment / routing path is live
- no material pricing, routing, or qualification-schema change occurs during
  the measurement window

Thresholds lock at the later of:

- `60` days of clean live operation, or
- `8` completed paid Health Checks

The window must also include at least `2` downstream conversions into
remediation or recurring counsel before ML1 finalizes locked F02 thresholds.

## Milestones

| Milestone | Target Date | Status | Evidence |
| --- | --- | --- | --- |
| Initiating to Planning approved | 2026-03-16 | complete | `initiation/APPROVAL_RECORD.md` |
| Planning to Executing confirmed by ML1 | 2026-04-01 | complete | `initiation/APPROVAL_RECORD.md` |
| Canonical planning packet normalized | 2026-04-07 | complete | full `planning/` packet present |
| Qualification-call schema frozen | 2026-04-07 | complete | adopted operating decision in this file |
| Offer and pricing re-review complete | 2026-04-07 | complete | this file + updated implementation pricing doc |
| Next ML1 operating review prepared | TBD | pending | updated `implementation/` logs and governed metrics |

## Resource Plan

### Human / Decision Roles

| Role | Responsibility |
| --- | --- |
| ML1 | sole authority for scope, pricing, channel sequencing, ICP boundary, and stage advancement |
| ML2 | packet normalization, artifact maintenance, and governance synchronization |
| website / funnel implementation support | prepare and maintain F02 landing-page and intake configuration artifacts |
| GHL operations support | implement non-bypass intake and qualification controls once ML1 approves changes |

### Source Inputs

- `README.md`
- `initiation/APPROVAL_RECORD.md`
- `planning/SCOPE_STATEMENT.md`
- existing Stage 2 planning research notes
- `implementation/ACQUISITION_THESIS.md`
- `implementation/FRACTIONAL_COUNSEL_PRICING.md`

## Completion Condition

Planning is complete when the F02 packet can answer, without contradiction:

- who F02 is for
- how those operators are reached
- what must happen before ML1 time is allocated
- what the buyer receives and what they pay for
- how F02 hands qualified work into downstream fulfillment or retainer paths
- what metric, risk, and escalation controls govern live operation
- when provisional thresholds become locked thresholds
