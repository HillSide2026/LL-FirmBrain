---
id: 04_initiatives_ll_portfolio_03_firm_operations_llp_004_onboarding_implementation_qa_checklist_md
title: QA Checklist
owner: ML1
status: draft
created_date: 2026-05-18
last_updated: 2026-05-18
tags: []
---

# QA Checklist

Project ID: LLP-004
Project Path: 03_FIRM_OPERATIONS/LLP-004_ONBOARDING
Stage: Implementation

## Intake Confirmation
- [ ] Proceed-to-engage confirmation email received from Intake Coordinator or Assigned Lawyer.
- [ ] Email thread reviewed for client type (individual/corporation).
- [ ] Email thread reviewed for matter type/billing structure (hourly, retainer, flat fee, other).
- [ ] Required agreement template determined.
- [ ] If template unclear, clarification request sent to Assigned Lawyer before drafting.

## Clio Matter Setup
- [ ] Matter created in Clio (`Matters` -> `New Matter`).
- [ ] Correct matter template selected based on matter type.
- [ ] Client contact selected or created.
- [ ] Responsible attorney set to Matthew Levine.
- [ ] Responsible staff set to Exec Admin.
- [ ] Matter permissions set to Everyone.
- [ ] Matter status set to `Pending` (pre-signature).
- [ ] Related contacts added for corporation matters.
- [ ] Custom fields completed: matter type, matter opening, delivery status, relevant services, fulfillment status, accounts type.
- [ ] Clio reference number copied and recorded.

## Asana Setup
- [ ] Task created in Fulfillment (Admin & Accounts) Tracker -> Onboarding.
- [ ] Task naming standard followed: `[Clio Ref] - [Client Name]`.
- [ ] Required fields completed: fulfillment stage, matter type, fulfillment status, accounts type, financial readiness.

## SharePoint Setup
- [ ] Matter folder created under correct matter-type subfolder.
- [ ] Folder naming matches Asana task name.
- [ ] Draft working documents saved in SharePoint folder.

## Agreement Drafting
- [ ] Correct onboarding template selected.
- [ ] All placeholder fields (`<< >>`) completed.
- [ ] Draft saved as `.docx` using naming convention.
- [ ] Counsel matter check completed (agreement may be bypassed only with AL-confirmed exception).

## Lawyer Review
- [ ] `DRAFT: Engagement Agreement` subtask completed.
- [ ] `REVIEW: Engagement Agreement` assigned to Assigned Lawyer.
- [ ] Draft attached to review subtask.
- [ ] Review request comment added tagging Assigned Lawyer.
- [ ] Lawyer approval evidence captured before send step.

## Send for Signature
- [ ] Agreement uploaded to correct Clio matter documents.
- [ ] Signature fields inserted for each required signatory.
- [ ] Signer identity verified (individual vs corporate signatory).
- [ ] Standard outbound message used and Matthew added as CC.
- [ ] Clio confirmation of signature request captured.
- [ ] Follow-up task created in Clio.

## Signature Follow-up and Confirmation
- [ ] Signature status monitored daily.
- [ ] Reminder sent if unsigned after 2 days.
- [ ] Signed agreement receipt confirmed.
- [ ] Signed agreement confirmed stored and accessible in Clio.
- [ ] Asana send/confirm subtasks marked complete.

## Stage Transition (Onboarding -> Opening)
- [ ] Gate 2 condition met: signed engagement confirmed.
- [ ] Clio matter status transitioned `Pending` -> `Open` after signature confirmation.
- [ ] Handoff packet complete for LLP-005 Opening.
- [ ] Transition recorded in Asana and Clio notes.

## Final QA Result
- QA Reviewer: ______________________
- Date: ______________________
- Result: [Pass | Hold | Rework Required]
- Notes: ______________________
