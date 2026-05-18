---
id: 05_matters__ll_actions__matter_backlog_md
title: Matter Backlog
owner: ML1
status: draft
created_date: 2026-05-18
last_updated: 2026-05-18
tags: [ll, matters, backlog, delivery-stage]
---

# Matter Backlog

Index of open matters with `delivery_stage: active`, `delivery_stage: activated`, or `delivery_stage: backlog`.

Organized by `delivery_status` (tier), then `delivery_stage` within each tier.

Matters with `delivery_stage: parked` or `delivery_stage: finished` are excluded from this view. They are filed in their delivery_status tier folder (`05_MATTERS/NORMAL/`, etc.) with delivery_stage recorded in MATTER.yaml.

Governed by POL-071 (Matter Delivery Stage Policy).

---

## Essential

| Matter ID | Client | Delivery Stage | Fulfillment | Services |
|---|---|---|---|---|
| 25-927-00003 | Stream Ventures Limited | active | urgent | 5 |

---

## Strategic

| Matter ID | Client | Delivery Stage | Fulfillment | Services |
|---|---|---|---|---|
| 24-336-00004 | Mascore Helical Piles | active | active | 2 |
| 25-1231-00001 | Charmaine Spiteri | active | active | 3 |

---

## Standard

| Matter ID | Client | Delivery Stage | Fulfillment | Services |
|---|---|---|---|---|
| 22-194-00006 | Rousseau Mazzuca LLP | active | active | 0 |
| 23-194-00013 | Rousseau Mazzuca LLP | active | active | 0 |
| 23-235-00001 | Baobab Energy Africa Ltd | active | closing | 0 |
| 24-646-00001 | ByNature Design | active | active | 0 |
| 25-1185-00001 | Alexander Klys | active | active | 0 |
| 25-1318-00001 | Zelko Culibrk | active | closing | 0 |
| 25-1363-00001 | Raevan Joy Sambrano | active | closing | 0 |
| 25-1525-00001 | Kleenup Cleaning Services Inc. | active | active | 0 |
| 25-1538-00002 | Georgiana Nicoară | active | active | 0 |
| 25-1553-00001 | 15652227 Canada Inc. | active | active | 0 |
| 25-1571-00001 | Kishmish Inc. | active | active | 0 |
| 25-1588-00001 | Gregory Popov | active | active | 0 |
| 25-1593-00001 | 1001162998 Ontario Corp. o/a KaleMart | active | active | 0 |
| 25-1603-00001 | IBERBANCO LTD | active | closing | 0 |
| 25-1614-00001 | HillSide | active | active | 0 |
| 25-194-00059 | Rousseau Mazzuca LLP | active | active | 0 |
| 25-845-00002 | STAR 333 SPORTS INC. | active | active | 4 |
| 26-259-00003 | LL Onboarding | active | active | 0 |
| 26-1593-00002 | 1001162998 Ontario Corp. o/a KaleMart | active | closing | 0 |

---

## Backlog

Matters with `delivery_stage: backlog` — registered but not yet opened.

| Matter ID | Client | Delivery Status | Notes |
|---|---|---|---|

---

## Classification Pending

Matters with missing or unknown delivery_status. ML1 classification required.

| Matter ID | Client | Issue |
|---|---|---|
| 24-845-00001 | STAR 333 SPORTS INC. | delivery_status unknown |
| 25-256-00005 | Aspire Infusions Inc. | delivery_status unknown |

---

## Governance

- Filing is by `delivery_status` tier: `05_MATTERS/ESSENTIAL/`, `STRATEGIC/`, `STANDARD/`, `NORMAL/`. `delivery_stage` is recorded in MATTER.yaml, not by folder.
- `delivery_stage` is inferred from prior filing location for existing matters pending MATTER.yaml updates. Matters previously in `ESSENTIAL/`, `STRATEGIC/`, `STANDARD/` → `delivery_stage: active`. Matters moved from `PARKED/` to `NORMAL/` → `delivery_stage: parked`.
- Add a matter to the Backlog section on ML1 instruction only.
- Promotion from backlog to active requires ML1 instruction.
- This artifact is a view. Canonical matter records in MATTER.yaml are the source of truth.
- Refresh when MATTER_INDEX is updated or when ML1 changes delivery_stage on a matter.
