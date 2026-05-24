---
id: POL-051
title: LL Website Information Architecture Policy
owner: ML1
status: approved
approval: ML1
approved_by: ML1
approved_date: 2026-04-18
version: 0.1
effective_date: 2026-04-18
supersedes:
provenance:
  decided_by: ML1
  decided_on: 2026-04-18
  context: Metadata normalized by system admin cleanup on 2026-05-24
created_date: 2026-03-21
last_updated: 2026-03-21
tags: [policy, website, information-architecture, marketing, landing-pages]
---

# POL-051 — LL Website Information Architecture Policy

Policy Statement: The Levine Law website must follow a defined multi-level information architecture so homepage navigation, pillar pages, inquiries, and opt-in landing pages each have distinct roles and do not collapse into each other.

Authority (Principles referenced): PRN-005, PRN-009, PRN-020, PRN-021  
Boundary function: This policy defines structural website roles and page-level routing logic.  
Supersedes: None

---

## 1. Purpose

This policy defines the canonical website hierarchy for Levine Law.

It exists to prevent:
- homepage clutter
- page-role confusion
- mixing pillar-page education with aggressive opt-in behavior
- collapsing industry, service, and inquiry functions into one page type

---

## 2. Scope

This policy applies to:
- `levine-law.ca`
- any migrated or transitional pages from `levinelegal.ca`
- homepage navigation structure
- pillar pages
- service pages
- inquiries pages
- industry, client-profile, and service-specific soft landing pages

---

## 3. Canonical Website Hierarchy

### 3.1 Level 1

Level 1 consists of the homepage only.

Canonical Level 1 page:
- Home

The homepage is the top-level routing page for the site.

It must direct users to the primary Level 2 pages without trying to carry the
full burden of education, service explanation, and opt-in behavior itself.

### 3.2 Level 2

Level 2 consists of the primary website pillar / routing pages.

Canonical Level 2 pages:
- Industries / Industries Served
- Services / How We Help
- Inquiries

These pages sit directly below the homepage and perform distinct functions.

### 3.3 Level 3

Level 3 consists of narrower pages beneath the Level 2 structure.

Canonical Level 3 page types:
- industry-specific pages
- client-profile-specific pages
- service-specific soft landing pages

These are the pages where Levine Law actively seeks:
- opt-in behavior
- contact initiation
- more focused conversion intent

---

## 4. Page Role Definitions

### 4.1 Home

The homepage:
- introduces Levine Law at a high level
- routes users to the correct Level 2 page
- must not attempt to replace Level 2 or Level 3 pages

### 4.2 Industries / Industries Served

The Industries page is a Level 2 pillar page.

Its function is to:
- explain the industries Levine Law serves
- show why industry context matters
- organize industry-facing website information
- route users downward to relevant Level 3 pages

The Industries page is primarily:
- educational
- organizational
- navigational

It may contain a CTA, but it must not behave like a hard-conversion landing page.

### 4.3 Services / How We Help

The Services page is a separate Level 2 page.

Its function is to:
- explain how Levine Law helps
- organize services, solutions, or engagement pathways
- distinguish service logic from industry logic

The Services page must remain structurally distinct from the Industries page.

### 4.4 Inquiries

The Inquiries page is a separate Level 2 page.

Its function is to:
- provide the general inquiry path
- receive users who are ready to make contact but are not yet best routed to a
  narrower Level 3 page

The Inquiries page is not a substitute for Level 3 landing pages.

### 4.5 Level 3 Soft Landing Pages

Level 3 pages are the targeted pages where Levine Law actively seeks opt-in /
get-in-touch behavior.

These pages should be used when the visitor has:
- a specific industry context
- a defined client profile
- a specific service or issue pattern

Level 2 pages should usually route users to the appropriate Level 3 page rather
than absorbing all conversion behavior themselves.

---

## 5. Structural Rules

### 5.1 Distinct Roles Are Mandatory

Industries, Services, and Inquiries must not be collapsed into one page or one
page type.

### 5.2 Level 2 Pages Route; Level 3 Pages Convert

Level 2 pages primarily:
- educate
- organize
- route

Level 3 pages primarily:
- narrow
- qualify
- invite contact or opt-in

### 5.3 Homepage Must Link to Canonical Level 2 Pages

The homepage must link to:
- Industries / Industries Served
- Services / How We Help
- Inquiries

### 5.4 Transitional Domain Pages Must Be Reconciled to the Canonical Structure

Where legacy pages exist on `levinelegal.ca`, they must be evaluated against the
canonical Level 1 / Level 2 / Level 3 structure and either:
- migrated,
- merged,
- redirected, or
- retired

### 5.5 Funnel Separation Must Be Preserved

Website structure must not create confusion between different Levine Law funnel
or offer paths.

Industry pages, service pages, and inquiry routing must preserve approved
positioning and funnel boundaries.

---

## 6. Canonical Site Map

```text
Level 1
- Home

Level 2
- Industries / Industries Served
- Services / How We Help
- Inquiries

Level 3
- Industry-specific soft landing pages
- Client-profile-specific soft landing pages
- Service-specific soft landing pages
```

Routing model:

```text
Home
  -> Industries / Industries Served
      -> Level 3 industry / client-profile / service soft landing pages
  -> Services / How We Help
      -> Level 3 service-specific soft landing pages
  -> Inquiries
```

---

## 7. Operational Implication

Any website review, redesign, migration, or page-build task must respect this
information architecture.

In particular:
- homepage work must preserve Level 2 routing
- Industries page work must preserve its pillar-page function
- Services page work must remain separate from industry organization
- Inquiries page work must remain a distinct general-contact path
- Level 3 pages are the main targeted opt-in surfaces

---

## 8. Related Doctrine

- `POL-032` (Marketing Lifecycle Definition and Boundary)
- `POL-050` (LL Brand Identity Policy)
- `INV-0002` (No Autonomous Publish)
- `04_INITIATIVES/LL_PORTFOLIO/08_MARKETING/README.md`

