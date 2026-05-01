---
id: llp-037_ll_current_system
title: LLP-037 LL Current System Map
owner: ML1
status: draft
created_date: 2026-05-01
last_updated: 2026-05-01
tags: [system-design, current-state, architecture]
---

# LL Current System Map

**Version:** v0.1 — drafted 2026-05-01  
**Sources:** `00_SYSTEM/CONFIG/systems_of_record.yml`, `00_SYSTEM/integrations/`, `01_DOCTRINE/03_POLICIES/POL-043`, ll-secondbrain repo analysis  
**Status:** Draft — ML1 review and correction required

---

## What This Document Describes

This is the **operational system** Levine Law runs on today: Clio + Google Workspace + SharePoint + GHL + Asana, loosely coupled and manually coordinated. Asana has been used as an attempted integration layer to stitch these systems together — with limited success. This document is not a description of repos under development. Those are captured in `LL_FUTURE_SYSTEM.md`.

---

## System Inventory

### 1. Clio

| Attribute | Value |
|---|---|
| Role | Legal practice management — matter registry and billing |
| System type | **System of Record for Matters** |
| Authoritative fields | `matter_id`, `matter_number`, `status`, `responsible_attorney`, `client` (per `systems_of_record.yml`) |
| Matter ID format | `YY-CCC(C)-NNNNN` (e.g., `25-927-00003`) — Year / Client contact code / Per-client sequence (POL-043) |
| What it tracks | Matters, clients, contacts, time entries, invoices, trust accounts, billing |
| ll-secondbrain integration | Read-only cache access; Clio API integration planned but not implemented (`clio_sources.yaml`: *"Plan-level only; no config present"*) |
| Write policy | Read-only from ML2 |
| Constraints | Canonical matter_id must not be reinterpreted; client-of-record identity is strict and matter-bound (POL-043) |

---

### 2. SharePoint

| Attribute | Value |
|---|---|
| Role | Document storage and matter file truth |
| System type | **System of Record for Documents** |
| Authoritative fields | `drive_item_id`, `path`, `modified_at`, `web_url` (per `systems_of_record.yml`) |
| ll-secondbrain integration | Live MCP server (`scripts/sharepoint_mcp_server.py`) — read metadata on legalmatters; read/write on documentation and clients |

**Sites in use:**

| Site | Path | Authority | Purpose |
|---|---|---|---|
| `legalmatters` | `/sites/LegalMatters` | Read-only | Active matter files — `LL Matters (Essential)`, `LL Matters (Strategic)`, `LL Matters (Standard)`, `LL Matters (Standard Cash Cows)`, `LL Matters (Parked)`, `Clerk Work` |
| `documentation` | `/sites/Documentation` | Read/write/manage | Internal working docs, templates, SB execution workspace |
| `clients` | `/sites/Clients` | Read/write/manage | Current client portal — per-client branded pages and document libraries |

**Current client portal model (SharePoint-native):**
- Branded sign-in page at `/sites/Clients`
- Per-client SharePoint pages + document libraries (e.g., `ClientName-Documents`)
- Client access via SharePoint credentials / guest access
- No automated document delivery — manual upload by lawyer or admin

---

### 3. Gmail

| Attribute | Value |
|---|---|
| Role | All external communications |
| System type | **System of Record for Communications** |
| Inbox | `Matthew@levinelegalservices.com` |
| Authoritative fields | `thread_id`, `message_ids`, `participants`, `last_message_at`, `labels` (per `systems_of_record.yml`) |
| ll-secondbrain integration | Live MCP server (`scripts/gmail_mcp_server.py`) — read inbox, apply labels, create drafts |
| Write policy | Labels and drafts permitted under governed policy; no autonomous send |
| Matter linkage | Matter threads identified by Gmail labels and manual routing; no automated Clio↔Gmail link |

---

### 4. GHL (GoHighLevel)

| Attribute | Value |
|---|---|
| Role | Lead capture, CRM, and marketing automation |
| System type | System of Record (commercial / acquisition) |
| Owns | Leads, contacts (pre-matter), pipeline stages, form submissions, automations, email sequences |
| ll-secondbrain integration | Not integrated — referenced in operational context only |
| Handoff to Clio | Manual — no automated matter creation from GHL lead conversion |

---

### 5. Google Workspace (Calendar, Drive, Sheets)

| Tool | Role | Integration status |
|---|---|---|
| Google Calendar | Scheduling — deadlines, hearings, client meetings | Integration stub in `00_SYSTEM/integrations/google_calendar/` |
| Google Drive | Ad hoc document storage — drafts, working files not yet in SharePoint | Integration stub in `00_SYSTEM/integrations/google_drive/` |
| Google Sheets | Tracking tables, financial models, ad hoc data | Integration stub in `00_SYSTEM/integrations/google_sheets/` |

None of these are formally integrated into the automated pipeline. Google Drive and Google Sheets are used ad hoc alongside SharePoint, creating parallel document storage with no canonical routing rule between them.

---

### 6. Microsoft Word + OneDrive

| Tool | Role | Integration status |
|---|---|---|
| Microsoft Word | Document drafting — agreements, letters, corporate documents | Integration stub in `00_SYSTEM/integrations/microsoft_word/` |
| OneDrive | Personal file sync, sometimes used as working document location | Integration stub in `00_SYSTEM/integrations/onedrive/` |

Word is the primary document drafting tool. Completed documents are manually uploaded to SharePoint (`legalmatters`) or sent to clients via Gmail. No automated pipeline.

---

### 7. Asana

| Attribute | Value |
|---|---|
| Role | Task tracking and workflow coordination — used as the attempted integration glue between Clio, SharePoint, Gmail, and GHL |
| System type | Coordination surface (not a system of record) |
| What it was used for | Tracking work items, matter tasks, and deadlines across the disconnected operational stack; attempting to create a unified workflow view |
| Why it didn't fully work | Asana has no native integrations with Clio, SharePoint, or Gmail — task data lives in Asana separately from canonical matter IDs; it began accumulating operational state that conflicted with Clio as the matter SOR |
| Governing constraint | POL-045 (Asana Integration Safeguard Policy, ML1-approved 2026-04-18): *"Asana is an operational execution surface, not a governing authority."* Asana metadata must not redefine matter identity, delivery status, or doctrine. Canonical `matter_id` remains Clio's. |
| Current access model | Stage 1 (read-only) by default per POL-045; Stage 2 controlled writes require explicit ML1 activation |
| ll-secondbrain integration | Referenced in fulfillment workflows (`LLM-007_FULFILLMENT_ORCHESTRATOR_AGENT.md`); script-level access via `todo_rollup.py` and `inbox_classifier.py` |
| Connected project | LLP-006 (reconciliation workflows) |

**The Asana problem in one line:** it was pressed into service as a workflow system because no real workflow system existed, but without integrations it required manual data entry to stay current, and it had no authority to enforce the handoffs it was supposed to track.

---

### 8. Canva

| Attribute | Value |
|---|---|
| Role | Brand assets, marketing design |
| Integration status | Stub in `00_SYSTEM/integrations/canva/`; MCP tools exist for design production workflow |

---

### 9. ll-secondbrain (This Repo)

| Attribute | Value |
|---|---|
| Role | AI coordination and intelligence layer sitting on top of the operational stack |
| System type | Governed knowledge base + AI execution environment (not a system of record) |
| What it reads | Gmail (live MCP), SharePoint (live MCP), Clio (via cache) |
| What it produces | Matter digests, portfolio briefs, inbox routing, drafted communications, practice area analysis |
| What it does not replace | Any of the systems above — it reads and derives, does not own |
| Boundary | ML2 storage boundary prohibits source-of-truth overrides and unbounded shadow databases (`systems_of_record.yml`) |

---

## Current System Flow

```
GHL (lead capture)
    │ manual handoff — no automation
    ▼
CLIO (matter creation — manual)
    │ matter_id assigned: YY-CCC-NNNNN
    │ responsible lawyer assigned
    │ billing structure set
    │
    ├─ GMAIL (client communications — ongoing, manual labeling)
    │
    ├─ ASANA (attempted workflow glue — manual data entry, no native integrations)
    │   tracks tasks across Clio + SharePoint + Gmail but with no live sync to any of them
    │
    ├─ MICROSOFT WORD (document drafting — manual)
    │       │ completed document manually uploaded
    │       ▼
    │   SHAREPOINT /sites/legalmatters (matter file storage)
    │       │ manually shared with client
    │       ▼
    │   SHAREPOINT /sites/clients (client portal — per-client library)
    │
    └─ GOOGLE CALENDAR (deadline tracking — manual entry)

ll-secondbrain reads Gmail + SharePoint + Clio cache
    → produces digests, routing, analysis
    → does not write to Clio, Gmail (except drafts), or legalmatters SharePoint
```

---

## Integration Map (Actual State)

| From | To | Mechanism | Status |
|---|---|---|---|
| GHL | Clio | Manual — no integration | Operational gap |
| Clio | SharePoint | Manual — lawyer organizes files | Operational gap |
| Clio | Gmail | Manual — lawyer sends from Gmail | Operational gap |
| Gmail | Clio | Manual — lawyer logs communications | Operational gap |
| Word | SharePoint/legalmatters | Manual upload | Operational gap |
| SharePoint/legalmatters | SharePoint/clients | Manual copy / share | Operational gap |
| ll-secondbrain | Gmail | Live MCP (read + draft) | Active |
| ll-secondbrain | SharePoint | Live MCP (read metadata; write to documentation/clients) | Active |
| ll-secondbrain | Clio | Cache read only | Partial |
| ll-secondbrain | Asana | Script-level read; Stage 2 writes require ML1 activation (POL-045) | Stage 1 only |
| Asana | Clio | None — tasks manually keyed to matter IDs | Manual / no sync |
| Asana | SharePoint | None | No integration |
| Asana | Gmail | None | No integration |

---

## Known Problems With the Current System

| Problem | Impact |
|---|---|
| No GHL → Clio automation | Lead conversion to matter is manual; delay and drop risk |
| No Clio → SharePoint automation | Matter folders not automatically created; file organization is ad hoc |
| No Gmail ↔ Clio linkage | Communications not automatically associated with matters; tracking is manual |
| Documents in Word + Google Drive + SharePoint with no canonical routing | Document location is unpredictable; version control is informal |
| Client portal = SharePoint page with manual file uploads | No delivery tracking, no automated notifications, no access control automation |
| No billing automation | Invoice generation, retainer tracking, and payment follow-up are manual |
| No deadline / docketing system | Google Calendar is used ad hoc; no automated deadline extraction from documents or Clio |
| All systems disconnected | Every handoff between systems requires manual action from ML1 |
| No workflow tracking | No system tracks what work needs to be done on a matter, who is doing it, or what stage it is at |
| Asana used as glue without integrations | Asana was pressed into service as a workflow layer but has no live connections to Clio, SharePoint, or Gmail; staying current required manual re-entry; it accumulated shadow state that conflicted with Clio's canonical matter records (addressed by POL-045) |
