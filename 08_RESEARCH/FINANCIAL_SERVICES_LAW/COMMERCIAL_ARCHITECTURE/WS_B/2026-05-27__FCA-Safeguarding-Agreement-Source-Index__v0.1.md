---
id: ws-b-fca-safeguarding-agreement-source-index-v0.1
title: FCA Safeguarding Agreement Source Index
layer: 08_RESEARCH
domain: financial-services-law
workstream: WS-B
artifact_type: source_index
status: draft
authority: not-approved
confidence: exploratory
created: 2026-05-27
updated: 2026-05-27
scope: "UK FCA payment services / e-money safeguarding"
matter_id: null
output_label: "Derived from regulatory reconstruction (FCA) - not explicit contract language"
sources:
  - type: guidance
    citation: "FCA - Safeguarding requirements"
    url: "https://www.fca.org.uk/firms/emi-payment-institutions-safeguarding-requirements"
  - type: policy_statement
    citation: "FCA PS25/12"
    url: "https://www.fca.org.uk/publication/policy/ps25-12.pdf"
  - type: handbook
    citation: "FCA Handbook CASS 10A"
    url: "https://handbook.fca.org.uk/handbook/CASS/10A"
  - type: market_terms
    citation: "Telleroo EMI Terms"
    url: "https://www.telleroo.com/terms-and-conditions-emi"
  - type: market_terms
    citation: "Bound Safeguarding"
    url: "https://bound.co/legal/safeguarding"
  - type: market_terms
    citation: "VFX Safeguarding Funds"
    url: "https://vfxfinancial.com/regulatory-information/uk/safeguarding-funds"
  - type: market_terms
    citation: "MuchBetter Safeguarding"
    url: "https://muchbetter.com/it/legal/safeguarding-your-muchbetter-account"
  - type: market_terms
    citation: "Crezco Terms"
    url: "https://www.crezco.com/terms-and-conditions"
  - type: market_terms
    citation: "UK First Fintech Terms"
    url: "https://www.firstfintech.co.uk/es/condiciones/"
  - type: market_terms
    citation: "TallyMoney Terms"
    url: "https://www.tallymoney.com/terms-and-conditions/"
open_questions:
  - "Locate any publicly available executed safeguarding account acknowledgement letters, if available."
  - "Confirm whether each market example is current at time of extraction."
  - "Separate customer-facing safeguarding disclosure from bank/custodian acknowledgement letter mechanics."
next_actions:
  - "Extract each source into the WS-B seven-layer matrix."
  - "Create a control gap library for no set-off, reconciliation, insolvency distribution, and account designation mechanics."
---

# FCA Safeguarding Agreement Source Index

## Status

This is a draft source index for researching FCA safeguarding agreement mechanics.
It is not approved doctrine and does not state market standard.

The public sources located are mostly customer-facing terms or safeguarding
disclosures. They are useful for identifying disclosed safeguarding mechanics,
but they are not the private bank or custodian safeguarding account agreement.

The closest FCA-public "agreement" source is the CASS 15 safeguarding account
acknowledgement letter template referenced through FCA PS25/12.

---

## Regulatory Baseline

| Source | Link | Relevant provisions to extract |
|---|---|---|
| FCA safeguarding requirements page | https://www.fca.org.uk/firms/emi-payment-institutions-safeguarding-requirements | Safeguarding under PSRs reg. 23 and EMRs reg. 20; segregation or insurance/guarantee method; monthly reporting; daily reconciliations; third-party due diligence; resolution packs; safeguarding audits. |
| FCA PS25/12 / CASS 15 Annex 1 | https://www.fca.org.uk/publication/policy/ps25-12.pdf | Safeguarding account acknowledgement letters; account identification; bank/custodian acknowledgement; no set-off or counterclaim; safeguarding account title; release to firm or insolvency office-holder; annual review/replacement; five-year retention. |
| CASS 10A Resolution Pack | https://handbook.fca.org.uk/handbook/CASS/10A | Requires executed agreements, side letters, and CASS 15 acknowledgement letters relating to holding relevant funds/assets to be kept in a retrievable resolution pack. |

---

## Specific Market Examples

| Example | Link | Relevant safeguarding provisions to extract |
|---|---|---|
| Telleroo EMI terms | https://www.telleroo.com/terms-and-conditions-emi | E-money account; funds held in segregated accounts; bank assurances; no lending/use of customer funds; no FSCS for e-money; insolvency practitioner return mechanics; ClearBank insolvency / possible FSCS look-through. |
| Telleroo general terms page | https://www.telleroo.com/terms-conditions | Agent of Moorwand versus Telleroo EMI structure; safeguarded funds at ClearBank; useful for agency-to-direct EMI transition language. |
| Bound safeguarding page | https://bound.co/legal/safeguarding | Segregated accounts with UK-authorised banks; operational funds separation; point at which funds reserved/due for FX settlement cease to be safeguarded; separate treatment of regulated FX contract client money; FSCS distinction. |
| VFX safeguarding page | https://vfxfinancial.com/regulatory-information/uk/safeguarding-funds | Trust language; segregated UK high-street bank account; ringfencing; bank written classification as safeguarded account; bank confirms no set-off/counterclaim; daily reconciliation; annual independent audit. |
| VFX terms PDF | https://www.vfxfinancial.com/Files/VFXFinancial_Terms_1.8.pdf | Definitions such as "Client Safeguarding Account"; interaction with VFX account and FX order mechanics. |
| MuchBetter safeguarding page | https://muchbetter.com/it/legal/safeguarding-your-muchbetter-account | Dedicated safeguarding bank account; separation from operational funds; third-party access blocked; no FSCS. |
| MuchBetter business account agreement | https://muchbetter.com/business-accounts/legal-mbb/services-agreement | "Segregated Account" definition; not a bank disclosure; money kept separate in safeguarding account with banking partner; money paid into operational account is safeguarded and e-money credited; pooled accounts; no proprietary right to pooled funds, only account balance claim. |
| Crezco terms | https://www.crezco.com/terms-and-conditions | Dedicated safeguarding account or equivalent permitted method; insolvency priority before general creditors; segregated customer account with UK credit institution; no FSCS; not aggregated with working capital; limited use for payment instructions only; third-party provider / CurrencyCloud / ClearBank variants. |
| Crezco FAQ | https://support.crezco.com/faqs | Currencycloud as safeguarding provider for cross-border payments; funds held in safeguarded accounts; useful for outsourced EMI/provider model. |
| UK First Fintech terms | https://www.firstfintech.co.uk/es/condiciones/ | Authorised EMI; money held in relevant safeguarded account in exchange for e-money; segregation method; segregated bank accounts; no investment/lending; insolvency protection via EEA-authorised credit institution or Bank of England; no FSCS. |
| TallyMoney terms | https://www.tallymoney.com/terms-and-conditions/ | Transact Payments account; fiat e-money safeguarded; GFSC/FCA cross-border structure; no DSSG/FSCS equivalent for e-money; segregation from other cash balances; no lending/use of fiat funds; safeguarding stops once fiat converts to tally/gold; insolvency practitioner cost/delay disclosure. |
| TallyMoney protection page | https://www.tallymoney.com/is-tallymoney-a-scam/ | Security Trust Agreement and trustee structure for gold-side protection; useful as contrast with e-money safeguarding. |

---

## Extraction Headings

Use these headings for a later WS-B matrix or control-gap library:

| Heading | Extraction target |
|---|---|
| Regulatory status | EMI, API, agent, FCA FRN, named issuer, named safeguarding provider. |
| Safeguarding method | Segregation, trust, insurance/guarantee, pooled account, dedicated account. |
| Account location | UK-authorised bank, ClearBank, CurrencyCloud, banking partner, Bank of England, EEA credit institution. |
| Account characterization | Safeguarded account, client money account, segregated customer account, trust account. |
| No set-off / no counterclaim | Bank/custodian acknowledgement that it has no set-off, counterclaim, security interest, or recourse against relevant funds. |
| No use of funds | No lending, no business-purpose use, no aggregation with working capital. |
| Reconciliation / audit | Daily reconciliation, independent audit, monthly FCA reporting. |
| Insolvency mechanics | Return by insolvency practitioner, costs deducted, timing risk, priority over general creditors. |
| Compensation scheme disclosure | FSCS/DSSG not applicable, except limited look-through possibilities where a safeguarding bank fails. |
| Boundary of protection | When funds cease to be safeguarded, including FX settlement, conversion to gold/tally, or other non-e-money treatment. |
| Third-party provider model | Agent/issuer/provider split, including Telleroo/Moorwand, Crezco/CurrencyCloud/ClearBank, and Tally/TPL examples. |

---

## Research Use

This source index should feed:

- `FCA_CASE_ARCHITECTURE_MAP` artifacts for individual examples;
- a `CONTROL_GAP_LIBRARY` for no set-off, acknowledgement letter, reconciliation,
  insolvency distribution, and account designation mechanics;
- an `IMPLIED_CLAUSE_REQUIREMENTS` artifact translating FCA safeguarding
  expectations into structural drafting requirements.

Do not use these sources to claim market standard without a separate,
source-attributed Workstream A or ML1-approved synthesis.
