---
id: 04_initiatives__hillside_portfolio__business_projects__hbp_011_payments_regulatory_compliance_agency__executing__workplan_md
title: Payments Regulatory & Compliance Consulting Agency - Executing Workplan
owner: ML1
status: active
created_date: 2026-03-20
last_updated: 2026-04-25
tags: [payments-regulatory-compliance-agency, executing, workplan]
---

# IMPLEMENTATION WORKPLAN

Project ID: `HBP-011`
Project Path: `04_INITIATIVES/HillSide_PORTFOLIO/BUSINESS_PROJECTS/HBP-011_PAYMENTS_REGULATORY_COMPLIANCE_AGENCY`
Stage: `Executing`

## Objective

Operationalize a narrow payment services compliance service under
`17513721 Canada Inc` with FinSure as the initial entry offer.

Buyer profile: same PSP / MSB profile as HBP-010.

## EW-01 — Service Packaging (LOCKED 2026-04-25)

Three service tiers:

| Tier | Name | Description |
|---|---|---|
| 1 | Readiness | RPAA / MSB compliance assessment |
| 2 | Build | AML and compliance program build |
| 3 | Ongoing | Advisory (recurring) |

## EW-02 — Pricing Design (LOCKED 2026-04-25)

- Model: fixed fee plus retainer
- Margin floor: 30% minimum
- Hourly billing is not the core model

## EW-03 — Scope Control (LOCKED 2026-04-25)

**In scope:** compliance infrastructure and advisory to Canadian PSPs and fintechs.

**Explicitly excluded:**
- No CAMLO role
- No regulatory filings
- No regulator representation
- No decision-making delegation

**Scope narrowing note (2026-04-25):** Prior approval record (2026-03-20) listed "CAMLO services" as part of the initial service model. This has been removed. FinSure provides tools and advisory only; CAMLO responsibility stays with the client.

## EW-04 — Second-Model Decision (LOCKED 2026-04-25)

**Decision: NO.** Infrastructure-focused CAMLO-support model (client supplies in-house CAMLO) is deferred. Not part of the current service set.

## EW-05 — FinSure Positioning (LOCKED 2026-04-25)

**Positioning statement:** "We provide compliance infrastructure and advisory to Canadian PSPs and fintechs."

**Business name:** FinSure (confirmed entry offer and brand).

**Public front-end:** finsure.dominionpartners.ca (within the Dominion Platform).

## FinSure Product Model (updated 2026-05-03)

FinSure is being built out as a landing page leading to a portal where clients access
the entry-level product, with an opt-in path to higher-ticket services.

**Funnel:**

```
finsure.dominionpartners.ca (landing page)
   ↓
Portal (authenticated client area)
   ↓
Entry-level product (compliance tool / assessment)
   ↓
Opt-in to higher-ticket services
```

**Infrastructure:**
- Prior build: `https://finsure-w321.onrender.com`
- Target domain: `https://finsure.dominionpartners.ca` (Vercel; DNS via CNAME to cname.vercel-dns.com)
- DNS authority: single Vercel team / account per Dominion Platform architecture
- Prior HostGator DNS blocker is superseded by the Dominion Platform Vercel deployment model

**Higher-ticket opt-in path (confirmed 2026-05-03):**

```
Tier 1 — FinSure entry product (this project)
   ↓
Tier 2 — Rhizome white label (HBP-010)
   ↓
Tier 3 — Managed compliance, including fractional CAMLO if and as required
   ↓
Tier 4 — Levine Law F03 regulatory advisory (premium tier; Levine Law entity only)
```

Tier 4 is a Levine Law service. Referral from tier 3 to tier 4 is a cross-entity step
requiring ML1 authorization per engagement. HBP-011 governs tiers 1 and 3. HBP-010
governs tier 2.

**CAMLO scope note:** EW-03 excluded CAMLO from the FinSure entry product (tier 1).
Fractional CAMLO at tier 3 (managed compliance) is a separate, higher-ticket offering
and does not reopen that exclusion. The tier 1 scope boundary is unchanged.

**Confirmed build decisions:**
- Portal authentication: shared via Dominion `packages/auth` module across FinSure and dominionpartners.ca (confirmed 2026-05-03)

**Open build questions:**
- Whether the existing finsure-w321.onrender.com build migrates to Vercel or is rebuilt — TBD

See `MATTHEW_HOLDINGS_17513721_CANADA_INC/DOMINION_PLATFORM/PLATFORM_ARCHITECTURE.md`
for the full Dominion deployment and DNS model.

## Control Notes

- The approved path is narrower than the original broad agency concept.
- FinSure is the entry offer; the landing page and portal extend this into a product funnel.
- Rhizome white-label or partner implementation work is outside `HBP-011` and belongs in `HBP-010`.
- Higher-ticket opt-in services require a separate scoped decision before activation.

## Change Log

- 2026-03-20 — Workplan created; execution priorities authorized
- 2026-04-25 — All five workstreams locked per ML1 working parameters; CAMLO scope removal recorded; FinSure positioning confirmed
- 2026-05-03 — Product model updated: landing page → portal → entry-level product → higher-ticket opt-in; Dominion Platform architecture adopted; DNS model updated to Vercel
