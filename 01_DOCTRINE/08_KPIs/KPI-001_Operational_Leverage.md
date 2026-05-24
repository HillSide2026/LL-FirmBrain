---
id: kpi-001
title: Operational Leverage KPIs
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
applies_to: [ML2, ML1]
tags: [doctrine, kpi, operational, leverage, amplification]
---

# KPI-001: Operational Leverage KPIs

These measure whether ML2 is actually useful — whether ML1 thinking is compounding or leaking.

---

## Reuse Rate

**Definition:** % of work generated from existing artifacts vs. net-new.

**Signal:** Rising reuse rate = system is maturing. Flat or declining = doctrine is not being built up or is not being found.

---

## Decision Codification Latency

**Definition:** Time from ML1 decision → encoded in ML2.

**Signal:** High latency means ML1 is making decisions that live only in conversation or email. Those decisions are not compounding. They are leaking.

---

## Iteration Reduction

**Definition:** Average revisions per deliverable over time.

**Signal:** Should trend downward as templates and playbooks mature. Flat or rising = templates are not absorbing learned patterns.

---

## Time-to-First-Draft

**Definition:** Elapsed time from task initiation to first draft, when work is generated from an approved template.

**Signal:** Measures template coverage and retrieval efficiency. High values suggest missing templates or poor artifact discoverability.

---

## KPI-001-B: Doctrine Utilization Rate

**Definition:** % of ML2 artifacts (templates, playbooks) actively used within a defined time window.

**Why it matters:** Low utilization means doctrine is wrong, not discoverable, or the workflow is bypassing ML2 entirely.

**What low utilization diagnoses:**
- Doctrine does not reflect actual work being done
- Artifacts are not surfaced at the right moment
- ML2 is being bypassed in favor of manual or ad hoc approaches

**Status:** Deferred — revisit once system is operational. Thresholds cannot be set meaningfully before live utilization data exists.
