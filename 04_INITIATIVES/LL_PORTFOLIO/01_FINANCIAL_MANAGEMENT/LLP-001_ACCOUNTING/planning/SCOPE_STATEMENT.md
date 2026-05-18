---
id: 04_initiatives_ll_portfolio_01_financial_management_llp_001_accounting_planning_scope_statement_md
title: Scope Statement
owner: ML1
status: draft
created_date: 2026-05-18
last_updated: 2026-05-18
tags: []
---

# Scope Statement

Project ID: LLP-001
Project Path: 01_FINANCIAL_MANAGEMENT/LLP-001_ACCOUNTING
Stage: Planning

## Planning Objective

Define the execution-ready boundary for Levine Law's accounting fact layer so
historical records can be captured, reconciled, reviewed, and handed
downstream without drifting into modeling or decision authority.

## In Scope

### 1. Historical Fact Record Set

- booked transactions and supporting schedules
- bank, card, payment, and invoice-source evidence
- expense support and reimbursement records
- close support materials tied to observed historical activity

### 2. Reconciliation and Close Control Design

- identify the source classes that must reconcile into the governed packet
- lock the cadence for routine reconciliation and close review
- define how variances, unresolved items, and late evidence are captured
- define the minimum close support package for ML1 review

### 3. Exception and Review Governance

- define who prepares, reviews, and escalates accounting exceptions
- define which exceptions require explicit ML1 judgment
- define how unresolved items remain visible without being silently absorbed

### 4. Downstream Handoff Discipline

- define what facts may flow from LLP-001 into LLP-002
- define freshness and evidence expectations for any downstream fact handoff
- define how modeling consumers are warned when accounting facts are incomplete

### 5. Program and Project Spend Classification

- effective 2026-07-01, in-scope acquisition spend must be tracked as a
  governed project / program classification inside the accounting fact layer
- `acquisition` means the combined marketing and sales spend used to generate
  new business
- source-level detail should remain preserved so marketing and sales components
  can still be distinguished when the underlying records support that split
- LLP-001 owns the historical tagging of actual acquisition spend; LLP-002 owns
  the budget envelope and any scenario interpretation built from it

## Explicit Exclusions

- forecasting, scenario modeling, or planning assumptions
- pricing, discounting, or profitability recommendations
- strategic conclusions drawn from accounting patterns without ML1 review
- software-replacement, ERP-selection, or broad systems-transformation work
- tax-planning, compensation-design, or entity-structure redesign
- CAC, ROAS, pipeline-efficiency, or other performance interpretation inside
  LLP-001

## Boundary with LLP-002

LLP-001 owns historical facts only. LLP-002 may consume approved accounting
facts as model inputs, but LLP-002 does not define what counts as a valid
accounting fact, what evidence is sufficient, or when reconciliation is
complete.

For acquisition specifically:

- LLP-001 supplies actual historical spend tagged to the `acquisition`
  project / program classification starting 2026-07-01
- LLP-002 sets the combined acquisition budget for marketing + sales and may
  model pacing, variance, and scenario impacts from those facts

## Completion Condition

Planning is complete when ML1 can approve one clear operating shape for:

1. the fact sources in scope
2. the reconciliation and close cadence
3. the exception-review path
4. the fact-only handoff into LLP-002
5. the acquisition-spend classification and handoff rule effective 2026-07-01
