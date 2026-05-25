---
id: llp-011__surface_monitoring_notes
title: Surface Monitoring Notes — F1 External Surfaces
owner: ML1
status: working
created_date: 2026-04-05
last_updated: 2026-04-05
tags: [llp-011, funnel-01, monitoring, analytics, backlog]
---

# Surface Monitoring Notes — F1 External Surfaces

> Working notes from 2026-04-05 session. Covers the monitoring gap, domain
> migration context, and integration backlog. ML1 review required before
> any integration build is authorized.

---

## Current State

The repo has content production infrastructure (content files, publishing
scripts, funnel specs) but no live monitoring infrastructure. The external
surfaces — levinelegal.ca blog, hub pages, and GHL pipeline — are write-only
from the repo's perspective. Content goes out; no performance data comes back.

The data that matters sits in four external systems with no repo integration:

| System | What it holds | Repo connection |
|---|---|---|
| Google Search Console | Impressions, CTR, position, queries per URL | None |
| GA4 | Sessions, engagement, conversion events, user flows | None |
| GHL | Lead capture, pipeline stage, booked/retained events | API key confirmed in .env |
| Google Ads | Spend, CPC, CPA, impression share | None |

The KPI formulas in `planning/MEASUREMENT_METHOD.md` are correctly defined.
The denominator data (GHL stage transitions) never flows into the repo.

---

## Domain Migration Context

The intention is to move all content from levinelegal.ca to levine-law.ca.

Critical constraint: a domain migration without a pre-migration GSC baseline
is blind. Before executing the migration:

1. GSC baseline must be captured for levinelegal.ca (per-URL impressions,
   position, CTR for all published posts — IDs 1980–2015 F2, 2179–2190 F1).
2. 301 redirect map must be documented in the repo before any DNS change.
3. Post-migration GSC comparison must be tracked (typically 4–8 weeks to
   stabilize).

The WORDPRESS_BASE_URL in .env currently points to levinelegal.ca. This will
need to be updated when the migration executes.

---

## Three Monitoring Questions

**1. Is the content being found? (SEO)**
Google Search Console → per-URL impressions, CTR, average position, queries.
This is the primary signal for whether the F1 content cluster (published
2026-04-05) is indexing and ranking.

**2. Is the content converting? (Web analytics)**
GA4 → traffic-to-product-page flow, engagement rate, exit pages.
No GA4 event instrumentation is currently documented in the repo.

**3. Is the pipeline moving? (CRM)**
GHL → lead_captured → booked → consult_complete → retained stage transitions.
GHL API key is confirmed in .env (`Private_API_KEY`). Integration not yet built.

---

## Integration Backlog

See `INTEGRATION_BACKLOG.md` in this folder for the full task list.

---

## Known Gaps in Published F1 Content (2026-04-05)

1. **Internal links are broken.** Posts were published with flat slugs, but
   the markdown content contains relative paths (e.g.
   `/shareholder-disputes/partnership-not-tense`). These paths resolve to
   nothing on the live site. The links need to be updated to the actual
   published URLs before the content is promoted.

   Correct URL map:
   | Repo path | Live URL |
   |---|---|
   | `/shareholder-disputes/partnership-not-tense` | `https://levinelegal.ca/partnership-legally-meaningful-phase/` |
   | `/shareholder-disputes/early-signs` | `https://levinelegal.ca/early-signs-business-partner-breakdown/` |
   | `/shareholder-disputes/documentation` | `https://levinelegal.ca/what-to-document-shareholder-dispute/` |
   | `/shareholder-disputes/removing-partner-ontario` | `https://levinelegal.ca/removing-business-partner-ontario/` |
   | `/shareholder-disputes/shareholder-agreement-reality` | `https://levinelegal.ca/shareholder-agreement-no-longer-reflects-reality/` |
   | `/business-structure/drift-invisible-until-it-matters` | `https://levinelegal.ca/business-structure-drift-ontario/` |
   | `/business-structure/structure-outdated` | `https://levinelegal.ca/business-structure-stops-reflecting-operations/` |
   | `/business-structure/adding-shareholder-informally` | `https://levinelegal.ca/adding-shareholder-informally-ontario/` |
   | `/business-structure/investor-diligence-issues` | `https://levinelegal.ca/investor-diligence-corporate-structure/` |
   | `/business-structure/documents-vs-reality` | `https://levinelegal.ca/corporate-documents-vs-business-reality/` |
   | `/products/shareholder-dispute-readiness-guide` | Not yet built |
   | `/products/business-structure-diagnostic` | Not yet built |

2. **Product pages don't exist.** Both pillar posts link to product pages
   that have not been created. Until Product A and Product B pages are built,
   those links are dead.

3. **Pillar pages not created as WP pages.** The pillar page content was
   published as posts (`/shareholder-disputes-ontario/`,
   `/business-structure-ontario/`). They function as posts, not as hub pages.
   This is acceptable for now but means the URL hierarchy (e.g.
   `/shareholder-disputes/` as a parent) does not exist.
