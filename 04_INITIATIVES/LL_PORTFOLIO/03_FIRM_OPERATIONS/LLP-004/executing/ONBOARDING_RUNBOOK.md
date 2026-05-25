---
id: 04_initiatives_ll_portfolio_03_firm_operations_llp_004_onboarding_implementation_onboarding_runbook_md
title: Onboarding Runbook
owner: ML1
status: draft
created_date: 2026-05-18
last_updated: 2026-05-18
tags: []
---

# Onboarding Runbook

Project ID: LLP-004
Project Path: 03_FIRM_OPERATIONS/LLP-004
Stage: Implementation

## Purpose
Onboarding prepares the engagement agreement and matter records before client signature and handoff to Opening.

## Scope
### Roles
- Assigned Lawyer (AL)
- Accounts Manager (AM)
- Executive Administrator (EA)

### Systems and Materials
- SharePoint (Onboarding templates + matter folders)
- Clio (`app.clio.com`)
- Asana (Fulfillment: Admin & Accounts tracker)
- Engagement Agreement template reference

## High-Level Checklist
1. Create Clio matter in `Pending` status.
2. Create Asana matter task.
3. Create SharePoint matter folder.
4. Draft client agreement.
5. Obtain lawyer approval.
6. Send agreement for signature.
7. Confirm signed agreement stored in Clio.
8. Transition matter from Onboarding to Opening.

## Detailed Procedure
### 1) Intake Confirmation
1. Intake Coordinator or AL sends proceed-to-engage confirmation.
2. Review thread for client type and matter type/billing structure.
3. Determine template:
- Use lawyer-specified template when provided.
- Otherwise, choose by client type + matter type.
- If unclear, confirm with AL before drafting.

### 2) Create Clio Matter
1. Go to `app.clio.com` -> `Matters` -> `New Matter`.
2. Complete matter details using appropriate template.
3. Select/create client contact.
4. Assign responsible attorney (Matthew Levine).
5. Assign responsible staff (Exec Admin).
6. Set matter permissions (`Everyone`).
7. Add related contacts for corporation matters.
8. Complete custom fields:
- Matter Type
- Matter Opening
- Delivery Status
- Relevant Services
- Fulfillment Status
- Accounts Type (if applicable)
9. Set matter status to `Pending` (pre-signature state).
10. Save matter and copy Clio reference number.

### 3) Create Asana Matter Task
1. Go to Asana -> Fulfillment (Admin & Accounts) Tracker -> Onboarding.
2. Add task named `[Clio Ref] - [Client Name]`.
3. Complete required fields:
- Fulfillment Stage: Onboarding
- Matter Type
- Fulfillment Status
- Accounts Type
- Financial Readiness (AM-owned)

### 4) Create SharePoint Folder
1. Go to SharePoint onboarding matter area.
2. Select subfolder by matter type.
3. Create folder named `[Clio Ref] - [Client Name]`.
4. Store draft working documents in this folder.
5. Move/upload finalized executed agreement into Clio matter documents.

### 5) Draft Engagement Agreement
1. Open correct onboarding template in SharePoint.
2. Complete all placeholder fields (`<< >>`).
3. Save `.docx` using naming convention:
`[AgreementType]_[ClientName]_[DayMonthYear].docx`
4. Counsel-matter exception: agreement may be omitted only with explicit AL confirmation.

### 6) Review Engagement Agreement
1. In Asana, mark draft subtask complete.
2. Assign review subtask to AL.
3. Attach draft agreement.
4. Tag AL and request review.
5. Wait for approval/feedback.
6. Mark review complete only after approval evidence exists.

### 7) Send Agreement for Signature
1. In Clio matter documents, upload agreement.
2. Validate all signature fields.
3. Confirm signatory identity/email (individual or corporation signatory).
4. Send for signature and include standard message.
5. Add Matthew as CC.
6. Confirm send notification in Clio.
7. Create Clio follow-up task.

### 8) Monitor Signature and Close Onboarding
1. Track signature status daily.
2. If unsigned after 2 days, send reminder.
3. On receipt, confirm signed agreement is stored in correct Clio matter.
4. Transition Clio matter status from `Pending` to `Open`.
5. Complete Asana send/confirm subtasks.
6. Record Gate 2 completion and handoff to LLP-005 Opening.

## Controls
- No send-for-signature before AL review approval.
- Matter status remains `Pending` until signed agreement is confirmed.
- No Opening handoff before signed agreement is confirmed in Clio.
- Exceptions must be captured in Asana + Clio notes.

## Continuous Improvement
- Operations Manager may update this runbook after approved process changes.
- Feedback from AL/EA/AM is logged in `ISSUE_LOG.md` and implemented through controlled revisions.
