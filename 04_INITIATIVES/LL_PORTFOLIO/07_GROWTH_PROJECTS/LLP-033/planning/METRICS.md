---
id: 04_initiatives__ll_portfolio__07_growth_projects__llp_033_associate_lawyer__planning__metrics_md
title: Associate Lawyer - Metrics
owner: ML1
status: draft
created_date: 2026-03-23
last_updated: 2026-03-23
tags: [associate-lawyer, planning, metrics]
---

# Metrics

Project ID: `LLP-033`
Stage: `Planning`

## Planning Metric Rule

Metrics in LLP-033 exist to support a hiring and activation decision. They are
not vanity staffing metrics.

## Locked Current Inputs

- through the end of October `2025`, the narrowed `25-...` matter cohort
  excluding `Stream` and anything `Rousseau Mazzuca LLP` shows approximately
  `CAD 68,802.92` billed and `CAD 67,746.32` paid
- no contracting lawyer existed in `2025`, so this cohort is a revenue and
  matter-mix baseline only
- the full-year `2025` P&L shows approximately `CAD 25,189.02` in digital
  marketing expense and `CAD 25,946.90` in total marketing expense
- the current `LLP-030` business plan still treats `2026` as a no-core-hire
  year unless ML1 explicitly changes that posture

## Planning Exit Metrics

| Metric | Definition | Target | Evidence |
| --- | --- | --- | --- |
| Recruitment readiness | Candidate profile, sourcing channels, assessment method, and compensation options are explicit | one coherent recruitment model | `SCOPE_STATEMENT.md`, `PROJECT_PLAN.md` |
| Supervision readiness | Delegated matter eligibility, review levels, sign-off boundaries, and escalation triggers are explicit | one defensible supervision model | `SCOPE_STATEMENT.md`, `RISK_REGISTER.md` |
| Monitoring readiness | Weekly review cadence, exception logic, and review-load visibility are explicit | one workable monitoring framework | this file |
| Economics readiness | Delegated contribution formula and required inputs are explicit | one viable economic test | this file, `DEPENDENCIES.md` |
| Revenue-floor dependency | Levine Law has sustained at least three consecutive months at or above `CAD 20,000` in monthly revenue | dependency satisfied before activation recommendation | revenue reporting and `DEPENDENCIES.md` |
| Gate readiness | ML1 can make a bounded approve / defer / narrow / reject decision | full planning packet coherent | planning folder |

## Metric Dictionary

| Metric | Definition | Why It Matters |
| --- | --- | --- |
| Candidate pass rate | Candidates passing practical assessment ÷ candidates assessed | Prevents weak hiring decisions driven by speed or desperation |
| Time to qualified slate | Days from role-open decision to first credible slate | Tests whether the role is recruitable in practice |
| Delegable matter share | Eligible matters ÷ reviewed matters in the target population | Tests whether the role has enough real work to justify itself |
| Review turnaround | Time from draft submitted to review returned | Tests whether supervision is operationally workable |
| Rework rate | Matters needing material rewrite ÷ matters reviewed | Tests whether delegated work is real leverage or disguised second-draft work |
| Material error rate | Matters with substantive legal defect ÷ matters reviewed | Tests quality and malpractice risk exposure |
| ML1 supervision hours per delegated matter | Total ML1 review time ÷ delegated matters | Tests whether the role reduces or merely relocates bottlenecks |
| Delegated contribution per matter | Collected revenue less direct lawyer cost, direct matter cost, and allocated acquisition cost | Tests whether the role adds financial value |
| Delegated contribution margin | Delegated contribution ÷ collected revenue | Tests whether the economics are robust enough to scale |
| Exception rate | Matters triggering risk or client-service escalation ÷ delegated matters | Tests operating stability |

## Operating Metrics If the Role Is Activated

| Metric | Workstream | Definition | Source | Cadence |
| --- | --- | --- | --- | --- |
| Candidate pass rate | Recruitment | Candidates passing assessment ÷ candidates assessed | recruiting log | per hiring cycle |
| Time to qualified slate | Recruitment | Days from role-open decision to first qualified slate | recruiting log | per hiring cycle |
| Review turnaround | Supervision | Median time from draft submitted to ML1 review returned | supervision log | weekly |
| Rework rate | Supervision | Delegated files requiring material rewrite ÷ delegated files reviewed | supervision log | weekly |
| Material error rate | Supervision | Files with substantive legal or risk defect ÷ delegated files reviewed | QA / exception log | monthly |
| Active delegated matters | Monitoring | Count of live matters assigned to the role | Clio / docket log | weekly |
| ML1 supervision hours per delegated matter | Monitoring | ML1 review and correction time ÷ delegated matters | time log | weekly |
| Delegated matter cycle time | Monitoring | Matter open to matter completion for delegated files | Clio | monthly |
| Collected revenue per delegated matter | Analytics | Cash collected for delegated matter | Clio + accounting | monthly |
| Direct lawyer cost per delegated matter | Analytics | Compensation or contractor cost directly attributable to delegated matter | accounting | monthly |
| Delegated contribution per matter | Analytics | Collected revenue - direct lawyer cost - other direct matter cost - allocated acquisition cost | financial-model worksheet | monthly |
| Delegated contribution margin | Analytics | Delegated contribution ÷ collected revenue | financial-model worksheet | monthly |

## Measurement Method

### Method

LLP-033 measurement combines four source types:

- recruitment records for candidate quality and time-to-slate
- Clio / matter records for delegated matter volume, cycle time, billing, and
  collections
- accounting records for booked cost and paid-cost facts
- supervision logs for review time, rework, and exceptions

### Measurement Rule

No single source is sufficient on its own.

- recruitment data does not prove delivery quality
- Clio revenue data does not prove profitability
- accounting cost data does not prove source attribution
- supervision logs do not prove economics

### Core Data Sources

- Clio matter and billing records
- booked accounting data under `LLP-001`
- historical P&L outputs for marketing and cost baselines
- ML1 supervision log
- recruitment scorecards and assessment records

### Core Formulas

```text
Delegated contribution per matter
= collected revenue
- direct lawyer cost
- other direct matter cost
- allocated acquisition cost
```

```text
Fully loaded delegated contribution
= delegated contribution
- modeled ML1 supervision burden
```

```text
Rework rate
= delegated matters requiring material rewrite
/ delegated matters reviewed
```

### Review Cadence

- weekly: supervision and monitoring metrics
- monthly: economics and contribution metrics
- per hiring cycle: recruitment metrics

### Method Limitation

Until a real delegated-delivery period exists, economics remain
assumption-bound even if the historical revenue baseline is strong.

## Baseline Capture Period

### Historical Baseline Window

- Start: `2025-01-01`
- End: `2025-10-31`

### Historical Baseline Use

This window is used to understand:

- matter mix
- billed and paid revenue patterns
- collection behavior
- whether the target matter population is rich enough to justify modeling a
  delegated delivery role

### Locked Historical Baseline Note

- the narrowed `25-...` matter cohort excluding `Stream` and anything
  `Rousseau Mazzuca LLP` is the current primary baseline population
- no contracting lawyer existed in this baseline period, so it is not a
  delegated-fulfillment baseline

### First Activation Baseline Window

If ML1 activates the role, a second baseline window should open:

- first `15` delegated matters, or
- first `45` days after the first delegated matter,
  whichever is later

### Activation-Baseline Capture Items

- matter type
- billed amount
- collected amount
- direct lawyer cost
- ML1 supervision hours
- review turnaround
- rework count
- material exceptions

## Validation Review

### Review Criteria

| Area | Validation Question | Pass Condition |
| --- | --- | --- |
| Recruitment | Is the target role specific enough to recruit against? | candidate profile, sourcing logic, and assessment model are explicit |
| Supervision | Is the delegated-work boundary specific enough to defend? | eligible and excluded matter types are explicit and review points are clear |
| Monitoring | Can ML1 detect quality or capacity failure quickly? | weekly cadence and exception logging are explicit |
| Analytics | Can ML1 tell whether delegated delivery actually works financially? | contribution formula and required inputs are explicit |
| Governance | Does the packet preserve ML1 authority over activation? | no artifact implies automatic hiring or live delegation |

### Review Owner

- ML1

### Validation Outcome Scale

- `Pass` — planning packet is coherent enough for an activation decision
- `Pass with Conditions` — packet is usable, but specific gaps must be closed
- `Fail` — packet does not yet support a reliable decision

## ML1 Metric Approval

Approval Status: Proposed

Approved By: ______________________
Date: ______________________

### Proposed Approval Scope

- recruitment metrics accepted
- supervision metrics accepted
- monitoring metrics accepted
- analytics and economics metrics accepted
- activation-gate metrics accepted

### Threshold Rule

This section is the only valid home for ML1 threshold approval for LLP-033.
No separate approval artifact governs metrics for this planning packet.

## Gate Conditions

No activation recommendation should be made unless:
- delegated contribution can be modeled explicitly
- Levine Law has first sustained at least three consecutive months at or above
  `CAD 20,000` in monthly revenue
- supervision load can be measured explicitly
- an exception path exists when quality or economics deteriorate
- ML1 can tell which matter classes are in and out

## Approval Note

This file is the authoritative and complete source for LLP-033 metric logic,
measurement method, baseline logic, validation rules, and ML1 metric approval.
