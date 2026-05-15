---
id: 04_initiatives__ll_portfolio__financial_management_consolidation_plan_md
title: Financial Management Consolidation Plan
owner: ML1
status: implemented
created_date: 2026-05-15
last_updated: 2026-05-15
tags: [ll-portfolio, financial-management, consolidation]
---

# Financial Management Consolidation Plan

## Purpose

Record the implemented consolidation of `01_ACCOUNTING` and
`06_FINANCIAL_PORTFOLIO` into a single top-level LL program:
`01_FINANCIAL_MANAGEMENT`.

This is a structural consolidation plan. It does not collapse accounting and
finance into one analytical layer.

## Implemented Top-Level Change

The prior two-program split:

- `01_ACCOUNTING`
- `06_FINANCIAL_PORTFOLIO`

has been replaced by one canonical top-level program:

- `01_FINANCIAL_MANAGEMENT`

The new program includes both accounting and finance, while preserving the
internal distinction between:

- bookkeeping;
- management accounting;
- budgeting and budget control;
- financial risk and cash/collections;
- finance / capital strategy.

## Why Consolidate

The current structure creates unnecessary top-level separation between domains
that ML1 experiences together as firm financial management.

The separation was useful to clarify that:

- accounting records are not strategy;
- management accounting is not bookkeeping;
- budgeting is not historical fact;
- finance decisions are not automatically authorized by models.

Those boundaries should remain, but they can live inside one parent program.

## Target Internal Structure

Implemented target:

```text
01_FINANCIAL_MANAGEMENT/
├── README.md
├── LLP-001_ACCOUNTING/
├── LLP-002_BUDGETING/
├── management_accounting/
├── LLP-044_FINANCE/
│   ├── LL_FINANCE_PRINCIPLES.md
│   ├── LL_FINANCE_INVARIANTS.md
│   ├── LL_FINANCE_POLICIES.md
│   └── CFO/
└── risk_cash_collections/
```

`LLP-044_FINANCE` is the ML1-approved finance packet ID. Finance should be a
governed packet under `01_FINANCIAL_MANAGEMENT`, not a loose generic folder.

Implemented lower-churn structure:

```text
01_FINANCIAL_MANAGEMENT/
├── README.md
├── LLP-001_ACCOUNTING/
├── LLP-002_BUDGETING/
├── management_accounting/
├── LLP-044_FINANCE/
│   ├── LL_FINANCE_PRINCIPLES.md
│   ├── LL_FINANCE_INVARIANTS.md
│   ├── LL_FINANCE_POLICIES.md
│   └── CFO/
└── risk_cash_collections/
```

This lower-churn structure keeps the existing governed packets visible and
avoids over-nesting.

## Preserved Boundaries

### Bookkeeping

Bookkeeping records what happened:

- invoices;
- collections;
- payments;
- reconciliations;
- expenses;
- trust balances and transfers;
- accounting evidence.

Bookkeeping is not strategy, pricing, forecasting, or profitability judgment.

### Management Accounting

Management accounting analyzes how accounting facts behave as a law-firm
business system:

- revenue timing;
- revenue security;
- recurring vs one-off revenue;
- trust-funded vs unsecured AR;
- matter-level profitability;
- lawyer production;
- WIP conversion;
- collection reliability.

Management accounting may support decisions but does not itself decide.

### Budgeting

Budgeting governs approved baselines, targets, scenarios, and budget-control
views.

The margin-calibrated base case remains the approved baseline unless ML1
approves a specific baseline change with explanation.

Scenario matrices remain sensitivity views, not bankable forecasts.

### Financial Risk / Cash / Collections

This layer tracks risk in the operating money system:

- under-collection;
- uneven revenue conversion;
- AR exposure;
- WIP funding burden;
- liquidity stress;
- cash-risk adjustment.

This is adjacent to `04_RISK`, but its home is financial management when the
question is operating cash and collections rather than general firm risk.

### Finance

Finance governs capital and balance-sheet-level decisions:

- shareholder funding;
- debt facilities;
- credit cards and credit lines;
- tax-planning interfaces;
- major asset/liability decisions;
- leases;
- strategic banking relationships;
- investment and reserve policy;
- corporate finance;
- acquisition financing;
- partner/shareholder distributions.

Finance outputs are advisory unless ML1 approves a specific decision.

## Migration Record

### Step 1 — Doctrine Update

Updated `LL_PORTFOLIO/README.md` and `LL_PROGRAM_REVIEW_MATRIX.md` to recognize
`01_FINANCIAL_MANAGEMENT` as the consolidated financial program.

Status: complete.

### Step 2 — Create New Parent Folder

Created `01_FINANCIAL_MANAGEMENT/README.md` as the new parent program.

The README should state that the program includes accounting, management
accounting, budgeting, financial risk, cash/collections, and finance.

Status: complete.

### Step 3 — Migrate Budgeting First

Moved `LLP-002_BUDGETING` from `06_FINANCIAL_PORTFOLIO` into
`01_FINANCIAL_MANAGEMENT`.

Reason: the current finance README already describes budgeting as legacy
placement, and budgeting belongs naturally inside financial management.

Status: complete.

### Step 4 — Create Finance Packet

Created `01_FINANCIAL_MANAGEMENT/LLP-044_FINANCE/` as the governed finance
packet.

Moved finance doctrine files into `01_FINANCIAL_MANAGEMENT/LLP-044_FINANCE/`:

- `LL_FINANCE_PRINCIPLES.md`
- `LL_FINANCE_INVARIANTS.md`
- `LL_FINANCE_POLICIES.md`
- `CFO/`

Updated relative links to the revenue timing/security taxonomy.

Status: complete.

### Step 5 — Migrate Accounting

Moved `LLP-001_ACCOUNTING` into `01_FINANCIAL_MANAGEMENT`.

Keep its accounting-layer language intact.

Status: complete.

### Step 6 — Deprecate Old Top-Level Folders

Left pointer READMEs in:

- `01_ACCOUNTING/`
- `06_FINANCIAL_PORTFOLIO/`

Each pointer should state:

- this folder is deprecated;
- the canonical home is `01_FINANCIAL_MANAGEMENT`;
- old links are preserved only for transition.

Status: complete.

### Step 7 — Regenerate Portfolio Reports

Run the LL portfolio agents after file movement so project paths and dashboards
reflect the new structure.

Status: pending verification.

## ML1 Decisions

1. Consolidate `01_ACCOUNTING` and `06_FINANCIAL_PORTFOLIO` into
   `01_FINANCIAL_MANAGEMENT`.
2. Retire `06_FINANCIAL_PORTFOLIO` as a canonical program and leave a temporary
   pointer.
3. Keep general financial-risk governance in `04_RISK/LLP-018`, but move cash,
   collections, and operating financial-risk analysis under
   `01_FINANCIAL_MANAGEMENT`.
4. Keep `LLP-002_BUDGETING` as a separate governed project inside
   `01_FINANCIAL_MANAGEMENT`, because approved baseline control is important
   enough to remain visible.
5. Use `LLP-044_FINANCE` for the finance packet.
