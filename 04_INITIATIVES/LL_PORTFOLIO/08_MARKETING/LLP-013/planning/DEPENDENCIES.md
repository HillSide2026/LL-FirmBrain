---
id: llp-013__planning__dependencies
title: LLP-013 Funnel 3 — Dependencies
owner: ML1
status: draft
created_date: 2026-03-18
last_updated: 2026-04-03
tags: [funnel-03, marketing, planning, dependencies]
---

# Dependencies

Project ID: LLP-013
Project Path: 08_MARKETING/LLP-013
Stage: Planning

---

## Internal Dependencies (Within LL Portfolio)

| Dependency | Type | Required By | Status | Notes |
|------------|------|-------------|--------|-------|
| SE-01 (Strategic Editor) | Agent — content governance | All F3 content before publication | Active (lightweight mode) | All F3 copy must pass SE-01 scoring before ML1 approval. No F3 content bypasses SE-01. |
| SEO-01 (SEO Metrics Master) | Agent — keyword research | F3 SEO content (BSE-01 phase) | Active (limited) | SEO-01 not activated for F3 keyword research until website live. F3 SEO work deferred to Phase 2. |
| BSE-01 (Blog/SEO Engine) | Agent — content production | F3 SEO content | Blocked | Blocked until levine-law.ca traffic baseline established (F02 website live gate). Not needed for LinkedIn Ads phase. |
| SPE-01 (Selective Provocation Engine) | Agent — top-of-funnel hooks | F3 LinkedIn organic content (authority hooks) | Blocked | Blocked until ≥3 accountant referral relationships active (LLP-025 IMP-01). Manual hook drafting required in interim. |
| MKT_MUGGAH_SECURITIES_AGENT | Optional specialist agent — securities-adjacent perimeter analysis | F3 token / stablecoin / marketplace / exempt-distribution fact patterns | Draft | Supports NI 31-103 / 33-109 / 21-101 / 23-101 / 23-103 / 45-106 / 45-102 issue mapping for securities-adjacent entities in Funnel 3. Internal planning and pre-launch support only. |
| MKT_MUGGAH_MONEY_SERVICES_AGENT | Optional specialist agent — money-services perimeter analysis | F3 MSB / virtual-currency / remittance / FX / AML-reporting fact patterns | Draft | Supports FINTRAC / PCMLTFA issue mapping, MSB / foreign-MSB analysis, and client-risk assessment for money-services-adjacent entities in Funnel 3. Internal planning and pre-launch support only. |
| MKT_MUGGAH_PAYMENT_SERVICES_AGENT | Optional specialist agent — payment-services perimeter analysis | F3 PSP / RPAA / safeguarding / payment-function fact patterns | Draft | Supports RPAA / payment-services issue mapping, PSP registration logic, safeguarding analysis, and client-risk assessment for payment-services-adjacent entities in Funnel 3. Internal planning and pre-launch support only. |
| LLP-012 (F02) | Parallel project | Website — ensure F2/F3 page separation | Planning | F02 website page must be reviewed alongside F03 page to confirm ICPs and offers are not conflated. |
| LLP-011 (F01) | Executing project | No operational conflict | Executing | F01 targets ICP-01 (Ontario entrepreneur); F03 targets ICP-03 (payments / regulatory audience). No channel overlap. Google Ads budget is F01-only. |
| LLP-025 (Accountant Referral Program) | Parallel project | SPE-01 activation; F3 referral map | Planning | LLP-025 IMP-01 (≥3 accountant referrals) is also the gate for SPE-01. F3 referral channels (US lawyers, SaaS advisors) are separate and must be defined independently of LLP-025. |
| FIRM_STRATEGY.md / BUSINESS_PLAN.md (LLP-030) | Reference document | Capacity ceiling and setter trigger | Approved draft | F3 demand projections must stay within 20 billable hour/week ceiling and 12–18 active matter ceiling. |

---

## External Dependencies

| Dependency | Type | Required By | Notes |
|------------|------|-------------|-------|
| levine-law.ca (website platform) | External — ML1-controlled | WS-2 M2.3 (Payments page live) | Website update is prerequisite for LinkedIn Ads activation. MKT_WEBSITE_IMPLEMENTATION_AGENT owns implementation prep and repo-side fixes; live publish still requires ML1 to execute or direct execution. |
| LinkedIn Ads platform | External | WS-3 M3.2 (campaign launch) | Requires campaign manager access and approved budget. LinkedIn Ads minimum daily budget ~$10/day CAD. |
| BetaKit (media outlet) | External | WS-3 M3.3 | Editorial or sponsorship inquiry required. Pricing unknown — must be investigated before budget commitment. |
| RPAA regulatory calendar | External — regulatory | WS-3 M3.5 (RPAA content) | RPAA registration deadline 2026-03-31 has passed. Treat it as a historical buying trigger and shift planning to post-deadline applicability, remediation, reporting, and ongoing operating-discipline content. |
| CARF regulatory calendar | External — regulatory | Content phase 2 | CARF crypto reporting obligations begin 2027. Content targeting CARF preparation should begin in Q3 2026. |
| OSFI operational risk guideline | External — regulatory | Content phase 2 | September 2026 deadline for regulated entities. Content planning window opens Q2 2026. |

---

## Dependency Map

```
ML1 Positioning Approval (M1.1, M1.2)
       │
       ├── Website Page Production (M2.1) ── SE-01 Review ── ML1 Approval ── Website Live (M2.3)
       │                                                                              │
       │                                                                     LinkedIn Ads Launch (M3.2)
       │
       ├── Content Calendar (M2.5–M2.7) ── SE-01 Review ── ML1 Approval ── LinkedIn Organic Posts
       │
       └── Entry Offer Pricing (M1.4) ── Prerequisite for any paid channel activation

LLP-025 IMP-01 (≥3 accountant referrals) ── Unblocks SPE-01 ── F3 authority hooks at scale
LLP-012 F02 website live ── Unblocks BSE-01 ── F3 SEO content at scale
Token / stablecoin / marketplace fact pattern ── MKT_MUGGAH_SECURITIES_AGENT ── securities-adjacent issue map for ML1
MSB / virtual-currency / remittance fact pattern ── MKT_MUGGAH_MONEY_SERVICES_AGENT ── money-services issue map for ML1
PSP / safeguarding / RPAA fact pattern ── MKT_MUGGAH_PAYMENT_SERVICES_AGENT ── payment-services issue map for ML1
```
