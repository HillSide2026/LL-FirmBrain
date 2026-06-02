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

Three candidates identified for the stablecoin settlement layer of the Granville product:

| Candidate | Notes |
|---|---|
| Kwiikpay | Stablecoin partner candidate — role and terms TBD |
| RamPay | Stablecoin partner candidate — role and terms TBD |
| Marklane (marklane.io) | Stablecoin partner candidate — role and terms TBD |

These are candidates for the stablecoin settlement capability in the Granville product layer. They are distinct from the EMI (Airwallex) and core banking software vendors (FinLego, Crassula).

A stablecoin partner is relevant only if it supports the licensed-entity sale thesis — i.e., demonstrates a credible payment rail for buyer diligence, does not create non-transferable lock-in, and does not push 174 into operating meaningful stablecoin volume before sale.

ML1 to determine which candidates to engage and in what sequence.

## Minimum Acceptable Vendor Use Case

A vendor package is relevant only if it helps one or more of:

- FINTRAC / RPAA credibility
- EMI visibility
- buyer diligence
- transferability
- market-ready presentation of the licensed entity

If it mainly pushes 174 toward operating or marketing BaaS services, it is out
of scope for this project.
