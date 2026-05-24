---
id: PRO-026
title: Lexaro Mode 1 Integration Protocol
owner: ML1
status: draft
version: '1.0'
effective_date: '2026-05-12'
supersedes:
provenance:
  decided_by: ML1
  decided_on: '2026-05-12'
  context: Metadata normalized by system admin cleanup on 2026-05-24
created_date: '2026-05-12'
last_updated: '2026-05-12'
tags: [lexaro, integration, protocol, read-only, mode-1]
policy: POL-066
related_invariant: INV-0011
---

# PRO-026 — Lexaro Mode 1 Integration Protocol

---

## 1. Purpose

Define the architecture, required components, and acceptance criteria for
Mode 1 read-only integration between ML2 and Lexaro.

Mode 1 is observational only. No write capability may be introduced.

---

## 2. Operating Rule

> ML2 may see.
> ML2 may not act inside Lexaro.

---

## 3. Integration Architecture

### 3.1 Base URL

```
https://app.lexaro.ca
```

### 3.2 Authentication

```
X-Api-Key: {LEXARO_KEY_ID}
X-Api-Secret: {LEXARO_API_SECRET}
```

Credentials are loaded from environment only. Never hardcoded.

### 3.3 Module Structure

The Lexaro integration must be organized as a discrete module:

```
scripts/
  lexaro_smoke_test.py        # Connectivity verification (exists)

00_SYSTEM/integrations/lexaro/
  README.md                   # API surface and status notes (exists)

# Future: if a full client module is built
integrations/lexaro/
  client.py                   # HTTP client — GET only, credential loading, logging
  models.py                   # Normalized internal models with provenance
  repositories.py             # Domain-level read methods (list_matters, etc.)
```

If repo conventions differ from the above, follow the existing ML2 structure.

---

## 4. Required Components

### 4.1 Lexaro Client

A minimal HTTP client that:

- Loads credentials from environment (`LEXARO_KEY_ID`, `LEXARO_API_SECRET`)
- Constructs authenticated GET requests only
- Explicitly rejects `POST`, `PUT`, `PATCH`, `DELETE` — these must raise an error in code, not just be unused
- Redacts secrets in all log and error output
- Logs each request per Section 7 of POL-066

### 4.2 Smoke Test

`scripts/lexaro_smoke_test.py` satisfies this requirement (implemented 2026-05-12).

The smoke test must:

- Attempt harmless GET requests against at least: matters, clients, tasks
- Print: endpoint called, HTTP status, success/failure, small redacted sample
- Never print secrets
- Exit with a clear PASS/FAIL summary

### 4.3 Normalized Models

Do not expose raw Lexaro JSON directly to ML2 reasoning logic.

Each retrieved object type must be normalized into an internal model that includes:

| Field | Description |
|---|---|
| `source_system` | Always `"Lexaro"` |
| `source_object_type` | e.g., `"matter"`, `"client"`, `"task"`, `"document"` |
| `source_object_id` | Lexaro's native ID for the record |
| `retrieved_at` | ISO 8601 timestamp of retrieval |
| `endpoint` | API endpoint or repository method used |
| `fields` | Normalized field mapping from raw Lexaro response |

Minimum required models: `Matter`, `Client`, `Task`, `Document`.

Additional models (`File`, `Deadline`) may be added when confirmed available.

### 4.4 Provenance

Every retrieved object must carry a provenance block (see §4.3).
This satisfies POL-002 (Provenance Requirement) for externally sourced data.

---

## 5. Acceptance Criteria

Mode 1 is complete when all of the following are true:

| # | Criterion |
|---|---|
| 1 | ML2 can authenticate to Lexaro |
| 2 | ML2 can perform at least one successful GET request |
| 3 | ML2 can retrieve matters, clients, tasks, and document/file metadata (where endpoints exist) |
| 4 | No write method exists anywhere in the integration layer |
| 5 | Write HTTP methods are blocked by code (not merely unused) |
| 6 | Secrets are never logged or printed |
| 7 | Retrieved data includes provenance (source_system, source_object_type, source_object_id, retrieved_at) |
| 8 | Smoke test can be run safely and produces a clear PASS/FAIL |
| 9 | A README explains how to run the smoke test |
| 10 | No Lexaro state is changed by any operation |

---

## 6. Current Status

| Item | Status |
|---|---|
| Smoke test script | Implemented (`scripts/lexaro_smoke_test.py`) |
| Integration README | Implemented (`00_SYSTEM/integrations/lexaro/README.md`) |
| Auth format discovered | Confirmed (`X-Api-Key` + `X-Api-Secret`) |
| Connectivity | **Blocked** — Lexaro server-side 500 bug in `/api/external/v1/*` middleware |
| Normalized models | Not yet implemented |
| Full client module | Not yet implemented |

**Blocker:** Lexaro's external API middleware returns HTTP 500 for any request
with both `X-Api-Key` + `X-Api-Secret` headers, regardless of credential validity.
This is a Lexaro-side bug. Unblocked when Lexaro support resolves the issue.

---

## 7. Related Artifacts

| Artifact | Purpose |
|---|---|
| POL-066 | Lexaro Integration Scope Policy |
| INV-0011 | Integration Doctrine |
| `scripts/lexaro_smoke_test.py` | Smoke test (implemented) |
| `00_SYSTEM/integrations/lexaro/README.md` | API discovery notes |
