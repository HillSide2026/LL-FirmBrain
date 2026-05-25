---
id: 05_matters_dashboards_readme_md
title: Matter Dashboards
owner: ML1
status: generated
created_date: 2026-05-24
last_updated: 2026-05-24
tags: []
---

# Matter Dashboards

Deterministic outputs for Matter Command and Control runs.

These dashboards are **system tracking and visibility artifacts for ML1**. They
are not legal analysis, quality review, or automated task assignment.

Doctrine source: `repo://00_SYSTEM/matters/MATTER_TASK_AND_DASHBOARD_DOCTRINE.md`.

They exist to help ML1 see the matter portfolio, identify where signals may
need human review, and decide what to look at next. ML2 / Claude may use them
to orient review, but must not treat the dashboard labels as conclusions about
what ML1 has or has not done.

## Relationship to LL Portfolio

LL is organized at the top level around the numbered `LL_PORTFOLIO` program
structure, not around individual matters.

These matter dashboards provide the fast drill-down layer from that top-level
LL operating picture into the matter portfolio. Use them when ML1 needs to
shift from program/project review into client-service urgency, fulfillment
status, matter handling, WIP conversion, LL task load, or matter-level
bottlenecks.

The matter portfolio is a control surface inside the LL operating system. It is
not a replacement for the `LL_PORTFOLIO` program structure.

## Role of the matter index

`MATTER_INDEX.md` is the canonical matter tracking table. It shows the current
matter universe known to the repo and the runner, including:

- matter number and client/matter name;
- open/closed status;
- delivery classification;
- fulfillment/status posture;
- service definitions, where known;
- source pointer back to the matter folder.

The index answers: **what matters exist, how are they classified, and where do
we look next?**

The index does not answer: **what should ML1 do today, whether a legal document
is correct, whether a matter is actually neglected, or whether client work is
substantively complete.**

## Role of the matter digest

`MATTER_DIGEST.md` is the ML1-facing daily/periodic visibility layer. It rolls
up the matter index into queues and exception lists, including:

- active/watch/other matter groupings;
- service-definition gaps;
- inbox/linkage anomalies;
- unmapped or stale signals;
- generated escalation candidates.

The digest answers: **what matters must be handled, based on emails, calendar,
SharePoint, and Clio / Lexaro signals.**

The digest does not answer: **what exact legal steps must be taken, whether ML1
has failed to do something, whether a draft is substantively good, or what the
actual next legal step is.** Those require looking at the matter folder, recent
emails, attachments, live client context, and ML1 judgment.

## Use discipline

- Treat dashboard flags as prompts for review, not conclusions.
- Use **ML1 monitoring point** for a matter-linked signal that ML1 must keep
  visible, but where the exact legal step still requires matter-folder,
  email-thread, attachment, client-context, or ML1 judgment.
- Check the matter folder, recent email thread, attachments, and any live client
  context before stating a next action.
- Distinguish "tracking signal" from "legal/document analysis".
- Distinguish "possible ML1 review item" from "confirmed ML1 task".
- Avoid evaluating ML1's work from dashboard metadata alone.
- Drafting an email or checklist may be appropriate where the live thread
  supports it, but substantive document review requires the actual document or
  comments.

Primary Slice 1/2 outputs:

- `MATTER_INDEX.md`
- `MATTER_DIGEST.md`
- `INBOX_UNMAPPED.md`
- `SHAREPOINT_GAPS.md`

Commercial / profitability overlay:

- `CLIENT_DEMAND_PROFITABILITY_REVIEW.md` is the ML1-facing overlay for
  separating real client demand from stale, speculative, internal, or
  collection-risk work. It should be read with
  `../LL_TASK_TRACKER.md#client-demand--profitability-intake` before drawing
  conclusions about matter pressure or firm profitability.

Current manual overlay:

- `STANDARD_MATTER_REVIEW_2026-05-13.md` consolidates Standard-delivery
  ML1 monitoring points that require visibility but not automatic legal
  conclusions.

Canonical matter index:

- `MATTER_INDEX.md` is the current matter index.
- `../INDEX.md` is deprecated and retained only as a pointer.

Slice 3+ placeholders:

- `DEADLINE_RADAR.md`
