---
id: POL-039
title: Solution Policy
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
tags: [policy, solutions, architecture, playbooks]
---

# POL-039 — Solution Policy

Status: Draft for ML1 Approval  
Authority Flow: ML1 -> ML2 -> System -> LL  
Maintained by: ML2

## 1. Purpose

Policy Statement: A Solution is the canonical offering boundary for governed operational design and execution.

This policy defines the Solution as a governed architectural unit so the system can consistently represent what offering is being delivered and prevent drift in how offerings are structured.

## 2. Definition

A Solution is a productized offering that defines the business/legal outcome scope.

A solution:
- is approved under doctrine
- is decomposed into one or more modules
- contains reusable operational assets through those modules

## 3. Architectural Position

Canonical hierarchy:

Practice Area  
-> Solution  
-> Module  
-> Workflow

Example:

```text
FINANCIAL_SERVICES/
  SOLUTIONS/
    AML_COMPLIANCE/
      MODULES/
        CLIENT_ONBOARDING/
        ENHANCED_DUE_DILIGENCE/
```

## 4. Required Structure (Stub)

Each solution must include:

```text
SOLUTION_NAME/
  MODULES/
```

Additional required artifacts and schemas are TBD.

## 5. Naming Rules (Stub)

Solution names must:
- use `UPPERCASE_SNAKE_CASE`
- represent a clear offering concept
- avoid ambiguous labels

Detailed naming constraints are TBD.

## 6. Governance (Stub)

Solutions exist only within approved practice-area architecture.

Creation, modification, split, or retirement of solutions must follow governed change control with ML1 approval boundaries.

Detailed lifecycle and approval mechanics are TBD.

## 7. Summary

Solution is the canonical unit answering: what offering is being delivered.

Authority (Principles referenced): PRN-009, PRN-018, PRN-020, PRN-021  
Related policies: POL-015, POL-018, POL-038  
Enforcement expectation: Offerings executed without an approved solution boundary are non-compliant and must be corrected or escalated.  
Supersedes: None  
Version: 0.1  
Status: Draft
