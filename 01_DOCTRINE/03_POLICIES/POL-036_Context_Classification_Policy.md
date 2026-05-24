---
id: POL-036
title: Context Classification Policy
owner: ML1
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
tags: [policy, context, classification, mcp, security, retrieval]
---

# POL-036 — Context Classification Policy

## 1. Purpose

Policy Statement: All context exposed to models through MCP must be explicitly classified before retrieval.

Objectives:
- Protect confidential information
- Prevent data leakage
- Enforce predictable retrieval
- Control model grounding

Hard rule:
- Unclassified data may not be accessed by models.

## 2. Core Principle

Context must be:
- Structured
- Addressable
- Permissioned

Rules:
- Context must never be blindly injected into prompts.
- Retrieval must occur through MCP resource requests.

## 3. Context Classification Levels

ML2 defines five classification levels:

| Level | Name | Description |
| --- | --- | --- |
| L0 | Public | Public information |
| L1 | Internal | Internal operational information |
| L2 | Confidential | Sensitive internal data |
| L3 | Restricted | Client-sensitive or legal-sensitive data |
| L4 | Critical | Privileged or highly sensitive material |

## 4. Classification Rules

### L0 — Public
Examples:
- Published articles
- Marketing materials
- Publicly available laws
- Public datasets

Access:
- Unrestricted retrieval
- May be used freely by models

### L1 — Internal
Examples:
- Internal procedures
- Templates
- Workflows
- Operational playbooks

Access:
- Model retrieval allowed for governed workflows
- Outputs must be logged

### L2 — Confidential
Examples:
- Internal strategy documents
- Financial projections
- Proprietary methodologies

Access:
- Retrieval allowed only for approved workflows
- Must not be exposed externally without explicit authorization

### L3 — Restricted
Examples:
- Client files
- Legal work product
- Confidential communications

Access:
- Retrieval requires explicit task context
- Outputs must undergo review before use

### L4 — Critical
Examples:
- Attorney-client privileged material
- Client-provided documents
- Client deliverables (draft or final; delivered or undelivered)
- Legal strategy
- Security credentials
- Internal security architecture

Access:
- Prohibited by default
- Only ML1 may authorize retrieval

## 5. Resource Metadata Requirements

All resources must include metadata:
- `resource_id`
- `classification_level`
- `owner`
- `source_system`
- `version`
- `last_modified`
- `access_policy`

Rule:
- Resources without required metadata are not eligible for MCP retrieval.

## 6. Context Retrieval Controls

The MCP host must enforce:

### Context Scope
- Models may retrieve only the minimum context required for the task.

### Context Size Limits
- Maximum tokens retrieved per resource
- Maximum number of resources per request

### Context Provenance
Every retrieval must record:
- `resource_id`
- `retrieval_timestamp`
- `classification_level`
- `retrieval_reason`
- `requesting_model`

## 7. Prompt Injection Protection

Context retrieved from external sources must be treated as untrusted input.

Required controls:
- Instruction filtering
- Prompt boundary markers
- Tool-use restriction

Hard rule:
- External documents may not define tool instructions.

## 8. Output Restrictions

Models may not produce outputs containing:
- L3 or L4 data unless authorized
- Raw confidential records
- Security credentials

Sensitive outputs must pass through:
- Human review, or
- Automated redaction with logged controls

## 9. Context Lifecycle

Classification must be reviewed:
- At creation
- After modification
- During periodic system audits

Rule:
- Archived data retains its classification unless explicitly reclassified under approved governance.

## 10. Violations

The following events must trigger system alerts:
- Model access to unauthorized classification level
- Resource retrieval attempt without required metadata
- External context bypassing MCP

Rule:
- Violations must be logged, escalated, and reviewed.

Authority (Principles referenced): PRN-020, PRN-024, PRN-026, PRN-028, PRN-029
Enforcement expectation: Any context retrieval or output flow that bypasses classification, metadata, or permission controls is non-compliant and must be blocked or escalated to ML1.
Supersedes: None
Version: 0.1
Status: Draft
