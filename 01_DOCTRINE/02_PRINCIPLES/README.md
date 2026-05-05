---
id: 01_doctrine__principles__readme_md
title: Principles (Level 2)
owner: ML1
status: approved
approved_by: ML1
approved_date: 2026-04-18
version: 1.0
created_date: 2026-02-13
last_updated: 2026-03-23
tags: [doctrine, principles]
---

# Principles (Level 2)

Definition: Interpretive values that guide policy formation and resolution of ambiguity.
Principles are interpretation tools and decision heuristics when rules do not fully determine an outcome.
Boundary: Do not define enforcement mechanics or procedural steps.

Typical examples:
- Prefer explicit artifacts over conversational memory.
- Prefer inspectable systems over opaque automation.
- Prefer reversible changes over irreversible ones.
- Human authority overrides automated inference.

Governance Documents:
- [PRINCIPLE_POLICY_TRACEABILITY.md](PRINCIPLE_POLICY_TRACEABILITY.md) — Cross-reference showing which policies implement each principle
- [LL_BRAND_PRINCIPLES_SUITE.md](LL_BRAND_PRINCIPLES_SUITE.md) — Consolidated suite of LL brand principles (PRN-030 through PRN-035)
- [LL_SPECIFIC_PRINCIPLES_INDEX.md](LL_SPECIFIC_PRINCIPLES_INDEX.md) — Index of LL-level principles (portfolio-specific principles and LL applicability reference)

Naming convention:
- Canonical active principles in this folder should use `PRN-###_Descriptive_Name.md`.
- `README.md` is the only non-`PRN` exception in the active principles layer.

Numbering:
- Principles are numbered sequentially from PRN-001 onwards.
- PRN-011 is intentionally reserved (prior version was deprecated due to duplication with another principle; ID reserved to avoid reuse).

Frontmatter metadata convention:
- Active principle files should carry a dedicated `applies_to` frontmatter field.
- `applies_to` is separate from the flat `tags` list and uses controlled values: `ML2`, `System`, `LL`, `HillSide`.
- More than one `applies_to` value may be selected when a principle spans multiple portfolios.

Repository hygiene rule:
- Legacy family prefixes should not remain in this folder once the principle has been normalized into the active `PRN` sequence.
