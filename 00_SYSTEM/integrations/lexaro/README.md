---
id: 00_system_integrations_lexaro_readme_md
title: Lexaro Integration — Mode 1 (Read-Only)
owner: ML1
status: draft
created_date: 2026-05-18
last_updated: 2026-05-18
tags: []
---

# Lexaro Integration — Mode 1 (Read-Only)

## Status

**Mode 1 connectivity test implemented. Blocked on server-side bug in Lexaro.**

## Product

Lexaro is a Canadian legal practice management SaaS by TechHighway Systems Inc.
It is under evaluation as a potential Clio replacement for Levine Law.

ML2's integration is **read-only observation only**. No write operations are permitted.

---

## Discovered API Surface

| Item | Value |
|---|---|
| Base URL | `https://app.lexaro.ca` |
| Framework | Laravel + Inertia.js (TechHighway) |
| Auth type | API key + secret (custom middleware) |
| Auth headers | `X-Api-Key: {key_id}` + `X-Api-Secret: {api_secret}` |
| External API prefix | `/api/external/v1/` |
| OpenAPI spec route | `GET /firm/settings/api-access/openapi` (requires auth) |
| API guide route | `GET /firm/settings/api-access/guide` (requires auth) |

### Available Read-Only External Endpoints (GET)

```
/api/external/v1/matters
/api/external/v1/matters/{matter}
/api/external/v1/clients
/api/external/v1/clients/{client}
/api/external/v1/tasks
/api/external/v1/tasks/{task}
/api/external/v1/documents
/api/external/v1/documents/{document}
/api/external/v1/documents/folders
/api/external/v1/document-templates
/api/external/v1/clauses
/api/external/v1/task-reminders
/api/external/v1/tasks-due-soon
```

---

## Known Issue

Lexaro's external API middleware returns HTTP 500 (Server Error) whenever
both `X-Api-Key` and `X-Api-Secret` headers are present — regardless of
whether the credentials are valid or not. This is a server-side bug in
Lexaro's code (reproduced with bogus credentials).

Without both headers, the server returns 401 "Missing API credentials."

**Next steps before integration can proceed:**
1. Log into the Lexaro UI → Settings → API Access → confirm the API key is active.
2. Report the 500 bug to Lexaro support with a simple curl reproduction case.
3. Ask Lexaro support to confirm the correct auth header format.
4. Re-run `scripts/lexaro_smoke_test.py` once resolved.

---

## Credentials

Stored in `.env` (gitignored) using YAML-style syntax:

```
Lexaro_Key_ID: lex_...
Lexaro_API_Secret: ...
```

Note: standard `python-dotenv` will not parse these lines because they use
`: ` instead of `=`. The smoke test script handles this with a custom parser.

---

## Running the Smoke Test

```bash
# From repo root
python3 scripts/lexaro_smoke_test.py
```

Output: status codes and redacted sample responses for three read-only endpoints.
Secrets are never printed.

---

## Constraints

- ML2 may only read Lexaro data — no writes, no mutations.
- Do not add write scopes or call any non-GET endpoints.
- The full route map (405 routes) was reverse-engineered from the Ziggy JS object
  embedded in the app's HTML. This is supplemental information only — the OpenAPI
  spec at `/firm/settings/api-access/openapi` is the authoritative API contract.
