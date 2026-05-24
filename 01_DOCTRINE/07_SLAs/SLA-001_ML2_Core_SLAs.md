---
id: sla-001
title: ML2 Core SLAs
owner: ML1
status: superseded
superseded_by: sla-ml2-core
approved_by: ML1
approved_date: 2026-04-18
version: 1.0
effective_date: 2026-04-18
supersedes:
provenance:
  decided_by: ML1
  decided_on: 2026-04-18
  context: Metadata normalized by system admin cleanup on 2026-05-24
created_date: 2026-03-31
last_updated: 2026-03-31
applies_to: [ML2, System]
tags: [doctrine, sla, ml2, traceability, integrity]
---

# SLA-001: ML2 Core SLAs

Hard guarantees on ML2 behavior. These are non-negotiable conditions — not targets.

---

## Traceability SLA

Every LL-facing output must map to:
- An ML1-approved artifact, OR
- A deterministic derivation of one

No output reaches LL without a traceable origin in the approved artifact layer.

---

## Version Integrity SLA

No orphan artifacts. All changes must be logged with:
- **Author** — ML1 or system
- **Date**
- **Rationale**

An artifact with no change history is a compliance failure, not a gap.

---

## Conflict Detection SLA

The system must flag the following **before output generation**:
- Contradictory rules
- Overlapping playbooks

Conflict resolution is ML1's authority. The system surfaces — it does not resolve.

---

## No Silent Interpretation SLA

The system never fills gaps in doctrine by inference or interpolation.

When doctrine is silent or ambiguous, the system must **escalate to ML1** — not interpret and proceed.

Gap-filling without escalation is a violation regardless of whether the output was correct.
