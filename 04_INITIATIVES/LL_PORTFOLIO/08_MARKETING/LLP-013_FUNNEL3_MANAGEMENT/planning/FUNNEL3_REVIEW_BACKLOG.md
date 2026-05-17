---
id: llp-013_funnel3_management__review_backlog
title: Funnel 3 Review Backlog
owner: ML1
status: draft
created_date: 2026-04-03
last_updated: 2026-05-17
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

### 1. Add a Mandatory Specialist Regime-Screen Gate
- Problem: Funnel 3 targets stablecoin, tokenized-payment, custody, and PSP fact patterns, but specialist review is still optional and invoked ad hoc by ML1.
- Why it matters: overlapping securities, money-services, and payment-services issues can currently move through content or consult-routing without a required doctrinal screen.
- Initial action direction: define a mandatory triage rule for tokenized-payment, stablecoin, custody, marketplace, safeguarding, or hybrid MSB/RPAA fact patterns before outward routing or consult booking.
- Key refs:
  - `04_FUNNELS/funnel-03/FUNNEL_SPEC.md`
  - `planning/COMMUNICATION_PLAN.md`
  - `planning/DEPENDENCIES.md`

### 2. Define a Canonical PSP/RPAA Front-Door Offer
- Problem: planning says RPAA applicability is a primary entry question, but the canonical entry-offer map remains MSB/AML-shaped and only surfaces RPAA at the core-offer layer.
- Why it matters: Funnel 3 currently claims a PSP/payment-services lane without a matching front-door product.
- Initial action direction: define a canonical RPAA/PSP entry offer or rework the entry-offer map so payment-services applicability is visible at intake.
- Key refs:
  - `planning/SCOPE_STATEMENT.md`
  - `04_FUNNELS/funnel-03/FUNNEL_SPEC.md`
  - `04_FUNNELS/funnel-03/entry_offers.md`

### 3. Expand the Intake Schema to Capture Regime-Separating Facts
- Problem: the current funnel data model captures marketing metadata, but not the legal facts needed to separate securities, MSB, PSP, and hybrid files.
- Why it matters: safe routing currently depends too much on ad hoc judgment.
- Initial action direction: add intake fields for issuance/distribution, custody/safeguarding, payment-function model, reporting-entity status, end-user funds handling, marketplace matching, and key jurisdictional hooks.
- Key refs:
  - `04_FUNNELS/funnel-03/FUNNEL_SPEC.md`
  - `04_FUNNELS/funnel-03/entry_offers.md`

### 4. Re-scope EO2 Around Actual STR Obligations
- Problem: EO2 is currently pitched to generic `MSBs / PSPs`, even though the work product is STR threshold assessment, drafting, and filing support.
- Why it matters: RPAA-only or payment-function leads can be misrouted into an AML-reporting offer, and the packet does not yet make the client’s own prompt filing obligation explicit.
- Initial action direction: narrow EO2 to reporting-entity scenarios with live STR obligations and add explicit timing / client-responsibility safeguards.
- Key refs:
  - `04_FUNNELS/funnel-03/entry_offers.md`

### 5. Route Securities-Overlap Issues Out of EO1
- Problem: EO1 is aimed at crypto-enabled operators but does not clearly route out securities, marketplace, custody, or exempt-distribution issues.
- Why it matters: the MSB offer can read like a sufficient perimeter analysis for models that actually require separate securities screening.
- Initial action direction: add explicit exclusions / escalation language for securities-overlap fact patterns.
- Key refs:
  - `04_FUNNELS/funnel-03/entry_offers.md`
  - `00_SYSTEM/AGENTS/specs/marketing/MKT_MUGGAH_SECURITIES_AGENT.md`

### 6. Resolve F03 Top-of-Funnel Training Content vs. Paid Lead-Magnet Architecture
- Problem: the current F03 packet contains a `$97` paid lead-magnet / tripwire pricing scaffold, but the ICP and authority-building logic may point instead to executive-grade training or orientation content as the more realistic first-step asset.
- Why it matters: if the first paid asset is mismatched to actual buyer behavior, the funnel can overprice cold authority content, misread `lead magnet` metrics, and confuse training/orientation assets with true consult-intent signals.
- Initial action direction: decide whether the realistic first-step F03 asset is:
  1. free authority content plus paid consult,
  2. a paid orientation / training resource,
  3. a premium report / tripwire,
  or 4. a segmented combination by trigger type.
- Additional design question: if training is used, determine whether it should be framed as compliance training, executive orientation, effectiveness-readiness briefing, or a post-registration / post-consult add-on rather than a universal cold-acquisition asset.
- Key refs:
  - `LLP-013_FUNNEL3_MANAGEMENT/implementation/STRIPE_PRODUCTS.md`
  - `04_FUNNELS/funnel-03/funnel3_entryoffer2_leadmagnet_v3.md`
  - `04_FUNNELS/funnel-03/funnel3_entryoffer3_leadmagnet_v1.md`
  - `04_FUNNELS/funnel-03/funnel_02_payments_msb_psp/README.md`

### 7. Backlog Tokenized Payment Systems Regulatory Structuring
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
