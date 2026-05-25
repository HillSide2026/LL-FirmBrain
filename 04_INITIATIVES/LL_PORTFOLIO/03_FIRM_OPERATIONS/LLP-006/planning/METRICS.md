---
id: 04_initiatives_ll_portfolio_03_firm_operations_llp_006_maintenance_planning_metrics_md
title: Metrics
owner: ML1
status: draft
created_date: 2026-05-18
last_updated: 2026-05-18
tags: []
---

# Metrics

Project ID: LLP-006
Project Path: 03_FIRM_OPERATIONS/LLP-006
Stage: Planning

Approval Status: Approved (ML1, 2026-03-16)
Threshold Status: Framework approved. Numeric thresholds to be set from first 4-week operational baseline (2026-03-08 to 2026-03-29).

---

## KPI Definitions

| KPI | Definition | Formula |
| --- | --- | --- |
| `weekly_run_completion_rate` | Share of scheduled Sunday runs completed | `(completed_runs / scheduled_runs) * 100` |
| `active_matter_coverage_rate` | Share of active matters represented in all required reconciliation inputs | `(covered_active_matters / active_matters) * 100` |
| `clio_sb_status_parity_rate` | Share of active matters with no Clio-vs-SB status mismatch | `(parity_matters / active_matters) * 100` |
| `sharepoint_linkage_rate` | Share of active matters with valid SharePoint linkage | `(sharepoint_linked_matters / active_matters) * 100` |
| `asana_linkage_rate` | Share of active matters with valid Asana linkage | `(asana_linked_matters / active_matters) * 100` |
| `critical_exception_resolution_rate` | Share of critical exceptions resolved within SLA window | `(critical_resolved_within_sla / critical_exceptions_due) * 100` |
| `exception_backlog_growth_rate` | Week-over-week growth rate of unresolved exceptions | `((open_exceptions_this_week - open_exceptions_last_week) / open_exceptions_last_week) * 100` |

## Thresholds

| KPI | Target | Status |
| --- | --- | --- |
| `weekly_run_completion_rate` | TBD | Pending baseline |
| `active_matter_coverage_rate` | TBD | Pending baseline |
| `clio_sb_status_parity_rate` | TBD | Pending baseline |
| `sharepoint_linkage_rate` | TBD | Pending baseline |
| `asana_linkage_rate` | TBD | Pending baseline |
| `critical_exception_resolution_rate` | TBD | Pending baseline |
| `exception_backlog_growth_rate` | TBD | Pending baseline |

Thresholds will be anchored to the first 4 Sunday run cycles. Threshold review scheduled at first monthly governance rollup.

## Measurement Method

- Execute reconciliation once per Sunday against active matter set.
- Record run completeness and system-specific extraction results.
- Compute coverage/parity/linkage metrics from observed records only.
- Track exception lifecycle (new, open, resolved) with timestamps.
- Preserve source pointers for all mismatch assertions.

### Calculation Rules
- `active_matters` denominator is the active set from the cycle's canonical matter index snapshot.
- `covered_active_matters` requires usable records from SB, Clio, SharePoint, and Asana for the same matter_id.
- `parity_matters` requires no mismatch in governed status fields between Clio and SB snapshot.
- `sharepoint_linked_matters` requires a valid mapped folder/pointer for the matter.
- `asana_linked_matters` requires at least one valid matter-linked Asana artifact or an explicit N/A classification rule.
- `critical_exceptions_due` includes critical exceptions whose SLA window ended in the measurement window.
- If `open_exceptions_last_week = 0`, `exception_backlog_growth_rate` is reported as `N/A` for that cycle.

### Window and Reporting
- Operational window: weekly Sunday run.
- Default reporting window: trailing 4 weeks for trend metrics.

### Data Sources
- SB matter artifacts (`05_MATTERS`, mappings in `00_SYSTEM`)
- Clio matter export/API snapshot
- SharePoint metadata snapshot
- Asana task/project export/API snapshot
- Reconciliation run logs and exception artifacts

## Baseline Capture Period

- Start: 2026-03-08
- End: 2026-03-29 (first 4 Sunday cycles)

### Purpose
Capture initial four-cycle operating baseline before implementation hardening decisions, so exception behavior and parity performance can be compared against post-implementation performance.

### Inclusion Rules
- Include only scheduled Sunday reconciliation cycles.
- Include only active matters in each cycle snapshot.
- Include only exceptions with source pointers and severity labels.

### Exclusion Rules
- Test/sandbox runs.
- Runs missing one or more required systems without explicit partial-run classification.
- Artifacts lacking run ID or timestamp traceability.

### Baseline Outputs
- Baseline metric snapshot for all KPIs above.
- Baseline exception taxonomy distribution (critical/high/medium/low).
- Baseline median time-to-resolution for critical exceptions.

## Validation

### Review Criteria
- KPI formulas are unambiguous and reproducible.
- Denominators are clearly defined for all coverage/parity/linkage metrics.
- Exception classes are severity-labeled and source-attributed.
- Weekly run completeness can be verified from run artifacts.
- No metric depends on hidden inference or non-governed data.

### Review Outcome
Status: Approved (ML1, 2026-03-16)
Notes: Metric framework approved. Numeric thresholds to be set from first 4-week operational baseline and recorded at first monthly governance rollup.

## Goal Alignment
- Coverage/parity metrics support accurate matter status refresh.
- Linkage metrics support deterministic cross-system reconciliation.
- Resolution/backlog metrics support sustainable weekly operations.

## Retired Metric Artifact Consolidation

- Consolidated on: 2026-05-25
- Retired source artifacts moved to: `10_ARCHIVE/LL_PORTFOLIO_PM_CONFORMANCE_2026-05-25/04_INITIATIVES/LL_PORTFOLIO/03_FIRM_OPERATIONS/LLP-006/planning`
- Retired artifact names: ML1_METRIC_APPROVAL.md
- Threshold approval and measurement details now belong in this `METRICS.md` file.

