---
id: 00_system__matters__matter_task_and_dashboard_doctrine
title: Matter Task and Dashboard Doctrine
owner: ML1
status: draft
created_date: 2026-05-13
last_updated: 2026-05-13
tags: [matters, tasks, doctrine, matter-index, matter-digest, ml1]
---

# Matter Task and Dashboard Doctrine

This document defines the task vocabulary and dashboard interpretation rules
for Levine Law matter tracking.

The purpose is to prevent system tracking artifacts from being mistaken for
legal judgment, quality review, or final task assignment.

## Core task types

### ML1 Task

An **ML1 Task** is something Matthew / ML1 must personally decide, review,
approve, do, or consciously monitor.

ML1 Tasks include:

- decisions requiring legal judgment;
- client-facing judgment calls;
- supervising or reviewing work by LL team members or external lawyers;
- deciding whether a matter signal is important;
- approving strategy, priority, or risk posture;
- reviewing documents where ML1 judgment is required;
- monitoring points that ML1 must keep visible even before the exact legal step
  is determined.

An ML1 Task may or may not be a Legal Task. For example, checking whether a
matter needs attention, deciding who should handle it, or monitoring client
correspondence may be ML1 Tasks even before legal work is identified.

### Legal Task

A **Legal Task** is substantive legal-service work on a matter.

Legal Tasks include:

- reviewing, drafting, revising, or sending legal documents;
- giving legal advice;
- preparing legal correspondence;
- negotiating with counsel, counterparties, regulators, or clients;
- analyzing legal risk, rights, obligations, evidence, or strategy;
- filing or authorizing legal forms, notices, or registrations where legal
  judgment is involved.

A Legal Task requires the relevant matter folder, recent email thread,
attachments, client context, and ML1 judgment before the system may state the
actual legal step with confidence.

### LL Task

An **LL Task** is work that belongs to Levine Law as a firm or operating system,
but does not necessarily require ML1 personally and is not necessarily legal
work.

LL Tasks include:

- docketing, billing, accounting, trust-record, or collection follow-up;
- routing, filing, labeling, or matter-folder cleanup;
- client onboarding logistics;
- scheduling or administrative coordination;
- SharePoint / Clio / Lexaro / Gmail hygiene;
- matter status cleanup, service-definition cleanup, or dashboard maintenance;
- delegation to Sonia, Laura, Joy, Threcia, a clerk, or another team member.

An LL Task can support a Legal Task, but it should not be described as a Legal
Task unless substantive legal judgment or legal-service work is actually
required.

## Monitoring point

An **ML1 monitoring point** is a matter-linked signal that ML1 must keep visible
and check against live context.

It is stronger than background noise, but weaker than a concluded Legal Task.

Examples:

- a client may respond;
- correspondence may need to be sent by mail;
- a counterparty has asked for call times;
- a draft exists but its legal next step is not yet determined;
- an accounting or trust-record issue is matter-linked and may affect client
  handling;
- a reporting deadline, docketing gap, or routing anomaly needs visibility.

Monitoring points may later become ML1 Tasks, Legal Tasks, or LL Tasks after
review.

## Relationship between task types

| Type | Who owns it | What it means | Requires legal judgment? |
| --- | --- | --- | --- |
| ML1 Task | ML1 | ML1 must decide, review, do, approve, or monitor | Sometimes |
| Legal Task | Legal service provider / ML1-supervised lawyer | Substantive legal work must be done | Yes |
| LL Task | Levine Law operating system / team | Firm, admin, routing, finance, docketing, coordination, or support work | Not necessarily |
| ML1 monitoring point | ML1 visibility layer | Matter signal must stay visible pending judgment | Not yet determined |

The system must not collapse these categories into each other.

## Matter Index doctrine

`05_MATTERS/DASHBOARDS/MATTER_INDEX.md` is the canonical matter tracking table.

It answers:

- what matters exist;
- how they are classified;
- what their current delivery / fulfillment posture is;
- what services are known to the system;
- where to look next.

It does not answer:

- what ML1 must do today;
- what exact Legal Task must be performed;
- whether ML1 has failed to do something;
- whether a document is substantively good;
- whether client work is complete;
- whether a matter is being handled correctly.

The Matter Index is an inventory and classification artifact.

## Matter Digest doctrine

`05_MATTERS/DASHBOARDS/MATTER_DIGEST.md` is the ML1-facing handling and
visibility rollup.

It answers:

- what matters must be handled or checked based on emails, calendar,
  SharePoint, Clio, and Lexaro signals;
- what matters are active, watched, stalled, unmapped, or missing service
  definitions;
- what signals require ML1 visibility or routing review.

It does not answer:

- what exact Legal Task must be taken;
- whether ML1 has failed to do something;
- whether a draft is substantively good;
- what the actual next legal step is.

Those require looking at the matter folder, recent emails, attachments, live
client context, and ML1 judgment.

## System behavior rules

- Dashboard flags are prompts for review, not legal conclusions.
- A digest item may mean "matter must be handled" without deciding the legal
  step.
- Use "ML1 monitoring point" where visibility is required but legal next steps
  are not yet determined.
- Use "ML1 Task" only where ML1 personally must decide, review, approve, do, or
  monitor.
- Use "Legal Task" only where substantive legal-service work has been identified.
- Use "LL Task" for firm/admin/team/system work, even if matter-linked.
- Do not evaluate ML1 performance from dashboard metadata alone.
- Do not infer document quality without reviewing the document or comments.
- Do not infer client/counterparty posture without reviewing recent live
  correspondence.
- When uncertain, state the artifact level: tracking signal, monitoring point,
  ML1 Task, LL Task, or Legal Task.
