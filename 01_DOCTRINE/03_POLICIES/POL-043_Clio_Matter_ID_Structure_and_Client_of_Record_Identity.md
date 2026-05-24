---
id: POL-043
title: Clio Matter ID Structure and Client-of-Record Identity
owner: ML1
status: approved
approval: ML1
approved_by: ML1
approved_date: 2026-04-18
version: 0.1
effective_date: 2026-04-18
supersedes:
provenance:
  decided_by: ML1
  decided_on: 2026-04-18
  context: Metadata normalized by system admin cleanup on 2026-05-24
created_date: 2026-03-09
last_updated: 2026-03-09
tags: [policy, matters, clio, identity, matter-id]
---

# POL-043 — Clio Matter ID Structure and Client-of-Record Identity

Policy Statement: Clio matter IDs are canonical and must be interpreted using a fixed structure. The middle segment identifies the client-of-record contact code and must not be reinterpreted as a generic party or alias.

Authority (Principles referenced): PRN-003, PRN-005, PRN-009, PRN-020  
Enforcement expectation: Any mapping or automation that treats matter ID segments inconsistently with this policy is non-compliant and must be corrected or escalated.  
Supersedes: None  
Enforcement Protocol: PRO-014

---

## 1. Purpose

This policy defines how Clio matter IDs are structured and how identity semantics must be interpreted across systems (ML2, Clio, SharePoint, Asana, Gmail labels, and related integrations).

The objective is to prevent identity drift and ambiguous routing.

---

## 2. Canonical Matter ID Format

Canonical format:

```text
YY-CCC(C)-NNNNN
```

Regex:

```text
\d{2}-\d{3,4}-\d{5}
```

Example: `25-927-00003`

---

## 3. Segment Semantics

Segment 1 (`YY`):
- The two-digit year in which the specific sub-matter is created.

Segment 2 (`CCC` or `CCCC`):
- The designated client-of-record contact code for the matter.

Segment 3 (`NNNNN`):
- The zero-padded sequence count of matters associated to that client-of-record contact code.

---

## 4. Client and Contact Identity Rules

1. A contact may exist without a matter.
2. Without a matter, there is no client.
3. Client status is matter-bound: a contact becomes a client-of-record only when tied to a matter.
4. A client has one and only one client contact record.
5. A contact code maps to one and only one client contact record.
6. The matter ID middle segment is that client-of-record contact code.
7. A person/operator may control or represent multiple entities that each appear in the system as clients; each such client has its own client contact record and contact code.

---

## 5. Non-Client Contacts

A matter may include multiple non-client associated contacts (for example: officers, counterparties, advisors, signatories).

These contacts:
- do not redefine client-of-record identity
- do not change the matter ID middle segment
- must be represented as associated contacts, not as matter identifier substitutions

---

## 6. Interpretation and Routing Rules

1. `matter_id` is the canonical cross-system key.
2. Segment 2 must be interpreted as client-of-record contact code only.
3. Any alias mapping must preserve this semantics.
4. If source-system data conflicts with this policy, routing must halt and escalate for ML1 review.

---

## 7. Validation Requirements

Validation checks must enforce:
- format compliance (`YY-CCC(C)-NNNNN`)
- immutable `matter_id` usage once recorded
- no client designation without at least one linked matter
- exactly one client-of-record contact per matter
- unique contact-code mapping to one client contact record
- no reassignment of middle-segment contact code semantics

---

## 8. Change Control and Exceptions

Changes to matter identifier interpretation rules require ML1 approval.

If historical data requires reconciliation:
- preserve canonical `matter_id`
- record explicit mapping/remediation artifacts
- prohibit silent reinterpretation

---

## 9. Related Doctrine

- `01_DOCTRINE/01_INVARIANTS/INV-0003-matter-model-structural-invariants.md`
- `01_DOCTRINE/03_POLICIES/POL-042_Inbox_Governance_Policy.md`
- `01_DOCTRINE/05_PROTOCOLS/PRO-014_Inbox_Governance_Protocol.md`

---

## 10. Summary

Clio matter IDs are canonical and structurally meaningful:
- `YY` = sub-matter creation year
- middle segment = client-of-record contact code
- final segment = per-client matter sequence

Client-of-record identity is strict and non-interchangeable with non-client contacts.
Contact existence and client status are distinct: contacts may exist pre-matter, but client status cannot.
