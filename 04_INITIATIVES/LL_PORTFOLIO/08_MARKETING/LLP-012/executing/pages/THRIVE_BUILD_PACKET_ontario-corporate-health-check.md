---
id: thrive-build-packet-ontario-corporate-health-check
title: Thrive Architect Build Packet — Ontario Corporate Health Check Landing Page
produced_by: MKT_THRIVE_THEMES_AGENT
funnel: Funnel 2 — Corporate Law Services For Growing Businesses
offer: Corporate Health Check
status: draft
approval: pending ML1 review and execution
created_date: 2026-03-30
ia_level: Level 3 (service-specific soft landing page, per POL-051)
palette_ref: POL-049 Present State (active)
owner: ML1
last_updated: 2026-05-18
tags: []
---

# Thrive Architect Build Packet
# Ontario Corporate Health Check Landing Page

STATUS: DRAFT — Pending ML1 approval and execution. Do not publish until ML1
explicitly changes page status to Published and confirms all content and links.

---

## Palette Reference (POL-049 Present State — Active)

All color values in this packet map to the POL-049 active palette.

| Token used in this packet | Hex value | Role |
|---|---|---|
| NAVY | `#1D4771` | Primary dark background (sections 1, 2, 4, 6, 10) |
| BLUE | `#0365B2` | Accent, button hover, card accent border |
| WHITE | `#FFFFFF` | Text on dark, card backgrounds, section backgrounds |
| RED | `#FF5E5B` | Accent only — sparingly on icon/highlight elements |
| LIGHT-GRAY | `#D1D5DB` | Dividers, subtle borders, secondary text on white |
| BLACK | `#000000` | Body text on white backgrounds |

PALETTE FLAG FOR ML1: The reference pages at law.levinelegal.ca and
levinelegal.ca/corporate-law-firm/ use `#031b33` (very dark navy) and `#2f7ece`
(blue accent). These are outside the POL-049 active palette. This packet uses
the compliant equivalents `#1D4771` and `#0365B2`. If ML1 wishes to match the
reference pages exactly, an explicit palette exception approval is required
before execution.

---

## WordPress Page Setup

| Setting | Value |
|---|---|
| Page title | Ontario Corporate Health Check |
| URL slug | `/ontario-corporate-health-check/` |
| Parent page | Services / How We Help (Level 2) |
| WordPress template | Thrive Architect Blank (Full Width / No Sidebar) |
| Publish status | Draft — do not publish until ML1 approves |
| Menu assignment | See menu checklist below |
| Canonical URL | `https://levine-law.ca/ontario-corporate-health-check/` |

### WordPress Page Settings Checklist

- [ ] Page title set to: Ontario Corporate Health Check
- [ ] Slug set to: `ontario-corporate-health-check`
- [ ] Parent page set to: Services / How We Help
- [ ] WordPress template set to: Full Width / No Sidebar (or Thrive Architect Blank)
- [ ] Thrive Architect activated on this page
- [ ] Page status: Draft
- [ ] No menu item added yet — ML1 to confirm which menu location and position
      at publish time (this is a Level 3 conversion page; it may or may not
      appear in main nav — flag for ML1 decision)
- [ ] Yoast SEO title: `Ontario Corporate Health Check | Levine Law`
- [ ] Yoast meta description: `A structured legal review for growing Ontario businesses. Five-pillar assessment of governance, employment, contracts, and transaction readiness. Written findings report and prioritized action plan.`
- [ ] Yoast canonical URL: `https://levine-law.ca/ontario-corporate-health-check/`
- [ ] Yoast robots: Index, Follow
- [ ] Internal links verified in Thrive editor before publish

---

## Thrive Leads Form Setup (Complete Before Building Hero)

The hero section requires a Thrive Leads form embedded in a Lead Generation
element. Set up the Thrive Leads asset first so it is available to insert
during the hero build.

### Step-by-step Thrive Leads Setup

1. Go to: WordPress Dashboard > Thrive Dashboard > Thrive Leads
2. Click "Add New" under Lead Groups (or use a standalone Shortcode form)
3. Select form type: Shortcode (so it can be embedded in Thrive Architect)
4. Name the form: `Health Check Hero Form`
5. Click "Add new design" and select the 2-step or inline form template
6. Edit the form fields:

   Field 1:
   - Type: Text
   - Label: First Name
   - Placeholder: First Name
   - Required: Yes

   Field 2:
   - Type: Text
   - Label: Last Name
   - Placeholder: Last Name
   - Required: Yes

   Field 3:
   - Type: Phone
   - Label: Phone
   - Placeholder: Phone Number
   - Required: Yes

   Field 4:
   - Type: Email
   - Label: Email Address
   - Placeholder: Email Address
   - Required: Yes

   Field 5:
   - Type: Textarea
   - Label: Tell us about your business
   - Placeholder: Briefly describe your business structure, ownership, and
     what prompted you to reach out.
   - Required: No

   Submit button:
   - Label: Request Your Health Check
   - Background: BLUE `#0365B2`
   - Text: WHITE `#FFFFFF`
   - Width: 100% of form column
   - Font: Roboto Bold, 16px, uppercase

7. Success action: Redirect to a Thank You page (create a simple Draft thank-
   you page at `/health-check-thank-you/`) OR display a success message:
   "Thank you. We will be in touch within one business day."
8. Connect to GHL (Go High Level) via the Thrive Leads > API Connections
   settings. Tag the lead: `Health-Check-Request`, Funnel 2.
9. Save the form. Note the shortcode (e.g., `[thrive_leads id='xxx']`).
   You will embed this shortcode via a Custom HTML element in the hero Column 2.

---

## Symbol Definitions

### SYMBOL: Site Header (Sticky Nav)
Name in Thrive: `LL-HEADER-STICKY`

If this Symbol already exists on the site, reuse it. If not, create it now.

Symbol structure:

Content Box element (outermost wrapper):
- Background: NAVY `#1D4771`
- Padding: top 0 / bottom 0 / left 0 / right 0
- Width: 100%
- Position: This box is the Symbol container; sticky behavior is set on
  the Thrive Template (Header template), not inside the Symbol itself.
  If building this as a standalone page (not via Thrive Theme Builder
  header template), use the Thrive Architect "Sticky" option on this
  Content Box: enable sticky, offset 0px, sticky background NAVY `#1D4771`.

  Inside the Content Box:
  Columns element: 2 columns, 30/70 split, vertical-align: center
  Padding on the Columns row: top 14px / bottom 14px / left 4% / right 4%

    Column 1 (Logo):
      Image element:
      - Source: Levine Law logo asset (upload from Canva export, white version
        for use on dark background)
      - Alt text: Levine Law — Ontario Corporate Lawyers
      - Max-width: 160px
      - Alignment: left
      - Link: `https://levine-law.ca/`

    Column 2 (Nav + CTA):
      Columns element: 2 columns, 75/25 split, vertical-align: center

        Inner Column 1 (Nav links):
          Text element (inline nav — or use WordPress Menu widget if available):
          Render the following as a horizontal link row.
          If Thrive Architect does not support inline menu natively, use a
          Custom HTML element with the following structure:

          ```html
          <nav class="ll-sticky-nav">
            <a href="#why-it-works">Why It Works</a>
            <a href="#what-you-get">What You Get</a>
            <a href="#about">About</a>
            <a href="#faqs">FAQs</a>
          </nav>
          ```

          Custom CSS class on the Custom HTML element: `ll-sticky-nav`
          (CSS defined in the Custom CSS block at the end of this packet)

        Inner Column 2 (CTA + Phone):
          Button element:
          - Label: Book Your Health Check
          - Link: anchor `#hero-form` (smooth scroll to hero form)
          - Background: BLUE `#0365B2`
          - Text: WHITE, Roboto Bold, 13px, uppercase
          - Padding: 10px 18px
          - Border-radius: 4px
          - Hover background: `#024f8a` (darkened BLUE — flag if ML1 wants
            exact hover color defined; this is 15% darker than `#0365B2`)

          Text element (phone):
          - Content: 365-599-0078
          - Link: `tel:3655990078`
          - Font: Roboto, 13px, WHITE `#FFFFFF`
          - Alignment: center
          - Margin-top: 4px

Symbol assignment:
- Assign to this page's top position before Section 2 hero.
- If Thrive Theme Builder header template is in use site-wide, assign this
  Symbol to the header template region instead.
- Update behavior: Changes to this Symbol propagate to all pages where it
  is assigned.

---

## Section-by-Section Build Instructions

---

### SECTION 1 — STICKY NAV

This section is the Symbol defined above (LL-HEADER-STICKY).

Implementation:
- If using Thrive Theme Builder: the Symbol is already in the header template;
  no separate section needed on this page.
- If building as a standalone page: insert a Content Box element at the very
  top of the page, make it sticky, and place the LL-HEADER-STICKY Symbol
  inside it.

Responsive behavior:
- At 768px breakpoint: hide the nav link row. Show hamburger icon.
  Thrive does not have a native mobile hamburger for inline nav built in
  Architect (it does in Theme Builder header templates). If this is a
  standalone Architect page (not using Theme Builder), use the Thrive
  Mobile Visibility toggles to hide the nav text at mobile and display a
  simplified nav with just the CTA button and phone number stacked.
- At 480px: CTA button full-width, phone centered below.

---

### SECTION 2 — HERO

[SECTION ID: hero]

Thrive custom CSS class on section: `ll-section-hero`

Outer Content Box:
- Background color: NAVY `#1D4771`
- Padding: top 80px / bottom 80px / left 5% / right 5%
- Width: 100%
- Anchor/ID: `hero-form` (set via Thrive element ID field so the nav CTA
  button scrolls here)

Inside the outer Content Box, insert:
Columns element: 2 columns, 55/45 split, vertical-align: top, gap: 48px

  --- Column 1 (Left — Headline + Value Proposition) ---

  Heading element:
  - Tag: H1
  - Text: The Ontario Corporate Health Check
  - Font: Roboto
  - Weight: 700
  - Size: 52px desktop
  - Color: WHITE `#FFFFFF`
  - Alignment: left
  - Margin-bottom: 16px

  Text element:
  - Text: A structured legal review for growing Ontario businesses that have
    outgrown their original setup.
  - Font: Roboto
  - Weight: 400
  - Size: 20px desktop
  - Color: `#D1D5DB` (LIGHT-GRAY — slightly muted white for subhead contrast)
  - Line-height: 1.6
  - Margin-bottom: 32px

  Divider element:
  - Style: solid line
  - Color: BLUE `#0365B2`
  - Width: 60px
  - Align: left
  - Height: 3px
  - Margin-bottom: 28px

  Styled List element (3 value bullets):
  - List style: custom icon (use checkmark icon from Thrive icon library,
    color BLUE `#0365B2`, size 18px)
  - Font: Roboto
  - Text size: 16px
  - Text color: WHITE `#FFFFFF`
  - Line-height: 1.6
  - Item spacing: 16px between items

  Item 1:
    Icon: checkmark, BLUE `#0365B2`
    Bold label: Five-Pillar Review
    Body text: — Shareholder agreements, corporate records, employment
    structure, commercial contracts, and transaction readiness assessed in
    one structured engagement.

  Item 2:
    Icon: checkmark, BLUE `#0365B2`
    Bold label: Written Findings Report
    Body text: — Clear documentation of what is aligned, what has drifted,
    and where exposure exists.

  Item 3:
    Icon: checkmark, BLUE `#0365B2`
    Bold label: Prioritized Action Plan
    Body text: — A sequenced remediation roadmap organized by risk level
    and business impact.

  IMPLEMENTATION NOTE FOR STYLED LIST BOLD LABELS: Thrive's Styled List
  element does not natively support mixed bold/regular text within one list
  item. Use a Custom HTML element instead of a Styled List element for these
  three bullets. Custom HTML structure:

  ```html
  <ul class="ll-value-bullets">
    <li>
      <span class="ll-bullet-label">Five-Pillar Review</span>
      — Shareholder agreements, corporate records, employment structure,
      commercial contracts, and transaction readiness assessed in one
      structured engagement.
    </li>
    <li>
      <span class="ll-bullet-label">Written Findings Report</span>
      — Clear documentation of what is aligned, what has drifted, and
      where exposure exists.
    </li>
    <li>
      <span class="ll-bullet-label">Prioritized Action Plan</span>
      — A sequenced remediation roadmap organized by risk level and
      business impact.
    </li>
  </ul>
  ```

  Custom CSS for this element: defined in the Custom CSS block at the end
  of this packet under `.ll-value-bullets`.

  Button element (below the bullets):
  - Label: Book Your Health Check
  - Link: anchor `#hero-form`
  - Background: BLUE `#0365B2`
  - Text: WHITE `#FFFFFF`, Roboto Bold, 16px, uppercase
  - Padding: 16px 36px
  - Border-radius: 4px
  - Hover background: `#024f8a`
  - Margin-top: 32px
  - Alignment: left

  --- Column 2 (Right — Form) ---

  Content Box element (form card):
  - Background: WHITE `#FFFFFF`
  - Border-radius: 8px
  - Padding: top 32px / bottom 32px / left 32px / right 32px
  - Box-shadow: `0 8px 32px rgba(0,0,0,0.22)`

    Heading element (form title):
    - Tag: H3
    - Text: Request Your Health Check
    - Font: Roboto
    - Weight: 700
    - Size: 22px
    - Color: NAVY `#1D4771`
    - Alignment: center
    - Margin-bottom: 8px

    Text element (form subtitle):
    - Text: No obligation. We will review your intake and respond within
      one business day.
    - Font: Roboto
    - Size: 14px
    - Color: `#666666` (this is outside POL-049; use BLACK `#000000` at
      reduced opacity, or use LIGHT-GRAY `#D1D5DB`. ML1 to confirm.
      Flagged.)
    - Alignment: center
    - Margin-bottom: 24px

    Custom HTML element (Thrive Leads form embed):
    - Paste the Thrive Leads shortcode generated in the Form Setup section
      above: `[thrive_leads id='xxx']`
    - Thrive Architect will render the live form here.
    - If the shortcode does not render in preview, switch to the WordPress
      front-end preview mode to confirm rendering.

  FORM CARD COLOR FLAG: The form subtitle uses `#666666` which is not in
  the POL-049 palette. Use BLACK `#000000` at the minimum. ML1 to confirm
  preferred treatment for secondary text inside white cards.

Responsive behavior for Section 2:
- At 768px: Columns element stacks to single column. Column 2 (form card)
  moves ABOVE Column 1 on mobile (set Column 2 as "first" in mobile order
  via Thrive Architect responsive column order setting). This is standard
  practice for hero forms — form visible immediately on mobile without
  scrolling.
- H1 font-size: 36px at 768px / 30px at 480px
- Subhead font-size: 17px at 768px / 15px at 480px
- Value bullets font-size: 15px at 768px
- Form card padding: 24px all sides at 768px
- Button: full-width at 480px

---

### SECTION 3 — THE PROBLEM

[SECTION ID: the-problem]

Outer Content Box:
- Background color: WHITE `#FFFFFF`
- Padding: top 80px / bottom 80px / left 10% / right 10%
- Width: 100%

Thrive custom CSS class: `ll-section-problem`

Inside:
  Columns element: 1 column (full width, centered, max-width 860px,
  horizontally centered via Thrive's content alignment setting)

    Heading element:
    - Tag: H2
    - Text: Most Growing Ontario Businesses Are Operating on Outdated Legal
      Structure
    - Font: Roboto
    - Weight: 700
    - Size: 40px desktop
    - Color: NAVY `#1D4771`
    - Alignment: center
    - Margin-bottom: 32px

    Divider element:
    - Style: solid
    - Color: BLUE `#0365B2`
    - Width: 60px
    - Height: 3px
    - Align: center
    - Margin-bottom: 32px

    Text element:
    - Text: When a business incorporates, the documents reflect the company
      at that moment. As the business grows — adding shareholders,
      delegating authority, signing contracts, considering financing — the
      legal structure rarely keeps pace. The documents don't update
      themselves. The gap between what the structure says and how the
      business actually operates is where problems begin. Most companies
      discover this gap at the worst possible time: during a dispute, a
      financing process, or a transaction.
    - Font: Roboto
    - Size: 18px
    - Color: BLACK `#000000`
    - Line-height: 1.8
    - Alignment: center
    - Max-width: 760px (set via Thrive's width control on the Text element)

Responsive behavior for Section 3:
- At 768px: left/right padding 6%
- H2 font-size: 28px at 768px / 24px at 480px
- Body text size: 16px at 768px
- Padding: top 60px / bottom 60px at 768px

---

### SECTION 4 — FIVE PILLARS

[SECTION ID: five-pillars]

Thrive custom CSS class: `ll-section-pillars`

Anchor/ID: `what-you-get`

Outer Content Box:
- Background color: NAVY `#1D4771`
- Padding: top 80px / bottom 80px / left 5% / right 5%
- Width: 100%

Inside:
  Heading element:
  - Tag: H2
  - Text: Five Areas. One Structured Review.
  - Font: Roboto
  - Weight: 700
  - Size: 40px
  - Color: WHITE `#FFFFFF`
  - Alignment: center
  - Margin-bottom: 12px

  Divider element:
  - Style: solid
  - Color: BLUE `#0365B2`
  - Width: 60px
  - Height: 3px
  - Align: center
  - Margin-bottom: 48px

  Columns element: 3 columns, equal width (33/33/33), gap: 24px,
  vertical-align: top
  Margin-bottom: 24px

    Column 1 — Card: Shareholder Agreements
    Content Box element (card):
    - Background: `rgba(255,255,255,0.07)` (subtle white overlay on navy;
      achieve by setting Background color to WHITE at 7% opacity in Thrive)
    - Border: 1px solid `rgba(255,255,255,0.15)`
    - Border-radius: 8px
    - Padding: 28px
    - Border-top: 3px solid BLUE `#0365B2` (set via Custom CSS on this card;
      see CSS block)

      Heading element:
      - Tag: H3
      - Text: Shareholder Agreements
      - Font: Roboto Bold, 18px, WHITE `#FFFFFF`
      - Margin-bottom: 12px

      Text element:
      - Text: Are the exit mechanisms, valuation provisions, governance
        thresholds, and transfer restrictions still aligned with how the
        business actually operates?
      - Font: Roboto, 15px
      - Color: `#D1D5DB` (LIGHT-GRAY)
      - Line-height: 1.7

    Column 2 — Card: Corporate Records
    Content Box element (card):
    (same card styles as Column 1)

      Heading element:
      - Tag: H3
      - Text: Corporate Records
      - Font: Roboto Bold, 18px, WHITE `#FFFFFF`
      - Margin-bottom: 12px

      Text element:
      - Text: Are the minute book, resolutions, director appointments, and
        annual filings current and complete? Gaps here create friction in
        financing and transactions.
      - Font: Roboto, 15px
      - Color: LIGHT-GRAY `#D1D5DB`
      - Line-height: 1.7

    Column 3 — Card: Employment Structure
    Content Box element (card):
    (same card styles)

      Heading element:
      - Tag: H3
      - Text: Employment Structure
      - Font: Roboto Bold, 18px, WHITE `#FFFFFF`
      - Margin-bottom: 12px

      Text element:
      - Text: Are contractor relationships properly classified? Are
        termination clauses enforceable? Are equity promises documented?
      - Font: Roboto, 15px
      - Color: LIGHT-GRAY `#D1D5DB`
      - Line-height: 1.7

  Second Columns element (row 2): 2 columns, centered,
  max-width 800px, horizontally centered. Column widths: 50/50, gap: 24px

    Column 1 — Card: Commercial Contracts
    Content Box element (card):
    (same card styles)

      Heading element:
      - Tag: H3
      - Text: Commercial Contracts
      - Font: Roboto Bold, 18px, WHITE `#FFFFFF`
      - Margin-bottom: 12px

      Text element:
      - Text: Are your key contracts consistent? Do limitation of liability,
        indemnity, and assignment provisions reflect your current risk
        tolerance?
      - Font: Roboto, 15px
      - Color: LIGHT-GRAY `#D1D5DB`
      - Line-height: 1.7

    Column 2 — Card: Transaction Readiness
    Content Box element (card):
    (same card styles)

      Heading element:
      - Tag: H3
      - Text: Transaction Readiness
      - Font: Roboto Bold, 18px, WHITE `#FFFFFF`
      - Margin-bottom: 12px

      Text element:
      - Text: If a buyer, investor, or lender reviewed your structure today,
        what would they find? Are the documents organized to support a
        transaction?
      - Font: Roboto, 15px
      - Color: LIGHT-GRAY `#D1D5DB`
      - Line-height: 1.7

LAYOUT NOTE: Thrive Architect does not natively support a 5-card layout
with a top row of 3 and a bottom row of 2 centered. The two-row approach
above (first Columns = 3 cols, second Columns = 2 cols centered to 800px)
achieves this. Ensure the second Columns element's container is centered
using Thrive's "Center" alignment option.

Responsive behavior for Section 4:
- At 768px: first Columns element stacks to 1 column (cards full width,
  stacked). Second Columns element also stacks to 1 column.
- Card padding: 20px at 768px
- H2 font-size: 28px at 768px / 24px at 480px
- H3 inside cards: 17px at 768px
- Padding on outer Content Box: top 60px / bottom 60px / left 4% / right 4%
  at 768px

---

### SECTION 5 — HOW IT WORKS

[SECTION ID: how-it-works]

Anchor/ID: `why-it-works`

Thrive custom CSS class: `ll-section-how-it-works`

Outer Content Box:
- Background color: WHITE `#FFFFFF`
- Padding: top 80px / bottom 80px / left 5% / right 5%
- Width: 100%

Inside:
  Heading element:
  - Tag: H2
  - Text: How the Health Check Works
  - Font: Roboto Bold, 40px
  - Color: NAVY `#1D4771`
  - Alignment: center
  - Margin-bottom: 12px

  Divider element:
  - Style: solid
  - Color: BLUE `#0365B2`
  - Width: 60px / Height: 3px / Align: center
  - Margin-bottom: 56px

  Columns element: 3 columns, 33/33/33, gap: 32px, vertical-align: top

    Column 1 — Step 1: Intake
    Content Box element:
    - Background: WHITE
    - Padding: 28px
    - Border-radius: 8px
    - Border: 1px solid LIGHT-GRAY `#D1D5DB`

      Text element (step number):
      - Text: 01
      - Font: Roboto Bold, 48px
      - Color: BLUE `#0365B2`
      - Margin-bottom: 8px

      Heading element:
      - Tag: H3
      - Text: Intake
      - Font: Roboto Bold, 20px
      - Color: NAVY `#1D4771`
      - Margin-bottom: 12px

      Text element:
      - Text: You complete a short intake form describing your business
        structure, ownership, and current concerns. We review it before
        your first call.
      - Font: Roboto, 16px
      - Color: BLACK `#000000`
      - Line-height: 1.7

    Column 2 — Step 2: Review
    Content Box element: (same card styles as Column 1)

      Text element (step number):
      - Text: 02
      - Font: Roboto Bold, 48px, BLUE `#0365B2`
      - Margin-bottom: 8px

      Heading element:
      - Tag: H3
      - Text: Review
      - Font: Roboto Bold, 20px, NAVY `#1D4771`
      - Margin-bottom: 12px

      Text element:
      - Text: We conduct a structured review across the five pillars —
        examining your documents, identifying gaps, and assessing alignment
        between structure and operations.
      - Font: Roboto, 16px, BLACK `#000000`
      - Line-height: 1.7

    Column 3 — Step 3: Findings and Plan
    Content Box element: (same card styles)

      Text element (step number):
      - Text: 03
      - Font: Roboto Bold, 48px, BLUE `#0365B2`
      - Margin-bottom: 8px

      Heading element:
      - Tag: H3
      - Text: Findings and Plan
      - Font: Roboto Bold, 20px, NAVY `#1D4771`
      - Margin-bottom: 12px

      Text element:
      - Text: You receive a written findings report and a prioritized action
        plan. Clear, actionable, organized by risk level.
      - Font: Roboto, 16px, BLACK `#000000`
      - Line-height: 1.7

Responsive behavior for Section 5:
- At 768px: Columns stack to 1 column. Cards full-width.
- H2 font-size: 28px at 768px / 24px at 480px
- Step number font: 40px at 768px
- Outer padding: top 60px / bottom 60px / left 4% / right 4% at 768px

---

### SECTION 6 — WHY LEVINE LAW

[SECTION ID: why-levine-law]

Anchor/ID: (no anchor needed; accessible from nav via scroll)

Thrive custom CSS class: `ll-section-why`

Outer Content Box:
- Background color: NAVY `#1D4771`
- Padding: top 80px / bottom 80px / left 5% / right 5%
- Width: 100%

Inside:
  Heading element:
  - Tag: H2
  - Text: Why Serious Operators Work with Levine Law
  - Font: Roboto Bold, 40px
  - Color: WHITE `#FFFFFF`
  - Alignment: center
  - Margin-bottom: 12px

  Divider element:
  - Style: solid, BLUE `#0365B2`, 60px wide, 3px, centered
  - Margin-bottom: 48px

  Columns element: 4 columns, 25/25/25/25, gap: 24px, vertical-align: top

    Column 1 — Tile: Fast Turnarounds, Real Access
    Content Box element:
    - Background: `rgba(255,255,255,0.07)`, border 1px solid
      `rgba(255,255,255,0.15)`, border-radius 8px, padding 28px

      Icon element:
      - Icon: Clock / Speed (use Thrive icon set — "clock" or "time" icon)
      - Size: 36px
      - Color: BLUE `#0365B2`
      - Alignment: center
      - Margin-bottom: 16px

      Heading element:
      - Tag: H3
      - Text: Fast Turnarounds, Real Access
      - Font: Roboto Bold, 17px
      - Color: WHITE `#FFFFFF`
      - Alignment: center
      - Margin-bottom: 12px

      Text element:
      - Text: Responsive communication and efficient file management without
        the delays of large-firm bureaucracy.
      - Font: Roboto, 14px
      - Color: LIGHT-GRAY `#D1D5DB`
      - Line-height: 1.7
      - Alignment: center

    Column 2 — Tile: Big-Firm Capability, Entrepreneurial Focus
    Content Box element: (same tile styles)

      Icon element:
      - Icon: Building / corporate icon
      - Size: 36px, BLUE `#0365B2`, centered, margin-bottom 16px

      Heading element:
      - Tag: H3
      - Text: Big-Firm Capability, Entrepreneurial Focus
      - Font: Roboto Bold, 17px, WHITE, centered, margin-bottom 12px

      Text element:
      - Text: Trained at major corporate law firms with deep transactional
        and governance experience — applied directly to growing businesses.
      - Font: Roboto, 14px, LIGHT-GRAY `#D1D5DB`, line-height 1.7, centered

    Column 3 — Tile: Strategies Built for Scale
    Content Box element: (same tile styles)

      Icon element:
      - Icon: Chart / growth icon
      - Size: 36px, BLUE `#0365B2`, centered, margin-bottom 16px

      Heading element:
      - Tag: H3
      - Text: Strategies Built for Scale
      - Font: Roboto Bold, 17px, WHITE, centered, margin-bottom 12px

      Text element:
      - Text: Legal advice structured for businesses that are growing, not
        just operating. Governance and contracts that hold up as complexity
        increases.
      - Font: Roboto, 14px, LIGHT-GRAY `#D1D5DB`, line-height 1.7, centered

    Column 4 — Tile: Future-Proof Your Business
    Content Box element: (same tile styles)

      Icon element:
      - Icon: Shield / protection icon
      - Size: 36px, BLUE `#0365B2`, centered, margin-bottom 16px

      Heading element:
      - Tag: H3
      - Text: Future-Proof Your Business
      - Font: Roboto Bold, 17px, WHITE, centered, margin-bottom 12px

      Text element:
      - Text: Build the structure that supports a transaction, a financing,
        or a leadership transition — before you need it.
      - Font: Roboto, 14px, LIGHT-GRAY `#D1D5DB`, line-height 1.7, centered

COPY FLAG FOR ML1: The tile body copy above (Columns 1–4) is inferred from
the offer positioning and the reference page. ML1 must confirm these are the
exact tile descriptions from the reference page, or substitute the approved
copy. The tile titles match the reference spec provided.

Responsive behavior for Section 6:
- At 768px: Columns stack to 2 columns, 2-up grid (Thrive responsive: change
  column count to 2 at tablet breakpoint).
- At 480px: stack to 1 column.
- H2: 28px at 768px / 24px at 480px
- Tile padding: 20px at 768px

---

### SECTION 7 — ABOUT

[SECTION ID: about]

Anchor/ID: `about`

Thrive custom CSS class: `ll-section-about`

Outer Content Box:
- Background color: WHITE `#FFFFFF`
- Padding: top 80px / bottom 80px / left 5% / right 5%
- Width: 100%

Inside:
  Columns element: 2 columns, 35/65 split, vertical-align: top, gap: 48px

    Column 1 (Photo):
      Image element:
      - Source: Matthew Levine headshot / professional photo asset
        (upload or reference existing site image)
      - Alt text: Matthew Levine — Levine Law, Ontario Corporate Lawyer
      - Max-width: 320px
      - Border-radius: 8px
      - Box-shadow: `0 8px 28px rgba(0,0,0,0.12)`
      - Alignment: center

    Column 2 (Bio):
      Heading element:
      - Tag: H2
      - Text: About Matthew Levine
      - Font: Roboto Bold, 36px
      - Color: NAVY `#1D4771`
      - Margin-bottom: 16px

      Divider element:
      - Solid, BLUE `#0365B2`, 60px, 3px, left-aligned
      - Margin-bottom: 24px

      Text element (bio body):
      - Text: [Insert approved bio copy from the reference page at
        law.levinelegal.ca — About Matthew Levine section. Copy should
        include: JD UBC, LLM University of Toronto, 10+ years of corporate
        law experience, CBA and LSO membership, and positioning for growing
        Ontario businesses.]
      - Font: Roboto, 16px
      - Color: BLACK `#000000`
      - Line-height: 1.8
      - Margin-bottom: 20px

      COPY FLAG FOR ML1: The exact bio copy was not provided in the brief.
      ML1 must paste the approved bio copy from the reference page into this
      Text element before publishing.

      Styled List element (credentials / affiliations):
      - Icon: checkmark, BLUE `#0365B2`, 16px
      - Items:
          JD, University of British Columbia
          LLM, University of Toronto
          Member, Canadian Bar Association
          Member, Law Society of Ontario

      - Font: Roboto, 15px, BLACK `#000000`
      - Item spacing: 10px

Responsive behavior for Section 7:
- At 768px: columns stack. Photo above bio. Photo max-width 240px, centered.
- H2: 28px at 768px

---

### SECTION 8 — TESTIMONIALS

[SECTION ID: testimonials]

Thrive custom CSS class: `ll-section-testimonials`

Outer Content Box:
- Background color: `#F4F6F9` (very light gray — closest to LIGHT-GRAY
  `#D1D5DB` at reduced saturation. ML1 flag: this is outside the exact
  POL-049 palette. Alternatives: use WHITE `#FFFFFF` or LIGHT-GRAY
  `#D1D5DB` as the section background. Recommend WHITE for compliance.
  Flagged for ML1 decision.)
- Padding: top 80px / bottom 80px / left 5% / right 5%
- Width: 100%

Inside:
  Heading element:
  - Tag: H2
  - Text: What Clients Say
  - Font: Roboto Bold, 40px
  - Color: NAVY `#1D4771`
  - Alignment: center
  - Margin-bottom: 12px

  Divider element:
  - Solid, BLUE `#0365B2`, 60px, 3px, centered
  - Margin-bottom: 48px

  Columns element: 2 columns, 50/50, gap: 32px

  TESTIMONIAL COPY FLAG FOR ML1: The 4 specific testimonials were not
  provided in this brief. ML1 must insert the exact approved testimonial
  text from the reference page. The structure below is a placeholder using
  the Thrive Testimonial element for each of the 4 testimonials, arranged
  as a 2x2 grid (2 columns, 2 rows).

    Column 1:
      Testimonial element (Testimonial 1):
      - Quote: [Approved testimonial 1 text from reference page]
      - Attribution name: [Client name or "Ontario Business Owner"]
      - Attribution role: [Position / company type if approved]
      - Star rating: 5 stars (if applicable; use 0 stars / hide if no
        rating is shown on the reference page)
      - Style: card with border-radius 8px, white background,
        padding 28px, box-shadow `0 4px 16px rgba(0,0,0,0.08)`
      - Quote font: Roboto Italic, 16px, BLACK `#000000`, line-height 1.8
      - Attribution font: Roboto Bold, 14px, NAVY `#1D4771`

      Testimonial element (Testimonial 2):
      (same configuration; insert Testimonial 2 text)
      - Margin-top: 32px

    Column 2:
      Testimonial element (Testimonial 3):
      (same configuration; insert Testimonial 3 text)

      Testimonial element (Testimonial 4):
      (same configuration; insert Testimonial 4 text)
      - Margin-top: 32px

Responsive behavior for Section 8:
- At 768px: 2 columns stack to 1 column; testimonials display full width,
  stacked vertically.
- Testimonial margin-top: 24px at 768px between stacked items.

---

### SECTION 9 — FAQS

[SECTION ID: faqs]

Anchor/ID: `faqs`

Thrive custom CSS class: `ll-section-faqs`

Outer Content Box:
- Background color: WHITE `#FFFFFF`
- Padding: top 80px / bottom 80px / left 10% / right 10%
- Width: 100%

Inside:
  Heading element:
  - Tag: H2
  - Text: FAQs
  - Font: Roboto Bold, 40px
  - Color: NAVY `#1D4771`
  - Alignment: center
  - Margin-bottom: 12px

  Divider element:
  - Solid, BLUE `#0365B2`, 60px, 3px, centered
  - Margin-bottom: 48px

  Content Box element (accordion wrapper, max-width 820px, centered):

    Toggle (Accordion) element — FAQ 1:
    - Default state: Closed
    - Allow multiple open: No (only one open at a time)
    - Heading text: What is the Ontario Corporate Health Check?
    - Heading font: Roboto Bold, 17px, NAVY `#1D4771`
    - Heading background: WHITE `#FFFFFF`
    - Heading padding: 20px 24px
    - Heading border-bottom: 1px solid LIGHT-GRAY `#D1D5DB`
    - Open/close icon: Thrive default chevron, BLUE `#0365B2`, right-aligned
    - Body content: Text element inside accordion body:
        A structured legal review of your company's governance and
        commercial structure. We examine five areas — shareholder agreements,
        corporate records, employment, commercial contracts, and transaction
        readiness — and deliver a written findings report with a prioritized
        action plan.
      Font: Roboto, 16px, BLACK `#000000`, line-height 1.8
      Body padding: 20px 24px
      Body background: `#F9FAFB` (very light gray — see palette flag above;
      use WHITE `#FFFFFF` for strict compliance)

    Toggle (Accordion) element — FAQ 2:
    - (same configuration)
    - Heading text: Who is it for?
    - Body text: Ontario businesses with at least CAD 5M in annual cash flow,
      typically with 5–30 employees, that operate in a strategic industry lane
      and want to understand whether their legal structure still reflects how
      the business actually works.

    Toggle (Accordion) element — FAQ 3:
    - (same configuration)
    - Heading text: What do I receive at the end?
    - Body text: A written findings report documenting alignment, gaps, and
      exposures across the five pillars — plus a prioritized action plan
      organized by risk level and business impact.

    Toggle (Accordion) element — FAQ 4:
    - (same configuration)
    - Heading text: How is this different from a free consultation?
    - Body text: A free consultation is a conversation. The Health Check is
      a structured engagement that produces written deliverables. It is
      designed for business owners who want a documented baseline, not a
      general discussion.

    Toggle (Accordion) element — FAQ 5:
    - (same configuration)
    - Heading text: What happens after the Health Check?
    - Body text: If issues are identified, you have the option to engage
      Levine Law to address them. The Health Check is not a sales pitch —
      it is a diagnostic. What you do with the findings is your decision.

  THRIVE ACCORDION CONFIGURATION NOTE: In Thrive Architect, the Toggle
  element is found under the "Advanced" or "Complex" element group. Each
  Toggle is inserted as a separate element — they are not automatically
  linked as an accordion group. To achieve "only one open at a time"
  behavior, wrap all five Toggle elements inside a single Thrive Tabs
  element (FAQ-style layout) OR accept that multiple can be open. If ML1
  wants true single-open accordion behavior, the cleanest approach is to
  use a Custom HTML element with a lightweight vanilla JS accordion.
  Custom HTML accordion code is provided at the end of this packet.
  Recommended: use the Custom HTML accordion approach for FAQ section.

Responsive behavior for Section 9:
- At 768px: left/right padding 4%
- H2: 28px at 768px
- Accordion heading font: 15px at 768px

---

### SECTION 10 — BOTTOM CTA

[SECTION ID: bottom-cta]

Thrive custom CSS class: `ll-section-bottom-cta`

Outer Content Box:
- Background color: NAVY `#1D4771`
- Padding: top 80px / bottom 80px / left 5% / right 5%
- Width: 100%

Inside:
  Columns element: 1 column, full width, centered

    Heading element:
    - Tag: H2
    - Text: Understand Where Your Business Stands.
    - Font: Roboto Bold, 44px
    - Color: WHITE `#FFFFFF`
    - Alignment: center
    - Margin-bottom: 20px

    Text element:
    - Text: The Corporate Health Check gives Ontario business owners a clear
      picture of structural alignment and a prioritized path forward.
    - Font: Roboto, 18px
    - Color: LIGHT-GRAY `#D1D5DB`
    - Line-height: 1.7
    - Alignment: center
    - Max-width: 680px (center via Thrive width control)
    - Margin-bottom: 36px

    Button element:
    - Label: Book Your Health Check
    - Link: anchor `#hero-form`
    - Background: BLUE `#0365B2`
    - Text: WHITE `#FFFFFF`, Roboto Bold, 16px, uppercase
    - Padding: 18px 48px
    - Border-radius: 4px
    - Hover background: `#024f8a`
    - Alignment: center

Responsive behavior for Section 10:
- H2: 32px at 768px / 26px at 480px
- Body text: 16px at 768px
- Button: full-width at 480px
- Padding: top 60px / bottom 60px at 768px

---

### SECTION 11 — FOOTER

[SECTION ID: footer]

If a site-wide footer Symbol (LL-FOOTER) already exists, assign it here
as a Symbol element. Do not rebuild the footer from scratch.

If no footer Symbol exists yet, create the LL-FOOTER Symbol using the
reference page footer structure:

Symbol name: `LL-FOOTER`

Content Box:
- Background: NAVY `#1D4771`
- Padding: top 48px / bottom 32px / left 5% / right 5%

  Columns element: 3 columns, 33/33/33, gap: 32px

    Column 1:
      Image element: Levine Law logo (white version)
      Max-width: 140px, margin-bottom 16px

      Text element: [Firm tagline or short descriptor from reference footer]
      Font: Roboto, 14px, LIGHT-GRAY `#D1D5DB`, line-height 1.6

    Column 2:
      Heading element: H4, "Services", Roboto Bold, 14px, WHITE, uppercase,
      letter-spacing 1px, margin-bottom 12px

      Text element (footer nav links — use Custom HTML):
      ```html
      <ul class="ll-footer-links">
        <li><a href="/ontario-corporate-health-check/">Corporate Health Check</a></li>
        <li><a href="/corporate-law-firm/">Corporate Law</a></li>
        <li><a href="/shareholder-agreements/">Shareholder Agreements</a></li>
      </ul>
      ```

    Column 3:
      Heading element: H4, "Contact", Roboto Bold, 14px, WHITE, uppercase,
      letter-spacing 1px, margin-bottom 12px

      Text element:
      - 365-599-0078
      - Link: `tel:3655990078`, color WHITE

      Text element:
      - [Contact email from reference page]
      - Link: `mailto:[email]`, color WHITE

  Divider element: solid, 1px, `rgba(255,255,255,0.15)`, full width,
  margin-top 32px, margin-bottom 16px

  Text element (copyright + legal):
  - Text: © [current year] Levine Law. All rights reserved. | Privacy
    Policy | Terms of Use
  - Font: Roboto, 12px, `#D1D5DB`, centered
  - Links for Privacy Policy and Terms of Use: [target URLs from reference]

FOOTER COPY FLAG FOR ML1: Footer column 1 tagline, column 2 service
links, column 3 email address, and privacy/terms URLs must be verified
against the reference page before publishing. These are structural
placeholders.

---

## Custom CSS Block

Enter the following CSS in one of two locations:
- Option A (preferred for page-scoped rules): In Thrive Architect, click
  on the page wrapper > Custom CSS tab > paste all CSS there.
- Option B (for site-wide rules): Thrive Dashboard > Theme Options >
  Custom CSS > paste there.

The sticky nav CSS and symbol CSS should go in Option B (site-wide).
All other CSS below is page-scoped and should go in Option A.

```css
/* =====================================================
   LEVINE LAW — ONTARIO CORPORATE HEALTH CHECK PAGE CSS
   POL-049 compliant palette tokens used throughout.
   ===================================================== */

/* --- Sticky Nav --- */
.ll-sticky-nav {
  display: flex;
  align-items: center;
  gap: 28px;
  list-style: none;
  margin: 0;
  padding: 0;
}

.ll-sticky-nav a {
  font-family: 'Roboto', sans-serif;
  font-size: 14px;
  color: #ffffff;
  text-decoration: none;
  font-weight: 400;
  transition: color 0.2s ease;
}

.ll-sticky-nav a:hover {
  color: #0365B2;
}

/* --- Hero Value Bullets --- */
.ll-value-bullets {
  list-style: none;
  margin: 0 0 32px 0;
  padding: 0;
}

.ll-value-bullets li {
  font-family: 'Roboto', sans-serif;
  font-size: 16px;
  color: #ffffff;
  line-height: 1.7;
  padding: 0 0 16px 32px;
  position: relative;
}

.ll-value-bullets li::before {
  content: '';
  position: absolute;
  left: 0;
  top: 6px;
  width: 18px;
  height: 18px;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20' fill='%230365B2'%3E%3Cpath fill-rule='evenodd' d='M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z' clip-rule='evenodd'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-size: contain;
}

.ll-bullet-label {
  font-weight: 700;
  color: #ffffff;
}

/* --- Pillar Cards — top border accent --- */
.ll-pillar-card {
  border-top: 3px solid #0365B2 !important;
}

/* --- FAQ Accordion (Custom HTML approach) --- */
.ll-faq-accordion {
  max-width: 820px;
  margin: 0 auto;
}

.ll-faq-item {
  border-bottom: 1px solid #D1D5DB;
  margin-bottom: 0;
}

.ll-faq-question {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px 24px;
  cursor: pointer;
  font-family: 'Roboto', sans-serif;
  font-size: 17px;
  font-weight: 700;
  color: #1D4771;
  background: #ffffff;
  border: none;
  width: 100%;
  text-align: left;
  transition: background 0.2s ease;
}

.ll-faq-question:hover {
  background: #f4f6f9;
}

.ll-faq-question .ll-faq-icon {
  font-size: 22px;
  color: #0365B2;
  transition: transform 0.25s ease;
  flex-shrink: 0;
  margin-left: 16px;
}

.ll-faq-item.open .ll-faq-question .ll-faq-icon {
  transform: rotate(45deg);
}

.ll-faq-answer {
  display: none;
  padding: 0 24px 20px 24px;
  font-family: 'Roboto', sans-serif;
  font-size: 16px;
  color: #000000;
  line-height: 1.8;
  background: #ffffff;
}

.ll-faq-item.open .ll-faq-answer {
  display: block;
}

/* --- Footer Links --- */
.ll-footer-links {
  list-style: none;
  margin: 0;
  padding: 0;
}

.ll-footer-links li {
  margin-bottom: 8px;
}

.ll-footer-links a {
  font-family: 'Roboto', sans-serif;
  font-size: 14px;
  color: #D1D5DB;
  text-decoration: none;
  transition: color 0.2s ease;
}

.ll-footer-links a:hover {
  color: #ffffff;
}

/* =====================================================
   RESPONSIVE OVERRIDES
   ===================================================== */

@media (max-width: 768px) {

  /* Nav */
  .ll-sticky-nav {
    display: none;
  }

  /* Hero headline */
  .ll-section-hero h1.tve_heading {
    font-size: 36px !important;
  }

  /* Hero subhead */
  .ll-section-hero .tve_text p {
    font-size: 17px !important;
  }

  /* Section headings */
  .ll-section-problem h2.tve_heading,
  .ll-section-pillars h2.tve_heading,
  .ll-section-how-it-works h2.tve_heading,
  .ll-section-why h2.tve_heading,
  .ll-section-faqs h2.tve_heading,
  .ll-section-bottom-cta h2.tve_heading {
    font-size: 28px !important;
  }

  /* Bottom CTA H2 */
  .ll-section-bottom-cta h2.tve_heading {
    font-size: 32px !important;
  }

  /* FAQ question */
  .ll-faq-question {
    font-size: 15px;
    padding: 16px 16px;
  }

  .ll-faq-answer {
    padding: 0 16px 16px 16px;
    font-size: 15px;
  }
}

@media (max-width: 480px) {

  .ll-section-hero h1.tve_heading {
    font-size: 30px !important;
  }

  .ll-section-problem h2.tve_heading,
  .ll-section-pillars h2.tve_heading,
  .ll-section-how-it-works h2.tve_heading,
  .ll-section-why h2.tve_heading,
  .ll-section-faqs h2.tve_heading {
    font-size: 24px !important;
  }

  .ll-section-bottom-cta h2.tve_heading {
    font-size: 26px !important;
  }

  /* Full-width buttons on mobile */
  .ll-section-hero .thrv_button,
  .ll-section-bottom-cta .thrv_button {
    width: 100% !important;
    text-align: center !important;
  }
}
```

---

## Custom HTML — FAQ Accordion (Replace Thrive Toggle Elements)

If ML1 chooses the Custom HTML accordion approach for Section 9 FAQs
(recommended for true single-open behavior), replace the five Toggle
elements in Section 9 with a single Custom HTML element containing the
following HTML. The CSS above handles all styling.

```html
<div class="ll-faq-accordion">

  <div class="ll-faq-item">
    <button class="ll-faq-question">
      What is the Ontario Corporate Health Check?
      <span class="ll-faq-icon">+</span>
    </button>
    <div class="ll-faq-answer">
      A structured legal review of your company's governance and commercial
      structure. We examine five areas — shareholder agreements, corporate
      records, employment, commercial contracts, and transaction readiness —
      and deliver a written findings report with a prioritized action plan.
    </div>
  </div>

  <div class="ll-faq-item">
    <button class="ll-faq-question">
      Who is it for?
      <span class="ll-faq-icon">+</span>
    </button>
    <div class="ll-faq-answer">
      Ontario businesses with at least CAD 5M in annual cash flow, typically
      with 5–30 employees, that operate in a strategic industry lane and want
      to understand whether their legal structure still reflects how the
      business actually works.
    </div>
  </div>

  <div class="ll-faq-item">
    <button class="ll-faq-question">
      What do I receive at the end?
      <span class="ll-faq-icon">+</span>
    </button>
    <div class="ll-faq-answer">
      A written findings report documenting alignment, gaps, and exposures
      across the five pillars — plus a prioritized action plan organized by
      risk level and business impact.
    </div>
  </div>

  <div class="ll-faq-item">
    <button class="ll-faq-question">
      How is this different from a free consultation?
      <span class="ll-faq-icon">+</span>
    </button>
    <div class="ll-faq-answer">
      A free consultation is a conversation. The Health Check is a structured
      engagement that produces written deliverables. It is designed for
      business owners who want a documented baseline, not a general discussion.
    </div>
  </div>

  <div class="ll-faq-item">
    <button class="ll-faq-question">
      What happens after the Health Check?
      <span class="ll-faq-icon">+</span>
    </button>
    <div class="ll-faq-answer">
      If issues are identified, you have the option to engage Levine Law to
      address them. The Health Check is not a sales pitch — it is a
      diagnostic. What you do with the findings is your decision.
    </div>
  </div>

</div>

<script>
(function() {
  var items = document.querySelectorAll('.ll-faq-item');
  items.forEach(function(item) {
    var btn = item.querySelector('.ll-faq-question');
    btn.addEventListener('click', function() {
      var isOpen = item.classList.contains('open');
      // close all
      items.forEach(function(i) { i.classList.remove('open'); });
      // open this one if it was closed
      if (!isOpen) { item.classList.add('open'); }
    });
  });
})();
</script>
```

NOTE: Thrive Architect's Custom HTML element renders script tags. The
inline script above uses an IIFE (immediately-invoked function expression)
to avoid global scope pollution. Test after publishing in a staging
environment to confirm the accordion fires correctly before live deployment.

---

## Responsive Settings Summary

| Section | Desktop | 768px tablet | 480px mobile |
|---|---|---|---|
| Nav | Full horizontal, sticky | Hide nav links, show CTA + phone only | CTA full-width, phone below |
| Hero cols | 55/45 | 1 col, form card on top | 1 col |
| Hero H1 | 52px | 36px | 30px |
| Hero subhead | 20px | 17px | 15px |
| Section 3 H2 | 40px | 28px | 24px |
| Pillars row 1 | 3 cols | 1 col | 1 col |
| Pillars row 2 | 2 cols centered | 1 col | 1 col |
| How It Works | 3 cols | 1 col | 1 col |
| Why LL | 4 cols | 2 cols | 1 col |
| About | 2 cols 35/65 | 1 col, photo above | 1 col |
| Testimonials | 2 cols | 1 col | 1 col |
| FAQs | 1 col, max 820px centered | full-width, padding 4% | full-width |
| Bottom CTA | 1 col | 1 col, H2 32px | H2 26px, btn full-width |
| Footer | 3 cols | 1 col | 1 col |

---

## Build Sequence Recommendation for ML1

Execute in this order to avoid dependency issues:

1. Create the WordPress page (title, slug, parent, template, Draft status).
2. Set up the Thrive Leads form (Health Check Hero Form) and note the
   shortcode ID before opening Thrive Architect.
3. Create or locate the LL-HEADER-STICKY Symbol and LL-FOOTER Symbol.
4. Open the page in Thrive Architect.
5. Insert Section 1 (nav Symbol or sticky header).
6. Build Section 2 (hero) — paste the Thrive Leads shortcode into the
   Custom HTML element in Column 2.
7. Build Sections 3, 4, 5, 6, 7 in order.
8. Build Section 8 (testimonials) — have approved testimonial copy ready.
9. Build Section 9 (FAQs) using the Custom HTML accordion block.
10. Build Section 10 (bottom CTA).
11. Insert footer Symbol.
12. Enter Custom CSS in the page-level Custom CSS tab.
13. Switch to responsive preview (768px and 480px) and verify all
    column stacking and font sizes. Apply per-element responsive overrides
    as needed.
14. Set Yoast SEO fields.
15. Save. Leave as Draft.
16. Share preview link with ML1 for review.

---

## Outstanding Items Flagged for ML1 Decision

1. PALETTE: Reference pages use `#031b33` and `#2f7ece`. This packet uses
   POL-049 compliant equivalents. ML1 must decide: use compliant palette
   OR approve explicit exception to match reference pages.

2. TESTIMONIALS: Exact testimonial copy not provided in brief. ML1 must
   supply the 4 approved testimonials before Section 8 is complete.

3. BIO COPY: Exact bio copy from reference page not provided. ML1 must
   paste approved bio copy into Section 7 Text element.

4. FORM COLOR — SUBTITLE: Form card subtitle uses text color `#666666`
   which is not in the active POL-049 palette. Use BLACK `#000000` unless
   ML1 approves an exception.

5. TESTIMONIAL BACKGROUND: Sections 8 and FAQ body use a light gray
   (`#F4F6F9` / `#F9FAFB`) outside the active palette. Use WHITE
   `#FFFFFF` for strict compliance, or ML1 to approve exception.

6. MENU PLACEMENT: This is a Level 3 conversion page per POL-051. Whether
   to include it in main site navigation is an ML1 decision. The page slug
   and parent page are set; menu item should only be added on ML1
   instruction.

7. FOOTER COPY: Footer column 1 tagline, contact email, and privacy/terms
   URLs are placeholders. ML1 to confirm from reference page.

8. WHY LEVINE LAW TILE COPY: Tile body descriptions in Section 6 are
   inferred from the offer. ML1 to confirm or substitute approved copy
   from the reference page.

9. THRIVE LEADS > GHL CONNECTION: The form must be connected to Go High
   Level via Thrive Leads API Connections before the page is live. ML1
   to verify the GHL integration is active and the correct pipeline and
   tag are applied.

10. THANK YOU PAGE: A `/health-check-thank-you/` redirect page is needed
    as the form success destination. This page is not in scope for this
    packet but must be created before the form goes live.

---

## ML1 Publish Step

This page is a Draft. To publish:
1. Open the page in WordPress > Thrive Architect.
2. Review all sections end-to-end in desktop and mobile preview.
3. Confirm all Outstanding Items above are resolved.
4. Confirm Thrive Leads form is connected to GHL.
5. Confirm all internal links and anchor scrolls work.
6. Verify Yoast SEO fields are complete.
7. Change page Status from Draft to Published.
8. Add menu item to the correct WordPress menu location and position
   per ML1 instruction.
9. Test form submission end-to-end (submit a test lead and confirm it
   appears in GHL with the correct tag and pipeline).

INV-0002 applies: ML1 must execute all publish actions. No autonomous
publish by the system.
