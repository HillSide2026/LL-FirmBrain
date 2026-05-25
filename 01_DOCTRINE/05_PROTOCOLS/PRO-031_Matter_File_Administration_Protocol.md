---
id: PRO-031
title: Matter File Administration Protocol
owner: ML1
status: draft
version: 0.1
created_date: 2026-05-25
last_updated: 2026-05-25
tags: [protocol, matters, matter-file-administration, mapping, source-verification]
---

# PRO-031 — Matter File Administration Protocol

> **DRAFT — PENDING ML1 APPROVAL.**
> This protocol has not been approved and is not yet in effect.

---

## 1. Purpose

This protocol defines the Matter File Administration layer.

Matter File Administration governs the federated Matter File across approved
systems.

It answers questions such as:

- which external records belong to this matter,
- which system is authoritative for the question being asked,
- what mapping gaps remain unresolved,
- what changed in the document / folder / thread surfaces tied to the matter

It does not decide canonical matter-record metadata.

---

## 2. Scope

This protocol applies to cross-system matter-file artifacts and operations,
including:

- SharePoint folder mapping
- Gmail matter-thread mapping
- Clio linkage verification
- matter-to-system maps
- folder protocol assessments
- document inventory and delta tracking
- authoritative-source verification outputs
- matter-file gap reports

It governs the Matter File as a federated record, not as a single folder or
single document set.

---

## 3. Matter File Boundary

Matter File Administration may:

- map external surfaces to a matter
- verify source authority
- assess folder protocol compliance
- record document deltas and external-surface changes
- identify gaps, conflicts, or ambiguity in the federated file
- propose Matter Management or Matter Administration follow-up when evidence
  suggests it

Matter File Administration may not:

- create or redefine matter identity,
- alter canonical matter-record metadata,
- treat an external artifact as changing canon without a Matter Management
  decision,
- silently absorb Matter Administration functions

---

## 4. Typical Matter File Administration Questions

Matter File Administration is the right layer for questions like:

- Does this Gmail thread belong to this matter?
- Which SharePoint folders belong to this matter?
- Is the current SharePoint folder protocol-compliant?
- What new documents or deltas appeared since the last check?
- Did we verify the claim from the authoritative source?
- What source relationship remains unresolved?

These are not automatically Matter Management questions.

---

## 5. Authoritative-Source Discipline

Matter File Administration must follow authoritative-source discipline.

Rules:

1. use the authoritative source for the thing being reviewed,
2. treat summaries, cached extracts, and prior notes as secondary artifacts,
3. preserve source pointers and confidence,
4. surface unresolved verification gaps explicitly

Matter File Administration may use derived artifacts for routing or historical
context, but must not silently substitute them for the authoritative source
when source verification is required.

---

## 6. Output Rules

Matter File Administration outputs must:

1. identify the target `matter_id`,
2. identify the system or surface under review,
3. preserve the basis for inclusion or exclusion,
4. distinguish between:
   - deterministic mapping,
   - inferred mapping,
   - unresolved gap,
   - source conflict

Typical outputs may include:

- matter-file maps
- gap reports
- folder protocol assessments
- document-delta artifacts
- source-verification notes

These outputs are not canonical matter-record metadata.

---

## 7. Relationship to Matter Management

Matter File Administration may produce evidence that suggests a Matter
Management change is needed.

Examples:

- Clio and repo identity values appear misaligned
- authoritative source shows the client name differs from matter canon
- source evidence shows a service record likely needs correction

When that happens, Matter File Administration must:

1. flag the issue,
2. preserve the evidence,
3. route the issue to Matter Management

It must not directly rewrite matter canon.

---

## 8. Relationship to Matter Administration

Matter File Administration may also produce evidence that supports Matter
Administration outputs, such as:

- a new thread that should be surfaced for action,
- a newly visible deadline in source material,
- a folder change that implies a queue review

But Matter File Administration should hand those forward as evidence or
proposals, not as silent operational rewrites.

---

## 9. Routing Rule

When a new external-system development appears:

1. if the main question is system membership, source verification, or file
   mapping -> Matter File Administration
2. if the main question is tasking, deadline surfacing, or ML1 attention ->
   Matter Administration
3. if the main question is whether a canonical matter-record field changed ->
   Matter Management

If more than one layer is implicated, begin with Matter File Administration
only to establish the evidentiary basis, then route onward as needed.

---

## 10. Change Log

| Version | Date | Change |
|---|---|---|
| 0.1 | 2026-05-25 | Initial draft. Defines Matter File Administration as the federated mapping, verification, and document-delta layer distinct from Matter Management and Matter Administration. |
