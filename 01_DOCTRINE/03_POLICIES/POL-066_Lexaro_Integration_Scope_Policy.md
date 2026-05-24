---
id: POL-066
title: Lexaro Integration Scope Policy
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
tags: [lexaro, integration, policy, read-only]
related_invariant: INV-0011
related_protocol: PRO-026
---

# POL-066 — Lexaro Integration Scope Policy

---

## 1. Purpose

Define the permitted and prohibited scope of ML2's interaction with Lexaro.

Lexaro is under evaluation as a potential system of record for Levine Law.
During Mode 1, ML2 may only observe Lexaro data. No mutations of any kind are permitted.

---

## 2. Authority Boundary

Lexaro remains the transactional system of record.

ML2 may read selected Lexaro data for context, mapping, validation, and future
controlled derivations.

ML2 may not mutate Lexaro in any way.

---

## 3. Permitted Capabilities

ML2 may read the following Lexaro data types when available via the external API:

| Data type | Lexaro external endpoint |
|---|---|
| Client / contact metadata | `/api/external/v1/clients` |
| Matter metadata | `/api/external/v1/matters` |
| Task metadata and task states | `/api/external/v1/tasks` |
| Document metadata / document indexes | `/api/external/v1/documents` |
| Document folder structure | `/api/external/v1/documents/folders` |
| Document templates | `/api/external/v1/document-templates` |
| Task reminders | `/api/external/v1/task-reminders` |
| Tasks due soon | `/api/external/v1/tasks-due-soon` |
| Clauses | `/api/external/v1/clauses` |

Calendar and deadline metadata may be added if a read-only endpoint is confirmed.

All reads must use the `GET` HTTP method. No other HTTP method is permitted.

---

## 4. Prohibited Capabilities

ML2 must not:

- Create records in Lexaro
- Update records in Lexaro
- Delete records in Lexaro
- Change matter status
- Change task status
- Create calendar events
- Modify deadlines
- Upload documents
- Send communications
- Write notes or comments
- Trigger workflows
- Mark anything complete
- Infer approval
- Use any endpoint with `POST`, `PUT`, `PATCH`, or `DELETE`

The integration layer must enforce the HTTP method restriction in code.
No write method may exist in the Lexaro client module.

---

## 5. Credentials

### 5.1 Storage

Credentials must be stored in `.env` (gitignored) using standard dotenv format:

```
LEXARO_KEY_ID=<value>
LEXARO_API_SECRET=<value>
```

### 5.2 Handling

- Secrets must never be printed to logs, console output, or error messages.
- Secrets must never be committed to the repository.
- Secrets must never be pasted into prompts.
- The integration module must redact credentials in all log and error output.
- The smoke test must redact credentials in all output.

---

## 6. Required API Scopes

The Lexaro API key must have only read scopes:

- `clients:read`
- `matters:read`
- `tasks:read`
- `documents:read`
- `files:read`

No write scopes are permitted on the key. If write scopes are observed on the
active key, ML1 must be notified and the key must be replaced.

---

## 7. Logging Requirements

Each Lexaro API request must be logged with:

- Timestamp
- HTTP method (must always be `GET`)
- Endpoint called
- HTTP status code
- Request latency (ms)
- Success or failure flag
- Response size in bytes (if easily available)

Logs must not include:

- API secret
- Full client personal data
- Privileged document content
- Matter-level confidential information beyond metadata fields

---

## 8. Error Handling Requirements

The integration must clearly distinguish the following failure categories:

| Failure type | Expected handling |
|---|---|
| Missing credentials | Fail with clear message; do not attempt request |
| Authentication failure (401) | Log; escalate to ML1 |
| Permission / scope failure (403) | Log; escalate to ML1 |
| Endpoint not found (404) | Log; treat as capability gap; do not retry |
| Rate limit (429) | Log; back off; retry after delay |
| Server error (500+) | Log; do not retry automatically; surface to operator |
| Malformed response | Log raw response (redacted); raise parse error |
| Network failure | Log; raise with clear message |

---

## 9. Non-Goals

Mode 1 does not include:

- AI summaries derived from Lexaro data
- Task generation or task inference from Lexaro state
- Issue spotting from matters or documents
- Workflow recommendations
- Writing back to Lexaro in any mode
- Syncing Lexaro documents into ML2 storage
- Modifying deadlines
- Client communications
- Autonomous decisions based on Lexaro data

Mode 1 only proves safe observational access.

---

## 10. Related Artifacts

| Artifact | Purpose |
|---|---|
| INV-0011 | Integration Doctrine — Lexaro classified as read-only Tier-1 system |
| PRO-026 | Lexaro Mode 1 Integration Protocol — architecture, components, acceptance criteria |
| `scripts/lexaro_smoke_test.py` | Executable connectivity verification |
| `00_SYSTEM/integrations/lexaro/README.md` | API surface discovery notes |
