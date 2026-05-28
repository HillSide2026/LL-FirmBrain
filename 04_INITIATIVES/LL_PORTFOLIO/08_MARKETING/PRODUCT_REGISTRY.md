---
id: mkt__product_registry
title: Product Registry — All Funnels
owner: ML1
status: working
created_date: 2026-04-05
last_updated: 2026-05-27
tags: [product-registry, funnel-01, funnel-02, funnel-03, pricing]
---

# Product Registry — All Funnels

> Working registry. Prices from ML1-supplied pricing table 2026-04-05. ML1 review required before any build or deployment.
> Collisions flagged for ML1 resolution.

---

## Registry Table

| # | Product Name | Regular Price | Intro Price | Funnel | Format | Audience | Status |
|---|---|---|---|---|---|---|---|
| 1 | Business Structure Diagnostic | $259 | $49 | F1 | Async written output, 1-page, 48hr delivery | Ontario SMB owner, existing corp, nagging structural concern | Documented — PRE-ENGAGEMENT_MONETIZATION_SHORTLIST.md |
| 2 | Shareholder Dispute Readiness Guide | $97 | $9 | F1 | PDF, 8–12 pages | Ontario SMB owner in deteriorating partnership | Documented — PRE-ENGAGEMENT_MONETIZATION_SHORTLIST.md |
| 3 | Corporate Governance Triage Consult | $859 | — | F1 / F2 | Live consultation (ML1) | Ontario SMB owner with governance or structural urgency | Not separately documented — see collision note below |
| 4 | Corporate Check-Up | $2,499 | — | F2 | Full document review + structured analysis + delivery meeting | $1M–$8M Ontario operator, preventative, not in crisis | Documented in F2 positioning.yaml — see collision note below |
| 5 | AML Health Check Consult | $859 | — | F3 | Live consultation (ML1) | Registered MSBs / PSPs preparing for exam or with AML program concerns | Mentioned in F3 entry_offers.md upsell path; not separately scoped as consultation product |
| 6 | STR Triage Consult | $859 | — | F3 | Live consultation (ML1) | Canadian MSBs / PSPs facing suspicious transaction threshold questions | Mentioned in F3 entry_offers.md Entry 2; priced at $3,500–$7,500 per incident in entry_offers.md — see collision note below |
| 7 | Six (6) Hidden Owner/Operator Mistakes You Cannot Afford to Make | $97 | — | F1 or F2 | PDF or digital guide | Ontario SMB owner/operator | Not documented — title truncated in source; funnel assignment unclear — see collision note below |
| 8 | Whitepaper: Tokenization in Canadian Capital Markets | $97 | — | F3 | PDF whitepaper | Fintech / token issuers with Canadian capital markets exposure | Not documented in current F3 content files |
| 9 | Six (6) STR Mistakes That Create Unnecessary Regulatory Risk | $97 | — | F3 | PDF or digital guide | Canadian MSBs / PSPs with STR reporting obligations | Not documented in current F3 content files |
| 10 | Six (6) Hidden MSB Triggers in Fintech & Crypto | $97 | — | F3 | PDF or digital guide | Fintech and crypto operators with potential unregistered MSB exposure | Not documented in current F3 content files |
| 11 | LL Funnel 2026 — Launch Your Payments Business in Canada | Free for first 3 months; paid platform version after revision | — | F3 | E-book | Payments, MSB, PSP, stablecoin, and embedded-finance operators seeking a Canada-entry/regulatory-readiness mental model | Draft concept documented in legacy payments folder; distinct from `Canadian Fintech Law in 2026`; requires lifecycle tracking |
| 12 | RPAA Applicability Checklist for Payment Service Providers | $97 | — | F3 | PDF or digital guide | PSPs and payment operators assessing Bank of Canada registration exposure | Pending offer approval; specification pending; do not add to Stripe until RPAA offer approved |
| 13 | RPAA Registration Consult | $859 | — | F3 | Live consultation (ML1) | PSPs and payment operators with Bank of Canada registration, payment-function, safeguarding, or application-review questions | Pending offer approval; specification pending; do not add to Stripe until RPAA offer approved |

---

## Collision Log

> All items below require ML1 resolution before build.

---

### COLLISION 1 — Corporate Governance Triage Consult rate vs. ML1 rate in F1 shortlist

**Issue:** PRE-ENGAGEMENT_MONETIZATION_SHORTLIST.md (Product B upsell path) records the ML1 consultation rate as $475. The pricing table lists "Corporate Governance Triage Consult" at $859.

**Possibilities:**
- (a) The $475 rate in the shortlist is wrong / outdated — canonical ML1 consult rate is $859.
- (b) The $475 rate is a separate lower-tier consult (e.g., associate rate or an older product), and $859 is for a named triage product.
- (c) Both products exist at different price points.

**Pending:** ML1 to confirm canonical ML1 consult rate and whether $475 product still exists.

**Affected files:** `LLP-011/PRE-ENGAGEMENT_MONETIZATION_SHORTLIST.md` (price table row for ML1 consult)

---

### COLLISION 2 — "Corporate Check-Up" vs. "Ontario Corporate Health Check (TM)"

**Issue:** The pricing table names this product "Corporate Check-Up" at a fixed $2,499. F2 positioning.yaml uses "Ontario Corporate Health Check" with a range of $2,500–$4,500. The shortlist and F2 docs use "Corporate Health Check (TM)."

**Three-part conflict:**
- Name: "Corporate Check-Up" vs. "Ontario Corporate Health Check" / "Corporate Health Check (TM)"
- Price: $2,499 fixed vs. $2,500–$4,500 range
- Tier: positioning.yaml includes Health Check + Workshop ($6k) and Maintenance Retainer — not reflected in pricing table

**Pending:** ML1 to confirm (a) canonical product name, (b) fixed vs. range pricing, (c) whether $2,499 is the intro or regular rate.

**Affected files:** `04_FUNNELS/funnel-02/positioning.yaml`, `LLP-011/PRE-ENGAGEMENT_MONETIZATION_SHORTLIST.md` (price table)

---

### COLLISION 3 — STR Triage Consult price ($859) vs. Entry 2 price ($3,500–$7,500)

**Issue:** The pricing table lists "STR Triage Consult" at $859. F3 entry_offers.md prices Entry 2 (Suspicious Transaction Triage & STR Filing) at $3,500–$7,500 per incident.

**Likely explanation:** These are different products. The $859 consult is a scoped assessment/call; the $3,500–$7,500 is the full STR threshold analysis + drafting + internal debrief engagement. If so, the registry should distinguish them clearly.

**Pending:** ML1 to confirm whether the $859 "STR Triage Consult" is a pre-engagement assessment that gates into the $3,500–$7,500 engagement, or a standalone substitute.

**Affected files:** `04_FUNNELS/funnel-03/entry_offers.md`

---

### COLLISION 4 — "Six (6) Hidden Owner/Operator Mistakes" — funnel assignment and full title unknown

**Issue:** Title was truncated in the source pricing table as "Six (6) Hidden Owner/Operator Mistakes You Cann[ot...]." Full title and funnel assignment are unknown.

**Pending:** ML1 to provide full title and confirm F1 or F2 assignment.

---

## F3 Product Notes

Products 8–10 are $97 PDF/digital products not currently documented in any F3 content or scope file. F3 entry_offers.md documents service-level entry offers (MSB Registration Mandate, STR Triage, and AML Health Check) and core offers — none of which are $97 PDF products. RPAA Registration Readiness & Application Review is recorded as a pending candidate, not an approved entry offer.

These three products represent a parallel low-ticket F3 entry layer (similar to F1's Product A), and may benefit from the same GHL + Stripe build approach used in F1.

**No action taken** — pending ML1 confirmation of whether these are approved for the F3 product stack.

Product 11 is a distinct e-book authority asset, not the same asset as
`Canadian Fintech Law in 2026`.

Products 12 and 13 were added to reflect the RPAA front-door offer candidate.
They are pending approval and specification. Product 12 should satisfy the
previously identified RPAA lead-magnet gap if approved. Product 13 would become
the pre-entry consult that gates into the broader fixed-fee RPAA Registration
Readiness & Application Review mandate if approved.

Lifecycle:
- launch version: free for the first three months after release
- revision: revise after the free launch window
- paid platform version: post revised version on a separate platform for sale
- planned update: update again in 2027

This e-book should sit at the free authority / trust-building layer of F3 during
the launch window, then become a paid external-platform asset after revision.

---

## Summary of Confirmed Products (No Collisions)

| Product | Funnel | Prices Confirmed | Documentation Complete |
|---|---|---|---|
| Shareholder Dispute Readiness Guide | F1 | $9 intro / $97 regular | Yes — shortlist |
| Business Structure Diagnostic | F1 | $49 intro / $259 regular | Yes — shortlist |

All other products have either collision flags, documentation gaps, or both.
