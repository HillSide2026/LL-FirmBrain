# Canonical Artifact Location Map

Use this map to locate controlling artifacts. When in doubt about which artifact governs a question, start here.

## ML2 — System of Record

| Directory | What lives here | Index / Entry point |
|---|---|---|
| `01_DOCTRINE/` | All doctrine: invariants, principles, policies, protocols, capability profiles, procedural rules, SLAs, KPIs | `01_DOCTRINE/index.yaml` |
| `01_DOCTRINE/01_INVARIANTS/` | Hard structural rules — highest authority tier within ML2 | `INV-0008-authority-hierarchy-ml1-ml2-system-ll.md` for the authority model |
| `01_DOCTRINE/03_POLICIES/` | Operational policies governing system and agent behavior | `index.yaml` for full list |
| `01_DOCTRINE/05_PROTOCOLS/` | Enforcement and compliance check protocols | `index.yaml` for full list |
| `02_PLAYBOOKS/` | Practice area playbooks and solution frameworks | No master index — navigate by practice area subfolder |
| `02_PLAYBOOKS/FINANCIAL_SERVICES/` | Financial services market structure, RPAA doctrine, FOPs | `MARKET_STRUCTURE_FRAMEWORK.md` |
| `03_TEMPLATES/` | Approved output templates | Navigate by template type |
| `05_MATTERS/` | All active matter records | `05_MATTERS/DASHBOARDS/MATTER_INDEX.md` |
| `06_RUNS/` | Agent run outputs, portfolio reports, ops data | Navigate by run folder |
| `07_REFERENCE/` | External references and reference materials | `07_REFERENCE/INDEX.md` (sparse) |
| `08_RESEARCH/` | Research notes and legal research | Navigate by practice area subfolder |

## The System — Execution Layer

| Directory | What lives here |
|---|---|
| `agents/` | Agent skill.md files and workflow specs — each agent lists its controlling ML2 artifacts |
| `scripts/` | MCP servers, automation scripts, validation scripts |
| `09_INBOX/` | Intake pipeline stages (_sources → 00_UNTRIAGED → 01_CLASSIFIED_PROPOSALS → 02_NEEDS_HUMAN → 03_REJECTED_NOISE → 04_HISTORY) |
| `00_SYSTEM/` | Integration documentation, retrieval bundles, system configuration |

## Initiatives and Portfolio

| Directory | What lives here |
|---|---|
| `04_INITIATIVES/LL_PORTFOLIO/` | All firm portfolio projects: portfolio management, marketing, operations |
| `04_INITIATIVES/LL_PORTFOLIO/08_MARKETING/04_FUNNELS/` | Funnel definitions — navigate by funnel subfolder for current state |
| `04_INITIATIVES/HillSide_PORTFOLIO/` | HillSide business project portfolio |
