---
id: INV-0005
title: Runtime Authority, Separation, and Final Output Invariants
owner: ML1
status: approved
approved_by: ML1
approved_date: 2026-04-18
version: 1.1
effective_date: 2026-04-18
supersedes:
provenance:
  decided_by: ML1
  decided_on: 2026-04-18
  context: Metadata normalized by system admin cleanup on 2026-05-24
created_date: 2026-03-08
last_updated: 2026-03-28
tags: [invariant, runtime, authority, separation, outputs]
---

# Runtime Authority, Separation, and Final Output Invariants (Binding Invariant)

## Runtime Authority Invariants
1. Doctrine Precedes Runtime: No runtime component may act outside ML2-defined doctrine and capability boundaries.
2. No Runtime Doctrine Creation: Agents, workers, tools, integration adapters, and run containers may not create doctrine.
3. Final Output Issuance Is Layer-Limited: Only the run's orchestrating agent may issue a final output.

## Separation Invariants
4. Orchestration / Execution / I-O Separation: Orchestration, bounded task execution, and external I/O must remain distinct functions.
5. Role Mapping Requirement:
   - Agents orchestrate.
   - Workers execute bounded tasks.
   - Tools and integration adapters perform external I/O.
6. No Collapsed Runtime Component: No single runtime component may simultaneously operate as orchestrator, worker, and integration adapter for the same governed action.
7. Tools Are Non-Governing: Tools and integration adapters perform actions only; they do not interpret doctrine, decide scope, or issue final outputs.
8. Matter Administration / Matter File Administration Separation: Matter Administration may govern matter identity, routing, status, deadlines, digests, and ML1-action views, but may not assert Matter File authority.
9. Matter File Administration Boundary: Matter File Administration may map, assess, and verify federated Matter File surfaces, but may not redefine matter identity or canonical `delivery_status` / `fulfillment_status`.

## Final Output Invariants
10. Final Outputs Must Be Attributable: Every final output must be attributable to a governed run, its orchestrating agent, and an authoritative basis in ML2.
11. Intermediate Artifacts Are Not Final Outputs: Drafts, classifications, extractions, QA findings, and other intermediate artifacts are not final outputs unless issued by the run's orchestrating agent.
12. Delivery Consumes, Not Reclassifies: The delivery layer may consume and distribute final outputs but may not reclassify intermediate artifacts as final outputs.

## Boundary and Escalation Invariants
13. Ambiguity Does Not Expand Authority: When authority, scope, or interpretation is unclear, the system must escalate rather than infer expanded permission.
14. Capability Boundaries Are Hard Limits: Assigned capability boundaries constrain runtime behavior even when broader action would be technically possible.
15. Failure Does Not License Improvisation: If a worker, tool, or integration adapter cannot complete a task within its boundaries, the failure must be surfaced rather than bypassed through improvised behavior.

## LL-Facing Invariants
16. Distribution Is Downstream of Final Output Issuance: Distribution may occur only after final-output issuance; market readiness does not itself convert an intermediate artifact into a final output.
17. Market Feedback Is Informational, Not Authoritative: Market response may generate Operational Signals but does not create doctrine or permit deviation.

## Boundary
These invariants define constitutional runtime boundaries.
Policies and protocols define operational enforcement details (gates, checks, escalation paths, and evidence schemas).
