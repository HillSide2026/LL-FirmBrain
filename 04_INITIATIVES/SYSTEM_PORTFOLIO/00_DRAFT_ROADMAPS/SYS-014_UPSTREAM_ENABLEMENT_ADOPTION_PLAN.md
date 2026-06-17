---
id: 04_initiatives__system_portfolio__00_draft_roadmaps__sys_014_upstream_enablement_adoption_plan_md
title: SYS-014 — Upstream Enablement Adoption Plan (Draft)
owner: ML1
status: draft
created_date: 2026-06-17
last_updated: 2026-06-17
tags: [system-portfolio, draft, upstream, matter-control, operator-enablement]
---

# SYS-014 — Upstream Enablement Adoption Plan (Draft)

## Purpose

Capture a planning-only implementation sequence for selectively adopting the
highest-value assets from `second-brain-factory/matthew-levine-second-brain`
into `ll-secondbrain` without importing the upstream `memory/` and `tasks/`
model wholesale.

This is a planning artifact only. It does not authorize execution.

## Scope

### In Scope

- workflow authority normalization for the Levine Law matter control loop
- matter-control agent prompt refactors
- operator-facing startup and setup docs
- a local setup doctor
- command/skill layer templates adapted to ML2 surfaces
- generated context-pack outputs tied to current retrieval bundles
- optional Cowork skill enablement after a local skill layer exists

### Out of Scope

- direct import of upstream `memory/`, `tasks/`, `src/`, or PocketBase app stack
- execution-stage repo changes outside explicitly approved follow-on work
- any change that creates a second source of truth beside `00_SYSTEM/`,
  `05_MATTERS/`, and current ML2 control surfaces

## Key Constraint

Local ML2 structures govern. Upstream assets must be translated into existing
local control surfaces, not copied in as a parallel operating system.

## Target Local Surfaces

| Concern | Target Surface |
|---|---|
| Workflow authority | `00_SYSTEM/AGENTS/specs/matter_admin/` |
| Runtime agent prompts | `.claude/agents/` |
| Repo/operator startup docs | repo-root `AGENTS.md` plus `docs/` |
| Command manifest | repo-root `COMMANDS.md` |
| Generated context packs | `06_RUNS/ops/context-pack/` |
| Retrieval bundle selection | `00_SYSTEM/retrieval/bundles.yaml` |
| Cowork enablement | `scripts/` plus `docs/` |

## Preconditions

- ML1 confirms system-level work should be promoted from backlog before
  execution begins.
- Existing local matter-control surfaces remain authoritative:
  - `.claude/agents/llm-matter-command-control.md`
  - `.claude/commands/matter-overview.md`
  - `00_SYSTEM/retrieval/bundles.yaml`
- Any follow-on write work must satisfy canonical write validation and current
  doctrine constraints.

## Implementation Waves

### Wave 1 — Workflow Authority and Matter-Control Normalization

1. Map each upstream artifact to a local destination.
   - Separate reusable prompts, docs, and setup utilities from upstream
     `memory/`, `tasks/`, and app-stack assumptions.
   - Freeze the keep/translate/skip decision before code or doc changes begin.

2. Implement the workflow authority layer.
   - Port the upstream primary-workflow and workflow-context material into one
     local governing spec under `00_SYSTEM/AGENTS/specs/matter_admin/`.
   - Normalize the core categories:
     - action today
     - waiting
     - needs clarification
     - monitor
     - source freshness
     - safe next step
   - Cross-link the new spec from `CLAUDE.md` and `00_SYSTEM/AGENTS.md`.

3. Refactor the matter-control agents instead of replacing them.
   - Fold the upstream daily-control-loop logic into the existing local
     matter-control agent.
   - Add a narrower `matter-signal-triage` agent prompt as a separate local
     agent.
   - Preserve local rules that are stronger than upstream:
     - source-of-truth hierarchy
     - slice limits
     - provenance on every claim
     - no legal conclusions
   - Reconcile overlap with `matter-overview` so the outputs use the same
     categories and freshness language.

### Wave 2 — Operator Startup and Setup Layer

4. Add operator-facing startup docs.
   - Create a repo-root `AGENTS.md` for Codex entry behavior.
   - Add:
     - `docs/customer-onboarding.md`
     - `docs/codex-setup.md`
     - `docs/setup-doctor.md`
   - Describe the local repo as it actually works:
     - `05_MATTERS/`
     - `05_MATTERS/LL_TASK_TRACKER.md`
     - `06_RUNS/`
     - `09_INBOX/`
     - Gmail / SharePoint / Slides / Canva MCPs
     - canonical write validation via `.claude/settings.json`

5. Add a local setup doctor.
   - Implement `scripts/setup-doctor.mjs`.
   - Keep the upstream operator experience: show the first failing check and one
     next action.
   - Adapt checks to this repo:
     - `git`
     - `node`
     - `python3`
     - valid `.mcp.json`
     - valid `.claude/settings.json`
     - write-hook wiring
     - presence of local auth/config prerequisites for Gmail, SharePoint,
       Slides, and Canva

### Wave 3 — Command Surface and Context Handoff

6. Build the reusable command/skill layer.
   - Add `COMMANDS.md` as the local manifest.
   - Implement a small general workflow layer in `.claude/skills/`:
     - `start`
     - `setup`
     - `overview`
     - `simple-cycle`
     - `my-workflow`
   - Adapt each one to local sources, not upstream `memory/`:
     - `05_MATTERS/DASHBOARDS/`
     - `05_MATTERS/LL_TASK_TRACKER.md`
     - `06_RUNS/`
     - `09_INBOX/`
     - `00_SYSTEM/`
   - Keep domain-specific work in `.claude/commands/`, especially
     `matter-overview`.

7. Implement the context-pack as generated output.
   - Extend `00_SYSTEM/retrieval/bundles.yaml` with a
     `daily_matter_control_loop` bundle.
   - Add a generator that emits:
     - `brain-overview.md`
     - `workflows.md`
     - `open-loops.md`
     - `source-index.json`
   - Write generated packs to `06_RUNS/ops/context-pack/`.
   - Source them only from authoritative local artifacts.

8. Enable Cowork last.
   - Add:
     - `scripts/install-skills-to-cowork.sh`
     - `docs/COWORK-SKILLS.md`
   - Limit this to the new general workflow skills, not the whole repo.

## Deliverables

- a file-by-file upstream adoption matrix
- a local workflow authority spec for the matter control loop
- updated matter-control agent prompts
- operator-facing startup and setup docs
- `scripts/setup-doctor.mjs`
- `COMMANDS.md` plus a minimal local workflow-skill layer
- context-pack generation design and output location
- optional Cowork skill installation support

## Sequencing Rationale

- Start with workflow authority and matter-control normalization because that is
  the part most likely to affect daily ML1 use.
- Add setup and onboarding only after the local workflow surfaces are defined.
- Build generalized commands and generated context packs after the authority and
  setup surfaces are stable.
- Leave Cowork enablement last so it reflects the final local skill surface
  rather than an intermediate state.

## Main Risk

The upstream repo assumes a `memory/` and `tasks/` operating model. Literal
porting would create a competing control surface inside ML2. All follow-on work
must be framed as translation into current local structures.

## Completion Condition

This planning artifact is complete when ML1 can decide whether to keep `SYS-014`
in backlog, promote it into an initiating/planning packet, or decompose it into
smaller system-level items with clear file targets, sequence, and risk framing.
