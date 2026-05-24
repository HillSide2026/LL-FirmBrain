---
id: PRO-017
title: Repository Sync Verification Protocol
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
tags: [protocol, git, repository, sync, verification, agent-behaviour]
---

# PRO-017 — Repository Sync Verification Protocol

Enforces Policy: POL-041

Trigger condition: Any agent action or user request that requires reporting or acting on repository sync state. This includes (but is not limited to): "check git status", "are we in sync?", "is the repo up to date?", "what's the git state?", "please read the repo", and any pre-commit or pre-push verification.

---

## Required Procedure

Steps must be executed in order. No step may be skipped.

### Step 1 — Fetch from remote
```
git fetch origin
```
Purpose: Updates the local view of origin. Without this step, `git status` reflects a stale snapshot of the remote and cannot be used to determine actual sync state.

### Step 2 — Check working tree and staged state
```
git status
```
Read and report:
- Whether the working tree is clean (no modified or untracked files)
- Whether there are staged changes not yet committed
- The local branch name and its tracking branch

### Step 3 — Check local ahead of remote
```
git log origin/<branch>..HEAD --oneline
```
Report: The count and list of commits on local that have not been pushed to origin.

### Step 4 — Check remote ahead of local
```
git log HEAD..origin/<branch> --oneline
```
Report: The count and list of commits on origin that have not been pulled to local.

---

## Required Output Format

The agent must report all four dimensions explicitly:

```
Working tree:      clean | N uncommitted changes
Staged:            clean | N staged changes
Local ahead:       N commits to push | (list)
Remote ahead:      N commits to pull | (list)
```

If any dimension is non-zero or non-clean, recommend the appropriate action before proceeding with any other task.

---

## Recommended Actions by State

| State | Action |
|-------|--------|
| Remote ahead > 0 | Run `git pull` before any commit or push |
| Local ahead > 0 | Confirm with ML1 before pushing |
| Staged changes present | Confirm intent — commit or discard before proceeding |
| Working tree dirty | Do not commit or push until resolved |

---

## Enforcement Responsibilities

### Any agent performing git operations
Must:
- Run the full four-step procedure before reporting sync state
- Never substitute `git status` alone for a full sync verification
- Never use "in sync", "clean", or "up to date" without completing Steps 1–4

---

## Minimal Checklist

- [ ] `git fetch origin` executed
- [ ] Working tree state reported
- [ ] Staged state reported
- [ ] Local-ahead count reported
- [ ] Remote-ahead count reported
- [ ] Recommended action stated if any dimension is non-zero
