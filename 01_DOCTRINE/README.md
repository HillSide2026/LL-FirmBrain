---
id: 01_doctrine__readme_md
title: Doctrine
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
created_date: 2026-01-25
last_updated: 2026-03-08
tags: []
---

# Doctrine

Doctrine is the system's authoritative guidance. It is organized by layer and aligned to the governance hierarchy.

## 01_INVARIANTS (Level 1)
Structural properties that must remain true for system coherence and validity.
If violated, system integrity is broken and formal amendment is required.
This is the system constitution layer.

## 02_PRINCIPLES (Level 2)
Interpretive values that guide policy formation.
Principles are decision heuristics for ambiguity, not direct commands.

## 03_POLICIES (Level 3)
Binding constraints derived from principles.
Policies define allowed and disallowed behavior and are enforceable governance rules.

## 04_CAPABILITY_PROFILES
Opt-in profiles that grant scoped, revocable relaxations to default agent constraints.
Profiles define what specific components are allowed and not allowed to do.

## 05_PROTOCOLS (Level 4)
Operational enforcement rules that implement policies as conditional logic.
Protocols define interaction contracts and process choreography.

## 06_PROCEDURAL
Governance and change-control doctrine: how doctrine and system rules are reviewed, approved, versioned, deprecated, and migrated.
This section acts as the divider before operational execution artifacts.

## RULES
Atomic, executable rule fragments used by protocols (reserved for Stage 5).
Rules should be machine-checkable wherever possible.

## TESTS
Fixtures that validate rules and protocol behavior.
Tests verify doctrinal integrity and policy-protocol coherence.

## Classification rule
- "must / required / never / always" (structural) → invariants
- "must / required / never / always" (behavioral) → policies
- "means / applies when / examples / principles" → principles
- "review / approval / version / deprecate / change control" → procedural
