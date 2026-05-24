---
id: 01_doctrine__03_capability_profiles__readme_md
title: Capability Profiles
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
created_date: 2026-02-08
last_updated: 2026-03-28
tags: []
---

# Capability Profiles

Definition: Capability profiles define explicit permission boundaries for components, layers, and tools under ML1 control.
Capability profiles are system boundaries for what a component may and may not do.
Boundary: Profiles do not replace binding doctrine, policies, or protocols.

This directory contains capability profiles for:
- Layer/component authority boundaries
- Legacy agent-level exception profiles
- Tool and wrapper operational permissions

---

## Relationship to Doctrine

| Layer | Analogy | Changeability |
|-------|---------|---------------|
| Canonical Doctrine | Constitutional law | Rarely changed |
| Capability Profiles | Statutes / Permits | Task-specific, revocable |

Doctrine defines **what agents cannot do by default**.
Profiles define **what specific agents may do under controlled conditions**.

---

## Profile Families

This folder currently contains three profile families:

| Family | Pattern | Use |
|--------|---------|-----|
| Layer profiles | `CAP-###-*` | Stable authority boundaries for constitutional layers/components |
| Legacy agent exception profiles | historical one-off format | Narrow agent-specific relaxations retained for continuity |
| Tool / wrapper profiles | `<namespace>.<tool>.md` | Bounded MCP or integration permissions for concrete runtime surfaces |

## Status Semantics

| Status | Meaning |
|--------|---------|
| `ACTIVE` | The profile is approved and operative for a current governed surface |
| `DRAFT` | The profile is being formalized or the surface is not yet fully admitted |
| `REVOKED` | The profile must not be used |

## Relaxation Axes

Profiles typically relax constraints along **one axis at a time**:

| Axis | Example Relaxation |
|------|-------------------|
| Write access | Read-only → draft-only → scoped edits |
| Scope | Single folder → project class → portfolio |
| Autonomy | On-demand → batch → scheduled |
| Confidence | Conservative → moderate (never assertive) |
| Memory | Stateless → session → scoped retrieval |

---

## Agent Progression Model

| Phase | Capability | Constraints |
|-------|-----------|-------------|
| 1 — Analysis Only | Read, summarize, recommend | No writes, no memory |
| 2 — Draft Generation | Create draft files | No overwrites, no lifecycle changes |
| 3 — Maintenance Edits | Update drafts | Append-only logs, no deletions |
| 4 — Structured Updates | Schema-bound updates | Still no authority, still reversible |

For agent execution profiles, at no point does an agent: **decide**, **approve**, **or override doctrine**.

---

## Profile Index

| ID | Name | Status | Scope |
|----|------|--------|-------|
| CAP-001 | ML1 (Human Authority Layer) | ACTIVE | Human authority permissions |
| CAP-002 | ML2 (System-of-Record Layer) | ACTIVE | Canonical record permissions |
| CAP-003 | System (Execution Layer) | ACTIVE | Runtime execution permissions |
| CAP-004 | LL (Distribution Layer) | ACTIVE | Market-facing distribution permissions |
| CAP-005 | Execution Bridge (Integration Layer) | ACTIVE | Integration transport permissions |
| 0001 | Draft Write Access | ACTIVE | Documentation synthesis |
| gmail.get_thread | Capability Profile: Gmail.GetThread | DRAFT | Gmail read retrieval |
| gmail.search_threads | Capability Profile: Gmail.SearchThreads | DRAFT | Gmail search |
| gmail.create_draft | Capability Profile: Gmail.CreateDraft | DRAFT | Draft-only outbound composition |
| sharepoint.list_folder | Capability Profile: SharePoint.ListFolder | ACTIVE | Metadata-only folder enumeration across approved drive aliases |
| sharepoint.get_item | Capability Profile: SharePoint.GetItem | ACTIVE | Metadata-only item retrieval across approved drive aliases |
| sharepoint.upload_draft | Capability Profile: SharePoint.UploadDraft | ACTIVE | Documentation DRAFTS upload surface |
| sharepoint.find_latest_template | Capability Profile: SharePoint.FindLatestTemplate | ACTIVE | Template lookup |
| sharepoint.diff_docs | Capability Profile: SharePoint.DiffDocs | ACTIVE | Read-only comparison |
| sharepoint.copy_template_to_wip | Capability Profile: SharePoint.CopyTemplateToWIP | ACTIVE | WIP copy in allowlisted zones |
| sharepoint.review_site_page | Capability Profile: SharePoint.ReviewSitePage | ACTIVE | Clients site page review helper |
| sharepoint.update_site_page_content | Capability Profile: SharePoint.UpdateSitePageContent | ACTIVE | Clients site page update helper |
| sharepoint.provision_client_workspace | Capability Profile: SharePoint.ProvisionClientWorkspace | ACTIVE | Clients workspace provisioning helper |
| sharepoint.manage_clients_site | Capability Profile: SharePoint.ManageClientsSite | ACTIVE | Broad Clients site authority wrapper |
| sharepoint.manage_documentation_site | Capability Profile: SharePoint.ManageDocumentationSite | DRAFT | Formalized broad Documentation wrapper pattern; not yet exposed as a dedicated MCP tool |
| calendar.list_events | Capability Profile: Calendar.ListEvents | DRAFT | Read-only schedule retrieval |
| calendar.generate_prep_packet | Capability Profile: Calendar.GeneratePrepPacket | DRAFT | Prep packet generation |

---

## Creating a New Profile

1. Copy `_TEMPLATE.md` or the nearest existing profile family
2. Use the canonical naming/id pattern for that family
3. Define scope narrowly
4. Document all relaxations explicitly
5. Require ML1 approval or explicit runtime admission context

---

## Revocation

To revoke a profile:
1. Change status to `REVOKED`
2. Add revocation date
3. No justification required
