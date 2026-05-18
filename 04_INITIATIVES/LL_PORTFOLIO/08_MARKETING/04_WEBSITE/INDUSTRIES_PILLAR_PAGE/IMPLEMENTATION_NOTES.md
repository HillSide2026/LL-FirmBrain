---
id: IMPLEMENTATION_NOTES
title: Implementation Notes — Level 2 Industries Pillar Page
owner: ML1
status: draft
created_date: 2026-03-21
agent: MKT_WEBSITE_IMPLEMENTATION_AGENT
last_updated: 2026-05-18
---

# Implementation Notes — Level 2 Industries Pillar Page

## 1. Repo Architecture Note

No HTML or CMS files exist in this repository. This repo is the content and doctrine layer. All content is authored and QA-reviewed here as markdown draft artifacts before any CMS or GoHighLevel implementation.

The output directory for all Industries Pillar Page artifacts is:

```
04_INITIATIVES/LL_PORTFOLIO/08_MARKETING/04_WEBSITE/INDUSTRIES_PILLAR_PAGE/
```

---

## 2. Content Staging Flow

The correct staging flow for this page is:

```
Step 1: Repo draft (this build — markdown)
Step 2: ML1 approval of repo draft
Step 3: CMS or GoHighLevel handoff package prepared
Step 4: Staging environment build (CMS/GHL)
Step 5: ML1 review of staged page
Step 6: Production publish — requires explicit ML1 authorization per INV-0002
```

No content is to be published at any step without explicit ML1 authorization. This applies to all six sections of the Industries page.

---

## 3. CMS / GoHighLevel Handoff Notes

The current Levine Law website infrastructure appears to be WordPress with the Thrive Architect page builder (based on source page HTML review — presence of Thrive CSS classes and markup patterns).

When the repo draft is approved by ML1, the handoff package for the CMS implementer should include:

- The approved markdown content file (INDUSTRIES_PILLAR_PAGE_DRAFT_v1.md or its successor).
- This PAGE_ARCHITECTURE.md as the structural brief for the implementer.
- Section-by-section annotations identifying which content goes into which page builder section.
- The Level 2 to Level 3 URL map from PAGE_ARCHITECTURE.md, so the implementer knows which URLs to link to (even if those Level 3 pages are stubs at time of implementation).

If the website migrates to GoHighLevel (GHL) per the Funnel 2 strategy, the same content and architecture documents serve as the GHL page-build brief.

---

## 4. Section-by-Section Implementation Notes

### Section 1 — Intro / Why Industry Context Matters
- Place as the first content section below the page header.
- No hero image required — the copy should carry the section.
- If a background image is used, it must not undermine legibility or add decorative clutter.
- Recommended container: full-width text block, left-aligned, with a clean margin.

### Section 2 — Industries We Serve
- Recommended implementation: card grid with six entries (one per industry).
- Each card: industry name, one-sentence descriptor, link to Level 3 page.
- Level 3 page links should be placeholder links if those pages are not yet built (link to Inquiries as fallback).
- Do not use generic stock imagery for industry cards.

### Section 3 — How Our Advice Changes By Industry
- Recommended implementation: two- or three-column text layout, or a clean single-column narrative.
- Optional: a contrast example showing two different industry profiles side-by-side.
- No icons or graphics required.

### Section 4 — Common Industry-Specific Business and Legal Issues
- Recommended implementation: tabbed interface (one tab per industry) or accordion.
- Each industry tab/accordion: list of four to six issues, stated as business problems.
- Alternatively: issue grid with industry label and bullet points.

### Section 5 — Related Resources / Where To Go Next
- Recommended implementation: link cards or a structured list.
- Each entry: Level 3 page name, one-sentence descriptor, link.
- Include a fallback card for General Inquiry.

### Section 6 — Contact / CTA
- Recommended implementation: full-width CTA section at the bottom of the page.
- Two to four sentences of copy.
- One primary button: links to Inquiries.
- Optional secondary link: links to the most relevant Level 3 page.
- No form fields on this page.

---

## 5. URL and Navigation Notes

**Canonical URL for this page:** `/industries` (with or without trailing slash, but consistent).

**Navigation label:** Industries (preferred) or Industries Served.

**Where this page must be linked from:**
- Primary navigation (homepage and all site pages).
- Homepage secondary feature section (if applicable).
- Footer navigation (under Industry links or primary links).

**Where Level 3 pages will be linked from:**
- This Industries page (Section 2 cards and Section 5 resources).
- Relevant blog posts and resources.
- Services page (cross-link where industry and service overlap is relevant).

---

## 6. Legacy URL Reconciliation (POL-051 Section 5.4 Obligation)

The following legacy URLs were identified in the source page review and must be reconciled:

| Legacy URL | Current Behavior | Recommended Action |
|---|---|---|
| /ontario | Redirects to /ontario-corporation-vs-federal-corporation/ (blog post) | Evaluate: retain redirect if blog post is kept; retarget if a canonical Ontario-focused Level 3 page is created |
| /ontario1 | Resolves to a franchise law soft landing page at /ontario1/ | Evaluate: assign a canonical URL if this becomes a production Level 3 page; otherwise retire |
| /industries1 | 404 | Remove redirect if any exists; no production content |
| /industries2 | 404 | Remove redirect if any exists; no production content |

These reconciliation decisions require ML1 direction. They are noted here as open items that affect the final site architecture but do not block the Industries pillar page build.

---

## 7. Level 3 Pages — Build Sequencing

The Industries pillar page creates the routing structure. The Level 3 pages are the downstream build. Recommended build order based on ICP priority:

| Priority | Level 3 Page | ICP | Funnel |
|---|---|---|---|
| 1 | /industries/payments-fintech | ICP-02 | F03 |
| 2 | /industries/construction | ICP-01 | F02 |
| 3 | /industries/managed-services | ICP-01 | F02 |
| 4 | /industries/health-wellness | ICP-01 | F02 |
| 5 | /industries/food-agriculture | ICP-01 | F02 |
| 6 | /industries/energy-logistics | ICP-01 | F02 |

Each Level 3 page build will require its own content brief, strategy brief, and QA cycle consistent with this workflow.

---

## 8. GoHighLevel Integration (If Applicable)

If the Industries page is built in GoHighLevel rather than WordPress:

- Use a funnel or website page type in GHL (not a standalone funnel with conversion tracking — this is an informational pillar page, not a funnel page).
- Do not attach a lead form or GHL automation to this page.
- Lead capture and CRM activity should be triggered from Level 3 pages, not from the Industries Level 2 page.
- The Level 2 Industries page links to Level 3 pages, where GHL forms and automation are appropriate.

---

## 9. Open Items Requiring ML1 Direction

The following items cannot be resolved without ML1 input:

1. Canonical domain: is the Industries page being built for `levinelegal.ca` (current) or `levine-law.ca` (migration target)?
2. Legacy URL reconciliation decisions (see Section 6 above).
3. Level 3 page build priority and timeline authorization.
4. Whether a GoHighLevel or WordPress implementation is target for this page.
5. Whether the current /ontario1 franchise soft landing page should be canonicalized or retired.

---

*Status: DRAFT — Pending ML1 Approval*
