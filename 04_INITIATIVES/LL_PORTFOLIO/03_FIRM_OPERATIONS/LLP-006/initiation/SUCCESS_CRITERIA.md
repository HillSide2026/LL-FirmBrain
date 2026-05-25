---
id: llp-006__success_criteria
title: LLP-006 Success Criteria
owner: ML1
status: draft
created_date: 2026-03-07
last_updated: 2026-03-07
tags: []
---

# Success Criteria

**Project:** LLP-006 — Matter Maintenance

> **ML2 DRAFT — Awaiting ML1 review and approval.**

## Criteria

All criteria must be verifiable from system data. Thresholds are proposed — ML1 must approve before implementation begins.

| Criterion | Proposed Threshold | Verification Source |
|---|---|---|
| Active matters with linked SharePoint folder | 100% | Clio matter ID cross-referenced against SharePoint inventory |
| Active matters with Gmail label mapping | 100% | Gmail label list cross-referenced against Clio matter IDs |
| Clio fields current (status, responsible lawyer, next action) | 100% of active matters reviewed per cycle | Clio API |
| Exception list produced per cycle | Every maintenance cycle | Run log |
| ML1 review time per cycle | To be set by ML1 | ML1 judgment |
| Zero critical gaps missed (false negatives) | 0 per cycle | Spot-check audit |

## Implementation Phase Complete When

- First full maintenance cycle runs end-to-end without manual intervention
- Exception list is produced and reviewed by ML1
- Diff logic is confirmed accurate against known prior state

## Out of Scope

- Subjective quality judgments without defined thresholds
- Criteria that cannot be verified from system data
- Success criteria for legal delivery outcomes (those belong to individual matters)
