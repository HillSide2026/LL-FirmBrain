---
title: F3 Incident Sourcing Agent — Specification
owner: ML1
status: active
version: 2.0
created_date: 2026-04-15
last_updated: 2026-04-15
tags: [funnel-03, agent-spec, signal-sourcing, content-production]
id: 04_initiatives_ll_portfolio_08_marketing_llp_013_funnel3_management_planning_incident_sourcing_agent_spec_md
---

# F3 Incident Sourcing Agent — Specification

---

## 1. Objective

Identify and extract reportable incidents relevant to payments, crypto, and fintech that
are suitable for timely, topical content anchoring.

The agent surfaces developments that place a company, product, flow, platform, or
operating model into current market conversation — and routes each valid incident to
the appropriate post in the F3 content master list.

Output is structured incident cards ready for use in content production. The agent does
not draft content.

---

## 2. Subject Matter Scope

Monitor incidents across three overlapping areas:

### A. Payments

Domestic and cross-border payments; acquiring, issuing, payout infrastructure,
remittance, settlement, treasury movement; banking partners, payment processors, PSPs,
intermediaries, rails, routing, reconciliation.

### B. Crypto

Exchanges, stablecoins, wallets, custody, on-chain settlement, off-ramp/on-ramp
infrastructure; tokenized payment flows; crypto-fiat interaction points;
blockchain-based financial infrastructure; custody, reserve, settlement, listing,
delisting, access, partner dependencies.

### C. Fintech

Fintech products and platforms handling or enabling movement of money, value, credit,
stored value, customer balances, or financial access; banking-as-a-service, embedded
finance, neobanks, lending platforms, card programs, treasury tools, compliance
infrastructure, financial software tied to regulated activity; licensing, partner
dependencies, operational restrictions, market entry, supervision, shutdowns, product
changes with financial infrastructure implications.

---

## 3. Valid Incident Criteria

An incident is valid if it reflects a concrete development in one or more of the
following categories:

### A. Institutional Action
Bank action; regulator action; exchange or platform action; partner action; enforcement
action; licensing or registration action.

### B. Operational Change
Product launch with infrastructure implications; rollout of new rail, asset, corridor,
capability, or partner; change in routing, custody, settlement, access, or account
structure; pricing, eligibility, reserve, withdrawal, deposit, or payout changes.

### C. Constraint or Friction
Delay, suspension, restriction, rejection, de-risking, heightened diligence, onboarding
friction, service limitation, access loss, partner termination.

### D. Market Structure Event
Acquisition or partnership that changes control, flow, access, distribution, or
operating model; expansion into a new jurisdiction; exit from a product, corridor,
asset, or market; failure, outage, shutdown, insolvency, freeze, or wind-down.

---

## 4. Exclusions

Do not include:

- Funding announcements with no operating relevance
- Generic hiring news
- General market commentary
- Opinion pieces without a concrete event
- Pure feature releases with no financial, regulatory, operational, or partner
  significance
- Broad trend articles with no identifiable incident
- Gossip or personality-driven coverage
- Incidents whose primary impact is on retail consumers or investors rather than
  operators

---

## 5. Input Sources

Sources are tiered by ICP presence. Prioritise Tier 1. Use Tier 2 to supplement.
Tier 3 is supplementary only and should not dominate the signal feed.

### Tier 1 — Confirmed ICP Presence

| Source | Type |
|---|---|
| Stablecoin Insider | Industry newsletter — stablecoin/crypto payments |
| PYMNTS | Trade publication — payments executives |
| Payments NEXT | Trade publication — payments operators |
| Payments Dive (Industry Dive) | Trade publication — payments executives |

### Tier 2 — Probable ICP Presence

| Source | Type |
|---|---|
| BetaKit | Canadian fintech news |
| Fintech Blueprint (Lex Sokolin) | Newsletter — fintech operators and founders |
| The Paypers | Global payments intelligence |
| Fintech.ca | Canadian fintech aggregator |

### Tier 3 — Supplementary

| Source | Type |
|---|---|
| Company press releases | Operator-direct announcements |
| Company blogs and changelogs | Product and infrastructure updates |
| Status pages | Operational disruptions |
| Policy and partner update pages | Structural changes |
| Financial regulator publications | FINTRAC, OSFI, Bank of Canada, FCAC, RPAA-related |
| Central bank and payments authority notices | BoC, CDIC, CIRO |
| Securities regulators | OSC, CSA (for incidents with payments intersection) |
| Enforcement authority publications | FINTRAC enforcement, DOJ, FinCEN (US, where relevant) |
| Sanctions and licensing databases | OFAC, FINTRAC registration, RPAA registry |
| Official exchange or institutional notices | Direct from named platforms |

---

## 6. Processing Steps

---

### Step 1 — Event Extraction

For each source item, extract:

- Entity or entities involved
- Date
- Event
- Affected product, flow, asset, jurisdiction, or business line

---

### Step 2 — Scope Check

Confirm that the incident is relevant to at least one of:

- Payments
- Crypto
- Fintech

If none: discard.

---

### Step 2B — ICP Relevance Check

Confirm that the incident is relevant to the operating environment of at least one of
the four F3 ICP profiles:

| Profile | Description |
|---|---|
| Dani | Canadian fintech founder; cross-border payroll/MSB; Series A; RPAA and banking friction |
| James | US-based expansion VP entering Canada; no Canadian entity yet; architecture classification questions |
| Omar | Seed-stage stablecoin infrastructure operator; USDC-based settlement; MSB/RPAA classification; banking access |
| Kevin | CCO at established Canadian MSB; $200M volume; RPAA, RTR, bank de-risking, stablecoin operational questions |
| Sara | Series B embedded finance/BaaS operator; partner bank compliance friction; MSB classification uncertainty; card program compliance |
| David | COO at Canadian crypto custody/wallet platform; MSB-registered; FINTRAC examination risk; RPAA/custody overlap; institutional client compliance |

An incident is ICP-relevant if it affects the operating environment of at least one
profile — the companies they build, the partners they depend on, the regulators they
answer to, or the infrastructure they operate.

Incidents whose primary impact is on retail consumers, retail investors, or
consumer-facing products without operator-layer implications: discard.

---

### Step 3 — Reportability Check

Confirm that the incident is:

- Current or recent (see recency thresholds below)
- Concrete — tied to a named entity, specific action, or identifiable change
- Externally visible — sourced from a publication, regulator, or official notice
- Suitable for topical content — not speculative, not resolved with no residual relevance

**Recency thresholds by incident type:**

| Incident type | Maximum age for content use |
|---|---|
| Operational (outage, suspension, partner change, access loss) | 7 days |
| Regulatory / institutional (enforcement, registration change, policy update) | 21 days |
| Structural / market (acquisition, exit, new rail launch, jurisdiction entry/exit) | 30 days |

Incidents past threshold: archive. Available for background context but not surfaced
as content-ready.

---

### Step 4 — Category Assignment

Assign one primary category:

- BANK_ACTION
- REGULATORY_ACTION
- PARTNER_ACTION
- PRODUCT_OR_INFRASTRUCTURE_CHANGE
- MARKET_ENTRY_OR_EXIT
- SERVICE_DISRUPTION
- ENFORCEMENT_OR_RESTRICTION
- CRYPTO_ASSET_OR_STABLECOIN_EVENT
- FINTECH_OPERATING_MODEL_CHANGE

---

### Step 5 — Relevance Tagging

Tag the incident by applicable subject area. An incident may carry multiple tags.

- PAYMENTS
- CRYPTO
- FINTECH

---

### Step 6 — Operational Relevance Mapping

Identify which of the following are affected:

Access; distribution; bankability; compliance exposure; customer funds handling;
custody; settlement; liquidity; reconciliation; onboarding; withdrawals or deposits;
partner dependency; jurisdictional expansion; product viability.

---

### Step 6B — Content Routing

Map the incident to the F3 content framework. This step bridges signal sourcing and
content production.

**A. Master list mapping**
Identify which post(s) from the F3 Content Master List this incident most naturally
anchors. Reference post number and title. An incident may anchor more than one post.

**B. Content mode**
Identify which content mode the incident calls for:

| Mode | Use when |
|---|---|
| DIAGNOSIS | Incident illustrates a failure pattern, degradation mechanism, or structural problem |
| JUDGMENT | Incident forces a prioritisation or decision-making question |
| TRADEOFFS | Incident places two viable options in tension with real costs on each side |
| DEFINITION_OF_GOOD | Incident illustrates a well-functioning system, launch, or practice |

**C. Category**
Identify the primary content category (1–8):

| # | Category |
|---|---|
| 1 | Expansion & Growth |
| 2 | Speed & Reliability |
| 3 | Cost & Margin |
| 4 | Infrastructure & Rails |
| 5 | Product Design & UX |
| 6 | Stablecoins & New Rails |
| 7 | Bridge — regulation as market observation |
| 8 | Canada Bridge |

---

### Step 7 — Canada Lens

For each valid incident, identify:

- **Direct Canadian relevance** — the incident involves a Canadian entity, regulator,
  rail, or jurisdiction
- **Indirect Canadian relevance** — the incident involves a non-Canadian entity or
  market but has structural implications for Canadian operations
- **No current Canadian relevance**

If relevant, note the Canadian angle and which ICP profile(s) it applies to:

| Angle | Most relevant profile(s) |
|---|---|
| Market entry friction | James, Omar, Sara |
| Banking partner implications | Dani, Omar, Kevin, David |
| MSB registration or RPAA classification | Dani, Omar, James, Sara |
| Stablecoin or crypto treatment under PCMLTFA / RPAA | Omar, Kevin, David |
| Payment infrastructure constraints (RTR, Interac, rail access) | Dani, James, Kevin |
| Bank de-risking or account access | Omar, Kevin, David |
| Enforcement or compliance action | Kevin, David |
| Embedded finance or BaaS implications | Dani, James, Sara |
| Custody or wallet regulatory treatment | David, Omar |
| Card program or program manager compliance | Sara |
| Partner bank requirements or risk appetite shift | Sara, Dani |

---

## 7. Output Format — Incident Card

---

**Headline:**
Clear, factual summary of incident. Noun phrase or declarative statement. No theatrical
language.

**Date:**
Date of incident or announcement.

**Source:**
Publication, regulator, company, or institutional source.

**Primary Category:**
One category from the classification list.

**Subject Tags:**
PAYMENTS / CRYPTO / FINTECH

**Entities Involved:**
Named companies, regulators, banks, platforms, or assets.

**Event Summary:**
1–3 sentence factual summary.

**Why It Is Reportable:**
Short statement explaining why this is a timely, topical development.

**Operational Relevance:**
List of affected areas from Step 6.

**ICP Profile(s):**
Which of Dani / James / Omar / Kevin this incident is most relevant to, and why.

**Content Mode:**
DIAGNOSIS / JUDGMENT / TRADEOFFS / DEFINITION_OF_GOOD

**Content Routing:**
Post number(s) and title(s) from the master list. Content category (1–8).

**Canada Relevance:**
Direct / Indirect / None

**Canada Angle:**
Short explanation of Canadian dimension and which ICP profile(s) it applies to.

**Content Angle:**
One sentence describing what this incident enables the post to do — the argument or
observation it supports. This is not a drafted hook. Hook writing is a content
production task governed by the Content Production Standard.

---

## 8. Volume Targets

| Stage | Target |
|---|---|
| Raw signals per day | 10–20 |
| Pass scope check (Step 2) | ~70% |
| Pass ICP relevance check (Step 2B) | ~50% of scope-passing |
| Valid incidents per week | 15–25 |
| Shortlist candidates per week | 5–10 |
| Content-ready incidents per week | 2–5 |

---

## 9. Quality Standard

A valid, content-ready incident must meet all of the following:

- Tied to payments, crypto, or fintech
- Concrete and recent (within applicable recency threshold)
- Relevant to the operating environment of at least one F3 ICP profile
- Reportable without speculation
- Routed to at least one post in the F3 content master list
- Carries a content mode and content angle

---

## 10. System Summary

1. Monitor current developments across payments, crypto, and fintech using the tiered
   source list.
2. Filter for scope, ICP relevance, and reportability.
3. Classify by incident category, subject area, and operational relevance.
4. Route to the F3 content master list — identify post(s), content mode, and category.
5. Apply Canada lens where relevant, mapped to ICP profiles.
6. Output structured incident cards for content production.

The agent does not draft titles, hooks, or post copy. All content production is
governed by the Content Production Standard.
