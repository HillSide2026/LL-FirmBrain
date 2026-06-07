---
id: 04_initiatives__ll_portfolio__ll_project_backlog_md
title: LL Project Backlog
owner: ML1
status: draft
created_date: 2026-05-18
last_updated: 2026-06-07
tags: [ll, projects, backlog, portfolio]
---

# LL Project Backlog

Staging area for Levine Law Portfolio projects that have been identified but not
yet initiated. Items here are pre-Initiating stage under `POL-055`,
`POL-056`, and `POL-073`.

Promotion to an active project (Initiating stage, with a project folder under
`04_INITIATIVES/LL_PORTFOLIO/`) requires ML1 instruction.

## Backlog Items

| Project Name | Type | Description | Date Added | Priority | Notes |
|---|---|---|---|---|---|
| GHL Pipeline Governance and Stage Standardization | Operational | 7 GHL pipelines confirmed via API: "LL - Corporate (New)" (Funnel 02), "LL - Corporate (Google)" (duplicate/legacy — retire or merge decision required), "LL - FINTECH" (Funnel 03), "LL - Inquiries" (unassigned to a funnel), "Sales - New Business", "Sales - Renewal Business", "archive". Funnel 02 and Funnel 03 GHL stages are out of sync with repo `pipeline.yaml` specs. GHL specialist hired. Deliverables: (1) retire or merge the duplicate corporate pipeline; (2) standardize Funnel 02 and Funnel 03 GHL stages to match repo specs; (3) determine ownership of "LL - Inquiries", "Sales - New Business", and "Sales - Renewal Business" pipelines. | 2026-06-07 | — | GHL pipeline IDs registered in each funnel `pipeline.yaml`. Actual GHL stages documented in `ghl_actual_stages` fields. Full pipeline list retrieved via GHL API 2026-06-07. |

---

## Governance

- `Type` is one of: `Strategic`, `Management`, `Operational`, `Decision`.
- Items are added on ML1 instruction or captured during a session per POL-070.
- Promotion requires ML1 instruction. Do not auto-promote.
- Once promoted, create a project folder under the appropriate
  `04_INITIATIVES/LL_PORTFOLIO/` subfolder and assign a `LLP-NNN` identifier
  per `POL-056`.
- The project folder name must equal the `Project ID`. Do not create new
  `LLP-NNN_NAME` folders.
