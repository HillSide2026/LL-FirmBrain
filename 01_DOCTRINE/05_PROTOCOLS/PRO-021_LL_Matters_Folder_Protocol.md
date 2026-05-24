---
id: PRO-021
title: LL Matters Folder Protocol
owner: ML1
status: approved
approval: ML1
approved_by: ML1
approved_date: 2026-04-18
project: LLP-006
version: 0.1
effective_date: 2026-04-18
supersedes:
provenance:
  decided_by: ML1
  decided_on: 2026-04-18
  context: Metadata normalized by system admin cleanup on 2026-05-24
created_date: 2026-03-28
last_updated: 2026-03-28
tags: [protocol, ll-matters, folders, sharepoint, matter-structure]
---

# PRO-021 — LL Matters Folder Protocol

> **DRAFT — PENDING ML1 APPROVAL.**
> This protocol has not been approved and is not in effect.

## 1. Purpose

This protocol defines how ML2 is to reason about folder structure inside
`LL Matters`.

It is subordinate to, and must be read consistently with,
`PRO-013_Matter_Filing_Protocol.md`, which remains the governing approved
matter filing protocol.

It governs:

1. which folder structure is authoritative,
2. how a matter folder is identified,
3. how divergence from the required structure is handled,
4. what folder names may and may not be used to infer.

## 2. Authoritative Folder Structure

The authoritative `LL Matters` folder structure must be determined by governing
doctrine and, where applicable, the structure contained in `Model File`.

`Model File` is therefore the governing source for:

- required folder set
- required folder names
- ordering / numbering
- intended purpose of each folder

This protocol does not replace the filing hierarchy stated in `PRO-013`.
It governs how ML2 should assess folder compliance, divergence, and ambiguity.

## 3. Folder Compliance

A matter folder is **protocol-compliant** only if it has been reconciled against
`Model File` and determined to match the required structure, allowing only
approved variances.

A matter folder is **not** protocol-compliant merely because:

- it uses numbered folders,
- it resembles other active matter folders,
- it contains a recurring six-folder pattern,
- it looks substantively well organized.

## 4. Folder Categories

For ML2 purposes, every SharePoint matter-related folder must be treated as one
of the following:

| Category | Meaning |
|----------|---------|
| `protocol_primary` | The matter's main folder and compliant with the required `Model File` structure |
| `primary_unverified` | Likely the main matter folder, but protocol compliance has not been established |
| `related_substantive` | Contains substantive matter materials but is not yet established as the protocol primary folder |
| `shell_or_sparse` | Folder exists for the matter but appears thin, incomplete, or administrative only |
| `legacy_or_anomalous` | Folder structure diverges materially from protocol and requires explicit handling |

## 5. Folder Semantics

Folder names are structural signals, not legal-status conclusions.

Folder names may support:

- routing
- organization
- provisional provenance hypotheses

Folder names may not alone support:

- "this document is final"
- "this document is authoritative work product"
- "this folder is protocol-compliant"

## 6. Repeated Pattern Rule

A repeated pattern found across multiple matters is evidence of implementation
practice only.

Repeated pattern is not enough to conclude:

- that the pattern is the required folder protocol
- that a specific folder is compliant with `Model File`
- that folder semantics are uniform across all matters

## 7. Divergence Handling

When a matter-related folder diverges from `Model File` or when protocol
compliance cannot be established:

1. classify the folder as `primary_unverified`, `related_substantive`,
   `shell_or_sparse`, or `legacy_or_anomalous`
2. avoid calling it protocol-compliant
3. use explicit notes or mapping to preserve routing truth
4. separate folder usefulness from protocol status

## 8. Required ML2 Language

If protocol compliance is not established, ML2 should use language like:

- "appears to be the substantive working folder"
- "belongs to this matter"
- "contains substantive transaction materials"
- "protocol compliance not yet established against Model File"

ML2 should not use language like:

- "on-protocol"
- "on-spec"
- "the required structure"

unless those conclusions have been reconciled to `Model File`.

## 9. Relationship to Matter Mapping

Matter membership and folder compliance are separate questions.

A folder may:

- belong to a matter, and
- still fail or not yet satisfy folder protocol.

Likewise, a sparse numbered folder may belong to a matter even if it is not the
best substantive working folder.

## 10. Change Log

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-03-28 | Initial draft created to separate folder membership, structural usefulness, and protocol compliance. |
