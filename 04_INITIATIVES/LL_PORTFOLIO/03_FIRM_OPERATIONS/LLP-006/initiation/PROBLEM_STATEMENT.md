---
id: llp-006__problem_statement
title: LLP-006 Problem Statement
owner: ML1
status: draft
created_date: 2026-03-07
last_updated: 2026-03-07
tags: []
---

# Problem Statement

**Project:** LLP-006 — Matter Maintenance

> **ML2 DRAFT — Awaiting ML1 review and approval.**

## Problem

Active matter records drift across Clio, SharePoint, and Gmail over time. No systematic process exists to identify or resolve these inconsistencies. As a result, ML1 cannot reliably assess matter records.

Specific failure modes observed:
- Clio matter fields (status, responsible lawyer, next action) are not updated as matters evolve
- SharePoint folders are missing, misnamed, or not linked to the corresponding Clio matter
- Gmail threads are not labeled or are labeled inconsistently, making inbox triage unreliable
- Overdue items accumulate without surfacing to ML1

## Impact of Not Solving

- ML1 decisions are made on incomplete or incorrect matter data
- LLP-005 outputs are degraded — exception lists contain false negatives
- Matter risk (execution, relationship) cannot be assessed accurately
- Firm capacity and docketing posture are invisible or misleading

## Current State

Matter maintenance is performed ad hoc, when issues are noticed, rather than systematically. There is no scheduled cycle, no exception list, and no structured diff between current and prior state. The gap between Clio, SharePoint, and Gmail records is unknown but expected to be material across the active matter portfolio.
