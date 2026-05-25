---
id: 04_initiatives__ll_portfolio__07_growth_projects__llp_033_associate_lawyer__planning__staffing_recommendation_note__2026_04_03_md
title: Associate Lawyer - Staffing Recommendation Note
owner: ML1
status: draft
created_date: 2026-04-03
last_updated: 2026-04-03
tags: [associate-lawyer, planning, staffing, compensation]
---

# Staffing Recommendation Note

Project ID: `LLP-033`
Stage: `Planning`

## Recommendation

The first delivery-lawyer implementation should be modeled as a **mid-level but
competent supervised associate**, not as a senior lawyer.

Reason:

- this is the role the current `LLP-033` packet is already designed around
- the initial workset is supposed to be bounded, repeatable, and lower-variance
- the real test is whether Levine Law can create supervised delivery leverage
  without losing quality, margin, or control
- a senior-lawyer hire is a different operating scenario and should be modeled
  separately rather than treated as the default first step

## Recommended Initial Scenario

### Scenario A - Mid-Level Supervised Associate

Best fit for first implementation:

- a mid-level lawyer operating under ML1 supervision
- focused on repeatable corporate/commercial maintenance work
- repeatable contract drafting and review
- bounded remediation work arising from standardized diagnostics

Not the first delegation set:

- bespoke disputes
- major transactions
- unscripted high-stakes client strategy
- specialist regulatory matters unless later approved explicitly

### Candidate Compensation Structures

| Structure | How it works | Cost structure to firm | Best use | Main risk |
| --- | --- | --- | --- | --- |
| Contractor split | Lawyer is paid a percentage of collected fees on eligible delegated matters | variable lawyer cost + direct matter cost + allocated acquisition cost + ML1 supervision time; little idle-capacity burden | only suitable for someone comfortable with variability and needing strong self-management skills and experience | candidate wants employee security; candidate has significant financial obligations |
| Low-base / high-variable | Lawyer receives a smaller fixed base or retainer plus larger variable pay tied to collections or contribution | moderate fixed cost + variable comp + direct matter cost + allocated acquisition cost + ML1 supervision time | best for a hybrid profile that combines discipline with some entrepreneurial tolerance | candidate wants upside like a contractor but behaves like they expect guaranteed economics |
| Base salary + bonus | Lawyer receives fixed base pay plus a bonus tied to collected revenue, contribution, or quality targets | fixed salary cost + payroll burden/benefits + bonus + direct matter cost + allocated acquisition cost + ML1 supervision time | best for someone who wants stable integration and shows stronger consistency, teamwork, and long-term operating discipline | candidate expects stability but will not work inside structured supervision or process |

### Primary Selection Rule

The first question is not which compensation model looks best in theory.

The first question is:

**How much repeatable delegated work does Levine Law actually have?**

The compensation model should be chosen only after ML1 has a real view of:

- current eligible delegated matter volume
- stability of that volume month to month
- collections reliability on that work
- supervision burden per matter
- confidence that the delegated workset will persist long enough to justify the
  cost structure

### Workload-Driven Model Choice

| Workload condition at Levine Law | Best-fit model | Why |
| --- | --- | --- |
| work volume is still uncertain, intermittent, or being tested | Contractor split | keeps fixed-cost risk low while ML1 proves that the delegated workset is real |
| work volume looks real but is not yet fully stable or collections are still uneven | Low-base / high-variable | adds some stability without assuming a fully proven recurring workload |
| work volume is sustained, repeatable, and operationally stable | Base salary + bonus | makes sense only once Levine Law can support true integration with confidence |

### Working Recommendation On Structure

Preferred order for the first activation test:

1. contractor split
2. low-base / high-variable
3. base salary + bonus only after the delegated matter set is proven and the
   operating model is stable

Why:

- model choice should follow Levine Law's actual workload and revenue stability
- Levine Law still needs to prove the supervision model
- Levine Law still needs to prove the real delegated contribution margin
- the first implementation should minimize fixed-cost risk while the model is
  still being validated
- the commercial model should match candidate temperament, not just legal skill

## Separate Scenario

### Scenario B - Senior Lawyer Delivery Layer

This should be treated as a separate scenario, not just a more expensive
version of Scenario A.

It becomes plausible only when the firm is dealing with:

- sustained overflow beyond ML1 capacity
- larger and more judgment-heavy files
- a real need for more independent client-facing legal execution
- a stable enough revenue base to absorb materially higher fixed or semi-fixed
  lawyer cost

This is directionally consistent with `BUSINESS_PLAN.md`, which treats the
senior-lawyer delivery role as a later staffing layer triggered by sustained
capacity breach at `CAD 300,000+` annualized revenue.

### Senior Lawyer Compensation Structures

| Structure | How it works | Cost structure to firm | Best use | Main risk |
| --- | --- | --- | --- | --- |
| Contractor counsel split | Senior lawyer is paid a negotiated share of collected fees on clearly bounded files or overflow work | higher variable lawyer cost than a mid-level associate + direct matter cost + acquisition cost + reduced-but-still-real ML1 supervision burden | useful if the firm wants to test higher-level overflow capacity before taking on fixed salary | margin can compress quickly on files that already require substantial partner input |
| Higher base salary + performance bonus | Senior lawyer receives a larger fixed base plus bonus for collections, contribution, or book performance | high fixed salary cost + payroll burden/benefits + bonus + direct matter cost + acquisition cost + ongoing supervision/sign-off cost | appropriate only when the firm already has a durable book that justifies a real second delivery pillar | largest fixed-cost exposure and strongest pressure on utilization |
| Low-base / high-variable counsel model | Smaller fixed draw or salary plus larger variable comp tied to collected work, contribution, or partial book ownership | moderate fixed cost + more aggressive variable cost + direct matter cost + acquisition cost + supervision/governance overhead | useful where the lawyer is expected to carry more autonomy or help build a book | complexity, incentive drift, and possible confusion between employee, counsel, and partner-track logic |

## Practical Recommendation

For planning purposes:

- use **Scenario A** as the default implementation model
- treat the first hire as a **mid-level supervised associate**
- test the economics first with a **contractor split** or **low-base /
  high-variable** structure
- keep **Scenario B** as a later, separately modeled senior-lawyer option once
  revenue, supervision, and matter complexity justify it

## Decision Rule

No structure should be treated as approved until ML1 is satisfied that the
model works after including:

- direct lawyer cost
- direct matter cost
- allocated acquisition cost
- ML1 supervision time
- rework and exception burden

## Source Anchors

- `README.md`
- `SCOPE_STATEMENT.md`
- `ASSUMPTIONS_CONSTRAINTS.md`
- `DEPENDENCIES.md`
- `RISK_REGISTER.md`
- `../../LLP-030/BUSINESS_PLAN.md`
