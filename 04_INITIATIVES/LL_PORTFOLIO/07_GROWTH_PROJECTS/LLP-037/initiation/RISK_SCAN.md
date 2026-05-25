---
id: llp-037_risk_scan
title: LLP-037 Risk Scan — LL System Design
owner: ML1
status: draft
created_date: 2026-05-01
last_updated: 2026-05-01
tags: [llp-037, system-design, risk-scan]
---

# Risk Scan

| # | Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| R-01 | Lexora sync model decision delayed, blocking ll-task-tracker rearchitecting and accounts backlog | Medium | High | Prioritize OI-01 resolution as first ADR; do not start accounts lifecycle build until resolved |
| R-02 | Legal Work System evaluation expands into a full procurement/build cycle with long lead time | High | High | Timebox evaluation to 4 weeks; produce a requirements document and build-vs-adopt recommendation before committing |
| R-03 | ll-corporate evolves to absorb workflow logic while the Legal Work System is undefined | Medium | High | Enforce the self-declared constraint in ll-corporate's README; any expansion of ll-corporate scope requires an ADR approved in this project |
| R-04 | Accounts lifecycle built in ll-task-tracker before ownership question (OI-02) is resolved, requiring rework | Medium | Medium | Block accounts backlog implementation until OI-02 is resolved |
| R-05 | `LL_CURRENT_SYSTEM.md` becomes stale as repos evolve without being updated | Medium | Medium | Make LLP-037 the governing artifact; any system change that affects the current system map triggers an update obligation |
| R-06 | Mayan EDMS configuration (document types, workflows, cabinets) is never tracked in code, making ll-corporate-records opaque and unrecoverable | Low | High | Define a configuration-as-code strategy for Mayan as part of the ll-corporate-records integration contract |
