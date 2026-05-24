---
id: POL-067
title: Matter Authoritative Source Verification Requirement
owner: ML1
status: approved
approved_by: ML1
approved_date: 2026-04-18
version: 1.0
effective_date: 2026-04-18
supersedes:
provenance:
  decided_by: ML1
  decided_on: 2026-04-18
  context: Metadata normalized by system admin cleanup on 2026-05-24
created_date: 2026-03-28
last_updated: 2026-03-28
tags: [policy, matters, verification, source-authority, system-of-record, accuracy]
---

# POL-067 — Matter Authoritative Source Verification Requirement

Policy Statement: When an agent is asked to review, describe, classify, or draw
conclusions about matter-related content, it must use the authoritative source
for that content as the primary factual basis. Relying on derivative artifacts,
repo-stored exports, stale snapshots, or cached scan outputs in place of the
authoritative source is non-compliant and absolutely unacceptable.

Authority (Principles referenced): PRN-003, PRN-006, PRN-007, PRN-008, PRN-019, PRN-020  
Enforcement expectation: Any present-tense matter analysis that is based
primarily on a non-authoritative source must be treated as a factual
verification failure, corrected immediately, and not used as the basis for
further conclusions.  
Supersedes: None  
Enforcement Protocol: PRO-022

Version: 1.0

Status: Active

---

## 1. Scope

This policy applies whenever an agent is asked to review or make claims about:

- emails or email threads
- SharePoint folders or SharePoint-resident matter materials
- Clio matter records
- calendar events tied to matter work
- attachments, drafts, correspondence, or filings
- the relationship between systems that together constitute the Matter File

It applies across all matter tiers and all approved systems used to store,
transmit, or govern matter-related information.

---

## 2. Required Rule

The primary factual basis must be the authoritative system of record for the
thing being reviewed.

Examples:

- If the question is about emails, the authoritative source is the live mailbox
  or authoritative mail archive.
- If the question is about current SharePoint reality, the authoritative source
  is live SharePoint.
- If the question is about Clio matter data, the authoritative source is Clio.
- If the question is about a repo artifact, the authoritative source is the
  repository itself.

Derivative artifacts may be used only as secondary support, cross-checking, or
historical context. They must not silently substitute for the authoritative
source.

Prior summaries require separate treatment:

- For legal work, prior summaries are not an appropriate substitute for the
  underlying authoritative source.
- For matter management, prior summaries may be used if they are dated,
  version-controlled, and used within their proper management function.

---

## 3. Prohibited Behavior

The following is non-compliant:

1. Using an available derivative artifact because it is convenient, instead of
   using the authoritative source required by the question.
2. Treating repo-stored exports, JSON extracts, summaries, OCR outputs, cached
   scans, or prior review notes as if they are the underlying matter content
   itself.
3. Presenting statements derived from a secondary artifact as though they were
   directly verified from the system of record.
4. Silently downgrading from the authoritative source to a fallback source.
5. Continuing analysis after the user has challenged source validity, without
   first re-verifying against the authoritative source.

These are source-discipline failures and factual verification failures.

---

## 4. Fallback Rule

If the authoritative source is unavailable, inaccessible, or not yet
identified, the agent must say so plainly.

The agent must not solve that access problem by substituting a derivative source
unless:

- the user explicitly asks for derivative-artifact analysis, or
- the limitation is disclosed clearly and the answer is framed as partial,
  provisional, or historical.

Unavailable authoritative access is a reason to narrow the claim, not a license
to overstate.

Prior summaries do not change this rule for legal review. If the task is legal,
substantive, interpretive, or document-specific, the agent must return to the
underlying authoritative source.

---

## 5. Required Output Discipline

For matter reviews, the agent must be able to state:

- what source was reviewed
- whether that source is authoritative for the question asked
- whether the review is live, historical, derivative, or mixed
- what remains unverified, if anything

If the source is not authoritative, the agent must preserve that limitation in
its wording.

---

## 6. Matter File Implication

The Matter File may span multiple systems, including SharePoint, Gmail, Clio,
and other approved tools. That does not eliminate source hierarchy.

A federated Matter File may include references to emails, documents, tasks, and
records across systems, but a cross-system reference to an item is not the same
thing as the item itself.

Examples:

- an email summary is not the email
- a SharePoint scan is not live SharePoint
- a repo-stored JSON extract is not the live mailbox
- a matter note referencing a document is not the document itself

For matter management, a dated and version-controlled summary may be a valid
management artifact. It is still not a substitute for the underlying source
when the question is about the actual email, document, record, or legal
content.

---

## 7. Correction Requirement

If an agent has relied on a non-authoritative source where an authoritative
source was required, it must:

1. state that the source choice was wrong,
2. stop treating the derivative artifact as authoritative,
3. re-run the review against the proper source, if available,
4. replace or qualify the prior conclusion.

---

## 8. Relationship to POL-066

POL-066 is a specific application of this broader rule for current SharePoint
questions.

Where the question is specifically about current SharePoint contents or
structure, POL-066 remains fully in force.

---

## 9. Summary

For matter work:

- authoritative source first
- derivative artifacts second
- no silent substitution
- no present-tense claims from non-authoritative inputs

Relying on a non-authoritative source in place of the proper matter source of
record is non-compliant and absolutely unacceptable.
