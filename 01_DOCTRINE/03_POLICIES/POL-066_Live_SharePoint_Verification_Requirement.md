---
id: 01_doctrine_03_policies_pol_066_live_sharepoint_verification_requirement_md
title: Live SharePoint Verification Requirement
owner: ML1
status: approved
approved_by: ML1
approved_date: 2026-04-18
version: 1.0
created_date: 2026-03-28
last_updated: 2026-03-28
tags: [policy, sharepoint, verification, accuracy, live-data, agent-behaviour]
---

# POL-066 — Live SharePoint Verification Requirement

Policy Statement: When an agent is making claims about the current contents,
structure, implementation status, or present-tense state of SharePoint
LegalMatters folders, it must use live SharePoint review as the primary factual
basis. Relying on old scans instead is non-compliant and absolutely
unacceptable. Historical scans, cached enumerations, or prior snapshots may not
be used in place of live SharePoint verification unless the user explicitly asks
for a historical or scan-based assessment.

Authority (Principles referenced): PRN-003, PRN-006, PRN-007, PRN-008, PRN-019, PRN-020  
Enforcement expectation: Any statement about current SharePoint state that is
based primarily on a historical scan rather than live SharePoint inspection must
be treated as a factual verification failure, corrected immediately, and not
used as the basis for further conclusions.  
Supersedes: None  
Enforcement Protocol: PRO-020

Version: 1.0

Status: Active

---

## 1. Scope

This policy applies whenever an agent is asked to determine or describe:

- current SharePoint folder contents
- current matter-folder structure
- current Model File implementation status
- whether a matter is aligned with filing protocol in present tense
- whether specific documents or folders currently exist in SharePoint

It applies to all `legalmatters` SharePoint work, including Essential,
Strategic, Standard, Standard Cash Cows, and Normal tiers.

---

## 2. Required Rule

If the question is about current SharePoint reality, the agent must inspect live
SharePoint results directly before answering.

Historical sources such as:

- scan artifacts
- cached enumerations
- repo snapshots
- old dashboards
- previously generated review notes

may be used only as secondary support, drift indicators, or historical context.
They must not be treated as the primary factual basis for present-tense claims.

---

## 3. Prohibited Behavior

The following is non-compliant:

1. Relying on an old SharePoint scan instead of live SharePoint review to answer
   a present-tense question.
2. Presenting scan contents as if they are current facts.
3. Drawing structural or compliance conclusions from stale scan data without
   first checking live SharePoint.
4. Continuing analysis after the factual basis has been challenged, without
   first re-verifying against live SharePoint.

These failures are accuracy failures, not merely phrasing issues.

---

## 4. Permitted Use of Historical Scans

Historical scans are permitted only for:

- comparing past and present state
- identifying likely folders to inspect live
- surfacing drift or anomalies
- documenting historical evidence

When used, they must be labeled explicitly as historical artifacts and, where
relevant, dated.

---

## 5. Required Output Discipline

When current SharePoint state has been live-verified, the agent should say so.

When current SharePoint state has not yet been live-verified, the agent must use
language that preserves uncertainty, such as:

- "the historical scan shows"
- "the cached enumeration suggests"
- "live SharePoint verification is still required"

The agent must not collapse those statements into present-tense assertions.

---

## 6. Correction Requirement

If an agent has relied on historical SharePoint artifacts where live review was
required, it must:

1. state that the reliance was wrong,
2. stop treating the historical artifact as current truth,
3. re-run the review against live SharePoint,
4. replace or qualify the prior conclusion.

---

## 7. Summary

For current SharePoint questions:

- live SharePoint first
- historical scans second
- no present-tense claims from stale artifacts

Relying on old scans instead is non-compliant and absolutely unacceptable.
