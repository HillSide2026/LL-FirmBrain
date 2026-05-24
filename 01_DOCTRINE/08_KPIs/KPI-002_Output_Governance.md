---
id: kpi-002
title: Output Governance KPIs
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
created_date: 2026-03-31
last_updated: 2026-03-31
applies_to: [ML2, System, LL]
tags: [doctrine, kpi, governance, output, safety]
---

# KPI-002: Output Governance KPIs

These protect the boundary between ML2 and LL. If these rise, the system is losing control.

---

## Unauthorized Output Rate

**Definition:** Outputs used by LL without ML1 approval.

**Signal:** Any non-zero value is a governance failure. This is not a metric to optimize toward a target — it is a binary compliance indicator. Rising trend requires immediate escalation.

---

## Template Fidelity Score

**Definition:** Degree to which outputs match approved templates.

**Signal:** Declining fidelity means outputs are drifting from the approved artifact layer. Correlate with Drift Rate (SLA-002) to distinguish system error from template gaps.

---

## Exception Frequency

**Definition:** How often LL needs to escalate beyond system rules.

**Signal:** Rising frequency signals either (a) doctrine has gaps the system cannot resolve, or (b) the system is not surfacing relevant doctrine. Both require ML1 intervention — the cause determines the fix.

---

## KPI-002-D: Gate Pass Rate

Classification: Design Quality KPI (not execution)

**Definition:** % of artifacts that pass all required gates on first attempt, with no revisions.

**Formula:**
```
Gate Pass Rate (%) =
  (# artifacts passing all gates on first attempt)
  / (total artifacts processed)
```

**Targets:**

| Pass Rate | Interpretation |
|-----------|----------------|
| ≥ 85% | Strong doctrine + templates |
| 70–84% | Moderate friction |
| < 70% | System design failure |

**What counts as a gate failure:**
- Missing required fields
- Schema violations
- Template deviation
- Failed validation checks
- Escalation triggered due to ambiguity

**What this KPI diagnoses:**

| Symptom | Root Cause |
|---------|-----------|
| Low pass rate | Unclear doctrine |
| Repeated same failures | Bad template design |
| High variance | Inconsistent system rules |

**Relationship to SLAs:** Enforces SLA-001 (Traceability & Integrity). Reinforces SLA-003 (Gate Enforcement).

**ML1 Decision (Confirmed 2026-04-04):** Escalation triggered due to ambiguity counts as a gate failure — YES

---

## KPI-002-E: Escalation Resolution Rate

**Definition:** % of escalations that are resolved and codified into ML2 within a defined time window.

**Why it matters:** Escalation frequency is already measured. This KPI closes the loop — it measures whether ML1 decisions actually re-enter the system as doctrine.

**Key insight:** Unresolved escalations = system learning failure. The escalation happened but the system did not improve.

**Resolution window (confirmed 2026-04-04):** 2 days. An escalation unresolved after 2 days is flagged as a learning failure.
