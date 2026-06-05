---
id: 04_initiatives__hillside_portfolio__matthew_holdings__2b_federal_msb_17409052_canada_inc__sale_readiness_next_steps_md
title: 17409052 Canada Inc Sale-Readiness Next Steps
owner: ML1
status: draft
created_date: 2026-05-15
last_updated: 2026-05-19
tags: [granville, federal-msb, sale-readiness, rpaa, emi, product-software, users]
---

# 17409052 Canada Inc Sale-Readiness Next Steps

## Purpose

This document converts the 174 sale-readiness gates (minimum, preferred, stretch)
into near-term execution workstreams.

The objective is to move `17409052 Canada Inc` from a federal MSB / payments
infrastructure concept into a buyer-readable sale package.

## Sale-Readiness Gates

### Minimum
- FINTRAC MSB registration issued; and
- AML program complete enough for buyer review.

### Preferred
*(minimum gate satisfied, plus:)*
- FINTRAC and RPAA status established on the public registry;
- at least one EMI has provided written indication of willingness to onboard 174;
- compliance-software decision made (Rhizome as default unless EMI or bank requires Sumsub);
- Kwiikpay role as a 174 infrastructure path established or ruled out; and
- buyer can understand both outcomes: keep the EMI path or replace it without destroying value.

### Stretch
*(preferred gate satisfied, plus:)*
- direct EMI agreement is signed;
- lightweight integration has been tested;
- some actual flow of funds has occurred through the entity;
- compliance workflow is demo-ready;
- diligence folder is complete, including:
  - AML program;
  - RPAA analysis / status;
  - flow of funds (documented, with actual transaction evidence);
  - compliance software decision; and
  - EMI documentation;
- no exclusivity, lock-in, or dependency that impairs sale; and
- buyer transition steps are mapped.

## Current Priority Workstreams

| Workstream | Objective | Current state | Next output |
| --- | --- | --- | --- |
| Product-software pricing and offers | Obtain pricing, terms, and implementation offers for candidate product platforms | Candidate list exists; no vendor pricing / offer package yet | Vendor pricing grid and offer comparison |
| RPAA application | Advance and document RPAA application status | Pending; not yet waiting on Bank of Canada | RPAA status note and next-step log |
| EMI alternatives | Find alternatives to the EUR 12,000 EMI offer | EUR 12,000 offer exists; alternatives not yet identified | EMI alternatives shortlist |
| User acquisition / demand proof | Acquire or evidence users / prospective users to support buyer confidence | No 174 user proof recorded | User-acquisition test plan and prospect list |

## Product-Software Pricing and Offers

### Candidate Platforms

The current 174 product-software candidates are:

- Mambu Payments / Payments Hub;
- Toqio;
- Crassula; and
- SDK.finance.

### Pricing Status

| Candidate | Public pricing status | Required action |
| --- | --- | --- |
| Mambu Payments / Payments Hub | No full public quote located. Public materials point to sales contact / payment transformation discussion. | Request pricing and implementation proposal. |
| Toqio | No full public quote located. Public materials point to demo / sales discussion. | Request pricing and implementation proposal. |
| Crassula | Meeting held week of 2026-05-18. Crassula pitched software plus connectors. Modules discussed: UI, fiat accounts, EUR/GBP/USD. Opening pricing is still pending final confirmation at roughly 20k setup and 11k/month. Robust EMI connector list may be the main differentiator. Possible sandbox availability for regulator review is a bright spot, but prerequisites are unclear. | Confirm final quote and currency, EMI connector availability for 174, and sandbox prerequisites for regulator review. |
| SDK.finance | Public pricing page describes enterprise licensing options and quote process; no fixed price captured. | Request annual, lifetime, and SaaS / source-code options. |
| FinLego | Meeting held week of 2026-05-18. Software provider with UI, fiat accounts, and EUR/GBP/USD support. Banking access was described through Kanzum, which does not satisfy RPAA safeguarding. Opening pricing received at EUR 15k setup and EUR 4k/month; final offer pending. | Confirm final offer, whether software is separable from Kanzum, and whether any part of the structure materially helps the 174 value stack despite the safeguarding issue. |

### Offer Request Questions

Each candidate should be asked for:

1. Minimum viable module set for a pre-revenue MSB sale-readiness package.
2. Setup fee.
3. Monthly / annual fee.
4. Implementation timeline.
5. Required integrations.
6. Whether an EMI or bank relationship is required first.
7. Data export and portability.
8. Whether the offer can be documented in a buyer diligence folder.
9. Whether a non-core-banking package exists for an EMI-led, pre-revenue sale
   asset.
10. Whether sandbox or demo access can be provided for buyer or regulator review
    without full production deployment.
11. Which modules can be removed if 174 is not trying to market "banking."

### Desired Output

Create a pricing and offer grid with:

- vendor;
- product modules;
- minimum non-banking package;
- setup fee;
- recurring fee;
- implementation timeline;
- regulated-provider dependency;
- sandbox / demo availability;
- transferability;
- key restrictions;
- buyer-diligence usefulness; and
- ML1 posture: pursue, hold, reject, or use as pricing leverage.

## Advance RPAA Application

The Bank of Canada RPAA registration requires a description of the intended
safeguarding arrangement, not proof of a signed EMI contract. A written
indication from an EMI that it is willing to onboard 174 is sufficient to
support the safeguarding description in the application. The signed EMI
contract gates actual operations, not the application itself. The RPAA
application may be filed once both an EMI written indication and a software
written indication are in hand — it does not need to wait for signed deals.

The RPAA workstream should produce a current status record.

Required outputs:

- current RPAA application status;
- public-registry status, if available;
- date of last filing, submission, or correspondence;
- next required step;
- deadline or expected response date;
- sale / change-of-control implications;
- whether a buyer would need a new filing, notice, re-registration, or update;
  and
- whether 174 can be marketed as RPAA-initiated, RPAA-pending, or
  RPAA-registered.

## RPAA Application — Known Blockers

The following items have been identified as potentially blocking finalization
of the RPAA application. Each has a different character.

| # | Blocker | Character | Status |
| --- | --- | --- | --- |
| 1 | Credible domain | Hard requirement | Not yet confirmed |
| 2 | Financial institution to hold/safeguard funds | Appears to be unspoken/informal criteria | Not yet secured |
| 3 | Software in place | Better to have; not absolutely necessary | Not yet in place |

### Blocker 1 — Credible Domain

The Bank of Canada appears to require a credible domain as part of the
application. A domain that signals a legitimate, operating (or pre-operating)
payments business is expected.

**Current direction:** A single-page site. A single page describing the
entity's payments business and regulatory status (MSB registration pending,
RPAA application in progress) is likely sufficient for the Bank of Canada's
purposes at this stage.

**Branding:** The intended brand name is "Granville." This is how the business
will likely be branded and marketed. However, finding an available domain
containing the word "Granville" has proven difficult. A domain that
incorporates the brand name is preferred but the right available variant has
not yet been identified.

**Action required:** Maintain a credible Granville-facing page, confirm the
domain position is ready for the RPAA file, and record any Bank follow-up if
and when the application moves into Bank of Canada review.

### Blocker 2 — Financial Institution to Hold / Safeguard Funds

The RPAA requires a safeguarding arrangement: a financial institution that
holds end-user funds separate from the PSP's own funds. This does not appear
to be a formally stated pre-condition in the application form itself, but it
is an unspoken/informal criteria — the Bank of Canada expects a credible
safeguarding counterparty to be identified or in view.

An EMI satisfies this by definition. Under the EU/UK regulatory framework
(EMD2), safeguarding of client funds is a core licensing condition for all
EMIs — it is not optional. An EMI relationship therefore solves both the
operational model requirement and the safeguarding requirement simultaneously.

The RPAA nuance: the safeguarding obligation under RPAA Part 4 attaches to
17409052 as the registrant, not to the EMI. The Bank of Canada will expect
17409052 to document and own the safeguarding structure in its application —
the answer "the EMI holds client funds" is sufficient, but it must be
explicitly described as the safeguarding arrangement. A written indication or
draft terms from an EMI is therefore the output needed to clear this blocker.

**Note:** A letter of intent from an EMI is potentially sufficient for the
RPAA application. A fully executed agreement is not necessarily required at
the application stage.

**Current position:** Conversations are ongoing with at least one EMI,
including a quoted offer of EUR 12,000. This existing conversation is the
natural path to an LOI.

**How to convert the existing conversation into an LOI:** An LOI in this
context does not need to be a formal legal document. The practical path is:

1. Ask the EMI (the EUR 12,000 counterparty, or any other active conversation)
   to provide a written statement — which can be a formal letter or a detailed
   email — confirming that they are willing to provide payment accounts and
   safeguard client funds for 17409052 Canada Inc, subject to final agreement
   on terms.
2. The statement should identify: the EMI's name and regulated status; the
   scope of services (payment accounts, safeguarding, execution); and a
   reference to the commercial terms discussed (e.g. the EUR 12,000 offer).
3. It does not need to be binding. "Willing to proceed subject to final
   agreement" is sufficient.
4. A detailed email from the EMI confirming these points is acceptable as a
   written indication if a formal letter is not available.

**Action required:** Request a written indication or LOI from the EUR 12,000
EMI (or the strongest active conversation). File it in the RPAA application
folder as the safeguarding structure documentation.

### Blocker 3 — Software in Place

Having product software in place would strengthen the application by
demonstrating operational readiness. However, this is not an absolute
requirement — it is a value-add that improves credibility with the Bank of
Canada but does not gate the application.

**Action required:** Advance product-software evaluation in parallel. Do not
allow software procurement to block RPAA progress.

## Find Alternatives to the EUR 12,000 EMI Offer

The EUR 12,000 EMI offer should not be treated as the only path until at least
one alternative has been tested.

Alternative EMI search should focus on:

- direct or clearly visible EMI relationship;
- support for pre-revenue / low-flow entity;
- willingness to provide written indication or draft terms;
- payment-account capability;
- inbound / outbound payment capability;
- safeguarding visibility;
- reconciliation reporting;
- no exclusivity;
- no long lock-in;
- assignment or change-of-control path; and
- buyer-substitutable architecture.

Desired output:

- at least two alternative EMI candidates;
- one written outreach record per candidate;
- response / no-response status;
- pricing indication if available;
- transferability position if available; and
- comparison against the EUR 12,000 offer.

## Acquire Users / Demand Proof

174 does not need scaled operations before sale, but buyer confidence improves
if there is credible demand evidence.

User acquisition for 174 should be narrow and low-risk.

Potential user-proof categories:

- letters of interest;
- waitlist signups;
- design-partner conversations;
- non-binding pilot interest;
- prospective merchant / SME use cases;
- prospective payments or treasury users;
- Kwiikpay-related user path if Kwiikpay becomes 174 infrastructure; and
- buyer-facing evidence that the product stack solves a real market need.

Constraints:

- do not route significant funds through 174 before a separate ML1 decision;
- do not imply live regulated operations beyond actual status;
- do not create customer obligations that impair sale;
- do not blur 174 with Levine Law, FinSure, or 175 commercial channels; and
- do not let user acquisition outrun regulatory, EMI, and software readiness.

Desired output:

- 174 user-acquisition test plan;
- target user profile;
- offer / landing-page language;
- list of initial outreach targets;
- evidence log; and
- decision on whether user proof belongs in the sale package.

## Immediate Action List

1. Ask Crassula and FinLego whether 174 can buy a thinner non-core-banking
   package rather than full "core banking."
2. Request pricing and offer terms from Mambu Payments / Payments Hub.
3. Request pricing and offer terms from Toqio.
4. Confirm final pricing, connector availability, and sandbox / regulator-review terms from Crassula.
5. Request pricing and offer terms from SDK.finance.
6. Build the 174 product-software pricing grid.
7. Produce current RPAA application status note.
8. Identify at least two alternatives to the EUR 12,000 EMI offer.
9. Prepare EMI comparison grid.
10. Draft 174 user-acquisition / demand-proof test plan.
11. Decide whether minimum sale-readiness gate is satisfied after candidates,
    RPAA, EMI, and user-proof evidence are updated.

## Current Working Conclusion

The next phase for 174 is not more abstract strategy.

It is evidence capture:

- vendor pricing and offers;
- thinner non-banking package availability;
- RPAA status;
- EMI alternatives; and
- narrow user or demand proof.

Those are the materials that move 174 toward a buyer-readable sale package.
