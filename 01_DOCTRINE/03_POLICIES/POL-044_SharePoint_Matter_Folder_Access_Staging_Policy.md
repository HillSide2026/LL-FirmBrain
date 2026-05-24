---
id: POL-044
title: SharePoint Matter Folder Access Staging Policy
owner: ML1
status: approved
approval: ML1
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
tags: [policy, sharepoint, legalmatters, access-control, staging, matter-filing]
---

# POL-044 — SharePoint Matter Folder Access Staging Policy

Policy Statement: Access and write behavior for SharePoint LegalMatters matter folders must be stage-gated. Stage 1 is fully read-only. Stage 2 introduces controlled, folder-specific write permissions and prohibitions.

Authority (Principles referenced): PRN-003, PRN-004, PRN-006, PRN-020, PRN-026  
Enforcement expectation: Any write operation inconsistent with the active stage or folder-level rule is non-compliant and must be blocked or escalated.  
Supersedes: None  
Enforcement Protocol: PRO-013

---

## 1. Purpose

This policy defines stage-based write governance for the six canonical matter sub-folders in SharePoint LegalMatters (`Working Files` drive), so access behavior remains deterministic and auditable.

---

## 2. Scope

This policy applies to:
- `levinellp.sharepoint.com/sites/LegalMatters` matter folders implementing the canonical six-folder model
- System/agent-initiated operations and operational workflow tooling

Canonical sub-folders:
- `01_Opening`
- `02_Client Productions`
- `03_Communication`
- `04_Research`
- `05_Deliverables`
- `06_Closing`

---

## 3. Stage Model

| Stage | Status | Rule |
|------|--------|------|
| Stage 1 | Active default | All six sub-folders are read-only for system operations |
| Stage 2 | Planned | Folder-specific write permissions and prohibitions apply exactly as defined in Section 5 |

Stage transition from Stage 1 to Stage 2 requires explicit ML1 approval and recorded activation artifact.

---

## 4. Stage 1 Policy (Read-Only Baseline)

In Stage 1, all six folders are read-only.

No autonomous or assisted write operation is permitted by system tooling within these folders.

---

## 5. Stage 2 Policy (Controlled Folder Rules)

### `01_Opening`
- Write-heavy during LL administrative setup workflows, then primarily read.

### `02_Client Productions`
- Read-only.

### `03_Communication`
- System does not write to this folder.

### `04_Research`
- Write-risk zone.
- Any system-generated document must be explicitly tagged as system-generated.

### `05_Deliverables`
- No autonomous writing.
- Any write requires explicit governed approval path.

### `06_Closing`
- System does not write to this folder.

---

## 6. Required Tagging for Stage 2 `04_Research`

When the system generates a document in `04_Research`, it must include an explicit system-generated marker in available artifact metadata or visible document header.

Minimum requirement:
- marker text: `SYSTEM_GENERATED`

Absence of this marker in system-generated research artifacts is non-compliant.

---

## 7. Enforcement and Escalation

Runtime controls must enforce:
- stage-aware access gates
- folder-level write allow/deny checks
- tagging validation for `04_Research`
- autonomous-write blocking for `05_Deliverables`

Any violation must be blocked and escalated to ML1 with run-level evidence.

---

## 8. Summary

Stage 1: all six matter sub-folders are read-only.  
Stage 2: controlled exceptions apply by folder, with explicit prohibitions and tagging requirements.
