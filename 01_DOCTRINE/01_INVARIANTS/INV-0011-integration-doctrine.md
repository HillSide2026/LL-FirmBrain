---
id: INV-0011
title: 'INV-0011: Integration Doctrine (External Platform Governance)'
owner: ML1
status: approved
approved_by: ML1
approved_date: 2026-03-28
version: 1.0
created_date: 2026-02-27
last_updated: 2026-03-28
tags: [integration, governance, execution]

effective_date: 2026-03-28
supersedes:

provenance:
  decided_by: ML1
  decided_on: 2026-03-28
  context: Approved doctrine governing external platform integrations
---

# INV-0011 — Integration Doctrine

**Invariant ID:** INV-0011  
**Status:** APPROVED  
**Authority:** ML1

---

## 1. Purpose

To govern how ML2 interacts with Office 365 and Google Workspace.  
To ensure integrations increase leverage without compromising authority integrity.

---

## 2. Classification of External Platforms

### 2.1 Tier-2 Execution Surfaces

Office 365 and Google Workspace are classified as:
- Tier-2 Execution Surfaces

They are:
- Collaborative environments
- Distribution layers
- Communication tools

They are not:
- Canonical repositories
- Doctrine authorities
- Approval systems

### 2.2 Tier-1 External Systems (Integration Points)

The following systems are classified as Tier-1 External Integration Points:

| System | Purpose | Authority Level | Read Permissions | Write Permissions |
|--------|---------|-----------------|------------------|-------------------|
| **Gmail** | Email inbox, threading, message retrieval | Tier-1 | Permitted for inbox governance, triage, and message context | Drafts only; no autonomous send |
| **SharePoint** | Matter folder federation, document storage, matter file envelopes | Tier-1 | Permitted for matter file discovery, metadata enumeration, federated folder verification | Write only to designated staging areas and version-controlled artifact placement |
| **Clio** | Practice management, matter metadata, matter_id authority | Tier-1 | Permitted for matter identity verification, matter status retrieval, client-of-record lookup | Write only for matter lifecycle signals (status updates, closed/archived flagging) via gated protocols |
| **Asana** | Task management, project workflow coordination, external task tracking | Tier-1 | Permitted for task status, project progress monitoring, deadline tracking | Write only to designated project/task boards with audit logging |
| **Canva** | Brand asset templates, design templates, marketing collateral | Tier-1 | Permitted for template catalog enumeration, version tracking | Write only to designated template repositories with brand compliance verification |

### 2.3 Integration Tiers Defined

**Tier-1 External Systems:** Systems with formal MCP servers and explicit integration control policies. Integrations are governed; authority flow is ML2 → System → External Platform.

**Tier-2 Execution Surfaces:** Systems for collaborative work and distribution. These are not authoritative but may receive published copies of canonical artifacts.

---

## 3. Allowed Integration Actions by System

### 3.1 Office 365 & Google Workspace (Tier-2)

#### Read Permissions

Permitted when:
- Required for QC review
- Required for template population
- Required for drift detection
- Explicitly authorized in integration control policy

#### Write Permissions

Permitted only for:
- Publishing derived artifacts
- Updating approved distributed templates
- Writing structured outputs tied to ML2 version references

All writes must:
- Include version metadata
- Log artifact ID
- Log timestamp
- Log triggering agent

---

### 3.2 Gmail (Tier-1)

#### Read Permissions

Permitted for:
- Inbox triage and message retrieval
- Matter context hydration (message thread retrieval)
- Client communication thread assembly
- Email metadata extraction (sender, recipient, date, subject)

#### Write Permissions

**Prohibited:** Autonomous email send, scheduled send, reply composition, forwarding.

**Permitted:** 
- Draft composition (stored locally, requires ML1 review before send)
- Label application (if governed by inbox governance protocol)
- Email classification signals (extracting context without state mutation)

---

### 3.3 SharePoint (Tier-1)

#### Read Permissions

Permitted for:
- Matter folder structure enumeration
- Matter file metadata retrieval (folder names, item counts, modification dates)
- Federated matter file surface verification
- Document inventory and version tracking

#### Write Permissions

Permitted only for:
- Publishing versioned matter summary artifacts to designated matter folders
- Updating matter-level status overlays (when governed by PRO-020, PRO-021, PRO-022)
- Writing structured metadata files tied to canonical matter records

All writes must:
- Reference canonical matter_id
- Include version metadata and ML2 provenance
- Comply with matter file staging protocol (PRO-020, PRO-021, PRO-022)

---

### 3.4 Clio (Tier-1)

#### Read Permissions

Permitted for:
- Matter identity lookup (matter_id to Clio matter number mapping)
- Client-of-record and matter status retrieval
- Matter metadata synchronization for canonical verification

#### Write Permissions

Permitted only for:
- Matter lifecycle signals (archived/closed status updates when governed by policy)
- Hourly or billing code updates (when explicitly authorized by execution protocol)

All writes must:
- Be gated by explicit protocol (e.g., PRO-016 for fulfillment handoff)
- Include audit timestamp and triggering agent
- Reference the ML2 run that triggered the change

---

### 3.5 Asana (Tier-1)

#### Read Permissions

Permitted for:
- Task status retrieval and deadline tracking
- Project-level progress monitoring
- Task assignment and ownership verification

#### Write Permissions

Permitted only for:
- Task status updates (when governed by project workflow protocol)
- Task creation for project-linked work items (requires explicit gating)
- Subtask or checklist updates (when within allocated project scope)

All writes must:
- Include reference to authoritative project or work artifact in ML2
- Log timestamp, agent, and change summary
- Never autonomously resolve or close project tasks without explicit gate

---

### 3.6 Canva (Tier-1)

#### Read Permissions

Permitted for:
- Template catalog enumeration
- Template version tracking
- Brand asset and color palette verification

#### Write Permissions

**Prohibited:** Direct template mutation in Canva by agents.

**Permitted:**
- Template version registration and metadata logging
- Brand compliance overlay artifacts (stored locally or in designated staging areas)
- Template retirement and deprecation signaling

All template changes are staged locally, verified against brand policy (POL-047, POL-050), and promoted to Canva only via explicit ML1 approval.

---

## 4. Prohibited Behaviors

- Overwriting canonical ML2 artifacts
- Treating a shared Google Doc as authoritative
- Auto-promoting edited documents to canonical status
- Allowing undocumented edits to alter doctrine

---

## 5. Promotion Requirement

External edits become candidates only. They require:
- Candidate flag
- Diff vs canonical
- ML1 approval
- Version increment
- Republish

No bypass permitted.

---

## 6. Integration Logging

Every integration event must log:
- Source platform
- Target artifact
- Artifact version
- Change summary
- Initiating agent or human
- Approval reference (if applicable)

Logs must be auditable.

---

## 7. Related Policies and Protocols

This invariant is complemented by integration-specific policies and protocols:

| Artifact | Purpose |
|----------|---------|
| POL-024 | Integration Adapter Gatekeeping |
| POL-035 | Model Context Protocol Governance |
| POL-037 | External System Integration Policy |
| POL-043 | Clio Matter ID Structure and Client of Record Identity |
| POL-044 | SharePoint Matter Folder Access Staging Policy |
| POL-045 | Asana Integration Safeguard Policy |
| POL-046 | Canva Template Enforcement Policy |
| POL-059 | Integration Control Policy |
| PRO-014 | Inbox Governance Protocol (Gmail) |
| PRO-020 | LL Matters SharePoint Protocol |
| PRO-021 | LL Matters Folder Protocol |
| PRO-022 | LL Matters File Protocol |

---

## 8. Boundary

This invariant establishes the **classification and governance rules** for all external platform integrations.

Policies define operational constraints, approval gates, and use-case-specific permission boundaries.

Protocols define enforcement mechanics, validation checks, and audit logging formats.
