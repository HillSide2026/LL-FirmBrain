---
id: llp-037_planning_assumptions_constraints
title: LLP-037 Assumptions and Constraints
owner: ML1
status: draft
created_date: 2026-05-01
last_updated: 2026-05-01
tags: [llp-037, planning, assumptions, constraints, deployment]
---

# Assumptions and Constraints

Project ID: `LLP-037`  
Stage: `Planning`

---

## Deployment Infrastructure Constraints

### DC-001 — LL-WrkEngine: Split Frontend / Backend Deployment

| Field | Value |
|---|---|
| Decision | Frontend deployed on Vercel. Backend deployed on a full Node hosting platform (Render or Railway). |
| Decided by | ML1 |
| Date | 2026-05-01 |
| Reason | LL-WrkEngine backend requires capabilities not compatible with serverless constraints. |

**Implications:**

- Frontend (`engine.levinellp.ca`) routes to a Vercel deployment of the Next.js frontend
- Backend API is hosted on Render or Railway — a persistent, non-serverless Node process
- Backend requirements that drive this constraint include: LibreOffice process for DOC/DOCX to PDF conversion, long-running document processing, and stateful worker behavior incompatible with cold-start / ephemeral serverless execution
- CI/CD pipelines, environment variable management, and deployment configuration must account for two separate hosting targets
- CORS and API routing between Vercel frontend and Render/Railway backend must be explicitly configured

**Platform Selection (Render vs. Railway):**

Not yet decided between Render and Railway. Both are compatible with the constraint. Selection to be made during Phase 1 deployment setup. Record the decision in this file when made.

---

## Assumptions

| # | Assumption | Basis | Risk if Wrong |
|---|---|---|---|
| A-01 | Vercel supports the Next.js frontend without modification | Next.js is Vercel-native; frontend has no serverless-incompatible requirements | Low |
| A-02 | Render / Railway can run the Bun/Node backend with LibreOffice available | Both platforms support custom buildpacks or Docker-based deployments | Medium — verify LibreOffice availability on chosen platform before Phase 1 |
| A-03 | Supabase (auth + Postgres) is compatible with both Vercel and Render/Railway | Supabase is platform-agnostic | Low |
| A-04 | S3-compatible object storage (e.g. Cloudflare R2) is accessible from both deployment targets | Standard HTTPS API | Low |
| A-05 | Phase 1 testing data will not contain real client data | ML1 decision — Phase 1 is seeded/fake data only | High if violated — see `PHASE_1_DEPLOYMENT.md` exclusions |

---

## Open Constraints

| # | Constraint | Status |
|---|---|---|
| OC-01 | Render vs. Railway platform selection | Open — to be resolved during Phase 1 deployment setup |
| OC-02 | LibreOffice availability on chosen backend platform | Must be verified before Phase 1 deployment |
| OC-03 | AGPL-3.0 compliance posture for LL-WrkEngine customizations | Open — see `LL_FUTURE_SYSTEM.md` OI-03b |
