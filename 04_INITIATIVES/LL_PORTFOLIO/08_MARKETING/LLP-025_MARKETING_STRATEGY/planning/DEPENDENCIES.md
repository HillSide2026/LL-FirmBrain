---
id: 04_initiatives_ll_portfolio_08_marketing_llp_025_marketing_strategy_planning_dependencies_md
title: Dependencies
owner: ML1
status: draft
created_date: 2026-05-18
last_updated: 2026-05-18
tags: []
---

# Dependencies

Project ID: LLP-025
Project Path: 08_MARKETING/LLP-025_MARKETING_STRATEGY
Stage: Planning

## Doctrine Dependencies

| Dependency | Source | Risk if Unavailable |
|---|---|---|
| Audience definitions (ICP-01, ICP-02, ICP-03) | `MARKET_POSITIONING.md` | All channel and funnel decisions are unanchored |
| Marketing objectives (OBJ-01, OBJ-02, OBJ-03) | `OBJECTIVES.md` | KPI targets lose upstream alignment |
| Marketing strategy thesis and governance rules | `MARKETING_STRATEGY.md` | Funnel creation and agent decisions have no governing rules |
| Funnel specs (F01, F02, F03) | `04_FUNNELS/funnel-01,02,03/` | Offer mapping and channel strategy cannot be defined without funnel specs |

## Downstream Project Dependencies

| Project | Dependency Type | Notes |
|---|---|---|
| LLP-011 FUNNEL1_MANAGEMENT | LLP-025 governs F01 strategy; LLP-011 executes | F01 wind-down decision requires LLP-025 approval before LLP-011 can act |
| LLP-012 FUNNEL2_MANAGEMENT | LLP-025 governs F02 strategy and launch; LLP-012 executes | F02 launch milestone in LLP-025 unblocks LLP-012 execution |
| LLP-013 FUNNEL3_MANAGEMENT | LLP-025 governs F03 payments vertical program; LLP-013 executes | Payments vertical content cadence defined here; executed in LLP-013 |
| LLP-026 LEAD_CAPTURE | Receives channel strategy output from LLP-025 | ICP-02 channel decision in WS-01 directly shapes lead capture infrastructure |
| LLP-014 INTAKE_MANAGEMENT | Receives qualified leads from the marketing system | Intake pipeline must be ready to handle F02 (paid diagnostic) lead profile, which differs from F01 |

## Platform Dependencies

| Platform | Purpose | Risk |
|---|---|---|
| Google Ads | F01 acquisition channel | F01 continues during planning; platform disruption would affect bridge revenue |
| Go High Level (GHL) | Intake and scheduling flow | Required for lead routing from all funnels; GHL config must support F02 paid diagnostic intake |
| Website / Landing page infrastructure | F02 launch requires a landing page | If platform is not in place, F02 launch milestone is blocked |
| Analytics / tracking | Baseline KPI data source | 30-day baseline already collected; ongoing tracking required for Phase 2/3 KPI formalization |

## Governance Dependencies

| Item | Dependency |
|---|---|
| KPI target approval | ML1 must review and approve METRICS.md before execution is authorized |
| ICP-02 channel hypothesis | ML1 decision memo required before F02 distribution architecture can be defined |
| F02 offer scope | ML1 approval required before build begins |
| Agent activation decisions | ML1 approval required for any agent moving from specified to active |
