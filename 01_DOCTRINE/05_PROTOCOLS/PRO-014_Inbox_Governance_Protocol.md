---
id: PRO-014
title: Inbox State and Matter Management Protocol
owner: ML1
status: draft
approval: ML1
approved_by: ML1
approved_date: 2026-04-18
project: LLP-006
version: 0.4
created_date: 2026-03-07
last_updated: 2026-03-14
tags: [protocol, gmail, inbox, labeling, classification, legalmatters, clio]
---

# PRO-014 — Inbox State and Matter Management Protocol

Enforces Policy: POL-042

> **DRAFT — PENDING ML1 APPROVAL.**
> This protocol has not been approved and is not in effect.
> No labeling operations, batch executions, or automated classifications
> may be run under this protocol until ML1 approves and sets `status: active`.

---

## 1. Purpose

This protocol defines:

1. The canonical label taxonomy applied to Gmail threads in the LL inbox.
2. The classification decision tree used to assign state labels to threads.
3. The canonical sender lists used as classification signals.
4. The matter label structure linking threads to Clio matter records.
5. The approval gate required before any label is written to Gmail.
6. The agent access rules that govern inbox data within secondbrain.

This protocol does not govern inbox soft-junk cleanup. That is a separate inbox
admin lane governed by `PRO-018`.

**Objective:** The ultimate goal of inbox governance is to ensure that every matter-related
email is linked to its corresponding legal matter — both as a Clio matter reference and,
where applicable, as a SharePoint LegalMatters folder. This protocol operates in two phases:

- **Interim (current):** Tag emails within Gmail with the relevant legal matter / Clio matter
  number, using the label hierarchy defined in Section 4. This establishes a traceable
  matter-thread link without moving or copying email content.
- **Future:** Route or file emails from the inbox to the relevant matter record in SharePoint
  LegalMatters, once cross-system linking is in scope (see LLP-005).

The protocol applies to the Gmail account(s) associated with `matthew@levinelegal.ca`
and `matthew@levine-law.ca`. It does not govern Google Calendar, SharePoint, or
soft-junk cleanup directly (those are addressed in separate protocols or are pending).

---

## 2. Terminology

| Term | Definition |
|------|------------|
| **State label** | A canonical label expressing the action state of a thread (e.g., `10_Action_Matthew`). Only one state label may be applied to a thread at a time. |
| **Matter label** | A hierarchical label linking a thread to a Clio matter number (e.g., `LL/1./1.1/25-1593-00001 -- KaleMart`). |
| **Triage** | The process of reviewing unclassified threads and assigning state and/or matter labels. |
| **Batch proposal** | A machine-generated list of proposed label changes, not yet applied. Requires ML1 approval before execution. |
| **Execution** | Applying approved label changes to Gmail via the API. |
| **Automated sender** | A sender whose address contains: `noreply`, `no-reply`, `donotreply`, `do_not_reply`, `notifications@`, `automated@`, or `system@`. |

---

## 3. Canonical State Labels

Exactly one state label must be applied to each thread. State labels are mutually exclusive.

| Label | Meaning |
|-------|---------|
| `00_Triage` | Received; not yet reviewed. Default state for new threads. |
| `10_Action_Matthew` | Requires ML1 action. |
| `20_Action_Team` | Delegated to team member or firm admin. |
| `30_Waiting_External` | Waiting on external party (counterparty, court, government). ML1-assigned only; not auto-proposed. |
| `40_Replied_Awaiting_Response` | ML1 has replied; awaiting response. |
| `50_Calendar` | Thread is a Google Calendar notification; no separate action required. |
| `60_Filing` | Thread requires filing in SharePoint or Clio; no separate action. |
| `70_Filed` | Thread has been filed; no further action required. ML1-assigned only. |
| `80_Junk_to_Review` | Suspected low-value or junk; flagged for ML1 review within the state-management lane. |
| `90_Archive` | No further action required. |

**Enforcement rule:** Any thread carrying more than one state label is in violation.
`state_enforcement.py` detects and reports violations but does not resolve them without
ML1 approval.

**Manual-only labels:** `30_Waiting_External` and `70_Filed` are never auto-proposed.
They may only be assigned by ML1 directly.

---

## 4. Matter Label Structure

### 4.1 Canonical matter identifier

The canonical matter identifier is the **Clio matter ID**, which takes the form:

```
\d{2}-\d{3,4}-\d{5}  (e.g., 25-1593-00001)
```

This ID is the authoritative cross-system reference key linking a Gmail thread to:
- the corresponding Clio matter record, and
- the corresponding SharePoint LegalMatters folder (where implemented).

### 4.2 Label format

```
LL/1./{tier}/{clio_matter_id} -- {client_name}
```

Example: `LL/1./1.1/25-927-00003 -- Stream Ventures Limited`

### 4.3 Tier 1 delivery tiers

| Tier prefix | Delivery status | Enforcement |
|-------------|-----------------|-------------|
| `LL/1./1.1/` | Essential | Automated |
| `LL/1./1.2/` | Strategic | Automated |
| `LL/1./1.3/` | Standard | Automated |
| `LL/1./1.4/` | Parked | Manual only |

### 4.4 Canonical Tier 1 matter labels (ML Active matters)

**1.1 — Essential**

| Label | Matter |
|-------|--------|
| `LL/1./1.1/25-927-00003 -- Stream Ventures Limited` | SnowCap AML Policy Transition |
| `LL/1./1.1/26-1639-00001 -- Andersen` | Andersen matter 1 |
| `LL/1./1.1/26-1639-00002 -- Andersen` | Andersen matter 2 |
| `LL/1./1.1/26-1639-00003 -- Andersen` | Andersen matter 3 |
| `LL/1./1.1/26-927-00004 -- Stream Ventures Limited` | Stream matter 4 |

**1.2 — Strategic**

| Label | Client |
|-------|--------|
| `LL/1./1.2/24-336-00004 -- Mascore Helical Piles` | Mascore Helical Piles |
| `LL/1./1.2/25-1231-00001 -- Charmaine Spiteri` | Charmaine Spiteri |
| `LL/1./1.2/25-1318-00001 -- Zelko Culibrk` | Zelko Culibrk |
| `LL/1./1.2/25-256-00005 -- Aspire Infusions Inc` | Aspire Infusions Inc |
| `LL/1./1.2/26-1593-00002 -- KaleMart` | 1001162998 Ontario Corp. o/a KaleMart |

**1.3 — Standard**

| Label | Client |
|-------|--------|
| `LL/1./1.3/22-194-00006 -- Rousseau Mazzuca LLP` | Rousseau Mazzuca LLP |
| `LL/1./1.3/23-194-00013 -- Rousseau Mazzuca LLP` | Rousseau Mazzuca LLP |
| `LL/1./1.3/23-235-00001 -- Baobab Energy Africa Ltd` | Baobab Energy Africa Ltd |
| `LL/1./1.3/24-646-00001 -- ByNature Design` | ByNature Design |
| `LL/1./1.3/25-1185-00001 -- Alexander Klys` | Alexander Klys |
| `LL/1./1.3/25-1363-00001 -- Raevan Joy Sambrano` | Raevan Joy Sambrano |
| `LL/1./1.3/25-1525-00001 -- Kleenup Cleaning Services Inc.` | Kleenup Cleaning Services Inc. |
| `LL/1./1.3/25-1538-00002 -- Georgiana Nicoară` | Georgiana Nicoară |
| `LL/1./1.3/25-1553-00001 -- 15652227 Canada Inc.` | 15652227 Canada Inc. |
| `LL/1./1.3/25-1571-00001 -- Kishmish Inc.` | Kishmish Inc. |
| `LL/1./1.3/25-1588-00001 -- Gregory Popov` | Gregory Popov |
| `LL/1./1.3/25-1593-00001 -- KaleMart` | 1001162998 Ontario Corp. o/a KaleMart |
| `LL/1./1.3/25-1603-00001 -- IBERBANCO LTD` | IBERBANCO LTD |
| `LL/1./1.3/25-1614-00001 -- HillSide` | HillSide |
| `LL/1./1.3/25-194-00059 -- Rousseau Mazzuca LLP` | Rousseau Mazzuca LLP |
| `LL/1./1.3/25-845-00001 -- STAR 333 SPORTS INC.` | STAR 333 SPORTS INC. |
| `LL/1./1.3/25-845-00002 -- STAR 333 SPORTS INC.` | STAR 333 SPORTS INC. |
| `LL/1./1.3/26-259-00003 -- LL Onboarding` | LL Onboarding |

**1.4 — Parked**

`LL/1./1.4/` remains part of the canonical Tier 1 hierarchy for parked matters.
Those labels follow the same schema but are assigned manually and are not part
of the ML Active label list above.

The canonical label set is maintained in `scripts/reset_matter_labels.py` (`CANONICAL_LABELS`).
When a new matter opens, add it to that list and re-run the script.

### 4.5 Tier 2 (Fulfillment)

Tier 2 labels (`LL/2./`) are organized by service type rather than by matter:
- `LL/2./2.1 Opening`
- `LL/2./2.2 Maintenance` (sub-types: Flat Fee, Hourly Solutions, Hourly Strategies, Subscription, Counsel)
- `LL/2./2.3 Accounts`
- `LL/2./2.4 Admin`

These are applied manually. Automated enforcement of Tier 2 is deferred.

### 4.6 Matter label rules

- A thread may carry at most one matter label across all tiers.
- Threads relating to multiple matters are flagged for ML1 manual assignment.
- Matter labels must correspond to a valid Clio matter record in the secondbrain matter registry.
- `matter_enforcement.py` enforces Tier 1 only (tiers 1.1–1.4).

---

## 5. Classification

### 5.1 State classification decision tree

The classifier evaluates conditions in strict priority order. The first matching condition
determines the proposed state label.

| Priority | Condition | Proposed state | Notes |
|----------|-----------|----------------|-------|
| 1 | Sender is `calendar-notification@google.com` | `50_Calendar` | Calendar notifications are filed automatically |
| 2 | Thread carries or deterministically resolves to a matter AND sender is automated | `60_Filing` | Automated update on a known matter |
| 3 | Thread carries or deterministically resolves to a matter AND sender is human | `10_Action_Matthew` | Human contact on a known matter requires ML1 review |
| 4 | Sender domain in `TEAM_SENDERS` | `20_Action_Team` | Lino, Grace, levinelegalservices.com |
| 5 | Sender domain in `ADMIN_SENDERS` OR subject contains `ADMIN_SUBJECT_KEYWORDS` | `20_Action_Team` | Vendor / firm admin |
| 6 | ML1 sent last message AND thread has >= 2 messages | `40_Replied_Awaiting_Response` | ML1 is waiting for a response |
| 7 | Subject contains an `ARCHIVE_SUBJECT_SIGNALS` keyword AND no matter label | `90_Archive` | Automated receipt or completion; no action needed |
| 8 | Sender domain in `LEGAL_SENDERS` | `10_Action_Matthew` | Known legal service provider |
| 9 | Snippet contains `unsubscribe` and no matter association is found | `80_Junk_to_Review` | Low-value bulk mail; keep for ML1 review |
| 10 | No condition matched | `00_Triage` | Default; requires manual review |

Category-based inbox cleanup signals such as Gmail `CATEGORY_PROMOTIONS`,
`CATEGORY_SOCIAL`, and `CATEGORY_FORUMS` are not part of this protocol's
decision tree. They are governed by `PRO-018`.

### 5.2 Matter classification signals (in priority order)

| Signal | Assignment | Confidence |
|--------|-----------|------------|
| Matter number already in Gmail label path | Confirmed — no change needed | Determinative |
| Matter number (`\d{2}-\d{3,4}-\d{5}`) in email subject | Proposed matter label | High |
| Matter number in email snippet | Proposed matter label | Medium — flag for review |
| Thread reuse from a previously matter-labeled thread | Proposed same matter label | High when the thread lineage is intact |
| Exact match to a reviewed sender in `matter_identity_map.yaml` | Proposed matter label | High |
| Exact match to a reviewed sender domain in `matter_identity_map.yaml` | Proposed matter label | High |
| Exact match to a reviewed participant key in `matter_identity_map.yaml` | Proposed matter label | Medium — flag for review |
| Match resolves to multiple active matters or duplicate-client matters | No automatic assignment | Review required |
| Raw or generic keys from `participant_mapping.yaml` only | Suggestion only | Low — never determinative by itself |
| No confident signal | Unmapped | Logged to `INBOX_UNMAPPED.md`; requires ML1 assignment |

Additional enforcement rules:

- Automatic matter proposals should be limited to canonical active matters unless
  ML1 explicitly expands scope.
- `matter_identity_map.yaml` is the preferred identity source for matter routing.
  `participant_mapping.yaml` may support discovery, but unreviewed or generic
  tokens must not be used as determinative routing signals.
- Where a client has multiple concurrent matters, sender-identity alone is not
  sufficient unless the identity is explicitly scoped to one matter or the
  thread already carries a stable matter lineage.

### 5.3 Junk resolution rule (NTD-3, resolved)

Threads assigned `80_Junk_to_Review` are not auto-promoted. The batch proposal
includes them for ML1 review. ML1 may:
- Approve promotion to `90_Archive` (standard outcome for confirmed junk)
- Assign a different state label if the thread was misclassified

### 5.4 Canonical sender lists

The following lists are the canonical classification signals. Lists are maintained in
`gmail_governance/batch_classifier.py` and must match this protocol. Any change to
a list requires updating both this document and the script.

**MATTHEW_EMAILS** — ML1's known addresses (used for `40_Replied_Awaiting_Response`):
- `matthew@levinelegal.ca`
- `matthew@levine-law.ca`

**TEAM_SENDERS** → `20_Action_Team`:
- `levinelegalservices.com`
- `lino@levinelegal.ca`
- `grace@levinelegal.ca`
- `lino@levine-law.ca`
- `grace@levine-law.ca`

**LEGAL_SENDERS** → `10_Action_Matthew`:
- `cra-arc.gc.ca`
- `hamlins.com`
- `clio.com`
- `mail.hellosign.com`
- `dropbox.com`
- `cassels.com`
- `rousseaumazzuca.com`
- `docuseal.com`
- `cestlavielaw.ca`
- `asana.com`

**ADMIN_SENDERS** → `20_Action_Team`:
- `telus.com`
- `connect.telus.com`
- `soulpepper.com`
- `amazon.ca`
- `amazon.com`
- `regus.com`

**ADMIN_SUBJECT_KEYWORDS** → `20_Action_Team` (subject match):
- `invoice`, `billing`, `statement of account`, `social event`, `printer`,
  `office supply`, `supplies`, `get ready for your bill`

**ARCHIVE_SUBJECT_SIGNALS** → `90_Archive` (no matter label):
- `you just signed`, `order confirmation`, `your order`, `signed by all signers`

**AUTOMATED_SENDER_SIGNALS** (used in priority 2 and 3 above):
- `noreply`, `no-reply`, `donotreply`, `do_not_reply`, `notifications@`, `automated@`, `system@`

### 5.5 Signals not used

| Signal | Reason excluded |
|--------|----------------|
| Sender name alone | Not unique across contacts |
| Thread age | Not a reliable classification signal |
| Email body full-text | Only subject and snippet available without a full message fetch (requires separate ML1 authorization) |

---

## 6. Classification Procedure

For each unclassified thread (threads carrying `00_Triage` or no state label):

1. Apply the state decision tree (Section 5.1) in priority order. Record the matching condition.
2. Apply matter signals (Section 5.2) in priority order. Record the matching signal.
3. Produce a batch proposal entry with:
   - `thread_id`
   - `proposed_state_label`
   - `proposed_matter_label` (if determinable)
   - `signal_basis` (which condition/signal drove each assignment)
   - `confidence` (`high` / `medium` / `review_required`)
4. Proposals with `confidence: review_required` are excluded from automated batch execution
   and must be resolved by ML1 manually.
5. Submit the completed batch proposal to ML1 for approval before execution.

Batch proposals are written to `06_RUNS/batch/` as JSON files.
No label changes are applied to Gmail until ML1 approves via a signed approval record
in `06_RUNS/approvals/`.

---

## 7. Approval Gate

**All label writes to Gmail require prior ML1 approval.**

The approval record must specify:
- The batch file being approved (file path or hash).
- The scope of approval (all threads in batch, or specific thread IDs).
- The date of approval.
- Any exclusions or overrides.

Approval records are stored in `06_RUNS/approvals/` as Markdown files with
frontmatter `status: approved`.

The execution script (`apply_batch.py`) checks for a corresponding approval record
before writing any labels. If no approval record exists for a batch, execution is
blocked.

Soft-junk cleanup execution is governed separately by `PRO-018`.

---

## 8. Audit and Enforcement

### 8.1 State exclusivity audit

`state_enforcement.py` scans all threads for state label exclusivity violations.
Violations are reported but not auto-resolved.

### 8.2 Matter mapping audit

`matter_enforcement.py` scans all labeled threads and verifies that matter labels
correspond to known matter numbers in secondbrain. Currently enforces Tier 1 (`LL/1./`) only.

### 8.3 Unmapped thread log

Threads that cannot be assigned a matter label are logged to:
```
05_MATTERS/DASHBOARDS/INBOX_UNMAPPED.md
```

This file is updated on each classification run and reviewed by ML1.

### 8.4 Inbox presence audit

A thread simultaneously carrying `INBOX` and one of the inbox-exit state labels
(`50_Calendar`, `60_Filing`, `70_Filed`, `90_Archive`) is in invalid state (POL-042 §4).

**Prevention:** `hourly_inbox_triage.py` removes `INBOX` atomically in the same
`threads.modify` call whenever it applies an inbox-exit label. No intermediate state arises
for threads processed by the triage agent.

**Detection:** After each triage run, the agent scans for any surviving violations
(threads not yet processed by the agent, or produced by other code paths) and writes
the results to:
```
05_MATTERS/DASHBOARDS/INBOX_STATE_VIOLATIONS.md
```

**Scope separation:** This audit concerns inbox state only. It does not intersect with
matter label assignment. A thread may carry a matter label (`LL/`) and still be in
valid INBOX state if its state label is active (e.g., `10_Action_Matthew`).

Violations require ML1 review. Auto-resolution is prohibited.

---

## 9. Data Access Rules

| Data | May agent read? | May agent cite externally? | Notes |
|------|----------------|---------------------------|-------|
| Thread subject and snippet | Yes — for classification only | No | Never reproduce in external output |
| Thread body | Only via explicit ML1-approved fetch | No | Full body fetch requires separate approval |
| Sender/recipient metadata | Yes — for classification only | No | — |
| Gmail label state | Yes | No | Classification context only |

---

## 10. Scope Limitations

This protocol covers state and matter labeling of Gmail threads only.

Out of scope (pending separate protocols or manual processes):
- Google Calendar event classification
- Clio matter data integration
- SharePoint document classification (see PRO-013)
- Cross-system matter linking (Gmail ↔ Clio ↔ SharePoint)
- Matter label Tier 2 (`LL/2./`) automated enforcement

---

## 11. Open Items (NTD)

| Item | Description |
|------|-------------|
| NTD-2 | Define handling rule for multi-matter threads (currently flagged for ML1 manual assignment; no auto-resolution) |

---

## 12. Change Log

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-03-07 | Initial draft. Based on gmail_governance scripts and batch execution artifacts from 2026-02-09 to 2026-03-04. |
| 0.2 | 2026-03-09 | Clarify purpose: interim Gmail tagging to legal matter / Clio matter; future filing to SharePoint LegalMatters. Remove duplicate Section 12. Add `clio` tag. Establish Clio matter ID as canonical matter identifier in Section 4. Add POL-042 reference. |
| 0.3 | 2026-03-14 | Replace simplified signal table with 10-step priority decision tree (matches batch_classifier.py). Codify canonical sender lists (NTD-1 resolved). Document matter label Tier 1/Tier 2 structure (NTD-4 resolved). Define junk resolution rule (NTD-3 resolved). Mark 30_Waiting_External and 70_Filed as manual-only. Add confirmed noise/archive sender lists from 2026-03-14 ML1-directed cleanup. Add bulk cleanup exception to approval gate. Document new canonical label format (LL/1./{tier}/{matter_id} -- {name}) and full canonical label set for all ML Active matters. Update matter_enforcement.py and batch_classifier.py to use MATTER_TIER_PREFIXES. |
| 0.4 | 2026-03-14 | Narrow protocol scope to inbox state and matter management only. Move soft-junk cleanup doctrine to `PRO-018`. Remove category-driven cleanup rules and confirmed cleanup sender lists from this protocol. |
| 0.5 | 2026-04-20 | Add §8.4 Inbox Presence Audit: defines invalid state (INBOX + inbox-exit label), prevention via atomic removal in triage agent, post-run violation scan, and scope separation from matter labels. |
