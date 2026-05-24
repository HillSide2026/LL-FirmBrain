---
id: 01_doctrine__07_slas__readme_md
title: SLAs
owner: ML1
status: approved
approved_by: ML1
approved_date: 2026-04-18
version: 1.1
effective_date: 2026-04-18
supersedes:
provenance:
  decided_by: ML1
  decided_on: 2026-04-18
  context: Metadata normalized by system admin cleanup on 2026-05-24
created_date: 2026-03-31
last_updated: 2026-04-18
tags: [doctrine, slas]
---

# SLAs

## Three-Layer SLA Structure

SLAs are organized in three layers. Each layer governs a distinct scope.
A breach at any lower layer constitutes a breach of the corresponding
SLA-SB entry above it.

```
ML1 — judgment
 └── SLA-SB (Second Brain) — governs ML2 and The System as a whole
      ├── SLA-ML2 (ML2) — record integrity, approval, traceability, retrieval
      └── SLA-SYS (System) — integration, execution, containment, failure
```

## Active SLAs

| File | ID | Layer | Scope |
|---|---|---|---|
| `SLA-SB_Core.md` | sla-sb-core | Second Brain | SLA-SB-001–005: Integrity, Authority Discipline, Traceability, Boundary Discipline, Operational Reliability |
| `SLA-ML2_Core.md` | sla-ml2-core | ML2 | SLA-ML2-001–005: Record Integrity, Approval Traceability, Version Traceability, Retrieval Reliability, Status Clarity |
| `SLA-SYS_Core.md` | sla-sys-core | System | SLA-SYS-001–006: Integration Integrity, Execution Determinism, State Transfer Fidelity, Execution Containment, Failure Predictability, Escalation Fidelity |
| `SLA-004_Data_Freshness.md` | sla-004 | System | Data freshness thresholds by classification (D1–D4) |
| `SLA-005_Matter_Isolation.md` | sla-005 | ML2 + System | Matter-level isolation; zero cross-matter contamination |

## Superseded SLAs

| File | Superseded by |
|---|---|
| `SLA-001_ML2_Core_SLAs.md` | sla-ml2-core |
| `SLA-002_Integrity_Compliance_Standards.md` | sla-ml2-core |
| `SLA-003_System_Core_SLAs.md` | sla-sys-core |

## Naming Convention

| Layer | Format |
|---|---|
| Second Brain | `SLA-SB-001`, `SLA-SB-002`, … |
| ML2 | `SLA-ML2-001`, `SLA-ML2-002`, … |
| System | `SLA-SYS-001`, `SLA-SYS-002`, … |
| Legacy / standalone | `SLA-004`, `SLA-005`, … (retain existing IDs) |
