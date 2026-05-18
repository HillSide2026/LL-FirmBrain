# Inbox Triage Agent — Skill

## Core Operating Rule

If a thread belongs to a matter, tag the matter.
If not, assign exactly one state label.

---

## Decision Order

1. Work at thread level only.
2. Attempt matter detection first.
3. If matter found → apply matter label and stop.
4. If no matter found → assign exactly one state label.
5. Never apply multiple state labels.

---

## Matter Authority Rule

Existing matter labels are authoritative.
Do not override unless there is strong contradictory evidence.

---

## Anti-Churn Rule

Do not change labels without new information — a new message or a material context change.

---

## Priority Interpretation Rule

Priority is not determined in Gmail.
Priority is inherited from the linked matter's delivery status.

---

## Failure Bias

When uncertain, assign `00_Triage`.
Do not guess a matter.

---

## Prohibited Actions

Do not:
- create synthetic priority labels
- split a thread across multiple state labels
- archive threads that may still require action
- downgrade a matter thread into a state label

---

## Controlling ML2 Artifacts

This agent operates from the following ML2-held artifacts. Changes to these
artifacts take precedence over this skill.md where they conflict.

| Artifact | Path | Status |
|---|---|---|
| Inbox Governance Protocol | `01_DOCTRINE/05_PROTOCOLS/PRO-014_Inbox_Governance_Protocol.md` | draft |
| Inbox Governance Policy | `01_DOCTRINE/03_POLICIES/POL-042_Inbox_Governance_Policy.md` | draft |
| 09_INBOX Pipeline Specification | `09_INBOX/README.md` | draft |
| Matter Update Context Hydration | `01_DOCTRINE/05_PROTOCOLS/PRO-025_Matter_Update_Context_Hydration.md` | approved |

## Pre-Processing Requirement

Before updating any matter record (MATTER.yaml, MATTER_BRIEF.md, MATTER_STATUS.md,
LL_TASK_TRACKER.md, INDEX.md), this agent must execute the Context Hydration
pre-processing step defined in PRO-025. Email-derived classifications must not
overwrite existing service taxonomy without ML1 confirmation.
