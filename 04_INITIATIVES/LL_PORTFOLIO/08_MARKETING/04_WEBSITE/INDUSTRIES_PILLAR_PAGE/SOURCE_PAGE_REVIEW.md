---
id: SOURCE_PAGE_REVIEW
title: Source Page Review — Industries Pillar Page Build
owner: ML1
status: draft
created_date: 2026-03-21
agent: MKT_MARKETING_STRATEGY_AGENT
last_updated: 2026-05-18
---

# Source Page Review — Industries Pillar Page Build

## Review Purpose

This document reviews the five source pages specified in the orchestration brief. The purpose is to extract what the current site is doing, identify what is worth preserving, and flag what must be discarded or restructured for the canonical Level 2 Industries pillar page.

---

## Page-by-Page Review

---

### 1. levinelegal.ca/industries (redirects to /industries/)

**HTTP Status:** 301 redirect to /industries/ — 200 OK at destination.

**What the page is doing:**

The current /industries page is a composite page attempting to serve multiple functions simultaneously. It functions partly as a homepage substitute and partly as a practice-area overview. It contains:

- A hero section with generic copy: "We provide quality legal services advice and representation for entrepreneurs, executives and investors in a wide range of industrieses." (Note: typo "industrieses" present in live copy.)
- A list of industry categories with short descriptors: Agriculture and Food, Health and Wellness, Financial Services, Managed Services, Energy and Logistics, Construction.
- Short one-to-two sentence blurbs per industry, each with a "Learn more" call to action.
- A firm overview section ("Toronto Business Lawyers") with a brief paragraph and a secondary CTA ("Discover more").
- A quality and mission statement section with a process schematic.
- Practice area descriptions for Corporate Law and Contract Law.
- Client testimonials.
- Footer navigation referencing: About, Industries, Services, Corporate Law, Contract Law, Corporate Structure, Franchise, Fintech.

**What to keep:**

- The industry list itself (Agriculture and Food, Health and Wellness, Financial Services, Managed Services, Energy and Logistics, Construction) provides a starting signal for the industries the firm historically served. This list should be reviewed against current ICP targeting before adoption.
- The "Learn more" per-industry routing pattern is structurally correct as a Level 2 to Level 3 link model — the pattern is right even if the execution is weak.

**What to discard:**

- The generic hero copy is too broad and unfocused for a Level 2 pillar page. "Wide range of industrieses" is both typoed and vague.
- The practice area content (Corporate Law, Contract Law descriptions) belongs on the Services page, not the Industries page. Its presence here collapses the Services and Industries functions in direct violation of POL-051 section 5.1.
- The process schematic and quality mission statement are homepage-style content. They do not belong on a Level 2 pillar page.
- The testimonials section belongs at the Level 3 page level or on the homepage, not embedded in the Industries pillar page.
- No ICP-02 (Fintech/Payments/MSB/PSP) content is present on this page despite being a named ICP in approved positioning.
- No reference to the firm's maturity-gated, preventative positioning. The page reads as a general directory.

**Verdict:** Significant structural overhaul required. The industry list is the only usable raw material. All practice-area content, testimonials, and generic mission copy must be removed from this page.

---

### 2. levinelegal.ca/industries1

**HTTP Status:** 404 — Page Not Found.

**What the page is doing:** Does not exist as a live page.

**What to keep:** Nothing. No content available.

**What to discard:** N/A — page is absent.

**Verdict:** Non-existent page. No source material. Treat as a blank slate. The canonical Industries page being built in this project replaces any such placeholder.

---

### 3. levinelegal.ca/industries2

**HTTP Status:** 404 — Page Not Found.

**What the page is doing:** Does not exist as a live page.

**What to keep:** Nothing. No content available.

**What to discard:** N/A — page is absent.

**Verdict:** Non-existent page. No source material. Same disposition as industries1.

---

### 4. levinelegal.ca/ontario (redirects to /ontario-corporation-vs-federal-corporation/)

**HTTP Status:** 301 redirect to /ontario-corporation-vs-federal-corporation/ — 200 OK at destination.

**What the page is doing:**

The /ontario URL resolves to a blog post titled "Ontario Corporation vs Federal Corporation." This is a general-audience educational article from the early firm blog era. The content covers:

- Provincial vs. federal incorporation considerations (geography of operations, shareholder meeting rules, name availability, administrative cost and timing).
- Written in a casual, first-person voice ("Hey Guys!").
- Aimed at first-time entrepreneurs.
- No specific industry context. No ICP alignment.

**What to keep:**

- The topic (provincial vs. federal incorporation) is a legitimate structural question that operating businesses face. It could inform a Level 3 page on corporate structure or a services-specific page.
- The substantive legal information (CBCA vs. OBCA, residency requirements, name protection) is accurate and could be the basis for a properly positioned thought-leadership piece.

**What to discard:**

- The casual blog tone ("Hey Guys!") is inconsistent with the firm's current brand posture of calm authority.
- This page is mislabeled as an "ontario" page — the URL implies Ontario-specific industry or client targeting, but the content is a general incorporation comparison.
- It does not function as an industry page, a client-profile page, or a soft landing page. It is pure blog content.
- The /ontario URL redirect is a legacy artifact that should be reconciled per POL-051 section 5.4.

**Verdict:** Not a source for the Industries pillar page. The underlying content may eventually support a Level 3 service-specific or resource page with appropriate tone revision. The /ontario redirect is a legacy URL that should be reviewed separately against POL-051.

---

### 5. levinelegal.ca/ontario1 (redirects to /ontario1/)

**HTTP Status:** 301 redirect to /ontario1/ — 200 OK at destination.

**What the page is doing:**

The /ontario1 page is a franchise law soft landing page. The content covers:

- Franchise law services: agreement review, disclosure review, transfers, exits, termination, rescission.
- Audience segmentation: Entrepreneurs, Executives, Investors.
- Industry-specific franchise categories: Education and Child Services, Health Wellness and Fitness, Food and Beverage, Retail and Specialty Shops.
- A lead capture form (Name, Email, Phone).
- Testimonials.

**What to keep:**

- The per-audience framing (Entrepreneurs, Executives, Investors) is structurally sound.
- The industry-specific franchise breakdown (Education, Health, Food, Retail) shows how the firm has previously segmented industries within a specific practice area — this is a valid Level 3 pattern.
- The service description language is more specific than the /industries page.

**What to discard:**

- The lead capture form and aggressive opt-in behavior is appropriate for a Level 3 page, which this appears to be. It should not be replicated at the Level 2 Industries page.
- The page URL (/ontario1) suggests this is a draft or test variant of a soft landing page, not a canonical production URL.
- Franchise law is a practice area, not an industry category. This page conflates practice area and industry category in a way that should be separated in the new architecture.
- Testimonials should remain at Level 3, not migrate to the Level 2 pillar.

**Verdict:** This is effectively a Level 3 soft landing page for franchise law — not an industry page. Its structure (audience segmentation, specific service list, opt-in form) confirms the correct Level 3 pattern. It informs what Level 3 pages should look like beneath the Industries pillar, but contributes no content to the Level 2 Industries page itself.

---

## Cross-Page Summary Findings

**Industries the current site addresses (from /industries):**
- Agriculture and Food
- Health and Wellness
- Financial Services
- Managed Services
- Energy and Logistics
- Construction

**Industries implied by ICP doctrine but absent from site:**
- Fintech / Payments / MSB / PSP (ICP-02) — entirely absent from the /industries page despite being a named ICP with its own funnel (F03).

**Structural problems identified across source pages:**
1. The /industries page mixes Level 2 pillar functions with Level 3 service and conversion content — violates POL-051 section 5.1 and 5.2.
2. No clear Level 2 to Level 3 routing architecture is visible on the current site.
3. The /ontario and /ontario1 URLs are legacy redirects to blog and soft landing content — not canonical industry pages.
4. No ICP-02 (Payments/Fintech) presence in the current industry structure.
5. The current industries page reads like a firm overview page, not a sector-organized routing hub.

**Tone audit:**
- Current copy ranges from generic ("quality legal services") to casual blog voice ("Hey Guys!").
- Neither register matches the approved brand posture of calm authority, preventative orientation, and operator alignment.

---

## Disposition Decisions

| Source Page | Disposition |
|---|---|
| /industries | Structural overhaul. Industry list is the only usable material. All services and conversion content removed. |
| /industries1 | 404 — no content. Treat as non-existent. |
| /industries2 | 404 — no content. Treat as non-existent. |
| /ontario | Legacy redirect to blog post. Not relevant to Industries page build. Flag for POL-051 reconciliation. |
| /ontario1 | Legacy soft landing page (franchise). Confirms Level 3 page pattern. Does not contribute content to Level 2 page. |

---

*Status: DRAFT — Pending ML1 Approval*
