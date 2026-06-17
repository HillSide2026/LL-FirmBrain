---
id: 00_system__integrations__gmail__readme_md
title: Gmail Integration
owner: ML1
status: active
version: 3.0
created_date: 2026-02-15
last_updated: 2026-06-17
tags: [integration, gmail, mcp]
---

# Gmail Integration

Status (index): active

## Contract

- `gmail_sources.yaml`

## Architecture

Two MCP servers handle Gmail. Together they cover the full read/write surface with
governed writes separated from raw reads.

| Server | Name in config | Purpose |
|--------|---------------|---------|
| Google-managed remote MCP | `claude_ai_Gmail` | Read operations — search, retrieve, list labels |
| Local governance MCP | `gmail` | Write operations — state/matter labelling, bulk cleanup, draft creation |

The official Google server (`gmailmcp.googleapis.com/mcp/v1`) is registered through
Claude.ai Connectors and is always available as `mcp__claude_ai_Gmail__*` tools.
The local governance server runs from `scripts/gmail_mcp_server.py` and is registered
in `.mcp.json`.

## Read Tools (Official Google MCP — `mcp__claude_ai_Gmail__*`)

| Tool | Operation |
|------|-----------|
| `search_threads` | Search threads by Gmail query syntax. `pageSize` max 50. |
| `get_thread` | Fetch one thread by `threadId`. Use `messageFormat: FULL_CONTENT` for body. |
| `list_labels` | List all user-defined labels. System labels (`INBOX`, `TRASH`, etc.) are well-known IDs. |
| `list_drafts` | List draft messages. |
| `create_label` | Create a new label. |
| `delete_label` | Delete a label. |
| `update_label` | Update label name or visibility. |
| `label_thread` | Apply a label to a thread (raw — no governance enforcement). |
| `unlabel_thread` | Remove a label from a thread (raw). |
| `label_message` | Apply a label to an individual message. |
| `unlabel_message` | Remove a label from an individual message. |
| `create_draft` | Create a draft (raw — no approval gate). |

## Write Tools (Governance MCP — `mcp__gmail__*`)

All governance write tools require `approved_by`, `approval_artifact`, and `reason`.
Writes are audited to `06_RUNS/ops/gmail_mcp_audit.ndjson`.

| Tool | Operation | Write |
|------|-----------|-------|
| `apply_state_label` | Apply one canonical state label to a thread with mutual exclusion | Yes |
| `apply_matter_label` | Apply one canonical matter label to a thread with mutual exclusion | Yes |
| `apply_matter_label_query` | Apply matter label to all threads matching a query | Yes |
| `create_draft` | Create a governed draft with approval gate | Yes |
| `preview_inbox_cleanup` | Preview PRO-018 cleanup counts | No |
| `execute_inbox_cleanup` | Execute PRO-018 TRASH/ARCHIVE sender cleanup | Yes |
| `execute_category_sweep` | Archive soft-junk category threads before cutoff date | Yes |
| `preview_garbage_candidates` | PRO-014 classifier in proposal mode | No |
| `resolve_confirmed_junk_threads` | Promote confirmed junk to `90_Archive` | Yes |
| `pass_a_archive_threads` | Remove INBOX from contaminated threads | Yes |

## Controlled Write Policy

- Default posture is proposal-first.
- Governance write tools enforce mutual exclusion on state and matter labels.
- Every write tool call must include: `approved_by`, `approval_artifact`, `reason`.
- Gmail MCP write audits are appended to: `06_RUNS/ops/gmail_mcp_audit.ndjson`.

## Operations NOT Permitted via MCP

- Send mail (permanently prohibited — POL-042 §7)
- Delete, trash, or untrash (use inbox cleanup tools instead)
- Broad mailbox mutation beyond controlled thread label writes

## Canonical State Labels

```
00_Triage | 10_Action_Matthew | 20_Action_Team | 30_Waiting_External
40_Replied_Awaiting_Response | 50_Calendar | 60_Filing | 70_Filed
80_Junk_to_Review | 90_Archive
```

## Governance Server Registration

Registered in `.mcp.json` (project root).
Server process: `scripts/gmail_mcp_server.py`.
Auth: Gmail OAuth token from `00_SYSTEM/local_secrets/google_token.json`.

## Change Notes

- v1.0 2026-02-15: Integration stub created.
- v2.0 2026-03-14: Gmail MCP server implemented for interactive use.
- v3.0 2026-06-17: Split into two-server architecture. Read operations migrated to
  official Google-managed Gmail MCP (`claude_ai_Gmail`). Custom server retained for
  governance writes only. Read tools removed from `scripts/gmail_mcp_server.py`.
