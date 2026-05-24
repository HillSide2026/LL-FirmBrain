---
id: 01_doctrine__policies__readme_md
title: Policies (Level 3)
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
created_date: 2026-02-13
last_updated: 2026-03-23
tags: [doctrine, policies]
---

# Policies (Level 3)

Definition: Binding constraints derived from principles that specify what must or must not occur.
Policies are enforceable governance rules for allowed and disallowed behavior.
Boundary: Do not describe enforcement mechanics; those belong in protocols.

Typical examples:
- Output labels and provenance are mandatory where policy requires.
- ML1-approved doctrine overrides lower-layer artifacts.
- External integrations require explicit approvals where policy requires.

Naming convention:
- Canonical active policies in this folder should use `POL-###_Descriptive_Name.md`.
- `README.md` and explicitly superseded historical artifacts are permitted exceptions.

Repository hygiene rule:
- Deprecated alias files should not remain in this folder once downstream references have been migrated.
