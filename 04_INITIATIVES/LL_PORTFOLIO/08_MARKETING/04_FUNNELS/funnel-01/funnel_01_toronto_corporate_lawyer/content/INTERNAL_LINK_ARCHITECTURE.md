---
id: f01__shareholder-disputes-internal-link-architecture
title: Internal Link Architecture — Shareholder Disputes Cluster
type: reference
status: approved
funnel: funnel-01
created_date: 2026-04-05
last_updated: 2026-04-05
tags: [funnel-01, shareholder-dispute, SEO, internal-links]
owner: ML1
---

# Internal Link Architecture — Shareholder Disputes Cluster

## URL Registry

| Page | URL |
|---|---|
| Pillar Page | `/shareholder-disputes` |
| Pillar Post | `/shareholder-disputes/partnership-not-tense` |
| Supporting Post 1 | `/shareholder-disputes/early-signs` |
| Supporting Post 2 | `/shareholder-disputes/documentation` |
| Supporting Post 3 | `/shareholder-disputes/removing-partner-ontario` |
| Supporting Post 4 | `/shareholder-disputes/shareholder-agreement-reality` |
| Product A | `/products/shareholder-dispute-readiness-guide` |

---

## Link Graph

```
SUPPORTING POSTS
  └──→ PILLAR POST (/partnership-not-tense)
           └──→ PRODUCT (/products/shareholder-dispute-readiness-guide)

PILLAR PAGE (/shareholder-disputes)
  ├──→ PILLAR POST
  └──→ SUPPORTING POSTS (all 4)

PRODUCT PAGE
  └──→ (optional) PILLAR POST + PILLAR PAGE
```

---

## Per-Page Link Specification

### Supporting Posts (all four — same rules apply)

| Destination | Count | Placement | Anchor text |
|---|---|---|---|
| `/shareholder-disputes/partnership-not-tense` | 2 | 1 inline (mid-article) + 1 continuity (end) | See anchor text table below |
| `/shareholder-disputes` | 0–1 | Optional | — |

**Does NOT link to:** other supporting posts, product page.

#### Anchor text by post

| Post | Inline anchor text | Continuity anchor text |
|---|---|---|
| `/early-signs` | `how these situations typically develop` | `A Business Partnership Is Rarely "Tense." It Is Usually Entering a Legally Meaningful Phase.` |
| `/documentation` | `how early-stage situations develop` | `A Business Partnership Is Rarely "Tense." It Is Usually Entering a Legally Meaningful Phase.` |
| `/removing-partner-ontario` | `how these situations form` | `A Business Partnership Is Rarely "Tense." It Is Usually Entering a Legally Meaningful Phase.` |
| `/shareholder-agreement-reality` | `how these divergences develop into disputes` | `A Business Partnership Is Rarely "Tense." It Is Usually Entering a Legally Meaningful Phase.` |

---

### Pillar Page `/shareholder-disputes`

| Destination | Count | Placement | Anchor text |
|---|---|---|---|
| `/shareholder-disputes/partnership-not-tense` | 2 | 1 contextual (below Early Warning Signs section) + 1 in hub | `how these situations actually develop` / full title |
| `/shareholder-disputes/early-signs` | 1 | Hub | `Early Signs a Business Partner Relationship Is Breaking Down` |
| `/shareholder-disputes/documentation` | 1 | Hub | `What to Document When a Shareholder Dispute Is Emerging` |
| `/shareholder-disputes/removing-partner-ontario` | 1 | Hub | `Can a Business Partner Be Removed From a Company in Ontario?` |
| `/shareholder-disputes/shareholder-agreement-reality` | 1 | Hub | `When a Shareholder Agreement No Longer Reflects Reality` |

**Does NOT link to:** product page.

---

### Pillar Post `/shareholder-disputes/partnership-not-tense`

| Destination | Count | Placement | Anchor text |
|---|---|---|---|
| `/products/shareholder-dispute-readiness-guide` | 1 | Final paragraph only | `Shareholder Dispute Readiness Guide` |

**Does NOT link to:** supporting posts, pillar page.

**Exact sentence (locked):**
> The [Shareholder Dispute Readiness Guide](/products/shareholder-dispute-readiness-guide) is structured around those early-stage considerations.

---

### Product Page `/products/shareholder-dispute-readiness-guide`

| Destination | Required | Anchor text |
|---|---|---|
| `/shareholder-disputes/partnership-not-tense` | Optional | — |
| `/shareholder-disputes` | Optional | — |

**Does NOT link to:** supporting posts.

---

## Hard Rules

1. No supporting post links to another supporting post.
2. No supporting post links to the product page.
3. Pillar post links only to the product page (one link, end only).
4. Pillar page links to everything except the product page.
5. Product page does not link outward except optional return links to pillar post and pillar page.
