---
id: POL-065
title: Matthew Holdings Initiative Risk Policy
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
created_date: 2026-03-13
last_updated: 2026-03-23
tags: [policy, risk, hillside, matthew-holdings]
---

# POL-065 - MATTHEW HOLDINGS INITIATIVE RISK POLICY

## 1. Scope

This policy governs risk classification and risk tracking for ownership-layer initiatives under:

- `04_INITIATIVES/HillSide_PORTFOLIO/`
- `04_INITIATIVES/HillSide_PORTFOLIO/MATTHEW_HOLDINGS_17513721_CANADA_INC/`

This policy applies to:
- venture evaluation
- asset sale or divestiture initiatives
- regulated-shell monetization initiatives
- partnership or tie-up initiatives
- new-build initiatives pursued for ownership-level value creation

This policy does not apply to:
- Levine Law internal initiatives in `LL_PORTFOLIO`
- client matters

## 2. Purpose

Matthew Holdings initiatives are ownership and capital-allocation decisions, not firm-operations projects. They therefore require a policy that defaults to investment and portfolio-risk framing rather than only delivery framing.

## 3. Canonical Category Set

Matthew Holdings initiatives must use only the following canonical categories:
- `Scope`
- `Schedule`
- `Budget`
- `Financial`
- `Strategic`

## 4. Default Applicability Rule

Unless ML1 explicitly classifies an initiative otherwise, Matthew Holdings initiatives must be treated as ownership-level strategic initiatives.

That means all five categories are available:
- `Scope`
- `Schedule`
- `Budget`
- `Financial`
- `Strategic`

## 5. Category Meaning in Matthew Holdings Context

### `Strategic`

Use for:
- alignment or misalignment with ownership objectives
- portfolio-positioning exposure
- partnership alignment risk
- structural dependency or concentration concerns

### `Financial`

Use for:
- valuation risk
- buyer-search cost exposure
- transaction economics risk
- ROI uncertainty
- opportunity cost of capital allocation

### `Schedule`

Use for:
- regulatory timing risk
- approval-response timing risk
- closing or launch timing uncertainty
- dependency-driven delays

### `Scope`

Use for:
- transaction or initiative expansion beyond original intent
- added integration complexity
- execution-boundary drift

### `Budget`

Use for:
- risk of exceeding an established initiative budget
- overruns against approved advisor, diligence, or build spend

`Budget` is not a substitute for general financial exposure. If no approved budget exists, do not force a `Budget` risk.

## 6. Tracking Rules

### Pipeline-Level Tracking

Initiative pipelines may use compact plain-language entries, but every listed risk must still be assignable to exactly one canonical category.

Recommended pattern:
- `<Category> risk: <specific exposure>.`

### Structured Risk Register

When an initiative advances beyond early screening, a structured risk register should decompose each risk into:
- `Risk`
- `Category`
- `Likelihood`
- `Impact`
- `Mitigation`

Each row must carry exactly one category.

## 7. Related Doctrine

- `01_DOCTRINE/01_INVARIANTS/INV-0013-risk-model.md`
- `01_DOCTRINE/01_INVARIANTS/INV-0014-risk-classification-invariants.md`
- `01_DOCTRINE/03_POLICIES/POL-063_Project_Risk_Artifact_Lifecycle_Policy.md`
