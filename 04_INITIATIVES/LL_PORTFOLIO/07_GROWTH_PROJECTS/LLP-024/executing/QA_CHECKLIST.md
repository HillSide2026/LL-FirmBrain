---
id: llp-024__implementation__qa_checklist
title: LLP-024 NDA Esq — QA Checklist
owner: ML1
status: active
created_date: 2026-03-19
last_updated: 2026-04-02
tags: [nda-esq, executing, qa]
---

# QA Checklist

Project ID: LLP-024
Project Path: 07_GROWTH_PROJECTS/LLP-024
Stage: Executing

## Pre-Launch QA (MVP Gate)

| Check | Owner | Status | Notes |
|-------|-------|--------|-------|
| Generated NDA QA pass rate ≥ benchmark (per METRICS.md) | Product lead | Not checked | Required before public launch |
| Guided intake and generation flow end-to-end tested | Product lead | Not checked | |
| Billing and payment flow tested | Product lead | Not checked | |
| Data privacy compliance review complete | ML1 | Not checked | Required — SaaS product with user data |
| Terms of service and acceptable use policy reviewed by ML1 | ML1 | Not checked | |
| No negotiation, redlining, or bespoke drafting paths appear in product copy or UX | ML1 | Not checked | |
| Qualified consult routing path tested | Operations lead | Not checked | |
| Support response path tested | Operations lead | Not checked | |
| Performance under simulated load tested | Product lead | Not checked | |

## Post-Launch QA (30-Day Review)

| Check | Owner | Status | Notes |
|-------|-------|--------|-------|
| `retained_client_usage_30_day` threshold met | ML1 | Not checked | Per METRICS.md |
| `generated_nda_qa_pass_rate` validated against benchmark | ML1 | Not checked | |
| Qualified consult routing is producing usable handoff data | ML1 | Not checked | |
| Support response time within SLA | Operations lead | Not checked | |
| No data or privacy incidents | ML1 | Not checked | |

---

*All MVP gate checks must be complete before public launch. ML1 must sign off on privacy and legal guardrail checks.*
