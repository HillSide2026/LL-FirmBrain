---
id: PRO-022
title: LL Matters File Protocol
owner: ML1
status: approved
approval: ML1
approved_by: ML1
approved_date: 2026-04-18
project: LLP-006
version: 0.2
effective_date: 2026-04-18
supersedes:
provenance:
  decided_by: ML1
  decided_on: 2026-04-18
  context: Metadata normalized by system admin cleanup on 2026-05-24
created_date: 2026-03-28
last_updated: 2026-03-28
tags: [protocol, ll-matters, matter-file, cross-system, routing]
---

# PRO-022 — LL Matters File Protocol

> **DRAFT — PENDING ML1 APPROVAL.**
> This protocol has not been approved and is not in effect.

## 1. Purpose

This protocol defines what a **Matter File** is for LL Matters.

For LL Matters, the Matter File is not limited to any single SharePoint folder,
single email thread, single Clio record, or single document set.

The Matter File is the governed cross-system record of a matter, including the
relationship between the matter and all relevant external storage surfaces where
matter-related records may exist.

This protocol is subordinate to, and must be read consistently with,
`PRO-013_Matter_Filing_Protocol.md`.

## 2. Definition of Matter File

A Matter File is the full set of matter-related records across all approved
systems of work and record, including but not limited to:

- SharePoint matter folders
- Gmail threads and messages
- Clio matter records
- external tool records tied to the matter
- related document stores, portals, and transaction workspaces

The Matter File therefore consists of:

1. the matter identity,
2. the cross-system pointers to where matter records live,
3. the rules that determine which external records belong to the matter,
4. the local ML2 representation of that cross-system relationship.

## 3. Core Principle

The storage of matter-related or client-related records in external systems
constitutes the Matter File.

The Matter File is therefore a **federated file**, not a single folder and not
a pile of isolated documents.

## 4. Systems in Scope

For any given matter, the Matter File may include records from:

- SharePoint
- Gmail
- Clio
- Google Drive
- OneDrive
- external portals
- other ML1-approved systems

No single system is presumed to contain the whole Matter File.

## 5. Required Questions

For each matter, ML2 must be able to answer:

1. What is the canonical `matter_id`?
2. Which SharePoint folders belong to the matter?
3. Which Gmail threads/messages belong to the matter?
4. Which Clio matter or related records belong to the matter?
5. Which other external workspaces, if any, belong to the matter?
6. Which local ML2 matter folder represents that federated Matter File?

## 6. Matter File Mapping

Matter-file governance requires explicit mapping between `matter_id` and
external records.

The Matter File is not fully governed unless those relationships are either:

- deterministically derivable under approved rules, or
- explicitly mapped in approved registry artifacts.

Examples of valid matter-file mapping artifacts include:

- `00_SYSTEM/CONFIG/matter_folder_rules.yml`
- `05_MATTERS/_REGISTRY/matter_sharepoint_map.yml`
- `00_SYSTEM/matters/matter_identity_map.yaml`
- ML1-approved matter notes or doctrine artifacts

## 7. SharePoint Relationship

SharePoint folders may contain a large portion of the Matter File, but a
SharePoint folder is only one component of the Matter File.

Consequences:

1. A SharePoint folder may be protocol-compliant and still not exhaust the Matter File.
2. A SharePoint folder may be sparse while the Matter File is substantively rich
   elsewhere.
3. More than one SharePoint folder may belong to the same Matter File.

## 8. Gmail Relationship

Matter-related Gmail threads and messages are part of the Matter File when they
relate to the matter's work, client, transaction, counterparties, or closing
process.

The Matter File therefore includes communication records, not just uploaded
documents.

## 9. Clio Relationship

Clio is a matter identity and administration surface, not merely a metadata
overlay.

Clio matter linkage, status, client identity, and matter numbering are all part
of Matter File governance.

## 10. Document-Level Reasoning Is Secondary

Individual documents are components of the Matter File, but they are not the
primary object governed by this protocol.

This protocol governs:

- which systems and locations belong to the matter,
- how those locations relate to one another,
- how ML2 should represent the federated file.

Questions like draft/final/executed status are secondary and belong to narrower
document-status reasoning, not to the definition of the Matter File itself.

## 11. Required ML2 Behavior

ML2 must not reduce the Matter File to:

- one SharePoint folder,
- one document set,
- one Gmail thread,
- or one local folder.

ML2 must:

1. treat the Matter File as a cross-system construct,
2. preserve mappings between systems,
3. identify gaps where the cross-system relationship is unresolved,
4. distinguish between:
   - matter membership,
   - system location,
   - protocol compliance,
   - and document status.

## 12. Preferred Output Language

ML2 should prefer language like:

- "the Matter File includes records in SharePoint, Gmail, and Clio"
- "this SharePoint folder is one component of the Matter File"
- "the matter file relationship is established, but mapping remains incomplete"
- "this document belongs to the Matter File, but document status is a separate question"

ML2 should avoid language like:

- "the Matter File is this folder"
- "the file is these documents only"
- "document classification defines the Matter File"

## 13. Change Log

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-03-28 | Initial draft created with overly document-centric scope. |
| 0.2 | 2026-03-28 | Rewritten to define the Matter File as the federated cross-system matter record spanning SharePoint, Gmail, Clio, and other approved tools. |
