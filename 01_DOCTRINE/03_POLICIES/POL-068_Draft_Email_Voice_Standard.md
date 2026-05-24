---
id: POL-068
title: Draft Email Voice Standard
owner: ML1
status: approved
approval: ML1
approved_by: ML1
approved_date: 2026-04-20
version: 0.1
effective_date: 2026-04-20
supersedes:
provenance:
  decided_by: ML1
  decided_on: 2026-04-20
  context: Metadata normalized by system admin cleanup on 2026-05-24
created_date: 2026-04-20
last_updated: 2026-04-20
tags: [policy, gmail, drafts, voice, correspondence, communication]
---

# POL-068: Draft Email Voice Standard

Policy Statement: All Gmail draft emails produced by ML2 agents or Claude must conform to the voice standard defined in this policy. Voice governs register, tone, salutation, signature, and structure. No draft may be pushed to Gmail without conforming to this standard.

Authority (Principles referenced): PRN-003, PRN-004

Related policies: POL-042 (Inbox Governance Policy, governs draft creation and send prohibition)

---

## 1. Policy Purpose

This policy governs the voice and style of outbound email drafts composed by the System on ML1 direction.

The purpose is to ensure that system-authored drafts:
- Sound like ML1, not a language model
- Are appropriate to the recipient relationship and context
- Are ready to send or minimally adjusted by ML1
- Never contain hedging, filler, or boilerplate that ML1 would delete

---

## 2. Scope

This policy applies to:
- All draft emails created via the `create_draft` Gmail MCP tool
- All draft emails created by any ML2 agent or Claude session
- All email content composed for ML1 review regardless of the channel it enters Gmail

This policy does not govern:
- Internal ML2 system messages or agent outputs
- Clio notes or matter record entries
- Document drafts (letters, agreements, memos)

---

## 3. General Register

| Principle | Rule |
|---|---|
| Direct | Lead with the point. No warm-up sentence. |
| Short | Prefer short paragraphs. One idea per paragraph. |
| Plain | No legalese in client-facing emails unless quoting statute or contract. |
| Active voice | Prefer active. Avoid passive constructions. |
| Canadian spelling | Use Canadian/British spelling: "favour", "defence", "licence" (noun), "license" (verb), "analyse", "colour". |
| No filler | Never: "I hope this email finds you well", "Please don't hesitate to reach out", "As per my previous email". |
| No em dash | Never use em dashes (--). Use a comma, colon, or recast the sentence. |
| No hedging | Never qualify advice with "you may want to consider" or "it might be worth thinking about" unless the uncertainty is real and must be communicated. |

---

## 4. Salutation Standard

| Recipient relationship | Salutation |
|---|---|
| Established client (prior substantive exchange) | `Hey [First name],` |
| New client or first substantive exchange | `Hi [First name],` |
| Opposing counsel | `Hi [First name],` or `Dear [Mr./Ms. Last name],` depending on relationship |
| Court or tribunal | `Dear [Title],` |
| Regulatory body | `Dear [Title/Name],` |
| Referral source or professional contact | `Hi [First name],` |

Do not use: "To Whom It May Concern", "Dear Sir/Madam", "Hello [Full name]".

---

## 5. Signature Block

All drafts use the following signature block exactly:

```
[closing]
Matthew
```

**Closing word by context:**

| Context | Closing |
|---|---|
| Standard client correspondence | `Regards` |
| Warm or established client relationship | `Best regards` or `Best` |
| Brief or transactional reply | `Thanks` |
| Formal or adversarial context | `Yours truly` |

No firm name, phone number, or disclaimer in the signature unless ML1 explicitly directs it. The full firm signature block is ML1's prerogative to add before sending.

---

## 6. Structure

**Short replies (under ~100 words):** Prose only. No headers or bullets unless listing items.

**Substantive advice emails:** Use bullets or numbered lists for multi-item advice. Bold key terms or regulatory names on first reference. No headers unless the email is exceptionally long.

**Holding or acknowledgement replies:** One to three sentences. No bullets. State the action being taken and the timeline if known.

**Chase / follow-up emails:** Brief. Reference the prior communication in one clause. State what is needed. Close.

---

## 7. Prohibited Content

The following must never appear in a system-authored draft:

- Unsolicited legal disclaimers ("This email does not constitute legal advice...")
- "Please see attached" without an attachment reference that ML1 can verify
- References to the system or AI ("I've prepared this draft...", "As an AI...")
- Promises of a specific outcome
- Statements of absolute legal certainty on unsettled questions
- Offers to send, forward, or copy anyone without ML1 direction

---

## 8. Contextual Calibration

When drafting, the System must use available context to calibrate the draft:

| Signal | Calibration |
|---|---|
| Prior thread tone (client used first name, informal) | Match informality |
| Prior thread tone (formal, titles used) | Match formality |
| Matter type (litigation/adversarial) | Tighten language; avoid warmth |
| Matter type (transactional/advisory) | Professional warmth acceptable |
| Holding reply (advice not yet ready) | Brevity mandatory; no substance |
| Chase email | Assertive but not aggressive |

---

## 9. Open Items

| ID | Item |
|----|------|
| NTD-1 | Confirm salutation rule for opposing counsel: is first name always acceptable? |
| NTD-2 | Confirm whether firm signature block should ever be auto-appended |
| NTD-3 | Define voice rules for marketing or business development emails (currently out of scope) |

---

## 10. Change Log

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-04-20 | Initial draft for ML1 review. Derived from observed voice in session-authored drafts (Bou Doumit, Roop, Bridgman, Malheiro). |
