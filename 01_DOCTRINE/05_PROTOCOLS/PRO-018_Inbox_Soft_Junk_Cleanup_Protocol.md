---
id: PRO-018
title: Inbox Soft Junk Cleanup Protocol
owner: ML1
status: approved
approval: ML1
approved_by: ML1
approved_date: 2026-04-18
project: LLP-006
version: 0.1
effective_date: 2026-04-18
supersedes:
provenance:
  decided_by: ML1
  decided_on: 2026-04-18
  context: Metadata normalized by system admin cleanup on 2026-05-24
created_date: 2026-03-14
last_updated: 2026-03-23
tags: [protocol, gmail, inbox, cleanup, soft-junk]
---

# PRO-018 — Inbox Soft Junk Cleanup Protocol

Enforces Policy: POL-042

> **DRAFT — PENDING ML1 APPROVAL.**
> This protocol has not been approved and is not in effect.
> No cleanup operations, inbox removal, or bulk sender execution may be run
> under this protocol until ML1 approves and sets `status: approved`.

---

## 1. Purpose

This protocol governs the inbox admin lane for non-matter cleanup.

It defines:

1. how soft-junk candidates are identified
2. the matter-first rule that prevents cleanup from overriding matter routing
3. the confirmed sender cleanup lists used for bulk cleanup
4. the approval and audit requirements for inbox cleanup actions

This protocol is separate from `PRO-014`, which governs inbox state and matter
management.

---

## 2. Scope

This protocol applies to Gmail inbox cleanup for:

- `matthew@levinelegal.ca`
- `matthew@levine-law.ca`

It governs:

- category-driven soft-junk review
- confirmed sender cleanup lists
- ML1-directed trash and archive cleanup operations

It does not govern:

- canonical state labels
- matter label structure
- matter-routing logic
- state exclusivity enforcement

Those are governed by `PRO-014`.

---

## 3. Terminology

| Term | Definition |
|------|------------|
| **Soft junk** | Non-matter inbox content that is low-value, promotional, social, forum-based, or otherwise cleanup-oriented rather than matter-related. |
| **Soft-junk cleanup candidate** | A thread reported for cleanup review under this protocol. Reporting does not itself authorize inbox removal. |
| **Confirmed noise sender** | A sender or sender group that ML1 has designated as trash-class. |
| **Confirmed archive sender** | A sender or sender group that ML1 has designated as archive-class. |

---

## 4. Identification Rules

### 4.1 Matter-first rule

Inbox cleanup must never override matter management.

Before a category-driven cleanup action is proposed:

1. Check whether the thread already carries a canonical matter label.
2. Check whether the thread deterministically resolves to an active matter using
   the approved matter-routing signals from `PRO-014`.
3. If the thread belongs to a matter, route it back into the `PRO-014` lane for
   matter and state handling.
4. Only non-matter threads may proceed as cleanup candidates under this protocol.

### 4.2 Gmail category-driven soft junk

Gmail category labels are cleanup signals only. They are not evidence that a
thread has already been classified.

If a thread is:

- in `INBOX`
- carries `CATEGORY_PROMOTIONS`, `CATEGORY_SOCIAL`, `CATEGORY_UPDATES`, or `CATEGORY_FORUMS`
- and does not belong to a matter

then it should be reported as a **soft-junk cleanup candidate**.

Default action:

- report only
- do not archive
- do not delete
- do not remove `INBOX`

### 4.3 Confirmed noise senders (trash-class)

The following senders have been confirmed as noise by ML1 (2026-03-14). Emails from these
senders may be trashed during cleanup operations.

- `support@systemsandteams.com`
- `news@bizbuysell.com`
- `noreply@medium.com`, `newsletters@medium.com`, `hello@medium.com`
- `david.a@plantationsinternational.com`
- `notifications@account.brilliant.org`
- `bettiegram@backofficebetties.com`
- `email@e.lucid.co`
- `noreply@skool.com`
- `iwoszapar@user.luma-mail.com`
- `support@epicnetwork.com`
- `info@vivaglobal.us`
- `communications@riskintelligence.lseg.com`
- `communications@bnaibrith.ca`
- `sales@infowisesolutions.com`
- `team@weargustin.com`
- `Windows365@mails.microsoft.com`
- `teamzoom@zoom.us`
- `customer-success-advisor@zoom.us`
- `noreply@youtube.com`
- `no-reply@mail.instagram.com`
- `TDSurvey@feedback-td.com`
- `notification@promo.bitget.com`
- `talent@eq.tm.intuit.com`
- `newsletters@audible.com`
- `vaclav@vibetoexit.com`
- `Microsoft365@mails.microsoft.com`
- `lexisnexis@us.confirmit.com`
- `kelsey@digitalmainstreet.ca`
- `hello@render.com`

### 4.4 Confirmed archive senders (archive-class)

The following senders have been confirmed as low-value but retainable by ML1 (2026-03-14).
Emails from these senders may be archived during cleanup operations.

- `messaging@promo.lexisnexis.ca`, `experts@lawpay.info`
- `info@ontario-commercial.com`, `support@ontario-commercial.com`
- `marketing@getappara.ai`
- `bruna@legalboards.com`
- `inquiries-portagemaadvisory.ca@shared1.ccsend.com`
- `dbaskin@baskinwealth.com`
- `jprekaski@fbc.ca`
- `notifications-noreply@linkedin.com`, `linkedin@e.linkedin.com`,
  `messages-noreply@linkedin.com`, `jobs-listings@linkedin.com`
- `hello@bighand.com`
- `Jacob@updates.creme.digital`
- `MyClaw@aisecret.us`
- `jordan@e-stateplanner.com`
- `tsytner@villageshul.com`
- `calendar-notification@google.com`
- `no-reply@zoom.us`
- `email@e.email-td.com`
- `noreply@tdinsurance.com`
- `bmoalerts@bmo.com`
- `no-reply@asana.com`
- `noreply@donotreply.soulpepper.com`
- `no-reply@notifications.myassembly.com`
- `marlon.misra@assembly.com`
- `auto-confirm@amazon.ca`
- `notifications@clio.com`
- `microsoft-noreply@microsoft.com`
- `donotreply@upwork.com`
- `gmail-noreply@google.com`
- `drive-shares-dm-noreply@google.com`
- `reply@donotreply.soulpepper.com`
- `notify@payments.interac.ca`
- `catch@payments.interac.ca`
- `passwordreset@bmo.com`
- `bmo.authentication@bmo.com`
- `cpd@lso.ca`
- `room_44a0487a0182b6b1939be978a19d7b11@email.upwork.com`
- `customer-service@asana.com`
- `communication.preferences@communcations.lseg.com`
- `upwork@t.upwork.com`
- `bankconnections@quickbooks.intuit.com`
- `billing@zoom.us`
- `americanexpress@welcome.americanexpress.com`
- `hello@email.pipedrive.com`
- `td.estatementnoreplyaccount@td.com`
- `google-workspace-alerts-noreply@google.com`
- `message@adobe.com`
- `communications@lawpro.ca`
- `noreply@notifications.hubspot.com`
- `noreply-onlineaccess@td.com`
- `no_reply@notifications.intuit.com`
- `hi@mail.bcsos.club`
- `bschwartz@baskinwealth.com`
- `no-reply@account.canva.com`
- `donotreply@regus.com`
- `no-reply@zoom.us`
- `noreply@mail.hellosign.com`
- `td.esignnoreplyaccount@td.com`
- `weeklybrief@chainalysis.com`
- `webmaster@ontariobusinesscentral.ca`
- `td.wealth@td.com`
- `email@goodlifefitnessemail.com`
- `no-reply@sharepointonline.com`
- `customercomments@e.quickbooks.intuit.ca`
- `info@pipedrive.com`
- `tdapply@td.com`
- `ontarioreports@lexisnexis.ca`
- `workspace-noreply@google.com`
- `businessprofile-noreply@google.com`
- `no-reply@accounts.google.com`
- `outlook_cd4321b6a7502c1d@outlook.com`
- `mailer-daemon@googlemail.com`
- `map@homewoodhealth.com`
- `billing@hubspot.com`
- `recruiting@jobalerts.opentext.com`
- `autodebit.notification@lexisnexis.com`
- `ecards@vividgreetings.com`
- `ads-noreply@google.com`
- `sandra@mymarketerteam.com`
- `noreply-lsoconnects@lso.ca`
- `communications@lsbc.org`
- `room_9fef0404288cd30dd54a2bb953907582@email.upwork.com`
- `hey@jasper.ai`
- `steve@parrbusinesslaw.com`
- `registration@lsbc.org`
- `info@flexlegalnetwork.com`
- `ebill@bell.ca`
- `ca-merchantservices@email.clover.com`
- `do-not-reply@lso.ca`
- `receipt@moneris.com`
- `msonlineservicesteam@microsoftonline.com`
- `help@alfcloud.ca`
- `noreplyoffersrenewals@bmo.com`
- `fipa@fipa.bc.ca`
- `edgarems@substack.com`
- `security@mail.zapier.com`
- `noreply@pipedrive.com`
- `info@cira.ca`
- `info@torontoisraelitech.com`
- `help@alfcentral.com`
- `campaign@campaign.lawtrainings.com`
- `support@smith.ai`
- `support+chat-ai@smith.ai`
- `noreply@upwork.com`
- `room_5a241a2b68a109b5c64b4201901b80e0@email.upwork.com`
- `no_reply@communications.paypal.com`
- `office@villageshul.com`
- `toronto@policesolutions.ca`
- `noreply@tradingview.com`
- `analytics-noreply@google.com`
- `do-not-reply@market.envato.com`
- `welcome@apaylo.com`
- `room_28432681546512338666738039157560@upwork.com`
- `aurelie_tran@intuit.com`
- `info@wrk.com`
- `payments-noreply@google.com`
- `team@email.anthropic.com`
- `learn@email1.asana.com`
- `matthew@levinelegal.ca`
- `npi.einvoice.notification@lexisnexis.com`
- `hello@tradingview.com`
- `accounts@lc.soulpepper.com`
- `executiveassistant@e.read.ai`
- `team@dabblewriter.com`
- `info@poshmark.com`
- `shop@poshmark.com`
- `notifications@stripe.com`
- `return@amazon.ca`
- `payments-messages@amazon.ca`
- `equityevents@lso.ca`
- `dgrant@villageshul.com`
- `no-reply@shulcloud.com`
- `communications@lso.ca`
- `support@reply.clio.com`
- `chat-noreply@google.com`
- `alerts@lexisnexis.com`
- `noreply@luminpdf.com`
- `powerplat-noreply@microsoft.com`
- `no-reply@canva.com`
- `resolution@aircanada.econciliador.com`
- `do-not-reply@amazon.com`
- `account-update@amazon.ca`
- `noreply@lawpro.ca`
- `no-reply@business.amazon.ca`
- `design.research@bmo.com`
- `info@realaltinvestments.com`
- `mike@divinecaviar.com`
- `noreply@sf-notifications.com`
- `noreply@info.wise.com`
- `talent@intuit.com`
- `bryce.hedrick@chainalysis.com`
- `room_30421827209e396f88436134daf73f37@email.upwork.com`
- `hello@news.gemini.com`
- `noreply-marketplace@zoom.us`
- `noreply@dyedurham.com`
- `no-reply@myaccounts.lawpro.ca`
- `marketing@ownr.co`
- `dse@camail.docusign.net`
- `vote@simplyvoting.com`
- `product-team@hubspot.com`
- `rmcdonald@baskinwealth.com`
- `nihonpolitics@substack.com`
- `tdappointment-noreply@td.com`
- `steveparr@user.luma-mail.com`
- `no-reply@chainalysis.com`
- `lawsociety@lsbc.org`
- `ads-account-noreply@google.com`
- `customercare.serviceclient1@aircanada.ca`
- `events@weirfoulds.com`
- `emea@mail.docusign.com`
- `alerts@jobalerts.opentext.com`
- `noreply@opentext.com`
- `info@digitalmainstreet.ca`
- `andria@caef.ca`
- `room_0c1dcaec0203bad86678e32466f95219@email.upwork.com`
- `room_9653c29c9f847ca6c42568e9c925b551@email.upwork.com`
- `room_88212d1312630c77d4f2db58ef3e7c56@email.upwork.com`
- `no-reply-billing@hubspot.com`
- `no-reply@feedback.google.com`
- `wordpress@nikkodiscovery.com`
- `wordpress@studentrights.site`
- `alexis@kyrosaml.com`
- `info@comms.bell.ca`
- `greenvelope@invites.greenvelope.com`
- `room_0600f83fd0c8e5c64305c41a4f909adb@email.upwork.com`
- `rolandfrasier@epicnetwork.com`
- `messaging@lexisnexis.ca`
- `docusign@e.docusign.com`
- `room_e602e94583218071a55d2a4be973909e@email.upwork.com`
- `annual.giving@give.svc.ubc.ca`
- `room_d049978aba6951f55f32494523b79f58@email.upwork.com`
- `contact@leonenapoli.com`
- `accounts@macushlaw.ca`
- `alumni@allard.ubc.ca`
- `ebay@ebay.com`
- `room_e5d9104864cd642f373f0f60ceb04e5e@email.upwork.com`
- `noreply@td.com`
- `gemini-notes@google.com`
- `email@e.godaddy.com`
- `no-reply@agoda.com`
- `jeremy.g@icomplyis.com`
- `kurt@spellbook.legal`
- `googleads-research-noreply@google.com`
- `wordpress@mtt.lxh.temporary.site`
- `notifications@summaryai.app`
- `ertdgf34534577324@gmail.com`
- `forwarding-noreply@google.com`
- `baskin.portal@inf-systems.ca`
- `michael@get.gosingularitylawyer.com`
- `john.martinez@smbteam.com`
- `no-reply@fathom.video`
- `newuser@nuwelcome.ebay.com`
- `donotreply@goodlifefitness.com`
- `docs@email.pandadoc.net`
- `no-reply@dropbox.com`
- `jeromeocampo@xwf.google.com`
- `powerautomate@mails.microsoft.com`
- `msftpromo-noreply@microsoft.com`
- `noreply@tm.openai.com`
- `confirmation@bell.ca`
- `no_reply@bell.ca`
- `noreply@bell.ca`
- `noreply@validation.bell.ca`
- `work@mercor.com`
- `wordpress@castleviewsolutions.com`
- `wordpress@matthewajlevine.com`
- `orders@divinecaviar.com`
- `map@lso.ca`
- `toshi@e-housing.jp`
- `info@travel.priceline.com`
- `room_082501b49a2721bd4335923aeb1e6186@email.upwork.com`
- `room_08c31fe47124425d69d6673f562582ff@email.upwork.com`
- `donotreply@amazon.com`
- `room_6ecc5e617344b395d473367a96daaa91@email.upwork.com`
- `room_89c78cdac6a2323e480d0440ab63ca4c@email.upwork.com`
- `ivan@mail.notion.so`
- `marketing@dyedurham.com`
- `support@figma.com`
- `mail@sf-notifications.com`
- `prime@amazon.com`
- `order-update@amazon.ca`
- `ngalimski@bbgvf.com`
- `alumni@alumni.svc.ubc.ca`
- `no-reply@otter.ai`
- `amexgms@feedbackemail.americanexpress.com`
- `donotreply@appleexpress.com`
- `success=levinelegal.ca@hubspotstarter.hs-send.com`
- `notice@app.lucid.co`
- `room_e1ad5599aabf63dd91d7aee74333feeb@email.upwork.com`
- `team@mercor.com`
- `david@plantationsinternational.co`
- `yener@virtuallatinos.com`
- `security@mail.instagram.com`
- `onlinebankingforbusiness@bmo.com`
- `policyconsultation@lso.ca`
- `quickbooks@notification.intuit.com`
- `noreply@notifications.transactional.hubspot.com`
- `room_850ce3daf0855ab0f0ba00e4464c161c@email.upwork.com`
- `info@soulpepper.com`
- `kelsey@digitalmainstreet.ca`
- `googlecloud@google.com`
- `cloudplatform-noreply@google.com`
- `bmogc@service-now.com`
- `tdtdctpr@td.com`
- `hello@lawschool2-0.com`
- `clio@delighted.com`
- `webinars@e.lucid.co`
- `noreply@google.com`
- `thehubspotteam@hubspot.com`
- `notifications@discord.com`
- `msa@communication.microsoft.com`
- `signers@e-signlive.ca`
- `noreply@booking.com`
- `info@tcae.ca`
- `room_7a770c30455ae01fe2c24892c2944211@email.upwork.com`
- `billing@clio.com`
- `customer.support@td.com`
- `donotreply.nepasrepondre@aircanada.ca`
- `confirmation@aircanada.ca`
- `notifications@united.com`
- `notifications@agoda-messaging.com`
- `customer.service@booking.com`
- `no-reply-esta2@cbp.dhs.gov`
- `googlepay-noreply@google.com`
- `noreply-iam@booking.com`
- `no_reply@jp-den.jp`
- `support@e-signlive.ca`
- `notification@notification.aircanada.ca`
- `magazine_subline@subline.jp`
- `communications@info.aircanada.com`
- `room_f1bf5634cc3c3ebbbb06a41d34ff1d66@email.upwork.com`
- `support@wifi-cloud.jp`
- `value@accelerator.university`
- `emails@e.hostgator.com`
- `support@subline.jp`
- `digital-no-reply@amazon.ca`
- `wordpress@levine-law.ca`
- `docusign@mail.docusign.com`
- `noreply@github.com`
- `no-reply@northpass.com`
- `notification@promo1.bitget.com`
- `replies@tonyrobbins.com`
- `hello@notifications.iwoszapar.com`
- `telus@connect.telus.com`
- `noreply@email.openai.com`
- `teamtonyrobbins@tonyrobbins.com`
- `marketing@kiocafe.com`
- `bmo.experience@bmo.com`
- `noreply@notifications.elliptic.co`
- `grace+levine-law.ca@donotreply.soulpepper.com`
- `no-reply@riverside-fm.comeet-notifications.com`
- `kendall@riverside.fm`
- `cashandcarried@substack.com`
- `no-reply@amazon.com`
- `invoice+statements@mail.anthropic.com`
- `telusservice@i.telus.com`
- `noreply@telus.com`
- `cbenedek@villageshul.com`
- `td.webbroker@td.com`
- `activation.no.reply.tm@telus.com`
- `hey@git.law`
- `support@ownr.co`
- `amirklein@substack.com`
- `hello@chatprd.ai`
- `matthew+levinelegal.ca@donotreply.soulpepper.com`
- `hello@chess.com`
- `marcom@riverside.fm`
- `donotreply@e.godaddy.com`
- `service@send001.mail.bitget.com`
- `accounts+matthewajlevine.com@donotreply.soulpepper.com`
- `no-reply@mercor.com`
- `matej@vibetoexit.com`
- `noreply@receipts.tlaonline.ca`
- `notifications@riverside.fm`
- `invitations@alignable.com`
- `noreply@order.eventbrite.com`
- `account.helpdesk@regus.com`
- `scheduler@comeet-notifications.com`
- `notifications@riverside-fm.comeet-notifications.com`
- `googledev-noreply@google.com`
- `globalmba@bbs.unibo.it`
- `sales@sasigns.ca`
- `notification@slack.com`
- `notifications@github.com`
- `info@lrostaffing.com`
- `angela@soulpepper.com`
- `support@insightful.io`
- `room_a02f21c8e380dd8ab86be3dab0e2ee80@email.upwork.com`
- `noreply@wise.com`
- `print@promo.lexisnexis.ca`
- `no-reply@github.com`
- `help@instaheadshots.com`
- `hello@connect.joinlegalvantage.com`
- `no-reply-9oennkiskdsmxqgueu7raw@mail.anthropic.com`
- `notifications@link.com`
- `renewals@godaddy.com`
- `s@sunnylenarduzzi.co`
- `contact@mail.replit.com`
- `marketresearch@lexisnexis.ca`
- `marketing@assembly.com`
- `room_9c408576d14386329c1871947faa70e5@email.upwork.com`
- `room_a54200b82381ecc898175976a5405a7c@email.upwork.com`
- `room_55a35584d4744f94ae8ea624f8db5beb@email.upwork.com`
- `s@authority.io`
- `s@sunnylenarduzzi.com`
- `alisandaoelpha2000+gmail.com@lc.ghlpilipinas.com`
- `bmotps.communication@tps.bmo.com`
- `support@vibetoexit.com`
- `room_9459a85a521a3cc894091967942ba1e4@email.upwork.com`
- `tdcathas@td.com`
- `feedback@slack.com`
- `dusan.vuksanovic@lexisnexis.ca`
- `jamesstruthers@substack.com`
- `room_42101526472067935878718322206305@upwork.com`
- `service@intl.paypal.com`
- `do-not-reply-canada@fiserv.com`
- `room_52825740484226209600323841625834@upwork.com`
- `support@soulpepper.com`
- `qbo@intuit.com`
- `do_not_reply@intuit.com`
- `communications@acinfo.aircanada.com`
- `info@primafact.com`
- `room_66110465206659091267682326119866@upwork.com`
- `experts@email.affinipay.com`
- `workspacesupport@feedback.google.com`
- `workspacesupport@google.com`
- `replyto@email.microsoft.com`
- `room_81987293662825059737125812421868@upwork.com`
- `starbucks@giftcards.starbucks.com`
- `room_20134978956130859755073533412692@upwork.com`
- `travelinsurance@allianz-assistance.ca`
- `no-reply@hubspot.com`
- `noreply@legal-updates.wetransfer.com`
- `hp@iwgplc.com`
- `kevin@soulpepper.com`
- `no-reply@bdc.ca`
- `reconcile_report_noreplydev@e-customer-service.com`
- `adam.franklin@bluewiremedia.com.au`
- `bmo.confirmation@bmo.com`
- `jeanfrancois@wrk.com`
- `security-noreply@linkedin.com`
- `room_58462794916992226713348346990637@upwork.com`
- `practicalainvestor@substack.com`
- `room_66389138466760141896120632176979@upwork.com`
- `newsletters@audible.ca`
- `trygve@hey.databutton.com`
- `room_11448317148503463320838430013214@upwork.com`
- `adam@reply.bluewiremedia.com.au`
- `room_91157419677656808063016565538563@upwork.com`
- `contact@dubaidebtcollection.com`
- `george@dataspike.io`
- `activity@notifications.paperos.com`
- `room_10014270866160643198994106422109@upwork.com`
- `noreply@qemailserver.com`
- `qbocaresupport@intuit.com`
- `no-reply@slack.com`
- `support@notification.learnformula.com`
- `info@leonenapoli.com`
- `room_10696427214190098137443035641530@upwork.com`
- `room_68853099088879818255919662214416@upwork.com`
- `taina@legalboards.com`
- `no_response@intuit.com`
- `billing@email1.asana.com`
- `room_49208391569648405868341455273305@upwork.com`
- `microsoft365@information.microsoft.com`
- `adobesign@adobesign.com`
- `info@spacelist.co`
- `room_61888948804083308032501246220554@upwork.com`
- `powerautomatenoreply@microsoft.com`
- `noreply@wetransfer.com`
- `membership@bizbuysell.com`
- `derek@copyhour.com`
- `notifications@learnupon.com`
- `store+56549966000@g.shopifyemail.com`
- `noreply@surveys-sondages.edc.ca`
- `experts@updates.lawpay.com`
- `googleads-noreply@google.com`
- `noreply@redditmail.com`
- `tina.gill@lexisnexis.ca`
- `forms-receipts-noreply@google.com`

---

## 5. Execution Rules

### 5.1 Default mode

The default mode for soft-junk cleanup is proposal-only.

Proposal outputs may include:

- thread id
- sender
- subject
- Gmail category labels
- cleanup class (`soft_junk`, `trash_class`, `archive_class`)

### 5.2 Prohibited actions without explicit instruction

Without explicit ML1 instruction, the system must not:

- archive a soft-junk cleanup candidate
- trash a soft-junk cleanup candidate
- delete any message
- remove `INBOX`

### 5.3 ML1-directed cleanup execution

ML1 may authorize direct cleanup execution for:

- confirmed noise senders
- confirmed archive senders
- explicitly approved soft-junk cleanup candidate sets
- category sweep of pre-2026-01-01 inbox threads (via `execute_category_sweep`)

### 5.4 Category sweep execution path

`execute_category_sweep` is a governed bulk cleanup tool that:

1. Queries inbox for threads before 2026-03-01 carrying `CATEGORY_PROMOTIONS`,
   `CATEGORY_SOCIAL`, `CATEGORY_UPDATES`, or `CATEGORY_FORUMS`
2. Skips any thread with a canonical matter label (matter-first rule)
3. Archives all remaining threads (removes `INBOX`)
4. Extracts sender email addresses from archived threads
5. Appends new senders to §4.4 (archive-class) in this file
6. Appends new senders to `ARCHIVE_QUERIES` in `scripts/gmail_mcp_server.py`

Date cutoff (`before:2026/3/1`) is fixed by ML1 directive and must not be removed or extended without ML1 approval.
The tool may be run multiple times to process batches of up to 500 threads.

Such operations must be logged to:

- `06_RUNS/logs/inbox_cleanup.log`
- any applicable Gmail audit artifact for the execution path used
- substantive review / approval / execution artifacts under
  `06_RUNS/INBOX_GOVERNANCE/PRO-018_SOFT_JUNK/`

---

## 6. Audit and Review

Cleanup reviews should retain:

- the query used
- the candidate set generated
- the approval reference, if execution occurred
- the execution counts for trash/archive actions

Canonical storage location for substantive `PRO-018` artifacts:

- `06_RUNS/INBOX_GOVERNANCE/PRO-018_SOFT_JUNK/reviews/`
- `06_RUNS/INBOX_GOVERNANCE/PRO-018_SOFT_JUNK/approvals/`
- `06_RUNS/INBOX_GOVERNANCE/PRO-018_SOFT_JUNK/executions/`

If a thread later proves to belong to a matter, cleanup routing must stop and the
thread must be handled under `PRO-014`.

---

## 7. Related Doctrine

- `POL-042` Inbox Governance Policy
- `PRO-014` Inbox State and Matter Management Protocol

---

## 8. Change Log

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-03-14 | Initial split-out protocol for inbox soft-junk cleanup. Separates category-driven cleanup and confirmed sender cleanup from `PRO-014`. |
| 0.2 | 2026-03-23 | Added 4 trash-class senders (Bitget, Intuit talent, Audible, VibetToExit) and 3 archive-class senders (BigHand, Creme Digital, MyClaw) from promotions/updates scan. ML1 approved. |
| 0.3 | 2026-03-23 | Added CATEGORY_UPDATES to §4.2 scope. Added §5.4 category sweep execution path. New `execute_category_sweep` tool: archives pre-2026/1/1 category-tagged non-matter inbox threads and auto-populates archive sender lists. |
| 0.4 | 2026-03-24 | Added 4 trash-class senders (Microsoft365, LexisNexis Confirmit survey, Digital Main Street, Render) and 4 archive-class senders (eState Planner, Village Shul, Google Calendar notifications, Zoom Clips). ML1 approved. |
| 0.5 | 2026-03-24 | Extended category sweep date cutoff from before:2026/1/1 to before:2026/3/1 per ML1 directive. |
