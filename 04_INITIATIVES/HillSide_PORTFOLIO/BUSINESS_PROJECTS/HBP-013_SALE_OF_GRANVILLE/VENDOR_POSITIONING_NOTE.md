---
id: hbp-013-vendor-positioning-note
title: Vendor Positioning Note — HBP-013 — Sale of Granville
owner: ML1
status: draft
created_date: 2026-05-19
last_updated: 2026-05-19
tags: [hillside, hbp-013, granville, vendors, positioning]
---

# Vendor Positioning Note

Project: `HBP-013` - Sale of Granville

## Purpose

Record the current vendor takeaway inside the project folder itself.

The project is not selling BaaS services.

The project is licensing `17409052 Canada Inc`, making the licensed entity
market-ready, and eventually selling the licensed entity.

## FinLego

Current read:

- quoted "core banking"
- useful modules discussed: UI, fiat accounts, EUR / GBP / USD
- banking access described through Kanzum
- Kanzum does not solve RPAA safeguarding
- current pricing indication is cheaper than Crassula, but the structural issue
  remains

Project relevance:

- software may be relevant only as support for the licensed-entity story
- the "banking" framing is not itself the target product

## Crassula

Current read:

- quoted software plus connectors
- useful modules discussed: UI, fiat accounts, EUR / GBP / USD
- stronger point is broad EMI connector list
- sandbox availability for regulator review may be valuable
- current pricing indication is more expensive than FinLego

Project relevance:

- connector depth or sandbox utility may matter if they improve the licensed
  entity's credibility
- software breadth is not valuable just because it sounds bigger

## Correct Vendor Question

Do not ask:

- quote us more core banking

Ask:

- what is the minimum thinner package that supports licensing credibility,
  market-ready posture, and eventual sale of the licensed entity?

## Stablecoin Partners

Three candidates for the stablecoin settlement layer of the Granville product:

| Candidate | Status | Notes |
|---|---|---|
| Kwiikpay | Contracted | Agreement in place |
| RamPay | Unknown | Not yet engaged; status TBD |
| Marklane (marklane.io) | Evaluated | Terms appear competitive to Kwiikpay; see model note below |

### Kwiikpay

Contracted. Kwiikpay is the current primary stablecoin partner. Terms on file.

### RamPay

Status unknown. Not yet engaged. To be assessed if additional stablecoin rail is needed.

### Marklane (marklane.io)

Terms evaluated. Marklane operates a professional-ownership revenue-share model:

- **Client ownership:** belongs to the Professional (Granville / ML1 retains the client relationship)
- **Compensation:** 51%+ of revenue in perpetuity. Average is 51%+; specific rate varies by product.

This model is structurally different from a typical infrastructure provider — Marklane is a white-label revenue-share arrangement where the professional owns the client. Competitive to Kwiikpay on terms. May be relevant as a secondary rail or alternative if Kwiikpay terms prove limiting.

Open question: does the Marklane client-ownership and perpetual revenue-share structure travel cleanly on a share sale of 174? Transferability and assignment must be confirmed before Marklane is counted as an asset.

### Stablecoin Partner Positioning Rule

A stablecoin partner is relevant only if it:
- demonstrates a credible payment rail for buyer diligence
- does not create non-transferable lock-in
- does not push 174 into operating meaningful stablecoin volume before sale
- supports clean transferability on a share sale

## Minimum Acceptable Vendor Use Case

A vendor package is relevant only if it helps one or more of:

- FINTRAC / RPAA credibility
- EMI visibility
- buyer diligence
- transferability
- market-ready presentation of the licensed entity

If it mainly pushes 174 toward operating or marketing BaaS services, it is out
of scope for this project.
