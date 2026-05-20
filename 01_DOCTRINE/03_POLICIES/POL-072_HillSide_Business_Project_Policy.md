---
id: POL-072
title: HillSide Business Project Policy
owner: ML1
status: approved
approved_by: ML1
approved_date: 2026-05-19
version: '1.0'
created_date: 2026-05-19
last_updated: 2026-05-19
tags: [doctrine, policy, hillside, business-projects, stage-gates]
---

# HillSide Business Project Policy

## 1. Purpose

This policy is the doctrine-level subsidiary project policy for HillSide
business projects.

Canonical repository-level project stages, stage-gate rules, baseline artifact
requirements, and project-typing rules are defined in
`01_DOCTRINE/03_POLICIES/POL-055_Repository_Project_Policy.md`.

This policy applies those repository-level rules to HillSide business-project
packets and defines the HillSide-specific scope for their use.

## 2. Policy Hierarchy

`01_DOCTRINE/03_POLICIES/POL-055_Repository_Project_Policy.md` is the
repository-level canonical project policy.

This policy is explicitly subordinate to that repo-level project policy.

This policy may add HillSide-specific application rules, but it may not replace
the canonical delivery stages, ML1 stage-gate authority, Project ID rules,
project-type rules, or baseline artifact requirements defined at the repo
level.

## 3. Scope

This policy applies directly to:

- `04_INITIATIVES/HillSide_PORTFOLIO/BUSINESS_PROJECTS/HBP-*`

This policy does not apply to:

- entity folders outside `BUSINESS_PROJECTS`
- HillSide personal projects
- Levine Law client matters
- non-project reference material

Until a separate subsidiary policy is adopted, HillSide personal projects are
governed directly by the repo-level project policy.

## 4. Adoption of Repo-Level Project Rules

HillSide business projects adopt the canonical repository-level project rules
defined in
`01_DOCTRINE/03_POLICIES/POL-055_Repository_Project_Policy.md`, including:

- delivery stages: `Initiating`, `Planning`, `Executing`, `Closing`
- separation of delivery stages from register-level decision lifecycles
- ML1-only stage-gate advancement authority
- baseline stage artifact requirements
- project identity and project-type rules
- planning-discipline rules

Project ontology and work-container boundaries remain governed by:

- `01_DOCTRINE/01_INVARIANTS/INV-0012-project-structural-boundaries.md`
- `01_DOCTRINE/01_INVARIANTS/INV-0018-canonical-project-types.md`

## 5. Project Identity — HillSide Business Application

HillSide business projects apply the repo-level Project Identity Rule as
follows:

- All HillSide business projects use the `HBP-NNN` format.
- The number is unique across `04_INITIATIVES/HillSide_PORTFOLIO/BUSINESS_PROJECTS/`.
- The folder name equals the Project ID.
- New HillSide business projects must continue using the `HBP-NNN` series
  rather than inventing a parallel local numbering scheme.

## 6. HillSide Business Application Rules

For HillSide business projects specifically:

- project governance under this policy applies to business-project packets and
  supporting project-management structures under
  `04_INITIATIVES/HillSide_PORTFOLIO/BUSINESS_PROJECTS/`
- HillSide business projects may use `Decision` projects for bounded
  ownership-level evaluation work where the main objective is an ML1
  go / hold / no-go or reclassification decision
- `README.md` may coexist with the governed packet, but it is never itself a
  stage-gate artifact
- working-capture files such as idea backlogs may coexist with the packet, but
  they do not replace required artifacts

## 7. Early Initiating Shell Rule

A HillSide business project may exist as a folder shell with only:

- `README.md`
- a project-register entry

This is acceptable during early pre-packet structuring before the full
initiation packet exists.

Once a project packet is started or a project is described as `Initiating`, the
required initiation artifact set must be represented explicitly. Missing items
should be shown as pending, not implied complete.

## 8. Consistency Rule

HillSide READMEs, project summaries, and approval records must remain
consistent with repo-level doctrine and this subsidiary policy.

If a HillSide README lists artifact requirements, it should point to doctrine
rather than restating a conflicting local variant.

If a HillSide project artifact conflicts with this policy, this policy governs,
subject always to the repo-level project policy.

## 9. Related Artifacts

- `01_DOCTRINE/03_POLICIES/POL-055_Repository_Project_Policy.md`
- `01_DOCTRINE/03_POLICIES/POL-065_Matthew_Holdings_Initiative_Risk_Policy.md`
- `04_INITIATIVES/HillSide_PORTFOLIO/BUSINESS_PROJECTS/PROJECT_REGISTER.md`
- `04_INITIATIVES/HillSide_PORTFOLIO/BUSINESS_PROJECTS/STAGE_REFERENCE.md`
