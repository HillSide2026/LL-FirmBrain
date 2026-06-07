---
id: 04_initiatives__hillside_portfolio__business_projects__hbp_001_wealth_management__planning__opening_balance_sheet_md
title: Wealth Management - Opening Balance Sheet
owner: ML1
status: active
created_date: 2026-04-03
last_updated: 2026-06-07
tags: [wealth-management, planning, balance-sheet]
---

# Opening Balance Sheet

Project ID: `HBP-001`
Stage: `Planning`

## Planning Use

Use this file to document the opening consolidated balance-sheet view used by
the wealth plan. The purpose is decision usefulness, not false precision.

## Baseline Dates

- prior unreconciled planning anchor: `2026-03-23`
- current visible liquid / near-liquid input: `2026-04-03`
- YellowBricks closing confirmation: `2026-04-29`

## Working Baseline Table

| Line Item | Classification | Working Value / Status | Evidence / Basis | Decision-Use Treatment |
| --- | --- | --- | --- | --- |
| High-interest savings account | `U1` unrestricted liquid | `CAD 900,000` reported by ML1 as at `2026-04-03` | ML1 direct planning input | counts toward liquid capital subject to reserve rules |
| Managed equities | `U2` market-valued near-liquid | `CAD 560,000` reported by ML1 as at `2026-04-03` | ML1 direct planning input | counts toward decision use only after valuation date, market volatility, and liquidation assumptions are acknowledged |
| `17513721 Canada Inc` bank account | `R1` entity-bound liquid | slightly more than `CAD 27,000` received from the completed YellowBricks sale | HBP-003 closing report, ML1 direct planning input, `HBP-002_CASH_FLOW`, and `17513721 Canada Inc` identity records | excluded from personal deployable-capital calculations unless deliberately distributed or otherwise released across the entity boundary |
| Visible liquid / near-liquid subtotal | `U1/U2/R1` mixed personal and entity-bound liquidity | approximately `CAD 1,487,000+` as at current planning inputs (`CAD 1,460,000` personal plus `CAD 27,000+` inside 175) | line items above | current hard planning baseline before liabilities, taxes, and unresolved entity valuations |
| Prior cash and securities planning anchor | reconciliation item | first-pass `CAD 1,600,000` as at `2026-03-23`; not treated as the current authoritative hard balance | `METRICS.md` and `HBP-002_CASH_FLOW/README.md` | superseded for hard-balance purposes until the approximately `CAD 113,000` delta is reconciled or the anchor is retired |
| `Levine Professional Corporation` equity (`Levine Law`) | `I1` illiquid strategic equity | valuation unresolved | internal ownership and performance records | excluded from deployable-capital calculations until valuation policy is locked |
| `17513721 Canada Inc` equity and other personally owned venture equity, excluding separately listed corporate cash | `I1` illiquid strategic equity | valuation unresolved | internal records | included in long-term wealth framing, excluded from housing budgets |
| Ontario MSB sale thesis | `C1` conditional asset | optimistic sale case exists; not realized | `HBP-002_CASH_FLOW/README.md` | carried at zero for deployable-capital decisions until realized or legally committed |
| YellowBricks ownership value | divested asset | zero; YellowBricks has been sold and is gone | HBP-003 closing report | no ongoing asset value; only the realized `CAD 27,000+` cash proceeds inside 175 remain in the balance-sheet view |
| Federal MSB entity value | `I1/C1` illiquid / conditional | unresolved | internal records | carried at zero for deployable-capital decisions |
| Liabilities, taxes, and known obligations | `L1` liability | to be consolidated explicitly | accounting records and `HBP-002_CASH_FLOW` source mapping | must be deducted before any housing budget is treated as valid |

## Reconciliation Note

The current hard balance-sheet view is `CAD 1,460,000` personal liquid /
near-liquid input as at `2026-04-03` (`CAD 900,000` in a high-interest savings
account plus `CAD 560,000` in managed equities), plus slightly more than
`CAD 27,000` in `17513721 Canada Inc` from the completed YellowBricks sale.

The older `CAD 1,600,000` figure should not be read as money that moved down to
`CAD 1,460,000`. It was a first-pass planning anchor from `2026-03-23`. The
visible current subtotal is approximately `CAD 1,487,000+`, leaving an
approximately `CAD 113,000` reconciliation gap against the old anchor until
source records explain the difference or the old anchor is retired.

ML1 has confirmed personal ownership of `17513721 Canada Inc` and
`Levine Professional Corporation`. That ownership fact does not collapse the
entity boundaries for accounting or cash-flow treatment.

## Decision Rule

Housing budgets are not built from total baseline value. They are built from
unrestricted liquid capital after reserves, taxes, and committed obligations are
deducted.
