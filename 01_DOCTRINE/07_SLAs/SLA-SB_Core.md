---
id: sla-sb-core
title: Second Brain Core SLAs
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
created_date: 2026-04-18
last_updated: 2026-04-18
applies_to: [ML2, System]
tags: [doctrine, sla, second-brain, governance, integrity, authority]
---

# Second Brain Core SLAs

Governing SLAs for the Second Brain as a whole. These operate at a higher
level of abstraction than the ML2 and System SLAs. A breach of any downstream
SLA constitutes a breach of the corresponding SLA-SB entry.

The Second Brain comprises two components:
- **ML2** — the system-of-record. Holds ML1-approved doctrine, artifacts,
  and decisions. Governs: record integrity, schema compliance, approval
  traceability, versioning, retrieval reliability.
- **The System** — the execution layer. Operates across external environments,
  tools, and interfaces using only artifacts held in ML2. Governs: integration
  correctness, execution behavior, state transfer, failure handling, boundary
  containment.

---

## SLA-SB-001 — Integrity

**Commitment:** The Second Brain produces, holds, and transfers correct,
valid, and schema-compliant artifacts and data.

**Governs:** ML2 + System

**Downstream SLAs:**
- SLA-ML2-001 — Record Integrity
- SLA-ML2-005 — Status Clarity
- SLA-SYS-001 — Integration Integrity
- SLA-SYS-003 — State Transfer Fidelity
- SLA-004 — Data Freshness

**Breach rule:** A breach of any downstream SLA listed above constitutes a
breach of SLA-SB-001.

---

## SLA-SB-002 — Authority Discipline

**Commitment:** All authoritative artifacts carry visible ML1 approval. The
Second Brain does not exercise independent judgment. Ambiguity escalates to
ML1 — it is never resolved by inference.

**Governs:** ML2 + System

**Downstream SLAs:**
- SLA-ML2-002 — Approval Traceability
- SLA-SYS-006 — Escalation Fidelity

**Breach rule:** A breach of any downstream SLA listed above constitutes a
breach of SLA-SB-002.

---

## SLA-SB-003 — Traceability

**Commitment:** All changes to doctrine, all artifacts, and all outputs are
traceable to their origin. Authoritative artifacts are reliably discoverable
at the point of use.

**Governs:** ML2 + System

**Downstream SLAs:**
- SLA-ML2-003 — Version Traceability
- SLA-ML2-004 — Retrieval Reliability

**Breach rule:** A breach of any downstream SLA listed above constitutes a
breach of SLA-SB-003.

---

## SLA-SB-004 — Boundary Discipline

**Commitment:** Execution and record-keeping remain within defined scope and
matter boundaries. No scope leakage. No cross-matter contamination.

**Governs:** ML2 + System

**Downstream SLAs:**
- SLA-SYS-004 — Execution Containment
- SLA-005 — Matter Isolation

**Breach rule:** A breach of any downstream SLA listed above constitutes a
breach of SLA-SB-004.

---

## SLA-SB-005 — Operational Reliability

**Commitment:** The Second Brain operates consistently and predictably.
Failures are visible, logged, categorized, and surfaced. The Second Brain
never fails silently or non-deterministically.

**Governs:** ML2 + System

**Downstream SLAs:**
- SLA-SYS-002 — Execution Determinism
- SLA-SYS-005 — Failure Predictability

**Breach rule:** A breach of any downstream SLA listed above constitutes a
breach of SLA-SB-005.
