---
id: POL-064
title: Levine Law Initiative Risk Policy
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
tags: [policy, risk, ll-portfolio]
---

# POL-064 - LEVINE LAW INITIATIVE RISK POLICY

## 1. Scope

This policy governs risk classification and risk artifact expectations for initiatives inside `04_INITIATIVES/LL_PORTFOLIO/`.

This policy applies to:
- Strategic projects
- Management projects
- Operational projects

This policy does not apply to:
- Client matters
- HillSide / Matthew Holdings initiatives

## 2. Purpose

Levine Law initiatives need a portfolio-specific policy because not all LL initiatives carry the same risk axes. Category usage must stay consistent with work type and must not drift into ad hoc labels.

## 3. Canonical Category Set

Levine Law initiatives must use only the following canonical categories:
- `Scope`
- `Schedule`
- `Budget`
- `Financial`
- `Strategic`

No alternate category systems are permitted in canonical risk artifacts.

## 4. Category Applicability by Work Type

### Strategic Projects

Allowed categories:
- `Scope`
- `Schedule`
- `Budget`
- `Financial`
- `Strategic`

### Management Projects

Allowed categories:
- `Scope`
- `Schedule`
- `Budget`
- `Financial`
- `Strategic`

### Operational Projects

Allowed categories:
- `Scope`
- `Schedule`
- `Budget`

Operational projects must not introduce `Financial` or `Strategic` categories unless ML1 explicitly reclassifies the work type.

## 5. Artifact Rules

### `RISK_SCAN.md`

- May use plain-language top-risk statements.
- Every risk must still be classifiable under exactly one allowed category for the project type.
- If a risk appears to span more than one category, it must be rewritten or split.

### `RISK_REGISTER.md`

- Must include a `Category` column.
- Each row must carry exactly one category.
- Category names must match the canonical labels exactly.

### `RISKS_INITIAL.md`

- Deprecated for Levine Law initiatives.
- Legacy `RISKS_INITIAL.md` files must be migrated or replaced by canonical lifecycle artifacts.

## 6. Portfolio Boundary

This policy governs internal Levine Law initiative work. It is not the policy for ownership-layer initiatives, venture evaluation, entity monetization, or HillSide capital allocation decisions.

## 7. Related Doctrine

- `01_DOCTRINE/01_INVARIANTS/INV-0013-risk-model.md`
- `01_DOCTRINE/01_INVARIANTS/INV-0014-risk-classification-invariants.md`
- `01_DOCTRINE/03_POLICIES/POL-063_Project_Risk_Artifact_Lifecycle_Policy.md`
