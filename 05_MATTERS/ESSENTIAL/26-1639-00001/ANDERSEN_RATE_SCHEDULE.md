---
id: MATTER-26-1639-00001-ANDERSEN_RATE_SCHEDULE
title: Andersen Rate Schedule — 26-1639-00001
owner: ML1
status: draft
created_date: 2026-05-12
last_updated: 2026-05-12
tags: [matter, 26-1639-00001, andersen, rates, fee-schedule]
---

# Andersen Rate Schedule

## Purpose

Record the current Andersen rate economics for the Andersen relationship matter.
This file is a matter-level planning and reference artifact. It does not replace
any signed engagement letter, Andersen policy, invoice record, or accounting
reconciliation.

## Current Rate Input

Relationship structure:

- `17513721 Canada Inc` is a collaborating firm to Andersen Consulting.
- Under the Andersen Service Line, `17513721 Canada Inc` provides services to
  clients of Andersen Consulting and Andersen Consulting pays `17513721 Canada
  Inc`.
- Operational matters tied to the Andersen Service Line are tracked inside the
  Levine Law operating picture.

| Item | Value |
|---|---:|
| Andersen starting billing rate | `USD 650/hour` |
| Management fee | `10%` |
| Royalty fee | `2%` |

## ML1 / Lead Advisor Rate Ramp

ML1 provided the following Andersen / `17513721 Canada Inc` lead-advisor rate
ramp:

| Year | Gross hourly rate | Net hourly rate after 12% fees |
|---|---:|---:|
| `2026` | `USD 650/hour` | `USD 572/hour` |
| `2027` | `USD 700/hour` | `USD 616/hour` |
| `2028` | `USD 750/hour` | `USD 660/hour` |
| `2029` | `USD 800/hour` | `USD 704/hour` |
| `2030` | `USD 850/hour` | `USD 748/hour` |

The net-rate column uses the additive shorthand:

```text
gross rate x (1 - 10% - 2%)
```

If the management fee and royalty fee are applied sequentially, use `88.2%` of
gross instead of `88%`. The difference is not strategically material for rough
scenario planning.

## Indicative Role-Based Rate Schedule

ML1 provided the following example role-based schedule. Currency should be
confirmed before use in any invoice, forecast, or bankable model. Given the
current Andersen rate input above, the working planning assumption is that this
schedule is USD unless later corrected.

| Role | Indicative hourly rate | Notes |
|---|---:|---|
| Managing Partner / Lead Advisor | `$650-850/hour` | Senior strategic, regulatory, restructuring, M&A, banking, fintech, or transformation advisory |
| Principal Consultant | `$400-650/hour` | Client lead, architecture, governance, commercial structuring |
| Senior Consultant | `$350-400/hour` | Workstream ownership, process design, implementation oversight |
| Consultant | `$275-325/hour` | Analysis, PMO support, operational mapping |
| Technical Specialist | `$155-675/hour` | Technical architecture, implementation, systems, data, security, payments, compliance tooling, or other specialist technical support depending on seniority and scope |
| Analyst / Research | `$155-175/hour` | Research, data prep, benchmarking, reporting |

### Post-Fee Net Rate Shorthand

If the `10%` management fee and `2%` royalty fee are applied additively to the
gross hourly rate, the effective pre-FX rate is `88%` of gross.

| Role | Gross hourly rate | Net hourly rate after 12% fees |
|---|---:|---:|
| Managing Partner / Lead Advisor | `$650-850/hour` | `$572-748/hour` |
| Principal Consultant | `$400-650/hour` | `$352-572/hour` |
| Senior Consultant | `$350-400/hour` | `$308-352/hour` |
| Consultant | `$275-325/hour` | `$242-286/hour` |
| Technical Specialist | `$155-675/hour` | `$136-594/hour` |
| Analyst / Research | `$155-175/hour` | `$136-154/hour` |

If the fees are applied sequentially, use `88.2%` of gross instead. The
difference is not strategically material for rough scenario planning.

## Net Rate Shorthand

If the management fee and royalty fee are both applied against the gross
starting rate, the simple net-rate shorthand is:

```text
USD 650 x (1 - 10% - 2%) = USD 572/hour
```

If the fees are applied sequentially, the shorthand is:

```text
USD 650 x 90% x 98% = USD 573.30/hour
```

For planning purposes, the effective pre-FX range is therefore:

```text
USD 572-573/hour
```

## CAD Conversion Rule

The CAD-equivalent rate should be modeled as:

```text
USD 572-573 x USD/CAD exchange rate
```

This is clearly superior to the current direct Levine Law hourly anchors of
`CAD 480/hour` for standard corporate/commercial work and `CAD 550/hour` for
specialist regulatory/payments/MSB work, subject to realization, collection,
tax, currency, and entity-level reconciliation.

## Junior Fee-Earner Implication

Because the Andersen starting rate is `USD 650/hour` before the `10%`
management fee and `2%` royalty fee, the Andersen Service Line may support
economically attractive junior fee-earner leverage if the work can be delegated
without quality, supervision, or client-relationship risk.

The role-based schedule sharpens the modeling:

- junior analyst/research work may be billed at approximately `$155-175/hour`
  gross, or `$136-154/hour` after the current fee shorthand;
- consultant work may be billed at approximately `$275-325/hour` gross, or
  `$242-286/hour` after the current fee shorthand;
- senior consultant work may be billed at approximately `$350-400/hour` gross,
  or `$308-352/hour` after the current fee shorthand.
- technical specialist work may be billed across a wider `$155-675/hour` gross
  band, or `$136-594/hour` after the current fee shorthand, depending on
  seniority, technical depth, and scope.

Illustrative pre-compensation production at selected post-fee pre-FX rates:

| Role proxy | Post-fee pre-FX rate | `400` hours | `600` hours | `800` hours |
|---|---:|---:|---:|---:|
| Analyst / Research | `$136-154/hour` | `$54,000-62,000` | `$82,000-92,000` | `$109,000-123,000` |
| Consultant | `$242-286/hour` | `$97,000-114,000` | `$145,000-172,000` | `$194,000-229,000` |
| Senior Consultant | `$308-352/hour` | `$123,000-141,000` | `$185,000-211,000` | `$246,000-282,000` |
| Technical Specialist | `$136-594/hour` | `$54,000-238,000` | `$82,000-356,000` | `$109,000-475,000` |
| Principal / Lead lower-bound | `$352-572/hour` | `$141,000-229,000` | `$211,000-343,000` | `$282,000-458,000` |

CAD-equivalent economics depend on the actual USD/CAD exchange rate and should
not be locked in this matter record. The planning formula remains:

```text
fee-earner CAD receipts
= annual billable hours x applicable post-fee USD rate x USD/CAD exchange rate
```

This junior-fee-earner upside is separate from direct Levine Law associate
economics and should be modeled under the Andersen / `17513721 Canada Inc`
service line before being credited into Levine Law operating analysis.

## Reconciliation Notes

- Andersen fee receipts land in `17513721 Canada Inc`.
- Andersen operational matters are tracked inside the Levine Law operating
  picture.
- The relationship should not be double-counted across `17513721 Canada Inc`
  and Levine Law planning.
- Scenario models should separate:
  - gross Andersen billings;
  - management and royalty fee deductions;
  - net Andersen receipts before FX;
  - CAD-equivalent receipts after FX;
  - operating credit to Levine Law;
  - cash receipt and tax treatment inside `17513721 Canada Inc`.

## Open Validation Items

- Confirm whether the `10%` management fee and `2%` royalty fee are applied
  additively or sequentially.
- Confirm whether fees are applied to billed time, collected receipts, or
  another base.
- Confirm any additional transaction, platform, referral, tax, currency, or
  payment-processing costs.
- Confirm the accounting treatment for crediting Andersen economics to Levine
  Law while receipts remain in `17513721 Canada Inc`.
- Confirm whether junior fee-earner work can be billed through the Andersen
  Service Line at the same starting rate, and what supervision, credentialing,
  conflict, quality-control, and client-consent requirements apply.
