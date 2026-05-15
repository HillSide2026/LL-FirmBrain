# Risk Register

Project ID: LLP-001
Project Path: 01_FINANCIAL_MANAGEMENT/LLP-001_ACCOUNTING
Stage: Planning

## Planning Risk Register

| Risk | Category | Likelihood | Impact | Goal at Risk | Mitigation |
| --- | --- | --- | --- | --- | --- |
| Accounting facts drift into modeling or strategy language | Scope | M | H | Keep LLP-001 fact-only | Enforce explicit exclusions and LLP-002 boundary language in every planning artifact |
| Source evidence is incomplete or inconsistently available | Scope | M | H | Reliable fact packet | Freeze only the source classes that can actually be supported and flag the rest as explicit exceptions |
| Marketing and sales spend are tagged inconsistently before the July acquisition cutoff | Control | M | H | Reliable acquisition actuals feed | Freeze one acquisition classification rule, preserve source detail, and escalate ambiguous items instead of burying them in overhead |
| Reconciliation cadence is more ambitious than operating capacity | Schedule | M | H | Sustainable close rhythm | Design cadence around real operating support and escalate if coverage cannot be maintained |
| Open exceptions are hidden instead of surfaced | Control | M | H | Reviewable accounting packet | Require unresolved-item visibility and ML1 escalation rules before execution approval |
| LLP-002 consumes stale or qualified facts as if they were final | Financial | M | H | Safe downstream handoff | Add freshness warnings, exception disclosure, and explicit handoff conditions to the planning packet |

## Planning Risk Posture

The main risk is not inactivity. The main risk is false confidence: a packet
that looks governed while still mixing fact maintenance, judgment, and modeling
assumptions. Planning must keep those roles visibly separate.
