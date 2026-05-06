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

---

## Governing Rule Established

There are **nine state labels** in Gmail.

**Rule:** Every email must be assigned to at least one state label.

**Corollary:** Any email that carries a state label must not remain in the inbox.
Having a state label means the email has been processed — it should be out of the
inbox. Inbox presence + state label = a contradiction.

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

## Implications for LLP-023 Slice 1

1. **Thread-level search is insufficient.** The system must be capable of
   resolving at the message level when a thread-level search fails to surface a
   known email.

2. **Inbox presence check must be part of the label audit.** A correct state
   label on an email that remains in the inbox is a governance failure — both
   the label assignment and the inbox status must be reconciled together.

3. **Label accuracy cannot be assumed.** The batch proposal and execution
   pipeline must account for the possibility that prior labels are wrong, not
   just missing.

4. **A label audit and reconciliation pass is required before Slice 1 can be
   considered stable.** The two problems above mean the current Gmail label
   state is not a reliable foundation for the daily review pass.

---

## Open Questions

- What are the nine state labels? (To be confirmed with ML1.)
- What is the correct rule for correcting a wrong state label vs. removing it?
- Should the inbox contamination fix (removing inbox flag from state-labeled
  emails) be a separate authorized pass, or folded into the daily review pass?
- Is the Star 333 search failure a one-off retrieval gap or a systemic issue
  with the thread-level search path?

---

## Next Step

ML1 to confirm the nine state labels and authorize a reconciliation pass scope
before Slice 1 proceeds further.
