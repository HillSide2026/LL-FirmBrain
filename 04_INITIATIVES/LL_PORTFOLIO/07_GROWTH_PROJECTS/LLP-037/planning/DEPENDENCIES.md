---
id: llp_037_ll_system_design__planning__dependencies_md
title: LLP-037 LL System Design - Dependencies
owner: ML1
status: draft
created_date: 2026-05-25
last_updated: 2026-05-25
tags: [llp-037, system-design, dependencies]
---

# Dependencies

| Dependency | Role |
|---|---|
| Lexora sync model | Determines matter/task data flow and source-of-truth boundaries |
| Legal Work System candidate decision | Determines document-generation and work-execution architecture |
| ll-corporate and ll-corporate-records | Downstream product and document delivery surfaces |
| Mayan API contract | Document ingestion and storage boundary |
| LLP-038 Delivery Spine | Defines delivery workflow that system tooling must support |
