---
id: 01_doctrine__03_capability_profiles__calendar_generate_prep_packet_md
title: Capability Profile: Calendar.GeneratePrepPacket
owner: ML1
status: approved
approved_by: ML1
approved_date: 2026-04-18
version: 0.1
effective_date: 2026-04-18
supersedes:
provenance:
  decided_by: ML1
  decided_on: 2026-04-18
  context: Metadata normalized by system admin cleanup on 2026-05-24
created_date: 2026-02-26
last_updated: 2026-02-26
tags: [capability, calendar, mcp]
---
# Capability Profile: Calendar.GeneratePrepPacket (v0.1)

## Purpose
Generate a prep packet for a meeting: agenda, last notes, risks, and follow-ups list.

## Allowed Actions
- Read event details
- Read local ML2 context artifacts (notes, prior packets)
- Generate markdown artifacts

## Disallowed Actions
- Editing events/invites
- Creating external tasks automatically

## Inputs (Typed)
- event_id: string
- context_paths: array<string> (paths to local ML2 artifacts)

## Outputs (Typed)
- prep_packet_md: string
- followups_md: string

## Required Logs
- event_id
- context_paths_used
- output artifact paths

## Approval Mode
- Auto

## Boundary Rules
- Local artifact reads must remain within repo boundaries.
- No external writes.
