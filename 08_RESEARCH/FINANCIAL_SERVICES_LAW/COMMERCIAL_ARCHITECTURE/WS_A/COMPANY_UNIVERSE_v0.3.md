---
id: ws-a-company-universe-v0.3
title: WS-A Company Universe v0.3
workstream: WS-A
artifact_type: WS-A/0
status: draft
approved_by:
approved_date:
version: 0.3
supersedes: ws-a-company-universe-v0.2
output_label: Derived from disclosed agreement (SEC)
---

# WS-A/0 — Company Universe v0.3

**Workstream:** WS-A (SEC Disclosure Mining)
**Artifact Type:** WS-A/0 — Company Universe
**Status:** Draft — pending ML1 approval
**Output Label:** Derived from disclosed agreement (SEC)
**Supersedes:** v0.2 (2026-04-25)

---

## Purpose

This document is the canonical target list for Workstream A research. It defines
which companies are in scope for SEC EDGAR disclosure mining, their filing status,
expected agreement archetypes, and research priority.

The universe is organized into seven categories. Sponsor Banks are an elevated
category: they are not payment fintechs, but they are load-bearing counterparties
in issuer processor, program manager, and sponsor bank agreements. Their SEC
filings disclose these relationships from the bank's perspective. Canadian Major
Banks with US Presence is a new elevated category added in v0.3: these institutions
are relevant as correspondent banking counterparties, cross-border payment rail
providers, and increasingly as fintech program sponsors in Canada-US structures.

---

## Category 1 — Issuer Processing / Program Management / BaaS

| Company | SEC Status | CIK | Priority | Target Archetypes | Research Status |
|---|---|---|---|---|---|
| Marqeta, Inc. | SEC-registered (NASDAQ: MQ) | 1522540 | HIGH | Issuer Processor, Program Manager, Platform/Customer MSA | Initial harvest done (draft 2026-04-25). EX-10.21 (Sutton Bank PM Agmt) and EX-10.14 (Block MSA) extracted. Liability provisions redacted. Next: Bancorp/Green Dot to cross-reference Program Manager archetype. |
| Galileo Financial Technologies | Not SEC-registered; appears via SoFi Technologies (NASDAQ: SOFI) | 1818874 (SoFi) | MEDIUM | Issuer Processor, Program Manager, BaaS | Not yet initiated. Galileo acquired by SoFi 2020. Search SoFi 10-K/S-1 EX-10 exhibits for Galileo-related processing agreements. SoFi Bank N.A. (OCC-chartered 2022) alters sponsor bank dependency for newer programs. |
| Green Dot Corporation | SEC-registered (NYSE: GDOT) | 1309108 | HIGH | Sponsor Bank, Program Manager, Prepaid Card Program | Not yet initiated. Dual role (sponsor bank + issuer of own prepaid products) makes this a two-sided disclosure source. 10-K filings likely include program manager agreements from the bank's perspective. |
| i2c Inc. | Not SEC-registered (private) | — | LOW | Issuer Processor, Program Manager | Not yet initiated. Private company; no SEC filings. May appear as processor counterparty in clients' filings. Use client-side filings as indirect source. |

---

## Category 2 — Merchant Acquiring / Payment Processing

| Company | SEC Status | CIK | Priority | Target Archetypes | Research Status |
|---|---|---|---|---|---|
| Adyen NV | Not SEC-registered (Euronext Amsterdam: ADYEN) | 1788707 (ADR admin only) | LOW (SEC) / MEDIUM (Dutch annual reports) | FI Partnership, Issuer Processor, Enterprise Payment Services | Not yet initiated (SEC route closed). Holds own Dutch banking licence (2017) and UK banking licence (2023). Research requires Dutch GAAP annual reports from investors.adyen.com — separate workstream outside SEC scope. |
| Block, Inc. | SEC-registered (NYSE: SQ) | 1512673 | HIGH | Sponsor Bank, Platform/Customer MSA, Embedded Finance | Initial harvest partial (draft 2026-04-25). Sutton Bank and Celtic Bank disclosed in 10-K body text only; no standalone EX-10. Marqeta EX-10.14 (filed by Marqeta) is primary clause-level source for Block's card programs. Celtic Bank loan agreement extracted (public merchant-facing form only). |
| PayPal Holdings, Inc. | SEC-registered (NASDAQ: PYPL) | 1633917 | HIGH | Enterprise Payment Services, FI Partnership, Program Manager | Initial harvest partial (draft 2026-04-25). eBay Operating Agreement (EX-10.1, 2015) partially extracted; indemnification and liability provisions blocked (HTTP 403 — retry required). Bank partnership agreements (Synchrony, Bancorp, Wells Fargo) not filed as PayPal EX-10 exhibits; search Synchrony CIK 1601712. |
| Stripe, Inc. | Not SEC-registered (private) | — | MEDIUM (via counterparties) | Embedded Finance, Platform/Customer MSA, Sponsor Bank | Not yet initiated. No SEC filings. Search counterparty filings (Evolve, Cross River, Mercury-adjacent) for disclosed Stripe structures. Stripe's bank partners likely disclose Stripe-related structures in their own filings. |
| Global Payments Inc. | SEC-registered (NYSE: GPN) | 1123360 | MEDIUM | Issuer Processor, Enterprise Payment Services, FI Partnership | Not yet initiated. Large acquirer. EX-10 material contracts likely to include bank-fintech partnership and enterprise processing agreements. |
| Fiserv, Inc. | SEC-registered (NASDAQ: FISV) | 798354 | MEDIUM | Issuer Processor, Enterprise Payment Services, Bank-Fintech Partnership | Not yet initiated. Acquired First Data (2019) and Clover. EX-10 filings likely to include bank processing agreements. Note: CIK 798354 is also used for Pathward Financial in some legacy references — confirm CIK before querying. |
| FIS (Fidelity National Information Services) | SEC-registered (NYSE: FIS) | 798354 | MEDIUM | Issuer Processor, Enterprise Payment Services, Bank-Fintech Partnership | Not yet initiated. Spun off Worldpay (2023). Material agreement filings may include bank card processing and enterprise payment agreements. Confirm CIK separately from Fiserv. |
| Shift4 Payments, Inc. | SEC-registered (NYSE: FOUR) | 1794669 | MEDIUM | Payment Facilitator, Enterprise MSA, Platform/Customer MSA | Not yet initiated. Integrated payments for hospitality/restaurant. S-1 (2020) and 10-K filings. |
| Toast, Inc. | SEC-registered (NYSE: TOST) | 1793463 | MEDIUM | Payment Facilitator, Platform/Customer MSA, Merchant Acquiring | Not yet initiated. Restaurant-focused payment platform. S-1 (2021) and 10-K filings. |

---

## Category 3 — Cross-Border / Remittance / FX

| Company | SEC Status | CIK | Priority | Target Archetypes | Research Status |
|---|---|---|---|---|---|
| Wise plc | Not SEC-registered (LSE: WISE) | — | LOW (SEC) / MEDIUM (UK FCA/LSE) | FI Partnership, Cross-Border MSB, Correspondent Banking | Not yet initiated. UK-listed. No SEC filing. Holds FCA EMI licence and US state MTL licences. Annual reports and FCA disclosures are the primary source; outside SEC workstream scope. |
| Remitly Global, Inc. | SEC-registered (NASDAQ: RELY) | 1782372 | MEDIUM | FI Partnership, Cross-Border MSB, Enterprise Disbursement | Not yet initiated. S-1 (2021). Bank partnership and disbursement agreements likely in EX-10 exhibits. |
| Western Union Company | SEC-registered (NYSE: WU) | 1348925 | MEDIUM | FI Partnership, Enterprise Payment Services, Agent Network | Not yet initiated. Major MSB. Long SEC filing history. EX-10 exhibits likely to include agent appointment, bank partnership, and settlement agreements. |
| MoneyGram International | Went private 2023 (acquired by Madison Dearborn Partners) | 1273931 | MEDIUM | FI Partnership, Agent Network, Cross-Border MSB | Not yet initiated. SEC filing history available through 2023. Historical 10-K EX-10 exhibits accessible for archival doctrine purposes. |
| Flywire Corporation | SEC-registered (NASDAQ: FLYW) | 1816806 | MEDIUM | Enterprise Payment Services, FI Partnership, International MSA | Not yet initiated. Institutional/enterprise international payments. S-1 (2021) and 10-K filings. |
| OFX Group Limited | Not SEC-registered (ASX: OFX) | — | LOW | FI Partnership, Cross-Border MSB | Not yet initiated. ASX-listed Australian company. No SEC filing. Outside SEC workstream scope. |

---

## Category 4 — Embedded Finance / Platform Payments

| Company | SEC Status | CIK | Priority | Target Archetypes | Research Status |
|---|---|---|---|---|---|
| Shopify Inc. | SEC-registered (NYSE/TSX: SHOP) | 1594805 | MEDIUM | Embedded Finance, Platform/Customer MSA, Sponsor Bank | Not yet initiated. Shopify Balance and Shopify Capital involve banking partnerships. EX-10 filings may disclose bank and payment processor arrangements. Also TSX-listed — SEDAR+ filings available as parallel source. |
| Uber Technologies, Inc. | SEC-registered (NYSE: UBER) | 1543151 | MEDIUM | Embedded Finance, Enterprise Payment Services, FI Partnership | Not yet initiated. Uber Money / Uber Pro Card involve banking and prepaid card structures. S-1 (2019) and 10-K filings. |
| Lyft, Inc. | SEC-registered (NASDAQ: LYFT) | 1759509 | LOW | Embedded Finance, FI Partnership | Not yet initiated. Smaller payment footprint than Uber. S-1 (2019) and 10-K filings. |
| DoorDash, Inc. | SEC-registered (NYSE: DASH) | 1792789 | LOW | Embedded Finance, Enterprise Payment Services | Not yet initiated. DoorDash Pay and driver banking relationships. S-1 (2020) and 10-K filings. |
| Airbnb, Inc. | SEC-registered (NASDAQ: ABNB) | 1559720 | LOW | Enterprise Payment Services, FI Partnership | Not yet initiated. Cross-border payment and disbursement structures. S-1 (2020) and 10-K filings. |

---

## Category 5 — Crypto / Hybrid MSB Models

| Company | SEC Status | CIK | Priority | Target Archetypes | Research Status |
|---|---|---|---|---|---|
| Coinbase Global, Inc. | SEC-registered (NASDAQ: COIN) | 1679788 | MEDIUM | FI Partnership, Cross-Border MSB, Enterprise Payment Services | Not yet initiated. Registered MSB. Bank partnerships for fiat on/off ramps. S-1 (2021 direct listing) and 10-K filings. Material agreements may include bank partnership and custodian agreements. |
| Robinhood Markets, Inc. | SEC-registered (NASDAQ: HOOD) | 1783879 | LOW | FI Partnership, Embedded Finance, Sponsor Bank | Not yet initiated. Robinhood Money (spending account) and Robinhood Gold Card involve banking partnerships. S-1 (2021) and 10-K filings. |

---

## Category 6 — Sponsor Banks / Issuing Banks (Elevated)

Sponsor banks are a distinct research target. Unlike fintech filers who disclose
their bank relationships from the program manager's perspective, sponsor banks
that are SEC-registered disclose these relationships from the bank's perspective.
This provides a different documentary angle on the same commercial structures.

### 6.1 Core U.S. Fintech Sponsor Banks

| Bank | SEC Status | CIK | Priority | Research Status | Notes |
|---|---|---|---|---|---|
| Sutton Bank | Not SEC-registered (private Ohio-chartered bank) | — | HIGH (via counterparties) | Partial — disclosed in Marqeta EX-10.21 and Block 10-K body (initial harvest 2026-04-25). | Primary issuing bank for Marqeta programs (Block Cash App Card, Square Debit Card). No standalone EX-10 from Sutton; terms accessible only through counterparty filings. |
| The Bancorp, Inc. | SEC-registered (NASDAQ: TBBK) | 1295401 | HIGH | Not yet initiated. | Primary fintech prepaid/debit sponsor bank (Chime, etc.). 10-K filings disclose program manager relationships from the bank's perspective. Priority 1 in queue. |
| Pathward Financial, Inc. (f/k/a Meta Financial Group; operating subsidiary MetaBank) | SEC-registered (NASDAQ: CASH) | 798354 | HIGH | Not yet initiated. | Rebranded from Meta Financial Group in 2022; MetaBank was the operating bank subsidiary. Now trading as Pathward Financial. Major prepaid card sponsor bank and BaaS provider. Long SEC filing history under both names. EX-10 filings may disclose program manager agreements from bank's perspective. Priority 2 in queue. |
| Cross River Bank | Not SEC-registered (private NJ-chartered bank) | — | MEDIUM (via counterparties) | Not yet initiated. | Major fintech sponsor bank (Affirm, Upgrade, Coinbase, others). FDIC consent order (2023) for fair lending — enforcement record relevant to WS-B. Search counterparty SEC filings (Affirm AFRM, Upgrade via any SEC filings) for Cross River relationship disclosures. |
| Evolve Bank & Trust | Not SEC-registered (private Arkansas state bank) | — | HIGH (via counterparties / WS-B) | Not yet initiated. | Major fintech BaaS bank. Federal Reserve consent order (June 2024) for AML/BSA failures — critical WS-B source. Synapse insolvency (2024) involvement provides post-failure architecture visibility. Search Stripe, Mercury, and Synapse-adjacent counterparty filings. WS-B priority target. |

### 6.2 Secondary / Emerging Sponsor Banks

| Bank | SEC Status | CIK | Priority | Research Status | Notes |
|---|---|---|---|---|---|
| Lincoln Savings Bank | Not SEC-registered (private Iowa state bank) | — | LOW (via counterparties) | Not yet initiated. | Appears as sponsor bank in some fintech structures. Track via counterparty disclosures. |
| Blue Ridge Bank | Was SEC-registered (NASDAQ: BRBS) through 2024; acquired by National Bankshares October 2024 | 835324 | MEDIUM (historical) | Not yet initiated. | Filed 10-K through 2023. Had significant fintech BaaS partnerships (Unit, Synctera). Fed consent order re: BSA/AML. Historical SEC filings accessible for doctrine. |
| First Electronic Bank | Not SEC-registered (Utah ILC; subsidiary of CardWorks) | — | LOW (via counterparties) | Not yet initiated. | Utah ILC. Issues prepaid and credit cards. Track via counterparty disclosures. |

---

## Category 7 — Canadian Major Banks with US Presence (Elevated — Added v0.3)

These institutions are relevant as (a) correspondent banking counterparties in
MSB-to-bank commercial agreements, (b) cross-border payment rail providers for
Canada-US structures, and (c) increasingly as fintech program sponsors in
Canada-US commercial arrangements. All four file Form 40-F with the SEC as
foreign private issuers, giving access to their Annual Information Forms and
material agreement disclosures.

### 7.1 Core Targets

| Bank | SEC Filing | CIK | US Entity | Priority | Research Status | Notes |
|---|---|---|---|---|---|---|
| Toronto-Dominion Bank (TD) | Form 40-F (foreign private issuer) | 947263 | TD Bank, N.A. (US chartered bank; largest US retail banking footprint of any Canadian bank) | HIGH | Not yet initiated. | TD Bank, N.A. is a major US retail bank and payment services provider. Fintech partnerships and payment processing relationships likely disclosed in 40-F and US subsidiary SEC filings. TD's US operations include former Commerce Bank and South Financial Group franchises. |
| Bank of Montreal (BMO) | Form 40-F (foreign private issuer) | 927971 | BMO Bank N.A. (formerly Bank of the West; acquired 2023) | HIGH | Not yet initiated. | Significant US retail banking presence post-Bank of the West acquisition. BMO Bank N.A. is an OCC-chartered national bank. Cross-border payment and commercial banking structures likely in 40-F. |
| Royal Bank of Canada (RBC) | Form 40-F (foreign private issuer) | 1000177 | City National Bank (California; acquired 2015); RBC Capital Markets LLC | MEDIUM | Not yet initiated. | City National Bank is RBC's primary US retail banking entity. RBC's US investment banking and capital markets operations may have disclosed commercial payment structures. |
| Bank of Nova Scotia (Scotiabank) | Form 40-F (foreign private issuer) | 9631 | Scotia Capital (USA) Inc.; US branch operations | MEDIUM | Not yet initiated. | Smaller US retail footprint vs. TD/BMO. US presence primarily through capital markets and correspondent banking. Cross-border Canada-US payment corridors relevant to MSB clients. |

### 7.2 Research Approach for Canadian Banks

- Primary source: Form 40-F annual filings at SEC EDGAR (these are the Canadian equivalent of a Form 20-F; they incorporate the Canadian Annual Information Form by reference)
- Material agreements: Filed as exhibits under Item 9 of Form 40-F and Exhibit 1 (AIF)
- US subsidiary filings: TD Bank, N.A. and BMO Bank N.A. may file separately as national banks; FDIC call reports and OCC filings are parallel sources
- Relevance filter: Focus on payment services, correspondent banking, fintech partnership, and cross-border payment rail agreements disclosed in these filings

---

## Research Status Summary

| Company | Status | Source | Output Location |
|---|---|---|---|
| Marqeta | Initial harvest complete (draft, not ML1-approved) | EX-10.21, EX-10.14 | WS_A/RESEARCH_2026-04-25_INITIAL_HARVEST.md |
| Block | Partial (body text only for Sutton Bank; Celtic Bank loan form extracted) | 10-K FY2023 body; public loan agreement | WS_A/RESEARCH_2026-04-25_INITIAL_HARVEST.md |
| PayPal | Partial (eBay Operating Agreement; bank partnership agreements pending; indemnity/liability blocked) | 8-K EX-10.1 (2015) | WS_A/RESEARCH_2026-04-25_INITIAL_HARVEST.md |
| Adyen | No SEC filing (ADR only; Dutch annual reports required) | — | WS_A/RESEARCH_2026-04-25_INITIAL_HARVEST.md (noted) |
| All others | Not yet initiated | — | — |

---

## Priority Queue for Next Research Engagements

Sequencing based on disclosure quality, archetype coverage gaps, and Canada-US relevance:

**Tier 1 — Immediate priority (sponsor bank angle, fill Program Manager archetype from bank side)**
1. The Bancorp, Inc. (TBBK, CIK 1359190) — sponsor bank SEC filer; bank-side view of program manager agreements
2. Pathward Financial / MetaBank (CASH, CIK 798354) — same rationale; long prepaid card history
3. Green Dot Corporation (GDOT, CIK 1309108) — dual sponsor bank and program manager; two-sided disclosure

**Tier 2 — Complete existing partial research**
4. PayPal / eBay Operating Agreement — retry indemnification and liability extraction (HTTP 403 in initial session)
5. Synchrony Financial (CIK 1601712) — discloses PayPal credit program from Synchrony's perspective

**Tier 3 — Cross-border and Canada-US corridor**
6. TD Bank (Form 40-F, CIK 947484) — largest Canadian bank US retail footprint; fintech partnerships
7. BMO (Form 40-F, CIK 927971) — post-Bank of the West acquisition; US commercial banking

**Tier 4 — Remittance / cross-border MSB archetypes**
8. Western Union (WU, CIK 1348925) — agent network and bank partnership agreements
9. Remitly Global (RELY, CIK 1782372) — bank disbursement partnership agreements
10. MoneyGram (historical filings, CIK 1273931)

**Tier 5 — Embedded finance and platform payments**
11. Shopify (SHOP, CIK 1594805) — Shopify Balance / Capital bank partnerships
12. Coinbase (COIN, CIK 1679788) — fiat on/off ramp bank partnership agreements

**Tier 6 — Merchant acquiring / processing (enterprise scale)**
13. Global Payments (GPN, CIK 1123360)
14. Fiserv (FISV) — confirm CIK
15. Shift4 (FOUR, CIK 1794669)
16. Toast (TOST, CIK 1793463)

---

## Version History

| Version | Date | Change |
|---|---|---|
| 0.1 | 2026-04-25 | Initial universe defined in agent spec §4.1 and §4.2 |
| 0.2 | 2026-04-25 | Expanded to 6 categories; sponsor banks elevated to standalone category; 40+ targets; research status and priority queue added |
| 0.3 | 2026-04-28 | Added Category 7 — Canadian Major Banks with US Presence (TD, BMO, RBC, Scotiabank); elevated Pathward Financial note to include MetaBank alias; added research status column to all tables; expanded priority queue to Tier 1–6 structure |
