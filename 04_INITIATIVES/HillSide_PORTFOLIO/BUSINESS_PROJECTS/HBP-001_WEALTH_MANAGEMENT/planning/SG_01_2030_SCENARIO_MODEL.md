---
id: 04_initiatives__hillside_portfolio__business_projects__hbp_001_wealth_management__planning__sg_01_2030_scenario_model_md
title: Wealth Management - SG-01 2030 Scenario Model
owner: ML1
status: active
created_date: 2026-04-03
last_updated: 2026-06-07
tags: [wealth-management, planning, scenario-model, sg-01]
---

# SG-01 2030 Scenario Model

Project ID: `HBP-001`
Stage: `Planning`

## Planning Use

Use this file to test what level of net savings from business income is
required to achieve SG-01 under different investment-return assumptions.

## Fixed Assumptions

- visible liquid / near-liquid baseline: approximately `CAD 1,487,000+`,
  consisting of `CAD 1,460,000` personal liquid / near-liquid assets as at
  `2026-04-03` plus `CAD 27,000+` entity-bound cash inside 175 from the
  completed YellowBricks sale
- prior `CAD 1,600,000` planning anchor is treated as an unreconciled reference,
  not the current authoritative hard balance
- SG-01 target: consolidated net worth of at least `CAD 2,000,000` by
  `2030-12-31`
- return scenarios tested: `4%`, `6%`, and `8%` nominal annual return on the
  investment base
- model convention: monthly compounding from `2026-04-01` through
  `2030-12-31` (`57` months)
- business-income savings are modeled as monthly additions to the base
- no housing deployment, no new major liabilities, no extraordinary tax drag,
  and no large valuation reset are assumed in this scenario view
- the scenario uses `CAD 1,487,000` as the conservative visible base; unresolved
  business-equity values, liabilities, and taxes are not modeled

## Endpoint Sensitivity

| Return Scenario | Base-Only Value at `2030-12-31` | Position vs SG-01 | Required Net Savings from Business Income if Started in `2026-04` | Annualized Equivalent |
| --- | --- | --- | --- | --- |
| `4%` | `CAD 1,791,510` | short by `CAD 208,490` | about `CAD 3,333` per month | about `CAD 39,996` per year |
| `6%` | `CAD 1,961,164` | short by `CAD 38,836` | about `CAD 593` per month | about `CAD 7,114` per year |
| `8%` | `CAD 2,143,255` | above target by `CAD 143,255` | `CAD 0` | `CAD 0` |

## More Realistic Planning Lens

The current packet already says 2026 net savings from business income are near
zero. The table below therefore shows the average annual savings requirement if
`2026` contributes no additional business-income savings but the investment base
still compounds through the rest of `2026`.

| Return Scenario | Required Net Savings from Business Income During `2027-2030` | Monthly Equivalent Across `2027-2030` |
| --- | --- | --- |
| `4%` | about `CAD 48,219` per year | about `CAD 4,018` per month |
| `6%` | about `CAD 8,642` per year | about `CAD 720` per month |
| `8%` | `CAD 0` | `CAD 0` |

## Base-Only Year-End Path

| Year-End | `4%` Return | `6%` Return | `8%` Return |
| --- | --- | --- | --- |
| `2026-12-31` | `CAD 1,531,391` | `CAD 1,553,425` | `CAD 1,575,356` |
| `2027-12-31` | `CAD 1,592,646` | `CAD 1,646,631` | `CAD 1,701,385` |
| `2028-12-31` | `CAD 1,656,352` | `CAD 1,745,429` | `CAD 1,837,496` |
| `2029-12-31` | `CAD 1,722,606` | `CAD 1,850,154` | `CAD 1,984,495` |
| `2030-12-31` | `CAD 1,791,510` | `CAD 1,961,164` | `CAD 2,143,255` |

## Interpretation

1. Under a `4%` investment-return path, meaningful business-income savings are
   required to achieve SG-01.
2. Under `6%`, modest business-income savings are required on the visible base
   unless unresolved business-equity value closes the gap.
3. Under `8%`, SG-01 is achieved on the visible base alone.
4. Even where the math says `CAD 0`, business-income savings still matter
   strategically because they reduce dependence on market performance, improve
   housing flexibility, and create refill capacity after capital deployment.

## Working `4%` Staircase

The current working low-return planning staircase, while keeping `2026` net
savings at approximately zero, is:

| Year | Working Net Savings from Business Income |
| --- | --- |
| `2026` | `CAD 0` |
| `2027` | `CAD 7,000` |
| `2028` | `CAD 14,000` |
| `2029` | `CAD 21,000` |
| `2030` | `CAD 28,000` |

That staircase reaches approximately `CAD 2,001,833` by `2030-12-31` in the
`4%` case. It should be treated as the current planning reference for the
low-return scenario, not yet as a locked operating budget.

## Gross-Up To Pre-Tax Business Income

If the business-income funds must be paid to Matthew personally and taxed before
they become personal savings, the staircase above has to be grossed up.

For clarity, this gross-up is for combined pre-tax business income to Matthew.
That combined inflow may include compensation, bonus, dividends, and approved
distributions from Levine Law and `17513721 Canada Inc`, not only Levine Law.

This planning gross-up uses the following simplifying assumptions:

- Ontario resident
- ordinary personal taxable income
- `CAD 80,000` of annual pre-tax business income is enough to cover lifestyle
- gross-up measured as the additional pre-tax income required so that
  after-tax income above the `CAD 80,000` lifestyle base equals the target net
  savings
- 2026 federal and Ontario personal income tax rates, Ontario surtax, Ontario
  health premium, and basic personal credits are reflected
- CPP, EI, dividend-tax integration, and other personal deductions or credits
  are not reflected in this planning table

| Year | Working Net Savings from Business Income | Required Combined Pre-Tax Business Income to Matthew | Increment Above `CAD 80,000` Lifestyle Base |
| --- | --- | --- | --- |
| `2026` | `CAD 0` | `CAD 80,000` | `CAD 0` |
| `2027` | `CAD 7,000` | about `CAD 89,950` | about `CAD 9,950` |
| `2028` | `CAD 14,000` | about `CAD 100,034` | about `CAD 20,034` |
| `2029` | `CAD 21,000` | about `CAD 110,340` | about `CAD 30,340` |
| `2030` | `CAD 28,000` | about `CAD 121,569` | about `CAD 41,569` |

Rounded planning shorthand:

- `2027`: about `CAD 90,000`
- `2028`: about `CAD 100,000`
- `2029`: about `CAD 110,000` to `CAD 111,000`
- `2030`: about `CAD 122,000`

These are planning gross-up figures, not payroll-ready numbers. If the actual
cash is paid as salary, CRA payroll deductions may move the required gross
slightly. If the actual cash is paid as dividends or another form of
distribution, a different tax model is required.

## Planning Consequence

The immediate need is not to assume aggressive business-income growth. The
current low-return reference path is the working `4%` staircase above. The next
decision is how much weight the broader plan should place on:

- a low-savings `4%` path that still requires some business-income improvement
- a market-dependent `6%` base case with little or no required savings for
  SG-01
- a stronger-return case that creates cushion but should not be treated as the
  only acceptable plan
