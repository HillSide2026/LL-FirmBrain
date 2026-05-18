---
id: PRO-020
title: LL Matters SharePoint Protocol
owner: ML1
status: approved
approval: ML1
approved_by: ML1
approved_date: 2026-04-18
project: LLP-006
version: 0.1
created_date: 2026-03-28
last_updated: 2026-03-28
tags: [protocol, sharepoint, ll-matters, legalmatters, governance]
---

# PRO-020 — LL Matters SharePoint Protocol

> **DRAFT — PENDING ML1 APPROVAL.**
> This protocol has not been approved and is not in effect.

## 1. Purpose

This protocol defines the SharePoint-specific governance rules for how
`LL Matters` is to be interpreted by ML2.

It is subordinate to, and must be read consistently with,
`PRO-013_Matter_Filing_Protocol.md`, which remains the governing approved
matter filing protocol.

It answers four questions:

1. What SharePoint surfaces belong to `LL Matters`.
2. How authority claims about required matter structure should be assessed.
3. How matter folders are to be mapped to `matter_id`.
4. What observed folder patterns do and do not prove.

## 2. Authority Hierarchy

For `LL Matters`, SharePoint-facing authority is ranked as follows:

1. **Model File** in SharePoint.
2. ML1-approved doctrine in this repository.
3. ML1-approved explicit mapping files.
4. Observed folder names and repeated implementation patterns.

### Binding rule

Repeated structure in live matter folders is **evidence of practice**, not proof
of protocol. No recurring pattern observed in active folders may be treated as
the governing `LL Matters` protocol unless it has been reconciled to the
`Model File` and then codified in ML1-approved doctrine.

## 3. Scope

This protocol applies to the `legalmatters` SharePoint workspace described in:

- [sharepoint/README.md](../../00_SYSTEM/integrations/sharepoint/README.md)
- [matter_folder_rules.yml](../../00_SYSTEM/CONFIG/matter_folder_rules.yml)

In scope:

- `LL Matters (Essential)`
- `LL Matters (Strategic)`
- `LL Matters (Standard)`
- `LL Matters (Standard Cash Cows)`
- `LL Matters (Parked)`
- `Model File` as the governing structural reference, even if excluded from ML2
  intake access

Out of scope:

- `Clerk Work` as protocol authority
- `Data Management`
- ad hoc assumptions from live matter folders

## 4. Model File Rule

`Model File` is the authoritative source for:

- the required matter folder structure
- required folder names and sequencing
- intended semantic meaning of each folder
- what belongs in each folder

If doctrine in this repository conflicts with `Model File`, the conflict must
be flagged for ML1 reconciliation.

This protocol does not by itself displace `PRO-013`; it governs how ML2 should
reason about SharePoint authority claims and mapping uncertainty.

If ML2 cannot directly inspect `Model File`, ML2 must not invent or hard-code a
protocol from observation alone. The correct response is to:

1. record uncertainty,
2. avoid semantic overreach,
3. seek ML1 clarification or approved restatement.

## 5. Matter Identification

SharePoint matter resolution is governed by:

- [matter_folder_rules.yml](../../00_SYSTEM/CONFIG/matter_folder_rules.yml)
- `matter_sharepoint_map.yml` (legacy reference; file not present in this repo)

### Default rule

If a SharePoint folder name begins with a canonical matter number, that is the
primary deterministic routing signal.

### Fallback rule

If naming conventions are insufficient, `matter_sharepoint_map.yml` is the
authoritative override.

### Important limitation

A folder may belong to a matter even if it does not contain the matter number.
That relationship must be established by one of:

- explicit map entry
- ML1-approved matter note
- other approved doctrine artifact

It must not be assumed merely because the folder looks substantively related.

## 6. Primary Folder vs Related Folder

For any matter, ML2 must distinguish:

- **Primary SharePoint folder**: the folder designated by protocol, explicit map,
  or approved matter record as the matter's main workspace
- **Related SharePoint folder**: a folder containing matter-relevant documents
  but not, by itself, proof of protocol compliance or primacy

The existence of documents in a related folder does not make that folder the
primary matter folder.

## 7. Consequences for Interpretation

This protocol establishes the following:

1. SharePoint is a read-only intake source for `legalmatters`, not a doctrine
   source.
2. `Model File`, not repetition, defines the required `LL Matters` structure.
3. Folder repetition may support a hypothesis, but never by itself proves
   protocol compliance.
4. Folder names may inform routing and provisional classification, but may not
   be treated as self-authenticating legal-status labels.

## 8. Required ML2 Behavior

ML2 must not:

- call an observed folder "on-protocol" without reconciliation to `Model File`
- infer protocol authority from repeated live-folder patterns
- treat folder labels alone as dispositive of draft/final status

ML2 must:

- separate protocol authority from observed implementation
- explicitly label any inference as inference
- correct stale doctrine when protocol assumptions are shown to be unsupported

## 9. Change Log

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-03-28 | Initial draft created to distinguish SharePoint authority, Model File authority, matter mapping, and observed-pattern limitations. |
