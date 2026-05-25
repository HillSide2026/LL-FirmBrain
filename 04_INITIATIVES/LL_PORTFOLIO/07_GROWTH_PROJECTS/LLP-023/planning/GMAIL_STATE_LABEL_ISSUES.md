---
id: llp_023__gmail_state_label_issues
title: Gmail State Label Issues — Working Notes
owner: ML1
status: open
created_date: 2026-05-05
last_updated: 2026-05-05
tags: [gmail, labels, inbox, slice-1, issues]
---

# Gmail State Label Issues — Working Notes

Captured from ML1 session 2026-05-05.

---

## Trigger

During a search for an email related to **Star 333**, the system failed to surface
the email. Root cause identified: the search was operating at the **thread level**,
not the message level. The email existed but was not found because thread-level
search does not resolve all individual messages within a thread.

Star 333 has two active matters in Clio. The thread-level search could not
distinguish between them:

| Matter | Description | Status |
|---|---|---|
| `24-845-00001` | Corporate / Commercial Matters (ML1 to correct description in Clio) | Pending / Active |
| `25-845-00002` | League Operational Matters | Confirmed / Active |

---

## State Labels — Confirmed

There are **10 state labels** in Gmail. (Earlier reference to 9 was a ML1
correction.)

| Label | Count (2026-05-05) |
|---|---|
| `00_Triage` | 332 |
| `10_Action_Matthew` | 87 |
| `20_Action_Team` | 19 |
| `30_Waiting_External` | — |
| `40_Replied_Awaiting_Response` | — |
| `50_Calendar` | 216 |
| `60_Filing` | 8 |
| `70_Filed` | — |
| `80_Junk_to_Review` | 7 |
| `90_Archive` | 111 |

**Rule:** Every email must be assigned to at least one state label.

**Corollary:** Any email that carries a state label must not remain in the inbox.
Inbox presence + state label = a contradiction.

---

## Two Problems Identified

### Problem 1 — Inbox Contamination

Many emails carry a state label but remain in the inbox.

This violates the corollary above. The inbox should contain only emails that have
not yet been assigned a state label. Emails with state labels sitting in the inbox
create false positive inbox counts and obscure the true triage backlog.

### Problem 2 — Inaccurate State Labels

Some emails carry state labels that do not accurately reflect their actual state.

The label-write history cannot be relied upon without verification. Any batch
review or routing pass must treat existing state labels as **candidate truth, not
settled truth**, until a verification layer is in place.

---

## Three-Pass Remediation Plan

### Pass A — Inbox Contamination (approved to plan; execute pending ML1 batch approval)

**Logic:** Any thread that is `in:inbox` AND carries any state label is a
contradiction. Archive it (remove inbox flag only — no relabeling, no deletion).

**Steps:**

1. **Audit query (read-only)**
   Gmail search per label: `in:inbox label:<state_label>` for all 10 labels.
   Output: thread count + thread list with current labels and subjects.

2. **Proposal artifact**
   Write to `06_RUNS/batch/proposals/YYYY-MM-DD_inbox_contamination.json`.
   Fields: thread_id, subject, current_labels, proposed_action (`archive`).
   No Gmail writes at this step.

3. **ML1 review**
   ML1 reviews proposal. Flag any threads to exclude. Approve remainder.
   Approval artifact written to `06_RUNS/` before execution.

4. **Execution with audit trail**
   Archive approved threads. Write execution record to
   `06_RUNS/batch/executions/YYYY-MM-DD_inbox_contamination.json`.
   Archiving removes the inbox flag only — labels are preserved.

---

### Pass B — Label Accuracy (planned; scope to be defined before execution)

**Logic:** Some emails carry state labels that do not accurately reflect their
actual state. Existing labels are candidate truth, not settled truth.

Priority order for review: `10_Action_Matthew` (87 threads — highest operational
impact if mislabeled), then `20_Action_Team`, then others by count.

This pass requires human judgment. Automation can surface candidates; ML1 makes
the call on each correction.

---

### Pass C — Party Extraction (planned; runs on matter-tagged threads)

**Logic:** For all emails or threads tagged to a matter label, extract all
relevant parties — including non-clients. Parties include senders, recipients,
CC'd parties, and any named individuals in the thread.

**Purpose:** Build a complete participant map per matter from Gmail communications.
This supplements Clio contact records with parties who appear in email but are
not formally registered as Clio contacts (opposing counsel, third parties,
advisors, etc.).

**Scope:** All threads carrying a matter label (not state labels — matter labels
are the Clio matter number labels applied to routed threads).

**Output:** Per-matter party roster, flagging any party not matched to a known
Clio contact on that matter.

This pass can run independently of Pass A and Pass B — it operates on
already-labeled matter threads, not on inbox state.

---

## Open Items

- Full label name confirmed: `40_Replied_Awaiting_Response`.
- ML1 to update `24-845-00001` description in Clio to "Corporate / Commercial Matters"
  (simpler canonical name).
- Pass A: run audit query (Step 1) when ML1 is ready to proceed.
- Pass B: define review scope and sampling approach before starting.
- Pass C: define output schema and destination before starting.
