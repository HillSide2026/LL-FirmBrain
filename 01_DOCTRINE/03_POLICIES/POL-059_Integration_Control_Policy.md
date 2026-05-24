---
id: POL-059
title: Integration Control Policy
owner: ML1
status: approved
approved_by: ML1
approved_date: 2026-04-18
version: 1.5
effective_date: 2026-04-18
supersedes:
provenance:
  decided_by: ML1
  decided_on: 2026-04-18
  context: Metadata normalized by system admin cleanup on 2026-05-24
created_date: 2026-02-27
last_updated: 2026-03-28
tags: [integration, policy, control]
---

# Integration Control Policy

(Operational Control Specification)

This is the enforceable layer.

---

## 0. Precedence

For operational external writes, this policy **supersedes** `POL-058_System_Write_Back_Policy.md`.
Only explicit hard prohibitions defined as invariants remain controlling.

---

## 1. Data Classification

### 1.1 Canonical Data (ML2 Only)

- Templates
- Playbooks
- Risk registers
- Fallback ladders
- Governance documents

Cannot be modified externally.

### 1.2 Published Data

- Working drafts
- Client deliverables
- Internal collaboration copies

Editable externally but non-authoritative.

---

## 2. Read Controls

Agents may read external documents when:
- Triggered by QC gate
- Requested by ML1
- Required for drift detection

Bulk ingestion prohibited unless approved.

---

## 3. Write Controls

All writes must:
- Be to designated folders/sites
- Include artifact version reference
- Include "Derived from ML2 vX.Y" label
- Avoid modifying canonical paths

No direct writes into ML2 from external suites.

### 3.1 SharePoint Site Classes

SharePoint surfaces must be classified as one of:
- `read_only_authority`
- `managed_workspace`

Current approved classes:
- `levinellp.sharepoint.com/sites/LegalMatters` = `read_only_authority`
- `levinellp.sharepoint.com/sites/Documentation` = `managed_workspace`
- `levinellp.sharepoint.com/sites/Clients` = `managed_workspace`

### 3.1.1 Scoped Sub-Surface Exceptions

ML1 may approve a narrower operational exception inside a site that otherwise remains
`read_only_authority` when all of the following are true:
- the exact site, library or list, and path scope are named in ML2 integration contracts
- allowed tools and prohibited actions are explicitly listed
- structure, permission, deletion, publication, and retention authority remain separately controlled
- the action is invoked by an approved workflow, runbook, or capability when the exception permits writes
- run evidence is emitted into ML2

A scoped sub-surface exception does not reclassify the parent site.

### 3.2 Read-Only Authority Rule

For a site classified as `read_only_authority`, the system MAY perform read-only
operations within the explicitly approved site, library, and path scope when:
- the site is explicitly named in ML2 integration contracts
- the operation satisfies Section 2 read controls
- runtime boundaries restrict access to the approved read-only scope

The system MUST NOT, for a `read_only_authority` site:
- create, update, replace, move, or delete files or folders
- alter permissions, sharing state, or site structure
- infer write authority from visibility, existing credentials, or related site access

### 3.3 Managed Workspace Rule

For a site classified as `managed_workspace`, the system MAY perform read, write, and manage operations across the approved site when:
- the site is explicitly named in ML2 integration contracts
- the operation is invoked by an approved workflow, runbook, or capability
- run evidence is emitted into ML2

Managed-workspace authority does not convert that site into canonical storage.
ML2 remains the authority for doctrine and governed canonical artifacts.

### 3.3.1 Approved Clients Managed Workspace Authority

For `levinellp.sharepoint.com/sites/Clients`, ML1 has approved site-wide
`managed_workspace` authority.

Within this authority, the system MAY perform read, write, and manage operations
across the Clients site, including:
- create, update, replace, move, rename, publish, demote, or delete pages and libraries
- alter page layout, canvas structure, title area structure, navigation, permissions, sharing, retention, and site settings
- create, delete, reposition, and configure web parts
- create, update, move, rename, or delete client folders, libraries, and routing paths
- break inheritance and assign SharePoint principals within the site

The Clients managed-workspace authority is valid only when:
- the operation stays within the explicit `/sites/Clients` scope declared in ML2 integration contracts
- read actions satisfy Section 2 read controls
- write and manage actions are invoked by an approved workflow, runbook, or capability
- write invariants in Section 3 are satisfied
- run evidence is emitted into ML2

No separate `approval_reference` is required solely because a Clients-site
operation is structural, navigational, permission-bearing, or otherwise broader
than page content edits.

The system MUST NOT under this authority:
- infer authority over any non-`Clients` SharePoint surface
- create or manage tenant-wide identity objects unless separately admitted
- alter tenant-wide retention, compliance, or cross-site default sharing settings unless separately admitted

---

## 4. Folder & Site Segmentation

External platforms must maintain:
- /Published Templates/
- /Working Drafts/
- /Candidate for Promotion/
- /Archive/

No canonical artifacts stored outside ML2 repository.

For SharePoint:
- `Documentation` may implement this segmentation site-wide.
- `LegalMatters` remains outside this write-capable segmentation model and stays read-only.
- `Clients` may implement this segmentation site-wide as a managed workspace.

---

## 5. Promotion Workflow (Enforced)

When an external document is proposed for canonical status:

Step 1 — Move to /Candidate for Promotion/  
Step 2 — Automated diff vs canonical  
Step 3 — Structured change summary generated  
Step 4 — ML1 approval recorded  
Step 5 — Version increment in ML2  
Step 6 — Republish to /Published Templates/  

If ML1 does not approve, document remains non-canonical.

---

## 6. Audit Requirements

System must retain:
- 24-month integration activity log minimum
- Diff history for each promoted artifact
- Approval reference ID
- Agent version that executed action

For Clients managed-workspace operations, the retained audit trail must also
make the affected page paths, library names, permission targets, resolved
principals, navigation targets, and structural mutations reconstructable from
the run record.

---

## 7. Escalation Triggers

Immediate ML1 escalation if:
- Canonical artifact modified externally
- Version mismatch detected
- Unauthorized write detected
- Drift exceeds threshold
- Requested Clients permission or routing targets cannot be resolved confidently
