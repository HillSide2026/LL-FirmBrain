---
id: llp-030_financial_model_doc
title: Levine Law — Financial Model
owner: ML1
status: draft
created_date: 2026-03-17
last_updated: 2026-05-20
tags: [llp-030, financial-model, financial-authority, strategy-to-finance]
---

# Levine Law — Financial Model

## Authority

`FINANCIAL_MODEL.md` is the financial authority for `LLP-030`.

It is the strategy-to-finance bridge. It translates the firm's strategic
choices into financial tests, constraints, scenarios, and decision gates.

This authority is contingent on accounting reality. The financial model must be
adjusted when accounting facts, collections, WIP, AR, entity treatment,
payment timing, matter economics, or capacity evidence show that an assumption
is wrong or incomplete.

The model may guide strategic and operating judgment, but it does not override:

- accounting actuals;
- trust and operating-cash treatment;
- collected cash;
- ML1 approval;
- professional obligations;
- `LLP-002` annual budget control.

## Current Status

Status: draft financial authority, not yet fully decision-useful.

The model is authoritative as the financial bridge for LLP-030, but several
inputs still require validation before the model can be treated as complete:

- average matter value by channel and service type;
- lead-to-consult and consult-to-retained conversion rates;
- contribution margin by matter type;
- leverage economics for setter, associate, or second fee earner;
- Andersen cross-entity crediting and reconciliation method.

## Relationship to Financial Management

This document consumes the current owner compensation target and approved
budget-control assumptions defined in
`04_INITIATIVES/LL_PORTFOLIO/01_FINANCIAL_MANAGEMENT/LLP-002/`.

`LLP-002` answers whether annual revenue, spend, margin, and control
targets are approved for the operating year.

`FINANCIAL_MODEL.md` answers whether the strategy works financially:

- whether the market-position strategy converts into cash, margin, and
  enterprise value;
- whether matter quality is improving;
- whether channel economics justify continued investment;
- whether recurring revenue is real, committed, and collectible;
- whether staffing or leverage can be supported;
- whether the Tier 8 to Tier 5 climb is producing better financial structure,
  not merely visibility.

## Accounting-Reality Rule

Financial-model assumptions must be reconciled against accounting reality.

If actual collections, WIP conversion, AR aging, trust-transfer timing, channel
performance, matter value, or cross-entity receipts differ from the model, the
model must change. The model cannot preserve a strategic story by ignoring the
money facts.

Operational Andersen matters are tracked inside Levine Law because they follow
the same time-for-money model. In the 2026 operating picture, the Andersen
relationship is credited to Levine Law even though Andersen fee receipts land
in `17513721 Canada Inc` and therefore require explicit cross-entity
reconciliation.

The live planning risk is not whether Andersen should count toward Levine Law
at all, but whether the crediting and reconciliation method causes omission,
misclassification, or double counting in the model.

Historical channel note for downstream interpretation: ML1 reports that, with
the specific exceptions of `Mascore` and `Stream`, `2025` matters originated
through `F01 / Google Ads`. Directionally, `F01`-generated revenue in `2025`
appears to have significantly exceeded `F01` spend. The strategic issue with
`F01` is therefore not absence of revenue contribution, but that it produces
more reactive, lower-fit, and less controllable demand than the desired future
mix.

## Core Model Logic

This document models the path from:

**Market position → channel activity → matter quality → revenue → cash →
margin → reserves → capacity → enterprise value**

It also contains the narrower P&L logic linking:

**Marketing spend → matter volume → revenue → margin**

## Input Assumptions

| Input | Current Value | Source | Validated? |
|---|---|---|---|
| F01 Google Ads spend | $1,500/month | Current | Yes |
| 2025 F01 economic contribution | F01-generated revenue appears to have significantly exceeded F01 spend; almost all 2025 matters originated through F01 except `Mascore` and `Stream` | ML1 historical observation | Directionally yes — exact historical reconciliation still needed |
| Lead → consult conversion | 25–30% | Estimated | No — needs 30-day data |
| Consult → retained conversion | 40–50% | Estimated | No |
| Average matter value (F01) | Unknown — soft floor set at $1,000 | LLP-030 decision 2026-03-22 | Floor confirmed; average TBD — needs 30-day data |
| Average matter value (F02) | $1,500–$2,500 (Health Check entry) | Hypothesis | Not yet launched |
| Owner salary | $72,000 | LLP-002 `BUDGET_2026.md` | Yes |
| Owner bonus target | $8,000 | LLP-002 `BUDGET_2026.md` | Yes |
| Total owner compensation | $80,000 | LLP-002 `BUDGET_2026.md` | Yes |
| Overhead | $40,000–$50,000/year | Budget Scenario 1 | Yes |
| Andersen operating credit | Included in Levine Law operating picture; cash lands in `17513721 Canada Inc` | Cross-entity rule | Partially — crediting direction is set, reconciliation method still needs to be locked |

## P&L Projection by Target / Reference Case

Reference cases for planning:

| Case | Target Revenue | Marketing Spend | Owner Compensation | Overhead | Projected Margin |
|---|---|---|---|---|---|
| Reference floor | $200,000 | TBD | $80,000 | $40–50k | TBD |
| Current operating target | $240,000 | TBD | $80,000 | TBD | TBD |

## Staffing Impact Model

| Addition | Annual Cost (Est.) | Revenue Required to Absorb | Capacity Unlocked |
|---|---|---|---|
| Setter | TBD | TBD | Frees ML1 from intake; improves lead → consult conversion |
| Senior Lawyer (delivery) | TBD | TBD | Extends matter delivery capacity; enables volume growth |

## Break-Even Analysis

*To be completed with ML1 input on matter value floor.*

---

Key open items before this model is fully decision-useful: (1) validate average
matter value by channel; (2) validate conversion rates with actual data; (3)
lock Andersen cross-entity reconciliation; (4) quantify leverage economics.
