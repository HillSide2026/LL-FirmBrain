---
id: lexaro.list_tasks
title: 'Capability Profile: Lexaro.ListTasks'
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
tags: [lexaro, capability, read-only, tasks]
policy: POL-066
protocol: PRO-026
---

# Capability Profile: Lexaro.ListTasks (v0.1)

## Purpose

Retrieve task metadata and task states from Lexaro for observational use by ML2.
No mutation of Lexaro state is permitted.

## Allowed Actions

- `GET /api/external/v1/tasks` — list tasks
- `GET /api/external/v1/tasks/{task_id}` — get a single task by ID
- `GET /api/external/v1/task-reminders` — list task reminders
- `GET /api/external/v1/tasks-due-soon` — list tasks due soon
- Read task metadata fields (name, status, assignee, due date, matter reference, identifiers)

## Disallowed Actions

- Creating, updating, or deleting tasks
- Changing task status or completion state
- Marking tasks complete or incomplete
- Any request using `POST`, `PUT`, `PATCH`, or `DELETE`
- Writing inferences or summaries back to Lexaro

## Inputs (Typed)

- `task_id`: string (optional; omit to list all)
- `page`: integer (optional)
- `per_page`: integer (optional)

## Outputs (Typed)

- `source_system`: string — always `"Lexaro"`
- `source_object_type`: string — always `"task"`
- `source_object_id`: string — Lexaro native task ID
- `retrieved_at`: string — ISO 8601
- `endpoint`: string — API endpoint called
- `fields`: object — normalized task metadata

## Required Logs

- Endpoint called
- HTTP status code
- Request latency (ms)
- Number of records returned
- Success or failure flag

## Approval Mode

- Auto when request stays within approved read boundary for tasks.

## Boundary Rules

- HTTP method must be `GET`. No other method is permitted.
- Credentials must be loaded from environment only.
- Secrets must never appear in logs or output.
- Retrieved data must include provenance block.
- This capability is blocked pending resolution of Lexaro server-side bug (PRO-026 §6).
