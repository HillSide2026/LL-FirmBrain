# ML1 Decision Queue

- Generated: 2026-05-23T14:00:00Z
- Agent: LLM-001 Chief of Staff
- Input freshness: LLM-004 run 2026-05-23T10:30:12Z, LLM-005 run 2026-05-23T10:30:12Z, LLM-006 run 2026-05-23T10:30:12Z

> Advisory output. ML1 approval required before any action is taken.

---

## Decision Queue

| Rank | Project | Decision Needed | Cash Flow Impact | ML1 or System | Urgency | Blocking | Source |
|------|---------|----------------|-----------------|---------------|---------|----------|--------|
| 1 | LLP-012 Funnel 2 Management | Close Planning → Executing gate once planning packet is complete; authorize execution of the Funnel 2 corporate-law acquisition path for Ontario businesses with over $1M annual cash flow | Direct — activates second revenue channel | ML1_REQUIRED | High | Yes — execution cannot start without gate closure | LLM-005, LLM-004 |
| 2 | LLP-013 Funnel 3 Management | Confirm active-progress or formal hold status; close Planning → Executing gate when ready; all execution surfaces (publishing, paid channels, checkout activation) remain explicitly gated | Direct — payments/MSB/PSP authority-positioning funnel; next billable channel after Funnel 1 | ML1_REQUIRED | High | Yes — all Funnel 3 execution is explicitly blocked pending ML1 gate | funnel-03/README.md, LLM-004 |
| 3 | LLP-037/038/039 ID collision | Assign new canonical IDs (LLP-045 onward suggested) to the growth project folders that currently conflict: LLP-037_LL_SYSTEM_DESIGN (system design), plus any LLP-038/039-suffixed growth folders. Confirm resolution approach. | Indirect — ID collision corrupts governance output; produces false at-risk signals; blocks clean portfolio management runs | ML1_REQUIRED | High | Yes — blocks clean governance runs for service management and growth projects | LLM-006 CONTRADICTION_ALERTS |
| 4 | LLP-037_LL_SYSTEM_DESIGN (successor ID) | Confirm project type (strategic vs. management; determines whether BUSINESS_CASE is required); approve Planning → Executing gate when packet is complete | Indirect — governs LL-WrkEngine, ll-corporate, and Legal Work System architecture; affects delivery capacity | ML1_REQUIRED | Medium | Yes — Phase 1 internal deployment cannot execute without gate closure | LLM-004, LLM-006 |
| 5 | LLP-038 at-risk project (ID to be resolved per item 3) | Sign APPROVAL_RECORD.md for initiation; confirm project scope and type | Indirect | ML1_REQUIRED | Medium | Yes — APPROVAL_RECORD is ML1-only; project cannot advance to any stage without it | LLM-006 APPROVAL_GAP_REPORT |
| 6 | LLP-039 at-risk project (ID to be resolved per item 3) | Confirm project type and close artifact gaps (SUCCESS_CRITERIA, STAKEHOLDERS, RISK_SCAN, ASSUMPTIONS_CONSTRAINTS, DEPENDENCIES, COMMUNICATION_PLAN); approve Planning → Executing gate when packet is complete | Indirect | ML1_REQUIRED | Medium | Yes — 6 missing artifacts block stage advancement | LLM-004, LLM-006 |
| 7 | Initiating queue — go/hold/park sweep | For placeholder-level Initiating packets (LLP-031 Corporate Entity Mgmt, LLP-032 Corporate Clerk, LLP-033 Associate Lawyer, LLP-034 Partner Supervision, LLP-015/035/036 Practice Areas, LLP-007 Admin, LLP-008 Closing, LLP-009 Clerk Supervision, LLP-010 Associate Supervision, LLP-026 Lead Capture, LLP-027/028/029 Intake sub-projects): confirm which are (a) active with near-term work, (b) valid placeholders to maintain, or (c) candidates for parking | None near-term; reduces governance noise and clarifies real WIP | ML1_REQUIRED | Medium | No — projects are holding; no execution at risk | LLM-005, LLM-004 |
| 8 | LLP-042 / LLP-043 review date | Both portfolio-management and project-management control packets carry "Not yet reviewed" Last ML1 Review Date; confirm review to give governance outputs authoritative status | None | ML1_REQUIRED | Low | No — outputs are produced regardless; confirmed review date cleans governance signal | LLM-006 |
| 9 | Draft missing planning artifacts for LLP-037_LL_SYSTEM_DESIGN | System drafts PROJECT_PLAN, DEPENDENCIES, RISK_REGISTER, COMMUNICATION_PLAN, METRICS from existing SCOPE_STATEMENT.md and PHASE_1_DEPLOYMENT.md for ML1 review | Indirect | SYSTEM_CAN_HANDLE | Medium | No — drafts do not substitute for gate decision | LLM-004 |
| 10 | Draft missing planning artifacts for LLP-012 Funnel 2 | System drafts remaining planning packet from funnel-02/README.md and FUNNEL_SPEC.md | Direct | SYSTEM_CAN_HANDLE | Medium | No — drafts precede gate decision | LLM-005 |
| 11 | Draft/complete missing planning artifacts for LLP-013 Funnel 3 | System drafts remaining planning packet from funnel-03/README.md, FUNNEL_SPEC.md, BD_NETWORKING_PLAN.md, traffic.yaml | Direct | SYSTEM_CAN_HANDLE | Medium | No — drafts precede gate decision | LLM-005 |
| 12 | Refresh LL_PROJECT_DIGEST.md and .tsv | System regenerates both files; replaces deprecated paths (01_ACCOUNTING/, 06_FINANCIAL_PORTFOLIO/) with canonical paths; adds LLP-044 and correctly resolved LLP-037 series | None near-term | SYSTEM_CAN_HANDLE | Low | No — digest is reference material only | LLM-001 synthesis |
| 13 | Refresh LL_PROGRAM_SUMMARY_REPORT.md | System refreshes from current management outputs after ID collision is resolved | None | SYSTEM_CAN_HANDLE | Low | No — reference document only | LLM-001 synthesis |

---

## Queue Notes

**Ranking logic:** Items 1–2 are cash-flow-direct gate decisions on the next two revenue channels. Item 3 is a governance prerequisite that corrupts portfolio health signals and should be resolved before the next governance cycle. Items 4–6 are artifact/approval completions blocked on ML1 action. Item 7 is a portfolio hygiene decision with no urgency but high noise-reduction value. Items 8–13 are system tasks or low-urgency confirmations.

**Dependency between items:** Item 3 (ID collision resolution) should precede items 4–6 and item 9 (artifact work under the growth project) so artifacts are filed under the correct permanent ID. Items 1–2 are independent of the ID collision and can proceed immediately.

**Volume context:** Of 43 scanned projects, 40 are on-track with zero open gate requirements. The active ML1 decision surface is concentrated in 5 specific projects (Funnel 2 gate, Funnel 3 gate/hold, ID collision, system design gate, LLP-038 approval record). The Initiating queue sweep in item 7 is a one-time cleanup, not a recurring decision.

**Cleanup priority note:** ML1 asked specifically for cleanup identification. The highest-value cleanup actions in order are: (1) ID collision resolution (items 3–6), which eliminates false at-risk signals and unblocks clean governance; (2) Initiating queue sweep (item 7), which reduces the volume of governance noise from placeholder packets; (3) digest and report refresh (items 12–13), which aligns reference documents with current state.
