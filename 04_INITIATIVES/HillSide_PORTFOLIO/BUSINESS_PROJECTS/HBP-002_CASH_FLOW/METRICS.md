---
id: 04_initiatives__hillside_portfolio__business_projects__hbp_002_cash_flow__metrics_md
title: Cash Flow - Metrics
owner: ML1
status: draft
created_date: 2026-03-20
last_updated: 2026-06-07
tags: [cash-flow, metrics, initiating]
---

# Metrics

Project ID: `HBP-002`
Stage: `Initiating`

## Primary SMART Goal

By `2026-06-30`, Matthew has a monthly management-reporting pack,
closed and reviewed within 10 business days of month-end, that reports:

- gross cash inflows to Matthew from each in-scope entity
- gross cash outflows from Matthew to each in-scope entity
- net cash flow by entity and in aggregate across the in-scope set
- completed YellowBricks sale-proceeds cash activity already received into `17513721 Canada Inc`

## In-Scope Reporting Boundary

- all positive and negative cash flow between Matthew and `17513721 Canada Inc`
- classification of the completed YellowBricks sale proceeds and any historical sale-related cash events already reflected in `17513721 Canada Inc`
- all positive and negative cash flow between Matthew and Federal MSB (`17409052 Canada Inc`)
- all positive and negative cash flow between Matthew and Ontario MSB Corp (`1001494374 Ontario Corp`)
- all positive and negative cash flow between Matthew and `Levine Professional Corporation` (`Levine Law`)

## Metric Definitions

| Metric | Definition | Core Formula | Primary Source |
| --- | --- | --- | --- |
| Matthew gross inflow by entity | Total cash received by Matthew from one in-scope entity during the reporting period | sum of all in-scope cash receipts from the entity to Matthew | Matthew cash-account records, entity bank statements, general ledger, payroll/distribution/loan records |
| Matthew gross outflow by entity | Total cash paid by Matthew to one in-scope entity during the reporting period | sum of all in-scope cash payments from Matthew to the entity | Matthew cash-account records, entity bank statements, general ledger, capital/loan records |
| Matthew net cash flow by entity | Net cash impact on Matthew from one in-scope entity during the reporting period | Matthew gross inflow by entity less Matthew gross outflow by entity | same sources as the related inflow and outflow measures |
| Consolidated Matthew net cash flow | Aggregate net cash impact on Matthew across the full in-scope entity set | sum of Matthew net cash flow by entity | monthly management pack, reconciliation schedule, source ledgers |
| YellowBricks sale-proceeds cash flow | Completed sale proceeds received into `17513721 Canada Inc` | YellowBricks sale proceeds received less any documented sale-related costs already reflected in 175 records | HBP-003 closing report, closing statements, bank records, legal close-out file |

## Reporting Rules

- Both positive and negative cash movements are in scope.
- In-scope movement types include distributions, compensation, reimbursements, loans, capital contributions, sale proceeds, post-closing costs, and other direct cash transfers between Matthew and an in-scope entity.
- Unrealized gains and losses are excluded from cash-flow and free-cash-flow metrics.
- Intercompany transfers that do not create a cash movement to or from Matthew are excluded from the primary metric view and may be shown only for reconciliation.
- Supporting entity-level operating or free-cash-flow views may be calculated separately if needed to explain Matthew-level movements, but they do not define the primary project boundary.
- Andersen Service Line activity must be reconciled across two layers: cash receipt in `17513721 Canada Inc` and operational matter tracking inside Levine Law.
- In the 2026 operating picture, the Andersen relationship is credited to Levine Law even though the cash receipt remains in `17513721 Canada Inc`.
- YellowBricks is fully divested and closed. It remains in scope only for historical sale-proceeds classification and source-record reconciliation.
- `Matthew Holdings`, where referenced elsewhere, is a personal planning label
  for ML1 rather than a separate legal entity in this metric framework.

## Known Current Inputs

- Current explicit Levine Law -> Matthew compensation target for 2026: `CAD 72,000` salary + `CAD 8,000` bonus = `CAD 80,000`
- For `HBP-002`, this target is treated as compensation inflow from Levine Law to Matthew inside the Matthew gross inflow by entity metric family.
- Current realized YellowBricks sale inflow already received into `17513721 Canada Inc`: slightly more than `CAD 27,000`
- Andersen fees are received by `17513721 Canada Inc`, while Andersen operational matters are tracked inside Levine Law and credited to Levine Law in the 2026 operating picture.
- Risk to monitor: Andersen Service Line economics could be omitted, misclassified, or double-counted if the cross-entity reconciliation rule is not applied consistently.

## Current Forward-Looking Sale Thesis

- `17513721 Canada Inc` is optimistic that Ontario MSB Corp (`1001494374 Ontario Corp`) can be sold in 2026 for slightly more than `CAD 27,000` of corporate revenue.
- For `HBP-002`, this is a forward-looking Ontario MSB sale assumption, not a realized cash receipt.

## Initiation Exit Metrics

| Metric | Initiation exit test | Evidence |
| --- | --- | --- |
| Reporting boundary clarity | The five in-scope entities and Matthew-level cash movement rule are listed with no material ambiguity | `PROJECT_CHARTER.md`, `BUSINESS_CASE.md` |
| Formula clarity | Gross inflow, gross outflow, and net-cash-flow formulas are explicit enough for CPA-style review | `METRICS.md`, `STAKEHOLDERS.md` |
| Source-record mapping | Primary source records are identified for each in-scope entity and cash-movement family | `METRICS.md` |
| Close-process readiness | Monthly close and review can occur within 10 business days of month-end | `PROJECT_CHARTER.md`, `STAKEHOLDERS.md` |
| ML1 gate readiness | The initiation packet is specific enough for an `Initiating -> Planning` decision | `APPROVAL_RECORD.md` and packet review |
