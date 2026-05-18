---
id: PAGE_ARCHITECTURE
title: Page Architecture — Level 2 Industries Pillar Page
owner: ML1
status: draft
created_date: 2026-03-21
agent: MKT_WEBSITE_IMPLEMENTATION_AGENT
last_updated: 2026-05-18
---

# Page Architecture — Level 2 Industries Pillar Page

## 1. Overview

This document defines the structural design of the Level 2 Industries / Industries Served pillar page for Levine Law, consistent with POL-051 and the orchestration brief.

The page has two functions:
1. Educate visitors about why industry context matters to legal and structural advice.
2. Route visitors to the correct Level 3 pages for their industry or situation.

It does not attempt conversion. It does not carry the burden of the homepage, the Services page, or the Inquiries page.

---

## 2. Page Metadata

| Field | Value |
|---|---|
| Canonical URL (target) | `/industries` or `/industries-served` |
| Page level | Level 2 |
| Navigation placement | Primary nav |
| Parent page | Home |
| Primary routing function | Routes to Level 3 industry / client-profile pages |
| Secondary routing function | Routes to Inquiries if no Level 3 match |
| CTA type | Navigational (not lead capture) |
| Form present | No |
| Testimonials | No |
| Practice area content | No — that belongs on Services page |

---

## 3. Section Layout

The page is structured in exactly six sections. Section numbering is for production reference only and does not appear in published copy.

---

### Section 1: Intro / Why Industry Context Matters

**Purpose:** Establish the premise of the page — that industry context is not background noise; it shapes the legal, structural, regulatory, and governance issues a business faces.

**Content type:** Short narrative introduction. Two to four paragraphs maximum.

**Design guidance:**
- Hero or near-hero placement — the first thing a visitor sees after the page header.
- No form. No CTA button at this point. Let the visitor read.
- Clean, high-contrast layout. No decorative imagery that competes with the copy.

**What to avoid:**
- "We serve many industries" (generic, meaningless).
- Listing services in this section (that is the Services page job).
- Any language that sounds like a tagline or headline ad.

---

### Section 2: Industries We Serve

**Purpose:** Present a clean, business-facing list of the specific industries the firm works in.

**Content type:** List or card grid. One short descriptor per industry (one to two sentences max).

**Industries to include (based on approved positioning):**
- Construction and Real Estate
- Health and Wellness / Professional Services
- Managed Services and Technology
- Food, Agriculture, and Consumer Goods
- Energy and Logistics
- Payments / Fintech / MSB / PSP (ICP-02 — must be present)

**Design guidance:**
- Card or grid layout preferred — makes the list scannable.
- Each entry should link to the relevant Level 3 page (when those pages exist).
- In the interim (before Level 3 pages are built), entries can link to the Inquiries page with a contextual query string or anchor.
- No icons or decorative elements that substitute for substantive description.

**What to avoid:**
- Generic descriptors ("we help businesses in this industry grow").
- Repetitive sentence structures across all six entries.
- Marketing superlatives.

---

### Section 3: How Our Advice Changes By Industry

**Purpose:** Demonstrate that Levine Law does not apply one-size-fits-all legal advice. The nature of the business determines the nature of the legal and structural work.

**Content type:** Narrative explanation, optionally supported by a two- or three-column comparison format.

**Design guidance:**
- Two to three focused paragraphs, or a side-by-side comparison showing two contrasting industry profiles.
- Example contrast: a construction company (project-heavy contracts, subcontractor risk, corporate structure for growth) versus a payments operator (regulatory licensing, AML compliance, payment processing agreements).
- This section differentiates the firm from a generalist practice.

**What to avoid:**
- Legal advice.
- Claiming specialization in a way that conflicts with law society advertising rules.
- Overpromising outcomes.

---

### Section 4: Common Industry-Specific Business and Legal Issues

**Purpose:** List concrete, recognizable issues by industry. Visitors should read these and recognize their own situation.

**Content type:** Industry-by-industry issue list. Can be tabbed, expandable, or structured as a grid with callout boxes.

**Design guidance:**
- Group issues by industry or by issue type (structural, regulatory, contractual, governance, growth).
- Each issue stated as a recognizable business problem, not a legal theory.
- Four to six issues per industry maximum.
- Keep it scannable.

**Content range (by industry category):**
- Construction: project contract risk, subcontractor disputes, shareholder structure for scaling, bonding and surety issues.
- Health and Wellness: employment law for clinical staff, franchise and licensing compliance, professional corporation structure.
- Managed Services / Technology: MSA clarity, IP ownership and work-for-hire, vendor contract stacking, team structure.
- Payments / Fintech / MSB / PSP: MSB registration, AML compliance, RPAA obligations, payment processing agreements, licensing gaps.
- Food and Agriculture: supplier agreements, distribution contracts, franchise law intersections, corporate governance for scaling.
- Energy and Logistics: large commercial contracts, joint ventures, corporate structure for project-specific entities.

**What to avoid:**
- Legal advice or outcome guarantees.
- Framing issues as emergencies or crises.
- Duplicating Services page content.

---

### Section 5: Related Resources / Where To Go Next

**Purpose:** Perform the internal-routing function. Tell visitors which Level 3 page is right for them.

**Content type:** Link section with short descriptors.

**Design guidance:**
- Presented as a list or card grid of Level 3 page links.
- Each link entry should identify: the page name, who it is for, what it covers.
- Include a fallback link to the Inquiries page for visitors whose situation does not map to a specific Level 3 page.

**Recommended Level 3 page links (to be built):**
- Ontario Operating Companies — corporate structure and governance
- Construction and Real Estate Businesses — contracts, structure, scaling
- Health and Wellness Operators — corporate clarity and compliance
- Managed Services and Technology Companies — MSA, IP, structure
- Payments / Fintech / MSB / PSP Operators — regulatory counsel and compliance
- General Inquiry — if none of the above fit

**What to avoid:**
- Linking to blog posts as if they were landing pages.
- Linking to external resources.
- Making this section feel like a sidebar (it performs a critical routing function).

---

### Section 6: Contact / CTA

**Purpose:** Provide a clear, restrained next-step option for visitors who are ready to engage but have not yet identified a specific Level 3 page.

**Content type:** Short copy block with one or two links/buttons.

**Design guidance:**
- Two to four sentences maximum.
- Link to the Inquiries page as the primary path.
- Optionally include a secondary link to the most relevant Level 3 page if context is clear.
- No form on this page.
- No "free consultation" language as the primary offer.
- No urgency framing.

**Acceptable CTA language direction:**
- Route to the appropriate page for the visitor's industry.
- Invite them to reach out through the Inquiries page.
- Align with the firm's maturity-gated, paid-diagnostic entry model.

**What to avoid:**
- "Call us now."
- "Get a free consultation today."
- Any language that mimics a lead-gen landing page.

---

## 4. Homepage Link Recommendation

The Industries page must be linked from the homepage in the primary navigation per POL-051 section 5.3.

**Recommended primary nav label:** Industries
**Recommended fallback label:** Industries Served

**Additional homepage consideration:** If the homepage carries a secondary feature section highlighting the three Level 2 pages (Industries, Services, Inquiries), the Industries entry should be accompanied by a brief descriptor such as:

> "We work with operating businesses across selected industries. Industry context shapes structure, governance, and regulatory exposure."

This descriptor reinforces the Level 2 function without duplicating the full pillar page.

---

## 5. Level 2 to Level 3 Link Map

```
/industries  (Level 2 — this page)
  |
  +-- /industries/construction        (Level 3 — Construction and Real Estate)
  +-- /industries/health-wellness     (Level 3 — Health and Wellness)
  +-- /industries/managed-services    (Level 3 — Managed Services and Technology)
  +-- /industries/food-agriculture    (Level 3 — Food, Agriculture, and Consumer Goods)
  +-- /industries/energy-logistics    (Level 3 — Energy and Logistics)
  +-- /industries/payments-fintech    (Level 3 — Payments / Fintech / MSB / PSP)
  |
  +-- /inquiries                      (Level 2 fallback — General Inquiry path)
```

Level 3 pages are not yet built. This map defines the target architecture. The Industries page should be built with placeholder links to these Level 3 URLs so they can be activated as pages are built.

---

## 6. Page Boundaries

The Industries page stops at:
- Routing to Level 3 pages (it does not attempt to serve the Level 3 function).
- General framing of industry-specific issues (it does not provide legal advice).
- Restrained CTA that routes to Inquiries or Level 3 (it does not host a conversion form).

The Industries page does not:
- Describe specific services or engagement models (Services page function).
- Collect lead information (Level 3 page or Inquiries page function).
- Provide a firm introduction or overview (Homepage function).

---

*Status: DRAFT — Pending ML1 Approval*
