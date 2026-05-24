---
id: lexaro.list_documents
title: 'Capability Profile: Lexaro.ListDocuments'
owner: ML1
status: draft
version: '0.1'
effective_date: '2026-05-12'
supersedes:
provenance:
  decided_by: ML1
  decided_on: '2026-05-12'
  context: Metadata normalized by system admin cleanup on 2026-05-24
created_date: '2026-05-12'
last_updated: '2026-05-12'
tags: [lexaro, capability, read-only, documents]
policy: POL-066
protocol: PRO-026
---

# Capability Profile: Lexaro.ListDocuments (v0.1)

## Purpose

Retrieve document metadata and document indexes from Lexaro for observational
use by ML2. No mutation of Lexaro state is permitted. Document content is not
retrieved in Mode 1.

## Allowed Actions

- `GET /api/external/v1/documents` — list documents
- `GET /api/external/v1/documents/{document_id}` — get a single document by ID
- `GET /api/external/v1/documents/folders` — list document folder structure
- `GET /api/external/v1/document-templates` — list document templates
- Read document metadata fields (name, type, version, matter reference, folder path, identifiers)

## Disallowed Actions

- Downloading document content (`/api/external/v1/documents/{id}/download` is prohibited)
- Creating, updating, or deleting documents
- Uploading documents
- Modifying document metadata
- Any request using `POST`, `PUT`, `PATCH`, or `DELETE`
- Writing inferences or summaries back to Lexaro

## Inputs (Typed)

- `document_id`: string (optional; omit to list all)
- `page`: integer (optional)
- `per_page`: integer (optional)

## Outputs (Typed)

- `source_system`: string — always `"Lexaro"`
- `source_object_type`: string — always `"document"`
- `source_object_id`: string — Lexaro native document ID
- `retrieved_at`: string — ISO 8601
- `endpoint`: string — API endpoint called
- `fields`: object — normalized document metadata (no content)

## Required Logs

- Endpoint called
- HTTP status code
- Request latency (ms)
- Number of records returned
- Success or failure flag

## Approval Mode

- Auto when request stays within approved metadata-only read boundary for documents.

## Boundary Rules

- HTTP method must be `GET`. No other method is permitted.
- Document content (`/download` endpoints) is explicitly excluded from Mode 1.
- Credentials must be loaded from environment only.
- Secrets must never appear in logs or output.
- Retrieved data must include provenance block.
- The Lexaro server-side bug (PRO-026 §6) is resolved as of 2026-05-15; this capability is unblocked.
