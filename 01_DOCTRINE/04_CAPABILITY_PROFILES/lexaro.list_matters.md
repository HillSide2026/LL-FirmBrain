---
id: lexaro.list_matters
title: 'Capability Profile: Lexaro.ListMatters'
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
tags: [lexaro, capability, read-only, matters]
policy: POL-066
protocol: PRO-026
---

# Capability Profile: Lexaro.ListMatters (v0.1)

## Purpose

Retrieve matter metadata from Lexaro for observational use by ML2.
No mutation of Lexaro state is permitted.

## Allowed Actions

- `GET /api/external/v1/matters` — list matters
- `GET /api/external/v1/matters/{matter_id}` — get a single matter by ID
- Read matter metadata fields (name, status, client reference, dates, identifiers)

## Disallowed Actions

- Creating, updating, or deleting matters
- Changing matter status
- Any request using `POST`, `PUT`, `PATCH`, or `DELETE`
- Writing inferences or summaries back to Lexaro

## Inputs (Typed)

- `matter_id`: string (optional; omit to list all)
- `page`: integer (optional; for pagination)
- `per_page`: integer (optional)

## Outputs (Typed)

- `source_system`: string — always `"Lexaro"`
- `source_object_type`: string — always `"matter"`
- `source_object_id`: string — Lexaro native matter ID
- `retrieved_at`: string — ISO 8601
- `endpoint`: string — API endpoint called
- `fields`: object — normalized matter metadata

## Required Logs

- Endpoint called
- HTTP status code
- Request latency (ms)
- Number of records returned
- Success or failure flag

## Approval Mode

- Auto when request stays within approved read boundary for matters.

## Boundary Rules

- HTTP method must be `GET`. No other method is permitted.
- Credentials must be loaded from environment only.
- Secrets must never appear in logs or output.
- Retrieved data must include provenance block.
- This capability is blocked pending resolution of Lexaro server-side bug (PRO-026 §6).
