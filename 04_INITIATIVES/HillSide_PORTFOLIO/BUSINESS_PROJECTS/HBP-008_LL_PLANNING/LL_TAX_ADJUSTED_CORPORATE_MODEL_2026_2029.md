---
id: 04_initiatives__hillside_portfolio__business_projects__hbp_008_ll_planning__ll_tax_adjusted_corporate_model_2026_2029_md
title: LL Planning - Tax-Adjusted Corporate Model 2026-2029
owner: ML1
status: draft
created_date: 2026-05-05
last_updated: 2026-05-05
tags: [levine-law, corporate-tax, retained-profit, deployable-capital, 2026, 2027, 2028, 2029, hillside]
---

# Tax-Adjusted Corporate Model 2026-2029

**Project:** LL Planning
**Project ID:** HBP-008

## Purpose

Translate the HBP-008 retained-profit shorthand into an LL-side corporate-tax
view.

This artifact asks one question only:

```text
After corporate tax, how much of Levine Law's nominal retained-profit line is
available as corporate deployable capital?
```

It does **not** model ML1's personal after-tax cash, household savings,
investment account refill, or HBP-001 wealth-plan outcomes.

## Boundary

In scope:

- Levine Law fee generation
- fixed and discretionary owner-revenue lines as already reflected in the
  retained-profit model
- estimated corporate tax on the remaining corporate retained profit
- after-tax deployable capital inside Levine Law

Out of scope:

- personal income tax payable by ML1
- salary vs dividend integration at the personal level
- RRSP, TFSA, RESP, household, mortgage, or investment allocation decisions
- HBP-001 net-worth or 2030 wealth-target modeling

## Tax Assumptions

This is a planning model, not tax advice.

Working assumption:

- Levine Law is modeled as an Ontario CCPC earning active business income.
- Modeled taxable active business income remains below the CAD 500,000 small
  business limit.
- No associated-corporation business-limit sharing, taxable-capital grind,
  passive-income grind, personal-services-business treatment, or refundable-tax
  account is modeled.
- Corporate tax is modeled at `12.2%`, equal to the federal small-business rate
  of `9.0%` plus the current Ontario lower small-business rate of `3.2%`.
- A sensitivity at `11.2%` is included because Ontario has announced a proposed
  lower small-business rate of `2.2%`; this model should not use that as the
  main rate until confirmed for the relevant taxation year by the accountant.

Official source anchors:

- Canada Revenue Agency corporation tax rates: federal CCPC small-business net
  tax rate `9%`
  (`https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/corporation-tax-rates.html`).
- Ontario corporate income tax page: Ontario lower small-business corporate
  income tax rate `3.2%` on the first CAD 500,000 of active business income
  (`https://www.ontario.ca/document/corporations-tax/corporate-income-tax`).
- Ontario 2026 Budget / Ontario Newsroom: proposed reduction of the Ontario
  lower small-business rate from `3.2%` to `2.2%`
  (`https://budget.ontario.ca/2026/annex.html`;
  `https://news.ontario.ca/en/release/1007250/ontario-cutting-small-business-tax-by-11-billion`).

## Calculation Rule

```text
estimated corporate tax = pre-tax retained profit x corporate tax rate
after-tax deployable capital = pre-tax retained profit - estimated corporate tax
```

The model applies tax only to the retained-profit line. Fixed owner revenue and
discretionary owner distribution are treated as already removed by the retained
profit model. Their personal tax effects are outside HBP-008.

## Main Model - Current 12.2% Assumption

| Year | Pre-tax retained profit case | Estimated corporate tax @ `12.2%` | After-tax deployable capital |
|---|---:|---:|---:|
| `2026` @ `30%` | `CAD 72,000` | `CAD 8,784` | `CAD 63,216` |
| `2026` @ `35%` | `CAD 84,000` | `CAD 10,248` | `CAD 73,752` |
| `2026` @ `40%` | `CAD 96,000` | `CAD 11,712` | `CAD 84,288` |
| `2027` floor @ `30%` | `CAD 92,000-97,000` | `CAD 11,224-11,834` | `CAD 80,776-85,166` |
| `2027` floor @ `35%` | `CAD 109,000-114,000` | `CAD 13,298-13,908` | `CAD 95,702-100,092` |
| `2027` floor @ `40%` | `CAD 126,000-131,000` | `CAD 15,372-15,982` | `CAD 110,628-115,018` |
| `2027` target @ `30%` | `CAD 110,000-115,000` | `CAD 13,420-14,030` | `CAD 96,580-100,970` |
| `2027` target @ `35%` | `CAD 130,000-135,000` | `CAD 15,860-16,470` | `CAD 114,140-118,530` |
| `2027` target @ `40%` | `CAD 150,000-155,000` | `CAD 18,300-18,910` | `CAD 131,700-136,090` |
| `2028` placeholder @ `30%` | `CAD 110,000` | `CAD 13,420` | `CAD 96,580` |
| `2028` placeholder @ `35%` | `CAD 130,000` | `CAD 15,860` | `CAD 114,140` |
| `2028` placeholder @ `40%` | `CAD 150,000` | `CAD 18,300` | `CAD 131,700` |
| `2029` placeholder @ `30%` | `CAD 105,000` | `CAD 12,810` | `CAD 92,190` |
| `2029` placeholder @ `35%` | `CAD 125,000` | `CAD 15,250` | `CAD 109,750` |
| `2029` placeholder @ `40%` | `CAD 145,000` | `CAD 17,690` | `CAD 127,310` |

## 2029 Path B Sensitivity

| `2029` Path B revenue case | Pre-tax retained profit | Estimated corporate tax @ `12.2%` | After-tax deployable capital |
|---|---:|---:|---:|
| `CAD 379,000` at `30%` | `CAD 98,700` | `CAD 12,041` | `CAD 86,659` |
| `CAD 359,000` at `35%` | `CAD 110,650` | `CAD 13,499` | `CAD 97,151` |
| `CAD 344,000` at `40%` | `CAD 122,600` | `CAD 14,957` | `CAD 107,643` |

## Rate Sensitivity - If 11.2% Applies

This table is included only to show the planning effect of a lower Ontario
small-business rate. It should remain a sensitivity until accountant-validated.

| Case | Pre-tax retained profit | After-tax deployable capital @ `12.2%` | After-tax deployable capital @ `11.2%` | Difference |
|---|---:|---:|---:|---:|
| `2027` floor @ `30%` | `CAD 92,000-97,000` | `CAD 80,776-85,166` | `CAD 81,696-86,136` | `CAD 920-970` |
| `2027` floor @ `40%` | `CAD 126,000-131,000` | `CAD 110,628-115,018` | `CAD 111,888-116,328` | `CAD 1,260-1,310` |
| `2027` target @ `30%` | `CAD 110,000-115,000` | `CAD 96,580-100,970` | `CAD 97,680-102,120` | `CAD 1,100-1,150` |
| `2027` target @ `40%` | `CAD 150,000-155,000` | `CAD 131,700-136,090` | `CAD 133,200-137,640` | `CAD 1,500-1,550` |

## Interpretation

- The tax adjustment does not break the 2027 model. Even under the current
  `12.2%` assumption, the `2027` floor case leaves approximately
  `CAD 80,776-115,018` of after-tax deployable corporate capital depending on
  retained-profit margin.
- The `2027` target case leaves approximately `CAD 96,580-136,090` of after-tax
  deployable corporate capital.
- The difference between the current `12.2%` assumption and the possible `11.2%`
  sensitivity is useful, but not strategically decisive at the modeled scale.
- The main decision variable is still operating performance and owner extraction
  discipline, not corporate tax rate sensitivity.

## Open Validation Items

ML1 / accounting validation required before this artifact is treated as
decision-grade:

- confirm Levine Law's current CCPC / active-business-income treatment
- confirm whether any associated-corporation business-limit sharing applies
- confirm whether any income should be excluded from small-business-rate
  treatment
- confirm the correct Ontario lower small-business rate for each taxation year
- confirm whether the retained-profit line in the source model maps cleanly to
  taxable income after accounting adjustments
- confirm whether corporate tax instalment timing affects available cash within
  the operating year

## Source Anchors

- `LL_RETAINED_PROFIT_MODEL_2026_2029.md`
- `REVENUE_MODEL.md`
- `ANNUAL_PLAN_2028.md`
- `ANNUAL_PLAN_2029.md`
- `../../../LL_PORTFOLIO/07_GROWTH_PROJECTS/LLP-030_FIRM_STRATEGY/SECOND_FEE_EARNER_2030_REVENUE_SENSITIVITY__2026-04-03.md`
