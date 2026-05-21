---
id: repo_cleanup_audit_2026_05_20
title: Repo Cleanup Audit
owner: ML1
status: draft
created_date: 2026-05-20
last_updated: 2026-05-20
tags: [repo-cleanup, internal-records, audit]
---

# Repo Cleanup Audit

Purpose: identify internal records that are cluttering the repo and are safe
candidates to keep, archive, consolidate, or mark for deletion review.

This is a read-only audit. No files were deleted, moved, or rewritten.

Scope for this first pass:

- internal run logs
- generated audit/report outputs
- dashboard/report clusters
- obvious system exhaust

Excluded from this first pass:

- legal/matter source records
- SharePoint raw source files
- client documents
- doctrine and strategy artifacts that appear canonical

---

## Summary

The repo has a large amount of internal system output. The clearest cleanup
targets are not legal records. They are repeated run logs, generated audit
outputs, and internal dashboards that appear to be snapshots rather than
current operating records.

High-signal findings:

- `06_RUNS` contains 1,757 files.
- `06_RUNS/ops/backlog_cleanup` contains 60 files, mostly paired run logs and
  summary files.
- `06_RUNS` contains 28 `SYSTEM-ADMIN-SWEEP` run directories.
- `06_RUNS/logs/matter_admin` contains 85 JSON run logs.
- `04_INITIATIVES/LL_PORTFOLIO/03_FIRM_OPERATIONS/PORTFOLIO_GOVERNANCE`
  contains 7 generated governance report files.
- `04_INITIATIVES/LL_PORTFOLIO/03_FIRM_OPERATIONS/PORTFOLIO_MANAGEMENT`
  contains several generated dashboard/report files mixed with durable
  planning artifacts.

Recommended first cleanup move:

> Consolidate generated internal reports and run logs into retained summaries,
> then archive or delete redundant run-level records only after ML1 approval.

---

## Keep

Keep these categories as current operating records:

- `README.md` files that explain folder purpose
- doctrine files under `01_DOCTRINE`
- active strategy/project artifacts under `04_INITIATIVES`
- matter records under `05_MATTERS`
- canonical indexes, registries, and policies
- current dashboards that are actively used for decisions

Do not cleanup legal/matter source records in this pass.

---

## Archive

Archive candidates are old internal records that may preserve useful history but
should not remain in active operating folders.

Candidates:

- older `SYSTEM-ADMIN-SWEEP` directories under `06_RUNS`
- older generated governance reports under
  `04_INITIATIVES/LL_PORTFOLIO/03_FIRM_OPERATIONS/PORTFOLIO_GOVERNANCE`
- older generated portfolio-management snapshots under
  `04_INITIATIVES/LL_PORTFOLIO/03_FIRM_OPERATIONS/PORTFOLIO_MANAGEMENT`
- old `06_RUNS/ops/sla_audit` outputs, especially where both `.json` and `.md`
  versions exist for the same event

Suggested archive rule:

- keep the latest useful report in place
- move older snapshots to `10_ARCHIVE` or an archive subfolder
- mark archived items as deprecated where practical

---

## Consolidate

Consolidation candidates are clusters where many small internal records could
be replaced by one retained summary.

### 1. Backlog Cleanup Runs

Path:

`06_RUNS/ops/backlog_cleanup`

Observed:

- 60 files
- repeated `run_YYYYMMDD-...ndjson` files
- paired `run_YYYYMMDD-..._summary.json` files
- daily/repeated operational output

Recommended disposition:

- consolidate into a monthly or current-state summary
- retain only the most recent few raw runs if they are operationally useful
- mark older raw `.ndjson` files as delete candidates after summary retention

### 2. Matter Admin Run Logs

Path:

`06_RUNS/logs/matter_admin`

Observed:

- 85 JSON run logs
- repeated timestamped automation output

Recommended disposition:

- consolidate into one matter-admin run history summary
- keep recent logs only if needed for debugging
- mark older logs as delete candidates after summary retention

### 3. System Admin Sweeps

Path pattern:

`06_RUNS/RUN-*-SYSTEM-ADMIN-SWEEP-*`

Observed:

- 28 run directories
- many contain repeated `system_admin` reports

Recommended disposition:

- keep latest sweep report as current reference
- consolidate historical sweep findings into a single sweep-history summary
- archive or delete older run directories after confirming no unique decisions
  live only in those reports

### 4. Soft Junk / Gmail Ops Outputs

Path:

`06_RUNS/ops`

Observed examples:

- `soft_junk_review_*.json`
- `soft_junk_review_*.md`
- `soft_junk_cleanup_audit.ndjson`
- `gmail_label_audit.ndjson`
- `gmail_mcp_audit.ndjson`
- `gmail_label_manifest_dryrun.json`
- `gmail_label_manifest_execute.json`

Recommended disposition:

- consolidate into one retained Gmail cleanup/audit summary
- retain approval records separately where they document ML1 approval
- delete or archive repeated review drafts after approval trail is preserved

---

## Delete Candidates

Delete candidates are not approved for deletion. They are candidates for a
future approved cleanup.

Strong delete-candidate classes:

- old raw `.ndjson` run logs where a summary exists
- duplicate `.json` and `.md` outputs for the same internal audit event where
  only one version is useful
- failed or superseded system-admin sweep runs with no unique decisions
- temporary candidate lists later superseded by an approval record or final
  execution log
- generated reports that are recreated by automation and not used as durable
  evidence

Do not delete:

- matter documents
- client records
- SharePoint raw source files
- legal deliverables
- signed/approved records
- current operating dashboards
- doctrine/policy files

---

## First Cleanup Recommendation

Start with `06_RUNS/ops/backlog_cleanup`.

Why:

- It is clearly internal automation output.
- It has obvious repeated log/summary pairs.
- It is separate from legal/matter source records.
- It is small enough to clean safely.

Recommended next step:

1. Create one retained summary for backlog-cleanup runs.
2. Keep the latest 3-5 raw run pairs.
3. Mark older raw run pairs as delete candidates.
4. Confirm with ML1 before deletion.

---

## Open Question

Should `06_RUNS` be treated as:

- a durable audit archive, where old runs are archived but rarely deleted; or
- an operational log area, where summarized old runs can be deleted after a
  retention period?

This decision controls how aggressive the cleanup can be.

