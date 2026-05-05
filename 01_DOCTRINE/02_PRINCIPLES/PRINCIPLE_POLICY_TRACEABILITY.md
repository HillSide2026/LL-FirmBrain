---
id: 01_doctrine__principles_policy_traceability_md
title: Principle-to-Policy Cross-Reference (Traceability Index)
owner: ML1
status: active
created_date: 2026-05-04
last_updated: 2026-05-04
tags: [governance, traceability, principles, policies, doctrine]
---

# Principle-to-Policy Cross-Reference

This document maps principles (Level 2) to policies (Level 3), enabling traceability from interpretive values to operational constraints.

Use this index to:
- Understand which policies implement a principle
- Find the principle basis for a policy
- Trace doctrine hierarchy and dependencies

---

## Authority & Judgment Principles

| Principle | Title | Related Policies |
|-----------|-------|------------------|
| PRN-001 | Decision Principles | POL-003 (Novel Policy Prohibition), POL-013 (Steel Man Interpretation), POL-057 (ML1 Approval Boundaries) |
| PRN-002 | Human Primacy | POL-016 (System Authority Limit), POL-017 (Execution Authority Limit), POL-030 (Role Separation), POL-031 (Escalation on Boundary Failure) |
| PRN-020 | Authority-Boundary Clarity | POL-021 (Agent Orchestration), POL-022 (Worker Scope Limitation), POL-030 (Role Separation), POL-031 (Escalation on Boundary Failure) |
| PRN-038 | Relevance Does Not Imply Intervention | POL-021 (Agent Orchestration), POL-057 (ML1 Approval Boundaries) |

---

## Auditability & Inspection Principles

| Principle | Title | Related Policies |
|-----------|-------|------------------|
| PRN-003 | Auditability | POL-027 (Run Record Requirement), POL-028 (Auditable Tool Use), POL-029 (Output Provenance), POL-041 (Repository State Reporting Accuracy) |
| PRN-008 | Traceable Reasoning | POL-002 (Provenance Requirement), POL-008 (Traceable Reasoning Requirement), POL-029 (Output Provenance) |
| PRN-026 | Run-Centric Auditability | POL-027 (Run Record Requirement) |
| PRN-029 | Traceable Mediation | POL-028 (Auditable Tool Use), POL-024 (Integration Adapter Gatekeeping), POL-025 (No Direct External Access by Workers) |

---

## Stability & Drift Prevention Principles

| Principle | Title | Related Policies |
|-----------|-------|------------------|
| PRN-006 | Drift Intolerance | POL-007 (Consistency Supersession Requirement), POL-020 (Doctrine Bound Runtime), POL-041 (Repository State Reporting Accuracy) |
| PRN-007 | Interpretive Integrity | POL-013 (Steel Man Interpretation Requirement), POL-020 (Doctrine Bound Runtime) |
| PRN-009 | Structural Coherence | POL-014 (Doctrine Residency Requirement), POL-015 (Artifacts Residency Requirement), POL-055 (Repository Project Policy), POL-056 (Firm Project Policy) |
| PRN-019 | Observable Drift | POL-027 (Run Record Requirement), POL-041 (Repository State Reporting Accuracy) |

---

## Output & Execution Control Principles

| Principle | Title | Related Policies |
|-----------|-------|------------------|
| PRN-004 | Non-Autonomy | POL-016 (System Authority Limit), POL-017 (Execution Authority Limit), POL-023 (No Worker Final Output Issuance), POL-026 (Orchestrating Agent Final Output Issuance) |
| PRN-023 | Bounded Execution | POL-022 (Worker Scope Limitation), POL-023 (No Worker Final Output Issuance) |
| PRN-025 | Final Output Issuance | POL-023 (No Worker Final Output Issuance), POL-026 (Orchestrating Agent Final Output Issuance), POL-029 (Output Provenance) |
| PRN-027 | Layer Fidelity | POL-021 (Agent Orchestration), POL-023 (No Worker Final Output Issuance), POL-026 (Orchestrating Agent Final Output Issuance) |

---

## Scope & Clarity Principles

| Principle | Title | Related Policies |
|-----------|-------|------------------|
| PRN-005 | Explicit Scope | POL-006 (Clarity Single Job Requirement), POL-021 (Agent Orchestration Requirement) |
| PRN-028 | Capability Containment | POL-022 (Worker Scope Limitation), POL-024 (Integration Adapter Gatekeeping) |

---

## Output Quality Principles

| Principle | Title | Related Policies |
|-----------|-------|------------------|
| PRN-009 | Structural Coherence | POL-009 (Testability Requirement), POL-010 (Maintainability Versioning Requirement), POL-011 (Discoverability Requirement) |
| PRN-010 | Repeatable Excellence | POL-010 (Maintainability Versioning Requirement), POL-021 (Agent Orchestration Requirement) |
| PRN-036 | Reversibility | POL-058 (System Write Back Policy) |

---

## Doctrine & Governance Principles

| Principle | Title | Related Policies |
|-----------|-------|------------------|
| PRN-011 | *Reserved* | *Not applicable* |
| PRN-012 | Risk vs Uncertainty | POL-063 (Project Risk Artifact Lifecycle), POL-064 (LL Initiative Risk Policy), POL-065 (Matthew Holdings Initiative Risk Policy) |
| PRN-013 | Risk Lifecycle Governance | POL-063 (Project Risk Artifact Lifecycle), POL-064 (LL Initiative Risk Policy), POL-065 (Matthew Holdings Initiative Risk Policy) |
| PRN-014 | Deterministic Preference | POL-020 (Doctrine Bound Runtime), POL-021 (Agent Orchestration Requirement) |
| PRN-015 | Dependency Awareness | POL-021 (Agent Orchestration Requirement) |
| PRN-016 | Minimal Structural Mutation | POL-015 (Artifacts Residency Requirement), POL-058 (System Write Back Policy) |
| PRN-017 | Progressive Formalization | POL-003 (Novel Policy Prohibition), POL-020 (Doctrine Bound Runtime) |
| PRN-018 | Stability Under Extension | POL-014 (Doctrine Residency Requirement), POL-055 (Repository Project Policy) |
| PRN-021 | Layer Separation By Design | POL-020 (Doctrine Bound Runtime), POL-021 (Agent Orchestration), POL-022 (Worker Scope Limitation), POL-025 (No Direct External Access) |
| PRN-022 | Governed Orchestration | POL-021 (Agent Orchestration Requirement), POL-035 (Model Context Protocol Governance) |
| PRN-024 | Controlled Externality | POL-024 (Integration Adapter Gatekeeping), POL-025 (No Direct External Access by Workers), POL-035 (Model Context Protocol Governance), POL-037 (External System Integration Policy), POL-059 (Integration Control Policy) |

---

## Practice Area & Portfolio Principles

| Principle | Title | Related Policies |
|-----------|-------|------------------|
| PRN-019 | Observable Drift | POL-019 (Practice Area Tagging Requirement), POL-041 (Repository State Reporting Accuracy) |
| PRN-030 | LL Brand Identity Signal Integrity | POL-047 (LL Brand Governance), POL-048 (Off Template Asset Compliance), POL-049 (LL Brand Color Palette), POL-050 (LL Brand Identity) |
| PRN-031 | LL Brand Personality Expression | POL-046 (Canva Template Enforcement), POL-047 (LL Brand Governance), POL-048 (Off Template Asset Compliance), POL-050 (LL Brand Identity) |
| PRN-032 | LL Layout Discipline | POL-046 (Canva Template Enforcement), POL-047 (LL Brand Governance), POL-048 (Off Template Asset Compliance), POL-051 (LL Website Information Architecture) |
| PRN-033 | LL Image Style Restraint | POL-046 (Canva Template Enforcement), POL-047 (LL Brand Governance), POL-048 (Off Template Asset Compliance), POL-049 (LL Brand Color Palette), POL-050 (LL Brand Identity) |
| PRN-034 | LL Voice and Copy Alignment | POL-047 (LL Brand Governance), POL-048 (Off Template Asset Compliance), POL-050 (LL Brand Identity), POL-068 (Draft Email Voice Standard) |
| PRN-035 | Off-Template Brand Conformity | POL-046 (Canva Template Enforcement), POL-048 (Off Template Asset Compliance), POL-050 (LL Brand Identity) |
| PRN-037 | Wealth Building | POL-064 (Levine Law Initiative Risk Policy), POL-065 (Matthew Holdings Initiative Risk Policy) |

---

## Practice and Relationship Principles (LL)

*These principles are draft pending ML1 approval. Policy mappings are pending — each may warrant a dedicated client engagement or professional relationship policy.*

| Principle | Title | Related Policies |
|-----------|-------|------------------|
| PRN-039 | Retainer Precedence | POL-052 (Client Engagement Stage Policy) — partial; dedicated retainer policy pending |
| PRN-040 | Colleague Scarcity Gradient | *No governing policy yet — candidate for LL professional relationship policy* |
| PRN-041 | Good Colleague Reciprocity | *No governing policy yet — candidate for LL professional relationship policy* |
| PRN-042 | Colleague-Friend Distinction | *No governing policy yet — candidate for LL professional relationship policy* |
| PRN-043 | Demonstrate Understanding Before Probing | *No governing policy yet — candidate for LL client intake policy* |
| PRN-044 | Friendship Defines Altruistic Reciprocity | *No governing policy yet — candidate for LL professional relationship policy* |
| PRN-045 | Client-Friend Exclusion | *No governing policy yet — candidate for LL client engagement policy* |

---

## Strategic Principles (LL)

*Grounded in non-cooperative game theory. Policy mappings pending — these may warrant a dedicated LL Strategic Conduct Policy.*

| Principle | Title | Related Policies |
|-----------|-------|------------------|
| PRN-046 | Credible Commitment | *No governing policy yet* |
| PRN-047 | Cooperative Equilibrium | *No governing policy yet* |
| PRN-048 | Regulatory Mechanism Design | POL-052 (Client Engagement Stage Policy) — partial; covers when external enforcement is introduced |
| PRN-049 | Credible Retaliation | *No governing policy yet* |
| PRN-050 | Reputation Investment | *No governing policy yet* |

---

## Matter & Integration Principles

| Principle | Title | Related Policies |
|-----------|-------|------------------|
| PRN-024 | Controlled Externality | POL-035 (MCP Governance), POL-037 (External System Integration), POL-043 (Clio Matter ID Structure), POL-044 (SharePoint Staging), POL-045 (Asana Safeguard), POL-046 (Canva Enforcement), POL-059 (Integration Control) |

---

## Notes

- **Many-to-Many Relationship:** Principles often inform multiple policies; policies may implement multiple principles.
- **Hierarchical Enforcement:** Violations of principles flow through policies to protocols for enforcement.
- **Bidirectional Traceability:** Use this index to:
  1. **Forward:** From principle → related policies (answer: "What enforces this value?")
  2. **Backward:** From policy → related principles (answer: "What value justifies this rule?")

- **Missing References:** If a policy exists without a principle basis, it may indicate:
  - An operational/procedural rule (belongs in Protocols, not Policies)
  - A gap in principle coverage (candidate for new principle)

---

## Updates

- **Created:** 2026-05-04 (initial mapping)
- **Last Updated:** 2026-05-04

To update this cross-reference:
1. When adding a new principle, identify related policies and add rows.
2. When adding a new policy, identify the principle basis and add columns.
3. Mark deprecated mappings with `*Retired*` or `*Reserved*` status.
