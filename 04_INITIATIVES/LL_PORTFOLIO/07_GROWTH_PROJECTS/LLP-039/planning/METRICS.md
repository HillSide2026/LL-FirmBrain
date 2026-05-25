---
id: llp-039_metrics
title: LLP-039 Metrics
owner: ML1
status: draft
created_date: 2026-05-06
last_updated: 2026-05-10
tags: [llp-039, metrics, retainer, realization, fintech]
---

# Metrics

## Core Economics

| KPI | Target / Rule |
|---|---|
| Payment timing | Monthly in advance |
| Mandate types | CAD 8,000 / CAD 12,000 / CAD 20,000 per month |
| CAD 8,000 scope and capacity | To be determined |
| CAD 12,000 capacity limit | Maximum 6 hours/week |
| CAD 20,000 capacity limit | Maximum 10 hours/week |
| CAD 20,000 scope rule | Same scope envelope as CAD 12,000; higher weekly capacity only |
| Write-offs / absorbed overage | 0-3% |
| Collection rate | 95-100% |
| A/R days | 0-15 days |

## Mandate Unit Economics

| Mandate Type | Monthly Retainer | Weekly Capacity Limit | Approx. Monthly Capacity | Approx. Effective Capacity Rate |
|---|---:|---:|---:|---:|
| Tier 1 | CAD 8,000 | TBD | TBD | TBD |
| Tier 2 | CAD 12,000 | 6 hours/week | 26 hours/month | CAD 462/hour |
| Tier 3 | CAD 20,000 | 10 hours/week | 43 hours/month | CAD 462/hour |

Monthly capacity is calculated using approximately 4.33 weeks/month. The
economic objective is not to fill every available hour; it is to define the
maximum promised capacity and then use standardization, triage, and scope
control to preserve effective yield.

## Client Portfolio

| KPI | Target / Rule |
|---|---|
| Solo-owner concurrent mandate count | Governed by mandate mix and weekly capacity, not raw client count |
| Minimum active fintech retainers | 2 |
| Maximum active fintech retainers under solo-owner model | 3 |
| Reference revenue at 3 CAD 12,000 mandates | CAD 432,000/year |
| Concentration risk | Temporarily accepted; must be actively managed |
| Renewal review | Required before continuation |
| Offboarding trigger | Repeated overuse, late payment, scope resistance, or embedded-function drift |

## Capacity Test

| Scenario | Mandate Mix | Weekly Capacity Ceiling | Monthly Revenue | Capacity Read |
|---|---|---:|---:|---|
| Lower-retainer TBD | CAD 8,000 mix | TBD | Variable | Cannot approve until Tier 1 scope/capacity is defined |
| Existential-risk state | 0-1 active retainers | Variable | Variable | Below minimum viable retainer base |
| Minimum viable base | 2 active retainers | Depends on mix | Variable | Stabilizing, but still acquisition-positive |
| Reference middle-tier | 3 x CAD 12,000 | 18 hours/week | CAD 36,000 | Working solo-owner reference case |
| Premium-heavy | 2 x CAD 20,000 | 20 hours/week | CAD 40,000 | At nominal weekly capacity ceiling before other work |
| Mixed premium/reference | 1 x CAD 20,000 + 1 x CAD 12,000 | 16 hours/week | CAD 32,000 | Plausibly sustainable if non-retainer load is controlled |
| Beyond solo-owner ceiling | Any mix exceeding weekly capacity | 20+ hours/week | Variable | Not approved without delivery support or revised capacity model |

## Delivery Quality

| KPI | Target / Signal |
|---|---|
| Average delivery time | Track by mandate type against weekly cap and actual usage |
| Included vs separate-scope classification | Completed before substantive work on ambiguous requests |
| Template reuse rate | Increasing over time |
| Repeat-question capture | Reusable playbook created for recurring issue types |
| Premium-scope conversion | Excluded work converted to approved separate work where valuable |

## Red Flags

- CAD 12,000 mandate exceeds 6 hours/week without approved overage.
- CAD 20,000 mandate exceeds 10 hours/week without approved overage.
- Any mandate mix consumes more than available weekly ML1 capacity.
- Fewer than two active fintech retainers.
- More than three active fintech retainers.
- Repeated urgent requests inside ordinary retainer fee.
- Client expects operational compliance ownership.
- Client asks LL to interface with regulator, bank, or supervisor as part of ordinary retainer.
- New product launch, new jurisdiction, exam, incident, remediation, or safeguarding design appears without separate scope.
- Effective hourly yield remains below CAD 600/hour after standardization efforts.
