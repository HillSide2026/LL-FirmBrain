---
id: 04_initiatives__hillside_portfolio__matthew_holdings__2c_ontario_msb_corp_1001494374_ontario_corp__project_locarno_direct_bank_sponsorship_strategy_md
title: Project Locarno - Direct Bank Sponsorship Build Strategy
owner: ML1
status: draft
created_date: 2026-05-11
last_updated: 2026-05-11
tags: [locarno, ontario-msb, direct-bank-sponsorship, emi, rpaa, payments-infrastructure, sale-value]
---

# Project Locarno - Direct Bank Sponsorship Build Strategy

## Entity and Tag

Project Locarno relates to `1001494374 Ontario Corp`.

Locarno is an internal project tag. It has no operational, legal, branding, or
customer-facing significance.

## Strategic Objective

Build a clean, bankable payments platform that can later be sold as a
regulated infrastructure asset.

The core value proposition is not software alone.

Enterprise value comes from owning:

- a live regulatory perimeter;
- a direct EMI relationship;
- a direct sponsor-bank relationship; and
- a documented, audit-ready operating model.

The revised target state is an MSB and RPAA-active operating entity with direct
EMI and direct sponsor-bank relationships, capable of supporting regulated
payment flows without reliance on opaque program managers or aggregator
structures.

Preferred model:

- Canadian MSB under the PCMLTFA;
- RPAA-ready operating controls;
- direct EMI partnership in Europe or the UK; and
- direct bank sponsorship agreement with a smaller sponsor-friendly
  institution.

Potential sponsor-friendly examples include Solaris, ClearBank, B4B,
Modulr-partner bank structures, Banking Circle, and smaller Baltic or Central
European sponsor banks.

The asset being built is a clean compliance and banking distribution layer
that can later support embedded finance, cross-border payments, wallets,
treasury flows, stablecoin rails, or B2B payment orchestration.

## Revised Target Architecture

End-state structure:

```text
Customers
   ->
1001494374 Ontario Corp
MSB + RPAA-active compliance / control entity
   ->
Direct EMI relationship
   ->
Direct sponsor-bank relationship
   ->
Settlement / safeguarding accounts
```

Optional crypto structure:

```text
Customers
   ->
Segregated crypto partner
no commingling with fiat safeguarding structure
```

## Non-Negotiables

### Regulatory

The entity operates the AML perimeter.

It maintains direct FINTRAC registration.

It owns customer risk governance and transaction visibility.

RPAA readiness is built from inception.

### Banking

The sponsor bank is directly contracted or directly referenceable.

There should be no opaque nested sponsorship chains.

Program managers should not be the primary contractual counterparty.

### Structural

The entity does not hold customer funds.

The EMI performs safeguarding.

The bank holds safeguarding and settlement accounts.

Customer funds remain bankruptcy remote.

## Strategic Positioning

The platform should be positioned as:

```text
A compliance-first payment operating layer with direct regulated financial
institution connectivity.
```

This matters commercially because acquirers pay more for:

- clean financial-institution relationships;
- direct sponsor-bank access;
- transferable compliance infrastructure;
- documented flow-of-funds architecture; and
- reduced dependency concentration.

A software-only orchestration layer has limited strategic value.

A platform with active MSB status, RPAA-operational capability, direct EMI,
direct sponsor bank, and audited compliance infrastructure becomes
infrastructure-grade.

## Core Build Pillars

### A. Regulatory Perimeter

Canadian operating stack:

- FINTRAC-registered MSB;
- RPAA-ready payments operation; and
- audit-ready AML framework.

Deliverables:

- active MSB registration;
- compliance officer appointment;
- AML governance framework;
- independent review process;
- KYC / KYB policy;
- sanctions screening policy;
- transaction monitoring policy;
- STR / LCTR workflow;
- enhanced due diligence process;
- travel rule applicability analysis;
- crypto exposure controls;
- safeguarding logic;
- incident management;
- operational resilience;
- outsourcing governance;
- reconciliation controls;
- complaint handling; and
- audit trails.

Strategic goal:

```text
Build a diligence-clean operating perimeter that a bank, EMI, or acquirer can
underwrite quickly.
```

The objective is not merely registration.

### B. Direct EMI Relationship

Required structure:

- direct contract with the EMI;
- no reseller structure;
- no nested agent chain; and
- no embedded-finance aggregator that obscures banking access.

Preferred counterparty types:

- smaller European EMI platforms;
- UK EMI structures;
- EMI-bank hybrid platforms; and
- sponsor-bank-friendly fintech infrastructure providers.

Potential targets may include:

- Solaris;
- ClearBank;
- Banking Circle; and
- B4B Payments.

EMI responsibilities:

- hold customer funds;
- perform safeguarding;
- manage regulated payment accounts;
- potentially support onboarding / KYC tooling; and
- interface with sponsor-bank safeguarding structures.

The entity remains responsible for:

- AML program;
- customer risk governance;
- transaction visibility; and
- Canadian compliance obligations.

Critical negotiation points:

- safeguarding account visibility;
- reconciliation reporting;
- audit access;
- incident notification;
- regulator-request cooperation;
- customer data portability; and
- transition support if banking changes.

### C. Direct Sponsor Bank Relationship

This is the major revision from the earlier 174 / Granville concept.

Objective:

```text
Move from "EMI with hidden bank sponsor" to "directly referenceable
sponsor-bank relationship with contractual visibility."
```

Preferred structure:

```text
1001494374 Ontario Corp
   ->
Direct EMI agreement
   ->
Direct sponsor-bank sponsorship agreement
   ->
Safeguarding / settlement accounts
```

Why this matters:

- improves valuation;
- improves durability;
- improves regulator confidence;
- improves EMI portability;
- improves acquirer attractiveness; and
- reduces hidden banking dependency concentration.

Target sponsor-bank profile:

- not necessarily Tier 1 at first;
- sponsor-friendly;
- fintech-accommodative; and
- operationally flexible.

Examples:

- Solaris;
- ClearBank;
- Banking Circle;
- smaller Baltic or Central European sponsor banks; and
- EMI-aligned safeguarding banks.

Banks will diligence:

- customer geography;
- crypto exposure;
- sanctions exposure;
- AML maturity;
- transaction profile;
- source-of-funds logic;
- operational governance; and
- escalation procedures.

Bankability improves materially if:

- customer funds never touch the entity's balance sheet;
- crypto is segregated; and
- flows are fully traceable.

Required deliverables:

- bank-grade flow-of-funds package;
- customer onboarding map;
- payment initiation map;
- safeguarding mechanics;
- reconciliation logic;
- operational account map;
- exception handling process; and
- concise compliance narrative.

The compliance narrative should answer:

- why the model is low-risk;
- who holds funds;
- who performs safeguarding;
- how AML responsibilities are split; and
- how customer funds remain protected.

### D. Software Layer

The software stack should be intentionally minimal.

This is not a neobank UI business.

The build is regulatory-grade orchestration infrastructure.

Required components:

1. Independent ledger.

The ledger must support:

- reconciliation;
- customer balance visibility;
- auditability;
- EMI reconciliation; and
- transaction history.

This is required even if funds remain off balance sheet.

2. AML stack.

The AML stack must support:

- KYC / KYB;
- sanctions;
- transaction monitoring;
- case management;
- reporting workflows; and
- audit logs.

3. Orchestration layer.

The API layer should connect:

- EMI;
- sponsor bank;
- payment rails; and
- optional crypto provider.

Critical design requirements:

- portability;
- provider abstraction;
- banking migration capability;
- EMI-native stack;
- lightweight orchestration;
- outsourced tooling where necessary; and
- direct bank API connectivity where available.

## Flow of Funds

Target fiat flow:

```text
Customer
   ->
EMI payment account
   ->
Safeguarding account at sponsor bank
```

Operating role:

```text
Customer
   ->
1001494374 Ontario Corp
compliance supervision + onboarding governance
   ->
EMI
regulated payment account + safeguarding
   ->
Sponsor bank
settlement and safeguarding infrastructure
```

Critical design principle:

The entity orchestrates payments, monitors AML, and governs itself.

It does not custody customer funds, perform unauthorized deposit-taking, or
create balance-sheet exposure.

## Revised 90-Day Execution Plan

### Weeks 1-4: Foundation

- confirm entity-status assumptions for `1001494374 Ontario Corp`;
- confirm FINTRAC status and any update requirements;
- build AML framework;
- define RPAA operating model;
- prepare bank-grade flow-of-funds document;
- shortlist EMI partners;
- shortlist sponsor banks; and
- shortlist compliance tooling.

### Weeks 4-8: Institutional Layer

- execute direct EMI agreement;
- begin sponsor-bank onboarding discussions;
- validate safeguarding structure;
- implement KYC / AML stack;
- finalize operational policies; and
- build reconciliation framework.

### Weeks 8-12: Operationalization

- stand up ledger;
- complete transaction testing;
- finalize reporting workflows;
- validate safeguarding reporting;
- produce audit-ready documentation; and
- conduct dry-run compliance exercises.

## What Done Looks Like

The platform is successful when:

- MSB status is active and operational;
- RPAA-ready controls are implemented;
- direct EMI agreement is signed;
- sponsor bank relationship is direct and referenceable;
- flow of funds is clear, auditable, regulator-readable, and
  bank-understandable;
- customer funds never touch the entity's balance sheet;
- banking dependency risk is minimized; and
- platform can survive EMI or bank migration.

## Build Completion Criteria

Locarno has two possible completion standards because it has two different
value theses.

The pure-shell sale thesis and the infrastructure-asset thesis should not be
judged by the same gate.

### Track A: Pure MSB Shell Sale Completion

The pure-shell build is complete when:

- FINTRAC registration status is verified as active and in good standing;
- corporate minute book and ownership records are sale-ready;
- no legacy activity, liabilities, client funds, or undisclosed obligations
  impair diligence;
- AML program is documented at least to dormant / pre-operational standard;
- required dormant-period reports or nil-reporting assumptions are documented;
- no RPAA or PSP positioning creates unnecessary buyer friction;
- Canadian-director advantage of the Ontario corporation is clearly documented;
- buyer handoff memo is complete; and
- sale package explains why the Ontario corporation is cleaner than the
  federal company for a pure MSB buyer.

Track A is complete when a buyer can underwrite the asset as a clean MSB shell
without needing to rely on future EMI, sponsor-bank, or software build-out.

### Track B: Infrastructure Asset Completion

Track B should be judged through three gates.

#### Minimum Track B Gate

The minimum infrastructure build is complete when:

- FINTRAC status is active, verified, and operationally supportable;
- RPAA-ready controls are designed and documented;
- RPAA registration, application, or re-registration posture is clearly mapped
  for sale;
- direct EMI candidate shortlist is complete;
- at least one EMI has provided written indication that direct contracting is
  viable;
- sponsor-bank candidate shortlist is complete;
- at least one sponsor-bank path is directly referenceable or supported by a
  named EMI / bank structure;
- bank-grade flow-of-funds package is drafted;
- safeguarding structure is documented at the design level;
- customer funds are designed not to touch the entity's balance sheet;
- AML framework is complete enough for bank / EMI review;
- ledger and reconciliation requirements are specified;
- orchestration architecture is provider-abstracted on paper; and
- diligence folder can support initial bank, EMI, and buyer review.

The minimum gate means Locarno is more than a shell, but not yet fully
institutionalized.

#### Preferred Track B Gate

Preferred Track B is a yes / no gate.

It is complete only when the minimum gate is satisfied and all of the following
are true:

- RPAA registration is complete;
- direct EMI agreement is signed;
- EMI terms preserve assignment, change-of-control, termination, and migration
  optionality;
- sponsor-bank relationship is supported by written counterparty
  correspondence from a named sponsor bank, EMI-bank hybrid, or EMI-aligned
  safeguarding bank;
- safeguarding account visibility and reporting are confirmed in principle;
- reconciliation reporting is specified;
- independent ledger is implemented or demo-ready;
- AML stack is implemented or demo-ready;
- orchestration layer has a working adapter pattern;
- incident, reconciliation, outsourcing, complaint, and audit-trail controls
  are documented;
- at least one dry-run compliance exercise has been completed; and
- buyer can understand both keep-the-stack and replace-the-stack scenarios.

If any item is missing, Preferred Track B is not complete.

The preferred gate means Locarno can credibly be marketed as a payments
infrastructure asset, subject to remaining execution risk.

#### Stretch Track B Gate

Stretch Track B is a yes / no gate.

It is complete only when the preferred gate is satisfied and the institutional
stack is fully contracted:

- RPAA registration is complete;
- direct EMI agreement is signed;
- direct bank or sponsor-bank agreement is signed;
- bank / sponsor-bank terms preserve assignment, change-of-control,
  termination, and migration optionality;
- safeguarding reporting has been validated;
- ledger and reconciliation workflows have been tested;
- AML workflow is operational and audit-logged;
- payment initiation and account / wallet setup have been tested where
  applicable;
- dry-run compliance exercises are complete;
- migration plan covers both EMI replacement and sponsor-bank replacement;
- vendor contracts do not contain exclusivity, punitive exit fees, or
  non-transferability terms that materially impair sale;
- diligence folder supports bank, EMI, acquirer, and regulator-style review;
  and
- buyer transition steps are mapped.

If any item is missing, Stretch Track B is not complete.

The stretch gate means Locarno can be priced and discussed as a transferable
regulated payments infrastructure layer, not merely as an enhanced shell.

Track B is complete when a buyer can underwrite the asset as regulated payments
infrastructure, not merely as a shell.

### Valuation Readiness Gate

Locarno should not be valued as an infrastructure asset unless Track B is
substantially complete.

Working internal valuation markers:

| Gate | Working value marker |
| --- | --- |
| Track A pure MSB shell | CAD 50,000 |
| Minimum Track B | CAD 50,000 |
| Preferred Track B | CAD 200,000 |
| Stretch Track B | CAD 650,000 |

If only Track A is complete, the asset should be valued as a clean MSB shell at
the current working marker of `CAD 50,000`.

Minimum Track B should also be valued at `CAD 50,000`. The minimum gate
improves diligence quality, but does not itself create a pricing premium over
the shell case.

Preferred Track B should be valued at the current working marker of
`CAD 200,000`.

Stretch Track B should be valued at the current working marker of
`CAD 650,000`.

If Track B is partially complete, the sale narrative may support a premium, but
the price should be discounted for:

- unresolved EMI contract risk;
- unresolved sponsor-bank risk;
- RPAA acquisition-of-control or re-registration risk;
- lack of tested flows;
- non-transferable vendor relationships;
- software that is not yet operational; and
- incomplete audit-ready documentation.

### Not Complete If

Locarno should not be treated as build-complete if:

- FINTRAC status has not been verified;
- RPAA posture is unclear;
- the direct sponsor-bank relationship is only aspirational;
- EMI access depends on opaque program-manager structures;
- customer-funds safeguarding cannot be explained simply;
- software layer cannot produce ledger, reconciliation, AML, and audit outputs;
- buyer cannot inherit or replace key relationships cleanly; or
- the project cannot be sold as either a clean shell or a real infrastructure
  asset without mixing the two narratives.

## Goal

This is not a consumer fintech build.

The goal is to build a transferable regulated payments infrastructure layer
with direct institutional connectivity.

That is what creates acquisition value, financing optionality, and long-term
defensibility.
