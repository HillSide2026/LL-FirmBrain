---
id: INV-0010
title: 'INV-0010: Canonical Stage & Phase Numbering Doctrine'
owner: ML1
status: approved
approved_by: ML1
approved_date: 2026-03-28
version: 1.0
effective_date: 2026-03-28
supersedes:
provenance:
  decided_by: ML1
  decided_on: 2026-03-28
  context: Metadata normalized by system admin cleanup on 2026-05-24
created_date: 2026-02-08
last_updated: 2026-03-28
tags: []
---

# INV-0010 — Canonical Stage & Phase Numbering Doctrine

**Invariant ID:** INV-0010
**Status:** APPROVED
**Effective:** 2026-01-27
**Authority:** ML1

## Change Note
Enforcement responsibilities moved to `01_DOCTRINE/05_PROTOCOLS/PRO-012_Stage_Phase_Numbering_Enforcement.md` on 2026-02-13 to separate structural invariants from enforcement logic.

---

## 1. Stage numbering (top level)

Stages are integers only:
- `STAGE1`
- `STAGE2`
- `STAGE3`

A stage number is globally unique and never reused.

Stage numbers are assigned once in the roadmap and never inferred later.

**Rule:**
No artifact may invent a new stage number. Stages must already exist in the roadmap.

---

## 2. Phase numbering (within a stage)

Phases are decimal expansions of the stage.

**Format:**
```
<STAGE>.<PHASE>
```

**Examples:**
- 1.1, 1.2, 1.3, 1.4
- 2.1, 2.2, 2.3

**Rules:**
- Phase numbers start at `.1`
- Phase numbers increment sequentially
- Phase numbers are never skipped
- Phases are scoped to their stage
- Phase numbers reset when the stage changes

---

## 3. Artifact naming (hard requirement)

Any artifact that references a stage or phase MUST:
- Use both stage and phase where applicable
- Match one of these formats exactly:

**Stage-only artifact:**
```
STAGE2_<NAME>.md
```

**Stage + phase artifact:**
```
STAGE2.1_<NAME>.md
```

**Invalid formats (rejected):**
- `STAGE_2.1`
- `STAGE21`
- `STAGE3_PHASE1`
- `STAGE2-1`

---

## 4. Directory structure (enforced)

Directories must reflect stage first, phase second:

```
STAGE1/
  STAGE1.1/
  STAGE1.2/
  STAGE1.3/
  STAGE1.4/

STAGE2/
  STAGE2.1/
  STAGE2.2/
  STAGE2.3/
```

**Rule:**
No directory may contain artifacts from multiple stages.

---

## 5. Change control (critical)

Adding a new stage or new phase requires:
- Roadmap update
- Explicit ML1 approval

Agents may reference stages/phases.
Agents may **not** create new ones.
