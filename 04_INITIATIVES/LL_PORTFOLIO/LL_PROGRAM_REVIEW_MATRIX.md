---
id: 04_initiatives__ll_portfolio__ll_program_review_matrix_md
title: LL Program Review Matrix
owner: ML1
status: draft
created_date: 2026-04-03
last_updated: 2026-04-03
tags: [ll-portfolio, programs, review]
---

# LL Program Review Matrix

## Purpose

Provide a fast, repeatable path for reviewing one Levine Law program at a time.

Use this file after the portfolio-level read in `LL_PORTFOLIO_REVIEW.md` when
the next question is: which program needs attention, and where should the
review start?

## Standard Program Review Sequence

For any numbered LL program:

1. Read the relevant row in `LL_PROGRAM_SUMMARY_REPORT.md`
2. Open the program `README.md`
3. Review the governed packet folders inside that program
4. Cross-check relevant packet health in `03_FIRM_OPERATIONS/PROJECT_MANAGEMENT/PROJECT_HEALTH_ROLLUP.md`
5. If the issue is cross-project or stage-gate related, cross-check
   `PORTFOLIO_STATUS_DASHBOARD.md` and `GOVERNANCE_COMPLIANCE_AUDIT.md`

## Standard Review Questions

Use the same five questions for every program:

1. Is the program boundary still clean?
2. Are the governed packets real, active, and appropriately staged?
3. Are there missing approvals or artifact gaps suppressing signal quality?
4. Which packet in the program matters most right now?
5. Is the next action an ML1 decision, a system drafting task, or a park call?

## Program Matrix

Consolidation note: `01_ACCOUNTING` and `06_FINANCIAL_PORTFOLIO` have been
consolidated into `01_FINANCIAL_MANAGEMENT`. See
`FINANCIAL_MANAGEMENT_CONSOLIDATION_PLAN.md`. The old folders are transition
pointers only.

| Program | Start Here | Primary Review Question | Useful Cross-Checks |
| --- | --- | --- | --- |
| `01_FINANCIAL_MANAGEMENT` | `01_FINANCIAL_MANAGEMENT/README.md` | Are accounting, management accounting, budgeting, cash/collections, and finance unified without collapsing their internal boundaries? | `LLP-001_ACCOUNTING`, `LLP-002_BUDGETING`, `LLP-044_FINANCE`, `LL_PROGRAM_SUMMARY_REPORT.md` |
| `02_PRACTICE_AREAS` | `02_PRACTICE_AREAS/README.md` | Are the practice-area packets formalized enough to serve as governed operating knowledge? | `LL_PROGRAM_SUMMARY_REPORT.md`, packet READMEs under `LLP-015`, `LLP-035`, `LLP-036` |
| `03_FIRM_OPERATIONS` | `03_FIRM_OPERATIONS/README.md` | Are the firm-running systems mature, current, and properly governed? | `PORTFOLIO_MANAGEMENT/`, `PORTFOLIO_GOVERNANCE/`, `PROJECT_MANAGEMENT/` |
| `04_RISK` | `04_RISK/README.md` | Does the risk layer surface real defensive clarity or only placeholder structure? | `LLP-017`, `LLP-018`, `GOVERNANCE_COMPLIANCE_AUDIT.md` |
| `05_MATTER_DOCKETING` | `05_MATTER_DOCKETING/README.md` | Is the matter-delivery overlay clear and separate from billing, intake, and accounting? | `LLP-003`, `LLP-009`, `LLP-010`, `PROJECT_HEALTH_ROLLUP.md` |
| `07_GROWTH_PROJECTS` | `07_GROWTH_PROJECTS/README.md` | Which growth projects are real near-term operating bets versus placeholder future-state slots? | `LLP-023`, `LLP-024`, `LLP-030`, `LLP-031`, `LLP-032`, `LLP-033`, `LLP-034` |
| `08_MARKETING` | `08_MARKETING/README.md` | Is the pre-matter pipeline sequencing coherent from funnel through intake handoff? | `LLP-011` to `LLP-029`, `PORTFOLIO_STATUS_DASHBOARD.md`, `ML1_DECISION_QUEUE.md` |
| `09_SERVICE_MANAGEMENT` | `09_SERVICE_MANAGEMENT/README.md` | Is the service-tier cluster substantive enough to justify remaining active as separate packets? | `LLP-037` to `LLP-041`, `PROJECT_HEALTH_ROLLUP.md`, `GOVERNANCE_COMPLIANCE_AUDIT.md` |

## Program-Specific Review Notes

### 01_FINANCIAL_MANAGEMENT

Priority question:
- are the financial layers unified enough for ML1 review while still preserving the boundaries between bookkeeping, management accounting, budgeting, financial risk/cash/collections, and finance?

### 02_PRACTICE_AREAS

Priority question:
- are these packets still mostly registry slots, or are they becoming usable governed knowledge surfaces?

### 03_FIRM_OPERATIONS

Priority question:
- are the operational systems keeping up with real execution, especially the portfolio-management and governance layers?

### 04_RISK

Priority question:
- is the risk program producing decision-useful risk clarity, or just carrying placeholder packet structure?

### 05_MATTER_DOCKETING

Priority question:
- is the docketing overlay practically supporting matter delivery without crossing into other administrative domains?

### 07_GROWTH_PROJECTS

Priority question:
- which projects in this cluster should actively shape 2026 execution, and which should be parked or de-emphasized?

### 08_MARKETING

Priority question:
- is the funnel-to-intake architecture progressing in the intended order, or is execution running ahead of governance?

### 09_SERVICE_MANAGEMENT

Priority question:
- should the service-management cluster be strengthened, consolidated, or parked to reduce governance noise?

## Review Output Format

When writing a program review note, use this short structure:

- `program`
- `boundary read`
- `current dominant condition`
- `highest-value packet`
- `blocking gaps`
- `ml1 decisions needed`
- `system-follow-up possible`
