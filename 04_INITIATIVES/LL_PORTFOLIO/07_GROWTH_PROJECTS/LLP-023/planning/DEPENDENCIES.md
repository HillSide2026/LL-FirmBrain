---
id: 04_initiatives__ll_portfolio__07_growth_projects__llp_023_matter_command_control__planning__dependencies_md
title: Matter Command and Control - Dependencies
owner: ML1
status: draft
created_date: 2026-03-23
last_updated: 2026-03-23
tags: [matter-command-control, planning, dependencies]
---

# Dependencies

Project ID: `LLP-023`
Stage: `Planning`

## Project-Level Dependencies

| Dependency | Why It Matters | Primary Home |
| --- | --- | --- |
| Clio read access and stable matter identifiers | The command layer depends on a reliable matter registry key | Clio |
| Gmail label discipline and thread access | Slice 1 routing quality depends on stable communication signals | Gmail |
| Governed Gmail state-label write path | Reviewed threads only move into canonical state labels if the approval and audit path is usable | Gmail integration + approval artifacts |
| SharePoint naming discipline and file access | Slice 2 cannot work without deterministic document mapping | SharePoint |
| Approved cache and run-state rules | The project fails if normalized state drifts into shadow-database behavior | local run/cache discipline |
| ML1 acceptance of derivative-output boundaries | The project only works if outputs remain clearly subordinate to systems of record | ML1 governance |
| Run-graph and config discipline | Daily and one-matter modes depend on stable orchestration and config rules | `00_SYSTEM/orchestration` and `00_SYSTEM/CONFIG` |
| Exception visibility path | Ambiguous routing must surface somewhere explicit instead of disappearing | `INBOX_UNMAPPED.md` and run outputs |

## Dependency Notes

- `LLP-023` depends more on boundary discipline than on broad feature volume.
- The most important dependencies are the ones that preserve trust in outputs:
  join keys, naming discipline, exception visibility, citation coverage, and the
  approval-gated Gmail state-label path.
- Slice 2, 3, and 4 should not be treated as free extensions of Slice 1. Each
  depends on the earlier slice being trustworthy enough to promote.

## Planning-Gate Dependencies

Before ML1 should close a `Planning -> Executing` decision for the next phase,
the packet must show:

- explicit slice order
- explicit source-boundary rules
- explicit `25`-thread daily review-pass rule
- explicit promotion criteria between slices
- explicit exception-handling path
- explicit metric logic for daily-run reliability and citation coverage
