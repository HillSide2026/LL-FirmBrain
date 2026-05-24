---
id: POL-037
title: External System Integration Policy
owner: ML2
status: approved
approved_by: ML1
approved_date: 2026-04-18
version: 0.2
effective_date: 2026-04-18
supersedes:
provenance:
  decided_by: ML1
  decided_on: 2026-04-18
  context: Metadata normalized by system admin cleanup on 2026-05-24
created_date: 2026-03-09
last_updated: 2026-03-21
tags: [policy, integrations, external-systems, mcp, governance]
---

# POL-037 — External System Integration Policy

Status: Draft for ML1 Approval  
Authority Flow: ML1 -> ML2 -> System -> LL  
Maintained by: ML2

## 1. Purpose

Policy Statement: External system integrations must be governed, auditable, permission-controlled, and executed only through System-mediated runtime controls.

This policy governs how ML2 integrates with external software systems, data platforms, and operational infrastructure so that the Second Brain can participate in operational workflows (for example: document generation, compliance checks, communications, and synchronization) without breaking authority boundaries.

## 2. Definition of External Systems

An external system is any platform or service outside ML2 canonical storage and outside model reasoning context.

Examples include:
- Document platforms
- CRM systems
- Billing platforms
- Compliance systems
- Email infrastructure
- Cloud storage services

External systems may expose read access, write access, and structured API operations, subject to governed permissions.

## 3. Architectural Role

External integrations exist in the System execution layer.

Once explicitly integrated, an external platform becomes a governed execution surface for the System through the Execution Bridge. It does not become a new authority source and does not displace ML2 as canon.

Canonical flow:
- ML1 approves policy and integrations
- ML2 records specifications and governance rules
- System executes runtime tool calls to external systems
- LL consumes approved outputs

Hard boundary:
- Agents/models never connect directly to external systems.
- All access is mediated by System-managed tools.

## 4. Integration Mechanism

External systems must be accessed through MCP-governed tools and host runtime validation.

Required sequence:
1. Agent/model requests tool use
2. Host runtime validates schema and permission
3. System executes integration action
4. Structured response is returned

Rule:
- Models cannot directly call APIs, filesystems, or networks.

## 5. Categories of External Integrations

### 5.1 Document Systems
Examples: Google Docs, Word, SharePoint, DMS tools  
Typical capabilities: retrieve, update drafts, generate, archive

### 5.2 Communication Systems
Examples: email, internal messaging, client communication platforms  
Typical capabilities: draft/send/update/track correspondence  
Rule: outbound communications must remain policy-controlled and auditable.

### 5.3 Operational Systems
Examples: CRM, billing, matter/case systems, workflow trackers  
Typical capabilities: retrieve records, update metadata, generate proposals, track engagements

### 5.4 Compliance and Regulatory Systems
Examples: AML/sanctions/regulatory services  
Typical capabilities: screening, verification, analysis, audit reporting  
Rule: enhanced permission and logging controls are mandatory.

## 6. Access Control Principles

### 6.1 Least Privilege
Tools receive only minimum necessary scope (read-only where possible, scoped write/API permissions where necessary).

### 6.2 Explicit Access Scope
Each integration must define:
- systems accessed
- allowed operations
- prohibited actions

### 6.3 System-Level Credential Control
Credentials are held by host runtime only.  
Models must never receive API keys, passwords, or system credentials.

## 7. Data Flow Governance

### 7.1 Controlled Data Transfer
Transfers must be structured, validated, and logged.  
Sensitive transfers require additional controls.

### 7.2 Traceable Operations
Every external operation must log:
- tool invoked
- input parameters
- execution timestamp
- system response
- resulting artifact/reference

### 7.3 Data Ownership
ML2 remains canonical for doctrine and governed knowledge artifacts.  
External systems may store operational/transactional artifacts; ML2 records references and metadata rather than full external-system replicas by default.

## 8. Integration Design Principles

### 8.1 API-First Design
Prefer defined APIs over direct/manual system manipulation.

### 8.2 Idempotent Operations
Where feasible, integrations should be repeatable without unintended duplicate effects.

### 8.3 Structured Responses
Integration outputs returned to models must be structured and machine-parseable.

## 9. Monitoring and Audit

Required controls:
- execution logging
- error tracking
- rate limiting
- anomaly detection

Auditability must allow ML1 review of what action occurred, which system executed it, and what data/access scope was involved.

## 10. Risk Management

Primary risks:
- unauthorized access
- incorrect data modification
- API misuse
- unintended automation actions

Minimum mitigations:
- permission scoping
- runtime validation
- logging and auditing
- ML1 approval gates

## 11. Integration Approval Process

No integration may be activated without ML1 authorization.

Required change package:
1. Integration proposal
2. Access scope definition
3. Tool interface specification
4. Permission model
5. Security review
6. ML1 approval
7. Registration in ML2 governance artifacts

## 12. Enforcement

The System runtime must enforce:
- tool permission validation
- access scope enforcement
- argument/schema validation
- execution logging
- error reporting

Violations must be blocked or escalated to ML1.

Authority (Principles referenced): PRN-020, PRN-022, PRN-024, PRN-026, PRN-028, PRN-029
Related policies: POL-024, POL-025, POL-035, POL-036
Enforcement expectation: Any direct model/worker external access, undeclared integration, scope violation, or missing integration audit trail is non-compliant and must be blocked or escalated.
Supersedes: None
Version: 0.1
Status: Draft
