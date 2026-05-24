---
id: POL-045
title: Asana Integration Safeguard Policy
owner: ML1
status: approved
approval: ML1
approved_by: ML1
approved_date: 2026-04-18
project: LLP-006
version: 0.1
effective_date: 2026-04-18
supersedes:
provenance:
  decided_by: ML1
  decided_on: 2026-04-18
  context: Metadata normalized by system admin cleanup on 2026-05-24
created_date: 2026-03-10
last_updated: 2026-03-10
tags: [policy, asana, integrations, safeguards, change-control, fulfillment]
---

# POL-045 — Asana Integration Safeguard Policy

Policy Statement: Asana is an operational execution surface, not a governing authority. Default system posture is read-only. Any write activity must be stage-gated, explicitly approved, scoped, and auditable.

Authority (Principles referenced): PRN-003, PRN-004, PRN-020, PRN-022, PRN-026, PRN-028  
Enforcement expectation: Any Asana action outside approved scope, missing approval evidence, or lacking run-level audit data is non-compliant and must be blocked or escalated.  
Supersedes: None

---

## 1. Purpose

This policy establishes safeguards for system interaction with Asana so that:
- operational tracking can occur safely
- authority boundaries are preserved
- write risk is controlled
- all changes are attributable and reviewable

---

## 2. Scope

This policy applies to all system-mediated access to Asana workspaces, projects, sections, tasks, comments, and custom-field updates used by LL workflows, including LLP-006 reconciliation workflows.

This policy applies to:
- agent and script execution
- API-based automation
- batch update routines

This policy does not grant authority to bypass existing doctrine for matters, fulfillment stages, or approval gates.

---

## 3. Architectural Boundary

Asana is a tracking and coordination surface only.

Hard rules:
- ML2 remains the system of record for doctrine and governed artifacts.
- Canonical matter identity remains the Clio `matter_id` governed by POL-043.
- Asana metadata must not redefine matter identity, delivery status, or doctrine.

---

## 4. Stage Model

| Stage | Status | Rule |
|------|--------|------|
| Stage 1 | Active default | Read-only access only |
| Stage 2 | ML1-activated | Controlled writes allowed to approved projects/fields only |

Stage transition to Stage 2 requires explicit ML1 approval and a recorded activation artifact.

---

## 5. Stage 1 (Read-Only Baseline)

Permitted:
- read workspaces/projects/tasks
- read task state and assignment metadata
- generate reconciliation and health reports

Prohibited:
- create/update/delete tasks
- move tasks between sections
- write comments
- modify custom fields or project configuration

---

## 6. Stage 2 (Controlled Writes)

When Stage 2 is activated, writes are limited to approved operational scope:
- create task records linked to approved workflow execution
- update bounded task metadata (assignee, due date, approved custom fields)
- move tasks across approved sections according to governed workflow state
- add operational comments that preserve provenance

Mandatory controls:
- target project allowlist
- field allowlist
- write reason tied to run context
- approval reference attached to each write batch

---

## 7. Prohibited Actions (All Stages Unless One-Time ML1 Exception)

The system must not autonomously:
- delete tasks, sections, or projects
- modify workspace membership, permission models, or admin settings
- alter integration credentials, webhooks, or authentication configuration
- bulk-close or bulk-reassign tasks without explicit batch approval
- post doctrine text as authoritative policy inside Asana

Any required prohibited action must be executed only with explicit, one-time ML1 authorization.

---

## 8. Approval and Audit Requirements

Any Stage 2 write execution must record:
- run identifier
- actor/agent
- workspace/project identifier
- action type
- target object identifier (task/section/project)
- before/after values for changed fields
- timestamp
- approval artifact reference

Audit records must be persisted in governed run artifacts under `06_RUNS`.

Token safety rule:
- Asana tokens must never be written into logs, doctrine files, or user-facing artifacts.

---

## 9. Escalation Rules

The system must escalate (not infer expanded authority) when:
- requested action is outside configured write scope
- required field mapping is ambiguous
- matter linkage conflicts with canonical `matter_id`
- approval record is missing or stale

---

## 10. Related Doctrine

- `01_DOCTRINE/03_POLICIES/POL-024_Integration_Adapter_Gatekeeping.md`
- `01_DOCTRINE/03_POLICIES/POL-025_No_Direct_External_Access_by_Workers.md`
- `01_DOCTRINE/03_POLICIES/POL-027_Run_Record_Requirement.md`
- `01_DOCTRINE/03_POLICIES/POL-028_Auditable_Tool_Use.md`
- `01_DOCTRINE/03_POLICIES/POL-035_Model_Context_Protocol_Governance.md`
- `01_DOCTRINE/03_POLICIES/POL-037_External_System_Integration_Policy.md`
- `01_DOCTRINE/03_POLICIES/POL-043_Clio_Matter_ID_Structure_and_Client_of_Record_Identity.md`

---

## 11. Summary

Asana may be used for governed operations, but with strict safeguards:
- Stage 1: read-only by default
- Stage 2: controlled writes with explicit approval, scope limits, and full auditability
- destructive or boundary-breaking actions require explicit one-time ML1 authorization
