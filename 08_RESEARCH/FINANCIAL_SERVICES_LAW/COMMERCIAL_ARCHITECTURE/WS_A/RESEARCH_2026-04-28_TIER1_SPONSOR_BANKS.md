---
id: ws-a-tier1-sponsor-banks-2026-04-28
title: WS-A Tier 1 Harvest — Bancorp, Pathward/MetaBank, Green Dot
workstream: WS-A
status: draft
created_date: 2026-04-28
ml1_approval_required: YES
output_label: Derived from disclosed agreement (SEC)
targets: [The Bancorp, Pathward Financial, Green Dot]
---

# WS-A Tier 1 Harvest: Sponsor Banks — Bancorp, Pathward/MetaBank, Green Dot

**Research Date:** 2026-04-28
**Output Label:** Derived from disclosed agreement (SEC)
**Status:** Draft — not authoritative until ML1-approved
**Extraction scope:** 5-dimension first pass (parties/roles, compliance allocation, indemnification, liability cap, termination triggers)

---

## Research Method Notes

Law Insider (lawinsider.com) and Justia Contracts (contracts.justia.com) used as primary sources per credit-efficient protocol. SEC EDGAR used for filing index confirmation. All sponsor bank agreements found via counterparty filings — none of the three companies filed their program management agreements as standalone EX-10 exhibits in their own annual reports. This is consistent with the pattern observed in the initial harvest (Marqeta filed the exhibit; Block disclosed body text only).

Note on Bancorp CIK: The company universe listed CIK 1359190. Confirmed correct CIK is **1295401**. Universe to be corrected.

---

## Company 1: The Bancorp, Inc. (NASDAQ: TBBK)

**CIK:** 1295401 (note: universe v0.3 lists 1359190 — to be corrected)
**Filing screen result:** The Bancorp does not file standalone program management agreements as EX-10 exhibits in its own 10-K. Disclosure is body-text only in its own annual reports. Agreements appear via counterparty filings. One agreement located: Prepaid Card Issuer & Program Management Agreement filed by FiCentive/PaySign (CIK 1088034) in 2015, naming The Bancorp Bank as issuing bank. A Card Issuing Addendum with Block/Cash App (July 2025) filed via 8-K but terms confidential.

---

### AGREEMENT 1A

```
Filing: PaySign, Inc. (f/k/a 3PEA International, Inc.) / 10-K EX-10.26 / CIK 1088034 / Filed 2015-02-XX
Agreement title: Prepaid Card Issuer & Program Management Agreement
Parties: The Bancorp Bank (Issuing Bank) / FiCentive entity (Program Manager)
Archetype: Program Manager
Output label: Derived from disclosed agreement (SEC)
```

**DIMENSION 1 — Parties and Role Labels**

Party A: The Bancorp Bank — labeled "Bank" / "Issuing Bank." Functional role: chartered bank, BIN sponsor, card issuer, regulatory status holder.
Party B: FiCentive entity — labeled "Program Manager." Functional role: card program management, cardholder-facing operations.

Source: https://www.sec.gov/Archives/edgar/data/1088034/000135448815001406/pyds_ex1026.htm

**DIMENSION 2 — Compliance Responsibility Allocation**

AML/KYC performer: Program Manager — CIP/AML delegation to PM implied by structure.
AML/KYC responsible party (regulatory exposure): Bank — liable for its own Legal Requirements failures.
BSA/AML program ownership: Program Manager retains full responsibility for Processor acts. Bank bears ultimate regulatory exposure as charter holder.

Source: Agreement body; counterparty 10-K disclosure.

**DIMENSION 3 — Indemnification**

Direction: Mutual.
Scope: Bank indemnifies PM for Bank's own compliance failures. PM indemnifies Bank for Processor acts.
Carve-outs: Not disclosed beyond basic mutual structure.

Source: Agreement body (EX-10.26).

**DIMENSION 4 — Liability Cap Structure**

Cap structure: Not disclosed (confidential treatment).
Consequential loss exclusion: Not disclosed.
Carve-outs from cap: Not disclosed.

Source: Not available in filed exhibit.

**DIMENSION 5 — Termination Triggers**

Convenience termination: Either party may terminate "for any reason" at term boundaries.
Term structure: 4-year initial term with 2-year auto-renewals.
Regulatory trigger: Not separately disclosed.
De-risking / bank exit: Not specifically enumerated.
Material breach cure: Not disclosed.

Source: Agreement body (EX-10.26).

---

## Company 2: Pathward Financial, Inc. f/k/a Meta Financial Group / MetaBank (NASDAQ: CASH)

**CIK:** 798354 (confirmed)
**Filing screen result:** Pathward/MetaBank is named as bank party in multiple standalone EX-10 exhibits filed by fintech counterparties. Two high-quality agreements located with full clause text: (1) NetSpend Program Management Agreement (2010, filed by NetSpend CIK 1496623); (2) H&R Block/EFS Program Management Agreement (2020, filed by H&R Block CIK 12659). These are the richest sponsor-bank-side disclosures found in the harvest to date.

---

### AGREEMENT 2A

```
Filing: NetSpend Corporation / S-1 EX-10.20 / CIK 1496623 / Filed 2010
Agreement title: Second Amended and Restated Card Program Management Agreement
Parties: MetaBank dba Meta Payment Systems (Bank) / NetSpend Corporation (Company / Program Manager)
Archetype: Program Manager
Output label: Derived from disclosed agreement (SEC)
```

**DIMENSION 1 — Parties and Role Labels**

Party A: MetaBank dba Meta Payment Systems — labeled "Bank." Functional role: Utah-chartered bank, BIN sponsor, card issuer, BSA/AML regulatory holder, OFAC screener.
Party B: NetSpend Corporation — labeled "Company" / "Program Manager." Functional role: card program management, distribution, cardholder-facing operations, BSA agent (by express delegation from Bank).

Source: https://www.sec.gov/Archives/edgar/data/1496623/000104746910006467/a2199373zex-10_20.htm

**DIMENSION 2 — Compliance Responsibility Allocation**

AML/KYC performer: NetSpend — Bank formally appoints NetSpend as BSA agent and authorized delegate for state money transmitter compliance and Bank Secrecy Act. This is express statutory delegation, not just a service arrangement.
AML/KYC responsible party (regulatory exposure): Bank — retains ultimate regulatory exposure as charter holder. Bank screens cardholders for OFAC directly.
BSA/AML program ownership: Shared by express delegation. Bank owns CIP; NetSpend is BSA agent. Bank retains direction right to suspend distribution channels on regulatory, reputational, or safety grounds.

Source: Agreement body, BSA agent delegation provisions.

**DIMENSION 3 — Indemnification**

Direction: Mutual (Section 14.1).
Scope: Standard mutual indemnification for breach, negligence, willful misconduct, fraud, violation of applicable law.
Carve-outs from consequential damages exclusion: Three named carve-outs — (1) indemnified claims, (2) confidentiality/security breaches, (3) gross negligence/willful misconduct/fraud.

Source: Agreement Section 14.1 and consequential damages exclusion.

**DIMENSION 4 — Liability Cap Structure**

Cap structure: Dollar cap not disclosed (confidential treatment / redaction).
Consequential loss exclusion: Confirmed — consequential, indirect, punitive damages excluded.
Carve-outs from cap: Three carve-outs confirmed (same as indemnification carve-outs above).

Source: Agreement liability limitation provisions.

**DIMENSION 5 — Termination Triggers**

Convenience termination: 120-day notice for non-renewal of annual auto-renewals.
Term structure: 5-year initial term; annual auto-renewals thereafter.
Regulatory trigger: Bank holds unilateral right to suspend distribution channels on regulatory/reputational/safety grounds (de-risking short of full termination). Specific regulatory change termination not separately enumerated.
De-risking / bank exit: Yes — bank suspension right on regulatory/reputational/safety grounds.
Material breach cure: Not separately disclosed in excerpt.

Source: Agreement term and suspension provisions.

---

### AGREEMENT 2B

```
Filing: H&R Block, Inc. / 10-K EX-10.1 / CIK 12659 / Filed 2020; First Amendment filed 2021
Agreement title: Program Management Agreement
Parties: MetaBank N.A. (Bank) / Emerald Financial Services LLC (EFS — H&R Block subsidiary)
Archetype: Program Manager (tax-season prepaid card program — Emerald Card)
Output label: Derived from disclosed agreement (SEC)
```

**DIMENSION 1 — Parties and Role Labels**

Party A: MetaBank N.A. — labeled "Bank." Functional role: national bank charter, card issuer, BIN sponsor, BSA/AML policy owner, regulatory status holder.
Party B: Emerald Financial Services LLC (H&R Block subsidiary) — labeled "EFS" / "Program Manager." Functional role: card program management, cardholder-facing operations, tax refund disbursement mechanism.

Source: https://www.sec.gov/Archives/edgar/data/12659/000157484220000033/hrb20200731exhibit101.htm

**DIMENSION 2 — Compliance Responsibility Allocation**

AML/KYC performer: EFS — performs customer-facing compliance operations per Bank-provided written policies.
AML/KYC responsible party (regulatory exposure): Bank — owns CIP model and BSA/AML requirements; provides written policies to EFS; retains regulatory exposure as national bank charter holder.
BSA/AML program ownership: Bank provides written policies; EFS implements. Bank may require suspension of any financial product if regulatory directive received. Bank must use commercially reasonable efforts before suspending during Tax Season (seasonal operational constraint explicitly carved out).

Source: Agreement compliance provisions and suspension mechanics.

**DIMENSION 3 — Indemnification**

Direction: Mutual.
Scope: Same structure as Agreement 2A — mutual indemnification for breach, negligence, willful misconduct, fraud, violation of applicable law.
Carve-outs: Same three carve-outs as Agreement 2A: indemnified claims, confidentiality/security breaches, gross negligence/willful misconduct/fraud.

Source: Agreement indemnification provisions.

**DIMENSION 4 — Liability Cap Structure**

Cap structure: Dollar cap not disclosed.
Consequential loss exclusion: Confirmed — same architecture as Agreement 2A.
Carve-outs from cap: Same three carve-outs confirmed.

Source: Agreement liability limitation provisions.

**DIMENSION 5 — Termination Triggers**

Convenience termination: Not separately stated; governed by term structure.
Term structure: Not separately disclosed in excerpt.
Regulatory trigger — **Durbin Regulatory Event (notable):** Dedicated termination trigger for Bank exceeding $10B in assets, which would cause loss of the small-issuer exemption under the Durbin Amendment (Dodd-Frank Act interchange fee regulations). Named, dedicated exit right with 30-day notice. This is a bespoke regulatory trigger specific to MetaBank's regulatory economics — significant doctrine point.
De-risking / bank exit: Bank holds unilateral suspension right on regulatory/reputational/safety grounds (same structure as Agreement 2A). No commercial reasonableness obligation outside Tax Season.
Material breach cure: 30-day cure period confirmed.

Source: Agreement termination provisions; First Amendment (2021) at https://www.sec.gov/Archives/edgar/data/12659/000160529721000020/exhibit101firstamendmentto.htm

---

## Company 3: Green Dot Corporation (NYSE: GDOT)

**CIK:** 1309108 (confirmed)
**Filing screen result:** Green Dot files standalone program agreements as EX-10 exhibits in its own 10-K. Primary agreement: 2020 Amended and Restated Walmart MoneyCard Program Agreement (EX-10.6 to FY2019 10-K). Green Dot is uniquely vertically integrated: GDC = program manager; Green Dot Bank = issuing bank; both are parties on the same side of the agreement. This produces a different disclosure structure from the MetaBank/NetSpend pattern where bank and program manager are adverse parties.

**WS-B flag — Federal Reserve consent order (July 2024):** The Federal Reserve issued a consent order against Green Dot Corporation in July 2024 imposing a $44M civil money penalty and requiring a $50M remediation fund. Identified significant BSA/AML deficiencies including inadequate transaction monitoring and customer due diligence. This is a high-value WS-B target: the consent order surfaces what Green Dot's compliance architecture failed to provide, which translates directly into implied contractual requirements. Flag for Workstream B initiation.

---

### AGREEMENT 3A

```
Filing: Green Dot Corporation / 10-K EX-10.6 / CIK 1309108 / Filed 2020 (FY2019)
Agreement title: Second Amended and Restated Walmart MoneyCard Program Agreement (2020)
Parties: Walmart Inc. (Retailer) / Green Dot Corporation / GDC (Program Manager) / Green Dot Bank (Issuing Bank — Utah chartered, Federal Reserve member, wholly-owned GDC subsidiary)
Archetype: Program Manager (vertically integrated — program manager and issuing bank are affiliates on the same side)
Output label: Derived from disclosed agreement (SEC)
```

**DIMENSION 1 — Parties and Role Labels**

Party A: Walmart Inc. — labeled "Retailer." Functional role: distribution channel, point-of-sale card activation, co-brand program sponsor, data provider.
Party B: Green Dot Corporation / GDC — labeled "Program Manager." Functional role: overall program management, regulatory and legal compliance program design and delivery.
Party C: Green Dot Bank — labeled "Issuing Bank." Functional role: Utah-chartered bank, card issuer, FDIC-insured account holder, Federal Reserve member, holds issuing regulatory relationship.
Note on structure: GDC and Green Dot Bank are affiliates (Green Dot Bank is wholly owned by GDC). Their joint and several obligations are on the same side of the agreement, facing Walmart. This is structurally different from the MetaBank/NetSpend pattern where bank and program manager are separate, unaffiliated parties.

Source: https://www.sec.gov/Archives/edgar/data/1386278/000138627820000020/exb106-2020amendedandr.htm; Justia: https://contracts.justia.com/companies/green-dot-corporation-596/contract/91012/

**DIMENSION 2 — Compliance Responsibility Allocation**

AML/KYC performer: GDC and Green Dot Bank — jointly bear all program compliance responsibility.
AML/KYC responsible party (regulatory exposure): GDC and Green Dot Bank jointly — GDC designs and provides the regulatory and legal compliance program; Green Dot Bank holds the bank charter and regulatory relationship.
BSA/AML program ownership: GDC/Bank joint. Walmart provides Tender Type data for AML purposes. Walmart indemnifies for its own compliance failures; GDC/Bank not obligated to cover Walmart's compliance failures.

Source: Agreement compliance provisions; Walmart indemnification carve-out for its own compliance.

**DIMENSION 3 — Indemnification**

Direction: Tri-party mutual structure.
GDC and Bank (jointly and severally) indemnify Walmart for: IP infringement, breach of agreement, negligence/willful misconduct, violation of applicable law.
Walmart indemnifies GDC/Bank for the same categories attributable to Walmart.
GDC/Bank not obligated to cover Walmart's own compliance failures — compliance carve-out explicitly in Walmart's favor.

Source: Agreement indemnification provisions.

**DIMENSION 4 — Liability Cap Structure**

Cap structure: Not disclosed (confidential treatment). Revenue sharing formula disclosed in press releases but liability cap structure not available in filed exhibit.
Consequential loss exclusion: Not separately confirmed in available excerpt.
Carve-outs from cap: Not disclosed.

Source: Not available in filed exhibit excerpt.

**DIMENSION 5 — Termination Triggers**

Convenience termination: Walmart may terminate on GDC material breach, insolvency, service level failure, or change of control.
Term structure: Initial Term through January 31, 2027. One-year auto-renewal unless 1-year advance written notice of non-renewal.
Regulatory trigger: Not separately enumerated in available excerpt.
De-risking / bank exit: Green Dot disclosed in its 2023 10-K body text that it de-converted BaaS partners from Green Dot Bank — bank-side de-risking in practice, though not reflected as a contractual provision in this agreement.
Wind-down obligations: Confirmed on termination.
Change of control: Walmart termination right on GDC change of control confirmed.

Source: Agreement term and termination provisions; Green Dot 2023 10-K body disclosure re: BaaS de-conversion.

---

## Cross-Company Observations (Preliminary — Not Doctrine)

The following observations are preliminary only. They are patterns across three agreements and do not constitute "market standard" claims. ML1 review required before any of these enter the doctrine base.

1. **BSA agent delegation structure:** Both Pathward/MetaBank agreements (Agreements 2A and 2B) use express BSA agent delegation — the bank formally appoints the program manager as its BSA agent. This is a specific legal mechanism under the Bank Secrecy Act that allocates operational performance to the PM while the bank retains regulatory exposure. Not observed in Bancorp Agreement 1A (less clear delegation structure) or Green Dot Agreement 3A (vertically integrated — no delegation needed).

2. **Consequential damages exclusion with three carve-outs:** Both Pathward agreements use an identical three-carve-out structure (indemnified claims, confidentiality/security breaches, gross negligence/willful misconduct/fraud). This pattern warrants further validation against additional agreements before any inference is drawn.

3. **Durbin Regulatory Event as named termination trigger:** Observed in Agreement 2B (MetaBank/EFS) only. Specific to banks near the $10B threshold. Not generalizable beyond that context — but documents that parties do negotiate bespoke regulatory economics triggers, not just generic "regulatory change" provisions.

4. **Bank suspension right (de-risking short of termination):** Present in both Pathward agreements. Structurally important: the bank retains the right to suspend distribution channels unilaterally on regulatory/reputational/safety grounds, without triggering a full termination event. This is a de-risking mechanism within the ongoing agreement, not a termination trigger.

5. **Green Dot vertical integration:** The Green Dot/Walmart structure is architecturally different from all other agreements found so far — program manager and issuing bank are affiliates on the same side, facing an enterprise retailer. This archetype (vertically integrated PM/bank vs. enterprise merchant) is distinct from the two-sided bank-fintech structure and should be tracked separately.

---

## CIK Corrections Required in Universe v0.3

| Company | Universe v0.3 CIK | Correct CIK |
|---|---|---|
| The Bancorp, Inc. | 1359190 | 1295401 |
| Toronto-Dominion Bank | 947484 | 947263 |

---

## Research Gaps and Next Steps

1. **Bancorp limitation of liability:** Not disclosed in Agreement 1A. Additional counterparty filings (PaySign/3PEA later filings) may have subsequent amendments with less redaction.
2. **Green Dot limitation of liability:** Not disclosed in Agreement 3A. Revenue sharing formula suggests a high-value relationship — liability cap likely significant.
3. **Green Dot WS-B:** Federal Reserve July 2024 consent order is a high-priority WS-B initiation target. Initiate Workstream B extraction from that enforcement action.
4. **Pathward full 15-dimension extraction:** Agreements 2A and 2B are the highest-quality sponsor-bank-side agreements found to date. Recommend full 15-dimension extraction as next pass.

---

## Source List

**The Bancorp:**
- PaySign EX-10.26 (Bancorp program agreement): https://www.sec.gov/Archives/edgar/data/1088034/000135448815001406/pyds_ex1026.htm

**Pathward Financial / MetaBank:**
- NetSpend EX-10.20 (MetaBank/NetSpend agreement): https://www.sec.gov/Archives/edgar/data/1496623/000104746910006467/a2199373zex-10_20.htm
- H&R Block EX-10.1 (MetaBank/EFS agreement): https://www.sec.gov/Archives/edgar/data/12659/000157484220000033/hrb20200731exhibit101.htm
- H&R Block First Amendment: https://www.sec.gov/Archives/edgar/data/12659/000160529721000020/exhibit101firstamendmentto.htm

**Green Dot:**
- Green Dot EX-10.6 (Walmart MoneyCard agreement): https://www.sec.gov/Archives/edgar/data/1386278/000138627820000020/exb106-2020amendedandr.htm
- Justia mirror: https://contracts.justia.com/companies/green-dot-corporation-596/contract/91012/

---

## Change Log

- 2026-04-28 — Initial 5-dimension extraction completed. Three companies screened; four agreements extracted. Two CIK corrections identified (Bancorp, TD). Green Dot WS-B flag raised (Federal Reserve consent order July 2024). Pathward agreements flagged for full 15-dimension extraction.
