---
id: hbp-015-dependencies
title: Dependencies — HBP-015 — Ontario Corp / Locarno
owner: ML1
status: draft
created_date: 2026-05-31
last_updated: 2026-05-31
tags: [locarno, ontario-msb, hillside, hbp-015, planning, dependencies]
---

# Dependencies

**Project:** Ontario Corp / Locarno
**Project ID:** HBP-015
**Stage:** Planning

## External Dependencies

| ID | Dependency | Type | Owner | Impact if Not Met |
|---|---|---|---|---|
| D-01 | FINTRAC standing verification for `1001494374 Ontario Corp` | Regulatory | ML1 / FINTRAC | Track A shell package cannot be completed; Track B cannot progress |
| D-02 | RPAA transfer analysis — acquisition-of-control and re-registration rules | Regulatory / legal | ML1 / Levine PC | Buyer diligence package is incomplete; RPAA value claim is unsubstantiated |
| D-03 | ConnectPay written indication of willingness to onboard pre-revenue entity | Counterparty | ML1 / ConnectPay | Track B cannot progress; fallback to Track A or secondary EMI |
| D-04 | Sponsor-bank candidate assessment — Track C viability | Counterparty | ML1 / bank candidates | Track C remains speculative |
| D-05 | Rhizome compliance software scope confirmation (via HBP-010) | Internal / vendor | ML1 / HBP-010 | Track B software posture is undefined; Sumsub fallback at higher cost |
| D-06 | Q4 2026 Matthew Capital / Kendal Securities restructuring timeline | Adjacent strategic | ML1 / HBP-001 | Sale timing and use-of-proceeds planning require this timeline to be firm |

## Internal Dependencies

| ID | Dependency | Notes |
|---|---|---|
| D-07 | HBP-013 (174/Granville) ML1 time allocation | HBP-013 and HBP-015 share ML1 time; sequencing and prioritization must be explicit |
| D-08 | `LOCARNO_PRODUCT.md` | Track B/C diligence package must be coherent with the Locarno product description |
| D-09 | `PROJECT_CHARTER.md` gate definitions | All track milestones must use the charter's completion criteria, not informal substitutes |
| D-10 | `PROJECT_PLAN.md` and `METRICS.md` | Must use consistent readiness definitions and gate language |

## Dependency Risk Summary

D-01 (FINTRAC verification) and D-03 (ConnectPay written indication) are the two gating dependencies. D-01 gates Track A; D-03 gates Track B. Both must be resolved before track selection is possible.

D-02 (RPAA transfer analysis) is required regardless of track — it affects the buyer diligence package for all three tracks.

D-07 (ML1 time allocation) is the sequencing constraint. HBP-013 and HBP-015 should be explicitly prioritized against each other rather than left to compete implicitly.
