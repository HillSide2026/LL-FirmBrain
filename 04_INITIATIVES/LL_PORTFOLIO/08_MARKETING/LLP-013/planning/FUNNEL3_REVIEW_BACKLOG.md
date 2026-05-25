---
id: llp-013_funnel3_management__review_backlog
title: Funnel 3 Review Backlog
owner: ML1
status: draft
created_date: 2026-04-03
last_updated: 2026-05-19
tags: [marketing, funnel-03, backlog, review]
---

# Funnel 3 Review Backlog

## Purpose
Capture unresolved higher-severity findings from the April 3, 2026 three-Muggah review of Funnel 3 so they can be addressed deliberately in planning rather than patched piecemeal.

## Source Review
- `MKT_MUGGAH_SECURITIES_AGENT`
- `MKT_MUGGAH_MONEY_SERVICES_AGENT`
- `MKT_MUGGAH_PAYMENT_SERVICES_AGENT`

## High-Priority Backlog Items

### 1. RPAA Lead Magnet

- Problem: Funnel 3 has no free lead magnet specifically targeting the RPAA/PSP
  audience. Current lead magnets are MSB/AML-shaped. RPAA-regulated payment
  service providers (PSPs) face a distinct and complex applicability question
  that is not well-served by MSB registration content.
- Why it matters: RPAA applicability is a primary front-door question for PSPs
  entering Canada or expanding their payment activities. A dedicated RPAA lead
  magnet creates a direct acquisition asset for this segment and supports the
  canonical PSP/RPAA entry offer that Funnel 3 currently lacks.
- Initial action direction: design a free RPAA applicability guide or checklist
  targeted at PSPs and payment operators. Candidate angles: "Do You Need to
  Register Under the RPAA?" or "RPAA Applicability Checklist for Payment
  Service Providers." Seek ML1 approval before production.
- Added: 2026-05-19
- Key refs:
  - `04_FUNNELS/funnel-03/entry_offers.md`
  - `planning/SCOPE_STATEMENT.md`
  - `02_PLAYBOOKS/FINANCIAL_SERVICES/MARKET_STRUCTURE_FRAMEWORK.md`

### 2. CARF Lead Magnet

- Problem: Funnel 3 has no lead magnet targeting the CARF (Crypto-Asset
  Reporting Framework) audience. CARF creates reporting obligations for
  crypto-asset service providers (CASPs). This is an underserved front-door
  entry point for the fintech boutique positioning.
- Why it matters: CARF is a live and growing compliance surface for CASPs,
  stablecoin operators, and institutional crypto infrastructure providers.
  fintechlawyer.ca Cluster P8 (Stablecoin Regulatory Framework) positions LL
  as the right counsel for exactly this audience. A CARF lead magnet converts
  that positioning into a tangible acquisition asset.
- Initial action direction: design a free CARF orientation guide targeted at
  CASPs operating in or entering Canada. Candidate angles: "CARF Compliance
  for Canadian Crypto-Asset Service Providers" or "Is Your Business a CARF
  Reporting Entity?" Seek ML1 approval before production.
- Added: 2026-05-19
- Key refs:
  - `04_FUNNELS/funnel-03/entry_offers.md`
  - `04_INITIATIVES/LL_PORTFOLIO/07_GROWTH_PROJECTS/LLP-039/planning/RETAINER_PROSPECT_PIPELINE.md`
  - `04_INITIATIVES/LL_PORTFOLIO/08_MARKETING/FINTECHLAWYER_CONTENT_PLAN.md`

### 3. Research and Evaluate Industry Organization Partnership

- Problem: Funnel 3 lacks a structured presence in the Canadian fintech and
  payments ecosystem beyond content and referral channels. Industry organization
  membership or partnership is an untested authority-building and deal-flow
  channel for the payments/MSB/PSP/CARF audience.
- Why it matters: the Funnel 3 ICP (fintech operators, cross-border PSPs, crypto
  infrastructure businesses) clusters around industry bodies. Association
  membership creates speaking opportunities, committee access, peer referrals,
  and direct positioning with the target segment.
- Current lead candidate: Canada Blockchain Consortium (CBC). Evaluate fit for
  the regulatory counsel / boutique positioning given CBC's focus on blockchain
  and digital asset policy in Canada.
- Other contenders to research:
  - Digital Finance Institute (DFI) — **Do not pursue.** DFI appears to be a
    failed business development initiative by Christine Duhaime, a competitor
    in the tier 5 fintech/payments boutique space. Not a neutral or credible
    partnership vehicle. ML1-noted 2026-05-19.
  - Blockchain Association of Canada (BAC) — Vancouver-based; very early stage.
    Limited value as a partnership target at this time. Monitor but do not
    prioritize. ML1-noted 2026-05-19.
  - Toronto Israeli Tech (torontoisraelitech.com) — community connecting Israeli
    tech companies and entrepreneurs with the Toronto/Canadian market. Strong
    potential ICP overlap: Israeli fintech and payments operators entering Canada
    face MSB registration, RPAA, FINTRAC, and banking-relationship questions that
    are exactly LL's core offer. Explore membership, speaking, or referral
    partnership. ML1-flagged 2026-05-19.
  - Payments Canada — the payments infrastructure body; relevant for RPAA and
    PSP positioning; membership may signal institutional credibility
  - Toronto Finance International (TFI) — Toronto as global financial centre;
    relevant for institutional / cross-border mandate positioning
  - Canada FinTech Forum — annual conference + community; strong deal-flow signal
    for the MSB / payments segment
  - BetaKit — Canadian tech and startup media; editorial and event presence;
    relevant for visibility with the founder and operator segment that feeds
    Funnel 3; explore sponsored content, contributor, or event partnership angles
- Initial action direction: assess each organization on: (1) ICP overlap with
  Funnel 3 target; (2) cost of membership / participation; (3) speaking or
  committee access; (4) referral or deal-flow track record; (5) conflict or
  exclusivity constraints. Bring shortlist to ML1 for decision on pursuit.
- Added: 2026-05-19

### 4. Add a Mandatory Specialist Regime-Screen Gate
- Problem: Funnel 3 targets stablecoin, tokenized-payment, custody, and PSP fact patterns, but specialist review is still optional and invoked ad hoc by ML1.
- Why it matters: overlapping securities, money-services, and payment-services issues can currently move through content or consult-routing without a required doctrinal screen.
- Initial action direction: define a mandatory triage rule for tokenized-payment, stablecoin, custody, marketplace, safeguarding, or hybrid MSB/RPAA fact patterns before outward routing or consult booking.
- Key refs:
  - `04_FUNNELS/funnel-03/FUNNEL_SPEC.md`
  - `planning/COMMUNICATION_PLAN.md`
  - `planning/DEPENDENCIES.md`

### 5. Define a Canonical PSP/RPAA Front-Door Offer
- Problem: planning says RPAA applicability is a primary entry question, but the canonical entry-offer map remains MSB/AML-shaped and only surfaces RPAA at the core-offer layer.
- Why it matters: Funnel 3 currently claims a PSP/payment-services lane without a matching front-door product.
- Initial action direction: define a canonical RPAA/PSP entry offer or rework the entry-offer map so payment-services applicability is visible at intake.
- Key refs:
  - `planning/SCOPE_STATEMENT.md`
  - `04_FUNNELS/funnel-03/FUNNEL_SPEC.md`
  - `04_FUNNELS/funnel-03/entry_offers.md`

### 6. Expand the Intake Schema to Capture Regime-Separating Facts
- Problem: the current funnel data model captures marketing metadata, but not the legal facts needed to separate securities, MSB, PSP, and hybrid files.
- Why it matters: safe routing currently depends too much on ad hoc judgment.
- Initial action direction: add intake fields for issuance/distribution, custody/safeguarding, payment-function model, reporting-entity status, end-user funds handling, marketplace matching, and key jurisdictional hooks.
- Key refs:
  - `04_FUNNELS/funnel-03/FUNNEL_SPEC.md`
  - `04_FUNNELS/funnel-03/entry_offers.md`

### 7. Re-scope EO2 Around Actual STR Obligations
- Problem: EO2 is currently pitched to generic `MSBs / PSPs`, even though the work product is STR threshold assessment, drafting, and filing support.
- Why it matters: RPAA-only or payment-function leads can be misrouted into an AML-reporting offer, and the packet does not yet make the client’s own prompt filing obligation explicit.
- Initial action direction: narrow EO2 to reporting-entity scenarios with live STR obligations and add explicit timing / client-responsibility safeguards.
- Key refs:
  - `04_FUNNELS/funnel-03/entry_offers.md`

### 8. Route Securities-Overlap Issues Out of EO1
- Problem: EO1 is aimed at crypto-enabled operators but does not clearly route out securities, marketplace, custody, or exempt-distribution issues.
- Why it matters: the MSB offer can read like a sufficient perimeter analysis for models that actually require separate securities screening.
- Initial action direction: add explicit exclusions / escalation language for securities-overlap fact patterns.
- Key refs:
  - `04_FUNNELS/funnel-03/entry_offers.md`
  - `00_SYSTEM/AGENTS/specs/marketing/MKT_MUGGAH_SECURITIES_AGENT.md`

### 9. Resolve F03 Top-of-Funnel Training Content vs. Paid Lead-Magnet Architecture
- Problem: the current F03 packet contains a `$97` paid lead-magnet / tripwire pricing scaffold, but the ICP and authority-building logic may point instead to executive-grade training or orientation content as the more realistic first-step asset.
- Why it matters: if the first paid asset is mismatched to actual buyer behavior, the funnel can overprice cold authority content, misread `lead magnet` metrics, and confuse training/orientation assets with true consult-intent signals.
- Initial action direction: decide whether the realistic first-step F03 asset is:
  1. free authority content plus paid consult,
  2. a paid orientation / training resource,
  3. a premium report / tripwire,
  or 4. a segmented combination by trigger type.
- Additional design question: if training is used, determine whether it should be framed as compliance training, executive orientation, effectiveness-readiness briefing, or a post-registration / post-consult add-on rather than a universal cold-acquisition asset.
- Key refs:
  - `LLP-013/implementation/STRIPE_PRODUCTS.md`
  - `04_FUNNELS/funnel-03/funnel3_entryoffer2_leadmagnet_v3.md`
  - `04_FUNNELS/funnel-03/funnel3_entryoffer3_leadmagnet_v1.md`
  - `04_FUNNELS/funnel-03/funnel_02_payments_msb_psp/README.md`

### 10. Backlog Tokenized Payment Systems Regulatory Structuring
- Problem: tokenized payment systems are strategically interesting but are not
  approved as an active F03 entry offer.
- Why it matters: the topic creates securities, MSB, RPAA, custody,
  safeguarding, and banking-relationship overlap; marketing it prematurely
  could overstate the current approved offer perimeter.
- Current decision: keep Tokenized Payment Systems Regulatory Structuring in
  backlog as a candidate offer only.
- Activation condition: define scope at the practice layer, including
  securities-boundary exclusions and mandatory specialist screening, then seek
  ML1 approval before any marketing activation.
- Key refs:
  - `04_FUNNELS/funnel-03/FUNNEL_SPEC.md`
  - `04_FUNNELS/funnel-03/funnel.yaml`
  - `04_FUNNELS/funnel-03/content/blog/eo4_content_plan.md`
