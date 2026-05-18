---
id: f01__business-structure-internal-link-architecture
title: Internal Link Architecture — Business Structure Cluster
type: reference
status: approved
funnel: funnel-01
product_link: Business Structure Diagnostic ($49)
created_date: 2026-04-05
last_updated: 2026-04-05
tags: [funnel-01, business-structure, SEO, internal-links]
owner: ML1
---

# Internal Link Architecture — Business Structure Cluster

## URL Registry

| Page | URL |
|---|---|
| Pillar Page | `/business-structure` |
| Pillar Post | `/business-structure/drift-invisible-until-it-matters` |
| Supporting Post 1 | `/business-structure/structure-outdated` |
| Supporting Post 2 | `/business-structure/adding-shareholder-informally` |
| Supporting Post 3 | `/business-structure/investor-diligence-issues` |
| Supporting Post 4 | `/business-structure/documents-vs-reality` |
| Product B | `/products/business-structure-diagnostic` |

---

## Link Graph

```
SUPPORTING POSTS
  └──→ PILLAR POST (/drift-invisible-until-it-matters)
           └──→ PRODUCT (/products/business-structure-diagnostic)

PILLAR PAGE (/business-structure)
  ├──→ PILLAR POST
  └──→ SUPPORTING POSTS (all 4)

PRODUCT PAGE
  └──→ (optional) PILLAR POST + PILLAR PAGE
```

---

## Per-Page Link Specification

### Pillar Page `/business-structure`

**Sections:**
1. What "Business Structure" Actually Refers To — ownership, control, economics, obligations
2. Why Structures Do Not Stay Static — operational change vs static documentation
3. How Structural Drift Occurs — incremental changes, no single triggering event
4. Where Drift Becomes Visible — investors, banks, internal stress
5. What Misalignment Looks Like — documents vs operation, control vs ownership, risk vs allocation
6. When Structure Becomes a Problem — not at change, at interpretation

| Destination | Count | Placement |
|---|---|---|
| `/business-structure/drift-invisible-until-it-matters` | 2 | 1 contextual (after Section 3) + 1 in hub |
| `/business-structure/structure-outdated` | 1 | Hub |
| `/business-structure/adding-shareholder-informally` | 1 | Hub |
| `/business-structure/investor-diligence-issues` | 1 | Hub |
| `/business-structure/documents-vs-reality` | 1 | Hub |

**Does NOT link to:** product page.

---

### Pillar Post `/business-structure/drift-invisible-until-it-matters`

**Title:** Most Business Structures Drift. The Problem Is That the Drift Remains Invisible Until It Matters.

| Destination | Count | Placement | Anchor text options |
|---|---|---|---|
| `/products/business-structure-diagnostic` | 1 | Final paragraph only | `Business Structure Diagnostic` OR `structured assessment of the current structure` |

**Does NOT link to:** supporting posts, pillar page.

---

### Supporting Posts (all four — same rules apply)

| Destination | Count | Placement |
|---|---|---|
| `/business-structure/drift-invisible-until-it-matters` | 2 | 1 inline (mid-article) + 1 continuity (end) |
| `/business-structure` | 0–1 | Optional |

**Does NOT link to:** each other, product page.

#### Titles

| URL | Title |
|---|---|
| `/business-structure/structure-outdated` | When a Business Structure Stops Reflecting How a Company Operates |
| `/business-structure/adding-shareholder-informally` | Adding a Shareholder Informally: What Actually Changes |
| `/business-structure/investor-diligence-issues` | What Investors Flag First in a Company's Structure |
| `/business-structure/documents-vs-reality` | When Corporate Documents No Longer Match Business Reality |

---

### Product Page `/products/business-structure-diagnostic`

| Destination | Required | Notes |
|---|---|---|
| `/business-structure/drift-invisible-until-it-matters` | Optional | Recommended |
| `/business-structure` | Optional | Recommended |

**Does NOT link to:** supporting posts.

---

## Hard Rules

1. Supporting posts link to pillar post only (plus optional pillar page). No lateral links.
2. Pillar post links to product only — one link, final paragraph only.
3. Pillar page links to everything except the product page.
4. Product page outbound links are optional return links only.
