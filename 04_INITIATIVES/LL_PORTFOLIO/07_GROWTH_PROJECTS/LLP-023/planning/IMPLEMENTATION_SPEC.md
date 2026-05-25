---
id: 04_initiatives_ll_portfolio_07_growth_projects_llp_023_matter_command_control_planning_implementation_spec_md
title: Implementation Spec
owner: ML1
status: draft
created_date: 2026-05-18
last_updated: 2026-05-18
tags: []
---

# Implementation Spec

## 1) Target Daily Outputs

- Firm Matter Digest: what moved, what is stuck, what is due
- Firm Matter Digest split so it is clear:
  - what remains visible to ML1
  - what requires ML1 action now
  - what remains delegated to fulfillment
  - what counts as fulfillment escalation
- Per-matter Work Packet baseline (Slice 1 includes status + comm routing)
- Exception lists: unmapped inbox, mapping gaps
- Bounded Gmail review pass: review up to `25` threads and move each reviewed
  thread into exactly one canonical state label through the governed label-write
  path
- Batch proposal artifact for the reviewed Gmail pass in
  `06_RUNS/batch/proposals/`
- Batch execution artifact in `06_RUNS/batch/executions/` when ML1 approval is
  present and label execution is run

## 2) Canonical System Rules

- Clio = matter registry authority
- SharePoint = document authority
- Gmail = communication authority
- ML2 stores only derived/admin artifacts + source pointers
- Every generated assertion must include a source pointer

## 3) Deterministic Paths

Active implementation paths:

- `05_MATTERS/DASHBOARDS/MATTER_DIGEST.md`
- `05_MATTERS/DASHBOARDS/MATTER_INDEX.md`
- `05_MATTERS/DASHBOARDS/INBOX_UNMAPPED.md`
- `05_MATTERS/<tier>/<matter_id>/MATTER_STATUS.md` (generated for routed matters)
- `06_RUNS/batch/proposals/*.json`
- `06_RUNS/batch/executions/*.json`
- `cache/*.json` snapshots for connector normalization and run state

## 4) Connector Normalization Contracts

### Clio -> MatterRef
`{ clio_matter_id, matter_number, name, status, responsible, client, source_pointer }`

### Gmail -> ThreadRef
`{ thread_id, subject, participants, last_message_at, labels, latest_snippet, source_pointer }`

### SharePoint -> DocRef (Slice 2)
`{ drive_item_id, path, name, modified_at, size, web_url, source_pointer }`

## 5) Matter Resolution Rules

Primary key: Clio matter number.

Routing order:
1. Gmail label path contains matter number (canonical)
2. Subject/snippet fallback contains matter number (review-required)
3. Otherwise route to `INBOX_UNMAPPED.md`

SharePoint mapping:
- Prefer deterministic folder naming with leading matter number
- Use `05_MATTERS/_REGISTRY/matter_sharepoint_map.yml` for explicit overrides

## 5A) ML1 Triage Rules

Durable matter attributes remain:

- `delivery_status`
- `fulfillment_status`

The command layer must not overwrite those durable attributes with a shadow
classification. Instead, it computes a narrower ML1-action layer using:

- `next_ML1_decision_required`
- `decision_due_date`
- `decision_age_days`
- `blocking_actor`
- `inactivity_days`

Interpretive rules:

- `delivery_status` answers durable ML1 relevance and delivery importance.
- `fulfillment_status` answers delegated fulfillment operating posture.
- `next_ML1_decision_required` answers whether ML1 judgment is required now.
- `decision_due_date` is the primary timeliness anchor for ML1 action.
- `decision_age_days` measures unresolved ML1 decision aging.
- `blocking_actor` identifies who presently owns the blockage.
- `inactivity_days` is a drift signal only and does not by itself create ML1
  action.
- Ordinary fulfillment handling remains delegated.
- Only fulfillment escalation belongs in the ML1-action layer.

## 6) Agent Responsibilities (Operational)

1. Matter Index Agent
2. Inbox to Matter Router
3. Deadline Extractor (Slice 3)
4. Document Delta Agent (Matter File Admin / Slice 2)
5. Comms Drafting Agent (Slice 4)
6. Matter Digest Compiler

## 7) Orchestration Modes

- `RUN_MATTER_ADMIN_DAILY`
- `RUN_MATTER_ADMIN_ONE(matter_number)`

Daily mode review cap:
- default Gmail review scope is `25` threads per pass
- set the runner cap explicitly only when ML1 wants a narrower or broader pass

## 8) Managed Config Files

Under `00_SYSTEM/CONFIG/`:

- `systems_of_record.yml`
- `matter_folder_rules.yml`
- `gmail_label_rules.yml`
- `deadline_taxonomy.yml`
- `run_schedule.yml`

## 9) Snapshot Store

- `cache/clio_matters.json`
- `cache/gmail_threads.json`
- `cache/sharepoint_files.json`
- `cache/run_state.json`

## 10) Delivery Slices

- Slice 1: matter index + Gmail routing + digest/unmapped
- Slice 2: Matter File Administration document index + deltas
- Slice 3: deadline extraction + radar
- Slice 4: comms draft packets
