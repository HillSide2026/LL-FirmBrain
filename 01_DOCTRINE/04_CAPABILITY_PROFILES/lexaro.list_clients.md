---
id: lexaro.list_clients
title: 'Capability Profile: Lexaro.ListClients'
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
tags: [lexaro, capability, read-only, clients]
policy: POL-066
protocol: PRO-026
---

# Capability Profile: Lexaro.ListClients (v0.1)

## Purpose

Retrieve client and contact metadata from Lexaro for observational use by ML2.
No mutation of Lexaro state is permitted.

## Allowed Actions

- `GET /api/external/v1/clients` — list clients
- `GET /api/external/v1/clients/{client_id}` — get a single client by ID
- Read client metadata fields (name, contact details, identifiers, associated matters)

## Disallowed Actions

- Creating, updating, or deleting client records
- Modifying contact information
- Any request using `POST`, `PUT`, `PATCH`, or `DELETE`
- Writing inferences or summaries back to Lexaro

## Inputs (Typed)

- `client_id`: string (optional; omit to list all)
- `page`: integer (optional)
- `per_page`: integer (optional)

## Outputs (Typed)

- `source_system`: string — always `"Lexaro"`
- `source_object_type`: string — always `"client"`
- `source_object_id`: string — Lexaro native client ID
- `retrieved_at`: string — ISO 8601
- `endpoint`: string — API endpoint called
- `fields`: object — normalized client metadata

## Required Logs

- Endpoint called
- HTTP status code
- Request latency (ms)
- Number of records returned
- Success or failure flag

## Approval Mode

- Auto when request stays within approved read boundary for clients.

## Boundary Rules

- HTTP method must be `GET`. No other method is permitted.
- Credentials must be loaded from environment only.
- Secrets must never appear in logs or output.
- Retrieved data must include provenance block.
- This capability is blocked pending resolution of Lexaro server-side bug (PRO-026 §6).
