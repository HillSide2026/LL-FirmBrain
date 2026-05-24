---
id: 01_doctrine__03_capability_profiles__sharepoint_provision_client_workspace_md
title: Capability Profile: SharePoint.ProvisionClientWorkspace
owner: ML1
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
created_date: 2026-03-28
last_updated: 2026-03-28
tags: [capability, sharepoint, mcp, clients, provisioning]
---
# Capability Profile: SharePoint.ProvisionClientWorkspace (v0.2)

## Purpose
Provision one client-specific workspace inside the approved `/sites/Clients` managed workspace as a bounded helper capability.

## Allowed Actions
- Create one new client-specific page at `SitePages/<Client>.aspx`
- Create one new client-specific document library named `<Client>-Documents`
- Apply an initial supported page canvas and supported web parts during page creation
- Break inheritance and assign existing SharePoint principals to the created page and created library
- Add one shared-home navigation link pointing to the created client page or created library
- Execute only when invoked by an approved workflow, runbook, or capability and when run evidence is emitted into ML2

## Disallowed Actions
- Creating, deleting, or managing Entra groups, guest invitations, or tenant identity objects
- Altering tenant-wide retention, compliance, or external-sharing defaults
- Applying permissions outside the created page and created library
- Treating this capability as the full extent of authority over the broader `Clients` site

## Inputs (Typed)
- client_name: string
- page_name: string (optional, `<Client>.aspx`)
- page_title: string (optional)
- page_description: string (optional)
- page_body_html: string (optional)
- library_name: string (optional, `<Client>-Documents`)
- page_role_assignments: array of `{principal_id?: integer, principal_name?: string, role: string}`
- library_role_assignments: array of `{principal_id?: integer, principal_name?: string, role: string}`
- home_link_title: string (optional)
- home_link_location: string (optional, currently `TopNavigationBar` only)
- home_link_audience_ids: array of strings (optional)
- approval_reference: string (optional)

## Outputs (Typed)
- page: object
- library: object
- page_permissions: array
- library_permissions: array
- navigation_link: object
- warnings: array

## Required Logs
- client_name
- created page path and page id
- created library name and library id
- resolved principal ids and requested roles
- navigation target and created navigation node id when applicable
- run identifier
- acting tool or agent
- artifact version reference
- provenance label
- reason code
- upstream artifact reference
- approval_reference when provided

## Approval Mode
- Auto when the request stays within the current helper implementation, uses an approved workflow, runbook, or capability, and satisfies the active SharePoint write invariants.

## Boundary Rules
- The request MUST remain within `/sites/Clients`.
- The request MUST create at most one page and one library per invocation.
- The request MUST target existing principals only.
- The request MUST include artifact version reference and `Derived from ML2 vX.Y` provenance labeling or equivalent governed marker.
- The tool MUST NOT mutate arbitrary site structure outside the named page, named library, and one shared-home navigation target.
