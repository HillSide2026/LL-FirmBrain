---
id: 04_initiatives_ll_portfolio_08_marketing_llp_011_funnel1_management_planning_dependencies_md
title: Dependencies
owner: ML1
status: draft
created_date: 2026-05-18
last_updated: 2026-05-18
tags: []
---

# Dependencies

Project ID: LLP-011
Project Path: 08_MARKETING/LLP-011_FUNNEL1_MANAGEMENT
Stage: Planning

## Doctrine Dependencies
- `01_DOCTRINE/03_POLICIES/POL-032_Marketing_Lifecycle_Definition_and_Boundary.md`
- `01_DOCTRINE/03_POLICIES/POL-033_Conversion_Qualification_and_Revenue_Trigger.md`
- `01_DOCTRINE/05_PROTOCOLS/PRO-015_Marketing_Stage_Classification_and_Handoff.md`

## Funnel Definition Dependencies
- `04_INITIATIVES/LL_PORTFOLIO/08_MARKETING/04_FUNNELS/funnel-01/FUNNEL_SPEC.md`

## Operational Dependencies
- Google Ads campaign access and configuration continuity
- GHL intake form, booking, and follow-up configuration integrity
- Availability of stage-event evidence for lead -> screened -> booked -> consult_complete -> retained

## Integration Dependencies (as of 2026-04-05)

| Integration | Key / Credential | Status | Notes |
|---|---|---|---|
| GHL API | `GHL_API_KEY` in .env | Key confirmed | Pipeline stage pull not yet built. |
| Google Search Console API | Not yet in .env | Not started | Required before domain migration. OAuth credentials needed from Google Cloud Console. |
| GA4 | Not yet in .env | Not started | No event instrumentation documented. |
| WordPress REST API | `WORDPRESS_APP_PASSWORD` in .env | Active | `WORDPRESS_BASE_URL` points to levinelegal.ca — must be updated at domain migration. |

## Governance Dependencies
- ML1 availability for execution authorization and ongoing execution decisions
- CMO/marketing agent orchestration operating under current capability boundaries

## Dependency Risks
- External platform policy/config changes can disrupt lifecycle execution and conversion outcomes.
- Missing event instrumentation can block KPI operation and goal attainment tracking.
- Domain migration (levinelegal.ca → levine-law.ca) is a dependency risk: executing without a GSC baseline and 301 redirect map risks ranking loss. See `INTEGRATION_BACKLOG.md`.
