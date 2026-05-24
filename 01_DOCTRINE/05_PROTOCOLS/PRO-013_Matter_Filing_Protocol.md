---
id: PRO-013
title: Matter Filing Protocol
owner: ML1
status: approved
approval: ML1
approved_by: ML1
approved_date: 2026-04-18
project: LLP-006
version: 0.5
effective_date: 2026-04-18
supersedes:
provenance:
  decided_by: ML1
  decided_on: 2026-04-18
  context: Metadata normalized by system admin cleanup on 2026-05-24
created_date: 2026-03-07
last_updated: 2026-03-28
tags: [protocol, sharepoint, legalmatters, filing, provenance, classification]
---

# PRO-013 — Matter Filing Protocol

> **DRAFT — PENDING ML1 APPROVAL.**
> This protocol has not been approved and is not in effect.
> Classification rules defined here must not be implemented in any script,
> agent, or automated workflow until ML1 approves and sets `status: approved`.

---

## 1. Purpose

This protocol defines:

1. The required folder structure for matter files in `levinellp.sharepoint.com/sites/LegalMatters` (Working Files drive).
2. The five provenance classes assigned to documents within that structure.
3. The classification signals used to assign provenance.
4. The agent access rules that follow from provenance classification.

The protocol applies only to matters where the filing structure has been
implemented (as identified in the Phase 2 filing structure scan, 2026-03-06).
Matters that have not implemented the structure are out of scope for automated
classification until their filing structure is remediated.

---

## 2. Terminology

| Term | Definition |
|------|------------|
| **Filing Protocol** | This document. The prescriptive standard for how matter files must be organized and classified. |
| **Filing Structure** | The six-folder hierarchy defined in Section 3. A matter has "implemented the filing structure" only when all six canonical folders are present. |
| **Provenance** | The origin and authorship of a document — whether it came from the client, was drafted by LL, or was finalized by LL. |
| **Classification** | The act of assigning a provenance class to a document based on signals defined in Section 5. |
| **Client Productions** | Documents provided by the client to LL. The preferred term for what the `02_Client Productions` folder contains. |

---

## 3. Required Filing Structure

The canonical filing structure for ML2 is defined in this protocol itself.
Historical SharePoint "Model File" materials are not the governing source for
ML2 and must not be treated as a required upstream dependency.

Every matter folder must contain the following six numbered subfolders:

```
{matter_id} - {client_name}/         ← NTD: sub-matter reference may be suppressed
├── 01_Opening/
├── 02_Client Productions/
├── 03_Communication/
├── 04_Research/
├── 05_Deliverables/
└── 06_Closing/
```

### Folder descriptions

| Folder | Contents |
|--------|----------|
| `01_Opening` | LL-administered matter management documents: engagement agreement, conflict checks, ID records, accounts, notes to file. These are LL-internal administrative records, not client work product. |
| `02_Client Productions` | Documents provided by the client to LL (client productions). |
| `03_Communication` | Matter communications, including emails and notes on phone calls. |
| `04_Research` | LL-generated legal research, diligence analysis, transaction analysis, and strategy artifacts. |
| `05_Deliverables` | Documents prepared by LL and provided (or intended to be provided) to the client. This is the primary LL work product folder, whether marked draft or final. |
| `06_Closing` | Post-closing records. |

`03_Communication` subfolders (for example, `Emails`, `Phone Notes`) are optional and not mandatory.

### Observed folder name variations (accepted for compliance detection)

| Position | Canonical name | Accepted equivalents |
|----------|----------------|----------------------|
| 01 | `01_Opening` | `01_Admin`, `1. Admin`, `01_Admin_` |
| 02 | `02_Client Productions` | `02_Client Provided Documents`, `2. Client Provided Information including Corporate Records`, `02_Client Provided Documents_` |
| 03 | `03_Communication` | `03_Communication_` |
| 04 | `04_Research` | `04_Diligence`, `4. Diligence`, `04_Diligence _`, `05_Research`, `5. Research`, `05_Research_`, `03_Transaction_Documents`, `3. Transaction Documents`, `03_Transaction_Documents _` |
| 05 | `05_Deliverables` | `05_Deliverables_` |
| 06 | `06_Closing` | `6. Post-Closing`, `06_Post_Closing` |

---

## 4. Provenance Classes

Every document retrieved from LegalMatters must be assigned one of five
provenance classes before it may be accessed by any agent.

| Class | Meaning | Permissible agent actions |
|-------|---------|--------------------------|
| `CLIENT_PROVIDED` | Document originated from the client or a third party (client productions) | Reference only; never treat as LL work product; do not paraphrase as LL output |
| `LL_ADMIN` | LL-administered matter management document | Reference only for administrative context; do not treat as substantive work product or cite externally |
| `LL_DRAFT` | An LL-generated working draft, not finalized | May be used for context; must not be cited as final; must be labeled as draft if surfaced |
| `LL_FINAL` | An LL-signed or executed deliverable | May be cited as authoritative LL output; source URL must be included |
| `UNKNOWN` | Cannot be classified with available signals | Blocked from agent access until manually resolved by ML1 |

**Reservation:** Nothing from LegalMatters is assumed to be `LL_FINAL` without
at least one positive signal from Section 5 and explicit confirmation. Absence
of a draft signal does not imply final status.

---

## 5. Classification Signals

Classification is determined by evaluating signals in priority order. The
highest-confidence matching signal wins. If no signal matches, the class
is `UNKNOWN`.

### 5.1 Folder-path signals (highest priority)

| Folder | Class assigned | Notes |
|--------|---------------|-------|
| `02_Client Productions` (or accepted equivalent) | `CLIENT_PROVIDED` | Determinative |
| `01_Opening` (or accepted equivalent) | `LL_ADMIN` | Engagement agreements, conflicts, ID, accounts, opening records, notes to file |
| `03_Communication` (or accepted equivalent) | `LL_ADMIN` (default) | Communication record store; embedded attachments may be reclassified by origin |
| `04_Research` (or accepted equivalent) | `LL_DRAFT` (default) | This is a provenance/classification tag, not a legal-quality judgment |
| `05_Deliverables` | `LL_DRAFT` (default) | Primary LL work product folder; may be reclassified to `LL_FINAL` by positive signal |
| `06_Closing` (or accepted equivalent) | `LL_ADMIN` (default) | Closing records default to administrative class unless reclassified by signal |

### 5.2 Filename signals (secondary)

Applied as reclassification signals when a folder default class is assigned
(especially for `03_Communication`, `05_Deliverables`, and `06_Closing`).

| Pattern (case-insensitive) | Class assigned | Confidence |
|----------------------------|---------------|------------|
| `DRAFT` anywhere in name | `LL_DRAFT` | High |
| `redline` anywhere in name | `LL_DRAFT` | High |
| `_v1`, `_v2`, `_v3` … suffix | `LL_DRAFT` | High |
| `FINAL ML` in name | `LL_FINAL` | High |
| `For Execution` in name | `LL_FINAL` (pending execution) | High |
| `For Signature` in name | `LL_FINAL` (pending signature) | High |
| `Executed` in name | `LL_FINAL` | High |
| `PRECEDENT` in name | `LL_DRAFT` (template, not matter-specific) | High |
| `CLIENT RFI` in name | `CLIENT_PROVIDED` | Medium |
| Government form number prefix (e.g. `5261E`, `5271E`) | `UNKNOWN` — requires manual review | — |

### 5.3 Attachment origin signal (for `03_Communication`)

Embedded attachments in `03_Communication` may be reclassified by origin:

| Signal | Class assigned | Notes |
|--------|---------------|-------|
| Attachment origin verified as client/external source | `CLIENT_PROVIDED` | Requires provenance evidence |
| Attachment origin verified as LL-issued final deliverable | `LL_FINAL` | Requires positive final signal + provenance evidence |
| No origin evidence | Inherit folder default (`LL_ADMIN`) | Default behavior |

### 5.4 `createdBy` signal (not used)

Graph API `createdBy` always reflects the uploader, not the document author.
All sampled files showed `Matthew Levine` as creator regardless of provenance.
This field **must not** be used as a classification signal.

### 5.5 File extension signal (not used alone)

`.pdf` is not a reliable provenance signal — it can be any class. `.docx`
is more likely to be LL-generated but is not determinative. Extension may
be used as a supplementary signal only when combined with others.

---

## 6. Classification Procedure

For each document in a matter that has implemented the filing structure:

1. Evaluate folder-path signal (Section 5.1).
2. Assign the folder default class and record basis.
3. Evaluate filename signals (Section 5.2) and attachment-origin signals where applicable (Section 5.3).
4. If a higher-confidence reclassification signal matches, override default class and record basis.
5. If signals conflict or classification remains uncertain, assign `UNKNOWN` and add to the unclassified review list for ML1 resolution.
6. For any `LL_FINAL` assignment, record the specific positive signal(s) that
   support it. A bare `.pdf` with no naming signal does not qualify.

Classification results are written to `SHAREPOINT_MANIFEST.yaml` in the
matter's secondbrain folder (e.g., `05_MATTERS/STANDARD/{matter_id}/`).
No document content is written to secondbrain — only metadata and
provenance classification.

---

## 7. Agent Access Rules

| Class | May agent read content? | May agent cite externally? | Label required when surfaced |
|-------|------------------------|---------------------------|------------------------------|
| `CLIENT_PROVIDED` | Yes — for context only | No | "client-provided document" |
| `LL_ADMIN` | Yes — for administrative context only | No | "LL administrative record" |
| `LL_DRAFT` | Yes — for context only | No | "LL draft — not final" |
| `LL_FINAL` | Yes | Yes — with source URL | Source URL required |
| `UNKNOWN` | **No** | **No** | Blocked until ML1 resolves |

---

## 8. Scope Limitations

This protocol applies only to matters listed in the Phase 2 compliance scan
as `filing_structure_implemented: true`. Current baseline (2026-03-09): 0 of 41
matters (0%).

Matters not implementing the filing structure:
- Are not subject to automated classification.
- May not have their documents passed to any agent.
- Should be remediated by applying the six-folder structure before being
  brought into scope.

`Clerk Work`, `Data Management`, and `Model File` root folders are excluded
from classification scope entirely.

---

## 9. Open Items (NTD)

| Item | Description |
|------|-------------|
| NTD-1 | Confirm whether sub-matter reference should be suppressed in the matter folder name pattern |
| NTD-2 | None at this time |

---

## 10. Approval Gate

This protocol becomes active only after ML1 review and explicit approval.
Upon approval:
- Change `status` from `DRAFT` to `active`
- Change `version` from `0.4` to `1.0`
- Update `last_updated`
- Resolve NTD items before or concurrent with activation

Classification rules in Section 5 must not be coded into any script or agent
prior to that approval.

---

## 11. Change Log

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-03-07 | Initial draft. Based on Phase 2 enumeration (2026-03-06) and ML1 preliminary specifications. |
| 0.2 | 2026-03-07 | Revised per ML1 review: (1) Added `LL_ADMIN` as fifth provenance class. (2) Clarified `01_Admin` as `LL_ADMIN` (not client provided). (3) Clarified `04_Diligence` as mixed folder requiring filename tiebreaker. (4) Government forms confirmed as `UNKNOWN`. (5) Added NTD items for sub-matter folder naming and `02` folder rename. |
| 0.3 | 2026-03-09 | Revised filing hierarchy per ML1 direction: canonical folders updated to `01_Opening`, `02_Client Provided Documents`, `03_Communication`, `04_Research`, `05_Deliverables`, `06_Closing`; classification signals and accepted folder-name mappings reconciled to new structure. |
| 0.4 | 2026-03-09 | Revised per ML1 clarification: (1) Canonical `02` renamed to `02_Client Productions`. (2) Added explicit default-class model and attachment-origin reclassification for `03_Communication`. (3) Clarified `04_Research` default as a provenance tag. (4) Tightened filing-structure implementation requirement to all six canonical folders. (5) Updated baseline scope count to 0 of 41. |
