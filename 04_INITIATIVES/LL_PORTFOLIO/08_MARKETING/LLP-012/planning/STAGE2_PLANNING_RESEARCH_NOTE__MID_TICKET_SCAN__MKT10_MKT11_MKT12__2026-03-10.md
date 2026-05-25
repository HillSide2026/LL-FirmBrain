---
id: llp_012__stage2_planning_research_note__mid_ticket_scan__mkt10_mkt11_mkt12__2026_03_10
title: Stage 2 Planning Research Note — Mid-Ticket Scan (MKT-10/11/12)
owner: ML1
status: draft
project_stage: planning
created_date: 2026-03-10
last_updated: 2026-03-10
tags: [llp-012, planning, funnel-02, mid-ticket, mkt-10, mkt-11, mkt-12]
---

# Stage 2 Planning Research Note — Funnel 02 Mid-Ticket Scan

## Scope
This scan re-runs:
- `MKT_SOCIAL_NARRATIVE_AGENT` (message fit)
- `MKT_OFFER_FUNNEL_AGENT` (funnel structure and qualification)
- `MKT_COMPETITIVE_POSITIONING_AGENT` (market differentiation)

Context assumption: Funnel 02 is a **mid-ticket professional services** funnel, not a low-friction commodity funnel.

---

## Executive Finding
Funnel 02 strategy is directionally correct for mid-ticket professional services, but execution logic remains under-specified at the exact places where mid-ticket funnels win or lose:
1. human qualification rigor,
2. stage-specific message compression,
3. explicit differentiation vs low-ticket and elite-firm alternatives.

---

## A. MKT-10 Message Scan (Mid-Ticket Fit)

### What works
- Positioning is calm, professional, and non-alarmist.
- Paid diagnostic framing supports serious-buyer filtering.
- Narrative matches operators with structural exposure.

### Gaps
1. **Stage 1 and Stage 2 copy architecture is too academic at top-of-funnel**
- Discovery and interest assets need shorter, sharper commercial hooks.

2. **Message-to-action bridge is weak for mid-ticket motion**
- Assets explain "why this matters" but under-specify "why book qualification now."

3. **Offer naming still has drift risk**
- Multiple product labels remain in working artifacts.

### Mid-ticket correction
- For Stage 1 (`awareness_discovery`): 1 problem, 1 consequence, 1 directional remedy.
- For Stage 2 (`awareness_interest`): 1 proof signal, 1 buyer-fit statement, 1 next-step CTA.
- Keep one canonical entry-offer name across all assets.

---

## B. MKT-11 Funnel Structure Scan (Mid-Ticket Qualification)

### What works
- Lifecycle sequence is now coherent.
- Conversion/handoff boundary is explicit.
- ICP and readiness filters are aligned to paid diagnostic.

### Gaps
1. **`intake_completed` does not yet enforce a mandatory human qualification call**
- Current intake tools are form/voice/SMS oriented.
- For mid-ticket services, this should include a real SDR qualification call before conversion.

2. **Qualification evidence schema is not explicit in funnel artifacts**
- Missing required call outputs such as:
  - fit decision (`qualified` / `not_qualified`)
  - buyer role and authority signal
  - urgency/timeframe
  - budget willingness for paid diagnostic
  - disqualification reason (if rejected)

3. **Friction sequencing may be too front-loaded**
- Full document readiness at inquiry stage can suppress otherwise qualified mid-ticket buyers.

### Mid-ticket correction
- Define `intake_completed` gate as complete only if:
  - SDR qualification call held,
  - call disposition recorded,
  - minimum fit fields populated,
  - paid diagnostic recommendation explicitly issued.
- Split readiness into:
  - pre-conversion minimum signals,
  - post-purchase document package completion.

---

## C. MKT-12 Competitive Positioning Scan (Mid-Ticket Market)

### What works
- Competitive matrix captures major alternatives.
- Preventative structured-review angle is strong.
- Paid entry offer differentiates from free consultation market.

### Gaps
1. **Mid-ticket lane is implicit, not explicit**
- Current wording differentiates from low-ticket options but does not clearly separate from premium bespoke firms.

2. **Proof architecture is still light**
- Need repeatable proof artifacts suitable for mid-ticket trust transfer:
  - sample output structure,
  - anonymized before/after scenarios,
  - timeline clarity.

### Mid-ticket correction
- Add explicit lane statement in Funnel 02 positioning:
  - not commodity template work,
  - not full bespoke enterprise program,
  - structured fixed-fee diagnostic for scaling operators.
- Add proof block to funnel assets:
  - output examples,
  - turnaround expectations,
  - what buyer gets immediately after purchase.

---

## Stage 1 and Stage 2 Clarification

For Funnel 02:
1. `awareness_discovery`
- Objective: first recognition of risk pattern.
- Output expectation: short problem-framing asset.

2. `awareness_interest`
- Objective: curiosity becomes active evaluation intent.
- Output expectation: proof-backed interest asset with explicit CTA to inquiry.

These are distinct states and should not be collapsed operationally.

---

## Priority Planning Actions (Next)

1. Add mandatory SDR call criteria to `intake_completed` gate definition.
2. Add qualification evidence fields to funnel intake artifacts.
3. Add mid-ticket lane statement and proof architecture to positioning assets.
4. Define stage-specific content templates for `awareness_discovery` and `awareness_interest`.

## Planning Conclusion
Funnel 02 is structurally viable for mid-ticket professional services once human qualification and proof architecture are codified as first-class gate requirements.

