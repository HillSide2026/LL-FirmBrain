---
id: 04_initiatives__hillside_portfolio__matthew_holdings__2b_federal_msb_17409052_canada_inc__value_stack_md
title: 17409052 Canada Inc Value Stack
owner: ML1
status: draft
created_date: 2026-05-11
last_updated: 2026-05-11
tags: [granville, federal-msb, emi, payments, orchestration, safeguarding]
---

# 17409052 Canada Inc Value Stack

## Entity

`17409052 Canada Inc` is a federal company within the Matthew Holdings
structure.

Granville is an internal tag for `17409052 Canada Inc`.

The tag has no operational, legal, branding, or customer-facing significance.

Current operating activity: none.

FINTRAC registration is still pending.

The RPAA application has been initiated.

The wait for FINTRAC has motivated the effort to add value to the entity by
developing a clearer payments infrastructure stack.

The point is not to operate a significant funds-flow business through this
entity.

The current strategic point is to increase sale value.

## Target Model

The target value stack is:

```text
Customer
   ↓
17409052 Canada Inc
MSB; orchestration; application; AML control
   ↓
EMI
onboards clients; provides payment accounts; executes payments
   ↓
Bank
safeguards funds
```

The intended posture is deliberately infrastructure-light at the balance-sheet
level.

The entity would own the customer-facing application layer, orchestration
layer, and AML control layer.

The EMI provides client onboarding, payment accounts, and payment execution.

The bank safeguards funds.

This structure is intended to keep balance-sheet complexity minimal while
supporting a cleaner Retail Payment Activities Act posture.

## Sufficiency Standard

A payment account is sufficient only if the EMI relationship provides the
functional, safeguarding, and contractual features needed for the entity's
operating model.

### A. Full Transactional Capability

The EMI must support:

- inbound payments
- outbound payments
- domestic payment activity
- cross-border payment activity, ideally from the beginning
- account identifiers, such as IBANs or a practical equivalent
- reconciliation feeds

### B. Clear Safeguarding Structure

Funds should sit with:

- a named bank
- segregated safeguarding accounts

The entity does not need control of the safeguarding account in Stage 1.

It does need transparency.

The target visibility standard is enough to understand where funds sit, how
they are segregated, and how the safeguarding structure supports customer,
regulatory, and counterparty diligence.

### C. Direct EMI Relationship

The EMI must be contractually visible.

The entity should not rely on an opaque reseller or indirect arrangement where
the real EMI relationship is hidden, undocumented, or operationally fragile.

## Build Sequence

The build is deliberately sequenced in two stages.

### Stage 1 — EMI Plus Abstracted Bank

Stage 1 uses an EMI relationship with the bank layer abstracted through the
EMI.

The EMI onboards clients, provides payment accounts, and executes payments.

The bank safeguards funds behind the EMI structure.

This stage is acceptable if the EMI relationship satisfies the sufficiency
standard above.

### Stage 2 — EMI Plus Direct Bank Relationship

Stage 2 adds a direct bank relationship.

The entity's bank relationship becomes visible and contractual.

This does not replace the EMI.

It adds a second rail.

The EMI can continue to provide payment accounts and hold funds where that is
the right structure.

The entity may also add its own operating or settlement accounts, and possibly
client-money flows depending on the final structure.

## Software Architecture Implication

The orchestration layer should be bank-agnostic from day one.

The architecture should use one internal interface for payment instructions:

```text
17409052 Canada Inc System
   ├── EMI Adapter
   │   └── Stage 1 active
   └── Bank Adapter
       └── Stage 2 ready; unused at launch
```

All payment instructions should pass through the same internal routing
interface.

In Stage 1, instructions route to the EMI.

In Stage 2, instructions can route to:

- the EMI; or
- direct bank rails.

The goal is to avoid a future rewrite when direct bank connectivity is added.

## Product and Compliance Software Procurement

The value-stack build should include procured product software and compliance
software.

The procurement objective is not to create a heavy operating platform.

It is to make the entity more credible and more saleable by showing a buyer a
coherent stack:

- corporate vehicle
- FINTRAC application path
- initiated RPAA application
- EMI / payment-account path
- safeguarding visibility thesis
- product software
- compliance software
- bank-agnostic orchestration design

### Compliance Software Question

The main compliance-software question is whether the entity needs Sumsub or
whether Rhizome is sufficient.

Sumsub should be used only if EMI onboarding or bank / safeguarding
counterparties create a real need.

Rhizome may be sufficient if the immediate goal is to demonstrate compliance
workflow capability at lower cost, especially where the entity does not intend
to run significant funds through the stack before sale.

The current working bias is cost discipline.

Because the entity is sale-oriented and not expected to carry meaningful funds
flow, the procurement decision should avoid overbuilding.

### Decision Rule

Use Rhizome if it is enough to support the sale narrative, compliance workflow
demonstration, and diligence package.

Use Sumsub only if one of the following creates a real need:

- EMI onboarding requires it;
- a bank counterparty requires it; or
- a safeguarding counterparty requires it.

The software decision should remain reversible where possible.

The orchestration layer should avoid hard-coding either provider into the core
customer, ledger, AML, or payment-instruction model.

### Real Integration Question

The real build question is how to secure the EMI integration.

The compliance tooling decision is secondary.

The EMI relationship is what determines whether the entity can show a credible
payment-account path, transactional capability, safeguarding visibility, and
counterparty-ready operating model.

The EMI integration work should therefore focus on:

- which EMI will contract directly or visibly with the entity;
- whether the EMI can onboard the relevant client profile;
- whether the EMI supports the required inbound and outbound flows;
- whether account identifiers and reconciliation feeds are available;
- whether safeguarding visibility is adequate;
- whether the EMI requires Sumsub or another KYC / KYB layer; and
- whether the integration can be documented in a form that improves sale
  diligence.

## Pre-Revenue EMI Contracting Strategy

The entity should establish an EMI relationship pre-revenue only if the
relationship is structured as a transferable, low-commitment infrastructure
agreement.

With no flows, the EMI may push for fees, minimums, control rights, or
commitments.

The risk is not rejection.

The risk is locking into terms that collapse value on sale.

Core design principle:

```text
buyer-substitutable from day 1
```

### Decision Frame

The decision is how to contract with an EMI so that:

- the entity can close quickly despite having no flows;
- a buyer can inherit or replace the EMI cleanly; and
- the entity does not overpay or overcommit upfront.

### Candidate Provider Notes

| Provider | Type | Accessibility | Cost | Notes |
| --- | --- | --- | --- | --- |
| Moorwand | EMI | High | High | Flexible structurer; may accept non-standard setups |
| Paynetics | EMI / processor hybrid | Medium-High | Medium | More infrastructure-driven and less retail-facing; still viable |
| Wallester | EMI | Medium-High | Medium | Fast onboarding; more platformized |

### Target Relationship Structure

The ask is not for a long-term program.

The ask is for a revocable, transferable infrastructure access agreement.

### Engagement Model

Position the entity as:

```text
We are a technology platform integrating via standard APIs.
We are pre-revenue and expect to scale post-launch or post-transaction.
```

Avoid saying:

- we are building a full PSP;
- we will route flows dynamically;
- we need custom logic.

The goal is to land as a low-complexity, standard client with future upside.

### Contract Structure

The preferred core agreement structure is:

- direct EMI agreement, not reseller;
- standard API access; and
- no bespoke workflows.

Must-have clauses:

- change of control protection: the EMI cannot terminate solely because of an
  acquisition, or there is a predefined re-underwriting process;
- termination flexibility: no punitive exit fees; and
- no exclusivity: the entity can integrate other EMIs or migrate later.

Given no flows, the entity may need to accept:

- setup fee;
- monthly minimums; and
- conservative limits.

The entity should not accept:

- exclusivity;
- long-term lock-in; or
- revenue-share traps.

### Commercial Structure

The entity has no volume and limited leverage.

The commercial structure should therefore preserve optionality.

Preferred option:

- low setup fee;
- moderate monthly minimum.

Fallback option:

- higher setup fee;
- lower ongoing cost.

Avoid:

- long-term volume commitments; and
- penalty-based pricing.

Higher pricing may be acceptable if it preserves flexibility and sale value.

Higher pricing is not acceptable if it cannot be renegotiated, assigned,
terminated, or replaced before sale.

### Technical Structure

Technical non-negotiables:

- single integration layer;
- backend calls the EMI;
- no direct customer-to-EMI dependency;
- no EMI-specific custom logic;
- no custom workflows;
- no proprietary dependencies; and
- API abstraction ready from day one.

Even if only one EMI is active at launch, the system should be designed around
an adapter layer.

### Sequencing

Phase 1: Parallel outreach, weeks 1-2.

Target fast-access EMI candidates.

Candidate list to fill:

- TBD
- TBD

Goal: secure term sheets.

Phase 2: Term sheet pressure.

Run two EMIs in parallel.

Use the parallel process to test:

- pricing competition;
- transferability;
- monthly minimums;
- setup fees;
- change-of-control treatment;
- termination flexibility; and
- willingness to support a pre-revenue entity.

Phase 3: Contract lock.

Select the most flexible contract, not necessarily the cheapest contract.

The winning EMI should preserve sale value by allowing a buyer to inherit or
replace the relationship cleanly.

Phase 4: Lightweight integration, weeks 6-10.

Implement only what is needed to support the value stack:

- account creation;
- payment initiation;
- basic reconciliation feed; and
- integration documentation.

No scale build is required before sale.

### Sale Use Case

The EMI strategy must support both likely buyer scenarios.

Scenario A: buyer keeps the EMI.

The buyer values:

- speed to market;
- pre-integrated rails;
- reduced vendor-search burden; and
- a clearer regulatory and operational diligence package.

Scenario B: buyer replaces the EMI.

The buyer values:

- clean architecture;
- no lock-in;
- no exclusivity;
- no punitive termination economics; and
- a reusable adapter pattern.

The job is to support both outcomes.

### Key EMI Risks

Commercial risk:

- the entity accepts high pricing because it has no volume or leverage;
- the pricing cannot be renegotiated before sale; and
- the buyer treats the pricing as a drag on value.

Transactional risk:

- the EMI requires full re-underwriting after sale;
- the buyer cannot rely on the existing relationship for speed to market; and
- the pre-sale integration loses much of its value.

Structural risk:

- the contract cannot be assigned;
- change of control is treated as a termination event; or
- the contract otherwise prevents a buyer from inheriting the relationship.

This structural risk can destroy value.

### Recommendation

Build the EMI relationship this way:

| Element | Strategy |
| --- | --- |
| EMI selection | Tier 1 access first |
| Contract | Short-term and flexible |
| Pricing | Accept higher cost only where it preserves optionality |
| Integration | Minimal standard API |
| Optionality | Preserve ability to switch |

## Stage 2 Change Set

If Stage 1 is implemented properly, Stage 2 should require additions rather
than restructuring.

Stage 2 adds:

- bank API integration
- routing logic for rail selection
- direct-bank operational and contractual controls

Stage 2 should not require changes to:

- the ledger
- the AML layer
- the customer model
- the core payment-instruction interface

## Sale Thesis

The entity is being built for sale value rather than scaled operation.

The intended buyer should be able to see a cleaner asset package than a bare
federal company waiting on FINTRAC.

The sale package should show:

- pending FINTRAC path;
- initiated RPAA application;
- low-complexity funds-flow posture;
- EMI-led payment-account strategy;
- safeguarding transparency model;
- product and compliance software procurement path;
- bank-agnostic technical design; and
- clear boundaries from FinSure, the Payment Services Consulting Line, and
  Levine Law.

Significant funds should not be routed through the entity unless a separate
decision is made.

Pre-sale activity should be limited to what is needed to preserve regulatory
credibility, support diligence, and improve buyer confidence.

## Build Completion Criteria

Granville is complete when it is no longer just a pending federal company with
a concept note, but a sale-ready infrastructure package.

The completion standard is not scaled operations.

The completion standard is buyer diligence readiness.

### Minimum Completion Gate

The minimum build is complete when all of the following are true:

- FINTRAC status is resolved or the pending status is documented with current
  correspondence and expected next steps;
- RPAA application status is documented, including whether any re-registration
  issue would arise on sale;
- AML program package is complete enough for buyer review;
- product-software candidate is selected or deliberately deferred;
- compliance-software decision is made, with Rhizome as default unless EMI,
  bank, or safeguarding counterparties require Sumsub;
- EMI target shortlist is complete;
- at least one EMI has provided written indication of willingness to onboard or
  continue discussions with the entity;
- buyer-facing flow-of-funds and safeguarding memo is complete;
- architecture memo confirms bank-agnostic adapter design; and
- sale package clearly states that the entity is not intended to carry
  significant pre-sale funds flow.

### Preferred Completion Gate

The preferred build is complete when the minimum gate is satisfied and:

- EMI term sheet or draft agreement is received;
- EMI pricing, minimums, termination, exclusivity, and change-of-control terms
  are documented;
- contract structure preserves buyer optionality;
- lightweight API integration plan is documented;
- reconciliation-feed availability is confirmed;
- safeguarding visibility is confirmed at least in principle; and
- buyer can inherit or replace the EMI without destroying value.

### Stretch Completion Gate

The stretch build is complete when the preferred gate is satisfied and:

- direct EMI agreement is signed;
- lightweight integration has been tested;
- compliance workflow is demo-ready;
- diligence folder includes AML, RPAA, flow-of-funds, software, and EMI
  documentation;
- no exclusivity or long-term lock-in impairs sale; and
- buyer transition steps are mapped.

### Not Complete If

The build should not be treated as complete if:

- FINTRAC status is unresolved and undocumented;
- RPAA status is unclear;
- EMI access is only speculative;
- software procurement is only conceptual;
- flow-of-funds documentation is missing;
- EMI terms create exclusivity, long-term lock-in, punitive termination, or
  non-transferability risk; or
- the package cannot be explained to a buyer in one clean diligence narrative.

## Boundary Notes

`17409052 Canada Inc` is distinct from FinSure and the Payment Services
Consulting Line.

FinSure and the Payment Services Consulting Line are owned and operated by
`17513721 Canada Inc`, not by `17409052 Canada Inc`.

`17409052 Canada Inc` is also distinct from Levine Law F03 regulatory
advisory.

Any legal advisory, paid triage, fixed-fee regulatory mandate, or ongoing
Levine Law counsel relationship must remain a Levine Law matter, not an
operating activity of `17409052 Canada Inc`.

## Open Confirmation Items

- EMI candidate and contract path
- bank name and safeguarding-account structure
- confirmation of account-identifier capabilities
- reconciliation-feed availability
- Stage 1 launch scope
- Stage 2 direct-bank relationship trigger
- product software candidate
- Sumsub vs Rhizome decision
- EMI integration path
- EMI onboarding requirements
- EMI change-of-control treatment
- EMI exclusivity / lock-in terms
- EMI setup fee and monthly minimums
- bank / safeguarding counterparty requirements
- final RPAA / MSB operating analysis before launch
