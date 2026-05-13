# Dependencies

Project ID: LLP-001
Project Path: 01_ACCOUNTING/LLP-001_ACCOUNTING
Stage: Planning

## Material Dependencies

| Dependency | Type | Why It Matters | Current Planning Position |
| --- | --- | --- | --- |
| Source-record availability | Internal records | Reconciliation design fails if statements, invoice records, payment records, or expense support cannot be located consistently | Must be mapped before execution approval |
| Bookkeeping process reality | Operating support | The governed cadence must match how bookkeeping actually happens rather than an idealized schedule | Needs explicit review during planning |
| Acquisition-spend source tagging | Internal records | July acquisition tracking fails if marketing and sales spend cannot be identified consistently at source level | Classification rule must be frozen before 2026-07-01 |
| ML1 exception authority | Governance | Some accounting exceptions require human judgment and may not be auto-resolved | Must be frozen before execution |
| LLP-002 fact-consumption rules | Cross-project | Budgeting should consume only approved, freshness-bounded facts | Handoff rules must be explicit before execution |
| LLP-002 acquisition budget setup | Cross-project | Acquisition budget governance depends on LLP-001 supplying combined marketing + sales actuals as one historical category | Actuals handoff and budget cadence must be aligned before July |
| Close support standard | Control design | ML1 needs a minimum support package to review reconciliations and unresolved items | Standard must be defined in planning |

## Dependency Notes

- Dependencies listed here are limited to items that could block or materially
  change execution.
- Acquisition classification should preserve source-level detail where possible
  even though LLP-002 will consume a combined `acquisition` budget category.
- Platform migration or software-selection work is intentionally excluded from
  this dependency set because that would change the project itself.
- If a required source class cannot be reliably produced, planning should
  narrow scope or raise an explicit exception rather than pretending the packet
  is complete.
