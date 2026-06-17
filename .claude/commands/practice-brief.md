---
name: practice-brief
description: Generate a prioritized daily practice brief across all Essential, Strategic, and Standard delivery matters for ML1. Surfaces what requires ML1 action today vs what is delegated to fulfillment, with next steps, blockers, and due dates per matter. Writes DAILY_BRIEF.md to 05_MATTERS/DASHBOARDS/. Use whenever ML1 asks for a daily rundown, morning brief, practice overview, what to work on today, what's open across matters, or a status sweep across the practice — triggered by phrases like "what do I need to work on today", "give me a practice brief", "morning brief", "what matters need my attention", "run through my active matters", or "what's the state of the practice".
---

# Practice Brief

Generates a prioritized daily ML1 brief across all Essential, Strategic, and Standard delivery matters. Grounded in LLP-023 (Matter Command and Control). Produces a two-layer output: **ML1 Action Required** and **ML1 Visibility**, ordered by delivery tier.

---

## Step 1 — Load the Matter List

Read both of the following. For each, read the `generated:` field from YAML frontmatter — this is the machine-readable freshness signal. Surface the value and the age in the Source Log so ML1 can judge currency.

- `05_MATTERS/DASHBOARDS/MATTER_DIGEST.md` — read `generated:` from frontmatter; use its **ML Active Queue** table as the primary matter list
- `05_MATTERS/DASHBOARDS/MATTER_INDEX.md` — read `generated:` from frontmatter; use as a cross-check

Use both. If the Digest's ML Active Queue and the Index disagree on which matters are open, surface both and flag the discrepancy in the Source Log — do not silently pick one.

From the combined list, keep only matters where `Delivery` is Essential, Strategic, or Standard and `Status` is Open. For each, record: `matter_id`, `matter_name`, `delivery_status`, `fulfillment_status`.

---

## Step 2 — Read the Task Tracker

Read `05_MATTERS/LL_TASK_TRACKER.md` — the **Active Tasks** section. Read `last_reviewed:` from its YAML frontmatter — this is the freshness signal for the tracker. Surface the value in the Source Log.

For each matter in your working list, collect:
- Open LL Legal Tasks, LL Admin Tasks, or LL Firm Management Tasks tagged to that matter
- Task description, status (Open / In Progress / Waiting), and due date if present
- For Waiting tasks, note who the task is waiting on

An Open or In Progress task means ML1 owns the next move. A Waiting task means the ball is in another party's court — identify who.

---

## Step 3 — Read Per-Matter Status Files (Essential Tier Only)

For Essential tier matters, read `MATTER_STATUS.md` in the matter folder if it exists. Read `generated:` from its YAML frontmatter — surface the value in the Source Log. Extract current posture and any recorded blockers.

For Strategic and Standard matters, the task tracker and matter index are sufficient for the brief unless a matter has an urgent `fulfillment_status` flag — in that case, read its status file too.

---

## Step 4 — Gmail Signal Check (Targeted)

Run targeted Gmail queries to check for recent activity on the highest-priority matters.

**Query A — All Essential matters:**
```
after:YYYY/MM/DD (<client-name-1> OR <client-name-2> OR ...)
```

**Query B — Matters with Open or In Progress tasks:**
```
after:YYYY/MM/DD (<client-name-1> OR <client-name-2> OR ...)
```

Use `after:YYYY/MM/DD` where the date is 7 days before today. Use `max_results: 10` per query. The snippet stubs are enough — do not fetch full thread content for the brief.

For each result, map it to a matter and record the most recent message date. This surfaces which matters have had recent communication and which have gone quiet.

---

## Step 5 — Classify Each Matter

For each matter, decide which layer it belongs in using these rules:

**ML1 Action Required** — place here when ANY of the following is true:
- There is an Open or In Progress LL Task where ML1 is the actor
- `fulfillment_status` recorded in the source files is `urgent`
- Matter is Essential tier and there has been no Gmail signal in the last 7 days
- A Waiting task is explicitly waiting on ML1 (not a third party)

**ML1 Visibility** — place here when:
- No Open or In Progress ML1-owned task exists
- All Waiting tasks are waiting on a third party (client, counterparty, registry, government body)
- `fulfillment_status` is not `urgent`

Within each layer, order matters: Essential first, then Strategic, then Standard. Within a tier, matters with the earliest due dates appear first; matters with no due date follow.

---

## Step 6 — Write the Brief

Respond in conversation with the brief. Also write it to `05_MATTERS/DASHBOARDS/DAILY_BRIEF.md` (overwrite any previous version).

Use this structure:

```markdown
---
id: DASHBOARDS-DAILY-BRIEF
title: Practice Brief — <YYYY-MM-DD>
owner: ML1
status: draft
generated: <ISO-8601 timestamp>
---

# Practice Brief — <YYYY-MM-DD>

## ML1 Action Required

| # | Matter | Tier | Fulfillment Status | Next Action | Due | Waiting On |
|---|---|---|---|---|---|---|
| 1 | [matter name] ([matter-id]) | Essential | [value from source] | [what ML1 needs to do] | [date or —] | ML1 |

## ML1 Visibility

| Matter | Tier | Fulfillment Status | Last Signal | Posture |
|---|---|---|---|---|
| [matter name] ([matter-id]) | Strategic | [value from source] | [date or unknown] | [one-line posture] |

## Source Log

| Source | `generated:` / `last_reviewed:` | Notes |
|---|---|---|
| MATTER_DIGEST.md | [frontmatter generated: value] | [N matters in ML Active Queue] |
| MATTER_INDEX.md | [frontmatter generated: value] | [N matters loaded] |
| LL_TASK_TRACKER.md | [frontmatter last_reviewed: value] | [N open tasks across N matters] |
| MATTER_STATUS.md files | [frontmatter generated: per file] | [N files read for Essential/urgent matters] |
| Gmail | Live — [date queried] | [Last 7 days; N threads matched] |
| Calendar | ⏳ Pending integration | |
| Lexaro | ⏳ Pending integration | |
```

---

## Behavior Rules

- **Never fabricate a next action.** If the sources don't identify what ML1 needs to do, write: "No recorded next action — check matter folder."
- **Surface source dates, not freshness judgments.** Report what date each source records; let ML1 decide if that's current enough to act on.
- **`fulfillment_status` is a source field, not a priority rank.** Show its value as recorded in the source file; do not use it to label your own ordering scheme.
- **Essential matters always appear.** Never omit an Essential tier matter, even if there is no current signal.
- **Waiting tasks belong in the right column.** A task waiting on a client is not ML1's action — surface who is blocking and keep the matter in Visibility unless a due date is approaching.
- **Keep rows short.** The brief is a decision surface. One line per matter. Use `/matter-overview` for depth.
