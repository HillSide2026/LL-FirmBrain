---
id: kpi-ml2-core
title: ML2 Structural Health KPIs
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
applies_to: [ML2]
tags: [doctrine, kpi, ml2, structural-health, schema, retrieval]
---

# ML2 Structural Health KPIs

Measures ML2 integrity and reliability as a system-of-record. Complements
KPI-001 (Operational Leverage), KPI-002 (Output Governance), and KPI-003
(Matter Coverage) — which remain operative and are not superseded.

---

## KPI-ML2-001 — Doctrine Approval Coverage

**Definition:** % of doctrine artifacts that are ML1-approved

**Formula:** `approved_artifacts / total_artifacts`

**Target:** ≥ 95%

**Failure Condition:** < 95% (allows for legitimate short-lived drafts;
does not permit backslide from a previously higher baseline)

**Measurement:** Status audit across `01_DOCTRINE/`, `02_PLAYBOOKS/`

**Frequency:** Weekly

**Insight:** Measures system maturity. Decline signals unapproved doctrine
entering production or approved artifacts being demoted without ML1 direction.

**Current baseline:** ~100% as of 2026-04-18 (post bulk-promotion).

---

## KPI-ML2-002 — Draft Backlog Size

**Definition:** Number of `status: draft` artifacts in canonical directories

**Target:** ≤ 10 outstanding drafts at any time; any draft older than 30
days without a recorded blocker reason is a failure condition

**Failure Condition:** > 10 drafts, OR any single draft outstanding > 30
days with no recorded reason

**Measurement:** Status audit across `01_DOCTRINE/`, `02_PLAYBOOKS/`

**Frequency:** Weekly

**Insight:** Indicates unresolved decisions. Rising draft count means ML1
decisions are not being codified or doctrine is being created without
completing the approval cycle.

---

## KPI-ML2-003 — Conflict Rate

**Definition:** Number of conflicting artifact pairs identified (contradictory
rules, overlapping scope, inconsistent standards)

**Target:** 0

**Failure Condition:** Any unresolved conflict pair. Detection triggers
escalation to ML1 under SLA-ML2-001; resolution is ML1's authority.

**Measurement:** Manual audit; automated detection not yet built

**Frequency:** Monthly

**Insight:** Measures coherence. Any non-zero value must be resolved before
the conflicting artifacts are eligible for production use.

---

## KPI-ML2-004 — Schema Compliance Rate

**Definition:** % of artifacts in canonical directories meeting frontmatter
schema requirements (`status`, `owner`, `approved_by`, `approved_date` where
applicable)

**Formula:** `schema_compliant_artifacts / total_artifacts`

**Target:** 100%

**Failure Condition:** Any artifact with missing required fields in a
canonical directory. Non-compliant artifacts are not operative regardless
of content quality.

**Measurement:** Validator logs; periodic frontmatter audit

**Frequency:** Weekly

**Insight:** Measures structural integrity. A decline here means writes are
bypassing the validator (SLA-ML2-001 failure) or fields are being removed
without ML1 direction.

---

## KPI-ML2-005 — Retrieval Precision

**Definition:** % of test queries returning the correct controlling artifact
on first retrieval

**Formula:** `correct_retrievals / total_test_queries`

**Target:** ≥ 95%

**Failure Condition:** < 95%, OR any query that returns a superseded or draft
artifact in place of an approved one without flagging the conflict

**Measurement:** Manual sampling against known controlling artifacts (automated
tooling not yet built)

**Frequency:** Monthly

**Insight:** Measures usability of ML2. Low precision means structure, naming,
or indexing is misleading agents and reviewers toward non-authoritative material.

---

## KPI-ML2-006 — Orphan Artifact Rate

**Definition:** % of artifacts in ML2 not referenced by any workflow, index,
or controlling doctrine

**Formula:** `unreferenced_artifacts / total_artifacts`

**Target:** ≤ 5%

**Failure Condition:** > 5%, OR any orphan artifact in `01_DOCTRINE/01_INVARIANTS/`
(invariants must always have referencing doctrine)

**Measurement:** Index cross-reference analysis — manual audit until
automated tooling is built

**Frequency:** Monthly

**Insight:** Measures structural drift. High orphan rate means doctrine is
being created faster than it is being integrated, or artifacts have been
abandoned without being archived.
