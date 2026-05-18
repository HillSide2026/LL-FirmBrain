# CLAUDE.md — Agent Instructions for ll-secondbrain_fresh

## Integration and Tool Access Rules

### MCP Servers

Two MCP servers are registered for this repo. Both appear in `.mcp.json` (project-level) and in `.claude/settings.json` (local settings with hooks):

| Server | Script | Purpose |
|--------|--------|---------|
| `gmail` | `scripts/gmail_mcp_server.py` | Read Gmail inbox; controlled label writes |
| `sharepoint` | `scripts/sharepoint_mcp_server.py` | Read SharePoint folder/item metadata |

`.claude/settings.json` additionally defines the `PreToolUse` hook that validates all Write/Edit operations via `scripts/validate_canonical_write.py`. This is the only intentional split between the two config files.

**Before claiming a tool is unavailable**, use ToolSearch to check whether it loaded. If a tool is missing, check `.mcp.json` — do not assume it does not exist.

Full tool surface documented in:
- `00_SYSTEM/integrations/gmail/README.md`
- `00_SYSTEM/integrations/sharepoint/README.md`

### Gmail / Inbox

- **Gmail inbox** = `Matthew@levinelegalservices.com`, accessed via the `gmail` MCP server (`list_messages`, `get_message`, `list_threads`, `get_thread`)
- **09_INBOX** = ML2's in-tray pipeline for processed data (SharePoint metadata, drive sync, etc.) — this is NOT the Gmail inbox
- Never conflate these two. When asked to check the inbox, use the Gmail MCP.

### SharePoint

- The SharePoint MCP provides **folder and item metadata only** — it cannot read file content
- Locally synced raw files exist only for the Stream matter (`09_INBOX/_sources/sharepoint/raw/legalmatters_library/LL Matters (Essential)/24-682-00003 -- Stream`)
- The authoritative map of what is in SharePoint is: `09_INBOX/_sources/sharepoint/raw/legalmatters/phase2_enumeration.json`
- For all other matters, use `list_folder` via SharePoint MCP to enumerate live — do not assume files are missing because they are not locally synced

---

## Matter Index Governance

`05_MATTERS/INDEX.md` is updated on explicit ML1 instruction only. Do not modify it as part of any automated pipeline or housekeeping task.

## Personal Actions Governance

`04_INITIATIVES/HillSide_PORTFOLIO/PERSONAL_PROJECTS/PERSONAL_ACTIONS/` is maintained
by the system subject to ML1 override. Flow: `BACKLOG.md` → `ACTIVE_LIST.md` → `COMPLETED_LOG.md`.

**Session capture rule:** During any session, if ML1 mentions a personal to-do,
appointment, follow-up, or action item that is not a Levine Law matter task, add it
to `BACKLOG.md` immediately without waiting to be asked. Tag it to an existing
HillSide project where one exists.

**Gmail capture rule:** When reading Gmail in any context, flag personal action items
that are not Levine Law tasks — appointments, advisor follow-ups, personal
obligations — and add them to `BACKLOG.md`. Do not add LL Legal Tasks, LL Admin
Tasks, or LL Firm Management Tasks here; those belong in the LL Actions layer.

**Promotion:** Move items from `BACKLOG.md` to `ACTIVE_LIST.md` only on ML1
instruction. Do not auto-promote.

---

## LL Actions Hub

`05_MATTERS/LL_ACTIONS/README.md` is the firm-wide task index for Levine Law.
Use `LL Task` as the umbrella term. Avoid the obsolete category name that
described the work by professional role rather than by LL work type.
LL Tasks may be `LL Legal Task`, `LL Admin Task`, or `LL Firm Management Task`.
The hub references (but does not replace) the constituent artifacts:
`LL_TASK_TRACKER.md` and the marketing content backlogs. Gap artifacts are
created only on ML1 instruction.

---

## LL Task Tracker Governance

`05_MATTERS/LL_TASK_TRACKER.md` is maintained by the system subject to ML1 override.

- When ML1 marks a task as Done, move it to the Completed section. Do not delete it.
- Before adding any new task, check the Completed section. If the same task has already been completed on this matter, do not recreate it. A follow-up task is a new task with a distinct description — it is not the same task.
- Tasks are added by the system when ML1 directs it. Do not infer or auto-generate tasks from emails or other sources without ML1 instruction.

---

## Canonical Artifact Location Map

Use this map to locate controlling artifacts. When in doubt about which artifact governs a question, start here.

### ML2 — System of Record

| Directory | What lives here | Index / Entry point |
|---|---|---|
| `01_DOCTRINE/` | All doctrine: invariants, principles, policies, protocols, capability profiles, procedural rules, SLAs, KPIs | `01_DOCTRINE/index.yaml` |
| `01_DOCTRINE/01_INVARIANTS/` | Hard structural rules — highest authority tier within ML2 | `INV-0008-authority-hierarchy-ml1-ml2-system-ll.md` for the authority model |
| `01_DOCTRINE/03_POLICIES/` | Operational policies governing system and agent behavior | `index.yaml` for full list |
| `01_DOCTRINE/05_PROTOCOLS/` | Enforcement and compliance check protocols | `index.yaml` for full list |
| `02_PLAYBOOKS/` | Practice area playbooks and solution frameworks | No master index — navigate by practice area subfolder |
| `02_PLAYBOOKS/FINANCIAL_SERVICES/` | Financial services market structure, RPAA doctrine, FOPs | `MARKET_STRUCTURE_FRAMEWORK.md` |
| `03_TEMPLATES/` | Approved output templates | Navigate by template type |
| `05_MATTERS/` | All active matter records | `05_MATTERS/DASHBOARDS/MATTER_INDEX.md` |
| `06_RUNS/` | Agent run outputs, portfolio reports, ops data | Navigate by run folder |
| `07_REFERENCE/` | External references and reference materials | `07_REFERENCE/INDEX.md` (sparse) |
| `08_RESEARCH/` | Research notes and legal research | Navigate by practice area subfolder |

### The System — Execution Layer

| Directory | What lives here |
|---|---|
| `agents/` | Agent skill.md files and workflow specs — each agent lists its controlling ML2 artifacts |
| `scripts/` | MCP servers, automation scripts, validation scripts |
| `09_INBOX/` | Intake pipeline stages (_sources → 00_UNTRIAGED → 01_CLASSIFIED_PROPOSALS → 02_NEEDS_HUMAN → 03_REJECTED_NOISE → 04_HISTORY) |
| `00_SYSTEM/` | Integration documentation, retrieval bundles, system configuration |

### Initiatives and Portfolio

| Directory | What lives here |
|---|---|
| `04_INITIATIVES/LL_PORTFOLIO/` | All firm portfolio projects: portfolio management, marketing, operations |
| `04_INITIATIVES/LL_PORTFOLIO/08_MARKETING/04_FUNNELS/` | Funnel definitions (funnel-01 active, funnel-02 planned, funnel-03 payments/MSB) |
| `04_INITIATIVES/HillSide_PORTFOLIO/` | HillSide business project portfolio |

### Status vocabulary

| Status value | Meaning |
|---|---|
| `approved` | ML1-approved — the single authoritative status for all in-force doctrine, playbooks, and artifacts. `active` was a prior vocabulary variant; it has been unified to `approved`. |
| `draft` | Not yet approved — do not treat as authoritative |
| `superseded` | Replaced by a newer artifact — do not use |

### Output classification (ML1-approved 2026-04-18)

| Output source | Classification |
|---|---|
| Portfolio management agents (LLM-001 through LLM-006): portfolio briefs, decision queues, health rollups | **Internal working material** — not for LL consumption |
| Practice area agents: outputs produced in `05_MATTERS/` | **LL consumable** |

**LL consumption labeling standard:** To be determined. No structural output labeling mechanism exists yet. This is an open item pending ML1 definition.
