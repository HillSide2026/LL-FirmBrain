---
id: llp-013__planning__metrics
title: LLP-013 Funnel 3 — Metrics
owner: ML1
status: proposed
created_date: 2026-03-18
last_updated: 2026-04-03
tags: [funnel-03, marketing, planning, metrics]
---

# Metrics

Project ID: LLP-013
Project Path: 08_MARKETING/LLP-013
Stage: Planning

> Status: proposed. Requires ML1 approval before the Planning→Executing
> (`Pre-Launch`) gate can close.

---

## Metric Definitions

| KPI | Definition | Formula | Measurement Source |
|-----|-----------|---------|-------------------|
| `f3_qualified_consults_per_month` | Number of F3-attributed qualified consultation bookings per month | `count(booked_consults where source = F3)` | Consultation booking system; source tracking required |
| `f3_consult_to_matter_rate` | Share of F3 consultations that result in a matter opening | `(F3_matters_opened / F3_consults_booked) * 100` | Clio matter records; source tag required |
| `linkedin_cpl` | Cost per booked consultation generated through LinkedIn Ads | `linkedin_ads_spend / f3_consults_booked_from_linkedin` | LinkedIn Ads manager |
| `f3_matters_opened_per_month` | Number of new matters opened with F3 as attributed source per month | `count(matters_opened where source = F3)` | Clio; requires F3 source tag on matter record |
| `f3_avg_matter_value` | Average billed value of F3-sourced matters | `sum(billed_value, F3_matters) / count(F3_matters)` | Clio billing records |
| `se01_content_pass_rate` | Share of F3 content drafts that pass SE-01 scoring (≥0.60) on first submission | `(passing_drafts / submitted_drafts) * 100` | SE-01 audit log |
| `content_publishing_cadence` | Number of F3 LinkedIn posts published per month | `count(published_posts where funnel = F3)` | LinkedIn analytics |

---

## Thresholds (Proposed — Pending ML1 Approval)

| KPI | Baseline (Pre-Launch) | Target (Month 3) | Target (Month 6) | Threshold (Pause/Review) |
|-----|-----------------------|------------------|------------------|--------------------------|
| `f3_qualified_consults_per_month` | 0 (untracked) | ≥2 | ≥3 | <1 after 90 days of active channel |
| `f3_consult_to_matter_rate` | Unknown | ≥30% | ≥40% | <20% sustained over 60 days |
| `linkedin_cpl` | N/A | ≤$600 CAD | ≤$500 CAD | >$1,000 CAD after 45 days — pause and review |
| `f3_matters_opened_per_month` | 0 | ≥1 | ≥2 | 0 after 4 months of active channel |
| `f3_avg_matter_value` | Unknown | ≥$5,000 | ≥$8,000 | <$3,000 sustained over 3 months |
| `se01_content_pass_rate` | N/A | ≥80% | ≥85% | <60% sustained — content process review required |
| `content_publishing_cadence` | 0 | ≥4/month | ≥6/month | <2/month for 60 days — workplan review |

---

## Baseline Capture

Baseline capture period: First 30 days of live channel activity after ML1
authorizes `launch`.

If baseline for `f3_qualified_consults_per_month` is zero at 30 days, reassess channel targeting and ICP before month 2 spend.

---

## Validation Review

Metrics are reviewed at the following gates:

| Gate | Timing | Reviewer | Decision |
|------|--------|---------|---------|
| Planning→Executing (`Pre-Launch`) | 2026-04-18 (target) | ML1 | Approve thresholds; authorize controlled execution readiness work |
| Pre-Launch→Launch | TBD | ML1 | Confirm public launch thresholds, budget, and tracking before go-live |
| 45-day campaign review | 45 days post LinkedIn Ads launch | ML1 | Review CPL and consult rate; continue, adjust, or pause |
| 90-day funnel review | 90 days post channel activation | ML1 | Assess all thresholds; determine if F3 is generating viable pipeline or requires channel/messaging revision |

---

## Notes

- `f3_avg_matter_value` threshold of $8,000 (Month 6) is a working hypothesis. The canonical matter value floor for ICP-03 work is not yet defined — this metric validates the assumption over time. If average matter value is consistently <$5,000, the ICP or offer scope requires revision.
- LinkedIn CPL threshold of $600 (Month 3) is based on Soulpepper's benchmark for comparable B2B legal service LinkedIn campaigns. ML1 must set a hard pause threshold before campaign activation.
- All F3 matters must be tagged with source = F3 in Clio at matter opening for attribution to work. This is an operational dependency — Clio tagging discipline must be established before channel launch.

## Retired Metric Artifact Consolidation

- Consolidated on: 2026-05-25
- Retired source artifacts moved to: `10_ARCHIVE/LL_PORTFOLIO_PM_CONFORMANCE_2026-05-25/04_INITIATIVES/LL_PORTFOLIO/08_MARKETING/LLP-013/planning`
- Retired artifact names: ML1_METRIC_APPROVAL.md
- Threshold approval and measurement details now belong in this `METRICS.md` file.

