---
id: sla-ml2-core
title: ML2 Core SLAs
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
applies_to: [ML2]
supersedes: [sla-001, sla-002]
tags: [doctrine, sla, ml2, integrity, traceability, retrieval]
---

# ML2 Core SLAs

Operative SLAs for ML2 as a system-of-record. These replace SLA-001 (ML2
Core SLAs) and SLA-002 (Integrity Compliance Standards), which are marked
superseded. SLA-003 (System Core SLAs) remains operative for The System.

---

## SLA-ML2-001 — Record Integrity

**Definition:** All canonical artifacts must meet required schema and
validation rules.

**Target:** 100% of writes pass validation

**Failure Condition:** Any write bypasses the validator or produces malformed
frontmatter in a canonical path

**Measurement:** Validator logs (`scripts/validate_canonical_write.py`);
write audit trail via git

**Frequency:** Continuous (per-write enforcement)

---

## SLA-ML2-002 — Approval Traceability

**Definition:** All authoritative artifacts must show clear ML1 approval state.

**Target:** 100% of `status: approved` artifacts include both `approved_by`
and `approved_date`

**Failure Condition:** Any `status: approved` artifact missing either field

**Measurement:** Schema audit across `01_DOCTRINE/`, `02_PLAYBOOKS/`

**Frequency:** Weekly

---

## SLA-ML2-003 — Version Traceability

**Definition:** All changes to doctrine must be traceable.

**Target:** 100% of doctrine changes include a version increment or change
marker

**Failure Condition:** Silent overwrite or untracked modification — any change
that cannot be attributed to a specific commit, author, and rationale

**Measurement:** Git diff; version field consistency audit

**Frequency:** Per change (enforced at commit)

---

## SLA-ML2-004 — Retrieval Reliability

**Definition:** Authoritative artifacts must be reliably discoverable.

**Target:** ≥ 95% of retrieval queries return the correct controlling artifact

**Failure Condition:** Retrieval returns a draft in place of an approved
artifact, or returns conflicting artifacts without flagging the conflict

**Measurement:** Manual sampling of retrieval queries against known controlling
artifacts (automated tooling not yet built)

**Frequency:** Monthly

---

## SLA-ML2-005 — Status Clarity

**Definition:** Artifact status must be unambiguous and uniformly applied.

**Target:** 0 unresolved status ambiguities; single approved vocabulary
(`approved`, `draft`, `superseded`) enforced across all canonical paths

**Failure Condition:** Introduction of a new status value without ML1
approval; reappearance of `active` or other vocabulary variants

**Measurement:** Status field audit across canonical directories

**Frequency:** Monthly

**Current baseline:** 0 ambiguities as of 2026-04-18 (vocabulary unified
from `active`/`approved`/`draft` to `approved`/`draft`/`superseded`).
