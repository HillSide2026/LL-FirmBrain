---
id: POL-046
title: Canva Template Enforcement Policy
owner: ML1
status: approved
approval: ML1
approved_by: ML1
approved_date: 2026-04-18
version: 0.1
effective_date: 2026-04-18
supersedes:
provenance:
  decided_by: ML1
  decided_on: 2026-04-18
  context: Metadata normalized by system admin cleanup on 2026-05-24
created_date: 2026-03-10
last_updated: 2026-03-10
tags: [policy, canva, templates, brand-governance, marketing]
---

# POL-046 — Canva Template Enforcement Policy

Policy Statement: All Levine Law Canva assets must be created from ML1-approved templates. Candidate templates are not approved by default and must not be treated as authorized production bases.

Authority (Principles referenced): PRN-030, PRN-031, PRN-032, PRN-033  
Enforcement expectation: Any Canva output not traceable to an approved template is non-compliant and must remain non-authorized.  
Supersedes: None

---

## 1. Purpose

This policy establishes template-level controls to enforce brand consistency across Canva-generated assets.

---

## 2. Scope

This policy applies to all Canva assets produced for Levine Law, including:
- social posts
- pitch deck pages
- report covers
- one-page explainers
- quote graphics

---

## 3. Template Source of Authority

Only templates classified as `approved` may be used as production bases.

Template classification states:
- `approved`
- `candidate`
- `excluded`

Hard rule:
- `candidate` does not imply approval.
- `excluded` is prohibited for LL production use.

---

## 4. Required Template Standards

Each approved template must embed:
- approved color palette controls
- typography rules
- spacing and layout standards

If a template lacks these standards, it is non-compliant and cannot be promoted to `approved`.

---

## 5. Output Authorization Boundary

Any asset generated from a non-approved template remains:
- `approval_status: draft`
- `authorized: false`

Only ML1 may authorize promotion for production use.

---

## 6. Enforcement and Audit

For each generated Canva asset, run artifacts must record:
- template identifier
- template status at generation time
- generated asset identifier
- approval status

Missing template provenance is non-compliant.

---

## 7. Summary

Templates are the primary enforcement mechanism for LL Canva brand consistency.  
Approved templates are mandatory for production.  
Candidates are review inputs only, never implied approvals.

---

## 8. Related Doctrine

- `POL-049` (LL Brand Color Palette Policy)
