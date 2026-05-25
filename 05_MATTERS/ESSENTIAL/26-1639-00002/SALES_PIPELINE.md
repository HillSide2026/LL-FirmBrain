---
id: MATTER-26-1639-00002-SALES_PIPELINE
title: Sales Pipeline — 26-1639-00002 — Andersen (Trade Remedies)
owner: ML1
status: draft
created_date: 2026-04-02
last_updated: 2026-05-20
tags: [matter, sales-pipeline, 26-1639-00002]
practice_areas: [trade_remedies, trade_defence, customs]
---

# Sales Pipeline — 26-1639-00002 — Andersen (Trade Remedies)

## Purpose

This file breaks the Andersen trade-remedies matter into prospective end-client
files inside the Andersen relationship.

Andersen is the LL client. The pipeline here is about prospecting and
advancing end-client files through Andersen.

This is similar to LL Onboarding in that it moves opportunities toward close
and usable work, but it is not the same process. It does not treat the end
client as automatically being the LL client of record.

## Stage Model

- `identified` — a proceeding or file opportunity in Canada has surfaced; we are monitoring the proceeding, identifying relevant parties, and initiating outreach, but have not yet established live contact
- `contacted` — we have established contact with a real live human being at the target organization
- `qualified` — there is enough substance to treat the file as a real target
- `closing` — active effort is underway to convert the opportunity into instructed work through Andersen
- `active_file` — instructions are in and the file is now live inside the Andersen trade-remedies lane
- `inactive` — track has been reviewed and is not being pursued; reason documented

## Active Tracks

| Track ID | End-client file | Segment | Stage | Current signal | Next step |
|----------|-----------------|---------|-------|----------------|-----------|
| `TR-003` | Plywood — anti-dumping / countervailing duties (China) | Wood / Forest Products | `contacted` | **CITT PI-2026-001** — Decorative and Other Non-Structural Plywood (China); preliminary injury inquiry initiated April 13, 2026; **determination due June 9, 2026** | Qualify urgently: confirm whether contact is a domestic producer complainant already in the proceeding or an importer seeking to participate before the June 9, 2026 determination |
| `TR-004` | Processed wood — safeguard inquiry | Wood / Forest Products | `contacted` | **CITT GC-2026-001** — Certain Wood Goods; inquiry initiated April 21, 2026; **questionnaire deadline passed May 15, 2026**; public hearings Oct 1-9, 2026; report due Jan 15, 2027 | Reassess viability: confirm whether contact is a domestic producer, importer, or downstream user, and determine whether any practical participation path remains after the missed questionnaire deadline |

## Inactive Tracks

| Track ID | End-client file | Segment | Stage | Reason |
|----------|-----------------|---------|-------|--------|
| `TR-001` | Frozen vegetables imports into Canada — countervailing duties | Agri-food | `inactive` | Industry groups identified are focused on Brazil, not Canada; no engagement with a Canadian scope of work; no prospective end client seeking instructions (ML1, 2026-04-29) |
| `TR-002` | Custom furniture manufacturer — trade remedies | Manufacturing | `inactive` | Not referenced in ML1 pipeline review (2026-04-29); treated as stale pending ML1 confirmation |

## Qualification Criteria

Criteria for advancing a track from `contacted` to `qualified` are defined in:

- [`../26-1639-00001/ANDERSEN_QUALIFICATION_CRITERIA.md`](../26-1639-00001/ANDERSEN_QUALIFICATION_CRITERIA.md)

All seven threshold criteria must be met. When a track is qualified, record the qualification in `NOTES_TO_FILE.md` using the template in that document.

## Operating Notes

- Use [`../26-1639-00001/MATTER_BRIEF.md`](../26-1639-00001/MATTER_BRIEF.md) for Andersen relationship-level management.
- Use [`../26-1639-00001/BUSINESS_DEVELOPMENT_OVERVIEW.md`](../26-1639-00001/BUSINESS_DEVELOPMENT_OVERVIEW.md) for cross-lane Andersen business-development visibility.
- Use this matter for the trade-remedies lane within that Andersen relationship.
- Use [`../../STANDARD/26-259-00003/README.md`](../../STANDARD/26-259-00003/README.md) as the comparison point for LL's own onboarding matter, not as a claim that this pipeline is identical to LL Onboarding.
- Use [`CITT_WATCHLIST.yaml`](CITT_WATCHLIST.yaml) and [`CITT_SIGNAL_REPORT.md`](CITT_SIGNAL_REPORT.md) to monitor official CITT signals relevant to this pipeline.
