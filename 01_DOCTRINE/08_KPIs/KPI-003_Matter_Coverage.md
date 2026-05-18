---
id: kpi-003
title: Matter Coverage KPI
owner: ML1
status: approved
approved_by: ML1
approved_date: 2026-04-18
version: 1.0
created_date: 2026-04-04
last_updated: 2026-04-04
applies_to: [ML2, System, LL]
classification: Margin Realization / System Coverage KPI
tags: [doctrine, kpi, matter-coverage, system-coverage, margin]
---

# KPI-003: Matter Coverage

Classification: Margin Realization / System Coverage KPI

---

## 1. Purpose

Ensure ML2 is actually operating across the full matter portfolio, not selectively or reactively.

Directly tied to ML2 as a margin diagnostic system, not a passive repository.

---

## 2. Definition

% of active matters with at least one system-generated artifact within a defined time window.

---

## 3. Formula

```
Matter Coverage (%) =
  (# of active matters with ≥1 ML2-generated artifact in last N days)
  / (total # of active matters)
```

---

## 4. Parameters

Windows vary by matter class (confirmed 2026-04-04):

| Matter Class | Window |
|--------------|--------|
| Essential | 1 day |
| Strategic | 2 days |
| Standard | TBD |
| Normal | N/A |

---

## 5. What Counts as a System-Generated Artifact

**Valid:**
- Status digest
- Risk summary
- Workflow output
- Structured update

**Invalid:**
- Raw documents
- Manual notes
- External system entries (unless processed by ML2)

---

## 6. Targets

| Coverage Level | Interpretation |
|----------------|----------------|
| ≥ 90% | System fully operational |
| 70–89% | Partial coverage (acceptable early-stage) |
| < 70% | System blind spots — failure condition |

---

## 7. Failure Modes

| Failure | Meaning |
|---------|---------|
| Low coverage | System not scaling across matters |
| Uneven coverage | Certain matter types unsupported |
| Stale artifacts | Coverage illusion — artifacts exist but are outdated |

---

## 8. Diagnostic Use

Low Matter Coverage implies:
- Missing playbooks
- Weak ingestion pipelines
- System not embedded in LL workflow

---

## ML1 Decisions (Confirmed 2026-04-04)

1. Windows vary by matter class: Essential = 1 day, Strategic = 2 days — confirmed
2. Standard and Normal windows: pending
