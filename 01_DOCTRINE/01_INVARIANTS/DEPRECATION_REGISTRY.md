---
id: 01_doctrine__01_invariants__deprecation_registry_md
title: Invariant Deprecation Registry
owner: ML1
status: approved
effective_date: 2026-05-04
supersedes:
provenance:
  decided_by: ML1
  decided_on: 2026-05-04
  context: Metadata normalized by system admin cleanup on 2026-05-24
created_date: 2026-05-04
last_updated: 2026-05-04
tags: [governance, invariants, deprecation, archive]
---

# Invariant Deprecation Registry

This registry maintains a single source of truth for all retired, superseded, or deprecated invariants.

## Purpose
- Track which invariants have been formally retired or replaced
- Prevent accidental reuse of deprecated IDs
- Maintain audit trail of doctrinal evolution
- Clarify which version of a superseded invariant is authoritative

---

## Active Invariants (Not Deprecated)

All invariants with `status: approved` or `status: active` in their frontmatter are current and authoritative.

Current invariants: INV-0001 through INV-0016 (see `01_DOCTRINE/01_INVARIANTS/README.md` for full list).

---

## Superseded Invariants

| ID | Title | Status | Superseded By | Supersession Date | Notes |
|----|-------|--------|---------------|------------------|-------|
| INV-0008 v1.0 | Authority Hierarchy (former version) | Superseded | INV-0008 v2.0 | 2026-03-21 | v2.0 clarifies runtime authority separation and System vs LL layers |

---

## Retired Invariants

| ID | Title | Retirement Date | Reason | Successor |
|----|-------|-----------------|--------|-----------|
| (None currently) | | | | |

---

## Reserved / Unassigned IDs

The following invariant IDs are reserved and must not be reassigned without explicit ML1 approval:

- (None currently reserved)

---

## Amendment Protocol

To retire, supersede, or reserve an invariant:

1. **Proposal Phase**  
   Document the change rationale and send to ML1 for review.

2. **Approval Phase**  
   ML1 approves the change.

3. **Registry Update**  
   This file is updated with:
   - Invariant ID
   - Supersession/Retirement date
   - Reason
   - Links to successor (if applicable)
   - Version history (if versioned)

4. **Invariant File Update**  
   The deprecated invariant's status field is updated to `deprecated` or `superseded`.

5. **Version Increment**  
   This registry file version is incremented.

---

## Related Artifacts

- [01_DOCTRINE/01_INVARIANTS/README.md](README.md) — Canonical list of active invariants
- [01_DOCTRINE/01_INVARIANTS/INV-0007-what-qualifies-as-doctrine.md](INV-0007-what-qualifies-as-doctrine.md) — Definition of doctrine and approval lifecycle
