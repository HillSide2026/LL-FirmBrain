---
id: hbp-015-project-charter
title: Project Charter — HBP-015 — Ontario Corp / Locarno
owner: ML1
status: draft
created_date: 2026-05-31
last_updated: 2026-05-31
tags: [locarno, ontario-msb, hillside, charter, planning]
---

# Project Charter

**Project:** Ontario Corp / Locarno
**Project ID:** HBP-015
**Supersedes:** HBP-005
**Project Type:** Strategic
**Stage:** Planning

## Sponsor

ML1 (Matthew / HillSide)

## Mission

Build `1001494374 Ontario Corp` into a licensed, market-ready regulated payments asset and sell it on an ML1-approved timetable at the highest achievable track, with proceeds flowing into `17513721 Canada Inc`.

## Primary SMART Goal

By `2026-12-31`, `1001494374 Ontario Corp` has a confirmed sale track (A, B, or C), a complete market-ready package for that track, and active sale outreach is authorized or already underway.

## The Three Tracks

### Track A — Pure MSB Shell Sale

**Thesis:** Sell the Ontario corporation as a clean MSB shell. The Ontario corporation does not require a Canadian director — this makes it more portable than 174 for certain buyer profiles.

**Completion criteria:**
- FINTRAC registration verified as active and current with no deficiencies
- Required reports (MSRs, LCTRs if applicable) are in order for the dormant period
- AML program documented to dormant / pre-operational standard
- Corporate records and minute book are sale-ready
- No legacy activity, liabilities, or undisclosed obligations
- RPAA posture documented without creating unnecessary buyer friction
- Buyer handoff memo complete

**Working value marker:** CAD $50,000

### Track B — Infrastructure Asset

**Thesis:** Build the entity into a regulated payments infrastructure asset with direct institutional connectivity. The Locarno product runs on this entity.

**Three sub-gates:**

*Minimum Track B* — entity is more than a shell but not yet institutionalized:
- FINTRAC active and operationally supportable
- RPAA-ready controls designed and documented
- Direct EMI candidate shortlist complete
- At least one EMI (ConnectPay as primary target) has provided written indication of willingness to contract directly
- Bank-grade flow-of-funds package drafted
- AML framework complete enough for EMI / bank review
- Ledger and reconciliation requirements specified
- Orchestration architecture is provider-abstracted on paper

*Preferred Track B* — entity can be marketed as a payments infrastructure asset:
- RPAA registration complete
- Direct EMI agreement signed with assignment, change-of-control, and termination optionality preserved
- Sponsor-bank relationship supported by written counterparty correspondence from a named institution
- Independent ledger implemented or demo-ready
- AML stack implemented or demo-ready
- Orchestration adapter pattern working
- At least one dry-run compliance exercise complete

*Stretch Track B* — fully contracted institutional stack:
- All preferred gate criteria met
- Direct EMI and direct bank agreements signed
- Safeguarding reporting validated
- Ledger and reconciliation tested
- AML workflow operational and audit-logged
- Payment initiation tested
- Migration plan covers both EMI and bank replacement
- No exclusivity, punitive exit fees, or non-transferability terms

**Working value markers:** Low $150k / Medium $200k / High $300k / Stretch $650k

### Track C — Direct Sponsor-Bank

**Thesis:** Low-to-stretch plus a directly contracted, directly referenceable sponsor-bank relationship. Track C does not require a full Stretch build — the direct bank relationship is what defines it.

**Target sponsor-bank profile:** sponsor-friendly, fintech-accommodative, not necessarily Tier 1. Candidates: Solaris, ClearBank, Banking Circle, B4B, smaller Baltic or Central European sponsor banks.

**Working value marker:** TBD

## Stage Plan

1. Confirm entity-status assumptions: FINTRAC, RPAA, AML, corporate records
2. Select primary EMI and obtain written indication (ConnectPay as primary target)
3. Define minimum software posture (Rhizome default unless ConnectPay requires Sumsub)
4. Determine whether to pursue Track B or stop at Track A based on EMI progress
5. If Track B: build toward Preferred gate; assess Track C viability
6. Assemble market-ready package for the achieved track
7. Launch sale on ML1 approval

## Entity Context

| Entity | Role |
|---|---|
| `1001494374 Ontario Corp` | The regulated entity — MSB registered, RPAA registered |
| `17513721 Canada Inc` | Matthew Holdings — owner, proceeds recipient |
| `Levine Professional Corporation` | Legal advisory only |

**FINTRAC:** Registered. Verification of current standing required pre-sale.
**RPAA:** Registered. Travels with entity on a share sale.

## Key Risks

- FINTRAC standing not verified — unknown deficiencies could impair Track A
- EMI access: ConnectPay may not contract directly with a pre-revenue entity
- Sponsor-bank access: Track C requires a named, contracted institution
- RPAA acquisition-of-control or re-registration risk on share transfer
- Overbuild risk: Track B/C build costs may exceed sale premium achieved
- HBP-013 competition for ML1 time (parallel project on 174/Granville)

## Governance

ML1-controlled stage gate. Planning authorized 2026-05-31 as part of HBP-013 split.

Active sale outreach, binding documents, and close mechanics remain separately gated pending ML1 approval of track selection and market-ready package.
