---
id: 04_initiatives__ll_portfolio__03_firm_operations__project_management__pm_migration_program_md
title: PM Migration Program
owner: ML1
status: active
created_date: 2026-05-19
last_updated: 2026-05-19
tags: [ll, project-management, migration, controls]
---

# PM Migration Program

## Purpose

Operational migration tracker for Levine Law project-management controls.

Doctrine authority lives in:

- `01_DOCTRINE/03_POLICIES/POL-055_Repository_Project_Policy.md`
- `01_DOCTRINE/03_POLICIES/POL-056_Firm_Project_Policy.md`
- `01_DOCTRINE/03_POLICIES/POL-073_Project_Management_Control_Policy.md`

This file exists to track the LL-side migration into conformance.

## Active Cutovers

### 1. Identity

Target rule:
- `Project ID == folder name`

Migration rule:
- normalize `LLP-NNN_NAME` folders to plain `LLP-NNN`
- update `PROJECT_CHARTER.md`, `APPROVAL_RECORD.md`, dependency references, and rollups to match
- remove duplicate declared IDs across distinct folders

### 2. Stage Vocabulary

Target rule:
- canonical stages are `Initiating`, `Planning`, `Executing`, `Closing`

Migration rule:
- retire `implementation/` and `monitoring/` as canonical stage directories
- move live reporting expectations into `Executing`

### 3. Planning Artifact Baseline

Target rule:
- `PROJECT_PLAN.md` is canonical

Migration rule:
- retire `WORKPLAN.md`
- retire `SCOPE_DEFINITION.md`
- normalize legacy planning packets on next structural edit

### 4. Metric Governance

Target rule:
- `METRICS.md` is canonical

Migration rule:
- retire `METRIC_DEFINITION.md`
- retire `MEASUREMENT_METHOD.md`
- retire `BASELINE_CAPTURE_PERIOD.md`
- retire `VALIDATION_REVIEW.md`
- retire `ML1_METRIC_APPROVAL.md`
- move threshold approval into `METRICS.md`

### 5. Control-Surface Conformance

Target rule:
- packets or PM control surfaces marked `READ-ONLY`, `Not yet reviewed`, or otherwise non-authoritative do not receive `on-track`

Migration rule:
- clear false-clean statuses in generated PM outputs
- treat PM conformance failure as a run failure until residue is removed

## Control Outputs

Use these files as the operating migration dashboard:

- `../PORTFOLIO_GOVERNANCE/PM_CONFORMANCE_REPORT.md`
- `../PORTFOLIO_GOVERNANCE/MIGRATION_VALIDATION_REPORT.md`
- `PROJECT_HEALTH_ROLLUP.md`

## Exit Condition

The migration program is complete when:

- the LL PM runner exits zero
- `PM_CONFORMANCE_REPORT.md` shows no remaining failures
- legacy PM artifact families are absent from active governed project packets
- duplicate declared project IDs have been removed
