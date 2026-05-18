---
id: THRIVE_BUILD_PACKET_INDUSTRIES_v1
title: Thrive Architect Build Packet — Industries We Serve
owner: ML1
status: draft
created_date: 2026-03-21
page: /industries
platform: Thrive Architect + WordPress
approval: pending ML1 review
last_updated: 2026-05-18
---

# Thrive Architect Build Packet — Industries We Serve

**Source copy:** `INDUSTRIES_PILLAR_PAGE_DRAFT_v2.md`
**HTML reference:** `industries_draft.html`
**Brand palette:** POL-049 active state
**Typography:** Inter (Google Fonts)

This packet is an element-by-element construction guide for ML1 to execute in Thrive Architect. Every section is specified in the order it appears on the page, top to bottom. No live changes have been made.

---

## PRE-BUILD: GLOBAL CSS

Before building any sections, enter the following CSS block in **Thrive Dashboard > Global CSS** (or **WordPress Customizer > Additional CSS**). This CSS must be present before you apply the custom classes referenced in Section 2, Section 3, and Section 4.

```css
/* ============================================================
   LEVINE LAW — INDUSTRIES PAGE GLOBAL CSS
   Enter in: Thrive Dashboard > Global CSS
             OR WordPress Customizer > Additional CSS
   ============================================================ */

/* Google Fonts — Inter (add only if not already loaded by theme) */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

/* ---- Section 2: Industry card hover ---- */
.ll-industry-card {
  transition: box-shadow 0.2s ease, transform 0.2s ease;
}
.ll-industry-card:hover {
  box-shadow: 0 6px 24px rgba(0, 0, 0, 0.14);
  transform: translateY(-3px);
}

/* ---- Section 3: Comparison table ---- */
.ll-comparison-table {
  width: 100%;
  border-collapse: collapse;
  font-family: Inter, system-ui, sans-serif;
  font-size: 15px;
}
.ll-comparison-table thead th {
  background: #1D4771;
  color: #FFFFFF;
  font-weight: 600;
  padding: 14px 20px;
  text-align: left;
}
.ll-comparison-table tbody tr:nth-child(even) {
  background: #F8F8F8;
}
.ll-comparison-table tbody tr:nth-child(odd) {
  background: #FFFFFF;
}
.ll-comparison-table tbody td {
  padding: 14px 20px;
  border-bottom: 1px solid #D1D5DB;
  vertical-align: top;
  color: #000000;
  line-height: 1.5;
}
.ll-comparison-table tbody td:first-child {
  width: 32%;
  white-space: nowrap;
}
@media (max-width: 768px) {
  .ll-comparison-table tbody td:first-child {
    white-space: normal;
    width: auto;
  }
  .ll-comparison-table {
    font-size: 14px;
  }
  .ll-comparison-table thead th,
  .ll-comparison-table tbody td {
    padding: 10px 12px;
  }
}

/* ---- Section 4: Accordion ---- */
.ll-accordion .tve-toggle-header {
  border-radius: 6px 6px 0 0;
  transition: background 0.15s ease, color 0.15s ease;
}
.ll-accordion .tve-toggle-content {
  border: 1px solid #D1D5DB;
  border-top: none;
  border-radius: 0 0 6px 6px;
}
.ll-accordion + .ll-accordion {
  margin-top: 8px;
}
```

---

## SECTION: HERO

### Container element

| Setting | Value |
|---|---|
| Element | Content Box |
| Background color | #1D4771 |
| Padding top | 80px |
| Padding bottom | 80px |
| Padding left | 5% |
| Padding right | 5% |

### Inner layout

| Setting | Value |
|---|---|
| Element | Columns |
| Column count | 2 |
| Column widths | 45% / 55% |
| Vertical align | Center |
| Gap | 48px |
| Stack on mobile | Yes (breakpoint 767px) |

---

### Hero — Column 1 (left, image)

**Element: Image**

| Setting | Value |
|---|---|
| Source | Placeholder — rectangular photo of Toronto architectural detail (clock tower or glass building facade). NOT stock legal imagery (no gavels, no handshakes, no courtrooms). |
| Alt text | Toronto business district — Levine Law |
| Max-width | 420px |
| Alignment | Center |
| Border-radius | 16px |
| Box-shadow | 0 8px 32px rgba(0,0,0,0.25) |

---

### Hero — Column 2 (right, text)

**Element 1: Heading**

| Setting | Value |
|---|---|
| Tag | H1 |
| Text | Industries We Serve |
| Font | Inter |
| Size desktop | 52px |
| Size mobile | 36px |
| Weight | 700 |
| Color | #FFFFFF |
| Alignment | Left |
| Margin top | 0 |

**Element 2: Text**

| Setting | Value |
|---|---|
| Text | The legal and structural questions a business faces depend on the industry it operates in. Levine Law works with operating businesses across six industry categories. |
| Font | Inter |
| Size desktop | 18px |
| Size mobile | 16px |
| Color | #D1D5DB |
| Line-height | 1.6 |
| Margin top | 16px |

**Element 3: Button**

| Setting | Value |
|---|---|
| Label | Explore Industries → |
| Link | #industries-grid (page anchor — scroll to Section 2) |
| Background | #0365B2 |
| Text color | #FFFFFF |
| Font | Inter |
| Font size | 14px |
| Text transform | Uppercase |
| Font weight | 600 |
| Padding | 14px top/bottom, 32px left/right |
| Border-radius | 4px |
| Hover background | #1D4771 |
| Hover text color | #FFFFFF |
| Margin top | 28px |

---

## SECTION 1 — WHY INDUSTRY CONTEXT MATTERS

### Container element

| Setting | Value |
|---|---|
| Element | Content Box |
| Background color | #F8F8F8 |
| Padding top | 72px |
| Padding bottom | 72px |
| Padding left | 5% |
| Padding right | 5% |

### Inner layout

| Setting | Value |
|---|---|
| Element | Columns |
| Column count | 2 |
| Column widths | 55% / 45% |
| Vertical align | Top |
| Gap | 48px |
| Stack on mobile | Yes (breakpoint 767px) |

---

### Section 1 — Column 1 (left, text)

**Element 1: Heading**

| Setting | Value |
|---|---|
| Tag | H2 |
| Text | Industry context shapes the legal work. |
| Font | Inter |
| Size desktop | 32px |
| Size mobile | 26px |
| Weight | 700 |
| Color | #1D4771 |
| Alignment | Left |
| Margin top | 0 |

**Element 2: Text**

| Setting | Value |
|---|---|
| Text | It determines the regulatory framework that applies, the contracts that need to work, the governance structure that fits, and the risks that compound when left unaddressed. |
| Font | Inter |
| Size | 17px |
| Color | #000000 |
| Line-height | 1.65 |
| Margin top | 16px |

**Element 3: Text**

| Setting | Value |
|---|---|
| Text | Levine Law works with selected industries because informed, specific advice requires knowing the operating environment. |
| Font | Inter |
| Size | 17px |
| Color | #000000 |
| Line-height | 1.65 |
| Margin top | 12px |

---

### Section 1 — Column 2 (right, pull-quote card)

**Element: Content Box (nested)**

| Setting | Value |
|---|---|
| Background color | #1D4771 |
| Padding | 32px all sides |
| Border-radius | 8px |

Inside the nested Content Box:

**Element 1: Text (pull-quote body)**

| Setting | Value |
|---|---|
| Text | A payments operator entering Canada has different obligations than a construction company scaling its project portfolio. |
| Font | Inter |
| Size | 18px |
| Color | #FFFFFF |
| Line-height | 1.6 |
| Font style | Italic |

**Element 2: Text (attribution)**

| Setting | Value |
|---|---|
| Text | — Levine Law |
| Font | Inter |
| Size | 14px |
| Color | #D1D5DB |
| Margin top | 16px |

---

## SECTION 2 — INDUSTRIES WE SERVE

### Container element

| Setting | Value |
|---|---|
| Element | Content Box |
| HTML ID | industries-grid (set via Thrive element ID field — this is the scroll anchor target) |
| Background color | #FFFFFF |
| Padding top | 72px |
| Padding bottom | 72px |
| Padding left | 5% |
| Padding right | 5% |

### Section heading

**Element: Heading**

| Setting | Value |
|---|---|
| Tag | H2 |
| Text | The Industries We Work In |
| Font | Inter |
| Size desktop | 36px |
| Size mobile | 28px |
| Weight | 700 |
| Color | #1D4771 |
| Alignment | Center |
| Margin bottom | 48px |

### Card grid layout

| Setting | Value |
|---|---|
| Element | Columns |
| Column count | 3 (desktop) |
| Gap | 24px |
| At 768px | 2 columns (set in Thrive responsive controls) |
| At 480px | 1 column (set in Thrive responsive controls) |
| Vertical align | Top |

---

### Card component specification (apply identically to all 6 cards)

Each card is a **Content Box** element placed inside one column cell.

**Content Box settings:**

| Setting | Value |
|---|---|
| Background | #FFFFFF |
| Border | 1px solid #D1D5DB |
| Border-radius | 8px |
| Box-shadow | 0 2px 8px rgba(0,0,0,0.08) |
| Padding | 28px all sides |
| Custom CSS class | ll-industry-card |

Inside each card, place these elements in order:

1. **Icon** — 40x40px, color #0365B2 (see icon name per card below)
2. **Heading (H3)** — Inter 18px weight 700 color #1D4771, margin-top 12px
3. **Text (descriptor)** — Inter 15px color #000000 line-height 1.6, margin-top 8px
4. **Text ("Learn more →" link)** — Inter 14px color #0365B2 weight 600, margin-top 16px; configure as linked text to the slug listed below

---

### Card 1: Technology, Software & Digital Platforms

| Field | Value |
|---|---|
| Icon | code or layers (Thrive icon library) |
| H3 | Technology, Software & Digital Platforms |
| Descriptor | SaaS companies, IT service providers, software developers, marketplace operators, and digital platform businesses. |
| Link text | Learn more → |
| Link target | /industries/technology-software |

---

### Card 2: Payments, Fintech & Financial Services

| Field | Value |
|---|---|
| Icon | currency or payments (Thrive icon library) |
| H3 | Payments, Fintech & Financial Services |
| Descriptor | Money services businesses, payment service providers, stablecoin and crypto operators, and fintech companies with Canadian regulatory exposure. |
| Link text | Learn more → |
| Link target | /industries/payments-fintech-msb |

---

### Card 3: Construction & Property Development

| Field | Value |
|---|---|
| Icon | building or crane (Thrive icon library) |
| H3 | Construction & Property Development |
| Descriptor | General contractors, subcontractors, project-based operators, and property development businesses in Ontario. |
| Link text | Learn more → |
| Link target | /industries/construction-property-development |

---

### Card 4: Professional Services & Healthcare

| Field | Value |
|---|---|
| Icon | briefcase or clinic (Thrive icon library) |
| H3 | Professional Services & Healthcare |
| Descriptor | Agencies, consultants, accounting firms, staffing companies, medical and dental clinics, allied health providers, and professional corporations. |
| Link text | Learn more → |
| Link target | /industries/professional-services-healthcare |

---

### Card 5: Manufacturing, Wholesale & Distribution

| Field | Value |
|---|---|
| Icon | factory or warehouse (Thrive icon library) |
| H3 | Manufacturing, Wholesale & Distribution |
| Descriptor | Ontario manufacturers, importers, distributors, and wholesale operators managing supply chains, commercial contracts, and multi-entity corporate structures. |
| Link text | Learn more → |
| Link target | /industries/manufacturing-wholesale-distribution |

---

### Card 6: Consumer, Food & Retail

| Field | Value |
|---|---|
| Icon | storefront or shopping-bag (Thrive icon library) |
| H3 | Consumer, Food & Retail |
| Descriptor | Food producers, consumer goods companies, restaurants, retail operators, distributors, and franchise-model businesses. |
| Link text | Learn more → |
| Link target | /industries/consumer-food-retail |

---

## SECTION 3 — HOW OUR ADVICE CHANGES BY INDUSTRY

### Container element

| Setting | Value |
|---|---|
| Element | Content Box |
| Background color | #F8F8F8 |
| Padding top | 72px |
| Padding bottom | 72px |
| Padding left | 5% |
| Padding right | 5% |

### Section heading

**Element: Heading**

| Setting | Value |
|---|---|
| Tag | H2 |
| Text | The same legal playbook doesn't work across every business. |
| Font | Inter |
| Size desktop | 32px |
| Size mobile | 26px |
| Weight | 700 |
| Color | #1D4771 |
| Alignment | Left |
| Margin bottom | 32px |

### Comparison table

**Element: Custom HTML**

Paste the following HTML block exactly as written into the Custom HTML element:

```html
<table class="ll-comparison-table">
  <thead>
    <tr>
      <th>Industry</th>
      <th>What the legal work centres on</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Technology &amp; Software</strong></td>
      <td>IP ownership, MSA structure, contractor classification, equity documentation, SaaS contract terms</td>
    </tr>
    <tr>
      <td><strong>Payments &amp; Fintech</strong></td>
      <td>MSB registration, AML program design, FINTRAC compliance, RPAA obligations, payment processing agreements</td>
    </tr>
    <tr>
      <td><strong>Construction &amp; Property Development</strong></td>
      <td>Project contracts, subcontractor risk, corporate structure, shareholder transitions, asset separation</td>
    </tr>
    <tr>
      <td><strong>Professional Services &amp; Healthcare</strong></td>
      <td>Service agreements, professional corporation structure, clinical employment, IP ownership, equity arrangements</td>
    </tr>
    <tr>
      <td><strong>Manufacturing &amp; Distribution</strong></td>
      <td>Supply chain contracts, distribution agreements, multi-entity corporate structure, commercial terms</td>
    </tr>
    <tr>
      <td><strong>Consumer &amp; Retail</strong></td>
      <td>Supplier contracts, distribution terms, franchise structure, corporate governance for scaled businesses</td>
    </tr>
  </tbody>
</table>
```

The `.ll-comparison-table` CSS class was entered in Global CSS (Pre-Build step above). No additional configuration needed on this element.

### Below-table note

**Element: Text**

| Setting | Value |
|---|---|
| Text | This is why Levine Law organises advice by industry — not by document type. |
| Font | Inter |
| Size | 16px |
| Color | #000000 |
| Line-height | 1.6 |
| Font style | Italic |
| Margin top | 24px |

---

## SECTION 4 — COMMON ISSUES & WHERE TO GO NEXT

### Container element

| Setting | Value |
|---|---|
| Element | Content Box |
| Background color | #FFFFFF |
| Padding top | 72px |
| Padding bottom | 72px |
| Padding left | 5% |
| Padding right | 5% |

### Section heading

**Element: Heading**

| Setting | Value |
|---|---|
| Tag | H2 |
| Text | Recurring issues we see |
| Font | Inter |
| Size desktop | 32px |
| Size mobile | 26px |
| Weight | 700 |
| Color | #1D4771 |
| Margin bottom | 8px |

### Section subtext

**Element: Text**

| Setting | Value |
|---|---|
| Text | Select your industry to see the issues we commonly work through. |
| Font | Inter |
| Size | 16px |
| Color | #000000 |
| Margin bottom | 32px |

---

### Accordion: global Toggle settings (apply to all 6 Toggle elements)

| Setting | Value |
|---|---|
| Element | Toggle |
| Default state | Closed |
| Allow multiple open | No |
| Custom CSS class | ll-accordion |
| Heading font | Inter 16px weight 600 |
| Heading padding | 16px top/bottom, 20px left/right |
| Heading background (closed) | #F8F8F8 |
| Heading text color (closed) | #1D4771 |
| Heading background (open) | #1D4771 |
| Heading text color (open) | #FFFFFF |
| Icon style | + / − |
| Icon position | Right-aligned |
| Border | 1px solid #D1D5DB |
| Body background | #FFFFFF |
| Body padding | 20px top/bottom, 24px left/right |

Stack all 6 Toggle elements vertically inside the Section 4 Content Box, one after another. The `.ll-accordion + .ll-accordion` CSS rule (entered in Global CSS above) adds 8px margin between them automatically.

---

### Toggle 1: Technology, Software & Digital Platforms

**Heading text:** Technology, Software & Digital Platforms

**Body — add a Styled List element with these items:**

- MSA terms that don't define scope, liability, or IP ownership
- Contractor agreements where work-for-hire provisions are missing or ambiguous
- Equity and compensation documentation never properly formalized
- Corporate structure built for a small team that hasn't scaled with the business
- SaaS and enterprise agreements signed without legal review

**Styled List settings:**

| Setting | Value |
|---|---|
| Bullet style | Disc or custom dash |
| Item font | Inter 15px |
| Item color | #000000 |
| Item line-height | 1.6 |
| Item spacing | 8px between items |

**Below the list — add a Text element:**

| Setting | Value |
|---|---|
| Text | Learn more about Technology & Software → |
| Link | /industries/technology-software |
| Font | Inter 14px |
| Color | #0365B2 |
| Weight | 600 |
| Margin top | 16px |

---

### Toggle 2: Payments, Fintech & Financial Services

**Heading text:** Payments, Fintech & Financial Services

**Body — Styled List (same styling as Toggle 1):**

- MSB registration under federal AML legislation not yet assessed or completed
- AML compliance program not built for the specific business model and FINTRAC requirements
- Suspicious transaction reporting obligations not integrated into operations
- RPAA registration and reporting requirements for payment service providers
- Payment processing agreements negotiated without counsel
- Corporate structure questions when entering the Canadian market

**Below the list — Text element:**

| Setting | Value |
|---|---|
| Text | Learn more about Payments & Fintech → |
| Link | /industries/payments-fintech-msb |
| Font | Inter 14px |
| Color | #0365B2 |
| Weight | 600 |
| Margin top | 16px |

---

### Toggle 3: Construction & Property Development

**Heading text:** Construction & Property Development

**Body — Styled List:**

- Shareholder agreements that don't address growth, exits, or ownership transitions
- Project contracts that leave subcontractor and supplier risk unallocated
- Corporate structure not set up to hold real estate assets separately from operating risk
- Employment and classification issues for field staff and supervisors
- Governance gaps when bringing in new partners or preparing for sale

**Below the list — Text element:**

| Setting | Value |
|---|---|
| Text | Learn more about Construction & Property Development → |
| Link | /industries/construction-property-development |
| Font | Inter 14px |
| Color | #0365B2 |
| Weight | 600 |
| Margin top | 16px |

---

### Toggle 4: Professional Services & Healthcare

**Heading text:** Professional Services & Healthcare

**Body — Styled List:**

- Service and retainer agreements that don't define scope, deliverables, or liability
- Professional corporation structure misaligned with current ownership or partnership arrangements
- IP and work-product ownership unclear in client-facing or subcontractor relationships
- Clinical employment agreements that don't reflect the regulatory environment
- Early equity and profit-sharing arrangements never properly documented

**Below the list — Text element:**

| Setting | Value |
|---|---|
| Text | Learn more about Professional Services & Healthcare → |
| Link | /industries/professional-services-healthcare |
| Font | Inter 14px |
| Color | #0365B2 |
| Weight | 600 |
| Margin top | 16px |

---

### Toggle 5: Manufacturing, Wholesale & Distribution

**Heading text:** Manufacturing, Wholesale & Distribution

**Body — Styled List:**

- Supply and distribution agreements that don't protect against pricing variability or disruption
- Commercial contracts for large buyers or retailers signed without adequate legal review
- Multi-entity corporate structure that has grown without governance to match
- Ownership and equity arrangements for founder-operated businesses approaching transition
- Import/export and cross-border commercial terms not structured for Canadian exposure

**Below the list — Text element:**

| Setting | Value |
|---|---|
| Text | Learn more about Manufacturing & Distribution → |
| Link | /industries/manufacturing-wholesale-distribution |
| Font | Inter 14px |
| Color | #0365B2 |
| Weight | 600 |
| Margin top | 16px |

---

### Toggle 6: Consumer, Food & Retail

**Heading text:** Consumer, Food & Retail

**Body — Styled List:**

- Supplier agreements that don't protect against pricing variability or supply disruption
- Distribution contracts with inadequate exit or renegotiation terms
- Franchise law considerations for businesses that have grown through licensed models
- Corporate governance documents that haven't kept pace with business growth
- Ownership and equity arrangements that have evolved past the founding structure

**Below the list — Text element:**

| Setting | Value |
|---|---|
| Text | Learn more about Consumer, Food & Retail → |
| Link | /industries/consumer-food-retail |
| Font | Inter 14px |
| Color | #0365B2 |
| Weight | 600 |
| Margin top | 16px |

---

## SECTION 5 — CONTACT / CTA

### Container element

| Setting | Value |
|---|---|
| Element | Content Box |
| Background color | #1D4771 |
| Padding top | 72px |
| Padding bottom | 72px |
| Padding left | 5% |
| Padding right | 5% |
| Text alignment | Center |

### Section heading

**Element: Heading**

| Setting | Value |
|---|---|
| Tag | H2 |
| Text | Ready to Talk? |
| Font | Inter |
| Size desktop | 36px |
| Size mobile | 28px |
| Weight | 700 |
| Color | #FFFFFF |
| Alignment | Center |

### Text block 1

**Element: Text**

| Setting | Value |
|---|---|
| Text | If you've identified the category that fits, the relevant page above is the best next step. |
| Font | Inter |
| Size | 18px |
| Color | #D1D5DB |
| Line-height | 1.6 |
| Alignment | Center |
| Margin top | 16px |

### Text block 2

**Element: Text**

| Setting | Value |
|---|---|
| Text | If you're an operating business in Ontario — or a payments or fintech operator with Canadian regulatory exposure — and you want to understand where your legal foundation stands, start with Inquiries. |
| Font | Inter |
| Size | 18px |
| Color | #D1D5DB |
| Line-height | 1.6 |
| Alignment | Center |
| Margin top | 8px |

### CTA Button

**Element: Button**

| Setting | Value |
|---|---|
| Label | GET IN TOUCH → |
| Link | /inquiries |
| Background | #0365B2 |
| Text color | #FFFFFF |
| Font | Inter |
| Font size | 14px |
| Text transform | Uppercase |
| Font weight | 600 |
| Padding | 14px top/bottom, 40px left/right |
| Border-radius | 4px |
| Hover background | #FFFFFF |
| Hover text color | #1D4771 |
| Margin top | 32px |
| Alignment | Center |

---

## ELEMENT BUILD ORDER — QUICK REFERENCE

Use this list to confirm all elements are placed before starting mobile review:

```
[HERO]
  Content Box (navy bg)
    Columns (45/55)
      Col 1: Image (Toronto architectural)
      Col 2: Heading H1
              Text (subheading)
              Button (Explore Industries →)

[SECTION 1]
  Content Box (off-white bg)
    Columns (55/45)
      Col 1: Heading H2
              Text (para 1)
              Text (para 2)
      Col 2: Content Box (navy, nested — pull-quote card)
               Text (pull-quote italic)
               Text (attribution)

[SECTION 2]
  Content Box (white bg, id=industries-grid)
    Heading H2 (centered)
    Columns (3-col, responsive to 2 then 1)
      6x Content Box (class=ll-industry-card)
        each: Icon + H3 + Text + Text (link)

[SECTION 3]
  Content Box (off-white bg)
    Heading H2
    Custom HTML (comparison table)
    Text (italic note)

[SECTION 4]
  Content Box (white bg)
    Heading H2
    Text (subtext)
    6x Toggle (class=ll-accordion, stacked)
      each: heading + Styled List + Text (link)

[SECTION 5]
  Content Box (navy bg)
    Heading H2
    Text (para 1)
    Text (para 2)
    Button (GET IN TOUCH →)
```

---

## RESPONSIVE BEHAVIOUR NOTES

Check these specifically in Thrive's responsive preview (tablet icon and phone icon in the editor toolbar):

| Breakpoint | Required behaviour |
|---|---|
| Desktop (>1024px) | 3-column card grid, 2-column hero layout, full table visible |
| Tablet (768px) | Card grid collapses to 2 columns; hero columns stack (image above text); table font and padding reduce per CSS media query |
| Mobile (480px) | Card grid collapses to 1 column; all columns stack; table wraps; hero H1 at 36px |

For the Columns element in the hero and Section 1: set stack breakpoint to 767px in Thrive column settings.

For the card grid Columns element: set the responsive column count manually in Thrive's responsive editor for tablet (2 columns) and mobile (1 column).

---

## BRAND COMPLIANCE NOTES

Cross-check these before submitting for ML1 review:

- No stock legal imagery. The hero image must be architectural or urban — not a gavel, handshake, courtroom, or generic skyline.
- All body text on white backgrounds uses #000000 (not grey).
- All body text on navy (#1D4771) backgrounds uses #FFFFFF or #D1D5DB.
- Accent red (#FF5E5B) does not appear on this page. This page does not use the red-accent token.
- All headings use Inter, not a serif or display font.
- Buttons use Inter uppercase weight 600. No sentence-case buttons.
- The light-blue token (#4BD1FB) does not appear on this page.

---

## WORDPRESS PAGE SETUP CHECKLIST

```
WORDPRESS PAGE SETUP CHECKLIST

Pre-build:
[ ] Create new page: Pages > Add New
[ ] Title: Industries We Serve
[ ] Slug: /industries
    (confirm Settings > Permalinks is set to "Post name" before saving)
[ ] Parent page: none (this is a Level 2 pillar page)
[ ] WordPress template: Full Width / No Sidebar
    (exact label depends on active theme — choose the widest available option)
[ ] Page status: DRAFT — do not publish until ML1 approves
[ ] Save draft, then click "Launch Thrive Architect" to enter the builder

Post-build:
[ ] All 6 industry cards link to correct slugs:
    /industries/technology-software
    /industries/payments-fintech-msb
    /industries/construction-property-development
    /industries/professional-services-healthcare
    /industries/manufacturing-wholesale-distribution
    /industries/consumer-food-retail
[ ] "Explore Industries →" button anchor verified: href="#industries-grid"
    and the Section 2 Content Box has id="industries-grid" set
[ ] "GET IN TOUCH →" button links to /inquiries
[ ] All 6 accordion "Learn more" links verified against slug list above
[ ] Mobile preview checked in Thrive responsive view (tablet breakpoint + phone breakpoint)
[ ] Hero image placeholder replaced with approved asset (or confirmed as acceptable placeholder)
[ ] All image elements have descriptive alt text
[ ] No placeholder text remaining anywhere on page
[ ] Global CSS entered in Thrive Dashboard > Global CSS (or WP Customizer > Additional CSS)
[ ] Card hover effect tested in browser (not visible inside Thrive editor — test on frontend)
[ ] Table renders correctly at tablet and mobile widths

Menu assignment (complete after ML1 publishes):
[ ] WordPress > Appearance > Menus
[ ] Add "Industries We Serve" to primary navigation
[ ] Menu label: "Industries" — ML1 to confirm preferred label
[ ] Position: alongside Services and Inquiries in primary nav

SEO (Yoast or RankMath — complete before publish):
[ ] SEO title: Industries We Serve | Levine Law
    (confirm under 60 characters — this title is 38 characters)
[ ] Meta description: Levine Law works with operating businesses across six industry
    categories in Ontario. Learn how industry context shapes the legal and structural
    advice you need.
    (confirm under 160 characters — this is approximately 158 characters)
[ ] Canonical URL: https://[domain]/industries
    (replace [domain] with the live domain before publishing)
[ ] Robots: Index, Follow
[ ] Focus keyphrase (Yoast/RankMath): industries we serve ontario business law

ML1 PUBLISH STEP — HUMAN ACTION REQUIRED:
  After reviewing all content and links in Thrive Architect and on the
  WordPress frontend preview:
  1. Change page Status from Draft to Published in WordPress.
  2. Assign to the primary navigation menu and confirm menu position.
  3. Verify /industries loads correctly at the live URL.
  4. Confirm all internal links resolve (card links, anchor, /inquiries).
  This step cannot be automated. INV-0002 applies.
```

---

APPROVAL REQUIRED: This build packet requires ML1 review before execution in Thrive Architect. No live changes have been made. INV-0002 applies.
