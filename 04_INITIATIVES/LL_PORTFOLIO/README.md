---
id: 04_initiatives__ll_portfolio__readme_md
title: LL_PORTFOLIO — Levine Law Workstream Registry
owner: ML1
status: draft
created_date: 2026-02-08
last_updated: 2026-05-15
tags: []
---

# LL_PORTFOLIO — Levine Law Workstream Registry

## Meta-Rule

> **ML2 preserves ML1 intent. It does not approximate, infer, or replace it.**
>
> **When in doubt: STOP. LABEL. ESCALATE.**

---

## Core Definition

The LL Portfolio is a **governed, non-autonomous registry** where:

- **ML1** is the sole authority for judgment, approval, pricing, and strategy
- **ML2** preserves structure, scope, constraints, and state
- **LL** consumes ONLY ML1-approved outputs

## Portfolio Review Entry Points

Use these files to review the LL portfolio quickly:

- `LL_PORTFOLIO_REVIEW.md` — single front door for the portfolio review stack
- `CHIEF_OF_STAFF/README.md` — canonical synthesis layer for ML1 review
- `LL_PROGRAM_REVIEW_MATRIX.md` — fast path for program-by-program review
- `LL_PROGRAM_SUMMARY_REPORT.md` — current summary of the 9 numbered programs

When the Chief of Staff packet is current, start with:

1. `CHIEF_OF_STAFF/COS_BRIEF.md`
2. `CHIEF_OF_STAFF/ML1_DECISION_QUEUE.md`

When the Chief of Staff packet is stale, start with:

1. `LL_PROGRAM_SUMMARY_REPORT.md`
2. `03_FIRM_OPERATIONS/PORTFOLIO_MANAGEMENT/PORTFOLIO_STATUS_DASHBOARD.md`
3. `03_FIRM_OPERATIONS/PORTFOLIO_GOVERNANCE/GOVERNANCE_COMPLIANCE_AUDIT.md`
4. `03_FIRM_OPERATIONS/PROJECT_MANAGEMENT/PROJECT_HEALTH_ROLLUP.md`

## Review Hierarchy

The intended review hierarchy for Levine Law is:

1. Portfolio
2. Relevant programs
3. Relevant projects
4. Matters

That means matters sit inside the LL operating picture. They are not a
separate peer portfolio even though their source-of-truth files live under
`05_MATTERS/`.

## Program-Led / Matter-Aware Review Rule

LL must be organized around the numbered `LL_PORTFOLIO` program structure, not
around individual matters.

However, ML1 must be able to shift quickly from the LL portfolio level to the
matter portfolio level whenever the operating question becomes delivery,
client-service urgency, WIP conversion, matter quality, or matter-level
capacity.

Use the following transition:

1. Start at `LL_PORTFOLIO_REVIEW.md` for the top-level LL operating picture.
2. Identify the relevant program and project layer first.
3. Shift to `../../05_MATTERS/DASHBOARDS/MATTER_DIGEST.md` when ML1 needs to see
   which matters require handling or checking.
4. Shift to `../../05_MATTERS/DASHBOARDS/MATTER_INDEX.md` when ML1 needs the full
   matter roster, classification, and source-folder map.

The matter portfolio is therefore a drill-down control surface inside the LL
operating system. It is not the organizing spine of LL itself.

## Project Identity

Levine Law project identity is governed by:

- `01_DOCTRINE/03_POLICIES/POL-055_Repository_Project_Policy.md`
- `01_DOCTRINE/03_POLICIES/POL-056_Firm_Project_Policy.md`
- `01_DOCTRINE/03_POLICIES/POL-073_Project_Management_Control_Policy.md`

Working rules:

- Every governed project has one canonical identifier: `Project ID`.
- `Project ID` equals the project folder name.
- `Project Path` is a storage/location key and must not be treated as identity.
- New LL projects must use plain `LLP-NNN` folder names.
- Existing `LLP-NNN_NAME` folders are migration residue and should be
  normalized, not copied forward.

---

## LL Work Type Taxonomy

The LL system recognizes four work types:

- Strategic projects
- Management projects
- Operational projects
- Decision projects
- Client matters (aka client projects)

Definitions:

- Strategic projects: firm-direction initiatives that define or materially change long-horizon operating posture.
- Management projects: governance and control initiatives that coordinate, monitor, or optimize firm systems.
- Operational projects: execution-focused initiatives that improve how defined workflows are carried out.
- Decision projects: bounded evaluation projects whose main deliverable is an ML1 go / hold / no-go or reclassification decision.
- Client matters/client projects: client-specific legal work units governed by matter doctrine.

Applicability:

- The project stage-gate artifact lifecycle applies to strategic, management,
  operational, and decision projects.
- Client matters/client projects follow matter doctrine and matter-stage artifacts.
- If project type classification is unclear, escalate to ML1 before stage advancement.

## Planning Stage Standard

For governed LL projects, the `Planning` stage exists to prepare a clean
execution-authorization decision.

Planning artifacts must be:

- project-specific
- decision-oriented
- execution-focused
- as lean as possible while still supporting ML1 approval

Planning artifacts must not become planning for the sake of planning.

Required planning artifact set:

Strategic and management projects:

- `SCOPE_STATEMENT.md`
- `PROJECT_PLAN.md`
- `ASSUMPTIONS_CONSTRAINTS.md`
- `DEPENDENCIES.md`
- `RISK_REGISTER.md`
- `COMMUNICATION_PLAN.md`
- `METRICS.md`

Operational projects:

- `SCOPE_STATEMENT.md`
- `PROJECT_PLAN.md`
- `DEPENDENCIES.md`
- `RISK_REGISTER.md`
- `METRICS.md`

Operational projects may add these when the work actually needs them:

- `ASSUMPTIONS_CONSTRAINTS.md`
- `COMMUNICATION_PLAN.md`

Decision projects:

- `DECISION_FRAME.md`
- `PROJECT_PLAN.md`
- `ASSUMPTIONS_CONSTRAINTS.md`
- `DEPENDENCIES.md`
- `RISK_REGISTER.md`
- `METRICS.md`

Planning best-practice rules:

- `SCOPE_STATEMENT.md` locks the actual execution boundary and exclusions.
- `PROJECT_PLAN.md` locks the project decisions, sequence, and gate-readiness
  path. It should not read like generic PM overhead. Legacy `WORKPLAN.md`
  files remain acceptable during transition and should be normalized on next
  edit.
- `ASSUMPTIONS_CONSTRAINTS.md` captures the assumptions the project depends on and the limits it cannot cross.
- `DEPENDENCIES.md` lists only dependencies that could materially affect
  execution or authorization.
- `RISK_REGISTER.md` tracks risks that matter to scope, schedule, budget, operating control, or gate readiness.
- `COMMUNICATION_PLAN.md` should be minimal and limited to decision loops, coordination points, and escalation triggers. It is expected by default for strategic and management projects and optional for operational projects unless coordination complexity warrants it.
- `METRICS.md` is the single source for metric definitions, measurement method, baseline logic, validation rules, and ML1 threshold approval. `ML1_METRIC_APPROVAL.md` is legacy and should not be created for new work.
- Decision projects should use the lightest planning packet that still supports
  the specific ML1 decision at issue.

## PM Control Layer

LL project-management control behavior is governed in doctrine, not by this
README.

See:

- `01_DOCTRINE/03_POLICIES/POL-073_Project_Management_Control_Policy.md`

This includes:

- folder-name identity control
- stage-vocabulary migration
- retirement of `WORKPLAN.md` and split metric files
- health-state rules
- sequencing and WIP logic
- matter-to-project prioritization
- PM conformance failure rules

If a planning artifact does not help lock scope, reduce uncertainty, or support
the Planning -> Executing gate decision, it should be merged or removed.

---

## Canonical Structure (LOCKED)

```
LL_PORTFOLIO/
├── README.md                    ← You are here (authoritative)
├── 01_FINANCIAL_MANAGEMENT/     # Accounting, management accounting, budgeting, finance, cash/collections
├── 01_ACCOUNTING/               # Deprecated transition pointer
├── 02_PRACTICE_AREAS/           # Durable legal operating knowledge
├── 03_FIRM_OPERATIONS/          # How the firm runs
├── 04_RISK/                     # Defensive clarity
├── 05_MATTER_DOCKETING/         # Delivery overlay for matters
├── 06_FINANCIAL_PORTFOLIO/      # Deprecated transition pointer
├── 07_GROWTH_PROJECTS/          # Change and evolution
├── 08_MARKETING/                # Pre-matter pipeline (leads -> conversion; handoff enters fulfillment onboarding)
└── 09_SERVICE_MANAGEMENT/       # Service tier management across matters
```

**This structure is LOCKED unless explicitly changed by ML1.**

You must not infer, reorder, merge, or repurpose these folders.

## Financial Management Consolidation

ML1 approved consolidation of `01_ACCOUNTING` and `06_FINANCIAL_PORTFOLIO`
into a single `01_FINANCIAL_MANAGEMENT` program.

Financial management is now the parent domain while preserving internal
distinctions among bookkeeping, management accounting, budgeting, financial
risk, cash/collections, and finance.

Migration artifact:

- `FINANCIAL_MANAGEMENT_CONSOLIDATION_PLAN.md`

Canonical folder:

- `01_FINANCIAL_MANAGEMENT/`

Deprecated transition pointers:

- `01_ACCOUNTING/`
- `06_FINANCIAL_PORTFOLIO/`

## Review Support Artifacts Outside the Numbered Programs

These support review and synthesis but are not part of the numbered program
directories:

- `CHIEF_OF_STAFF/`
- `LL_PROGRAM_SUMMARY_REPORT.md`
- `LL_PROJECT_DIGEST.md`
- `LL_PROJECT_DIGEST.tsv`
- `LL_GLOSSARY.md`
- `LL_PORTFOLIO_REVIEW.md`
- `LL_PROGRAM_REVIEW_MATRIX.md`

---

## Portfolio Definitions

### 01_FINANCIAL_MANAGEMENT (Financial Management)

**Purpose:** Govern accounting, management accounting, budgeting, financial risk, cash/collections, and finance within one financial-management program.

**Characteristics:** Layered financial-management domain; each artifact must label whether it is bookkeeping, management accounting, budgeting, financial risk/cash/collections, or finance.

| ALLOWED | PROHIBITED |
|---------|------------|
| Bookkeeping records | Unlabelled mixing of accounting layers |
| Historical financial statements | Treating management accounting as bookkeeping |
| Reconciliations | Pricing decisions without ML1 approval |
| Invoices, payments, expense logs | Recommendations or optimization without explicit authority |
| Management accounting: revenue security, recurring vs one-off, revenue timing, trust-funded vs unsecured AR, matter-level profitability, lawyer production, WIP conversion, collection reliability | Unsupported assumptions about the future |
| Budgeting boundaries and controls | Treating budget outputs as operating decisions |
| Finance: capital, liabilities, strategic banking, tax interfaces, major asset/liability decisions, investment/reserve policy, corporate finance, acquisition financing, partner/shareholder distributions | Treating finance models as decisions |

**Rule:** Financial-management artifacts may inform decisions, but bookkeeping, management accounting, budgeting, financial risk/cash/collections, and finance must be labelled and not collapsed into one another.

---

### 02_PRACTICE_AREAS

**Purpose:** Durable legal operating knowledge by domain.

| ALLOWED | PROHIBITED |
|---------|------------|
| Playbooks, checklists, standards | Client-specific material |
| ML1-approved doctrine | Pricing, strategy |
| Version tracking | "Common practice" as authority |

---

### 03_FIRM_OPERATIONS

**Purpose:** How the firm runs day-to-day.

| ALLOWED | PROHIBITED |
|---------|------------|
| SOPs | Policy decisions |
| Process documentation | Enforcement without ML1 approval |
| Templates, internal workflows | Financial modeling |

---

### 04_RISK

**Purpose:** Defensive clarity and audit readiness.

| ALLOWED | PROHIBITED |
|---------|------------|
| Risk registers | Declaring compliance status |
| Compliance doctrines | Closing issues autonomously |
| Violation tracking, resolution logs | Waiving controls |

---

### 05_MATTER_DOCKETING

**Purpose:** Delivery and docketing overlay for matters in the system of record.

| ALLOWED | PROHIBITED |
|---------|------------|
| Matter State tracking (delivery posture) | Billing, accounting, collections |
| Activity Period tagging | CRM, intake, sales, pre-engagement |
| Delivery-related LL Legal Tasks | Pricing, strategy, financial modeling |
| Email-to-operations-queue event mapping | Modifying Clio source-of-truth fields |
| Suggested operations queue transitions (ML1 approval required) | Auto-applying State/Period changes without authorization |

---

### 07_GROWTH_PROJECTS

**Purpose:** Change, experimentation, and future direction.

**Characteristics:** Explicitly NON-AUTHORITATIVE until approved, judgment-heavy

| ALLOWED | PROHIBITED |
|---------|------------|
| Strategy drafts | Operating rules |
| Tradeoff analysis | Execution |
| Scenario exploration | Silent promotion into operations or pricing |

---

### 08_MARKETING

**Purpose:** Pre-matter pipeline for how potential work enters the firm.

**Characteristics:** Pre-matter only, ends at end of marketing conversion, no delivery semantics

| ALLOWED | PROHIBITED |
|---------|------------|
| Lead capture and tracking | Legal delivery work |
| Intake qualification | Docketing or capacity management |
| Conversion workflow and fulfillment handoff package | Modifying delivery states or periods |
| Conversion analytics | Billing, accounting, pricing decisions |
| Handoff to Matter Docketing | Accepting/rejecting work autonomously |

**Critical Boundary:**
- Marketing ends at the end of Conversion (marketing term)
- Fulfillment begins at Onboarding (fulfillment term)
- Matter Docketing begins when a matter exists
- **They must not overlap.**

---

### 09_SERVICE_MANAGEMENT

**Purpose:** Service-tier control map used to classify and monitor service posture.

| ALLOWED | PROHIBITED |
|---------|------------|
| Tier classification and service status tracking | Replacing matter/source-of-truth records |
| Cross-matter service visibility | Autonomously changing legal strategy |
| Escalation signaling for ML1 review | Publishing unapproved client-facing outputs |

---

## README Requirement (Mandatory)

Each folder under LL_PORTFOLIO must contain a README.md stating:

- Purpose
- Scope
- ML1 authority statement
- Explicit prohibitions
- Approval state
- Last ML1 review date

**If a README is missing or outdated:**
- Treat the folder as READ-ONLY
- Do not generate new outputs
- Escalate to ML1

---

## Enforcement Rule

If authorization is unclear:

**STOP. FLAG. ESCALATE TO ML1.**

---

## References

- 04_INITIATIVES Overview: `../README.md`
- Folder Map: `00_SYSTEM/architecture/FOLDER_MAP.md`
- Authority Hierarchy: `01_DOCTRINE/01_INVARIANTS/INV-0008-authority-hierarchy-ml1-ml2-system-ll.md`
- LL Project Digest (32 projects): `LL_PROJECT_DIGEST.md`
