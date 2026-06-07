---
id: 04_initiatives__hillside_portfolio__business_projects__hbp_001_wealth_management__planning__metrics_md
title: Wealth Management - Metrics
owner: ML1
status: active
created_date: 2026-03-20
last_updated: 2026-06-07
tags: [wealth-management, planning, metrics]
---

# Metrics

Project ID: `HBP-001`
Stage: `Planning`

## Planning Exit Metrics

| Metric | Definition | Target | Evidence |
| --- | --- | --- | --- |
| Baseline completeness | Share of in-scope assets and liabilities classified under one approved methodology | all material in-scope items classified | `SCOPE_STATEMENT.md`, `OPENING_BALANCE_SHEET.md`, `VALUATION_AND_CLASSIFICATION_POLICY.md` |
| Current visible liquid / near-liquid baseline | Personal liquid / near-liquid assets plus entity-bound YellowBricks sale proceeds inside 175 | approximately CAD 1,487,000+ (`CAD 1,460,000` personal plus `CAD 27,000+` inside 175), before liabilities, taxes, and unresolved entity valuations | `OPENING_BALANCE_SHEET.md`, ML1, HBP-003 closing report |
| Prior planning anchor reconciliation | Difference between the older `2026-03-23` first-pass anchor and the current visible hard baseline | prior CAD 1,600,000 anchor is retained only as an unreconciled reference; approximately CAD 113,000 delta remains to be explained or the anchor retired | `OPENING_BALANCE_SHEET.md`, `HBP-002_CASH_FLOW` source mapping |
| Conservative visible-baseline gap to SG-01 | CAD 2,000,000 minus approximately CAD 1,487,000+ | approximately CAD 513,000 before unresolved business-equity value and liabilities/taxes are finalized | `OPENING_BALANCE_SHEET.md`, `PROJECT_PLAN.md` |
| Conservative visible-baseline gap to SG-02 | CAD 4,000,000 minus approximately CAD 1,487,000+ | approximately CAD 2,513,000 before unresolved business-equity value and liabilities/taxes are finalized | `OPENING_BALANCE_SHEET.md`, `PROJECT_PLAN.md` |
| Governance readiness | Capital-allocation, liquidity, refill, and review rules are explicit enough to govern execution | governance rules documented clearly enough for ML1 review | `LIQUIDITY_AND_CAPITAL_GUARDRAILS.md`, `NET_SAVINGS_AND_REFILL_MODEL.md`, `COMMUNICATION_PLAN.md`, `WEALTH_PLAN.md` |
| Housing budget anchor | Shared housing-budget rules exist for Toronto and Japan planning | one housing-budget policy and output standard documented clearly enough for ML1 review | `HOUSING_BUDGET_POLICY.md`, `WEALTH_PLAN.md` |
| Dependency alignment | Critical dependencies needed for execution are identified and narrowed enough to manage | no unresolved dependency that makes the path unusable for decision-making | `DEPENDENCIES.md`, `RISK_REGISTER.md` |
| ML1 gate readiness | The planning packet is complete enough for a `Planning -> Executing` decision | all required planning artifacts drafted and coherent | planning folder and `../APPROVAL_RECORD.md` |

## Business Income Vs Investment Income

The wealth model has two distinct lanes. They must be tracked separately
because they answer different planning questions.

| Lane | Current State | Planning Use |
|--------|-------------|---------------------|
| Investment income and return on capital | The visible liquid / near-liquid base is approximately `CAD 1,487,000+` before unresolved valuations and liabilities/taxes; return requirements should be recalculated after the baseline is reconciled | Shows how the current balance sheet compounds over time |
| Business income to Matthew | This lane includes compensation, bonus, dividends, and approved distributions to Matthew from Levine Law and `17513721 Canada Inc`. The current explicit baseline locks Levine Law -> Matthew at `CAD 80,000`; no recurring `17513721 Canada Inc` -> Matthew distribution is yet assumed in the baseline. | Shows whether the liquid base can be refilled through owner cash flow rather than market performance |

**Current position:** business income to Matthew approximately covers living
costs, so net savings from business income are near zero. That means the
current path still depends mostly on investment income and compounding on the
existing base. This is viable for SG-01 if returns cooperate, but it leaves
less margin for return shortfalls and does not materially accelerate SG-02.

**What changes this:** If business income to Matthew rises enough to generate
net annual savings of `CAD 50,000`-`75,000` from 2027 onward, the combined
effect of savings plus compounding meaningfully reduces dependence on hitting
investment-return targets and accelerates SG-02.

**Where the business-income improvement is expected to come from:** `HBP-008`
(LL Planning) and `HBP-009` (2027 Business Ideas) remain the main growth
projects. Any recurring `17513721 Canada Inc` -> Matthew distributions should
also be documented in `HBP-002_CASH_FLOW` rather than assumed informally.

**Scenario note:** `SG_01_2030_SCENARIO_MODEL.md` now shows that the strict
business-income savings requirement for SG-01 is modest in the `4%` case and
zero in the `6%` and `8%` cases. Larger savings targets still matter if ML1
wants more cushion, less market dependence, or more housing flexibility.

---

## Measurement Rule

Planning is not complete when the goal is merely restated more elegantly.
Planning is complete only when the baseline, target gap, governance rules, and
dependency picture are specific enough for ML1 to authorize controlled
execution.
