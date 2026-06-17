---
name: matter-overview
description: Generate a live matter overview for any Levine Law matter at the Essential, Strategic, or Standard delivery tier. Pulls from repo artifacts (MATTER.yaml, MATTER_BRIEF.md, MATTER_STATUS.md, LL_TASK_TRACKER.md), Gmail (last 30 days), and SharePoint document inventory. Writes MATTER_OVERVIEW.md to the matter folder. Use this whenever ML1 asks for a briefing, status, or overview on a specific matter — triggered by phrases like "brief me on X", "what's the status on Y", "overview of the Boparai matter", "pull together a matter summary for [client]", "update me on [matter-id]", or when ML1 opens a matter folder and wants a current picture of the file.
---

# Matter Overview

Generates `MATTER_OVERVIEW.md` for a single matter by pulling every available live source into one synthesized snapshot. Scoped to **Essential, Strategic, and Standard** delivery tiers.

---

## Step 1 — Identify the Matter

Determine the target from the user's input:

- **Matter number** (format `YY-NNNN-NNNNN`): look for a matching folder under `05_MATTERS/ESSENTIAL/`, `05_MATTERS/STRATEGIC/`, or `05_MATTERS/STANDARD/`.
- **Keyword / client name**: search `05_MATTERS/DASHBOARDS/MATTER_INDEX.md` for matching rows. If more than one match, list the candidates and ask ML1 to confirm before proceeding.
- **Current directory**: if already inside a matter folder, use that matter.

Once located, read `MATTER.yaml`. Extract: `matter_id`, `matter_name`, `client_name`, `instructing_officer_name`, `delivery_status`, `fulfillment_status`, `practice_area`, `engagement_date`, and `services`.

**Halt conditions:**
- MATTER.yaml is missing → surface the expected path, ask ML1 to confirm the matter ID.
- `delivery_status` is Normal or Other → this skill does not apply to those tiers. Tell ML1 and stop.

---

## Step 2 — Read Repo Artifacts

Read whatever is present in the matter folder. Note gaps in the Source Log; do not halt for missing optional files.

| File | Required | Notes |
|---|---|---|
| `MATTER.yaml` | Yes | Identity fields; Step 1 already reads this |
| `MATTER_BRIEF.md` | No | Narrative brief and current posture |
| `MATTER_STATUS.md` | No | Latest status snapshot — check the `generated` date; it may be stale |
| `FACTS_TIMELINE.md` | No | Factual timeline |
| `ISSUES_AND_POSITIONS.md` | No | Open issues and party positions |
| `NOTES_TO_FILE.md` | No | Solicitor notes |

Also scan `05_MATTERS/LL_TASK_TRACKER.md` for open or recently completed tasks whose text contains this matter ID or client name.

---

## Step 3 — Gmail (Last 30 Days)

Call `mcp__gmail__list_threads` with:
- `max_results: 20`
- `query`: `after:YYYY/MM/DD (<matter-id> OR "<client-name>" OR "<instructing-officer-name>")`

Compute `YYYY/MM/DD` as 30 calendar days before today. Use the actual names from MATTER.yaml — quote multi-word names.

For each returned thread, call `mcp__gmail__get_thread` with `thread_id` to get subject, date, key participants, and a brief characterization of the most recent message (first 200 characters of body text is enough — do not quote long passages).

If the Gmail MCP is unavailable, skip this section and note the gap.

---

## Step 4 — SharePoint Document Inventory

Map `delivery_status` from MATTER.yaml to the SharePoint parent folder:

| Delivery Status | SharePoint Parent Path |
|---|---|
| Essential | `LL Matters (Essential)` |
| Strategic | `LL Matters (Strategic)` |
| Standard | `LL Matters (Standard)` |

Call `mcp__sharepoint__list_folder` with `drive: "legalmatters"` and `path: "<parent path>"`. Scan the returned items for a folder whose name begins with this matter's ID. If found, call `list_folder` again on that subfolder to enumerate its contents one level deep.

For Standard tier matters, if not found in `LL Matters (Standard)`, also check `LL Matters (Standard Cash Cows)`.

If SharePoint MCP is unavailable or the folder is not found, note the gap in the Source Log.

---

## Step 5 — Calendar and Lexaro (Placeholders)

- **Google Calendar**: integration is not yet active. Record "pending" in the Source Log.
- **Lexaro**: API connectivity in progress (server-side bug open with Lexaro support). Record "pending" in the Source Log. When resolved, this step will query `/api/external/v1/matters/<id>` for live matter status, tasks, and documents from Lexaro.

---

## Step 6 — Write MATTER_OVERVIEW.md

Write to `05_MATTERS/<TIER>/<matter-id>/MATTER_OVERVIEW.md`. Use the template below exactly — it includes the frontmatter fields required by the canonical write validator.

```markdown
---
id: MATTER-<matter-id>-OVERVIEW
title: Matter Overview — <matter-id> — <matter-name>
owner: ML1
status: draft
generated: <ISO-8601 timestamp>
sources_live: [repo, gmail, sharepoint]
sources_pending: [calendar, lexaro]
---

# Matter Overview — <matter-id>
## <matter-name>
**Generated:** <human-readable date and time>

---

## 1. Matter Identity

| Field | Value |
|---|---|
| Matter ID | |
| Client | |
| Instructing Officer | |
| Practice Area | |
| Delivery Tier | |
| Fulfillment Status | |
| Engagement Date | |

**Services on file:**

<bulleted list from MATTER.yaml services array>

---

## 2. Current Brief

<3–5 sentence narrative drawn primarily from MATTER_BRIEF.md. If MATTER_BRIEF.md is absent, synthesize from MATTER.yaml fields alone and append [BRIEF MISSING — synthesized from MATTER.yaml].>

**Current posture:** <one sentence on where the matter stands as of the generated date>

---

## 3. Active LL Tasks

<List each open task from LL_TASK_TRACKER.md whose text references this matter ID or client name. Include task type, description, and any noted deadline. If none found: "No open tasks found in tracker.">

---

## 4. Recent Email Activity (Last 30 Days)

<For each Gmail thread found, one row: Date | Subject | Participants | One-line summary of latest message>

_No Gmail threads found in last 30 days._ (use this line if the query returned nothing)

---

## 5. Documents on File (SharePoint)

**SharePoint path:** `legalmatters / <parent folder> / <matter subfolder>`

<Bulleted list of files and subfolders found, with last-modified date where available. For files: name, extension, last modified. For subfolders: name and item count.>

_SharePoint folder not found at expected path._ (use this line if the folder was missing or MCP unavailable — flag as [GAP])

---

## 6. Calendar

Google Calendar integration pending. No calendar data available.

---

## 7. Lexaro

Lexaro integration in progress (API bug open with Lexaro support). No live data available.

---

## 8. Synthesized Posture

<2–4 sentences synthesizing what the combined sources tell you about this matter's current state: what is actively in motion, what the key blockers or open items are, and what the most pressing next action appears to be. Base this strictly on what the sources show — do not speculate beyond the evidence.>

---

## Source Log

| Source | Status | Detail |
|---|---|---|
| MATTER.yaml | ✓ | |
| MATTER_BRIEF.md | ✓ Present / ✗ Missing | |
| MATTER_STATUS.md | ✓ Found, dated <date> / ✗ Missing | Note if stale |
| FACTS_TIMELINE.md | ✓ / ✗ | |
| ISSUES_AND_POSITIONS.md | ✓ / ✗ | |
| LL_TASK_TRACKER.md | ✓ Checked | N tasks found |
| Gmail | ✓ Live — N threads / ✗ Unavailable | Last 30 days |
| SharePoint | ✓ Live — N items / ✗ Not found | |
| Calendar | ⏳ Pending integration | |
| Lexaro | ⏳ Pending integration | |
```

---

## Output Requirements

- Write to `05_MATTERS/<TIER>/<matter-id>/MATTER_OVERVIEW.md` — no other location.
- Always include `generated` timestamp in frontmatter.
- Always include the Source Log — ML1 needs to know which sources were live vs. pending.
- `status: draft` always, unless ML1 explicitly approves it.
- The canonical write validator requires `status:` and `owner:` in frontmatter — both are in the template.
