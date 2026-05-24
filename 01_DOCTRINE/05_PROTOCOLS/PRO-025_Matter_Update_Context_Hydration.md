---
id: PRO-025
title: Matter Update Context Hydration
owner: ML1
status: approved
approved_by: ML1
approved_date: 2026-04-26
version: 1.0
effective_date: 2026-04-26
supersedes:
provenance:
  decided_by: ML1
  decided_on: 2026-04-26
  context: Metadata normalized by system admin cleanup on 2026-05-24
created_date: 2026-04-26
last_updated: 2026-04-26
tags: [protocol, matters, context, hydration, classification]
---

# PRO-025 — Matter Update Context Hydration

## 1. Purpose

This protocol defines the pre-processing requirement that must be satisfied before any agent
or system operation performs a matter record update. It prevents email-derived or signal-derived
inference from overwriting or conflating established matter structure, service taxonomy, and
playbook classifications.

The core problem it addresses: agents that read Gmail or other signals and update matter records
without first loading existing matter state and playbook taxonomy produce ad hoc classifications
that violate the established service model. Once written, these classifications corrupt the
matter record and require manual correction.

---

## 2. Scope

This protocol applies to any operation that writes to or updates:

- `MATTER.yaml` — any field, especially `services`
- `MATTER_BRIEF.md` — any section
- `MATTER_STATUS.md` — any section
- `LL_TASK_TRACKER.md` — adding or modifying tasks for a matter
- `INDEX.md` — any matter entry

It does not apply to read-only operations (summarizing, reporting, presenting).

---

## 3. Required Context Load — Pre-Processing Steps

Before executing any matter update, the agent must load all of the following:

### 3.1 Existing Matter State

| Artifact | Path | What to read for |
|---|---|---|
| MATTER.yaml | `05_MATTERS/{tier}/{matter_id}/MATTER.yaml` | Current delivery_status, fulfillment_status, services list (service_type and service_name for each entry) |
| MATTER_BRIEF.md | `05_MATTERS/{tier}/{matter_id}/MATTER_BRIEF.md` | Current posture, open services, near-term milestones, prior named workstreams |

### 3.2 Matter Model and Taxonomy Rules

| Artifact | Path | What to read for |
|---|---|---|
| Matter Model Structural Invariants | `01_DOCTRINE/01_INVARIANTS/INV-0003-matter-model-structural-invariants.md` | Taxonomy Separation Rule (Rule 15); service_type allowed values (strategy, solution); at-least-one-service rule (Rule 16); service stream embedding rule (Rule 17) |
| Matter Summary and Task Governance | `01_DOCTRINE/05_PROTOCOLS/PRO-019_Matter_Summary_and_Task_Governance.md` | delivery_status definitions and permitted values; MATTER_BRIEF currency rules |

### 3.3 Practice Area Playbooks (load the applicable practice area)

#### Corporate / Commercial

| Artifact | Path | What to read for |
|---|---|---|
| Corporate Solutions README | `02_PLAYBOOKS/CORPORATE/SOLUTIONS/README.md` | Full solution index with sub-specs; canonical solution names |
| Corporate Strategies README | `02_PLAYBOOKS/CORPORATE/STRATEGIES/README.md` | Registered strategies and their scope |
| Specific solution SOLUTION_SCOPE.md | e.g., `02_PLAYBOOKS/CORPORATE/SOLUTIONS/SHAREHOLDER_AGREEMENT/SOLUTION_SCOPE.md` | When a solution applies and what it includes |

#### Financial Services / Payments

| Artifact | Path | What to read for |
|---|---|---|
| Market Structure Framework | `02_PLAYBOOKS/FINANCIAL_SERVICES/MARKET_STRUCTURE_FRAMEWORK.md` | Practice area scope and solution mapping |
| Payments agent spec (current) | `02_PLAYBOOKS/FINANCIAL_SERVICES/PAYMENTS/AGENTS/` | Active workstream definitions and classification rules |

For other practice areas, load the corresponding `SOLUTIONS/README.md` or equivalent index before proceeding.

---

## 4. Preservation and Extension Rules

Once context is loaded, the following rules govern how the update may proceed:

1. **Preserve existing service_type and service_name entries.** Do not rename, reclassify, or delete existing services on the basis of email content alone. Existing entries represent ML1-confirmed classifications.

2. **Extend, do not overwrite.** New information from email or other signals may be added as new service entries or as additional workstream detail within an existing entry. It must not replace existing entries.

3. **Use canonical names.** Service names must match or derive from playbook-defined solution and strategy names. Ad hoc naming (e.g., "Founders Agreement Advice", "Corporate Housekeeping") is not permitted. If a signal does not map to a known solution or strategy, flag it per §5.

4. **service_type must be set from taxonomy, not from context.** Do not classify a service as `strategy` because the matter is Strategic, or as `solution` because it sounds like a deliverable. Apply the definitions in INV-0003.

5. **Do not infer delivery_status from email signal.** delivery_status is ML1-set and encoded in the matter folder path. It may not be changed by an agent.

---

## 5. Conflict Handling

If email-derived or signal-derived content conflicts with the existing matter structure or playbook taxonomy, the agent must:

1. **Flag the conflict explicitly** in its output (MATTER_DIGEST.md, MATTER_STATUS.md, or a dedicated flag section).
2. **Describe both the existing classification and the conflicting signal** so ML1 can resolve.
3. **Not overwrite** the existing classification without explicit ML1 instruction.
4. **Not defer resolution** by writing a partial or hybrid structure that blends the existing classification with the ad hoc signal.

### Conflict flag format

```
CLASSIFICATION CONFLICT — [matter_id]
Existing: [existing service_type / service_name from MATTER.yaml]
Signal: [what the email or source suggests]
Reason flagged: [why they conflict — taxonomy mismatch, unknown solution name, etc.]
ML1 action required: confirm existing classification, or provide revised service_name and service_type
```

---

## 6. Agent Responsibility

Any agent that performs matter record updates — including but not limited to
`llm-matter-command-control` — is responsible for executing this protocol before writing.

The protocol cannot be delegated to a downstream step. Context hydration must occur before
the write, not after.

If an agent cannot load a required artifact (file not found, read failure), it must:
- Flag the missing artifact in its output
- Proceed only with the artifacts it could load
- Not assume the missing context is empty or irrelevant

---

## 7. Change Log

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-04-26 | Initial version. Prompted by MRKT matter (26-1637-00001): inbox triage updated matter records without loading existing taxonomy, producing ad hoc service classifications that conflicted with FRACTIONAL_COUNSEL / SHAREHOLDER_AGREEMENT / Founders' Term Sheet structure. |
