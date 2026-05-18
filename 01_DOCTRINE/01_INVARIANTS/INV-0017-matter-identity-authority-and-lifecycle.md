---
id: INV-0017
title: 'INV-0017: Matter Identity Authority and Lifecycle'
owner: ML1
status: approved
approved_by: ML1
approved_date: 2026-05-04
version: 1.0
created_date: 2026-05-04
last_updated: 2026-05-04
tags: [invariant, matter, identity, authority]

effective_date: 2026-05-04
supersedes:

provenance:
  decided_by: ML1
  decided_on: 2026-05-04
  context: Clarifies who creates and authorizes matter_id and defines the canonical lifecycle for matter identity
---

# INV-0017 — Matter Identity Authority and Lifecycle

**Invariant ID:** INV-0017  
**Status:** APPROVED  
**Effective:** 2026-05-04  
**Authority:** ML1

---

## 1. Purpose

Define the **authoritative source and lifecycle for matter identity** (`matter_id`) across the Second Brain system.

Specifically:
- Who has authority to create and authorize new matter identities
- What qualifies as an authoritative matter record
- How matter_id persists and remains immutable once created
- The relationship between matter_id and external system records (Clio, SharePoint, etc.)

---

## 2. Matter Identity Authority

### 2.1 Primary Authority — Matter Creation

Matter identity creation is an **ML1-authorized action**.

A new matter is created when:

1. **Client Engagement Decision**  
   ML1 (or delegate acting under ML1 authority) decides to engage on a client matter.

2. **Matter Record Creation**  
   The matter is formally recorded in the canonical matter registry (`05_MATTERS/INDEX.md` and corresponding `05_MATTERS/MATTER_REGISTRY.md`).

3. **matter_id Assignment**  
   A globally unique `matter_id` is assigned and recorded.

4. **External System Registration**  
   The matter is registered in Clio (or other authoritative external system) to establish the Clio Matter Number mapping.

### 2.2 Secondary Authority — Matter Metadata Administration

Once a matter is created, day-to-day metadata administration (status updates, deadline changes, service additions) is delegated to System agents and workflows **within explicitly defined policy gates**.

- **Agent Authority Boundary:** Agents may update operational metadata (status, service stages, deadline signals) **only within the scope of approved protocols** (e.g., PRO-015, PRO-016, PRO-019).
- **No Autonomous Creation:** Agents may **not** create new matter identities.
- **No Autonomous Termination:** Agents may not unilaterally close or archive a matter; closure signals are escalated for ML1 review.

### 2.3 External System Synchronization

Clio, SharePoint, and other integrated systems **do not create matter identity**.

They are synchronized **with** matter identity (downstream):

- Clio Matter Number is a **mapping attribute** of matter_id, not the source of truth.
- SharePoint matter folders are **federated storage** for the matter; they do not define matter identity.
- Gmail threads are **evidence and context** for the matter; they do not create or redefine it.

If an external system record exists without a corresponding canonical matter record in ML2, the matter is **unregistered**. Unregistered matters must be **registered by ML1 decision** before being treated as canonical.

---

## 3. Matter Identity Immutability

Once assigned, `matter_id`:

- **Must not change** over the life of the matter
- **Must not be reused** for a different engagement
- **Must not be merged** with another matter_id

If matter records must be consolidated or restructured, a new matter_id is assigned and the prior matter is marked as **superseded** (not deleted).

---

## 4. Matter Registration Process

### 4.1 New Matter Workflow

1. **Decision**  
   ML1 approves engagement.

2. **Registration**  
   Matter is added to `05_MATTERS/INDEX.md` and `05_MATTERS/MATTER_REGISTRY.md` with:
   - matter_id (assigned by system, unique)
   - client_name
   - matter_description
   - engagement_date
   - status (`open`)
   - delivery_status (initial value)
   - fulfillment_status (initial value)
   - associated_matter_type (e.g., `standard`, `strategic`, `essential`)

3. **External Registration**  
   Matter is created in Clio with corresponding Matter Number.
   Matter Number is added to canonical matter record as `clio_matter_id`.

4. **Matter File Staging**  
   SharePoint matter folder is created or mapped (if applicable).
   Matter folder reference is added to canonical record.

### 4.2 Matter Closure Workflow

1. **Closure Signal**  
   Agent or ML1 signals that matter should close.

2. **ML1 Review**  
   ML1 approves closure decision.

3. **Status Update**  
   Matter status in canonical registry updated to `closed`.
   `closed_date` and `closure_reason` recorded.

4. **External System Synchronization**  
   Clio matter marked as archived/closed.
   SharePoint matter folder flagged as closed (if applicable).

5. **Archive**  
   Matter record remains in `05_MATTERS/MATTER_REGISTRY.md` (not deleted).
   Matter folder remains in its `delivery_status` tier folder (e.g., `05_MATTERS/NORMAL/`) with `delivery_stage` updated to `parked` or `finished` in MATTER.yaml, or moves to `05_MATTERS/ARCHIVE/` (by year) on full closure.

---

## 5. Canonical Matter Record Structure

The canonical matter record (stored in `05_MATTERS/MATTER_REGISTRY.md` or matter-specific MATTER.yaml) contains:

| Field | Authority | Mutable | Source |
|-------|-----------|--------|--------|
| `matter_id` | ML1 | No | ML2 (canonical) |
| `client_name` | ML1 | Yes (with approval) | ML2 (canonical) |
| `matter_description` | ML1 | Yes (with approval) | ML2 (canonical) |
| `engagement_date` | ML1 | No | ML2 (canonical) |
| `status` | System (gated), escalates to ML1 | Yes (within policy) | ML2 (canonical) |
| `delivery_status` | System (gated), escalates to ML1 | Yes (within policy) | ML2 (canonical) |
| `fulfillment_status` | System (gated), escalates to ML1 | Yes (within policy) | ML2 (canonical) |
| `clio_matter_id` | ML1 (at registration) | No | External (mapped) |
| `services` | System + ML1 (approval) | Yes (governed) | ML2 (canonical) |
| `closed_date` | ML1 | No (once set) | ML2 (canonical) |

---

## 6. Related Invariants

- [INV-0003](INV-0003-matter-model-structural-invariants.md) — Matter Model Structural Invariants (defines structure and cardinality)
- [INV-0006](INV-0006-matter-file-subordination-and-identity-boundary.md) — Matter File Subordination and Identity Boundary (defines Matter vs Matter File relationship)

---

## 7. Related Policies and Protocols

| Artifact | Purpose |
|----------|---------|
| POL-043 | Clio Matter ID Structure and Client of Record Identity |
| POL-044 | SharePoint Matter Folder Access Staging Policy |
| POL-052 | Client Engagement Stage Policy |
| PRO-013 | Matter Filing Protocol |
| PRO-020 | LL Matters SharePoint Protocol |
| PRO-021 | LL Matters Folder Protocol |
| PRO-022 | LL Matters File Protocol |

---

## 8. Boundary and Escalation

This invariant establishes **who has authority** to create, modify, and close matter identity.

Policies define **what state transitions are allowed** and under what conditions.

Protocols define **how** state transitions are enforced and **what gates** must be passed.

If authority boundaries are unclear or if an external system record conflicts with canonical matter identity, the conflict must be **escalated to ML1** rather than resolved autonomously.
