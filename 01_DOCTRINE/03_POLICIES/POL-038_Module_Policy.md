---
id: POL-038
title: Module Policy
owner: ML2
status: approved
approved_by: ML1
approved_date: 2026-04-18
version: 0.1
effective_date: 2026-04-18
supersedes:
provenance:
  decided_by: ML1
  decided_on: 2026-04-18
  context: Metadata normalized by system admin cleanup on 2026-05-24
created_date: 2026-03-09
last_updated: 2026-03-09
tags: [policy, modules, architecture, solutions, playbooks]
---

# POL-038 — Module Policy

Status: Draft for ML1 Approval  
Authority Flow: ML1 -> ML2 -> System -> LL  
Maintained by: ML2

## 1. Purpose

Policy Statement: Modules are canonical structural components within approved solutions and must be used to organize reusable operational artifacts.

This policy defines the Module as a canonical structural element in system architecture. Its purpose is to ensure consistent organization of operational artifacts and prevent semantic drift in how reusable solution components are defined and maintained.

Modules exist to organize reusable operational components of a solution.

## 2. Definition

A Module is a bounded, reusable component of an approved solution that groups operational artifacts required to perform a defined function.

A module typically contains:
- workflows
- templates
- checklists
- supporting guides or reference material

Modules represent functional components of a solution, not individual documents or isolated activities.

## 3. Architectural Position

Modules exist within this hierarchy:

Practice Area  
-> Solution  
-> Module  
-> Workflows  
-> Templates  
-> Checklists

Example:

```text
FINANCIAL_SERVICES/
  SOLUTIONS/
    AML_COMPLIANCE/
      MODULES/
        CLIENT_ONBOARDING/
        ENHANCED_DUE_DILIGENCE/
        REGULATORY_REPORTING/
```

Modules define the organizational boundary for operational artifacts inside a solution.

## 4. What a Module Is

A module is:
- a reusable functional component within a solution
- a container for multiple operational artifacts
- a unit supporting repeatable delivery
- a stable concept that may support multiple workflows

Modules may represent:
- a category of legal work
- a functional capability within a solution
- a repeatable procedural domain

## 5. What a Module Is Not

A module is not:
- a practice area
- a full solution
- a single workflow
- a single template
- a document collection
- a miscellaneous folder for unrelated artifacts

Modules must represent a clearly bounded operational function.

## 6. Creation Criteria

A module should be created only when the component:
- is repeatable across engagements
- has a clear functional boundary
- requires multiple operational artifacts
- is likely to persist over time
- represents a distinct capability within a solution

If these criteria are not met, artifacts should remain within an existing module.

## 7. Required Structure

Each module should contain the following directories where applicable:

```text
MODULE_NAME/
  WORKFLOWS/
  TEMPLATES/
  CHECKLISTS/
```

Optional directories may include:
- `GUIDES/`
- `REFERENCE/`

Artifacts in modules must follow system naming and schema conventions.

## 8. Naming Rules

Module names must:
- use `UPPERCASE_SNAKE_CASE`
- represent a clear functional concept
- avoid vague labels such as `GENERAL`, `MISC`, or `OTHER`
- remain stable over time

Examples:
- `CLIENT_ONBOARDING`
- `ENHANCED_DUE_DILIGENCE`
- `REGULATORY_REPORTING`
- `TRANSACTION_MONITORING_REVIEW`

## 9. Relationship to Workflows

Modules may contain multiple workflows.

Workflows define procedural execution for work represented by the module.

Example:

```text
ENHANCED_DUE_DILIGENCE/
  WORKFLOWS/
    edd_initial_review.md
    edd_source_of_funds_analysis.md
```

The module represents the functional domain; workflows represent procedural execution.

## 10. Governance

Modules exist only within approved solutions.

Creation or modification of modules must follow system governance to ensure:
- architectural consistency
- controlled system expansion
- prevention of structural drift

Modules should remain stable structural units within system architecture.

## 11. Summary

A Module is the smallest governed solution component used to organize reusable operational artifacts.

Modules:
- exist within solutions
- group related workflows, templates, and checklists
- represent bounded functional components
- support repeatable delivery of work

Authority (Principles referenced): PRN-009, PRN-016, PRN-018, PRN-020, PRN-021  
Related policies: POL-010, POL-011, POL-015  
Enforcement expectation: Any solution structure that bypasses module boundaries or uses non-canonical module naming is non-compliant and must be corrected or escalated.  
Supersedes: None  
Version: 0.1  
Status: Draft
