---
id: POL-041
title: Repository State Reporting Accuracy
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
created_date: 2026-03-09
last_updated: 2026-03-09
tags: [policy, git, repository, reporting, accuracy, agent-behaviour]
---

# POL-041 — Repository State Reporting Accuracy

Policy Statement: When an agent reports repository state, it must report all four dimensions of that state accurately and without omission. Partial reporting that conflates distinct dimensions, or that omits any dimension, is non-compliant.

Authority (Principles referenced): PRN-003, PRN-007, PRN-008

Enforcement expectation: Any agent response that omits or mischaracterizes repository state dimensions must be flagged, corrected, and the correct state reported before proceeding.

Supersedes: None

Version: 1.0

Status: Active

---

## The Four Dimensions of Repository State

An agent asked to report repository or git sync status must address all four dimensions:

| Dimension | Definition | Non-compliant conflation |
|-----------|-----------|--------------------------|
| **Working tree** | Uncommitted file changes (modified, deleted, untracked) | Reporting "clean" when staged changes exist |
| **Staged changes** | Changes added to the index but not yet committed | Omitting staged state from the report |
| **Local ahead of remote** | Commits on local branch not yet pushed to origin | Reporting "in sync" when local has unpushed commits |
| **Remote ahead of local** | Commits on origin not yet fetched/pulled to local | Reporting "in sync" without first fetching from origin |

---

## Prohibited Conflations

The following characterizations are non-compliant unless all relevant dimensions have been checked and confirmed:

- "Clean" — may only be used if working tree AND staged state are both clean
- "In sync" / "up to date" — may only be used after `git fetch`, and only if local-ahead AND remote-ahead are both zero
- "Nothing to commit" — does not imply sync with remote; must not be used as a proxy for overall sync status

---

## Enforcement Protocol

PRO-017 defines the required verification procedure.
