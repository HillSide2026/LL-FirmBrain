---
id: 00_system_repo_health_review_md
title: ll-secondbrain_fresh — Structured Repo Health Review
owner: ML1
status: draft
created_date: 2026-05-18
last_updated: 2026-05-18
tags: []
---

# ll-secondbrain_fresh — Structured Repo Health Review

**Date:** 2026-04-13
**Author:** Codex (implementation operator)
**Basis:** Direct repo inspection and implemented fixes — not speculative analysis

---

## 1. Review Frame

This is a repo-grounded structured review based on direct inspection and implemented
fixes executed on 2026-04-13. All findings are derived from reading source files,
running validators, and diffing scripts. No assumptions were made about ML1 intent.

---

## 2. Observed Facts

| # | Fact | Confidence |
|---|------|------------|
| 1 | 41 MATTER.yaml files exist across ESSENTIAL/STRATEGIC/STANDARD/PARKED | Confirmed |
| 2 | MATTER_REGISTRY.md had 26-1631-00001 duplicated on line 43 and 45 | Confirmed |
| 3 | MATTER_REGISTRY.md was missing 24-845-00001 (STAR 333 SPORTS INC., Standard) | Confirmed |
| 4 | MATTER_REGISTRY.md is hand-maintained (no generator script references it) | Confirmed |
| 5 | .mcp.json only registered `gmail`; `sharepoint` was absent despite CLAUDE.md claiming both | Confirmed |
| 6 | .claude/settings.json correctly registered both gmail and sharepoint + PreToolUse hook | Confirmed |
| 7 | DASHBOARDS/MATTER_INDEX.md shows 35 rows; 41 MATTER.yaml files exist — 6 matters absent from dashboard | Confirmed |
| 8 | scripts/ is canonical runtime location (pointed to by .mcp.json, .claude/settings.json, run_matter_admin.py) | Confirmed |
| 9 | 00_SYSTEM/scripts/ serves a distinct role: SMA orchestrators, LL Portfolio agents, trade remedies | Confirmed |
| 10 | 3 scripts in 00_SYSTEM/scripts/ were full copies with only path resolution diffs (gmail_labeler, prefilter_emails, validate_matter_yaml) | Confirmed |
| 11 | 4 scripts in 00_SYSTEM/scripts/ have material content divergence (inbox_classifier, todo_rollup, sharepoint_integration, gmail_integration) | Confirmed |
| 12 | 226 of 584 SharePoint items (39%) are unmapped: 176 in 24-682-00003 path, 49 in Clerk Work/ | Confirmed |
| 13 | Matter 24-682-00003 (Stream sub-matter) exists in SharePoint but has NO MATTER.yaml and is NOT in registry | Confirmed |
| 14 | 30 of 41 matters show zero SharePoint items linked | Confirmed |
| 15 | 41/41 MATTER.yaml files pass schema validation; 0 invalid | Confirmed |
| 16 | 27 ML Active matters have no services defined (validator warning, not error) | Confirmed |
| 17 | No unified health command existed before this review | Confirmed |

---

## 3. Findings by Domain

### 3.1 System-of-Record Integrity

**Observed state:** MATTER_REGISTRY.md had 1 duplicate entry and 1 missing entry. The
DASHBOARDS/MATTER_INDEX.md snapshot is stale — 35 vs 41 matters — because the daily
sweep pulls from Clio cache (`cache/clio_matters.json`) which only captured 35 matters
at last run.

**Why it matters:** MATTER_REGISTRY.md is used by `gmail_governance/matter_enforcement.py`.
Duplicates and missing entries cause mis-routing.

**What was fixed:** Removed duplicate 26-1631-00001. Added missing 24-845-00001.
Created `scripts/validate_matter_registry.py` to detect counts, duplicates, and
MATTER.yaml cross-reference mismatches automatically.

**What remains open:** Dashboard staleness (35 vs 41) resolves on next daily sweep
when Clio cache is refreshed. No action needed unless the Clio cache itself is stale.

**ML1 decision required:** No.

---

### 3.2 Schema / Index / Canonical Artifact Discipline

**Observed state:** `05_MATTERS/INDEX.md` is ML1-gated per CLAUDE.md.
`generate_matter_index.py` exists as a manual tool. `DASHBOARDS/MATTER_INDEX.md`
is the auto-generated daily snapshot — correct architecture.

**Why it matters:** Confusing INDEX.md (ML1 gated) with DASHBOARDS/MATTER_INDEX.md
(auto-generated) would cause silent governance violations.

**What was fixed:** CLAUDE.md already correctly documents the distinction. No change
needed. The .gitignore policy comment now makes this explicit.

**What remains open:** 27 ML Active matters have no `services` field defined. This is
a data completeness gap, not a schema error. Services should be populated for accurate
matter workload tracking.

**ML1 decision required:** No for the schema. Populating services fields requires ML1
direction on each matter.

---

### 3.3 Generated Artifact Governance

**Observed state:** .gitignore correctly ignored `06_RUNS/RUN-*/`, `06_RUNS/state/`,
`cache/*.json`, and OAuth tokens. However, the policy was implicit — no documentation
of which committed artifacts are intentional snapshots vs which are truly ephemeral.

**Why it matters:** Ambiguity causes developers (and agents) to commit ephemeral
outputs or to treat committed snapshots as permanent records.

**What was fixed:** Added explicit `GENERATED ARTIFACT POLICY` comment block to
.gitignore documenting:
- Committed (canonical snapshots): DASHBOARDS/, MATTER_REGISTRY.md, INDEX.md,
  MATTER_TODO_REPORT.md, MATTER_TODO_LEDGER.json, CHIEF_OF_STAFF/
- Ignored (ephemeral): RUN-*/,  state/, logs/, gmail_fetch_latest.json, cache/*.json

**What remains open:** `06_RUNS/ops/emails_attributed.json`,
`06_RUNS/ops/emails_prefiltered.json`, `06_RUNS/ops/MATTER_TODO_LEDGER.json`, and
related ops files are committed. Policy: these appear intentionally committed as
operational records. If ML1 prefers them ignored, requires explicit direction.

**ML1 decision required:** Confirm whether ops/ JSON files should remain committed or
move to .gitignore.

---

### 3.4 Script/Runtime Canonicalization

**Observed state:** Two script locations serve different purposes:
- `scripts/` — canonical runtime: MCP servers, matter admin, validation, health checks
- `00_SYSTEM/scripts/` — SMA orchestrators: portfolio agents, daily sweep, trade remedies, sb_graph_bridge

Overlap existed in 7 scripts with varying degrees of divergence.

**What was fixed:**
- Converted 3 path-only-diff scripts to shims:
  `00_SYSTEM/scripts/validate_matter_yaml.py` → shim → `scripts/validate_matter_yaml.py`
  `00_SYSTEM/scripts/prefilter_emails.py` → shim → `scripts/prefilter_emails.py`
  `00_SYSTEM/scripts/gmail_labeler.py` → shim → `scripts/gmail_labeler.py`
- Added `# DIVERGENCE WARNING` header to 4 materially diverged scripts:
  `inbox_classifier.py`, `todo_rollup.py`, `sharepoint_integration.py`, `gmail_integration.py`

**What remains open:** The 4 diverged scripts require a reconciliation decision.
Each has a `# CANONICAL LOCATION` and `# DIVERGENCE WARNING` comment identifying
the issue.

**ML1 decision required:** Approve which version of each diverged script is current,
then either merge or retire the non-canonical version. See Section 8 for specifics.

---

### 3.5 Validation / Health-Check Coverage

**Observed state:** Two validators existed (`validate_matter_yaml.py`,
`safety-rails.sh`) but ran independently with no unified entry point.
No registry integrity check existed. No health command existed.

**What was fixed:**
- Created `scripts/validate_matter_registry.py` — counts, duplicates, MATTER.yaml
  cross-reference, dashboard staleness warning
- Created `scripts/health.sh` — unified command that runs safety-rails, registry
  integrity, and YAML schema validation in sequence
  Usage: `bash scripts/health.sh` or `bash scripts/health.sh --quick`

**What remains open:** health.sh does not yet include a check that DASHBOARDS/ files
were generated within the last N days (staleness check). Low priority.

**ML1 decision required:** No.

---

### 3.6 Integration Configuration and Docs

**Observed state:** `.mcp.json` registered only `gmail`. `.claude/settings.json`
registered both `gmail` and `sharepoint`. CLAUDE.md claimed both were in `.mcp.json`
— a false statement that could cause agents to miss the sharepoint server or
incorrectly audit the config.

**What was fixed:**
- Added `sharepoint` server to `.mcp.json` — now matches `.claude/settings.json`
- Updated CLAUDE.md to accurately describe the intentional split: both servers in
  both files; `.claude/settings.json` additionally carries the PreToolUse hook

**What remains open:** None. Config and docs now agree.

**ML1 decision required:** No.

---

### 3.7 Data Quality Backlog and Mapping Gaps

**SharePoint unmapped (226 items):**

| Category | Count | Root Cause | Resolution Path |
|----------|-------|------------|-----------------|
| `24-682-00003` path items | 176 | Matter ID not in repo registry or identity map | ML1 decision: is 24-682-00003 a separate registerable matter or an alias for 24-682-00002? |
| `Clerk Work/` folder items | 49 | Firm-admin folder, not matter-specific | Policy: exclude from gap scan OR assign to FIRM_ADMIN bucket |
| Other | 1 | Unknown identity match | Manual review |

**30 matters with zero SharePoint items** — likely a mix of:
a. Matters that genuinely have no SP files yet (new matters, parked matters)
b. Matters whose SP files exist under a different ID or path

This is a data-quality gap, not a system error. Do not auto-resolve.

**Inbox unmapped (5 threads, stale 2026-03-05):**

| Count | Reason |
|-------|--------|
| 1 | No matter or identity match (promotional email) |
| 4 | Ambiguous — multiple matter candidates |

These require manual disambiguation or identity map updates. Small enough to review
in a single session.

**ML1 decision required:**
- Decide on 24-682-00003: register as new matter, alias to existing matter, or mark as
  excluded from scan
- Decide policy for Clerk Work/ non-matter SP items

---

### 3.8 Operational Review Cadence / Drift Prevention

**Observed state:** No recurring drift-prevention mechanism existed beyond the
pre-commit hook for write validation.

**What was fixed (drift prevention mechanisms added):**

| Mechanism | What it catches |
|-----------|-----------------|
| `scripts/validate_matter_registry.py` | Registry duplicates, count drift, MATTER.yaml mismatches |
| `scripts/health.sh` | All of the above + safety-rails + YAML schema in one command |
| `.gitignore` policy comment block | Documents which artifacts are canonical vs ephemeral |
| DIVERGENCE WARNING headers in 4 scripts | Flags content drift before it causes silent breakage |

**What remains open:** No pre-commit hook runs `validate_matter_registry.py`.
Adding it to `.claude/settings.json` hooks or `scripts/pre-commit` would close this.

---

## 4. ML2 / System Effectiveness Opportunities

| # | Gap | Type |
|---|-----|------|
| 1 | No staleness check: DASHBOARDS/ artifacts can silently be weeks old | Missing validation |
| 2 | `services` field not populated for 27 ML Active matters — workload tracking blind | Missing data completeness |
| 3 | `24-682-00003` Stream sub-matter exists in SP but has no repo presence | Missing source-of-truth rule |
| 4 | `Clerk Work/` firm-admin SP items will perpetually appear as "gaps" | Missing boundary definition |
| 5 | 4 diverged scripts have no test coverage to detect further drift | Missing validation |
| 6 | MATTER_REGISTRY.md is hand-maintained with no generation enforcement | Missing control mechanism |
| 7 | `generate_matter_index.py` can rewrite the ML1-gated INDEX.md if run without intent | Missing review cadence guard |
| 8 | Dashboard count (35 vs 41) driven by Clio cache coverage — no alert when cache is stale | Missing validation |

---

## 5. ML1 Actions for the Next 7 Days

Decisions only. Not busywork.

| # | Decision | Impact |
|---|----------|--------|
| 1 | **24-682-00003 Stream sub-matter**: register as new MATTER.yaml, alias to 24-682-00002 in identity map, or mark excluded from SP scan. 176 SP items are blocked on this. | High |
| 2 | **Clerk Work/ SP folder policy**: exclude from gap scan, assign to FIRM_ADMIN, or accept as permanent noise. 49 SP items are blocked on this. | Medium |
| 3 | **Diverged script reconciliation**: for each pair (`inbox_classifier`, `todo_rollup`, `sharepoint_integration`, `gmail_integration`), confirm which version is current. Codex can execute the shim conversion once ML1 designates the canonical version. | Medium |
| 4 | **ops/ JSON file commit policy**: confirm whether `06_RUNS/ops/*.json` files (MATTER_TODO_LEDGER.json, emails_attributed.json, etc.) should remain committed or be moved to .gitignore | Low |
| 5 | **Add `validate_matter_registry.py` to pre-commit hook**: approve adding this to the PreToolUse hook chain so registry drift is caught before commit | Low |

---

## 6. Backlog Candidates

| Title | Purpose | Evidence | Owner | Priority |
|-------|---------|----------|-------|----------|
| Register or alias 24-682-00003 | Resolve 176 SP unmapped items | SHAREPOINT_GAPS.md — 176 items in 24-682-00003 path | ML1 decision | Critical |
| Clerk Work/ exclusion policy | Resolve 49 permanently unmapped SP items | SHAREPOINT_GAPS.md — 49 Clerk Work items | ML1 decision | High |
| Reconcile 4 diverged scripts | Prevent silent logic drift in inbox_classifier, todo_rollup, sharepoint_integration, gmail_integration | DIVERGENCE WARNING headers added 2026-04-13 | ML1 decision + Codex execution | High |
| Populate services on 27 ML Active matters | Enable accurate matter workload tracking | validate_matter_yaml.py warnings | ML1 direction | Medium |
| Add registry check to pre-commit hook | Prevent future count drift without manual health check | validate_matter_registry.py created 2026-04-13 | Codex implementable | Medium |
| Dashboard staleness alerting | Detect when DASHBOARDS/ artifacts are > N days stale | Dashboard count 35 vs 41 observed today | Codex implementable | Medium |
| Clio cache coverage audit | Determine why Clio cache only returns 35 of 41 matters | MATTER_INDEX dashboard 35 vs 41 | Codex implementable | Medium |

---

## 7. Change Summary

### Files changed:
- `05_MATTERS/MATTER_REGISTRY.md` — removed duplicate 26-1631-00001; added missing 24-845-00001
- `.mcp.json` — added sharepoint MCP server (was missing)
- `CLAUDE.md` — corrected MCP server config description
- `.gitignore` — added explicit generated artifact policy comment block
- `00_SYSTEM/scripts/validate_matter_yaml.py` — converted to shim → scripts/
- `00_SYSTEM/scripts/prefilter_emails.py` — converted to shim → scripts/
- `00_SYSTEM/scripts/gmail_labeler.py` — converted to shim → scripts/
- `00_SYSTEM/scripts/inbox_classifier.py` — added DIVERGENCE WARNING header
- `00_SYSTEM/scripts/todo_rollup.py` — added DIVERGENCE WARNING header
- `00_SYSTEM/scripts/sharepoint_integration.py` — added DIVERGENCE WARNING header
- `00_SYSTEM/scripts/gmail_integration.py` — added DIVERGENCE WARNING header

### Files created:
- `scripts/validate_matter_registry.py` — new drift-prevention validator
- `scripts/health.sh` — unified health command

### Generators changed: None changed. Generators were correct; the registry was hand-maintained and had a manual entry error.

### Checks added:
- Registry count check (MATTER.yaml ↔ MATTER_REGISTRY.md)
- Duplicate detection in MATTER_REGISTRY.md
- MATTER.yaml cross-reference
- Dashboard staleness warning
- Unified health command wrapping all checks

### Docs updated:
- `.gitignore` — artifact policy documented
- `CLAUDE.md` — config split accurately described

### Compatibility notes:
- All 00_SYSTEM/scripts/ shims preserve the same invocation interface (runpy delegates to scripts/)
- health.sh exits 0 with warnings (does not fail on warnings)
- validate_matter_registry.py exits 1 on errors, 0 on warnings

---

## 8. Open Questions

1. **24-682-00003**: Is this a separate billable matter from 24-682-00002? If yes, it needs
   a MATTER.yaml. If it's a sub-engagement, it needs an alias in `matter_identity_map.yaml`.

2. **Clerk Work/ SP folder**: Is this firm-wide clerk work that should be permanently
   excluded from the gap scan? Needs a policy.

3. **Diverged scripts**: For each of the 4 flagged pairs — which is the authoritative version?
   - `inbox_classifier.py`: 00_SYSTEM uses `04_INITIATIVES` + `10_ARCHIVE`; scripts/ uses `04_OPERATIONS` + `09_ARCHIVE`. Which folder structure is current?
   - `todo_rollup.py`: 00_SYSTEM version is +5KB. What additional logic does it have?
   - `sharepoint_integration.py`: 00_SYSTEM version is +7KB.
   - `gmail_integration.py`: 00_SYSTEM version is +1.2KB.

4. **ops/ JSON commit policy**: Are `MATTER_TODO_LEDGER.json`, `emails_attributed.json`,
   and similar ops/ files intended to be committed long-term, or should they be ignored
   after the daily sweep is mature?

5. **Clio cache coverage**: Why does `cache/clio_matters.json` return only 35 matters
   when 41 exist in the repo? Is the Clio API paginating, filtering by status, or
   hitting a scope limitation?
