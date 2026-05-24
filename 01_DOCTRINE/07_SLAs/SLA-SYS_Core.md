---
id: sla-sys-core
title: The System Core SLAs
owner: ML1
status: approved
approved_by: ML1
approved_date: 2026-04-18
version: 1.0
effective_date: 2026-04-18
provenance:
  decided_by: ML1
  decided_on: 2026-04-18
  context: Metadata normalized by system admin cleanup on 2026-05-24
created_date: 2026-04-18
last_updated: 2026-04-18
applies_to: [System]
supersedes: [sla-003]
tags: [doctrine, sla, system, execution, integration, containment]
---

# The System Core SLAs

Operative SLAs for The System as the execution layer. These replace SLA-003
(System Core SLAs), which is marked superseded. SLA-004 (Data Freshness) and
SLA-005 (Matter Isolation) are not superseded.

---

## SLA-SYS-001 — Integration Integrity

**Definition:** All integrations (APIs, MCPs, file systems) must connect to
the correct resources with correct scope.

**Target:** 0 misconfigured or stale connections at time of execution

**Failure Condition:**
- Wrong endpoint or dataset targeted
- Over-permissioned access beyond defined scope
- Broken or stale connection (e.g., path pointing to a moved or renamed
  resource)

**Measurement:** Connection config audit (`.mcp.json`, `.claude/settings.json`);
integration smoke tests against known endpoints

**Frequency:** On any config change; monthly standing audit

---

## SLA-SYS-002 — Execution Determinism

**Definition:** Given identical inputs and identical ML2 state, execution
follows the same steps and produces the same output.

**Target:** 0% non-deterministic runs

**Failure Condition:**
- Different execution paths from identical inputs
- Dependency on hidden context not captured in ML2 state
- Non-repeatable workflows

**Measurement:** Run log comparison across equivalent runs; review for
undocumented context dependencies

**Frequency:** Per run (logged); periodic review of run log patterns

---

## SLA-SYS-003 — State Transfer Fidelity

**Definition:** Data passed between system components remains intact,
correctly structured, and unambiguous at the point of receipt.

**Target:** 0% transfers with data loss or schema deviation

**Failure Condition:**
- Data loss between components
- Schema drift — data arrives in a structure different from what was sent
- Misinterpretation of transferred data across system boundaries

**Measurement:** Schema validation at transfer points; run log input/output
comparison

**Frequency:** Per run (logged); monthly audit of transfer patterns

---

## SLA-SYS-004 — Execution Containment

**Definition:** Execution remains within defined system boundaries — correct
paths, authorized tools, and intended scope.

**Target:** 0 boundary breaches

**Failure Condition:**
- Writes to locations outside allowed paths
- Invocation of tools not authorized for the current workflow
- Cross-environment leakage (e.g., test/prod boundary, matter isolation
  boundary)
- Artifact progression without passing required validation gates (gate
  enforcement — no bypass paths exist; a gate that can be bypassed is
  not a gate)

**Measurement:** Path audit; tool invocation log; gate pass/fail records

**Frequency:** Per run (logged); monthly boundary audit

---

## SLA-SYS-005 — Failure Predictability

**Definition:** Failures are explicit, detectable, logged, and non-destructive.

**Target:** 0% silent failures; all failures categorized as
**schema** / **doctrine** / **execution**

**Failure Condition:**
- Silent failure — execution stops or produces wrong output with no signal
- Partial execution without a logged indication of where and why it stopped
- Cascading errors that corrupt downstream state before the failure is
  surfaced

**Measurement:** Run log completeness audit; failure categorization review

**Frequency:** Per run (logged); monthly pattern review

---

## SLA-SYS-006 — Escalation Fidelity

**Definition:** When The System encounters ambiguity it cannot resolve from
ML2-held doctrine, it stops and surfaces to ML1. It does not guess,
interpolate, or best-effort complete.

**Target:** 0% unescalated ambiguity events

**Failure Condition:**
- The System proceeds on a plausible path when doctrine is silent or
  conflicting
- Inference substituted for escalation
- "Best-effort" output issued where doctrine does not support it

**Measurement:** Escalation log completeness; run log review for inference
events; output audit against controlling artifacts

**Frequency:** Per run (logged); monthly review of escalation patterns

**Note:** Mirrors the No Silent Interpretation constraint in the ML2 layer.
The constraint applies at both layers — ML2 does not fill doctrine gaps by
inference; The System does not fill execution gaps by inference.
