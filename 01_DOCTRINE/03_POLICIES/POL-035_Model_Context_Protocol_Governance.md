---
id: POL-035
title: Tool Architecture and Governance Policy (Model Context Protocol)
owner: ML2
status: approved
approved_by: ML1
approved_date: 2026-04-18
version: 0.2
effective_date: 2026-04-18
supersedes:
provenance:
  decided_by: ML1
  decided_on: 2026-04-18
  context: Metadata normalized by system admin cleanup on 2026-05-24
created_date: 2026-03-09
last_updated: 2026-03-09
tags: [policy, mcp, tools, governance, runtime, auditability]
---

# POL-035 — Tool Architecture and Governance Policy (Model Context Protocol)

Status: Draft for ML1 Approval  
Authority Flow: ML1 -> ML2 -> System -> LL

## 1. Purpose

Policy Statement: MCP is the mandatory governance layer for tool and context interaction between model reasoning and system execution.

This policy establishes the definition, structure, governance, and operational use of tools in ML2 so that:
- external actions are executed by the System, not the model
- operational capabilities remain governed and inspectable
- interactions with external systems remain safe, deterministic, and auditable

Tools are the controlled boundary between model reasoning and real-world execution.

## 2. Definition of a Tool

A tool is a formally declared capability that a model may request the host runtime to execute.

Key properties:
- The model does not execute the operation directly.
- The model emits a structured tool request.
- The host runtime validates and executes the request.
- Results are returned as structured data.

## 3. Execution Model

Tool usage follows this pipeline:

1. User
2. Application / Agent
3. Model
4. Tool call (structured request)
5. Host runtime (MCP server/host)
6. Tool execution
7. External systems

Hard rules:
- The model cannot directly access external systems.
- All external actions occur through explicit tool requests.
- The host validates permissions and arguments before execution.
- Tool results return in structured form.

## 4. Tool Specification Structure

Every tool must declare at minimum:
- `name`
- `description`
- `input_schema`
- `output_schema`
- `permission_level`
- `execution_environment`

Example:
- Tool: `read_file`
- Purpose: retrieve file contents from a governed repository path
- Input schema: object with required `path` string

## 5. Tool Invocation Process

Standard sequence:
1. Model identifies required external action.
2. Model emits structured tool call.
3. Host validates schema and permission.
4. Host executes tool.
5. Host returns structured result.
6. Model continues reasoning from returned data.

## 6. Categories of Tools

### 6.1 Retrieval Tools
Purpose: expand model context from governed sources.
Examples: `read_file`, `search_repository`, `query_database`, `retrieve_document`

### 6.2 Action Tools
Purpose: create or modify system artifacts under permission control.
Examples: `create_document`, `send_email`, `create_ticket`, `update_database_record`

### 6.3 Computational Tools
Purpose: deterministic processing outside probabilistic model reasoning.
Examples: `run_python`, `calculate_financial_metrics`, `parse_document`, `run_regulatory_analysis`

### 6.4 Integration Tools
Purpose: connect governed workflows to enterprise systems.
Examples: CRM APIs, billing systems, compliance platforms, payment processors

## 7. Why Tools Matter

Models are probabilistic reasoning systems. Tools add:
- deterministic execution
- controlled access to external data
- governed interaction with software systems
- persistent operational effects under system control

## 8. Safety and Governance

All tool execution is host-controlled.

The host must enforce:
- tool availability scope
- argument/schema validation
- permission constraints
- execution policies
- logging and audit requirements
- rate limits and safety controls

Security requirements:
- sensitive systems remain permission-gated
- actions remain traceable
- prompt injection cannot elevate tool authority
- models cannot invent undeclared tools
- shell/scripting/system-modification tools must be sandboxed and explicitly gated

## 9. Relationship to Agents

Agents operate as a reasoning-and-tool loop:
1. interpret goal
2. plan steps
3. invoke tools
4. observe results
5. continue or escalate

Role boundary:
- Agents may decide sequence and strategy.
- Agents may not bypass MCP controls.
- Tools execute actions; agents/models do not directly perform external I/O.

## 10. Tool Design Principles

### Narrow scope
Each tool must perform one clearly defined function.

### Deterministic outputs
Tools should return predictable structured responses suitable for chaining.

### Explicit access boundaries
Each tool must declare system scope and permission boundary (read-only vs write vs restricted).

## 11. Professional Implementation

Typical operational tools include:
- `retrieve_matter_documents`
- `generate_proposal`
- `run_compliance_check`
- `extract_contract_terms`
- `create_client_email`

## 12. Change Control

No tool may be deployed without ML1 authorization through ML2 change governance.

Required change package:
- tool specification draft
- input/output schema
- access boundary statement
- security/execution rules
- risk assessment and rollback plan
- ML1 approval record

## 13. Enforcement

The System must enforce:
- schema validation
- access permissions
- invocation logging
- execution monitoring
- escalation on boundary failure

All tool activity must remain auditable, controlled, and attributable to governed runs.

Authority (Principles referenced): PRN-020, PRN-022, PRN-024, PRN-026, PRN-028, PRN-029
Enforcement expectation: Any runtime flow that bypasses MCP mediation, invokes undeclared tools, violates permission scope, or omits required audit logs is non-compliant and must be blocked or escalated to ML1.

Supersedes: None
Version: 0.1
Status: Draft
