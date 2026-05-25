---
id: llp_030__second_fee_earner_2030_revenue_sensitivity__2026_04_03
title: LLP-030 Note — Second Fee Earner 2030 Revenue Sensitivity
owner: ML1
status: draft
created_date: 2026-04-03
last_updated: 2026-04-03
tags: [llp-030, financial-model, staffing, sensitivity]
---

# LLP-030 Note — Second Fee Earner 2030 Revenue Sensitivity

## Purpose

Save a simple planning shorthand for the question:

If Levine Law's current baseline is `CAD 240,000` of revenue to support
`CAD 80,000` of owner compensation, how much total firm revenue would be needed
to support the `2030` owner-income target if all revenue above `CAD 240,000` is
billed by a second fee earner?

This is a sensitivity note, not a full financial model.

## Inputs

### 1. Current Levine Law baseline

- Current working baseline: `CAD 240,000` revenue supports `CAD 80,000` of
  owner compensation.

### 2. `2030` owner-income target

- `SG_01_2030_SCENARIO_MODEL.md` currently shows required pre-tax business
  income in `2030` of about `CAD 121,569`, rounded planning shorthand:
  `CAD 122,000`.

### 3. Increment above current base

- Increment above current `CAD 80,000` base:
  `CAD 121,569 - CAD 80,000 = CAD 41,569`

## Formula

Let:

- `B = CAD 240,000` current base revenue
- `T = CAD 121,569` target owner income in `2030`
- `C = CAD 80,000` current owner-compensation base
- `M = contribution margin on second fee earner billings`

Then:

- Incremental owner income required: `T - C`
- Incremental revenue required from second fee earner: `(T - C) / M`
- Total required firm revenue: `B + ((T - C) / M)`

Working shorthand:

```text
Total required revenue
= 240,000 + (41,569 / M)
```

## Sensitivity Table

| Second fee earner contribution margin | Extra revenue required above `CAD 240,000` | Total firm revenue required |
| --- | ---: | ---: |
| `30%` | `CAD 138,563` | `CAD 378,563` |
| `35%` | `CAD 118,769` | `CAD 358,769` |
| `40%` | `CAD 103,923` | `CAD 343,923` |

Rounded planning shorthand:

- `30%` margin -> about `CAD 379,000`
- `35%` margin -> about `CAD 359,000`
- `40%` margin -> about `CAD 344,000`

## Interpretation

- If the second fee earner is only a `30%` contributor after compensation and
  related delivery cost, the firm likely needs roughly `CAD 379,000` of total
  revenue to support the `2030` owner-income target.
- If the second fee earner contributes `35%`, the required total revenue drops
  to about `CAD 359,000`.
- If the second fee earner contributes `40%`, the required total revenue drops
  further to about `CAD 344,000`.

## Boundaries And Caveats

- This note assumes the first `CAD 240,000` of revenue continues to support the
  current `CAD 80,000` owner-compensation base.
- It assumes all incremental owner-income support above that base is funded by
  contribution from revenue billed by a second fee earner.
- It is not a complete firm P&L. It does not yet price:
  - actual senior-lawyer compensation structure
  - supervision burden
  - additional intake or support staffing
  - overhead changes from leverage
  - pricing changes or matter-mix changes
- It is therefore a planning shortcut for `LLP-030`, not an approved staffing
  decision rule.

## Source Anchors

- `LLP-002/BUDGET_2026.md`
- `LLP-030/FINANCIAL_MODEL.md`
- `HBP-001_WEALTH_MANAGEMENT/planning/SG_01_2030_SCENARIO_MODEL.md`
