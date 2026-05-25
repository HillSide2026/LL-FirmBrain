---
id: 04_initiatives__ll_portfolio__07_growth_projects__llp_023_matter_command_control__planning__risk_register_md
title: Matter Command and Control - Risk Register
owner: ML1
status: draft
created_date: 2026-03-23
last_updated: 2026-03-23
tags: [matter-command-control, planning, risk-register]
---

# Risk Register

Project ID: `LLP-023`
Stage: `Planning`

## Category Rule

As a Levine Law strategic project, LLP-023 must use only the canonical
categories permitted by `POL-063` and `POL-064`:
- `Scope`
- `Schedule`
- `Budget`
- `Financial`
- `Strategic`

| Risk ID | Risk | Category | Likelihood | Impact | Planned Control | Owner |
| --- | --- | --- | --- | --- | --- | --- |
| R-01 | The command layer drifts into shadow-system behavior beyond approved caches and derivative artifacts | Scope | Medium | High | Freeze read-only boundaries and explicitly prohibit source-of-truth replication | ML1 + ML2 |
| R-02 | ML2 outputs are treated operationally as authoritative matter truth rather than derivative visibility artifacts | Strategic | Medium | High | Require citation-backed assertions and preserve source-of-record language in outputs | ML1 |
| R-03 | Slice creep pushes document, deadline, or comms features ahead of core Slice 1 stabilization | Scope | High | High | Freeze slice order and require promotion criteria before adding later slices | ML1 |
| R-04 | Gmail label drift or SharePoint naming inconsistency reduces routing or mapping confidence | Schedule | High | Medium | Keep ambiguous cases in exception outputs and use explicit overrides instead of silent guesses | ML2 |
| R-05 | Heuristic fallback behavior creates false confidence in routing quality | Strategic | Medium | High | Surface review-required cases explicitly and measure citation/routing confidence before promotion | ML1 + ML2 |
| R-06 | Build effort on later slices consumes time without proving command-layer value first | Budget | Medium | Medium | Treat Slice 1 as the first value gate and block later-slice expansion until it passes | ML1 |
| R-07 | Daily run reliability remains too weak to support a trusted morning command view | Schedule | Medium | High | Measure run completion and required outputs over a controlled baseline window | ML2 |

## Highest-Leverage Planning Risks

- `R-01`: shadow-system drift breaks the project's governing boundary
- `R-03`: slice creep destroys prioritization discipline
- `R-05`: false confidence is worse than visible incompleteness
