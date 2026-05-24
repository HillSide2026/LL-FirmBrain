---
id: pro-023
title: Run Log Standard
owner: ML1
status: approved
approved_by: ML1
approved_date: 2026-04-18
version: 1.0
effective_date: 2026-04-18
supersedes:
provenance:
  decided_by: ML1
  decided_on: 2026-04-18
  context: Metadata normalized by system admin cleanup on 2026-05-24
created_date: 2026-04-18
last_updated: 2026-04-18
applies_to: [System, ML2]
tags: [doctrine, protocol, run-log, audit, sla-sys-005, sla-ml2-001]
---

# PRO-023: Run Log Standard

## 1. Purpose

Define the required schema for all run log entries written to `06_RUNS/`. This is a convention requirement before it is a tooling requirement.

Every System output that enters `06_RUNS/` must comply with this schema. The `scripts/run_log_validator.py` script checks compliance. Non-compliant logs are flagged in the SLA audit cycle.

---

## 2. Scope

Applies to all entries under:

```
06_RUNS/
  ops/          — operational audit outputs (schema audit, integration health)
  proposals/    — client-facing proposals
  matter/       — matter-specific run outputs
  agent/        — agent execution logs
```

---

## 3. Required Schema

### 3.1 Frontmatter (all run log .md files)

```yaml
---
run_id: {YYYYMMDD_HHMMSS}_{agent_or_script_id}
run_date: {YYYY-MM-DD}
run_time: {HH:MM:SS UTC}
agent_or_script: {id of the agent or script that produced this output}
matter_id: {Clio matter ID, or "none" for system-level runs}
task: {one-line description of what was executed}
slas_covered: [{list of SLA IDs this run is evidence for}]
output_classification: {internal | ll-consumable}
status: {complete | partial | failed}
---
```

### 3.2 Required Fields — Definition

| Field | Requirement | Notes |
|-------|-------------|-------|
| `run_id` | Required | Format: `YYYYMMDD_HHMMSS_{agent}`. Must be unique. |
| `run_date` | Required | ISO 8601 date |
| `run_time` | Required | UTC time |
| `agent_or_script` | Required | Must match an agent ID or script filename |
| `matter_id` | Required | Clio ID or literal `none` |
| `task` | Required | Non-empty string |
| `slas_covered` | Required | At least one SLA ID, or `[]` with justification |
| `output_classification` | Required | Must be `internal` or `ll-consumable` |
| `status` | Required | Must be `complete`, `partial`, or `failed` |

### 3.3 Body Structure

The body following the frontmatter is not schema-enforced but must include at minimum:

1. **Summary** — one paragraph describing what ran and what it found
2. **Findings or Output** — structured output (table, list, or reference to JSON output file)
3. **Violations or Flags** — explicit section, even if empty (`None`)
4. **Next Actions** — explicit section, even if none (`None`)

---

## 4. JSON Output Files

Scripts that produce structured data (audit scripts, health checks) must write both:
- A `.md` file complying with §3 above
- A companion `.json` file with the same `run_id` as the base filename

The `.json` file must include at minimum:

```json
{
  "run_id": "...",
  "run_date": "...",
  "run_time": "...",
  "agent_or_script": "...",
  "matter_id": "...",
  "status": "...",
  "summary": "...",
  "findings": [...],
  "violations": [...],
  "exit_code": 0
}
```

---

## 5. Output Classification

| Origin | Default Classification |
|--------|----------------------|
| LLM-001 through LLM-006 (portfolio agents) | `internal` |
| `scripts/ml2_schema_audit.py` | `internal` |
| `scripts/integration_health_check.py` | `internal` |
| `scripts/run_log_validator.py` | `internal` |
| Matter agent outputs in `05_MATTERS/` | `ll-consumable` |
| Proposals in `06_RUNS/proposals/` | `ll-consumable` |

---

## 6. Validation

`scripts/run_log_validator.py` checks:
- All required frontmatter fields present and non-null
- `run_id` format conforms to `YYYYMMDD_HHMMSS_*`
- `output_classification` is a valid value
- `status` is a valid value
- Body contains the four required sections (by heading keyword)

Validation is run as part of the monthly ML1 review (PRO-024) and may be run ad hoc.

---

## 7. SLA Coverage

| This protocol enforces | Via |
|------------------------|-----|
| SLA-SYS-005 (Failure Predictability) | Requires `status` and `violations` in every log |
| SLA-ML2-001 (Record Integrity) | Requires frontmatter on all ML2 artifacts |
| KPI-ML2-004 (Schema Compliance) | Validated by run_log_validator.py |

---

## 8. Non-Compliance

A run log that fails validation is a SLA-ML2-001 violation. The generating agent or script is responsible for producing compliant output. Non-compliant logs are flagged in the next SLA audit cycle and reported to ML1.
