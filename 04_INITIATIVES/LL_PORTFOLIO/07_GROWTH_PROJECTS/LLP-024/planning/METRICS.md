---
id: 04_initiatives__ll_portfolio__07_strategic_projects__llp_024_nda_esq__metrics_md
title: NDA Esq - Metrics
owner: ML1
status: approved
created_date: 2026-03-14
last_updated: 2026-04-02
tags: [nda-esq, strategic-project, planning, metrics]
---

# Metrics and Validation

Project ID: LLP-024
Project Path: 04_INITIATIVES/LL_PORTFOLIO/07_STRATEGIC_PROJECTS/LLP-024
Stage: Planning

## Metric Definition

| KPI | Definition | Formula |
| --- | --- | --- |
| `mvp_ready_on_or_before_target` | Whether the MVP is launched on or before the approved target date | `1 if launch_date <= target_date, else 0` |
| `generated_nda_qa_pass_rate` | Share of sampled generated NDAs that meet the ML1-approved QA benchmark | `(qa_pass_generated_ndas / sampled_generated_ndas) * 100` |
| `retained_client_usage_30_day` | Number of retained clients who complete at least one NDA generation in the first 30 days after launch | `count(retained_clients with >=1 completed_generation in first_30_days)` |
| `qualified_consults_90_day` | Number of qualified consults produced from external NDA Esq usage in the first 90 days after launch | `count(qualified_consults from external_users in first_90_days)` |
| `product_revenue_4_month` | Total NDA Esq product revenue recognized by the close of month 4 | `sum(product_revenue through month_4_close)` |
| `cac_per_qualified_consult` | Average acquisition cost per qualified consult generated from external usage | `acquisition_spend / qualified_consults_from_external_users` |
| `retained_client_repeat_usage_rate` | Share of active retained-client users who complete more than one NDA generation in the measurement window | `(retained_clients_with_2plus_generations / active_retained_client_users) * 100` |
| `support_response_time_hours` | Average or monitored response time for customer support | `average(first_response_time_hours)` |

### Goal Alignment

- `mvp_ready_on_or_before_target`, `generated_nda_qa_pass_rate`, and `retained_client_usage_30_day` support product-readiness goals.
- `qualified_consults_90_day`, `product_revenue_4_month`, and `cac_per_qualified_consult` support acquisition and growth goals.
- `retained_client_repeat_usage_rate` and `support_response_time_hours` support operating-performance goals.

### Target Status

- Thresholds are proposed in `ML1_METRIC_APPROVAL.md`.
- Metrics are not active implementation gates until ML1 signs off on thresholds.

### Measurement Cadence

- weekly planning review for readiness metrics
- monthly governance summary for revenue and retention metrics

## Measurement Method

### Method

- Capture product, acquisition, subscription, and support events from approved operational systems.
- Use only observed system events, revenue records, campaign spend, and sampled validation outputs.
- Maintain evidence references for each aggregated metric report.
- Separate launch-window metrics from ongoing operating metrics so thresholds are not mixed across phases.

### Calculation Rules

- `mvp_ready_on_or_before_target`
  Rule: binary success measure based on launch date versus approved target date.
- `generated_nda_qa_pass_rate`
  Numerator: generated NDAs that pass the approved QA benchmark in the sampled set.
  Denominator: total sampled generated NDAs reviewed against the approved benchmark.
- `retained_client_usage_30_day`
  Window: first 30 calendar days after MVP launch.
  Rule: count unique retained clients who complete at least one NDA generation.
- `qualified_consults_90_day`
  Window: first 90 calendar days after launch.
  Rule: count qualified consults attributable to external NDA Esq usage.
- `product_revenue_4_month`
  Rule: total recognized product revenue through the close of month 4.
- `cac_per_qualified_consult`
  Numerator: attributable acquisition spend for the relevant measurement window.
  Denominator: count of qualified consults generated from external users in the same window.
- `retained_client_repeat_usage_rate`
  Rule: cohort-based repeat usage measure for retained-client users in the approved review window.
- `support_response_time_hours`
  Rule: measure first-response lag for inbound support requests.

### Windows and Reporting

- launch metrics: first 30 and first 90 days after MVP launch
- recurring operating metrics: monthly
- any metric below an ML1-approved threshold for two consecutive review windows triggers escalation

### Data Sources

- application event logs and user-account records
- generated NDA QA sample set and benchmark review notes
- Stripe revenue and payment records
- campaign and ad-platform spend and conversion exports
- consult-booking, intake, and routing records
- email automation and onboarding records
- support and ticketing or chat records

## Baseline Capture Period

### Baseline Window

- Launch baseline start: MVP launch date
- Launch baseline end: 30 calendar days after MVP launch
- Growth baseline end: 90 calendar days after MVP launch

### Purpose

NDA Esq is a greenfield project, so there is no legacy operating baseline. The
baseline will therefore be captured from the controlled launch period and used
as the first reference point for post-launch optimization.

### Inclusion Rules

- include only real user activity tied to the approved NDA Esq product
- include only attributable acquisition spend from approved channels
- include only paid users and revenue records reconciled to the approved billing system
- include only support requests generated by live product usage

### Exclusion Rules

- exclude test users, internal QA activity, and synthetic NDA submissions
- exclude spend or traffic from unapproved channels
- exclude any manual lawyer-review work that is not part of the approved premium path

### Output

- first-30-day baseline for generation QA, retained-client usage, and support metrics
- first-90-day baseline for qualified consults and acquisition metrics
- initial operating baseline for product revenue and retained-client repeat usage review

## Validation Review

### Review Criteria

- scope boundaries are explicit across product, acquisition, and operations workstreams
- exclusions are clear enough to prevent negotiation, redlining, drafting, and consultation creep
- metric formulas and denominators are reproducible from approved evidence sources
- launch and growth baseline windows are unambiguous
- threshold package is sufficient to judge MVP, acquisition, and operations success
- risk, dependency, and communication controls are strong enough for implementation authorization

### Review Owner

- ML1
- Project Owner

### Review Outcome

Status: Proposed
Notes: Planning packet drafted; implementation remains gated pending ML1 review
of thresholds and final Planning -> Executing approval.

## ML1 Metric Approval

Approval Status: Proposed

Approved By: ______________________
Date: ______________________

### Metrics Submitted for Approval

- `mvp_ready_on_or_before_target`
- `generated_nda_qa_pass_rate`
- `retained_client_usage_30_day`
- `qualified_consults_90_day`
- `product_revenue_4_month`
- `cac_per_qualified_consult`
- `retained_client_repeat_usage_rate`
- `support_response_time_hours`

### Proposed Thresholds

| KPI | Direction | Proposed Threshold |
| --- | --- | --- |
| `mvp_ready_on_or_before_target` | Higher is better | `= 1` |
| `generated_nda_qa_pass_rate` | Higher is better | `>= 85%` |
| `retained_client_usage_30_day` | Higher is better | `>= 10` |
| `qualified_consults_90_day` | Higher is better | `>= 10` |
| `product_revenue_4_month` | Higher is better | `>= 5000` |
| `cac_per_qualified_consult` | Lower is better | `< 250` |
| `retained_client_repeat_usage_rate` | Higher is better | `>= 30%` |
| `support_response_time_hours` | Lower is better | `< 24` |

### Threshold Status

- Thresholds are proposed and not yet active until ML1 approval is recorded.
- Any budget envelope or launch-spend ceiling remains separately subject to ML1 determination before implementation.

Notes:
- This file is the canonical measurement, baseline, validation, and threshold-approval document for NDA Esq.
- Implementation must not begin until ML1 records threshold approval in this document.
