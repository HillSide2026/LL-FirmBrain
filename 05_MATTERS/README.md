---
id: MATTERS-README

title: 05_MATTERS
owner: ML1
status: draft
created_date: 2026-01-30
last_updated: 2026-03-28
tags: [matter]
---

# 05_MATTERS

## Purpose

This directory contains matter-level information organized by **Delivery Status**.

Folder placement reflects `delivery_status` only. The other fields (`status`, `fulfillment_status`, `services`) are metadata stored in each matter's `MATTER.yaml`.

---

## Directory Structure

```
05_MATTERS/
├── ESSENTIAL/      # Highest delivery attention
├── STRATEGIC/      # Strategic importance
├── STANDARD/       # Normal priority
├── PARKED/         # Temporarily deprioritized
└── LL_ACTIONS/     # LL task hub — indexes LL_TASK_TRACKER.md and content backlogs
```

---

## ESSENTIAL

| matter_id | matter_name | status | delivery_status | fulfillment_status | path |
|-----------|-------------|--------|-----------------|-------------------|------|
| 25-927-00003 | Stream Ventures Limited | Open | Essential | urgent | `ESSENTIAL/25-927-00003/` |
| 26-1639-00001 | Andersen | Open | Essential | active | `ESSENTIAL/26-1639-00001/` |
| 26-1639-00002 | Andersen | Open | Essential | active | `ESSENTIAL/26-1639-00002/` |
| 26-1639-00003 | Andersen | Open | Essential | active | `ESSENTIAL/26-1639-00003/` |
| 26-927-00004 | Stream Ventures Limited | Open | Essential | active | `ESSENTIAL/26-927-00004/` |

---

## STRATEGIC

| matter_id | matter_name | status | delivery_status | fulfillment_status | path |
|-----------|-------------|--------|-----------------|-------------------|------|
| 24-336-00004 | Mascore Helical Piles | Open | Strategic | active | `STRATEGIC/24-336-00004/` |
| 25-1231-00001 | Charmaine Spiteri | Open | Strategic | active | `STRATEGIC/25-1231-00001/` |
| 25-256-00005 | Aspire Infusions Inc | Open | Strategic | active | `STRATEGIC/25-256-00005/` |
| 26-1631-00001 | 1713425 Ontario Inc. (Tejvir Boparai) | Open | Strategic | active | `STRATEGIC/26-1631-00001/` |

---

## STANDARD

| matter_id | matter_name | status | delivery_status | fulfillment_status | path |
|-----------|-------------|--------|-----------------|-------------------|------|
| 22-194-00006 | Rousseau Mazzuca LLP | Open | Standard | active | `STANDARD/22-194-00006/` |
| 23-194-00013 | Rousseau Mazzuca LLP | Open | Standard | active | `STANDARD/23-194-00013/` |
| 23-235-00001 | Baobab Energy Africa Ltd | Open | Standard | active | `STANDARD/23-235-00001/` |
| 24-646-00001 | ByNature Design | Open | Standard | active | `STANDARD/24-646-00001/` |
| 25-1185-00001 | Alexander Klys | Open | Standard | active | `STANDARD/25-1185-00001/` |
| 25-1363-00001 | Raevan Joy Sambrano | Open | Standard | active | `STANDARD/25-1363-00001/` |
| 25-1525-00001 | Kleenup Cleaning Services Inc. | Open | Standard | active | `STANDARD/25-1525-00001/` |
| 25-1538-00002 | Georgiana Nicoară | Open | Standard | active | `STANDARD/25-1538-00002/` |
| 25-1553-00001 | 15652227 Canada Inc. | Open | Standard | active | `STANDARD/25-1553-00001/` |
| 25-1571-00001 | Kishmish Inc. | Open | Standard | active | `STANDARD/25-1571-00001/` |
| 25-1588-00001 | Gregory Popov | Open | Standard | active | `STANDARD/25-1588-00001/` |
| 25-1593-00001 | 1001162998 Ontario Corp. o/a KaleMart | Open | Standard | active | `STANDARD/25-1593-00001/` |
| 25-1603-00001 | IBERBANCO LTD | Open | Standard | active | `STANDARD/25-1603-00001/` |
| 25-1614-00001 | HillSide | Open | Standard | active | `STANDARD/25-1614-00001/` |
| 25-194-00059 | Rousseau Mazzuca LLP | Open | Standard | active | `STANDARD/25-194-00059/` |
| 25-845-00001 | STAR 333 SPORTS INC. | Open | Standard | active | `STANDARD/25-845-00001/` |
| 25-845-00002 | STAR 333 SPORTS INC. | Open | Standard | active | `STANDARD/25-845-00002/` |
| 25-1318-00001 | Zelko Culibrk | Open | Standard | closing | `STANDARD/25-1318-00001/` |
| 26-1593-00002 | 1001162998 Ontario Corp. o/a KaleMart | Open | Standard | closing | `STANDARD/26-1593-00002/` |
| 26-259-00003 | LL Onboarding | Open | Standard | active | `STANDARD/26-259-00003/` |

---

## PARKED

| matter_id | matter_name | status | delivery_status | fulfillment_status | path |
|-----------|-------------|--------|-----------------|-------------------|------|
| 23-169-00003 | Best Bottles Inc. | Open | Parked | active | `PARKED/23-169-00003/` |
| 24-347-00002 | Brand Butter | Open | Parked | inactive | `PARKED/24-347-00002/` |
| 24-409-00001 | A. Mukherjee & Co. | Open | Parked | inactive | `PARKED/24-409-00001/` |
| 24-601-00001 | Meta Bytes North America Inc | Open | Parked | inactive | `PARKED/24-601-00001/` |
| 24-682-00002 | Stream Ventures Limited | Open | Parked | inactive | `PARKED/24-682-00002/` |
| 25-1024-00001 | AllPro Construction Group | Open | Parked | active | `PARKED/25-1024-00001/` |
| 25-1192-00001 | The Knot Churros International Limited | Open | Parked | active | `PARKED/25-1192-00001/` |
| 25-174-00001 | Danielle Thompson | Open | Parked | inactive | `PARKED/25-174-00001/` |
| 25-192-00003 | If Not Me Inc | Open | Parked | inactive | `PARKED/25-192-00003/` |
| 25-822-00001 | Majid Hajibeigy | Open | Parked | active | `PARKED/25-822-00001/` |
| 26-1630-00001 | Marcela Hernandez | Open | Parked | keep in view | `PARKED/26-1630-00001/` |

---

## Field Model

| Field | Storage | Source | Values |
|-------|---------|--------|--------|
| `status` | Metadata | Clio | Open \| Pending \| Closed |
| `delivery_status` | Directory | ML1 | Essential \| Strategic \| Standard \| Parked |
| `fulfillment_status` | Metadata | Admin | urgent \| active \| keep in view \| dormant \| inactive \| pausing |
| `services` | Metadata | ML1/Admin | Canonical service list (`solution` and `strategy` types) |

**Non-inference rule:** Do not infer any field from any other.

## Derived Categories

- `ML Active` (computed, not stored):
  - `status` in `Open|Pending`
  - `delivery_status` in `Essential|Strategic|Standard`
  - `fulfillment_status` in `urgent|active`
- `ML Watch` (computed, not stored):
  - `status` in `Open|Pending`
  - `delivery_status` = `Parked`
  - `fulfillment_status` in `keep in view|active|urgent`

## Services Model

Use `services` as the canonical umbrella for both playbook concepts:
- `service_type: solution`
- `service_type: strategy`

Legacy fields (`solutions`, `strategies`) may exist and are normalized into `services` at runtime.
