---
id: llp_025_marketing_strategy__planning__metrics_md
title: LLP-025 Marketing Strategy - Metrics
owner: ML1
status: draft
created_date: 2026-04-07
last_updated: 2026-04-07
tags: [llp-025, marketing, planning, metrics]
---

# Metrics

Project ID: LLP-025
Project Path: 08_MARKETING/LLP-025
Stage: Planning

Approval Status: Pending ML1 review.
Threshold Status: This file intentionally carries a mix of provisional targets,
one ML1-adopted bridge-channel control, and deferred post-launch targets
because LLP-025 is the strategy-setting packet for downstream funnel work.

## Metric Design Principles

- ICP quality overrides volume. No target should reward diluting qualification.
- Positioning overrides metrics. If a target requires compromising positioning,
  the target is wrong.
- Funnel 01 metrics are useful now but do not define the future-state strategy.
- Funnel 02 targets cannot be locked until a post-launch baseline exists.
- Funnel 03 targets should begin as provisional and harden only after an initial
  operating baseline is captured.

## Funnel 01 Metric Set

| KPI | Definition | Source | Provisional Target | Locked Target Status |
| --- | --- | --- | --- | --- |
| Lead volume | Total inbound leads from F01 | Google Ads + GHL | `40-50/month` | TBD |
| Lead to consult scheduled rate | Consults booked divided by leads | GHL | `>= 30%` | TBD |
| Consult to paid project rate | Paid projects divided by consults completed | GHL / Clio | `>= 40%` | TBD |
| Lead to paid project rate | Paid projects divided by total leads | GHL / Clio | `>= 10%` | TBD |
| Matters retained per month | New matters opened via F01 | Clio | `4/month` | TBD |
| Cost per matter | Monthly ad spend divided by matters retained | Google Ads + Clio | `<= 375` | TBD |
| Matter value floor | Minimum fee value per retained matter | Clio | `>= CAD 600` | Provisional ML1 floor adopted 2026-04-07; revisit at next baseline review |
| Share of matters above value floor | Matters at or above floor divided by total matters | Clio | TBD | TBD |
| 90-day retention rate | Clients retained at 90 days divided by onboarded clients | Clio | TBD | TBD |

## Funnel 02 Metric Set

| KPI | Definition | Source | Target Status |
| --- | --- | --- | --- |
| Health Check purchase conversion rate | Health Check purchases divided by landing-page visitors | Website analytics | Deferred until post-launch baseline |
| Health Check to remediation conversion | Remediation engagements divided by Health Checks delivered | Clio | Deferred until post-launch baseline |
| Remediation to retainer conversion | Retainers from remediation divided by remediation engagements | Clio | Deferred until post-launch baseline |
| Lead magnet download rate | Downloads divided by landing-page visitors | Website analytics | Deferred until post-launch baseline |
| F02 cost per qualified lead | Spend divided by qualified leads generated | Ads / analytics | Deferred until post-launch baseline |

## Funnel 03 Metric Set

| KPI | Definition | Source | Provisional Target Status |
| --- | --- | --- | --- |
| F03 cost per qualified lead | Spend divided by qualified leads | Ads + GHL | To be set from 30-day baseline |
| Consult show rate | Booked consults that occur divided by total booked | GHL | To be set from 30-day baseline |
| Entry-offer conversion rate | Entry-offer purchases divided by qualified leads | GHL / Clio | To be set from 30-day baseline |
| Entry-offer to retainer conversion | AML/regulatory retainers divided by entry offers delivered | Clio | To be set from 30-day baseline |
| Content authority metrics | Impressions, CTR, time-on-page, lead magnet downloads | Website analytics | Track immediately; lock after baseline |

## Funnel 01 Wind-Down Framework

F01 is a bridge channel. It should be reduced only when F02 has shown enough
replacement evidence to carry the firm without creating a revenue or capacity
gap.

### Trigger Conditions

Begin F01 wind-down only when all conditions below are true for `2`
consecutive rolling `30`-day windows:

- F02 produces at least `3` paid Corporate Health Checks in each window.
- F02 converts at least `1` Health Check client in each window into
  remediation work or a monthly retainer.
- F02 Health Check -> retained/remediation conversion rate is `>=` F01
  consult -> retained conversion rate over the same window.
- F02 generates at least `CAD 8,000` in combined collected Health Check
  revenue plus first-month value of signed downstream engagements in each
  window.
- Total firm active matters remain below `15`.

### Trigger Action

- Reduce F01 Google Ads spend by `50%` for the next `30` days.
- If the same conditions hold during that reduced-spend month and firm monthly
  revenue remains `>= CAD 22,000`, pause F01 entirely.

## Measurement Method

| Data Type | Source | Frequency | Responsible Party |
| --- | --- | --- | --- |
| Ad spend and CPL | Google Ads dashboard | Weekly pull; monthly review | ML1 / SEO Metrics Master Agent |
| Lead volume and qualification | Go High Level intake records | Weekly | ML1 |
| Consult bookings and show rate | GHL calendar | Weekly | ML1 |
| Retainer conversions | Clio matter records | Monthly | ML1 |
| Website and content analytics | Website analytics platform | Monthly | SEO Metrics Master Agent |
| Entry-offer purchases | GHL / payment processor | Monthly | ML1 |

## Baseline and Threshold Phases

### Phase 1 - Instrumentation

- ensure tracking is correct
- ensure pipeline stages are logged
- ensure conversion events are measurable
- ensure attribution is consistent

### Phase 2 - Baseline Collection

- use a 30-day clean data window
- avoid optimization unless results are catastrophic
- capture actual funnel economics before target locking

### Phase 3 - Target Formalization

- define acceptable CPL
- define acceptable show rate
- define acceptable diagnostic conversion
- define acceptable retainer conversion
- define CAC ceiling per offer

## Validation Review

### Review Criteria

- Metric definitions are specific enough to govern downstream funnel packets.
- Source systems and reporting cadence are explicit.
- F01 metrics are decision-useful now, even if some thresholds are still provisional.
- F02 metrics clearly distinguish pre-launch deferral from post-launch target locking.
- F03 metrics can be activated without conflating authority-building with conversion economics.

### Review Outcome

Status: Proposed
Notes: This file supersedes `METRIC_FRAMEWORK.md` as the canonical planning
measurement artifact. The legacy framework remains in the packet for reference.

## ML1 Approval

| Item | Status | Notes |
| --- | --- | --- |
| Metric definitions | pending | Awaiting ML1 review |
| Measurement sources and cadence | pending | Awaiting ML1 review |
| F01 provisional targets | partial | Matter value floor recorded at `CAD 600`; remaining F01 thresholds still provisional |
| F02 targets | deferred | Cannot be locked before post-launch baseline |
| F03 provisional targets | pending | To be set from first baseline window |
| F01 wind-down trigger conditions | adopted | ML1-directed rule recorded on `2026-04-07` |

## Open Measurement Decisions

- decide whether F01 and F03 provisional targets should be locked now or held
  pending a refreshed baseline
- confirm when F02 becomes baseline-eligible after launch
