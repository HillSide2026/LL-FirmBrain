---
id: POL-056
title: Firm Project Policy
owner: ML1
status: approved
approved_by: ML1
approved_date: 2026-05-19
version: '1.2'
effective_date: 2026-05-19
supersedes:
provenance:
  decided_by: ML1
  decided_on: 2026-05-19
  context: Metadata normalized by system admin cleanup on 2026-05-24
created_date: 2026-03-14
last_updated: 2026-05-19
tags: [doctrine, policy, projects, ll, stage-gates]
---

# Firm Project Policy

## 1. Purpose

This policy is the Levine Law subsidiary project policy.

Canonical repository-level project stages, artifact requirements, and type
rules are defined in:

- `01_DOCTRINE/03_POLICIES/POL-055_Repository_Project_Policy.md`

Doctrine-side PM controls are defined in:

- `01_DOCTRINE/03_POLICIES/POL-073_Project_Management_Control_Policy.md`

This policy applies those rules to Levine Law project governance.

## 2. Policy Hierarchy

`POL-055` is the repository-level project policy for the repo.

`POL-073` is the doctrine-side project-management control policy that governs
PM identity, sequencing, conformance, and migration rules.

This policy is explicitly subordinate to both.

This policy may add Levine Law-specific application rules, but it may not
replace the canonical delivery stages, ML1 stage-gate authority, Project ID
rules, project-type rules, or PM conformance rules defined at the higher layer.

## 3. Scope

This policy applies directly to Levine Law:

- strategic projects
- management projects
- operational projects
- decision projects

This policy does not apply to:

- HillSide project packets
- legal matter stages
- matter delivery-state doctrine

LL client matters remain governed by matter doctrine, not project doctrine.

## 4. Adoption of Repo-Level Project Rules

Levine Law projects adopt the canonical repository-level project rules defined
in `POL-055`, including:

- delivery stages: `Initiating`, `Planning`, `Executing`, `Closing`
- separation of delivery stages from register-level decision lifecycles
- ML1-only stage-gate advancement authority
- baseline stage artifact requirements
- canonical project identity and project-type rules
- planning-discipline rules

Levine Law PM automation and PM control surfaces adopt the doctrine-side PM
controls defined in `POL-073`, including:

- `Project ID == folder name`
- migration away from `LLP-NNN_NAME` folders
- retirement of `WORKPLAN.md`
- retirement of the split metric schema
- retirement of `ML1_METRIC_APPROVAL.md`
- matter-aware sequencing and WIP controls
- explicit PM conformance failure rules

## 5. Project Identity — Levine Law Application

Levine Law applies the repo-level Project Identity Rule as follows:

- LL project folders use the `LLP-NNN` series unless ML1 has approved a stable
  slug ID for a control or program-level project.
- The folder name equals the Project ID.
- The Project ID is unique across the entire
  `04_INITIATIVES/LL_PORTFOLIO/` tree.
- The deprecated `LLP-26-XX` year-prefixed format must not be used.
- New LL projects must not be created as `LLP-NNN_NAME`.

### 5a. Legacy LL Folder Migration

Existing `LLP-NNN_NAME` folders are legacy migration residue.

Rules:

- They are readable during transition, but they are non-canonical.
- They must be normalized to plain `LLP-NNN` before their next material
  structural edit or before their next stage gate is closed, whichever comes
  first.
- Until normalized, PM conformance outputs should flag them explicitly.

## 6. Levine Law Project Type Application

Levine Law recognizes four governed project types:

- `Strategic`
- `Management`
- `Operational`
- `Decision`

Rules:

- `Decision` projects are valid LL projects and may be used where the main
  objective is an ML1 go / hold / no-go or reclassification decision.
- Decision projects remain governed projects under the same canonical delivery
  stages.
- Client matters are not LL projects and do not become `Decision` projects by
  virtue of needing a matter-level judgment.

## 7. Levine Law Application Rules

For Levine Law specifically:

- project governance under this policy applies to project packets and PM
  structures under `04_INITIATIVES/LL_PORTFOLIO/`
- LL templates, backlog surfaces, READMEs, and agent specifications must conform
  first to `POL-055`, then to `POL-073`, then to this policy
- `LL_PROJECT_BACKLOG.md` may hold pre-Initiating LL projects of any of the
  four canonical project types
- local templates or READMEs outside doctrine may explain or scaffold LL use,
  but they are not canonical doctrine

## 8. Matter-to-Project Sequencing Rule

Levine Law project sequencing must respect matter pressure.

Rules:

- active `essential` and `strategic` matters outrank discretionary internal
  project acceleration unless ML1 decides otherwise
- LL projects that directly unblock active matter delivery may be prioritized
  ahead of other internal projects
- in the absence of an explicit matter-support linkage, assume matter delivery
  takes priority over discretionary project expansion

Matter-priority vocabulary remains governed by matter doctrine, especially
`POL-071`.

## 9. Drift Control

If a Levine Law template, agent specification, runner, README, or summary
conflicts with `POL-055` or `POL-073`, the higher-order doctrine governs.

If a Levine Law-specific project artifact conflicts with this policy, this
policy governs, subject always to `POL-055` and `POL-073`.

## 10. Related Artifacts

- `01_DOCTRINE/03_POLICIES/POL-055_Repository_Project_Policy.md`
- `01_DOCTRINE/03_POLICIES/POL-070_Backlog_Routing_Policy.md`
- `01_DOCTRINE/03_POLICIES/POL-071_Matter_Delivery_Stage_Policy.md`
- `01_DOCTRINE/03_POLICIES/POL-073_Project_Management_Control_Policy.md`
- `01_DOCTRINE/03_POLICIES/POL-063_Project_Risk_Artifact_Lifecycle_Policy.md`
- `04_INITIATIVES/LL_PORTFOLIO/03_FIRM_OPERATIONS/LLP-043/PROJECT_ARTIFACT_TEMPLATE.md`
- `00_SYSTEM/AGENTS/LLM-004_LLP-043_AGENT.md`
- `00_SYSTEM/AGENTS/LLM-005_LLP-042_AGENT.md`
- `00_SYSTEM/AGENTS/LLM-006_PORTFOLIO_GOVERNANCE_AGENT.md`
