---
id: sla-003
title: System Core SLAs
owner: ML1
status: superseded
superseded_by: sla-sys-core
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
last_updated: 2026-04-04
applies_to: [System]
tags: [doctrine, sla, system, runtime, execution]
---

# SLA-003: System Core SLAs

Defines how the System runtime behaves. These are runtime guarantees, distinct from ML2 integrity (SLA-001) and compliance measurement (SLA-002).

---

## 1. Execution Determinism

Same input + same ML2 state → same output.

Non-deterministic variation must be bounded or flagged. Variation that is neither bounded nor flagged is a runtime failure, not an acceptable output range.

---

## 2. Gate Enforcement

No artifact progresses stages unless:
- Validation checks pass
- Required fields are complete

No bypass paths exist. A gate that can be bypassed is not a gate.

---

## 3. Escalation Fidelity

Ambiguity → escalate to ML1.

The System must not:
- Guess
- Interpolate
- "Best-effort complete"

This mirrors the No Silent Interpretation SLA in SLA-001. The same constraint applies at the runtime layer: when the System cannot determine the correct path, it stops and surfaces — it does not proceed on a plausible path.

---

## 4. State Awareness

Every run must log:
- **Inputs** — what was received
- **Outputs** — what was generated
- **Referenced artifacts** — what doctrine or templates were used

This supports the Traceability SLA (SLA-001). A run with no state log is a compliance failure.

---

## 5. Failure Visibility

Failures must be:
- Explicit
- Logged
- Categorized as one of: **schema** / **doctrine** / **execution**

No silent degradation. A system that fails quietly is more dangerous than one that fails loudly.
