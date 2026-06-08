---
id: 04_initiatives__ll_portfolio__08_marketing__funnels__funnel_02__funnel_spec_md
title: Funnel Spec — Funnel 02
owner: ML1
status: planned
created_date: 2026-02-25
last_updated: 2026-06-07
tags: []
---

# Funnel Spec — Funnel 02

## Funnel ID + Status

- funnel_id: funnel-02
- status: planned

## Purpose / Role

Corporate-law acquisition path for growing businesses with at least `CAD 5M`
annual cash flow, unless ML1 grants an exception, using a preventative paid
diagnostic as the entry point.

## Funnel Distinction

Funnel 02 captures corporate-law demand at the trigger moment — when an
operator is already searching because something has happened or is imminent.
Ambient awareness-building is not the model: corporate legal needs at this ICP
stage are episodic, not ambient. The content cluster catches operators at the
moment of urgency; the checklist converts them.

## Positioning Reference

- 00_POSITIONING/MARKET_POSITIONING.md
- ICP-01: Ontario Operating Company
- Category: Fractional Counsel / Legal Function as a Service (preventative entry)
- Competitive framing: `COMPETITIVE_DIFFERENTIATION_MATRIX.md`
- Proof architecture: `PROOF_ARCHITECTURE.md`

## Target ICP (Must Match Positioning)

- Ontario-based operating businesses
- at least `CAD 5M` annual cash flow unless ML1 grants an exception
- 5-30 employees
- 2+ years in operation
- Accountant involved
- Document-ready
- Not in active crisis

### Working Corporation Taxonomy (ML1-approved 2026-06-07)

Near-exhaustive taxonomy of Ontario private operating businesses in the ICP
revenue band. Classification notes: VC-backed companies are digital by
definition and fall under Type 1. PE-backed companies are non-family-controlled
and fall under Type 3.

| Type | Description |
|---|---|
| 1. Start-up (digital) | Digital business model; typically founder-led; includes VC-backed; IP, equity, and founder agreement surface prominent |
| 2. Family-owned company | Controlled by a single family; succession, family governance, and shareholder alignment surface prominent |
| 3. Private company (non-digital, non-family) | Operating business not in a digital sector and not family-controlled; includes PE-backed; classic corporate governance, commercial contracts, and growth financing surface |
| 4. Foreign subsidiary in Canada | Canadian entity owned by a foreign parent; local governance compliance, intercompany agreements, and Canadian regulatory surface |
| 5. Professional corporation | Regulated professional practice (accounting, consulting, or similar); ownership and transfer constrained by professional body rules; distinct governance surface |

The 25-point checklist lead magnet applies across all five types at the pillar
level. Individual items within pillars may weight differently by type — to be
assessed when the checklist is produced.

Secondary planning hypothesis (research only):
- operators acquiring an existing operating business (independent or backed), pending cohort-comparison findings and ML1 approval.

## Entry Channel(s)

- Content / SEO (primary — see Traffic / Acquisition)
- Google Ads
- `levine-law.ca`
- Overlapping NDA Esq landing-page acquisition surface on `levine-law.ca`
- **Type 4 channel (under development)** — see below

## Type 4 Channel: Foreign-Owned and Controlled Subsidiaries

Status: identified as a focus channel 2026-06-07. Development pending.

### Why Type 4 is a distinct channel

Foreign subsidiaries arriving in Canada do not find their corporate lawyer
through content or Google search the same way a Canadian-founded company does.
The foreign parent typically has its own legal relationships; the Canadian
entity needs a local corporate lawyer but lacks an established referral network
in Canada. This creates a specific acquisition dynamic: the entry point is
referral and relationship, not search.

### Decision-maker profile

The buying decision typically involves the Canadian country manager or GM
(day-to-day contact and felt need), with approval or direction from the foreign
parent's GC, CFO, or outside counsel. The Canadian entity often cannot
self-select a lawyer without parent involvement.

### Trigger moments

- Initial Canadian subsidiary setup (incorporation, governance, first
  commercial contracts)
- Compliance review required by the parent or a regulator
- Employment issues with Canadian staff (distinct from home-country norms)
- Key commercial contract with a Canadian customer or supplier
- Intercompany agreement restructuring
- M&A involving the Canadian entity

### Likely referral and entry sources

- International accounting firms with Canadian practices (Big 4 and mid-tier)
- Trade commissioners and consulates (foreign governments with Canadian trade
  presence)
- Canadian chambers of commerce with international member bases
- International law firms referring Canadian work
- Canadian banks with foreign corporate banking relationships

### Channel development questions (open)

- Which source country segments are addressable and worth targeting?
- Does this channel require dedicated content or landing page
  (e.g., "Canadian subsidiary legal counsel") or does the existing
  `levine-law.ca` surface adequately capture inbound?
- What is the referral relationship investment required (trade commissions,
  international accounting contacts) and is that realistic at current capacity?

## Traffic / Acquisition

- Authority content / SEO is the primary acquisition lane. The blog and
  content cluster serve the awareness function by being findable at trigger
  moments — not by creating ambient demand. There is no standalone awareness
  lead magnet. "Growth Without Structural Drift" is retired as a lead magnet
  concept. If retained at all, it is top-of-funnel brand content only, not a
  conversion asset.
- Sole lead magnet: the Corporate Health Check checklist (conversion asset).
  Spec: `funnel2_leadmagnet_checklist_spec_v1.md`.
- Higher-quality, higher-cost Google Ads traffic is allowed where it improves
  fit and downstream economics.
- NDA Esq may act as a supplementary traffic and lead source for Funnel 02
  where the acquisition surface overlaps, without changing project boundaries.
- Advisor referrals (accountants, financial advisors) are a referral channel,
  not a content distribution channel. The advisor play is relationship-based;
  no circulating asset is planned.

## Intake Mechanism

- Go High Level (GHL) form
- Voice AI
- SMS follow-up
- SDR qualification call (mandatory for `intake_completed`)
- setter-supported qualification and scheduling

## Qualification Gates

- annual_cash_flow_min: CAD 5M unless ML1 exception applies
- employee_min: 5
- years_in_operation_min: 2
- ontario_incorporation_required: true
- active_operating_business_required: true
- accountant_involved_required: true
- pre_conversion_minimum_readiness_required: true
- post_purchase_document_package_required: true
- qualification_call_evidence_required: true

Required documents:
- articles and bylaws
- shareholder agreement
- director and officer registers
- key commercial contracts
- employment and contractor agreements
- option or equity documents
- minute book (if maintained)
- recent financing documents

## Core Narrative / Promise

Structured corporate-law and governance assessment for operating companies that
have outgrown their original setup.

## F02 / F03 Routing Rule

- Fintech corporate, contracts, governance, financing-readiness, and general
  commercial legal issues route to Funnel 02 where the F02 cash-flow and
  qualification gates are met.
- MSB, RPAA, AML, STR, payments-infrastructure, stablecoin settlement, PSP, and
  payments-regulatory classification issues route to Funnel 03.

## Conversion Event Definition

- health_check_purchased

## Pipeline Stages

ML1-approved 2026-06-07. Single pipeline. Canonical spec governs `pipeline.yaml`.

- new_lead
- worked
- qualified
- consult_booked
- consult_completed
- engagement_out
- retained
- closed_lost

`worked` = first outreach attempt (call placed, no answer counts). Stage/status
separation enforced: no-show, rescheduled, and unresponsive are opportunity
status fields, not stages. See `pipeline.yaml` for custom fields and automation
definitions.

## Diagnostic Offer Routing

The Corporate Health Check (paid diagnostic) is not offered to all leads
universally. Two lead types enter this funnel with different routing:

**Awareness leads** (source: health check content cluster — blog posts, pillar
pages): low problem clarity, arrived in learning mode, not carrying a defined
mandate. These leads are routed automatically to the diagnostic purchase page
directly from the inquiry form. No SDR judgment required at this step.

**Mandate leads** (source: referral, direct, event, networking): high problem
clarity, specific legal problem in hand. These leads are routed to a
consultation to scope and price the work. The diagnostic may still be offered
by the SDR at Qualified if structural complexity is identified, but it is not
the default.

Routing decision point: at the Qualified stage, the SDR sets `Offer Path` =
Diagnostic or Consultation based on lead type. Inbound content leads may be
pre-routed to Diagnostic via form logic before reaching the SDR.

## Lead Magnet

One lead magnet. Sole conversion asset for this funnel.

**Corporate Health Check Checklist** — a 25-point scorecard organized across
the five health check pillars. Operator confronts their gaps line by line;
"Not sure" answers surface the liability; the gap bridges to the health check
purchase. Accessible directly from blog posts and the pillar page. Gate
mechanic (Option A vs B) pending ML1 decision.

Full spec: `funnel2_leadmagnet_checklist_spec_v1.md`

## Primary Metrics

- paid_health_check_conversion_rate
- remediation_project_conversion_rate
- retainer_conversion_rate
- lead_response_time
- scheduled_consult_rate
- intake_reporting_completeness

## KPI Targets (Must Map to Goals)

- Goals reference: 02_GOALS/KPI_DEVELOPMENT_PROJECT/GOALS_2026.md
- KPI targets: TBD

## Objective Mapping (Reference OBJECTIVES.md Items)

- OBJ-01
- OBJ-02

## Offer Mapping (Strategy/Solution Supported)

- Strategy: Corporate Health Check -> Remediation -> Fractional Counsel
- Strategy folder: 02_PLAYBOOKS/CORPORATE/STRATEGIES/CORPORATE_HEALTH_CHECK_REMEDIATION/
- Entry offer: Corporate Health Check (paid diagnostic)
- Core offer: Remediation + Fractional Counsel
- Scope note: the Corporate Health Check may include bounded regulatory review where the client's business model or industry exposure requires it
- Solutions: Corporate solution frames as indicated by remediation scope (TBD)

## Compliance Constraints / Disclaimers

- Do not launch until Positioning, Objectives, and Goals are formalized
- Marketing only; no legal advice or acceptance decisions
- ML1 approval required for acceptance

## Owner + Review Cadence

- Owner: ML1
- Review cadence: TBD
