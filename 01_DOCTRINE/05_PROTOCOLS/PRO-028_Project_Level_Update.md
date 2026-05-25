---
id: PRO-028
title: Project Level Update
owner: ML1
status: draft
version: 0.1
created_date: 2026-05-20
last_updated: 2026-05-20
tags: [protocol, projects, updates, scope, change-control]
---

# PRO-028 — Project Level Update

> **DRAFT — PENDING ML1 APPROVAL.**
> This protocol has not been approved and is not yet in effect.

---

## 1. Purpose

This protocol defines a five-level scale for changes made within an existing
project.

It exists to prevent overreach, under-description, and scope confusion when a
project is updated.

The governing assumption is fixed:

- the project structure does not change

For this protocol, "project structure does not change" means:

- no new Project ID
- no split, merge, or retirement of projects
- no reclassification of one project into multiple projects
- no change to the project container itself

This protocol therefore governs only within-project update scope.

---

## 2. Scope

This protocol applies whenever an agent or operator updates files inside an
existing project.

For purposes of this protocol, project scope is determined by the project's
canonical scope artifact for its stage:

- `SCOPE_STATEMENT.md` where that artifact is required for Planning or later
- otherwise `PROJECT_CHARTER.md`
- for decision projects, `DECISION_FRAME.md` as applicable

It does not govern:

- creation of a new project
- deletion, merger, or supersession of a project
- changing the number of projects used to govern the work

Those are structural changes and are outside this protocol.

For clarity, a change is not structural if it only changes project-internal
files.

---

## 3. Classification Rule

Before making a project update, classify the intended change at one of the five
levels below.

If the change includes elements from multiple levels, classify it at the
highest level reached.

If uncertain between two levels, use the higher level.

---

## 4. The Five Levels

### Level 1 — Sync

Purpose:
- typo, date, wording only

### Level 2 — Refresh

Purpose:
- sync current-facing project files to an already-accepted posture

### Level 3 — Update

Purpose:
- record a real new development in the project, without changing the project's
  scope, purpose, or stage

### Level 4 — Rewrite

Purpose:
- substantially revise multiple files within a project to reflect accumulated
  developments, but without changing the project's scope or purpose

### Level 5 — Revision

Purpose:
- materially revise how the project documentation is written, without changing
  the project's scope or purpose

---

## 5. Operational Use

When describing or proposing a project update, state:

1. the target project
2. the intended level
3. the reason for that level
4. the files expected to change

Suggested format:

```text
Project: [project_id]
Update level: [1-5]
Why: [short reason]
Files: [file list]
```

---

## 6. Interpretation Notes

- Level 1 fixes wording.
- Level 2 catches the files up.
- Level 3 records a real new development.
- Level 4 substantially rewrites multiple files.
- Level 5 materially revises how the documentation is written.

The scale is cumulative in significance, not in word count.

---

## 7. Related Doctrine

- `01_DOCTRINE/01_INVARIANTS/INV-0012-project-structural-boundaries.md`
- `01_DOCTRINE/03_POLICIES/POL-055_Repository_Project_Policy.md`
- `01_DOCTRINE/03_POLICIES/POL-056_Firm_Project_Policy.md`

---

## 8. Change Log

| Version | Date | Change |
|---|---|---|
| 0.1 | 2026-05-20 | Initial draft. Creates a five-level scale for within-project updates while holding project structure constant. |
| 0.2 | 2026-05-20 | Clarifies that project scope is determined by the canonical scope artifact for the project's stage. |
