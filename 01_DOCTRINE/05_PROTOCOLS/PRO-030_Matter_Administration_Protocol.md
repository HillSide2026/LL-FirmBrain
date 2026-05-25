---
id: PRO-030
title: Matter Administration Protocol
owner: ML1
status: draft
version: 0.1
created_date: 2026-05-25
last_updated: 2026-05-25
tags: [protocol, matters, matter-administration, operations, non-canonical]
---

# PRO-030 — Matter Administration Protocol

> **DRAFT — PENDING ML1 APPROVAL.**
> This protocol has not been approved and is not yet in effect.

---

## 1. Purpose

This protocol defines the Matter Administration layer.

Matter Administration governs the non-canonical operational handling of a
matter.

It answers questions such as:

- what needs attention now,
- what tasks or deadlines are live,
- what ML1 should see,
- what is blocked,
- what the current operational posture appears to be,
- which derived summaries should be refreshed

It does not determine what the canonical matter record is.

---

## 2. Scope

This protocol applies to non-canonical operational matter artifacts, including:

- `README.md`
- `MATTER_BRIEF.md`
- `MATTER_STATUS.md`
- `FACTS_TIMELINE.md`
- `ISSUES_AND_POSITIONS.md`
- `NOTES_TO_FILE.md`
- `LL_TASK_TRACKER.md`
- matter dashboards, digests, queue views, and next-action artifacts

It governs those artifacts only as operational / administrative artifacts.

This protocol does not elevate them to canonical matter-record status.

---

## 3. Matter Administration Boundary

Matter Administration may:

- summarize operational posture
- record next steps, blockers, and pending actions
- maintain task and deadline surfaces
- refresh non-canonical summaries for ML1 visibility
- propose Matter Management changes when canonical fields appear to have changed

Matter Administration may not:

- create, redefine, or silently mutate canonical matter-record metadata
- use non-canonical summaries to override `MATTER.yaml`
- infer that a correspondence development changed matter canon without a
  Matter Management basis

If a Matter Administration artifact conflicts with canonical matter-record
metadata, canonical matter metadata wins.

---

## 4. Typical Matter Administration Questions

Matter Administration is the right layer for questions like:

- What is the current operational posture on this matter?
- What is the next step?
- What is ML1 waiting on?
- What deadline or follow-up should be surfaced?
- What should appear in the morning digest or queue?
- Does this summary need refreshing for operational clarity?

These are not automatically Matter Management questions.

---

## 5. Update Triggers

Matter Administration updates are appropriate when a development changes
operational handling without changing canonical matter-record metadata.

Examples:

- a new follow-up obligation appears in email
- a client or counterparty is now waiting on LL
- a deadline becomes visible and needs to be tracked
- an old next step is resolved and a new one replaces it
- a summary is stale and should be refreshed to reflect the present operational
  posture
- ML1 visibility needs change even though matter canon does not

---

## 6. Output Rules

Matter Administration outputs must:

1. treat canonical matter-record metadata as inputs, not editable assumptions,
2. label themselves as derived / operational where helpful,
3. preserve source pointers for significant operational claims,
4. distinguish between:
   - observed facts,
   - operational interpretation,
   - proposed next step,
   - proposed Matter Management change

If an operational summary says something that would imply a change to a
canonical field, it must surface that as a proposal or escalation rather than
silently editing matter canon.

---

## 7. Relationship to Matter Management

Matter Administration is downstream of Matter Management for canonical field
truth.

Matter Administration may:

- consume canonical matter-record metadata,
- display it,
- restate it,
- flag possible needed changes

Matter Administration may not:

- set or revise canonical field values on its own authority

Canonical field changes are reserved to Matter Management.

---

## 8. Relationship to Matter File Administration

Matter Administration is also distinct from Matter File Administration.

Matter Administration focuses on operational handling.
Matter File Administration focuses on cross-system mapping, source verification,
and document / folder / thread relationship management.

Matter Administration may consume Matter File outputs, but must not absorb the
Matter File role.

---

## 9. Escalation Rules

Escalate to Matter Management when:

- a canonical field appears to have changed,
- a summary refresh would require a canonical matter-record change,
- identity or service classification is unclear,
- a change to the canonical matter record is being proposed

Escalate to Matter File Administration when:

- the issue is really about whether an email, folder, or document belongs to
  the matter,
- source verification is incomplete,
- the matter-file relationship across systems is unresolved

---

## 10. Change Log

| Version | Date | Change |
|---|---|---|
| 0.1 | 2026-05-25 | Initial draft. Defines Matter Administration as the non-canonical operational layer for summaries, queues, tasks, and ML1 visibility around a matter. |
