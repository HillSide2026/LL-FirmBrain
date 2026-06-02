---
id: hbp-013-locarno-product
title: Locarno — Product Description
owner: ML1
status: draft
created_date: 2026-05-31
last_updated: 2026-05-31
tags: [locarno, product, payments, treasury, international, hbp-013, ontario-msb]
---

# Locarno — Product Description

## What Locarno Is

Locarno is an international payments and treasury platform operated from Canada. It is not a Canadian business banking platform. The Canadian regulatory layer is infrastructure — not the market position.

Locarno sits above a regulated EMI partner. The EMI holds and safeguards client funds, issues accounts, and executes payments. Locarno owns the customer relationship, onboarding workflow, product experience, and relationship management.

---

## The Offer

Multi-currency accounts, cross-border payments, FX, treasury functionality, stablecoin settlement, and safeguarded client funds — for businesses that operate in USD, EUR, GBP, AED, USDC rather than CAD.

---

## The Stack

```
Customer
    ↓
Locarno
(customer acquisition, experience, onboarding, product design, relationship management)
    ↓
EMI / Regulated Partner
(holding, safeguarding, custody of client balances, account issuance, payment execution)
    ↓
Safeguarded Funds / Accounts / Payment Rails
```

The entity does not hold customer funds. The regulated institution performs all activities requiring institutional credibility.

---

## Target Customer

Service businesses with international revenue and multi-currency exposure:

- Software development agencies
- Design agencies
- Marketing agencies
- Consulting firms
- Fractional CFO firms
- Recruiters
- Engineering consultants

These businesses receive foreign funds, hold multiple currencies, move money internationally, and want FX friction reduced.

**What they need:** receiving foreign funds, holding multiple currencies, moving money internationally, reducing FX friction.

**What they do not need:** Interac, EFT, Canadian bill pay, payroll integration.

---

## Regulatory Philosophy

Locarno is not attempting to become a bank or directly safeguard funds. It sits above regulated infrastructure providers.

`1001494374 Ontario Corp` provides the registration perimeter: FINTRAC MSB registration, RPAA compliance, AML control, customer risk governance. The entity owns the Canadian regulatory layer.

The EMI does not have to be Canadian. A reputable Lithuanian EMI, a UK EMI, a European embedded-finance provider, or a regulated payment institution may be more valuable than a Canadian payments partner. The critical infrastructure requirement is a credible institution that can legitimately hold and safeguard customer funds. ConnectPay (connectpay.com) is the current primary EMI target.

---

## Infrastructure Requirements

The critical requirement is not Canadian rails. It is:

- Multi-currency account issuance
- Inbound and outbound cross-border payments
- FX execution
- Safeguarding visibility and reporting
- Stablecoin settlement capability (where available)

---

## How Locarno Differs from Granville

| Dimension | Granville | Locarno |
|---|---|---|
| Entity | 17409052 Canada Inc (174) | 1001494374 Ontario Corp |
| Customer | Founders and small businesses outgrowing a single-provider integration | Service businesses with international treasury workflows |
| Problem solved | Provider portability and reconciliation | Multi-currency accounts, cross-border payments, FX friction |
| Competitive moat | Orchestration layer — provider portability, ledger integrity, reconciliation | Regulated layer — registration perimeter, direct institutional connectivity, compliance infrastructure |
| EMI model | Airwallex (primary, pending) — bank abstracted through EMI | ConnectPay (primary target) — EMI-centric, international |
| Rails emphasis | Provider routing and failover | International payments, FX, stablecoin |

---

## Relationship to `1001494374 Ontario Corp`

`1001494374 Ontario Corp` is the regulated entity. Locarno is the product that the entity enables. The entity provides the registration, compliance perimeter, and AML governance. Locarno provides the customer-facing product layer built on top of it.

This mirrors the 174 / Granville structure: the entity is the asset; the product is what the customer sees.

---

## Track Relevance

This product description is specifically relevant to Track B. Track A (pure MSB shell sale) does not require the Locarno product to be built. Track B builds toward this product thesis. Track C adds a direct sponsor-bank relationship on top of the EMI layer.
