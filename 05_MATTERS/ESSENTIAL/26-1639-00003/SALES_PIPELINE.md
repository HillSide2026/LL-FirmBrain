---
id: MATTER-26-1639-00003-SALES_PIPELINE
title: Sales Pipeline — 26-1639-00003 — Andersen (Market Access)
owner: ML1
status: draft
created_date: 2026-04-03
last_updated: 2026-05-20
tags: [matter, sales-pipeline, 26-1639-00003]
practice_areas: [market_access, trade, customs]
---

# Sales Pipeline — 26-1639-00003 — Andersen (Market Access)

## Purpose

This file breaks the Andersen market-access matter into prospective end-client
files inside the Andersen relationship.

Andersen is the LL client. The pipeline here is about prospecting and
advancing end-client files through Andersen.

This is similar to LL Onboarding in that it moves opportunities toward close
and usable work, but it is not the same process. It does not treat the end
client as automatically being the LL client of record.

## Stage Model

- `identified` — a proceeding, transaction, or file opportunity has surfaced; we are identifying relevant parties, jurisdictions, and issues, and initiating outreach where appropriate, but have not yet established live contact
- `contacted` — we have established contact with a real live human being at the target organization
- `qualified` — there is enough substance to treat the file as a real target
- `closing` — active effort is underway to convert the opportunity into instructed work through Andersen
- `active_file` — instructions are in and the file is now live inside the Andersen market-access lane
- `inactive` — track has been reviewed and is not being pursued; reason documented

## Industry Segment Model

Current target segments for the Andersen market-access lane:

- `agriculture_and_agri_food`
- `mining_and_minerals`
- `manufacturing`
- `dual_use_manufacturing`
- `data_and_data_centres`
- `financial_services_fintech`

The current live track sits inside `financial_services_fintech`. Legacy inactive
tracks sit inside `agriculture_and_agri_food`. Additional tracks should be
tagged to one of the above segments when first recorded.

## Active Tracks

| Track ID | End-client file | Segment | Stage |
|----------|-----------------|---------|-------|
| `MA-003` | Albor Financial — stablecoin treasury software, LatAm market access | `financial_services_fintech` | `identified` |

### MA-003 — Albor Financial

- **Company:** Albor Financial
- **Product:** Stablecoin treasury software sold to banks
- **Ask:** Andersen to lead a market access strategy across Latin America
- **Stage:** `identified` — lead received; no live contact established yet
- **Segment:** `financial_services_fintech` (new segment; not in original segment model)
- **Next step:** Qualify the ask — confirm which LatAm jurisdictions, what Andersen's proposed role is, and whether LL has a legal advisory angle (regulatory, market entry, licensing)

## Inactive Tracks

| Track ID | End-client file | Segment | Stage | Reason |
|----------|-----------------|---------|-------|--------|
| `MA-001` | Pecans from Northern Israel — agri-food market-access | `agriculture_and_agri_food` | `inactive` | No importer interest identified; ML1 has lost interest in this track (2026-04-29) |
| `MA-002` | Flavored butter from Manitoba — agri-food market-access | `agriculture_and_agri_food` | `inactive` | No importer interest identified; ML1 has lost interest in this track (2026-04-29) |

## Qualification Criteria

Criteria for advancing a track from `contacted` to `qualified` are defined in:

- [`../26-1639-00001/ANDERSEN_QUALIFICATION_CRITERIA.md`](../26-1639-00001/ANDERSEN_QUALIFICATION_CRITERIA.md)

All seven threshold criteria must be met. When a track is qualified, record the qualification in `NOTES_TO_FILE.md` using the template in that document.

## Operating Notes

- Use [`../26-1639-00001/MATTER_BRIEF.md`](../26-1639-00001/MATTER_BRIEF.md) for Andersen relationship-level management.
- Use [`../26-1639-00001/BUSINESS_DEVELOPMENT_OVERVIEW.md`](../26-1639-00001/BUSINESS_DEVELOPMENT_OVERVIEW.md) for cross-lane Andersen business-development visibility.
- Use this matter for the market-access lane within that Andersen relationship.
- Use [`../26-1639-00002/SALES_PIPELINE.md`](../26-1639-00002/SALES_PIPELINE.md) as the parallel Andersen lane using the same stage model.
