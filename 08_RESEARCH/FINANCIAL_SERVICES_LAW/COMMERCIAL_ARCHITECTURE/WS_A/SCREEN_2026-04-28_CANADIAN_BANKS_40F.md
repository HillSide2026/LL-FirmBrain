---
id: ws-a-screen-canadian-banks-40f-2026-04-28
title: WS-A Screen — Canadian Banks 40-F (TD, BMO)
workstream: WS-A
status: draft
created_date: 2026-04-28
ml1_approval_required: NO
output_label: Derived from disclosed agreement (SEC)
targets: [Toronto-Dominion Bank, Bank of Montreal]
---

# WS-A Screen — Canadian Banks 40-F (TD, BMO)

**Research Date:** 2026-04-28
**Output Label:** Derived from disclosed agreement (SEC)
**Status:** Screen report only — not a full extraction. ML1 approval not required for screens.

---

## CIK Correction

The Company Universe v0.3 listed TD CIK as 947484. That CIK resolves to Arch Capital Group Ltd. (insurer), not Toronto-Dominion Bank. **TD's correct EDGAR CIK is 947263.** The universe file must be corrected before any TD EDGAR queries are run.

---

## BANK: Toronto-Dominion Bank (TD Bank Group)

**40-F CIK:** 947263 (corrected from 947484 in universe v0.3)
**Most recent 40-F:** December 5, 2024 (FY ended October 31, 2024), accession 0001562762-24-000281. FY2025 filing confirmed December 3, 2025.
**Exhibit list summary:** Standard foreign private issuer wrapper. Exhibits: 99.1 (AIF), 99.2 (MD&A), 99.3 (Financial Statements), Exhibit 23 (Ernst & Young auditor consent), Exhibits 31.1/31.2 and 32 (SOX certifications). No EX-10 exhibits in any filing year reviewed.
**Payment services agreement exhibits found:** NO
**Disclosure method:** Body-text / AIF only. The AIF discloses the Schwab Insured Deposit Account (IDA) Agreement (amended May 2023, extended to July 1, 2034) as a material contract — a deposit sweep arrangement, not a card or payments program. TD Retail Card Services operates private label and co-brand card programs (Target, Nordstrom, Zale, etc.) but those agreements are filed as EX-10 exhibits by the merchant counterparties in their own 10-K filings, not by TD in its 40-F.
**Law Insider result:** Found — but sourced from merchant-side filings only. TD Retail Card Services corporate private label credit card program agreements appear at lawinsider.com. No agreement filed by TD as issuing bank identified.
**US subsidiary filing status:** TD Bank, N.A. is OCC-chartered and does not file 10-K with the SEC. FDIC resolution plan public sections available but no payment agreement exhibits.

**Recommended next step:**
- Skip 40-F extraction for payment services agreements.
- Redirect to: (a) **Target Corporation 10-K (CIK 27419)** — TD card program amendment confirmed filed as Exhibit 10.jj through at least February 2025; this gives the program agreement from the merchant counterparty's side; (b) TD AIF body text for Schwab IDA agreement summary; (c) SEDAR+ for fuller Canadian AIF material contracts text.

---

## BANK: Bank of Montreal (BMO Financial Group)

**40-F CIK:** 927971 (confirmed)
**Most recent 40-F:** December 4, 2025 (FY ended October 31, 2025), accession 0001193125-25-307982. 40-F/A amendment filed subsequently to correct MD&A date.
**Exhibit list summary:** Same foreign private issuer pattern. Exhibits 99.1–99.6 (AIF, MD&A, financials, certifications). No EX-10 exhibits.
**Payment services agreement exhibits found:** NO
**Disclosure method:** Body-text / press release only. BMO has multiple disclosed fintech/payments partnerships — Extend (virtual cards, December 2022), Elavon (payment solutions platform for US clients, March 2024), DailyPay (earned wage access), Mastercard (remittance expansion, 2025) — but none identified as SEC exhibit-level disclosures. All found in press releases only.
**Law Insider result:** Not found as standalone payment services agreement. BMO appears in Law Insider as a credit facility counterparty only (BMO Harris Bank credit lines). No card program, merchant acquiring, or payment services agreement filed by BMO as a party identified.
**US subsidiary filing status:** BMO Bank N.A. (formerly Bank of the West, acquired 2023) is OCC-chartered and does not file 10-K with the SEC.

**Recommended next step:**
- Skip 40-F extraction for payment services agreements.
- Redirect to: (a) **BMO AIF body text** — fetch https://www.bmo.com/ir/archive/en/bmo_AIF2024.pdf and review material contracts section for Elavon and Extend disclosures; (b) **US Bancorp (CIK 36104)** — Elavon is a US Bancorp subsidiary; the BMO-Elavon payment platform arrangement may be disclosed in US Bancorp's own SEC filings; (c) SEDAR+ for Canadian AIF.

---

## Overall Conclusion

Neither TD nor BMO files standalone payment services agreement exhibits (EX-10 or equivalent) in their Form 40-F filings. The 40-F structure for Canadian bank foreign private issuers incorporates all material disclosure by reference to the AIF (filed as Exhibit 99.1). Payment services partnerships are disclosed at press-release and AIF body-text level only.

**Higher-yield extraction routes:**
1. Merchant counterparty 10-K filings on EDGAR (Target Corporation for TD card programs)
2. BMO and TD AIFs directly (for program-level descriptions)
3. US Bancorp (CIK 36104) for the BMO-Elavon arrangement

**Universe correction required:** Update COMPANY_UNIVERSE TD CIK from 947484 to 947263.

---

## Change Log

- 2026-04-28 — Screen completed. No standalone payment services agreement exhibits found in either 40-F. Redirected to merchant counterparty filings and AIF body text. TD CIK error identified and flagged for correction.
