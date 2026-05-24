---
id: INV-0016
title: 'INV-0016: No Top-Level Directories'
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

# INV-0016 — No Top-Level Directories

**Status:** APPROVED
**Invariant ID:** INV-0016
**Effective:** 2026-02-07
**Authority:** ML1
**Applies To:** Claude Code; any agent writing to the LL-Secondbrain repo

---

## 1. Rule

Claude Code MUST NOT create new **top-level directories** in the repository.

Top-level directories are those that appear at the repository root (same level as `00_SYSTEM`, `01_DOCTRINE`, etc.).

Claude Code MAY create, move, or modify files and subdirectories **only within existing top-level directories**.

---

## 2. Allowed Root Changes (Explicit Exceptions)

Claude Code MAY modify or create files at the repo root ONLY if they already exist or are explicitly authorized, including:

- `README.md`
- `LICENSE`
- `.gitignore`
- `.gitattributes` (if present)
- `.env.example` (if present)

Claude Code MUST NOT create new root-level folders such as:
- `05_MATTER_DOCKETING/`
- `TESTS/`
- `SPECS/`
- `outputs/`
- any folder containing spaces or display labels

---

## 3. Path Construction Constraint (Display Labels ≠ Paths)

Claude Code MUST NOT construct filesystem paths from display labels.

Specifically:
- Strings containing `" / "` MUST NOT be used as directory names.
- Slash (`/`) MUST be treated only as a path separator, never as literal folder text.
- Folder names at root MUST match canonical identifiers exactly.

---

## 4. Required Behavior When a New Root Folder Would Be Needed

If Claude Code believes a new top-level directory is required, it MUST:

1. STOP
2. Produce a short proposal stating:
   - intended folder name
   - why it is needed
   - where it fits in the repo taxonomy
3. Await ML1 instruction / approval

No directory creation occurs until approval is received.

---

## 5. Validation Check (Pre-Write Guard)

Before writing any files, Claude Code MUST:

- list the current repo root directories
- verify all target paths begin with an existing top-level directory name
- refuse any write that would add a new root directory

---

## 6. Examples

### Allowed
- Create: `04_INITIATIVES/LL_PORTFOLIO/05_MATTER_DOCKETING/SPECS/MATTER_TODO_REPORT.md`
- Move: `03_TESTS/...` → `06_RUNS/03_TESTS/...`

### Forbidden
- Create: `05_MATTER_DOCKETING/` at repo root
- Create: `05_MATTER_DOCKETING / SPECS` as a literal folder name
- Create any new root folder not already present

---

## 7. Rationale

The repository root is a controlled taxonomy.
Root drift breaks retrieval, indexing, and governance.
All new domains require ML1 approval.

---
