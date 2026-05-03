---
id: 04_initiatives__hillside_portfolio__matthew_holdings_17513721_canada_inc__dominion_platform__platform_architecture_md
title: Dominion Platform Architecture
owner: ML1
status: draft
created_date: 2026-05-03
last_updated: 2026-05-03
tags: [dominion, platform, architecture, 17513721, payments, flowsignal, d-airpay]
---

# Dominion Platform Architecture

**Entity owner:** 17513721 Canada Inc (Matthew Holdings)
**Last updated:** 2026-05-03

---

## 1. Core Structure

### Entity Ownership

All assets owned and controlled by 17513721 Canada Inc.

### Brand and Domain Hierarchy

| Brand | Domain | Role |
|---|---|---|
| Dominion | dominionpartners.ca | Branding and intake for enterprise clients |
| FlowSignal | flowsignal.dominionpartners.ca | Intelligence layer |
| D-AirPay | d-airpay.dominionpartners.ca | Monetization / payments execution |
| FinSure | finsure.dominionpartners.ca | Compliance product — landing page, portal, and entry-level product with upsell to higher-ticket services |

---

## 2. Functional Layering (System View)

```
Dominion (Root)
   ↓
FlowSignal (Intelligence / Distribution Layer)
   ↓
D-AirPay (Execution / Payments Layer)
```

### Layer Roles

**Dominion**
- Narrative and positioning layer
- Intake for enterprise clients

**FlowSignal**
- Market intelligence
- Partner and introducer interface

**D-AirPay**
- Payments execution layer
- Rails abstraction (fiat and stablecoin)

---

## 3. Repository Architecture

```
repos/
├── dominion
├── flowsignal
├── d-airpay
└── finsure
```

### Rules

- Each repo is an independent deployable unit
- No uncontrolled code duplication across repos
- Shared logic must be explicitly modularized:

```
packages/
├── ui
├── auth
└── types
```

---

## 4. Deployment Architecture (Vercel)

Each repo is deployed as a separate Vercel project.

| Repo | Vercel Project | Domain |
|---|---|---|
| dominion | dominion | dominionpartners.ca |
| flowsignal | flowsignal | flowsignal.dominionpartners.ca |
| d-airpay | d-airpay | d-airpay.dominionpartners.ca |
| finsure | finsure | finsure.dominionpartners.ca |

### DNS Configuration

| Record | Type | Value |
|---|---|---|
| @ | A | 76.76.21.21 |
| www | CNAME | cname.vercel-dns.com |
| flowsignal | CNAME | cname.vercel-dns.com |
| d-airpay | CNAME | cname.vercel-dns.com |
| finsure | CNAME | cname.vercel-dns.com |

---

## 5. Control Layer Requirements

To avoid system drift:

- Single DNS authority
- Single Vercel team / account
- Consistent environment variable naming
- Centralized secret management

---

## 6. Platform Decision

**Option A — Independent Apps (current direction)**

- No shared authentication
- No shared data layer
- Simple linking between products

---

## 7. Operational Principles

- Treat Dominion as intake for enterprise clients, not just a website
- Treat FlowSignal as distribution engine
- Treat D-AirPay as monetization infrastructure
- Avoid mixing responsibilities across repos
- Maintain clear separation between:
  - narrative (Dominion)
  - intelligence (FlowSignal)
  - execution (D-AirPay)

---

## 8. FinSure Product Model

FinSure is a compliance product for Canadian PSPs and fintechs, operated under
17513721 Canada Inc and governed by HBP-011.

**Funnel structure:**

```
finsure.dominionpartners.ca (landing page)
   ↓
Portal (authenticated)
   ↓
Entry-level product (compliance tool / assessment)
   ↓
Opt-in to higher-ticket services
```

**Product layers:**
- Landing page: conversion-focused; positions FinSure for the target buyer (PSP / MSB / fintech)
- Portal: authenticated client area; access to the entry-level product
- Entry-level product: the existing FinSure compliance tool (previously deployed at finsure-w321.onrender.com); to be re-hosted at finsure.dominionpartners.ca
- Higher-ticket opt-in path: four-tier upsell funnel (confirmed 2026-05-03):

```
Tier 1 — FinSure entry product (portal)
   ↓
Tier 2 — Rhizome white label (HBP-010)
   ↓
Tier 3 — Managed compliance (including fractional CAMLO if and as required)
   ↓
Tier 4 — Levine Law F03 regulatory advisory (premium tier; Levine Law entity)
```

**Governance note:** Tier 4 (Levine Law F03) is a Levine Law service, not a 17513721
Canada Inc service. The boundary between tiers 1-3 (17513721 Canada Inc) and tier 4
(Levine Law) must be maintained. Referral or handoff from tier 3 to tier 4 is a
deliberate cross-entity step requiring ML1 authorization per engagement.

**Confirmed decisions:**
- Portal authentication: shared via Dominion `packages/auth` module across FinSure and dominionpartners.ca (confirmed 2026-05-03)

**Open questions:**
- Whether the existing finsure-w321.onrender.com build migrates directly or is rebuilt — TBD

**Governing project:** HBP-011 (Payments Regulatory and Compliance Agency)

---

## Relationship to Prior Structure

The prior recorded structure (as of 2026-04-25) had a two-lane model:
- Lane 1: referral introductions to providers (Interpolitan, KwiikPay)
- Lane 2: FinSure as entry product at `finsure.dominionpartners.ca`

The three-tier Dominion / FlowSignal / D-AirPay architecture supersedes that model.
The status of FinSure and the prior HBP-010 (Rhizome White Label) and HBP-011
(Payments Regulatory Compliance Agency) in relation to this architecture is an
open question pending ML1 direction.
