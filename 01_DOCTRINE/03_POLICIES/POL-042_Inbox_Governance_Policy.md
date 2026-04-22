---
id: POL-042
title: Inbox Governance Policy
owner: ML1
status: approved
approval: ML1
approved_by: ML1
approved_date: 2026-04-18
project: LLP-006
version: 0.3
created_date: 2026-03-09
last_updated: 2026-04-19
tags: [policy, gmail, inbox, labeling, classification, legalmatters, clio, cleanup]
---

# POL-042 — Inbox Governance Policy

Policy Statement: Gmail inbox administration must distinguish between state-and-matter management and soft-junk cleanup. Gmail state or matter labels must be governed by a canonical framework and approval gate. Inbox cleanup actions must be governed by a separate cleanup protocol. No Gmail label may be written by an agent or script without prior ML1 approval unless the governing cleanup protocol expressly allows ML1-directed execution.

Authority (Principles referenced): PRN-003, PRN-004, PRN-008, PRN-026

Enforcement expectation: Violations of state exclusivity, unauthorized label writes, or matter labels referencing unknown matter IDs are non-compliant and must be flagged for ML1 remediation.

Supersedes: None

Enforcement Protocols: PRO-014, PRO-018

---

## 1. Policy Purpose

This policy establishes the governance rules for Gmail inbox classification
within the Levine Law Second Brain system.

The policy defines:

- The authoritative state label framework applied to Gmail threads.
- The structure of matter labels linking emails to legal matters.
- The separate cleanup lane for soft-junk inbox administration.
- The approval controls required before Gmail labels are written.
- The permitted data access scope for inbox classification agents.

The policy ensures that inbox activity supports the matter-centric architecture
of the system, in which each email thread related to legal work can be traced
to a corresponding legal matter.

Operational protocols implementing this policy are defined in `PRO-014` and `PRO-018`.

---

## 2. Policy Objective

Inbox governance exists to ensure that all matter-related email is traceably
linked to the corresponding legal matter object in ML2 and LL systems.

The architecture operates in two phases.

**Interim Phase (Current)**

Emails remain in Gmail but are labeled to reflect:
- thread action state
- associated legal matter number (Clio matter ID)

Matter labels serve as the cross-system reference key linking Gmail threads
to Clio matters and ML2 matter records.

**Future Phase**

Emails may be routed or filed into the SharePoint LegalMatters
structure once cross-system matter linking is implemented.
Future integration is governed under LLP-005.

---

## 3. System Scope

This policy applies only to Gmail inbox governance for:
- `matthew@levinelegal.ca`
- `matthew@levine-law.ca`

The policy governs:
- Gmail thread classification
- Gmail label structure
- Batch labeling controls
- Approval requirements for label writes
- Inbox cleanup controls

The policy does not govern:
- Google Calendar
- SharePoint document storage
- Clio matter management
- Cross-system document routing

Those areas require separate policies or protocols.

---

## 4. Canonical State Label Framework

Each Gmail thread must contain exactly one state label.

State labels represent the operational status of the thread.
State labels are mutually exclusive.

| Label | Meaning |
|-------|---------|
| `00_Triage` | Thread received but not yet reviewed |
| `10_Action_Matthew` | Thread requires ML1 action |
| `20_Action_Team` | Delegated to team member |
| `30_Waiting_External` | Waiting on external party |
| `40_Replied_Awaiting_Response` | ML1 replied and awaiting response |
| `50_Calendar` | Calendar-related thread |
| `60_Filing` | Requires filing to document system |
| `70_Filed` | Thread has been filed; no further action required |
| `80_Junk_to_Review` | Suspected junk pending ML1 review |
| `90_Archive` | No further action required |

**Enforcement Rule:** A Gmail thread must not contain more than one state label.
Detection of multiple state labels constitutes a policy violation and must be
reported by enforcement scripts. Automatic resolution of such violations is
prohibited without ML1 approval.

**Inbox Presence Rule:** A thread must not simultaneously carry `INBOX` and an inbox-exit
state label. Inbox-exit labels are: `50_Calendar`, `60_Filing`, `70_Filed`, `90_Archive`.
These labels imply the thread has exited triage. Applying any inbox-exit label must
atomically remove `INBOX` in the same operation — no intermediate state is permitted.

Detection of threads in this invalid state constitutes a policy violation. Violations
are reported to `05_MATTERS/DASHBOARDS/INBOX_STATE_VIOLATIONS.md` after each triage run.
Automatic resolution is prohibited without ML1 approval.

This rule is distinct from matter management. Matter labels (`LL/`) are orthogonal to
inbox presence and do not themselves require INBOX removal.

---

## 5. Matter Label Policy

Matter labels create the link between a Gmail thread and a legal matter.

The **canonical matter identifier** is the **Clio matter ID**, in the format:
```
\d{2}-\d{3,4}-\d{5}  (e.g., 25-1593-00001)
```

Identifier semantics (segment meaning and client-of-record identity constraints) are governed by `POL-043`.

The canonical label hierarchy is:
```
LL/
└── {tier_number}.
    └── {tier_name}
        └── {clio_matter_id}
```

Example: `LL/1./1.1 - Essential/25-1593-00001`

**Policy rules:**
- A thread may contain no more than one matter label.
- Threads referencing multiple matters require ML1 assignment.
- Matter labels must correspond to a valid Clio matter record.

---

## 6. Classification Governance

Automated classification may generate proposed label assignments.

These proposals must be based on deterministic signals such as:
- Sender domain classification
- Existing Gmail label paths
- Presence of Clio matter IDs in subject or snippet

State and matter signal lists are defined in `PRO-014`.
Soft-junk cleanup signals and confirmed cleanup sender lists are defined in `PRO-018`.

**Automated classification does not authorize execution.**
All classification results are proposals only.

---

## 7. Draft and Send Policy

The System may create Gmail drafts on ML1 direction. **Sending is permanently prohibited.**

No agent, script, or MCP tool may send a Gmail message or transmit a draft to any recipient. Only ML1 may send email. This rule has no exceptions and may not be overridden by any downstream approval or automation instruction.

No `send_message`, `send_draft`, or equivalent capability may be added to the Gmail MCP server or any other system integration without explicit ML1 doctrine amendment to this policy.

---

## 8. Approval Gate Policy

No Gmail labels may be written by agents or scripts unless
ML1 approval has been recorded.

An approval record must specify:
- Batch file identifier or hash
- Scope of approval
- Date of approval
- Any exclusions or overrides

Execution scripts must verify the existence of a valid approval record
before performing any Gmail write operation. If approval is not present,
execution must halt.

---

## 9. Audit and Enforcement

The system must provide enforcement checks for:

**State Exclusivity:** Detect Gmail threads containing multiple state labels.

**Matter Mapping:** Verify that applied matter labels correspond to known
Clio matter identifiers.

**Unmapped Threads:** Threads lacking matter assignment must be logged to:
```
05_MATTERS/DASHBOARDS/INBOX_UNMAPPED.md
```
The log is reviewed periodically by ML1.

---

## 10. Data Access Policy

Inbox classification agents may access only the minimum data necessary
for classification.

| Data | Agent Read | External Citation |
|------|-----------|-------------------|
| Email subject | Permitted | Prohibited |
| Email snippet | Permitted | Prohibited |
| Sender metadata | Permitted | Prohibited |
| Gmail label state | Permitted | Prohibited |
| Email body | Prohibited unless ML1 explicitly authorizes | Prohibited |

Email content must never appear in external outputs.

---

## 11. Policy Limitations

This policy governs label classification only.

It does not define:
- Gmail execution scripts
- Classification logic implementation
- Clio integration
- SharePoint document filing

These are defined in supporting protocols.

---

## 12. Open Governance Items

| ID | Item |
|----|------|
| NTD-1 | Confirm canonical sender domain lists |
| NTD-2 | Define handling of multi-matter threads |
| NTD-3 | Confirm final operating boundary between `80_Junk_to_Review` and `PRO-018` cleanup actions |

---

## 13. Change Log

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-03-09 | Initial policy. Derived from PRO-014 v0.2. |
| 0.2 | 2026-03-14 | Distinguish inbox state-and-matter management from soft-junk cleanup. Add `PRO-018` as a separate enforcement protocol. |
| 0.3 | 2026-04-19 | Add §7 Draft and Send Policy: System may create drafts; sending is permanently prohibited; no send capability may be added without doctrine amendment. |
| 0.4 | 2026-04-20 | Add Inbox Presence Rule to §4: inbox-exit labels must atomically remove INBOX; invalid state detection logged to INBOX_STATE_VIOLATIONS.md; scope separation from matter labels clarified. |
