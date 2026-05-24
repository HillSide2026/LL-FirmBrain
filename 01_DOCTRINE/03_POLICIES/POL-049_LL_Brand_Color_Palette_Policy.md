---
id: POL-049
title: LL Brand Color Palette Policy
owner: ML1
status: approved
approval: ML1
approved_by: ML1
approved_date: 2026-04-18
version: 0.4
effective_date: 2026-04-18
supersedes:
provenance:
  decided_by: ML1
  decided_on: 2026-04-18
  context: Metadata normalized by system admin cleanup on 2026-05-24
created_date: 2026-03-10
last_updated: 2026-03-20
tags: [policy, brand, color, palette, canva, templates]
---

# POL-049 — LL Brand Color Palette Policy

Policy Statement: Levine Law visual outputs must use the defined LL brand palette. Colors outside the approved palette are non-compliant unless explicitly approved by ML1.

Authority (Principles referenced): PRN-030, PRN-031, PRN-032, PRN-035  
Enforcement expectation: Any asset that uses non-approved colors without explicit ML1 approval is non-authorized for distribution.  
Supersedes: None

---

## 1. Purpose

This policy defines:
- the current active LL palette (`Present State`)
- the pending target LL palette (`Future State`)
- the transition rule for cutover between states

---

## 2. Present State (Active Palette)

Primary palette:
- `#1D4771`
- `#0365B2`
- `#FFFFFF`
- `#FF5E5B`

Secondary palette:
- `#000000`
- `#1D4771`
- `#0365B2`
- `#4BD1FB`
- `#D1D5DB`

---

## 3. Future State (Target Palette - Pending Activation)

Primary palette:
- `#1D4771`
- `#0365B2`
- `#FFFFFF`
- `#2E2E2E`

Accent:
- `#FF5E5B`

Neutral:
- `#D1D5DB`

Total colors: `6`

---

## 4. Transition Rule

Until ML1 issues explicit activation, Section 2 (`Present State`) remains the only enforceable palette.

When ML1 activates the target palette:
- Section 3 becomes the active enforceable palette
- Section 2 moves to historical reference
- affected templates must be remediated to match the active palette

---

## 5. Compliance Rule

Assets must be reviewed for palette compliance against the currently active state.

If an asset includes colors outside the approved palette:
- the asset is non-compliant by default
- it must be corrected, or
- explicitly approved by ML1

---

## 6. B&W Print Exception

A gray variant is permitted exclusively for assets produced for black-and-white print output (e.g., printed documents without color printing capability).

Two gray values are observed in the current Canva logo files (audit 2026-03-20):
- `#7E7E7E` — darker gray (Rectangle Set page 8)
- `#B4BABA` — lighter gray (Rectangle Set page 12)

**Open item — ML1 decision required:** One of these must be declared the canonical B&W print gray. The other must be retired. Until ML1 decides:
- Both are provisionally permitted for B&W print use only.
- Neither is permitted for color digital outputs.
- `#B4BABA` is the recommended canonical candidate (lighter value, provides adequate contrast for white text, prints with clear differentiation from white).

Once ML1 selects the canonical value, add it to the Present State secondary palette and remove the other from production.

---

## 7. Governance and Storage

Canonical palette values must be stored in ML2 brand doctrine and referenced by approved templates and template usage rules.

---

## 8. Summary

LL color usage is governed by an active-state palette model with a documented future target state.
Non-palette colors require correction or explicit ML1 approval.
B&W print gray is a provisionally permitted exception pending ML1 canonicalization.
