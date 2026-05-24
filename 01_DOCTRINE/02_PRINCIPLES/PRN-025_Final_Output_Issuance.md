---
id: PRN-025
title: Final Output Issuance
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
created_date: 2026-03-08
last_updated: 2026-03-23
tags: [principle, authority, outputs]
applies_to: [ML2, System, LL, HillSide]
---

# PRN-025 - Final Output Issuance

Title: Final Output Issuance

Statement:
Only the orchestrating agent for a governed run may issue final outputs. Other agents, workers, and integration adapters may generate intermediate artifacts but may not issue the run's final output.

Rationale:
Single-point final issuance preserves accountability and avoids output-status confusion across execution chains.

Supersedes: None
Version: 1.0
Status: Active
