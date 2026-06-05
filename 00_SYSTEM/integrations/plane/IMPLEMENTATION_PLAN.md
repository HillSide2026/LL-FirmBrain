---
id: 00_system_integrations_plane_implementation_plan
title: Plane Integration Implementation Plan
owner: ML1
status: draft
created_date: 2026-06-05
last_updated: 2026-06-05
tags: [plane, integration, implementation-plan]
---

# Plane Integration Implementation Plan

## Deployment Model

Plane is self-hosted via Docker Compose on this machine. No cloud account.
Docker is confirmed available. Target: `http://localhost`.

### Setup steps (one-time)

1. Clone `https://github.com/makeplane/plane`
2. Configure env vars in the Plane repo (follow Plane's `setup.sh` or `.env` guidance)
3. Run `docker compose up` to bring up all services
4. Create the first admin user via the Plane web UI at `http://localhost`
5. Create a workspace (e.g. "Levine Law")
6. Generate an API token from Settings → API Tokens

## Repo-Side Setup (after Plane is running)

Set three env vars in this repo's shell environment:

```
PLANE_API_KEY=<from Plane Settings → API Tokens>
PLANE_WORKSPACE_SLUG=<workspace slug from Plane URL>
PLANE_API_BASE_URL=http://localhost  # or the port Plane binds to
```

Then run the provisioning script once:

```
npm run setup:plane
```

This scans the repo and creates 36 Plane projects:

- 2 portfolio projects: LL Portfolio, HillSide Portfolio
- 34 matter projects: all Essential, Strategic, and Standard matters
  (names derived from `MATTER.yaml`: `"<matter_name> (<matter_id>)"`)

It writes all mappings to `project-map.json` and is idempotent on re-run.
Use `--dry-run` to preview without touching the Plane API.

Then sync ticket snapshots any time:

```
npm run sync:plane
```

## Smallest Fitting Integration

1. Plane is the source of truth for ticket state, assignee, priority,
   labels, cycle, and project.
2. Only Markdown snapshots are stored in this repo.
3. Each Plane project is explicitly mapped in `project-map.json` to a repo
   project folder. Unmapped projects are skipped with a logged warning.
4. Snapshots are written into a `plane/` subdirectory inside each mapped folder.
5. Repo project folders are never created from Plane.
6. Manual sections (`## Links` and below) are preserved across syncs.

## Scripts and Files

| Artifact | Path | Purpose |
|---|---|---|
| Provisioning script | `scripts/setup-plane-projects.ts` | Create Plane projects + write project-map.json |
| Sync script | `scripts/sync-plane-tickets.ts` | Pull ticket snapshots from Plane API |
| Mapping file | `00_SYSTEM/integrations/plane/project-map.json` | Plane project → repo folder mappings |
| NPM setup | `npm run setup:plane` | Run provisioning script |
| NPM sync | `npm run sync:plane` | Run sync script |

## Mapping Format

Each entry in `project-map.json` supplies:

- `plane_project_id` (written by setup script after project creation)
- `plane_project_name`
- `project_path`: repo-relative path to the project folder
- `ticket_dir`: path relative to `project_path` where snapshots land (`plane/`)

## Status

| Step | Status |
|---|---|
| Scripts written and type-checked | Done |
| Plane self-hosted service running | Pending |
| Env vars configured | Pending |
| `npm run setup:plane` run | Pending |
| `npm run sync:plane` run | Pending |
