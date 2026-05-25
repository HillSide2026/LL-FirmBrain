---
id: llp-011__integration_backlog
title: Integration Backlog — F1 Surface Monitoring
owner: ML1
status: backlog
created_date: 2026-04-05
last_updated: 2026-04-05
tags: [llp-011, funnel-01, monitoring, analytics, integrations, backlog]
---

# Integration Backlog — F1 Surface Monitoring

> Items below are proposed. None are authorized for build until ML1 approves.
> Priority order reflects dependency sequencing, not urgency ranking.

---

## ITEM 1 — Fix broken internal links in published F1 posts

**Type:** Immediate fix (content)
**Priority:** High — links are live and broken now
**Effort:** 1–2 hours (scripted WP REST PATCH calls)

The 12 F1 posts published on 2026-04-05 contain internal links that use the
original repo path conventions (e.g. `/shareholder-disputes/partnership-not-tense`).
These resolve to 404s on the live site. A patch script using the WP REST API
can update the post content with the correct live URLs.

Full URL map in `SURFACE_MONITORING_NOTES.md`.

**Prerequisite:** None.
**ML1 decision needed:** Approve the link patch run.

---

## ITEM 2 — GSC baseline capture before domain migration

**Type:** Pre-migration gate
**Priority:** Critical — must complete before levine-law.ca migration
**Effort:** 2–4 hours (GSC API OAuth setup + pull script)

Google Search Console API provides per-URL data: impressions, clicks, CTR,
average position, top queries. A one-time pull against the current levinelegal.ca
property establishes the baseline that post-migration performance will be compared
against.

Output: structured report file in `05_ANALYTICS/GSC_BASELINE_LEVINELEGAL_CA.md`

**Prerequisite:** GSC API OAuth credentials (client ID + secret from Google Cloud
Console, same Google account that owns the GSC property).
**ML1 decision needed:** Provide or authorize GSC API credentials. Confirm migration
is intended before building.

---

## ITEM 3 — GHL pipeline stage pull (daily)

**Type:** Ongoing monitoring integration
**Priority:** High — KPI formulas in MEASUREMENT_METHOD.md are defined but have no data
**Effort:** 3–4 hours

GHL API key is confirmed in .env (`Private_API_KEY`). The GHL REST API exposes
contact/pipeline stage data. A daily pull of stage transition counts
(lead_captured → booked → consult_complete → retained) would populate the F1
KPIs defined in `planning/MEASUREMENT_METHOD.md`.

Output: daily `PIPELINE_SNAPSHOT.md` in `05_ANALYTICS/` or appended to a running
report, consumed by the daily sweep.

**Prerequisite:** Confirm GHL pipeline IDs for F1.
**ML1 decision needed:** Authorize build. Confirm pipeline/stage IDs in GHL.

---

## ITEM 4 — GSC ongoing weekly pull (post-migration)

**Type:** Ongoing monitoring integration
**Priority:** Medium — follows ITEM 2
**Effort:** 1–2 hours once ITEM 2 OAuth is set up

Weekly per-URL GSC data pull into `05_ANALYTICS/GSC_WEEKLY_REPORT.md`.
Feeds the SEO_METRICS_MASTER agent with the data it is specced to receive.
Replaces manual GSC review.

**Prerequisite:** ITEM 2 (GSC OAuth setup).
**ML1 decision needed:** None beyond ITEM 2 approval.

---

## ITEM 5 — 301 redirect map for domain migration

**Type:** Pre-migration artifact
**Priority:** Critical — must be complete before migration executes
**Effort:** 1–2 hours (scripted from WP REST API post list)

Before levinelegal.ca → levine-law.ca migration, every live URL must be mapped
to its destination URL on the new domain. This file becomes the source of truth
for the redirect configuration and for GSC property change verification.

Output: `05_ANALYTICS/REDIRECT_MAP_MIGRATION.md`

**Prerequisite:** None — can be built now from the known post inventory.
**ML1 decision needed:** Confirm migration is approved before this is treated as
an execution artifact rather than a planning artifact.

---

## ITEM 6 — WordPress base URL update in .env

**Type:** Config change
**Priority:** Execute at migration time only
**Effort:** 5 minutes

`WORDPRESS_BASE_URL` in .env currently points to `https://levinelegal.ca`.
At migration, this must be updated to `https://levine-law.ca` to route all
subsequent publishing scripts to the new domain.

**Prerequisite:** Migration complete and DNS propagated.
**ML1 decision needed:** Confirm at migration time.

---

## Sequencing

```
ITEM 1  (fix broken links)       → do now, independent
ITEM 2  (GSC baseline)           → do before migration
ITEM 5  (redirect map)           → do before migration
ITEM 3  (GHL daily pull)         → do now, key is ready
ITEM 4  (GSC weekly pull)        → do after ITEM 2
ITEM 6  (update .env base URL)   → do at migration
```
