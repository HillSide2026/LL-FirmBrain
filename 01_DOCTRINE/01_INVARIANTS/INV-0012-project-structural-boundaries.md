---
id: INV-0012
title: 'INV-0012: Governed Work Structural Boundaries'
owner: ML1
status: approved
approved_by: ML1
approved_date: 2026-05-19
version: '2.0'
effective_date: 2026-05-19
supersedes:
provenance:
  decided_by: ML1
  decided_on: 2026-05-19
  context: Metadata normalized by system admin cleanup on 2026-05-24
created_date: 2026-03-15
last_updated: 2026-05-19
tags: [doctrine, invariants, projects, structure, governance]
---

# INV-0012 — Governed Work Structural Boundaries

## Purpose

Define the structural ontology for governed work so the repository does not
blur portfolios, programs, projects, milestones, tasks, matters, solutions,
modules, or workflows.

This invariant defines what these units are, how they relate, and what they are
not.

Artifact requirements, stage-gate packets, lifecycle controls, and behavioral
rules remain at the policy layer.

## Structural Rule

The repository recognizes the following distinct structural units:

- portfolio
- program
- project
- milestone
- task
- matter
- solution
- module
- workflow

These are not interchangeable labels.

No artifact, folder, register, dashboard, or policy may silently collapse one
unit into another.

## Canonical Definitions

### 1. Portfolio

A portfolio is the highest governed grouping of related work organized by
primary beneficiary, operating domain, or ownership branch.

The current repository has three canonical portfolios under `04_INITIATIVES`:

- `SYSTEM_PORTFOLIO`
- `LL_PORTFOLIO`
- `HillSide_PORTFOLIO`

A portfolio:

- groups one or more programs and related governance structures
- sets broad scope and boundary for included work
- is not itself a program, project, milestone, or task

### 2. Program

A program is a governed grouping of related projects or ongoing governance lines
within a portfolio that share a common operating aim, domain, or coordination
need.

A program:

- contains one or more projects
- coordinates related projects
- may hold a shared register, policy overlay, or decision frame
- may define program-level milestones
- is not itself a single project deliverable
- is not a matter, solution, module, or workflow

### 3. Project

A project is a bounded change initiative governed by the project delivery-stage
system.

A project:

- has a defined purpose, scope boundary, and owner
- uses exactly one canonical project type defined in
  `01_DOCTRINE/01_INVARIANTS/INV-0018-canonical-project-types.md`
- advances, when authorized, through project delivery stages
- may consume solutions, modules, workflows, and templates
- may affect a portfolio or program
- may define milestones and tasks

A project is not:

- a portfolio
- a program
- a milestone
- a task
- a solution architecture unit
- a workflow definition
- a doctrine artifact

### 4. Milestone

A milestone is a governed checkpoint or completion condition inside a program or
project.

A milestone:

- marks meaningful readiness, completion, approval, or sequencing status
- exists only within a broader governed container
- may be evidenced by one or more artifacts or tasks
- may inform gate readiness, but does not itself advance a project stage
- is not a project, task, dependency, or register row substitute

### 5. Task

A task is the smallest actionable execution unit tracked for work completion.

A task:

- expresses a concrete action to be performed
- may support a project, milestone, matter, or workflow
- may carry assignee, status, due date, and context
- does not define portfolio, program, or project identity
- does not itself create stage advancement, project closure, or policy status

A task is not:

- a portfolio
- a program
- a project
- a milestone
- a dependency

### 6. Matter

A matter is a client-specific legal work unit governed by matter doctrine, not
project doctrine.

A matter:

- is tied to a client engagement
- follows matter lifecycle and matter-stage rules
- may use solutions, modules, workflows, and tasks in delivery
- may depend on projects that improve firm capability

Whether a matter is a type of project is not resolved by current doctrine and
remains an open question.

Current rule:

- matter governance is separate from project governance
- the matter/project relationship must not be inferred beyond what doctrine
  explicitly states

### 7. Solution

A solution is the canonical offering boundary for reusable operational design
and delivery.

A solution:

- defines what offering or outcome is being delivered
- is decomposed into modules
- may be used across multiple matters or operating contexts

A solution is not a project, milestone, task, matter, or workflow.

### 8. Module

A module is a bounded reusable functional component within a solution.

A module:

- groups operational artifacts required for a defined function
- may contain workflows, templates, checklists, and supporting references
- remains subordinate to its parent solution

A module is not a project, milestone, task, matter, or full solution.

### 9. Workflow

A workflow is the canonical procedural execution unit.

A workflow:

- defines how work is performed
- operates within a bounded solution/module or other approved operational scope
- consumes governed inputs and produces governed outputs
- may generate or sequence tasks

A workflow is not a project, milestone, matter, solution, or doctrine artifact.

## Structural Relationships

The canonical relationships are:

```text
Portfolio
-> Program
-> Project
-> Milestone

Project or Matter
-> Task

Practice Area
-> Solution
-> Module
-> Workflow
```

Cross-system relationship rules:

- Portfolios contain programs.
- Programs contain projects.
- Programs and projects may define milestones.
- Projects, matters, and workflows may use tasks.
- Projects may create, change, govern, or improve solutions, modules, and workflows.
- Workflows may execute work that supports a project or a matter.
- Matters may consume solutions, modules, workflows, and tasks.

Containment must not be inferred where doctrine does not define it.

## Non-Equivalence Rules

The following terms are structurally distinct and must not be collapsed:

- program and project
- project and milestone
- milestone and task
- task and dependency
- project stage and milestone
- decision lifecycle status and decision project

## Stage-System Separation

Project delivery stages are a distinct system from:

- roadmap `STAGE<n>[.<phase>]` numbering
- register decision lifecycles such as `idea`, `screening`, or `approved`
- milestones
- tasks
- matter delivery-status states

These systems must not be collapsed into one vocabulary.

## Identity Rule

Project identity, project type, project stage, and storage location are related
but distinct concepts.

- `Project ID` is canonical identity.
- the applicable project policy determines the required relation between folder
  name and `Project ID`.
- project path is a location key, not a substitute for project type or stage.
- folder placement does not by itself determine project authority, stage, or
  artifact completeness.

## Boundary Rule

If classification is ambiguous, the system must escalate rather than guess.

No artifact may:

- treat a milestone or task list as if it were a project
- classify a workflow, module, or solution as a project
- treat a portfolio or program as if it were a single project
- infer the matter/project relationship beyond explicit doctrine

## Related Doctrine

- `01_DOCTRINE/01_INVARIANTS/INV-0018-canonical-project-types.md`
- `01_DOCTRINE/03_POLICIES/POL-055_Repository_Project_Policy.md`
- `01_DOCTRINE/03_POLICIES/POL-052_Client_Engagement_Stage_Policy.md`
- `01_DOCTRINE/03_POLICIES/POL-038_Module_Policy.md`
- `01_DOCTRINE/03_POLICIES/POL-039_Solution_Policy.md`
- `01_DOCTRINE/03_POLICIES/POL-040_Workflow_Policy.md`
- `01_DOCTRINE/01_INVARIANTS/INV-0013-risk-model.md`
