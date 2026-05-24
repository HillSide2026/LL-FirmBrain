---
id: sla-004
title: Data Freshness SLA
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
applies_to: [System]
classification: System Core SLA (Runtime Integrity)
tags: [doctrine, sla, system, runtime, data-freshness, integrations]
---

# SLA-004: Data Freshness SLA

Classification: System Core SLA (Runtime Integrity)

---

## 1. Purpose

Ensure that all outputs relying on external or mutable data sources are:
- Temporally valid
- Verifiably current
- Explicit about staleness risk

Prevents silent degradation from stale inputs in a system dependent on Gmail, SharePoint, Clio, and other external integrations.

---

## 2. Guarantee

No System output may incorporate data that exceeds defined freshness thresholds without explicit disclosure and/or escalation.

---

## 3. Data Freshness Classification Model

All data accessed by the System must be classified at read-time:

### D1 — Immutable Data
Examples: signed agreements, filed court documents, finalized PDFs

**Rule:** Always valid once verified. No freshness constraint after integrity check.

### D2 — Semi-Static Internal Data
Examples: ML2 templates, internal notes, doctrine artifacts

**Threshold:** ≤ 24 hours

**Rule:** Cached reads allowed within window. Beyond threshold → must re-validate against source of truth.

### D3 — External Operational Data
Examples: emails (Gmail), matter updates (Clio), working documents (SharePoint)

**Threshold:** ≤ 5 minutes

**Rule:** Cached data beyond threshold → non-compliant. Must re-fetch before use.

### D4 — Real-Time Critical Data
Examples: deadlines, filing statuses, time-sensitive obligations

**Threshold:** 0 tolerance (must be live)

**Rule:** If live read unavailable → MANDATORY ESCALATION to ML1. Output blocked.

---

## 4. Enforcement Rules

### Rule 1 — Freshness Validation Required

Every data read must include:
- Timestamp of retrieval
- Classification (D1–D4)

### Rule 2 — Stale Data Handling

| Condition | System Behavior |
|-----------|----------------|
| Within threshold | Proceed |
| Exceeds threshold | Re-fetch required |
| Cannot re-fetch | Escalate OR block |
| Used despite staleness | SLA violation |

### Rule 3 — Output Disclosure Requirement

If any data is near threshold (>80% of limit), output must include:

> "WARNING: Data freshness approaching SLA threshold"

### Rule 4 — Non-Compliance Conditions

An output is invalid if:
- Stale data used without disclosure
- Freshness cannot be verified
- Classification missing

---

## 5. Logging Requirements

Each run must log:
- Data sources accessed
- Freshness classification
- Timestamps
- Re-fetch events
- Violations

---

## 6. Failure Modes

| Failure | Classification |
|---------|---------------|
| Stale data used silently | Critical |
| Incorrect classification | Major |
| Missing timestamp | Major |
| Re-fetch skipped | Critical |

---

## ML1 Decisions (Confirmed 2026-04-04)

1. D2 threshold: **24 hours** — confirmed
2. D3 threshold: **5 minutes** — confirmed
3. D4: **real-time only, no exceptions** — confirmed
