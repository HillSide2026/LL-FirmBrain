---
id: sla-005
title: Matter Isolation SLA
owner: ML1
status: approved
approved_by: ML1
approved_date: 2026-04-18
version: 1.0
effective_date: 2026-04-18
supersedes:
provenance:
  decided_by: ML1
  decided_on: 2026-04-18
  context: Metadata normalized by system admin cleanup on 2026-05-24
created_date: 2026-04-04
last_updated: 2026-04-04
applies_to: [ML2, System]
classification: System Core SLA (Security + Boundary Enforcement)
tags: [doctrine, sla, system, matter-isolation, confidentiality, security]
---

# SLA-005: Matter Isolation SLA

Classification: System Core SLA (Security + Boundary Enforcement)

---

## 1. Purpose

Guarantee strict matter-level isolation in a multi-matter legal system.

Prevents:
- Data leakage across matters
- Cross-contamination of outputs
- Breach of client confidentiality

---

## 2. Guarantee

No data from one matter may be accessed, referenced, or included in another matter's execution or output unless explicitly authorized by ML1.

---

## 3. Core Principle

Each matter is treated as a sealed execution boundary — equivalent to an isolated memory space with zero implicit shared context.

---

## 4. Isolation Rules

### Rule 1 — Context Binding

Every run must be explicitly bound to:
- A single Matter ID
- A defined task scope

If either is missing → execution blocked.

### Rule 2 — Read Isolation

System may only read:
- Artifacts tagged to the active Matter ID
- Global ML2 doctrine (read-only)

System may NOT read:
- Artifacts from other matters
- Prior runs from unrelated matters

### Rule 3 — Write Isolation

All outputs must be written to the same Matter ID namespace. No cross-matter writes allowed under any condition.

### Rule 4 — No Implicit Memory

The System must not reuse context from prior runs in different matters or carry forward latent memory across matters. Each run is stateless with respect to other matters.

### Rule 5 — Explicit Cross-Matter Exception

Cross-matter access is only allowed if:
- ML1 explicitly authorizes it
- Authorization is recorded in ML2
- Scope of sharing is defined

Without this → hard prohibition.

---

## 5. Output Validation

Before output is released, System must validate:
- All referenced artifacts belong to the same Matter ID
- No foreign identifiers present
- No semantic leakage (names, facts, clauses)

---

## 6. Detection Mechanisms

System must actively check for:
- Entity mismatch (client names, parties)
- Document ID mismatch
- Metadata inconsistency

If detected → execution halted, flag: **ISOLATION BREACH RISK**

---

## 7. Logging Requirements

Each run must log:
- Matter ID
- All accessed artifacts (IDs + matter association)
- Validation results
- Any blocked cross-access attempts

---

## 8. Failure Classification

| Failure | Severity |
|---------|----------|
| Cross-matter data included in output | Critical |
| Unauthorized read attempt | Critical |
| Missing matter binding | Critical |
| Incomplete validation | Major |

---

## 9. Relationship to Other SLAs

- Supports **SLA-SB-003** (Traceability) — operationalized by SLA-ML2-003 and SLA-ML2-004
- Reinforces **SLA-SB-004** (Boundary Discipline) — operationalized by SLA-SYS-004
- Enables **KPI-002** (Unauthorized Output Rate = 0)

---

## ML1 Decisions (Confirmed 2026-04-04)

1. Zero cross-matter memory: **YES** — confirmed
2. ML1-only override authority: **YES** — confirmed
