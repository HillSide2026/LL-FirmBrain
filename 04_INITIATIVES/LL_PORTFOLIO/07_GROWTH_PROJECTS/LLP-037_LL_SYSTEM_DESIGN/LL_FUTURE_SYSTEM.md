---
id: llp-037_ll_future_system
title: LLP-037 LL Future System — Lead to Client Delivery (v0.1)
owner: ML1
status: approved
created_date: 2026-05-01
last_updated: 2026-05-01
tags: [system-design, future-state, architecture]
---

# LL Future System — Lead → Matter → Documents → Client Delivery

**Version:** v0.3  
**ML1 Approval Date:** 2026-05-01  
**Last updated:** 2026-05-01 — Lexora identified as early-stage legal practice management solution; open items expanded to Tier 1/2/3 structure  
**Status:** Approved — open items documented below

---

## End-to-End Flow

```
Lead Capture (GHL)
    │
    ▼
Conversion & Onboarding Layer (ll-corporate)
    - Thin interface
    - Handles product selection, retainer signup, and client authentication
    │
    ▼
Matter Creation (Authoritative System: Lexora)
    │
    ├─ Admin & Accounts Matter
    │   - Created in Lexora
    │   - Mirrored to ll-task-tracker
    │   - Used for intake, billing, and administrative lifecycle
    │
    └─ Legal Work Matter
        - Created in Lexora
        - Executed in LL-WrkEngine (Mike)
        - Projects = matters; Workflows = legal service execution
    │
    ▼
Matter Lifecycle Execution
    - Work performed in LL-WrkEngine (Mike)
    - Lawyer-AI collaboration via per-project and per-document chat
    - Workflow execution: document review, analysis, and generation
    - Status / state anchored to Lexora
    │
    ▼
Document Generation
    - Produced by LL-WrkEngine (Mike)
    - Output: DOCX with tracked changes, versioned documents
    │
    ▼
Document Storage Layer (ll-corporate-records)
    - Responsible for ingestion, metadata, and retrieval interface
    │
    ▼
Underlying Storage Engine (Mayan EDMS)
    - Provides document storage, indexing, and audit trail
    │
    ▼
Client Portal (ll-corporate)
    - Surfaces matter status
    - Provides document access to clients
```

---

## System Roles and Boundaries

| System | Role | Constraints |
|---|---|---|
| GHL | Lead capture / CRM | No matter or legal state |
| ll-corporate | Thin conversion + client portal | Must not own workflow or documents |
| Lexora | System of record for matter creation and lifecycle state | Early-stage legal practice management solution; API surface and capabilities still being defined |
| ll-task-tracker | Admin/accounts lifecycle mirror | Deployed at `firm.levinellp.ca`; no legal work logic |
| LL-WrkEngine (Mike) | Executes legal workflows; produces and manages documents | Deployed at `engine.levinellp.ca`; AGPL-3.0; must not own matter state (Lexora owns); must push outputs to ll-corporate-records |
| ll-corporate-records | Document system abstraction layer | No workflow logic |
| Mayan EDMS | Storage backend behind ll-corporate-records | Replaceable implementation detail |

---

## ML1 Decisions (Authoritative)

The following decisions are ML1-approved as of 2026-05-01.

**Decision 1: Lexora is the authoritative system for matter creation and lifecycle state.**

Lexora is the system of record. All matter identity and canonical lifecycle state originates in Lexora. Lexora is an early-stage legal practice management solution. Its API surface and capability set are not yet fully defined; integration contracts with ll-task-tracker and LL-WrkEngine must be deferred until Lexora's API is stable enough to specify against.

**Decision 2: ll-task-tracker operates strictly as a mirror for admin and accounts workflows.**

ll-task-tracker receives matter state from Lexora and manages the admin and accounts lifecycle layers. It does not originate matter state. The sync mechanism (event shape, push/pull model) is an open item — see below.

**Decision 3: Legal work execution is assigned to LL-WrkEngine (Mike).**

Legal work — task orchestration, document review, document generation, approval flows, completion states — is assigned to LL-WrkEngine. The repo has been initiated at `LL-WrkEngine`. It is based on Mike, an open-source AI legal work platform (AGPL-3.0).

LL-WrkEngine current capabilities (from repo analysis 2026-05-01):
- Projects (maps to matters) with document upload, versioning, and DOCX tracked-changes view
- Per-project and per-document AI chat (Claude + Gemini)
- Workflow execution (prompt-driven; currently built-in workflows cover credit agreement review, CP checklists, shareholder agreement summaries)
- Tabular review (structured multi-document analysis)
- Supabase (auth + Postgres) + S3-compatible object storage (Cloudflare R2) + LibreOffice for DOCX conversion

What still needs to be built for Levine Law's corporate services:
- Workflow templates for corporate service types (incorporation, director change, share issuance, minute book update, annual return)
- Integration with Lexora (receive matter trigger; send completion signal)
- Integration with ll-corporate-records (push finalized documents to the document store)
- Delivery confirmation / `markReadyToDeliver` coordination with ll-task-tracker

**Decision 4: ll-corporate must remain a thin layer.**

ll-corporate handles conversion, onboarding, and client interface only. It must not evolve into a workflow engine or system of record. This constraint is also stated in the repo's own README.

**Decision 5: ll-corporate-records is the document system of record.**

ll-corporate-records is responsible for document ingestion and retrieval. It is the abstraction layer. Mayan EDMS is the initial storage backend behind it.

**Decision 6: Mayan EDMS is an implementation detail behind ll-corporate-records.**

Mayan must not be directly coupled to any other system. All document access goes through ll-corporate-records. Mayan is replaceable.

---

## LL-WrkEngine (Mike) — Legal Work System

**Status:** Repo initiated (`LL-WrkEngine`). Base platform (Mike, AGPL-3.0) in place. LL-specific workflow templates and system integrations not yet built.

### What Mike Provides (From Repo Analysis)

| Capability | Status |
|---|---|
| Project-based matter organization | Exists |
| Document upload and versioning | Exists |
| DOCX tracked-changes view | Exists |
| Per-project and per-document AI chat (Claude + Gemini) | Exists |
| Workflow execution (prompt-driven, outputs to DOCX) | Exists — generic legal templates only |
| Tabular review (multi-document structured analysis) | Exists |
| Auth (Supabase) | Exists |
| Document storage (S3-compatible, e.g. Cloudflare R2) | Exists |

### What Still Needs to Be Built

| Capability | Notes |
|---|---|
| Corporate service workflow templates | Incorporation, director/officer change, share issuance, minute book update, annual return — none exist yet |
| Lexora integration | Receive matter-opened trigger; send completion signal back |
| ll-corporate-records integration | Push finalized documents to the document store abstraction layer |
| Delivery coordination | `markReadyToDeliver` signal to ll-task-tracker accounts lifecycle |
| Client-facing document access | ll-corporate surfaces documents — needs retrieval path from ll-corporate-records |

### License Constraint

LL-WrkEngine is based on Mike (AGPL-3.0). Any modifications distributed as a network service are subject to AGPL copyleft obligations. This must be assessed before any LL-specific customizations are deployed as a hosted service.

---

## Open Items

Grouped by resolution priority. Tier 1 items block integration design. Tier 2 items block Phase 2 build. Tier 3 items are tracked from earlier analysis and depend on Tier 1.

### Tier 1 — Cannot proceed without answers

| # | Open Item | Blocking |
|---|---|---|
| OI-07 | Lexora API surface — what does Lexora expose today? What endpoints, webhooks, or event mechanisms are available or planned? | OI-01, OI-02, OI-05, OI-06 — all integration contracts |
| OI-08 | Matter creation trigger — what event causes a matter to be created in Lexora? Client retainer completion? ML1 manual action? GHL automation? | ll-corporate conversion flow; GHL → Lexora handoff design |
| OI-09 | Matter identity scheme — what is the canonical matter ID in Lexora? Is it the existing Clio `YY-CCC-NNNNN` format (POL-043) or a new scheme? What is the cross-system identifier that ties a matter across Lexora, ll-task-tracker, LL-WrkEngine, and Mayan? | Every integration contract; document routing; matter linkage |
| OI-10 | Clio → Lexora transition — what happens to active matters currently in Clio? Migration, coexistence, or hard cutover from a date? Clio is the current authoritative SOR; Lexora is the future SOR; the handoff is undefined. | Any production use of Lexora as authoritative |

### Tier 2 — Block Phase 2 design

| # | Open Item | Blocking |
|---|---|---|
| OI-11 | Identity and auth model — ll-task-tracker uses Keycloak; LL-WrkEngine uses Supabase; ll-corporate uses Keycloak. Is there a single identity provider for the future system, or do users have separate sessions per surface? Can a lawyer access `firm.levinellp.ca` and `engine.levinellp.ca` with the same credentials? | User experience and auth architecture for Phase 2 |
| OI-12 | Document lifecycle trigger — when does a document move from LL-WrkEngine's own S3 storage to ll-corporate-records (Mayan)? At completion? At delivery? At every version? What happens to the copy in LL-WrkEngine after the push? | OI-05; ll-corporate-records ingestion contract |
| OI-13 | ll-task-tracker transition authority — when a lawyer performs a state transition in `firm.levinellp.ca`, does that write to ll-task-tracker first (which then syncs to Lexora), or must all transitions originate in Lexora and flow down? Camunda either stays as the execution engine or gets bypassed — these are different architectures. | OI-01; ll-task-tracker rearchitecting |
| OI-04 | Retainer signup and payment surface — where does payment processing and retainer setup live? Not present in ll-corporate or any other repo. Which payment processor? | Conversion and onboarding flow completeness |

### Tier 3 — Depend on Tier 1 resolution

| # | Open Item | Blocking |
|---|---|---|
| OI-01 | Lexora sync model — push (webhook/event) or pull? What is the event shape? | ll-task-tracker mirror architecture |
| OI-02 | Accounts lifecycle ownership — does Lexora own accounts state, or does ll-task-tracker own it and sync to Lexora? | Accounts lifecycle build |
| OI-03 | LL-WrkEngine workflow template sequence — which corporate service types first? | Legal work execution for corporate services |
| OI-03b | AGPL-3.0 compliance posture for LL-WrkEngine customizations | LL-WrkEngine deployment |
| OI-05 | ll-corporate-records → Mayan ingestion contract — how does LL-WrkEngine push documents in? How does ll-corporate retrieve them? | Document flow end-to-end |
| OI-06 | `markReadyToDeliver` cross-system coordination — originally designed as an in-process Spring event; must be redesigned as a cross-system call with Lexora as SOR and LL-WrkEngine as executor | Accounts backlog Phase 5 |

---

## Next Work Items

**Work Item 1: LL-WrkEngine Capability Scoping (v0.1)**

**Objective:** Define which corporate service workflow templates need to be built in LL-WrkEngine for Levine Law's initial service scope, and sequence their development.

**Dependencies:**
- Confirmation of initial corporate service scope (incorporation first? which matter types?)
- Matter model in Lexora (to understand what data is available at workflow trigger)

**Output:** A workflow template backlog for LL-WrkEngine, ordered by service priority.

---

**Work Item 2: LL-WrkEngine Integration Contracts**

**Objective:** Specify the integration points between LL-WrkEngine and (a) Lexora, (b) ll-corporate-records, and (c) ll-task-tracker delivery coordination.

**Dependencies:**
- Lexora sync model resolved (OI-01)
- ll-corporate-records document ingestion contract (OI-05)

**Output:** Integration contract specs for each boundary, suitable for implementation.

---

**Work Item 3: AGPL-3.0 Compliance Assessment**

**Objective:** Assess whether planned LL-specific customizations to Mike trigger AGPL-3.0 obligations, and determine the appropriate compliance posture.

**Output:** Legal assessment and deployment decision (internal-only vs. hosted service implications).
