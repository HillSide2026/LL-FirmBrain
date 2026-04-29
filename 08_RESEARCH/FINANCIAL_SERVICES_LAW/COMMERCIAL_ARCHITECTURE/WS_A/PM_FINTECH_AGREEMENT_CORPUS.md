---
id: ws-a-pm-fintech-agreement-corpus
title: WS-A — PM ↔ Fintech / Product Partner Agreement Corpus
workstream: WS-A
status: draft
created_date: 2026-04-28
last_updated: 2026-04-28
ml1_approval_required: NO
output_label: Derived from disclosed agreement (SEC)
---

# WS-A — PM ↔ Fintech / Product Partner Agreement Corpus

**Purpose:** Index of all known publicly disclosed Program Manager ↔ Fintech / Product Partner agreements, their SEC filing sources, access status, and retrieval instructions.

**Layer:** This is one layer below the Bank ↔ PM agreements harvested in Tier 1 (Bancorp, Pathward, Green Dot). The stack:

```
Card Network
    ↕
Issuing Bank          ← covered in RESEARCH_2026-04-28_TIER1_SPONSOR_BANKS.md
    ↕
Program Manager       ← THIS DOCUMENT (PM ↔ Fintech product partner agreements)
    ↕
Fintech / Product Partner
    ↕
End Customer
```

---

## Access Problem

All SEC.gov Archives exhibit URLs return HTTP 403 for automated access (non-browser user agents are blocked). Law Insider refuses full text reproduction. Justia mirrors also 403. The agreements exist and URLs are confirmed valid — they require a browser or a paid API to retrieve.

**Three retrieval options:**

| Option | Cost | Speed | How |
|---|---|---|---|
| Manual browser download | Free | Immediate | Open URL in browser → Save Page As HTML → drop into `WS_A/RAW_AGREEMENTS/` → I read and extract |
| sec-api.io | ~$50/mo | Fast | Programmatic access to EDGAR exhibit text without 403 block; unlocks entire corpus |
| EDGAR full-text search UI | Free | Manual | `https://efts.sec.gov/LATEST/search-index` in browser; search `"program management services agreement" "processing services"` filtered to S-1; returns inline exhibit text |

**Recommended immediate path:** Manual download of the 3-4 highest-priority agreements (Marqeta/Block MSA + one or two unknown-CIK agreements below). Once local, full clause extraction is straightforward.

---

## Known Agreements — Confirmed in SEC Filings

### Group A: Marqeta as Program Manager (PM filing its own customer agreements)

| # | Agreement | Filing | Exhibit | URL | Access |
|---|---|---|---|---|---|
| A1 | Marqeta / Block (Square) Master Services Agreement — original (2016, as amended) | Marqeta S-1/A, CIK 1522540 | EX-10.14 | https://www.sec.gov/Archives/edgar/data/1522540/000119312521177861/d64065dex1014.htm | Manual download required |
| A2 | Marqeta / Block — Amendment No. 17 | Marqeta 8-K/A, CIK 1522540 | EX-10.1 | https://www.sec.gov/Archives/edgar/data/1522540/000152254023000027/exhibit101-8xka81123.htm | Manual download required |
| A3 | Marqeta / Block — Amendment No. 18 | Marqeta 10-Q Q3 2023, CIK 1522540 | EX-10.1 | https://www.sec.gov/Archives/edgar/data/1522540/000162828023037578/exhibit101-q32023.htm | Manual download required |
| A4 | Marqeta / Block — Amendment No. 21 (or later) | Marqeta 10-K FY2024, CIK 1522540 | EX-10.19 | https://www.sec.gov/Archives/edgar/data/1522540/000162828025008232/exhibit1019-202410xk.htm | Manual download required |
| A5 | Marqeta / [customer — Q1 2023 amendment] | Marqeta 10-Q Q1 2023, CIK 1522540 | EX-10.4 | https://www.sec.gov/Archives/edgar/data/1522540/000152254023000024/exhibit104q12023.htm | Manual download required |

**Note on Block/Square MSA:** This is the richest known PM ↔ Fintech agreement in public SEC filings. Marqeta filed the original as EX-10.14 in its S-1/A (June 2021); 20+ amendments have been filed in subsequent 10-K and 10-Q filings through 2024. The original agreement text was partially extracted in the initial harvest (RESEARCH_2026-04-25_INITIAL_HARVEST.md) from a Law Insider mirror, but full text including redactions was not retrieved.

---

### Group B: Fintechs Disclosing Their PM Agreement in Their Own IPO Filing

These are fintech product partners who disclosed their Marqeta or other PM agreement as a material contract when filing their own S-1 or going public.

| # | CIK | Company (unconfirmed) | Filing | Exhibit | URL | Access | Notes |
|---|---|---|---|---|---|---|---|
| B1 | 1846084 | Unknown — filed S-1 December 2021 | S-1, CIK 1846084 | EX-10.26 | https://www.sec.gov/Archives/edgar/data/1846084/000119312521355341/d140617dex1026.htm | Manual download required | Filed December 2021; agreement is a Program Management Services Agreement type; company identity not confirmed via automated search |
| B2 | 1803112 | Unknown — filed S-1 2021 | S-1, CIK 1803112 | EX-10.10 | https://www.sec.gov/Archives/edgar/data/1803112/000095012321005660/filename4.htm | Manual download required | Filed 2021; company identity not confirmed |

**Priority:** B1 (CIK 1846084) is the highest-value unknown. The exhibit is labeled EX-10.26 in a December 2021 S-1 — this timing coincides with the neobank/BaaS IPO wave. Once downloaded, the agreement parties will be visible on the first page.

---

### Group C: Fintech Product Partners — Narrative Disclosure Only (No Standalone Exhibit)

These companies disclose their Marqeta relationship in 10-K body text but have not filed the agreement as a standalone exhibit. Clause-level extraction is not possible without the underlying agreement.

| Company | CIK | Disclosure method | Notes |
|---|---|---|---|
| DoorDash, Inc. | 1792789 | 10-K body text only | Marqeta named as card program processor in DoorDash 10-K risk factors |
| Uber Technologies, Inc. | 1543151 | 10-K body text only | Marqeta partnership disclosed; Uber Eats card program |
| Instacart (Maplebear Inc.) | 1834585 | TBC — S-1 filed 2023; may have standalone exhibit | Instacart was a significant Marqeta customer (disclosed in Marqeta 10-K as material revenue concentration). Check Instacart S-1 EX-10 exhibits. |

**Recommended next check:** Instacart S-1 (CIK 1834585, filed 2023) — search for EX-10 exhibits related to Marqeta or card program management. This is the most likely source for a second full-text PM ↔ Fintech agreement.

---

### Group D: Other PM ↔ Fintech Agreements — To Be Identified

The following companies are SEC-registered program managers or payment platforms that have disclosed customer-facing program management agreements. Their S-1 filings may contain additional PM ↔ Fintech agreements not yet identified.

| Company | CIK | Search priority | Notes |
|---|---|---|---|
| Toast, Inc. | 1793463 | MEDIUM | Restaurant payment platform; S-1 (2021). Toast acts as PM for restaurant operators — merchant-facing program agreements may be filed as EX-10 material contracts. |
| Shift4 Payments | 1794669 | MEDIUM | Integrated payments; S-1 (2020). Similar structure to Toast. |
| Shopify Inc. | 1594805 | MEDIUM | Shopify Balance / Shopify Capital involve PM-style relationships with banking partners. |
| Coinbase Global | 1679788 | LOW | Coinbase Card program with Marqeta/Sutton Bank; may be in Coinbase S-1 (direct listing, 2021). |

---

## Retrieval Instructions (Manual Download Path)

1. Open each URL in a browser (Chrome/Safari)
2. Verify the page loads (should show agreement text)
3. Save as: File → Save Page As → Web Page, Complete (or HTML Only)
4. Save to: `/Users/matthewlevine/Repos/ll-secondbrain_fresh/08_RESEARCH/FINANCIAL_SERVICES_LAW/COMMERCIAL_ARCHITECTURE/WS_A/RAW_AGREEMENTS/`
5. Name the file: `[CIK]_[company]_[agreement-type]_[year].html` e.g. `1522540_marqeta_block_msa_2021.html`
6. Once saved locally, full clause extraction can be run directly

**Priority download order:**
1. A1 — Marqeta/Block MSA original (EX-10.14, 2021) — richest known PM ↔ Fintech agreement
2. B1 — CIK 1846084 EX-10.26 — identify the company and extract full agreement
3. A4 — Marqeta/Block Amendment No. 21 (most current version)
4. B2 — CIK 1803112 EX-10.10 — identify and extract

---

## Related Files in This Research Corpus

| File | Contents |
|---|---|
| [COMPANY_UNIVERSE_v0.3.md](COMPANY_UNIVERSE_v0.3.md) | Full target list, 7 categories, 40+ companies, priority queue |
| [RESEARCH_2026-04-25_INITIAL_HARVEST.md](RESEARCH_2026-04-25_INITIAL_HARVEST.md) | Initial harvest: Marqeta, Block, PayPal, Adyen — partial clause extraction |
| [RESEARCH_2026-04-28_TIER1_SPONSOR_BANKS.md](RESEARCH_2026-04-28_TIER1_SPONSOR_BANKS.md) | Tier 1: Bancorp, Pathward/MetaBank, Green Dot — Bank ↔ PM agreements, 5-dimension pass |
| [SCREEN_2026-04-28_CANADIAN_BANKS_40F.md](SCREEN_2026-04-28_CANADIAN_BANKS_40F.md) | Canadian banks 40-F screen: TD and BMO — no standalone payment exhibits found |
| `RAW_AGREEMENTS/` | Local copies of SEC exhibit HTML files (to be populated via manual download) |

---

## Change Log

- 2026-04-28 — Created. Identified access problem (SEC 403 on all automated access). Mapped known PM ↔ Fintech agreement corpus: 5 Marqeta/Block agreements (Group A), 2 unknown-CIK agreements (Group B), 3 narrative-only disclosures (Group C), 4 candidates to search (Group D). Manual download path documented.
