---
id: CMO_PRE_BUILD_REVIEW_INDUSTRIES_v1
title: CMO Pre-Build Review — Industries We Serve (Thrive Architect Build Packet)
owner: ML1
status: complete
created_date: 2026-03-21
reviewer: MKT_CHIEF_MARKETING_OFFICER_AGENT
source_packet: THRIVE_BUILD_PACKET.md
source_copy: INDUSTRIES_PILLAR_PAGE_DRAFT_v2.md
policy_refs: POL-051, POL-049, POL-050
approval: pending ML1
last_updated: 2026-05-18
---

# CMO Pre-Build Review — Industries We Serve

**Build packet reviewed:** `THRIVE_BUILD_PACKET.md`
**Copy source reviewed:** `INDUSTRIES_PILLAR_PAGE_DRAFT_v2.md`
**Review date:** 2026-03-21
**Reviewer:** MKT_CHIEF_MARKETING_OFFICER_AGENT
**INV-0002 applies:** No live changes authorized.

---

## 1. Copy Accuracy

**Finding: PASS WITH THREE MINOR VARIANCES**

The build packet is substantively faithful to the approved v2 copy. The following specific variances were identified on a line-by-line comparison.

### 1A. Hero subheading — abridged from approved copy

Approved v2 hero body text reads:

> "The legal and structural questions a business faces depend on the industry it operates in. What matters for a software company is different from what matters for a construction company or a payments operator. We work with operating businesses across six industry categories. This page explains who we serve, how the work differs by sector, and where to go next."

Build packet renders this as:

> "The legal and structural questions a business faces depend on the industry it operates in. Levine Law works with operating businesses across six industry categories."

The second sentence of v2 ("What matters for a software company is different from what matters for a construction company or a payments operator.") and the orienting third and fourth sentences ("This page explains who we serve, how the work differs by sector, and where to go next.") are omitted.

Assessment: The omission of the orienting sentences is a deliberate compression for the hero, which is acceptable for layout reasons. However, the removal of "This page explains who we serve, how the work differs by sector, and where to go next" removes the only sentence that tells the visitor explicitly what to expect from the page. ML1 should decide whether to restore it or consciously accept the shorter version. This is not blocking but warrants ML1 attention.

### 1B. Card 3 descriptor — minor wording variance

Approved v2: "General contractors, subcontractors, project-based operators, and **real estate businesses operating in Ontario**."

Build packet: "General contractors, subcontractors, project-based operators, and **property development businesses in Ontario**."

The phrase "real estate businesses" in v2 has been replaced with "property development businesses." This is consistent with the card heading "Construction & Property Development" and is arguably an improvement in precision. ML1 should confirm this substitution is intentional.

### 1C. Section 4 — Professional Services & Healthcare: one bullet omitted

Approved v2 includes six bullet points for this accordion panel:

1. Service and retainer agreements that don't define scope, deliverables, or liability clearly
2. Professional corporation structure misaligned with current ownership or partnership arrangements
3. IP and work-product ownership unclear in client-facing or subcontractor relationships
4. Clinical employment agreements that don't reflect the regulatory environment of the practice
5. Corporate structure not updated as the firm or practice grew
6. Early equity and profit-sharing arrangements that were never properly documented

Build packet includes only five bullets, omitting bullet 5: "Corporate structure not updated as the firm or practice grew."

This is a factual omission from the approved copy. It is not blocking (the five remaining bullets are accurate), but it should be restored before build to match the approved source.

### 1D. Section 4 — Construction accordion link text variance

Approved v2 link text: "Learn more about Construction & Real Estate →"
Build packet link text: "Learn more about Construction & Property Development →"

The build packet version is more consistent with the heading taxonomy used throughout the page ("Construction & Property Development"). This appears to be a correction of v2 copy rather than an error. ML1 should confirm intent, but this is not blocking.

### 1E. Section 5 CTA text — minor paraphrase

Approved v2: "If you've **found** the category that fits, the relevant page above is the best next step."
Build packet: "If you've **identified** the category that fits, the relevant page above is the best next step."

The substitution of "found" with "identified" is a trivial paraphrase with no material meaning difference. Not blocking.

---

## 2. Structural Compliance — POL-051

**Finding: PASS**

POL-051 requires the Industries page (Level 2) to be primarily educational, organizational, and navigational — and explicitly prohibits it from behaving like a hard-conversion landing page.

The build packet satisfies this:

- Section 1 (Why Industry Context Matters) is educational.
- Section 2 (Industry card grid) is organizational and navigational.
- Section 3 (Comparison table) is educational and differentiating.
- Section 4 (Accordion) routes users downward to Level 3 pages.
- Section 5 (CTA) is a soft close: the first line explicitly directs users to the Level 3 pages before mentioning the /inquiries route. There is no urgency language, no lead-capture form, and no hard-sell.

The page does not collapse the Industries, Services, and Inquiries functions into one surface. The CTA routes first to Level 3 and only secondarily to /inquiries for users who have not yet identified their category. This is correct POL-051 behavior.

The Level 3 slugs used as card link targets and accordion link targets are structurally consistent with the canonical routing model defined in POL-051 Section 6.

**No POL-051 violations found.**

---

## 3. CTA Correctness

**Finding: PASS**

### Final CTA button

The Section 5 "GET IN TOUCH" button is specified to route to `/inquiries`. This is correct.

### Accordion "Learn more" links — all 6 verified

| Toggle | Link target in packet | Expected slug |
|---|---|---|
| Technology, Software & Digital Platforms | /industries/technology-software | Correct |
| Payments, Fintech & Financial Services | /industries/payments-fintech-msb | Correct |
| Construction & Property Development | /industries/construction-property-development | Correct |
| Professional Services & Healthcare | /industries/professional-services-healthcare | Correct |
| Manufacturing, Wholesale & Distribution | /industries/manufacturing-wholesale-distribution | Correct |
| Consumer, Food & Retail | /industries/consumer-food-retail | Correct |

### Industry card "Learn more" links — all 6 verified

All 6 card link targets match the accordion link targets and the canonical Level 3 slugs defined in v2. No mismatches found.

### Hero anchor button

"Explore Industries →" routes to `#industries-grid`. The Section 2 container is specified with `HTML ID: industries-grid`. The anchor is internally consistent.

**All routing is correct.**

---

## 4. Brand Compliance — POL-049 and POL-050

**Finding: PASS**

### Color palette

The packet uses the following color values:

| Color | Role | POL-049 status |
|---|---|---|
| #1D4771 | Navy — primary, section backgrounds, headings | Approved (Primary) |
| #0365B2 | Blue — buttons, links, icons | Approved (Primary / Secondary) |
| #FFFFFF | White — section backgrounds, text on navy | Approved (Primary) |
| #F8F8F8 | Off-white — alternating section backgrounds, table rows | Not a named palette token |
| #D1D5DB | Border lines, subdued text on navy | Approved (Secondary) |
| #000000 | Body text on white | Approved (Secondary) |

The only color used that is not explicitly listed in POL-049 is #F8F8F8. It appears in alternating section backgrounds and table row striping. This is a near-white neutral used purely for layout rhythm, not as a brand color. It does not conflict with any palette token and creates no identity confusion. Assessment: acceptable functional neutral; not a POL-049 violation.

The build packet explicitly confirms that #FF5E5B (red accent) and #4BD1FB (light blue) do not appear on this page. This is consistent with the page's function — neither token is appropriate for a content-heavy pillar page, and their deliberate exclusion is correct.

### Typography

All elements use Inter. No serif or display fonts are specified. This is compliant with POL-050 Section 4.2.

### Image style

The packet specifies: "Placeholder — rectangular photo of Toronto architectural detail (clock tower or glass building facade). NOT stock legal imagery (no gavels, no handshakes, no courtrooms)."

This is compliant with POL-050 Section 4.4 and POL-050/PRN-033 (image style restraint). The placeholder note correctly excludes cliche legal imagery. However, the image has not yet been procured — this is flagged as an open item below.

### Layout and whitespace

Generous padding (72px top/bottom on most sections, 80px on hero), clear grid discipline, and alternating section backgrounds are specified. No clutter indicators. Compliant with POL-050 Section 4.3.

**No brand compliance violations found.**

---

## 5. Completeness

**Finding: PASS — packet is execution-ready with noted open items**

The packet provides:

- Global CSS block ready to paste
- Section-by-section element-by-element build instructions in Thrive Architect sequence
- Complete element settings (tag, font, size, weight, color, line-height, padding, margin, border-radius, box-shadow) for every element
- All 6 card content blocks
- All 6 accordion content blocks with full copy
- Responsive behavior specification (desktop / tablet / mobile breakpoints)
- WordPress page setup checklist (slug, template, draft status)
- Post-build link verification checklist
- SEO field values (title, meta description, canonical, robots, focus keyphrase with character counts verified)
- Menu assignment instruction
- INV-0002 acknowledgment on the final publish step

The quick-reference element build order is a useful execution aid and is structurally accurate.

**Nothing required to execute the build is absent from the packet.** The open items below are either pre-existing placeholders (hero image) or minor copy corrections that can be addressed in Thrive Architect during build.

---

## 6. Open Items Before Execution

The following items are noted. They are categorized as BLOCKING or NON-BLOCKING.

### BLOCKING items

None.

### NON-BLOCKING items requiring ML1 decision or attention

**OI-1 — Hero image not yet procured**

The hero image slot is specified as a placeholder ("Toronto architectural detail — clock tower or glass building facade"). No approved asset exists yet. ML1 must source or commission this before the page can be published. The page can be built and placed in draft with the placeholder; the image can be swapped before publishing. This does not block the build step but does block publishing.

**OI-2 — Hero subheading: confirm compressed version is intentional**

The build packet compresses the v2 hero body from four sentences to two, dropping the orienting line "This page explains who we serve, how the work differs by sector, and where to go next." ML1 should confirm this compression is accepted or request restoration of the orienting sentence.

**OI-3 — Card 3 descriptor: confirm "property development businesses" vs. "real estate businesses"**

Build packet uses "property development businesses in Ontario" where v2 reads "real estate businesses operating in Ontario." Confirm substitution is intentional.

**OI-4 — Professional Services & Healthcare accordion: restore omitted bullet**

The build packet omits bullet 5 from the v2-approved list ("Corporate structure not updated as the firm or practice grew"). This should be added to the accordion body content in Thrive Architect during build.

**OI-5 — Construction accordion link text: confirm heading taxonomy alignment**

Build packet uses "Learn more about Construction & Property Development →" where v2 reads "Learn more about Construction & Real Estate →." The build packet version is more internally consistent with the heading. Confirm ML1 preference.

**OI-6 — Level 3 pages do not yet exist**

All 6 card links and accordion links route to Level 3 slugs that have not been built yet. These links will return 404 errors until the Level 3 pages are created. ML1 should be aware that publishing /industries before the Level 3 pages exist will result in broken internal links. Options: (a) hold publishing until at least the Level 3 pages are in draft/published, (b) publish /industries now and accept temporary 404s, or (c) disable the "Learn more" links in the initial publish and add them progressively. This does not block the build step but is a publishing sequencing decision for ML1.

**OI-7 — Domain placeholder in canonical URL**

The SEO checklist specifies `https://[domain]/industries` for the canonical URL. ML1 must replace `[domain]` with the live domain before publishing.

---

## Summary

| Review dimension | Result |
|---|---|
| Copy accuracy vs. v2 | Pass — 5 minor variances, 1 omitted bullet to restore (OI-4) |
| Structural compliance — POL-051 | Pass |
| CTA routing — /inquiries | Pass |
| Accordion / card slug routing | Pass — all 6 correct |
| Brand palette — POL-049 | Pass |
| Typography — POL-050 | Pass |
| Image style — POL-050 | Pass (placeholder compliant; asset not yet sourced) |
| Packet completeness | Pass — execution-ready |
| Blocking items | None |

---

## VERDICT

**APPROVED FOR ML1 EXECUTION**

The build packet is structurally sound, copy-faithful to the approved source with only minor and documented variances, brand-compliant, correctly routed, and complete enough to execute in Thrive Architect without gaps.

ML1 may proceed with the Thrive Architect build in draft mode.

Before publishing (not before building):
- Resolve OI-1 (hero image)
- Restore OI-4 (Professional Services & Healthcare omitted bullet — can be corrected during build)
- Decide OI-6 (Level 3 page sequencing)
- Replace OI-7 (domain placeholder in canonical URL)

OI-2, OI-3, and OI-5 are minor copy alignment questions that ML1 can resolve at any point before publish.

INV-0002 applies. No publication authorized until ML1 explicitly advances page status from Draft to Published.

---

*Produced by MKT_CHIEF_MARKETING_OFFICER_AGENT. No live changes made. Draft state only.*
