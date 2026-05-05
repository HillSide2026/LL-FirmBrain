---
id: 01_doctrine__01_invariants__readme_md
title: Invariants (Level 1)
owner: ML1
status: approved
approved_by: ML1
approved_date: 2026-04-18
version: 1.0
created_date: 2026-02-13
last_updated: 2026-03-21
tags: [doctrine, invariants]
---

# Invariants (Level 1)

Definition:
An Invariant is a structural property that must remain true for the system to remain coherent and valid.
This is the system constitution layer.

Characteristics:
- Architectural, not interpretive.
- Rarely changed.
- Violation breaks system integrity.
- Requires formal amendment to modify.
- Higher than Policies.
- If something conflicts with an invariant, the other thing is wrong.

Boundary:
Invariants do NOT:
- Govern behavior within workflows.
- Describe quality posture.
- Define enforcement routines.
- Replace Policies.

Classification:
- If a rule governs behavior, it belongs in Policies.
- If it defines enforcement logic, it belongs in Protocols.
- If it defines interpretive posture, it belongs in Principles.

Naming convention:
- Canonical numbered invariants in this folder should use `INV-####-descriptive-name.md`.
- `README.md`, `SECOND_BRAIN_MODEL.md`, `SYSTEM_IDENTITY.md`, and `DEPRECATION_REGISTRY.md` are the only unnumbered exceptions that should remain active in this folder.
- Legacy `DOCTRINE-*` filename prefixes should not remain in this folder once an artifact has been normalized into the active invariant sequence.

Active Invariants (Approved/Active Status):
- INV-0001 through INV-0017 (see DEPRECATION_REGISTRY.md for superseded/retired artifacts)

Governance:
- See [DEPRECATION_REGISTRY.md](DEPRECATION_REGISTRY.md) for retired invariants and supersession history.
- See [INV-0007-what-qualifies-as-doctrine.md](INV-0007-what-qualifies-as-doctrine.md) for doctrine approval lifecycle.

Typical examples in the ML1/ML2/System/LL model:
- ML1 retains final judgment authority.
- ML2 is a system of record, not an autonomous actor.
- LL consumes only ML1-approved outputs.
- System decisions and changes must be auditable.
