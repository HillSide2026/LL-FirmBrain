---
id: kpi-sys-core
title: The System Operational KPIs
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
applies_to: [System]
tags: [doctrine, kpi, system, execution, integration, failure]
---

# The System Operational KPIs

Measures execution layer reliability and boundary discipline. Complements
KPI-ML2 (structural health of ML2) and KPI-001/002/003 (operational leverage,
output governance, matter coverage).

---

## KPI-SYS-001 — Integration Failure Rate

**Definition:** % of integration connections that are failed, degraded, or
misconfigured at time of execution

**Formula:** `failed_or_degraded_connections / total_connections`

**Target:** ≤ 2%

**Failure Condition:** > 2%, OR any integration pointing to a wrong endpoint
or operating with over-permissioned scope

**Measurement:** Connection config audit; integration smoke tests

**Frequency:** Monthly; on any config change

**Insight:** Rising rate indicates configuration drift or unmaintained
integrations. The stale hook path (B-001 from 2026-04-18 review) is an
example of this failure mode.

---

## KPI-SYS-002 — Non-Deterministic Execution Rate

**Definition:** % of runs producing different execution paths from equivalent
inputs

**Formula:** `non_deterministic_runs / total_runs`

**Target:** 0%

**Failure Condition:** Any run that cannot be reproduced from the same inputs
and ML2 state, without a documented and bounded reason for variation

**Measurement:** Run log comparison; review for undocumented context
dependencies

**Frequency:** Monthly review of run log patterns

**Insight:** Non-determinism is a system design failure, not an acceptable
operating range. Any non-zero value requires root cause investigation.

---

## KPI-SYS-003 — Data Integrity Error Rate

**Definition:** % of inter-component transfers with schema or content issues

**Formula:** `transfers_with_errors / total_transfers`

**Target:** 0%

**Failure Condition:** Any data loss, schema deviation, or misinterpretation
at a system boundary

**Measurement:** Schema validation at transfer points; run log input/output
comparison

**Frequency:** Per run (logged); monthly aggregate review

**Insight:** Data integrity errors compound — a corrupted transfer early in
a workflow produces invalid outputs downstream without necessarily triggering
a visible failure. Zero tolerance is the only defensible standard.

---

## KPI-SYS-004 — Boundary Breach Incidents

**Definition:** Number of executions that left defined system scope — wrong
paths, unauthorized tools, cross-environment leakage, bypassed gates

**Formula:** Count (not a rate)

**Target:** 0

**Failure Condition:** Any non-zero value. Each incident is individually
reviewed and resolved before the affected workflow resumes.

**Measurement:** Path audit; tool invocation log; gate enforcement records

**Frequency:** Per run (logged); monthly boundary audit

**Insight:** Boundary breaches are not frequency-managed — they are
individually investigated. A ≤ N target would imply tolerance; none exists.

---

## KPI-SYS-005 — Silent Failure Rate

**Definition:** % of failures not explicitly surfaced, logged, and
categorized at time of occurrence

**Formula:** `silent_failures / total_failures`

**Target:** 0%

**Failure Condition:** Any failure that is not logged, not categorized
(schema / doctrine / execution), or not surfaced to ML1 where escalation
is required

**Measurement:** Run log completeness audit; cross-reference failures against
logged events

**Frequency:** Monthly

**Insight:** Silent failures are more dangerous than visible ones — they
allow corrupted state to propagate and make root cause analysis impossible.
The measurement challenge is identifying failures that were not logged.

---

## KPI-SYS-006 — Recovery Success Rate

**Definition:** % of failures handled to a clean resolution without data
corruption or required ML1 escalation

**Formula:** `clean_recoveries / total_failures`

**Target:** ≥ 95%

**Failure Condition:** < 95%, OR any recovery that produces corrupted
downstream state

**Measurement:** Post-failure run log review; outcome classification
(clean recovery / ML1 escalation required / corruption)

**Frequency:** Monthly

**Insight:** Recovery success measures system resilience. Failures below 95%
clean recovery indicate either poor error handling design or failures more
complex than the system was designed to handle — both require ML1 review.
