---
id: llp_012_funnel2_management__planning__dependencies_md
title: LLP-012 Funnel 2 - Dependencies
owner: ML1
status: draft
created_date: 2026-04-07
last_updated: 2026-04-07
tags: [llp-012, funnel-02, planning, dependencies]
---

# Dependencies

Project ID: LLP-012
Project Path: 08_MARKETING/LLP-012
Stage: Planning

## Internal Dependencies

| Dependency | Type | Required By | Status | Notes |
| --- | --- | --- | --- | --- |
| LLP-025 Marketing Strategy | Strategic packet | Channel sequencing, positioning, and KPI framing | active | F02 inherits the firm-level positioning and channel logic from LLP-025. |
| LLP-011 Funnel 1 Management | Adjacent funnel | Shared intake infrastructure and F01-to-F02 transition logic | active | F01 remains the bridge funnel while F02 is normalized and matured. |
| LLP-014 Intake Management | Adjacent management layer | Intake handoff and post-conversion routing discipline | in progress | F02 should hand qualified buyers into the governed intake layer rather than invent a separate fulfillment path. |
| LLP-024 NDA Esq | Adjacent product surface | Overlap management where NDA or contract issues route into broader corporate-health work | active | README already treats traffic overlap as possible without subordination. |

## Platform and Tool Dependencies

| Dependency | Type | Required By | Notes |
| --- | --- | --- | --- |
| `levine-law.ca` landing-page surface | Platform | F02 offer presentation and conversion path | A live page is required for a stable paid-diagnostic surface. |
| Go High Level | Platform | Intake form, qualification workflow, booking, and follow-up | Must support a non-bypass qualification gate and evidence capture. |
| Payment / checkout path | Platform | Paid Health Check purchase or booking | Required to preserve the paid-diagnostic posture. |
| Clio / fulfillment operations | Operating system | Downstream matter opening and handoff | Required once a buyer converts beyond the diagnostic stage. |

## Channel Dependencies

| Dependency | Type | Required By | Notes |
| --- | --- | --- | --- |
| Accountant referral network | Primary channel | Referral-based acquisition path | This is the adopted primary F02 channel. |
| LinkedIn | Secondary channel | Mid-ticket operator discovery and proof distribution | Useful, but subordinate to accountant referral for core ICP reach. |
| Structuring SEO assets | Secondary channel | Long-tail discovery and authority support | Should activate after the Health Check page and routing logic are stable. |

## Dependency Rules

- F02 must not change the firm-level positioning defined in LLP-025 without ML1 direction.
- Referral, landing-page, intake, and payment surfaces must all point to the
  same offer and ICP boundary.
- Downstream remediation or retainer logic must remain compatible with firm
  operations and matter-opening controls rather than living as a separate funnel
  exception.
