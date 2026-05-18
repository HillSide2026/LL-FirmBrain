---
id: 04_initiatives_system_portfolio_01_active_roadmaps_stage5_readme_md
title: STAGE5 — Operating System Layer
owner: ML1
status: draft
created_date: 2026-05-18
last_updated: 2026-05-18
tags: []
---

# STAGE5 — Operating System Layer

## Goal
Convert ML2 from "files + chat" into an orchestrated, gated execution system.

## Ships
1) Run Graph orchestration (pipelines)
2) Hardened playbooks (acceptance-tested)
3) Executable doctrine (rules + tests + provenance)
4) Automatic retrieval + decision gating (bundles + gates)

## Exit Criteria
- 2 run graphs execute end-to-end and write to 06_RUNS/
- 2 playbooks hardened with acceptance criteria and passing runs
- Doctrine index exists with >=10 rules and >=10 tests
- Retrieval bundles are used automatically by run graphs
- Gates block external output without ML1 approval labeling
- All outputs carry label + provenance
