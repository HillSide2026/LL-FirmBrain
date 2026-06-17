#!/usr/bin/env python3
"""
Gmail MCP Server — LL Second Brain
==================================
Native MCP access for Gmail, bounded to the same governed access surface as the
repo's Gmail scripts.

ACCESS POLICY (per ML1 directive):
  - Proposal-first for interactive mailbox work.
  - Controlled writes are permitted only for explicit label application tools.
  - Write tools require approved_by, approval_artifact, and reason.
  - No broader permissions than the existing Gmail script workflows.
  - Sending is permanently prohibited. No send_message tool may be added (POL-042 §7).

PERMITTED OPERATIONS:
  1. list_messages            — list message stubs using Gmail query semantics
  2. get_message              — fetch one message by id
  3. list_threads             — list thread stubs using Gmail query semantics
  4. get_thread               — fetch one thread by id
  5. list_labels              — list mailbox labels
  6. apply_state_label        — apply one canonical state label to a thread
  7. apply_matter_label       — apply one canonical matter label to a thread
  8. apply_matter_label_query — apply one canonical matter label to all threads
                                 matching a Gmail query
  9. create_draft             — create a Gmail draft (optionally threaded reply)

Python 3.9 compatible. No external MCP SDK required.
Implements MCP JSON-RPC 2.0 stdio transport manually.
"""

from __future__ import annotations

import base64
import email.mime.multipart
import email.mime.text
import json
import logging
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional


_REPO_ROOT = Path(__file__).resolve().parents[1]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))
_GMAIL_GOVERNANCE_DIR = _REPO_ROOT / "gmail_governance"
if str(_GMAIL_GOVERNANCE_DIR) not in sys.path:
    sys.path.insert(0, str(_GMAIL_GOVERNANCE_DIR))

try:
    from dotenv import load_dotenv

    load_dotenv(_REPO_ROOT / ".env")
except ImportError:
    pass

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


CANONICAL_STATE_LABELS = {
    "00_Triage",
    "10_Action_Matthew",
    "20_Action_Team",
    "30_Waiting_External",
    "40_Replied_Awaiting_Response",
    "50_Calendar",
    "60_Filing",
    "70_Filed",
    "80_Junk_to_Review",
    "90_Archive",
}
LEGACY_STATE_LABEL_ALIASES = {
    "08_Junk_to_Review": "80_Junk_to_Review",
    "80_Junk (Pending Review)": "80_Junk_to_Review",
}

MATTER_TIER_PREFIXES = {"LL/1./1.1/", "LL/1./1.2/", "LL/1./1.3/", "LL/1./1.4/"}
MATTER_LEAF_PATTERN = re.compile(r"^(\d{2,3}-\d{2,5}(?:-\d{5})?)\b")
VALID_MESSAGE_FORMATS = {"minimal", "metadata", "full", "raw"}

OPS_DIR = _REPO_ROOT / "06_RUNS" / "ops"
AUDIT_LOG = OPS_DIR / "gmail_mcp_audit.ndjson"
LOG_DIR = _REPO_ROOT / "06_RUNS" / "logs"
CLEANUP_LOG = LOG_DIR / "inbox_cleanup.log"

BATCH_SIZE = 1000

TRASH_QUERIES = [
    "in:inbox from:support@systemsandteams.com",
    "in:inbox from:news@bizbuysell.com",
    "in:inbox from:(noreply@medium.com OR newsletters@medium.com OR hello@medium.com)",
    "in:inbox from:david.a@plantationsinternational.com",
    "in:inbox from:notifications@account.brilliant.org",
    "in:inbox from:bettiegram@backofficebetties.com",
    "in:inbox from:email@e.lucid.co",
    "in:inbox from:noreply@skool.com",
    "in:inbox from:iwoszapar@user.luma-mail.com",
    "in:inbox from:support@epicnetwork.com",
    "in:inbox from:info@vivaglobal.us",
    "in:inbox from:communications@riskintelligence.lseg.com",
    "in:inbox from:communications@bnaibrith.ca",
    "in:inbox from:sales@infowisesolutions.com",
    "in:inbox from:team@weargustin.com",
    "in:inbox from:Windows365@mails.microsoft.com",
    "in:inbox from:teamzoom@zoom.us",
    "in:inbox from:customer-success-advisor@zoom.us",
    "in:inbox from:noreply@youtube.com",
    "in:inbox from:no-reply@mail.instagram.com",
    "in:inbox from:TDSurvey@feedback-td.com",
    "in:inbox from:notification@promo.bitget.com",
    "in:inbox from:talent@eq.tm.intuit.com",
    "in:inbox from:newsletters@audible.com",
    "in:inbox from:vaclav@vibetoexit.com",
    "in:inbox from:Microsoft365@mails.microsoft.com",
    "in:inbox from:lexisnexis@us.confirmit.com",
    "in:inbox from:kelsey@digitalmainstreet.ca",
    "in:inbox from:hello@render.com",
]

ARCHIVE_QUERIES = [
    "in:inbox from:(messaging@promo.lexisnexis.ca OR experts@lawpay.info)",
    "in:inbox from:(info@ontario-commercial.com OR support@ontario-commercial.com)",
    "in:inbox from:marketing@getappara.ai",
    "in:inbox from:bruna@legalboards.com",
    "in:inbox from:inquiries-portagemaadvisory.ca@shared1.ccsend.com",
    "in:inbox from:dbaskin@baskinwealth.com",
    "in:inbox from:jprekaski@fbc.ca",
    "in:inbox from:(notifications-noreply@linkedin.com OR linkedin@e.linkedin.com OR messages-noreply@linkedin.com OR jobs-listings@linkedin.com)",
    "in:inbox from:hello@bighand.com",
    "in:inbox from:Jacob@updates.creme.digital",
    "in:inbox from:MyClaw@aisecret.us",
    "in:inbox from:jordan@e-stateplanner.com",
    "in:inbox from:tsytner@villageshul.com",
    "in:inbox from:calendar-notification@google.com",
    "in:inbox from:no-reply@zoom.us",
    "in:inbox from:email@e.email-td.com",
    "in:inbox from:noreply@tdinsurance.com",
    "in:inbox from:bmoalerts@bmo.com",
    "in:inbox from:no-reply@asana.com",
    "in:inbox from:noreply@donotreply.soulpepper.com",
    "in:inbox from:no-reply@notifications.myassembly.com",
    "in:inbox from:marlon.misra@assembly.com",
    "in:inbox from:auto-confirm@amazon.ca",
    "in:inbox from:notifications@clio.com",
    "in:inbox from:microsoft-noreply@microsoft.com",
    "in:inbox from:donotreply@upwork.com",
    "in:inbox from:gmail-noreply@google.com",
    "in:inbox from:drive-shares-dm-noreply@google.com",
    "in:inbox from:reply@donotreply.soulpepper.com",
    "in:inbox from:notify@payments.interac.ca",
    "in:inbox from:catch@payments.interac.ca",
    "in:inbox from:passwordreset@bmo.com",
    "in:inbox from:bmo.authentication@bmo.com",
    "in:inbox from:cpd@lso.ca",
    "in:inbox from:room_44a0487a0182b6b1939be978a19d7b11@email.upwork.com",
    "in:inbox from:customer-service@asana.com",
    "in:inbox from:communication.preferences@communcations.lseg.com",
    "in:inbox from:upwork@t.upwork.com",
    "in:inbox from:bankconnections@quickbooks.intuit.com",
    "in:inbox from:billing@zoom.us",
    "in:inbox from:americanexpress@welcome.americanexpress.com",
    "in:inbox from:hello@email.pipedrive.com",
    "in:inbox from:td.estatementnoreplyaccount@td.com",
    "in:inbox from:google-workspace-alerts-noreply@google.com",
    "in:inbox from:message@adobe.com",
    "in:inbox from:communications@lawpro.ca",
    "in:inbox from:noreply@notifications.hubspot.com",
    "in:inbox from:noreply-onlineaccess@td.com",
    "in:inbox from:no_reply@notifications.intuit.com",
    "in:inbox from:hi@mail.bcsos.club",
    "in:inbox from:bschwartz@baskinwealth.com",
    "in:inbox from:no-reply@account.canva.com",
    "in:inbox from:donotreply@regus.com",
    "in:inbox from:no-reply@zoom.us",
    "in:inbox from:noreply@mail.hellosign.com",
    "in:inbox from:td.esignnoreplyaccount@td.com",
    "in:inbox from:weeklybrief@chainalysis.com",
    "in:inbox from:webmaster@ontariobusinesscentral.ca",
    "in:inbox from:td.wealth@td.com",
    "in:inbox from:email@goodlifefitnessemail.com",
    "in:inbox from:no-reply@sharepointonline.com",
    "in:inbox from:customercomments@e.quickbooks.intuit.ca",
    "in:inbox from:info@pipedrive.com",
    "in:inbox from:tdapply@td.com",
    "in:inbox from:ontarioreports@lexisnexis.ca",
    "in:inbox from:workspace-noreply@google.com",
    "in:inbox from:businessprofile-noreply@google.com",
    "in:inbox from:no-reply@accounts.google.com",
    "in:inbox from:outlook_cd4321b6a7502c1d@outlook.com",
    "in:inbox from:mailer-daemon@googlemail.com",
    "in:inbox from:map@homewoodhealth.com",
    "in:inbox from:billing@hubspot.com",
    "in:inbox from:recruiting@jobalerts.opentext.com",
    "in:inbox from:autodebit.notification@lexisnexis.com",
    "in:inbox from:ecards@vividgreetings.com",
    "in:inbox from:ads-noreply@google.com",
    "in:inbox from:sandra@mymarketerteam.com",
    "in:inbox from:noreply-lsoconnects@lso.ca",
    "in:inbox from:communications@lsbc.org",
    "in:inbox from:room_9fef0404288cd30dd54a2bb953907582@email.upwork.com",
    "in:inbox from:hey@jasper.ai",
    "in:inbox from:steve@parrbusinesslaw.com",
    "in:inbox from:registration@lsbc.org",
    "in:inbox from:info@flexlegalnetwork.com",
    "in:inbox from:ebill@bell.ca",
    "in:inbox from:ca-merchantservices@email.clover.com",
    "in:inbox from:do-not-reply@lso.ca",
    "in:inbox from:receipt@moneris.com",
    "in:inbox from:msonlineservicesteam@microsoftonline.com",
    "in:inbox from:help@alfcloud.ca",
    "in:inbox from:noreplyoffersrenewals@bmo.com",
    "in:inbox from:fipa@fipa.bc.ca",
    "in:inbox from:edgarems@substack.com",
    "in:inbox from:security@mail.zapier.com",
    "in:inbox from:noreply@pipedrive.com",
    "in:inbox from:info@cira.ca",
    "in:inbox from:info@torontoisraelitech.com",
    "in:inbox from:help@alfcentral.com",
    "in:inbox from:campaign@campaign.lawtrainings.com",
    "in:inbox from:support@smith.ai",
    "in:inbox from:support+chat-ai@smith.ai",
    "in:inbox from:noreply@upwork.com",
    "in:inbox from:room_5a241a2b68a109b5c64b4201901b80e0@email.upwork.com",
    "in:inbox from:no_reply@communications.paypal.com",
    "in:inbox from:office@villageshul.com",
    "in:inbox from:toronto@policesolutions.ca",
    "in:inbox from:noreply@tradingview.com",
    "in:inbox from:analytics-noreply@google.com",
    "in:inbox from:do-not-reply@market.envato.com",
    "in:inbox from:welcome@apaylo.com",
    "in:inbox from:room_28432681546512338666738039157560@upwork.com",
    "in:inbox from:aurelie_tran@intuit.com",
    "in:inbox from:info@wrk.com",
    "in:inbox from:payments-noreply@google.com",
    "in:inbox from:team@email.anthropic.com",
    "in:inbox from:learn@email1.asana.com",
    "in:inbox from:matthew@levinelegal.ca",
    "in:inbox from:npi.einvoice.notification@lexisnexis.com",
    "in:inbox from:hello@tradingview.com",
    "in:inbox from:accounts@lc.soulpepper.com",
    "in:inbox from:executiveassistant@e.read.ai",
    "in:inbox from:team@dabblewriter.com",
    "in:inbox from:info@poshmark.com",
    "in:inbox from:shop@poshmark.com",
    "in:inbox from:notifications@stripe.com",
    "in:inbox from:return@amazon.ca",
    "in:inbox from:payments-messages@amazon.ca",
    "in:inbox from:equityevents@lso.ca",
    "in:inbox from:dgrant@villageshul.com",
    "in:inbox from:no-reply@shulcloud.com",
    "in:inbox from:communications@lso.ca",
    "in:inbox from:support@reply.clio.com",
    "in:inbox from:chat-noreply@google.com",
    "in:inbox from:alerts@lexisnexis.com",
    "in:inbox from:noreply@luminpdf.com",
    "in:inbox from:powerplat-noreply@microsoft.com",
    "in:inbox from:no-reply@canva.com",
    "in:inbox from:resolution@aircanada.econciliador.com",
    "in:inbox from:do-not-reply@amazon.com",
    "in:inbox from:account-update@amazon.ca",
    "in:inbox from:noreply@lawpro.ca",
    "in:inbox from:no-reply@business.amazon.ca",
    "in:inbox from:design.research@bmo.com",
    "in:inbox from:info@realaltinvestments.com",
    "in:inbox from:mike@divinecaviar.com",
    "in:inbox from:noreply@sf-notifications.com",
    "in:inbox from:noreply@info.wise.com",
    "in:inbox from:talent@intuit.com",
    "in:inbox from:bryce.hedrick@chainalysis.com",
    "in:inbox from:room_30421827209e396f88436134daf73f37@email.upwork.com",
    "in:inbox from:hello@news.gemini.com",
    "in:inbox from:noreply-marketplace@zoom.us",
    "in:inbox from:noreply@dyedurham.com",
    "in:inbox from:no-reply@myaccounts.lawpro.ca",
    "in:inbox from:marketing@ownr.co",
    "in:inbox from:dse@camail.docusign.net",
    "in:inbox from:vote@simplyvoting.com",
    "in:inbox from:product-team@hubspot.com",
    "in:inbox from:rmcdonald@baskinwealth.com",
    "in:inbox from:nihonpolitics@substack.com",
    "in:inbox from:tdappointment-noreply@td.com",
    "in:inbox from:steveparr@user.luma-mail.com",
    "in:inbox from:no-reply@chainalysis.com",
    "in:inbox from:lawsociety@lsbc.org",
    "in:inbox from:ads-account-noreply@google.com",
    "in:inbox from:customercare.serviceclient1@aircanada.ca",
    "in:inbox from:events@weirfoulds.com",
    "in:inbox from:emea@mail.docusign.com",
    "in:inbox from:alerts@jobalerts.opentext.com",
    "in:inbox from:noreply@opentext.com",
    "in:inbox from:info@digitalmainstreet.ca",
    "in:inbox from:andria@caef.ca",
    "in:inbox from:room_0c1dcaec0203bad86678e32466f95219@email.upwork.com",
    "in:inbox from:room_9653c29c9f847ca6c42568e9c925b551@email.upwork.com",
    "in:inbox from:room_88212d1312630c77d4f2db58ef3e7c56@email.upwork.com",
    "in:inbox from:no-reply-billing@hubspot.com",
    "in:inbox from:no-reply@feedback.google.com",
    "in:inbox from:wordpress@nikkodiscovery.com",
    "in:inbox from:wordpress@studentrights.site",
    "in:inbox from:alexis@kyrosaml.com",
    "in:inbox from:info@comms.bell.ca",
    "in:inbox from:greenvelope@invites.greenvelope.com",
    "in:inbox from:room_0600f83fd0c8e5c64305c41a4f909adb@email.upwork.com",
    "in:inbox from:rolandfrasier@epicnetwork.com",
    "in:inbox from:messaging@lexisnexis.ca",
    "in:inbox from:docusign@e.docusign.com",
    "in:inbox from:room_e602e94583218071a55d2a4be973909e@email.upwork.com",
    "in:inbox from:annual.giving@give.svc.ubc.ca",
    "in:inbox from:room_d049978aba6951f55f32494523b79f58@email.upwork.com",
    "in:inbox from:contact@leonenapoli.com",
    "in:inbox from:accounts@macushlaw.ca",
    "in:inbox from:alumni@allard.ubc.ca",
    "in:inbox from:ebay@ebay.com",
    "in:inbox from:room_e5d9104864cd642f373f0f60ceb04e5e@email.upwork.com",
    "in:inbox from:noreply@td.com",
    "in:inbox from:gemini-notes@google.com",
    "in:inbox from:email@e.godaddy.com",
    "in:inbox from:no-reply@agoda.com",
    "in:inbox from:jeremy.g@icomplyis.com",
    "in:inbox from:kurt@spellbook.legal",
    "in:inbox from:googleads-research-noreply@google.com",
    "in:inbox from:wordpress@mtt.lxh.temporary.site",
    "in:inbox from:notifications@summaryai.app",
    "in:inbox from:ertdgf34534577324@gmail.com",
    "in:inbox from:forwarding-noreply@google.com",
    "in:inbox from:baskin.portal@inf-systems.ca",
    "in:inbox from:michael@get.gosingularitylawyer.com",
    "in:inbox from:john.martinez@smbteam.com",
    "in:inbox from:no-reply@fathom.video",
    "in:inbox from:newuser@nuwelcome.ebay.com",
    "in:inbox from:donotreply@goodlifefitness.com",
    "in:inbox from:docs@email.pandadoc.net",
    "in:inbox from:no-reply@dropbox.com",
    "in:inbox from:jeromeocampo@xwf.google.com",
    "in:inbox from:powerautomate@mails.microsoft.com",
    "in:inbox from:msftpromo-noreply@microsoft.com",
    "in:inbox from:noreply@tm.openai.com",
    "in:inbox from:confirmation@bell.ca",
    "in:inbox from:no_reply@bell.ca",
    "in:inbox from:noreply@bell.ca",
    "in:inbox from:noreply@validation.bell.ca",
    "in:inbox from:work@mercor.com",
    "in:inbox from:wordpress@castleviewsolutions.com",
    "in:inbox from:wordpress@matthewajlevine.com",
    "in:inbox from:orders@divinecaviar.com",
    "in:inbox from:map@lso.ca",
    "in:inbox from:toshi@e-housing.jp",
    "in:inbox from:info@travel.priceline.com",
    "in:inbox from:room_082501b49a2721bd4335923aeb1e6186@email.upwork.com",
    "in:inbox from:room_08c31fe47124425d69d6673f562582ff@email.upwork.com",
    "in:inbox from:donotreply@amazon.com",
    "in:inbox from:room_6ecc5e617344b395d473367a96daaa91@email.upwork.com",
    "in:inbox from:room_89c78cdac6a2323e480d0440ab63ca4c@email.upwork.com",
    "in:inbox from:ivan@mail.notion.so",
    "in:inbox from:marketing@dyedurham.com",
    "in:inbox from:support@figma.com",
    "in:inbox from:mail@sf-notifications.com",
    "in:inbox from:prime@amazon.com",
    "in:inbox from:order-update@amazon.ca",
    "in:inbox from:ngalimski@bbgvf.com",
    "in:inbox from:alumni@alumni.svc.ubc.ca",
    "in:inbox from:no-reply@otter.ai",
    "in:inbox from:amexgms@feedbackemail.americanexpress.com",
    "in:inbox from:donotreply@appleexpress.com",
    "in:inbox from:success=levinelegal.ca@hubspotstarter.hs-send.com",
    "in:inbox from:notice@app.lucid.co",
    "in:inbox from:room_e1ad5599aabf63dd91d7aee74333feeb@email.upwork.com",
    "in:inbox from:team@mercor.com",
    "in:inbox from:david@plantationsinternational.co",
    "in:inbox from:yener@virtuallatinos.com",
    "in:inbox from:security@mail.instagram.com",
    "in:inbox from:onlinebankingforbusiness@bmo.com",
    "in:inbox from:policyconsultation@lso.ca",
    "in:inbox from:quickbooks@notification.intuit.com",
    "in:inbox from:noreply@notifications.transactional.hubspot.com",
    "in:inbox from:room_850ce3daf0855ab0f0ba00e4464c161c@email.upwork.com",
    "in:inbox from:info@soulpepper.com",
    "in:inbox from:kelsey@digitalmainstreet.ca",
    "in:inbox from:googlecloud@google.com",
    "in:inbox from:cloudplatform-noreply@google.com",
    "in:inbox from:bmogc@service-now.com",
    "in:inbox from:tdtdctpr@td.com",
    "in:inbox from:hello@lawschool2-0.com",
    "in:inbox from:clio@delighted.com",
    "in:inbox from:webinars@e.lucid.co",
    "in:inbox from:noreply@google.com",
    "in:inbox from:thehubspotteam@hubspot.com",
    "in:inbox from:notifications@discord.com",
    "in:inbox from:msa@communication.microsoft.com",
    "in:inbox from:signers@e-signlive.ca",
    "in:inbox from:noreply@booking.com",
    "in:inbox from:info@tcae.ca",
    "in:inbox from:room_7a770c30455ae01fe2c24892c2944211@email.upwork.com",
    "in:inbox from:billing@clio.com",
    "in:inbox from:customer.support@td.com",
    "in:inbox from:donotreply.nepasrepondre@aircanada.ca",
    "in:inbox from:confirmation@aircanada.ca",
    "in:inbox from:notifications@united.com",
    "in:inbox from:notifications@agoda-messaging.com",
    "in:inbox from:customer.service@booking.com",
    "in:inbox from:no-reply-esta2@cbp.dhs.gov",
    "in:inbox from:googlepay-noreply@google.com",
    "in:inbox from:noreply-iam@booking.com",
    "in:inbox from:no_reply@jp-den.jp",
    "in:inbox from:support@e-signlive.ca",
    "in:inbox from:notification@notification.aircanada.ca",
    "in:inbox from:magazine_subline@subline.jp",
    "in:inbox from:communications@info.aircanada.com",
    "in:inbox from:room_f1bf5634cc3c3ebbbb06a41d34ff1d66@email.upwork.com",
    "in:inbox from:support@wifi-cloud.jp",
    "in:inbox from:value@accelerator.university",
    "in:inbox from:emails@e.hostgator.com",
    "in:inbox from:support@subline.jp",
    "in:inbox from:digital-no-reply@amazon.ca",
    "in:inbox from:wordpress@levine-law.ca",
    "in:inbox from:docusign@mail.docusign.com",
    "in:inbox from:noreply@github.com",
    "in:inbox from:no-reply@northpass.com",
    "in:inbox from:notification@promo1.bitget.com",
    "in:inbox from:replies@tonyrobbins.com",
    "in:inbox from:hello@notifications.iwoszapar.com",
    "in:inbox from:telus@connect.telus.com",
    "in:inbox from:noreply@email.openai.com",
    "in:inbox from:teamtonyrobbins@tonyrobbins.com",
    "in:inbox from:marketing@kiocafe.com",
    "in:inbox from:bmo.experience@bmo.com",
    "in:inbox from:noreply@notifications.elliptic.co",
    "in:inbox from:grace+levine-law.ca@donotreply.soulpepper.com",
    "in:inbox from:no-reply@riverside-fm.comeet-notifications.com",
    "in:inbox from:kendall@riverside.fm",
    "in:inbox from:cashandcarried@substack.com",
    "in:inbox from:no-reply@amazon.com",
    "in:inbox from:invoice+statements@mail.anthropic.com",
    "in:inbox from:telusservice@i.telus.com",
    "in:inbox from:noreply@telus.com",
    "in:inbox from:cbenedek@villageshul.com",
    "in:inbox from:td.webbroker@td.com",
    "in:inbox from:activation.no.reply.tm@telus.com",
    "in:inbox from:hey@git.law",
    "in:inbox from:support@ownr.co",
    "in:inbox from:amirklein@substack.com",
    "in:inbox from:hello@chatprd.ai",
    "in:inbox from:matthew+levinelegal.ca@donotreply.soulpepper.com",
    "in:inbox from:hello@chess.com",
    "in:inbox from:marcom@riverside.fm",
    "in:inbox from:donotreply@e.godaddy.com",
    "in:inbox from:service@send001.mail.bitget.com",
    "in:inbox from:accounts+matthewajlevine.com@donotreply.soulpepper.com",
    "in:inbox from:no-reply@mercor.com",
    "in:inbox from:matej@vibetoexit.com",
    "in:inbox from:noreply@receipts.tlaonline.ca",
    "in:inbox from:notifications@riverside.fm",
    "in:inbox from:invitations@alignable.com",
    "in:inbox from:noreply@order.eventbrite.com",
    "in:inbox from:account.helpdesk@regus.com",
    "in:inbox from:scheduler@comeet-notifications.com",
    "in:inbox from:notifications@riverside-fm.comeet-notifications.com",
    "in:inbox from:googledev-noreply@google.com",
    "in:inbox from:globalmba@bbs.unibo.it",
    "in:inbox from:sales@sasigns.ca",
    "in:inbox from:notification@slack.com",
    "in:inbox from:notifications@github.com",
    "in:inbox from:info@lrostaffing.com",
    "in:inbox from:angela@soulpepper.com",
    "in:inbox from:support@insightful.io",
    "in:inbox from:room_a02f21c8e380dd8ab86be3dab0e2ee80@email.upwork.com",
    "in:inbox from:noreply@wise.com",
    "in:inbox from:print@promo.lexisnexis.ca",
    "in:inbox from:no-reply@github.com",
    "in:inbox from:help@instaheadshots.com",
    "in:inbox from:hello@connect.joinlegalvantage.com",
    "in:inbox from:no-reply-9oennkiskdsmxqgueu7raw@mail.anthropic.com",
    "in:inbox from:notifications@link.com",
    "in:inbox from:renewals@godaddy.com",
    "in:inbox from:s@sunnylenarduzzi.co",
    "in:inbox from:contact@mail.replit.com",
    "in:inbox from:marketresearch@lexisnexis.ca",
    "in:inbox from:marketing@assembly.com",
    "in:inbox from:room_9c408576d14386329c1871947faa70e5@email.upwork.com",
    "in:inbox from:room_a54200b82381ecc898175976a5405a7c@email.upwork.com",
    "in:inbox from:room_55a35584d4744f94ae8ea624f8db5beb@email.upwork.com",
    "in:inbox from:s@authority.io",
    "in:inbox from:s@sunnylenarduzzi.com",
    "in:inbox from:alisandaoelpha2000+gmail.com@lc.ghlpilipinas.com",
    "in:inbox from:bmotps.communication@tps.bmo.com",
    "in:inbox from:support@vibetoexit.com",
    "in:inbox from:room_9459a85a521a3cc894091967942ba1e4@email.upwork.com",
    "in:inbox from:tdcathas@td.com",
    "in:inbox from:feedback@slack.com",
    "in:inbox from:dusan.vuksanovic@lexisnexis.ca",
    "in:inbox from:jamesstruthers@substack.com",
    "in:inbox from:room_42101526472067935878718322206305@upwork.com",
    "in:inbox from:service@intl.paypal.com",
    "in:inbox from:do-not-reply-canada@fiserv.com",
    "in:inbox from:room_52825740484226209600323841625834@upwork.com",
    "in:inbox from:support@soulpepper.com",
    "in:inbox from:qbo@intuit.com",
    "in:inbox from:do_not_reply@intuit.com",
    "in:inbox from:communications@acinfo.aircanada.com",
    "in:inbox from:info@primafact.com",
    "in:inbox from:room_66110465206659091267682326119866@upwork.com",
    "in:inbox from:experts@email.affinipay.com",
    "in:inbox from:workspacesupport@feedback.google.com",
    "in:inbox from:workspacesupport@google.com",
    "in:inbox from:replyto@email.microsoft.com",
    "in:inbox from:room_81987293662825059737125812421868@upwork.com",
    "in:inbox from:starbucks@giftcards.starbucks.com",
    "in:inbox from:room_20134978956130859755073533412692@upwork.com",
    "in:inbox from:travelinsurance@allianz-assistance.ca",
    "in:inbox from:no-reply@hubspot.com",
    "in:inbox from:noreply@legal-updates.wetransfer.com",
    "in:inbox from:hp@iwgplc.com",
    "in:inbox from:kevin@soulpepper.com",
    "in:inbox from:no-reply@bdc.ca",
    "in:inbox from:reconcile_report_noreplydev@e-customer-service.com",
    "in:inbox from:adam.franklin@bluewiremedia.com.au",
    "in:inbox from:bmo.confirmation@bmo.com",
    "in:inbox from:jeanfrancois@wrk.com",
    "in:inbox from:security-noreply@linkedin.com",
    "in:inbox from:room_58462794916992226713348346990637@upwork.com",
    "in:inbox from:practicalainvestor@substack.com",
    "in:inbox from:room_66389138466760141896120632176979@upwork.com",
    "in:inbox from:newsletters@audible.ca",
    "in:inbox from:trygve@hey.databutton.com",
    "in:inbox from:room_11448317148503463320838430013214@upwork.com",
    "in:inbox from:adam@reply.bluewiremedia.com.au",
    "in:inbox from:room_91157419677656808063016565538563@upwork.com",
    "in:inbox from:contact@dubaidebtcollection.com",
    "in:inbox from:george@dataspike.io",
    "in:inbox from:activity@notifications.paperos.com",
    "in:inbox from:room_10014270866160643198994106422109@upwork.com",
    "in:inbox from:noreply@qemailserver.com",
    "in:inbox from:qbocaresupport@intuit.com",
    "in:inbox from:no-reply@slack.com",
    "in:inbox from:support@notification.learnformula.com",
    "in:inbox from:info@leonenapoli.com",
    "in:inbox from:room_10696427214190098137443035641530@upwork.com",
    "in:inbox from:room_68853099088879818255919662214416@upwork.com",
    "in:inbox from:taina@legalboards.com",
    "in:inbox from:no_response@intuit.com",
    "in:inbox from:billing@email1.asana.com",
    "in:inbox from:room_49208391569648405868341455273305@upwork.com",
    "in:inbox from:microsoft365@information.microsoft.com",
    "in:inbox from:adobesign@adobesign.com",
    "in:inbox from:info@spacelist.co",
    "in:inbox from:room_61888948804083308032501246220554@upwork.com",
    "in:inbox from:powerautomatenoreply@microsoft.com",
    "in:inbox from:noreply@wetransfer.com",
    "in:inbox from:membership@bizbuysell.com",
    "in:inbox from:derek@copyhour.com",
    "in:inbox from:notifications@learnupon.com",
    "in:inbox from:store+56549966000@g.shopifyemail.com",
    "in:inbox from:noreply@surveys-sondages.edc.ca",
    "in:inbox from:experts@updates.lawpay.com",
    "in:inbox from:googleads-noreply@google.com",
    "in:inbox from:noreply@redditmail.com",
    "in:inbox from:tina.gill@lexisnexis.ca",
    "in:inbox from:forms-receipts-noreply@google.com",
]

# Category sweep — archives inbox threads with soft-junk category labels up to ML1-approved cutoff.
# Date cutoff is fixed by ML1 directive. Do not remove or extend without ML1 approval.
# Extended from before:2026/1/1 to before:2026/3/1 by ML1 directive 2026-03-24.
CATEGORY_SWEEP_QUERY = (
    "in:inbox before:2026/3/1 "
    "(category:promotions OR category:social OR category:updates OR category:forums)"
)

_FROM_ANGLE_RE = re.compile(r"<([^>]+@[^>]+)>")
_EMAIL_RE = re.compile(r"[\w.+\-]+@[\w.\-]+")


logging.basicConfig(
    stream=sys.stderr,
    level=logging.INFO,
    format="%(asctime)sZ [%(levelname)s] gmail-mcp: %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S",
)
log = logging.getLogger("gmail_mcp")

cleanup_logger = logging.getLogger("gmail_inbox_cleanup")
cleanup_logger.setLevel(logging.INFO)
if not cleanup_logger.handlers:
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    cleanup_handler = logging.FileHandler(CLEANUP_LOG)
    cleanup_handler.setFormatter(logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    ))
    cleanup_logger.addHandler(cleanup_handler)


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _append_audit(entry: Dict[str, Any]) -> None:
    OPS_DIR.mkdir(parents=True, exist_ok=True)
    with AUDIT_LOG.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(entry, ensure_ascii=False) + "\n")


def _resolve_approval_artifact(path_text: str) -> Path:
    artifact_path = Path(path_text)
    if not artifact_path.is_absolute():
        artifact_path = _REPO_ROOT / artifact_path
    return artifact_path


def _require_write_approval(args: Dict[str, Any], tool_name: str) -> Dict[str, str]:
    approved_by = str(args.get("approved_by", "")).strip()
    approval_artifact_text = str(args.get("approval_artifact", "")).strip()
    reason = str(args.get("reason", "")).strip()

    if not approved_by:
        raise PermissionError(f"{tool_name} requires 'approved_by'.")
    if not approval_artifact_text:
        raise PermissionError(f"{tool_name} requires 'approval_artifact'.")
    if not reason:
        raise PermissionError(f"{tool_name} requires 'reason'.")

    artifact_path = _resolve_approval_artifact(approval_artifact_text)
    if not artifact_path.exists():
        raise PermissionError(f"approval_artifact not found: {artifact_path}")

    return {
        "approved_by": approved_by,
        "approval_artifact": str(artifact_path),
        "reason": reason,
    }


def _require_cleanup_authorization(args: Dict[str, Any], tool_name: str) -> Dict[str, str]:
    approved_by = str(args.get("approved_by", "")).strip()
    reason = str(args.get("reason", "")).strip()
    if not approved_by:
        raise PermissionError(f"{tool_name} requires 'approved_by'.")
    if not reason:
        raise PermissionError(f"{tool_name} requires 'reason'.")
    return {
        "approved_by": approved_by,
        "reason": reason,
    }


def _get_token_path() -> Path:
    configured = os.getenv("GOOGLE_OAUTH_TOKEN_PATH", "").strip()
    if configured:
        token_path = Path(configured)
        if not token_path.is_absolute():
            token_path = _REPO_ROOT / configured
        return token_path
    return _REPO_ROOT / "00_SYSTEM" / "local_secrets" / "google_token.json"


_GMAIL_SERVICE_CACHE: Optional[Any] = None
_GMAIL_CREDS_CACHE: Optional[Any] = None


def _get_gmail_service() -> Any:
    global _GMAIL_SERVICE_CACHE, _GMAIL_CREDS_CACHE

    # Reuse cached service if credentials are still valid.
    if _GMAIL_SERVICE_CACHE is not None and _GMAIL_CREDS_CACHE is not None:
        if not _GMAIL_CREDS_CACHE.expired:
            return _GMAIL_SERVICE_CACHE

    token_path = _get_token_path()
    if not token_path.exists():
        raise FileNotFoundError(
            f"Gmail OAuth token not found at {token_path}. "
            "Set GOOGLE_OAUTH_TOKEN_PATH or run the Gmail OAuth setup."
        )

    creds_data = json.loads(token_path.read_text())
    creds = Credentials.from_authorized_user_info(creds_data)
    if creds.expired:
        if not creds.refresh_token:
            raise RuntimeError(
                "Gmail OAuth token is expired or invalid. Re-authenticate and update credentials."
            )
        try:
            creds.refresh(Request())
            # Persist the refreshed token so the next call doesn't re-refresh.
            token_path.write_text(creds.to_json())
        except Exception as exc:
            raise RuntimeError(
                "Gmail OAuth token is expired or invalid. Re-authenticate and update credentials."
            ) from exc

    _GMAIL_CREDS_CACHE = creds
    _GMAIL_SERVICE_CACHE = build("gmail", "v1", credentials=creds)
    return _GMAIL_SERVICE_CACHE


def _with_backoff(fn: Any, context: str = "") -> Any:
    """Call fn(), retrying up to 3 times on HTTP 429/503 with exponential backoff."""
    for attempt in range(4):
        try:
            return fn()
        except HttpError as exc:
            if exc.resp.status in (429, 503) and attempt < 3:
                wait = 2 ** attempt  # 1s, 2s, 4s
                msg = f"[backoff] {context} attempt {attempt + 1} got HTTP {exc.resp.status}, retrying in {wait}s"
                print(msg, file=sys.stderr)
                _append_audit({"timestamp": _now_iso(), "event": "backoff_retry", "context": context, "attempt": attempt + 1, "status": exc.resp.status})
                time.sleep(wait)
            else:
                raise


def _list_all_labels(service: Any) -> List[Dict[str, Any]]:
    return service.users().labels().list(userId="me").execute().get("labels", [])


def _label_name_to_id(labels: List[Dict[str, Any]]) -> Dict[str, str]:
    return {str(label.get("name", "")): str(label.get("id", "")) for label in labels if label.get("name")}


def _label_id_to_name(labels: List[Dict[str, Any]]) -> Dict[str, str]:
    return {str(label.get("id", "")): str(label.get("name", "")) for label in labels if label.get("id")}


def _get_thread(service: Any, thread_id: str) -> Dict[str, Any]:
    return service.users().threads().get(userId="me", id=thread_id).execute()


def _collect_thread_label_ids(thread: Dict[str, Any]) -> List[str]:
    label_ids = set()
    for message in thread.get("messages", []):
        label_ids.update(message.get("labelIds", []))
    return sorted(label_ids)


def _find_existing_matter_label_ids(thread_label_ids: List[str], label_id_to_name: Dict[str, str]) -> List[str]:
    matter_label_ids: List[str] = []
    for label_id in thread_label_ids:
        label_name = label_id_to_name.get(label_id, "")
        if not any(label_name.startswith(prefix) for prefix in MATTER_TIER_PREFIXES):
            continue
        leaf = label_name.split("/")[-1] if "/" in label_name else label_name
        if MATTER_LEAF_PATTERN.match(leaf):
            matter_label_ids.append(label_id)
    return matter_label_ids


def _resolve_matter_label_id(
    labels: List[Dict[str, Any]],
    matter_label_name: str = "",
    matter_number: str = "",
) -> Dict[str, Any]:
    name_to_id = _label_name_to_id(labels)

    if matter_label_name:
        if matter_label_name not in name_to_id:
            raise ValueError(f"Matter label not found: {matter_label_name}")
        return {
            "matter_label_name": matter_label_name,
            "matter_label_id": name_to_id[matter_label_name],
            "resolution": "explicit_label_name",
        }

    if not matter_number:
        raise ValueError("Either 'matter_label_name' or 'matter_number' is required.")

    candidates: List[Dict[str, str]] = []
    for label in labels:
        label_name = str(label.get("name", ""))
        if not any(label_name.startswith(prefix) for prefix in MATTER_TIER_PREFIXES):
            continue
        leaf = label_name.split("/")[-1] if "/" in label_name else label_name
        match = MATTER_LEAF_PATTERN.match(leaf)
        if match and match.group(1) == matter_number:
            candidates.append({
                "matter_label_name": label_name,
                "matter_label_id": str(label.get("id", "")),
            })

    if not candidates:
        raise ValueError(f"No matter label found for matter_number '{matter_number}'.")
    if len(candidates) > 1:
        candidate_names = sorted(item["matter_label_name"] for item in candidates)
        raise ValueError(
            "Ambiguous matter_number '{}'; matching labels: {}".format(
                matter_number,
                candidate_names,
            )
        )

    resolved = candidates[0]
    resolved["resolution"] = "matter_number_lookup"
    return resolved


def _apply_thread_modify(
    service: Any,
    thread_id: str,
    add_label_ids: List[str],
    remove_label_ids: List[str],
) -> Dict[str, Any]:
    return service.users().threads().modify(
        userId="me",
        id=thread_id,
        body={
            "addLabelIds": add_label_ids,
            "removeLabelIds": remove_label_ids,
        },
    ).execute()


def _collect_message_ids_by_query(service: Any, query: str) -> List[str]:
    message_ids: List[str] = []
    page_token: Optional[str] = None

    while True:
        kwargs: Dict[str, Any] = {"userId": "me", "q": query, "maxResults": 500}
        if page_token:
            kwargs["pageToken"] = page_token

        response = service.users().messages().list(**kwargs).execute()
        message_ids.extend(str(item["id"]) for item in response.get("messages", []) if item.get("id"))
        page_token = response.get("nextPageToken")
        if not page_token:
            break

    return message_ids


def _collect_thread_ids_by_query(service: Any, query: str) -> List[str]:
    thread_ids: List[str] = []
    page_token: Optional[str] = None

    while True:
        kwargs: Dict[str, Any] = {"userId": "me", "q": query, "maxResults": 500}
        if page_token:
            kwargs["pageToken"] = page_token

        response = service.users().threads().list(**kwargs).execute()
        thread_ids.extend(str(item["id"]) for item in response.get("threads", []) if item.get("id"))
        page_token = response.get("nextPageToken")
        if not page_token:
            break

    return thread_ids


def _batch_modify_messages(
    service: Any,
    message_ids: List[str],
    add_label_ids: List[str],
    remove_label_ids: List[str],
) -> None:
    if not message_ids:
        return

    for start in range(0, len(message_ids), BATCH_SIZE):
        chunk = message_ids[start:start + BATCH_SIZE]
        service.users().messages().batchModify(
            userId="me",
            body={
                "ids": chunk,
                "addLabelIds": add_label_ids,
                "removeLabelIds": remove_label_ids,
            },
        ).execute()


def _cleanup_query_sets(scope: str) -> List[Dict[str, Any]]:
    if scope not in {"trash", "archive", "all"}:
        raise ValueError("'scope' must be one of ['trash', 'archive', 'all'].")

    query_sets: List[Dict[str, Any]] = []
    if scope in {"trash", "all"}:
        query_sets.append({
            "class": "trash",
            "queries": TRASH_QUERIES,
            "add_label_ids": ["TRASH"],
            "remove_label_ids": ["INBOX"],
        })
    if scope in {"archive", "all"}:
        query_sets.append({
            "class": "archive",
            "queries": ARCHIVE_QUERIES,
            "add_label_ids": [],
            "remove_label_ids": ["INBOX"],
        })
    return query_sets


def _preview_cleanup(scope: str) -> Dict[str, Any]:
    service = _get_gmail_service()
    preview: Dict[str, Any] = {
        "scope": scope,
        "trash_total": 0,
        "archive_total": 0,
        "queries": [],
    }

    for query_set in _cleanup_query_sets(scope):
        cleanup_class = query_set["class"]
        for query in query_set["queries"]:
            ids = _collect_message_ids_by_query(service, query)
            count = len(ids)
            preview["queries"].append({
                "class": cleanup_class,
                "query": query,
                "count": count,
            })
            if cleanup_class == "trash":
                preview["trash_total"] += count
            else:
                preview["archive_total"] += count

    preview["total"] = preview["trash_total"] + preview["archive_total"]
    return preview


def _log_cleanup_event(message: str) -> None:
    cleanup_logger.info(message)


def _extract_from_email(header_val: str) -> str:
    m = _FROM_ANGLE_RE.search(header_val)
    if m:
        return m.group(1).lower().strip()
    m2 = _EMAIL_RE.search(header_val)
    if m2:
        return m2.group(0).lower().strip()
    return ""


def _get_thread_from_email(thread: Dict[str, Any]) -> str:
    messages = thread.get("messages", [])
    if not messages:
        return ""
    headers = messages[0].get("payload", {}).get("headers", [])
    for h in headers:
        if h.get("name", "").lower() == "from":
            return _extract_from_email(h.get("value", ""))
    return ""


def _existing_sender_emails() -> set:
    emails: set = set()
    for q in TRASH_QUERIES + ARCHIVE_QUERIES:
        emails.update(m.lower() for m in _EMAIL_RE.findall(q))
    return emails


def _update_pro018_archive_senders(new_senders: List[str]) -> None:
    pro018_path = (
        _REPO_ROOT / "01_DOCTRINE" / "05_PROTOCOLS"
        / "PRO-018_Inbox_Soft_Junk_Cleanup_Protocol.md"
    )
    content = pro018_path.read_text(encoding="utf-8")
    new_lines = "\n".join(f"- `{s}`" for s in new_senders)
    marker = "\n\n---\n\n## 5."
    idx = content.find(marker)
    if idx != -1:
        content = content[:idx] + "\n" + new_lines + content[idx:]
        pro018_path.write_text(content, encoding="utf-8")


def _update_script_archive_queries(new_senders: List[str]) -> None:
    script_path = Path(__file__).resolve()
    content = script_path.read_text(encoding="utf-8")
    new_entries = "\n".join(f'    "in:inbox from:{s}",' for s in new_senders)
    pattern = re.compile(r"(^ARCHIVE_QUERIES\s*=\s*\[)(.*?)(\n\])", re.MULTILINE | re.DOTALL)

    def replacer(m: re.Match) -> str:  # type: ignore[type-arg]
        return m.group(1) + m.group(2) + "\n" + new_entries + m.group(3)

    new_content, count = pattern.subn(replacer, content)
    if count == 1:
        script_path.write_text(new_content, encoding="utf-8")


def tool_preview_inbox_cleanup(args: Dict[str, Any]) -> str:
    scope = str(args.get("scope", "all")).strip().lower() or "all"
    preview = _preview_cleanup(scope)
    return json.dumps(preview, indent=2)


def tool_preview_garbage_candidates(args: Dict[str, Any]) -> str:
    batch_size = int(args.get("batch_size", 50))
    if batch_size < 1 or batch_size > 500:
        raise ValueError("'batch_size' must be between 1 and 500.")

    import batch_classifier as governance_batch_classifier

    batch = governance_batch_classifier.generate_batch(batch_size)
    candidate_labels = {"80_Junk_to_Review", "90_Archive"}
    candidates = [
        thread
        for thread in batch.get("threads", [])
        if thread.get("proposed_label") in candidate_labels
    ]
    result = {
        "batch_id": batch.get("batch_id"),
        "batch_size": batch.get("batch_size", 0),
        "candidate_count": len(candidates),
        "junk_count": sum(1 for item in candidates if item.get("proposed_label") == "80_Junk_to_Review"),
        "archive_count": sum(1 for item in candidates if item.get("proposed_label") == "90_Archive"),
        "candidates": candidates,
    }
    return json.dumps(result, indent=2)


def tool_execute_inbox_cleanup(args: Dict[str, Any]) -> str:
    scope = str(args.get("scope", "all")).strip().lower() or "all"
    authorization = _require_cleanup_authorization(args, "execute_inbox_cleanup")
    preview = _preview_cleanup(scope)

    service = _get_gmail_service()
    run_ts = _now_iso()
    _log_cleanup_event(
        "=== inbox_cleanup START | {} | mode=MCP_EXECUTE | scope={} | approved_by={} | reason={} ===".format(
            run_ts,
            scope,
            authorization["approved_by"],
            authorization["reason"],
        )
    )

    executed_queries: List[Dict[str, Any]] = []
    for query_set in _cleanup_query_sets(scope):
        cleanup_class = query_set["class"]
        add_label_ids = query_set["add_label_ids"]
        remove_label_ids = query_set["remove_label_ids"]
        for query in query_set["queries"]:
            ids = _with_backoff(lambda q=query: _collect_message_ids_by_query(service, q), f"collect_ids:{query[:60]}")
            if ids:
                _with_backoff(lambda: _batch_modify_messages(service, ids, add_label_ids, remove_label_ids), f"batch_modify:{query[:60]}")
            _log_cleanup_event(
                "query={!r} | class={} | count={} | add={} | remove={}".format(
                    query,
                    cleanup_class,
                    len(ids),
                    add_label_ids,
                    remove_label_ids,
                )
            )
            executed_queries.append({
                "class": cleanup_class,
                "query": query,
                "count": len(ids),
            })

    result = {
        "executed_at": run_ts,
        "scope": scope,
        "trash_total": preview["trash_total"],
        "archive_total": preview["archive_total"],
        "total": preview["total"],
        "approved_by": authorization["approved_by"],
        "reason": authorization["reason"],
        "queries": executed_queries,
    }
    _log_cleanup_event(
        "=== inbox_cleanup COMPLETE | trashed={} | archived={} | mode=MCP_EXECUTE ===".format(
            result["trash_total"],
            result["archive_total"],
        )
    )
    _append_audit({
        "timestamp": run_ts,
        "tool": "execute_inbox_cleanup",
        **result,
    })
    return json.dumps(result, indent=2)


def tool_execute_category_sweep(args: Dict[str, Any]) -> str:
    authorization = _require_cleanup_authorization(args, "execute_category_sweep")
    max_threads = int(args.get("max_threads", 500))
    if max_threads < 1 or max_threads > 2000:
        raise ValueError("max_threads must be between 1 and 2000.")

    service = _get_gmail_service()
    labels = _list_all_labels(service)
    label_id_to_name = _label_id_to_name(labels)

    thread_ids = _collect_thread_ids_by_query(service, CATEGORY_SWEEP_QUERY)
    if len(thread_ids) > max_threads:
        thread_ids = thread_ids[:max_threads]

    existing = _existing_sender_emails()
    seen_senders: set = set()
    new_sender_emails: List[str] = []
    archived_ids: List[str] = []
    archived_message_ids: List[str] = []
    skipped_matter = 0
    errors: List[str] = []

    for thread_id in thread_ids:
        try:
            thread = service.users().threads().get(
                userId="me",
                id=thread_id,
                format="metadata",
                metadataHeaders=["From"],
            ).execute()
        except Exception as exc:
            errors.append(f"{thread_id}: {exc}")
            continue

        thread_label_ids = _collect_thread_label_ids(thread)
        if _find_existing_matter_label_ids(thread_label_ids, label_id_to_name):
            skipped_matter += 1
            continue

        archived_ids.append(thread_id)
        for msg in thread.get("messages", []):
            if msg.get("id"):
                archived_message_ids.append(msg["id"])

        from_email = _get_thread_from_email(thread)
        if from_email and from_email not in existing and from_email not in seen_senders:
            seen_senders.add(from_email)
            new_sender_emails.append(from_email)

    if archived_message_ids:
        _batch_modify_messages(service, archived_message_ids, [], ["INBOX"])

    if new_sender_emails:
        _update_pro018_archive_senders(new_sender_emails)
        _update_script_archive_queries(new_sender_emails)

    run_ts = _now_iso()
    result = {
        "executed_at": run_ts,
        "query": CATEGORY_SWEEP_QUERY,
        "threads_inspected": len(thread_ids),
        "archived": len(archived_ids),
        "skipped_matter": skipped_matter,
        "new_senders_added": len(new_sender_emails),
        "new_senders": new_sender_emails,
        "errors": len(errors),
        "approved_by": authorization["approved_by"],
        "reason": authorization["reason"],
    }
    _log_cleanup_event(
        f"execute_category_sweep | archived={result['archived']} | "
        f"new_senders={result['new_senders_added']} | approved_by={authorization['approved_by']}"
    )
    _append_audit({"timestamp": run_ts, "tool": "execute_category_sweep", **result})
    return json.dumps(result, ensure_ascii=False, indent=2)


def tool_resolve_confirmed_junk_threads(args: Dict[str, Any]) -> str:
    approval = _require_write_approval(args, "resolve_confirmed_junk_threads")
    thread_ids = args.get("thread_ids", [])
    if not isinstance(thread_ids, list) or not thread_ids:
        raise ValueError("'thread_ids' must be a non-empty list.")

    clean_thread_ids = [str(thread_id).strip() for thread_id in thread_ids if str(thread_id).strip()]
    if not clean_thread_ids:
        raise ValueError("'thread_ids' must contain at least one non-empty thread id.")

    service = _get_gmail_service()
    labels = _list_all_labels(service)
    name_to_id = _label_name_to_id(labels)

    if "90_Archive" not in name_to_id:
        raise ValueError("State label does not exist in Gmail: 90_Archive")

    target_label_id = name_to_id["90_Archive"]
    results: List[Dict[str, Any]] = []

    for thread_id in clean_thread_ids:
        thread = _with_backoff(lambda tid=thread_id: _get_thread(service, tid), f"resolve_junk:get_thread:{thread_id}")
        thread_label_ids = _collect_thread_label_ids(thread)
        current_state_labels = [
            label_name
            for label_name in CANONICAL_STATE_LABELS
            if name_to_id.get(label_name) in thread_label_ids
        ]
        remove_label_ids = {
            name_to_id[label_name]
            for label_name in current_state_labels
            if label_name in name_to_id
        }
        if "INBOX" in thread_label_ids:
            remove_label_ids.add("INBOX")

        no_change = (
            len(current_state_labels) == 1
            and current_state_labels[0] == "90_Archive"
            and "INBOX" not in thread_label_ids
        )

        if not no_change:
            _with_backoff(
                lambda tid=thread_id, rl=sorted(remove_label_ids): _apply_thread_modify(service, tid, [target_label_id], rl),
                f"resolve_junk:modify:{thread_id}",
            )

        result = {
            "thread_id": thread_id,
            "prior_state_labels": current_state_labels,
            "new_state_label": "90_Archive",
            "archived": True,
            "no_change": no_change,
        }
        results.append(result)
        _append_audit({
            "timestamp": _now_iso(),
            "tool": "resolve_confirmed_junk_threads",
            "approved_by": approval["approved_by"],
            "approval_artifact": approval["approval_artifact"],
            "reason": approval["reason"],
            **result,
        })

    summary = {
        "thread_count": len(results),
        "approved_by": approval["approved_by"],
        "approval_artifact": approval["approval_artifact"],
        "reason": approval["reason"],
        "results": results,
    }
    return json.dumps(summary, indent=2)


def tool_pass_a_archive_threads(args: Dict[str, Any]) -> str:
    """Pass A inbox contamination cleanup: remove INBOX from threads, preserve all existing labels."""
    approval = _require_write_approval(args, "pass_a_archive_threads")
    thread_ids = args.get("thread_ids", [])
    if not isinstance(thread_ids, list) or not thread_ids:
        raise ValueError("'thread_ids' must be a non-empty list.")

    clean_thread_ids = [str(tid).strip() for tid in thread_ids if str(tid).strip()]
    if not clean_thread_ids:
        raise ValueError("'thread_ids' must contain at least one non-empty thread id.")

    execution_artifact = str(args.get("execution_artifact", "")).strip() or \
        "06_RUNS/batch/executions/2026-05-05_inbox_contamination.json"

    service = _get_gmail_service()
    results: List[Dict[str, Any]] = []
    skipped = 0
    archived = 0

    for thread_id in clean_thread_ids:
        thread = _with_backoff(
            lambda tid=thread_id: _get_thread(service, tid),
            f"pass_a_archive:get_thread:{thread_id}",
        )
        thread_label_ids = _collect_thread_label_ids(thread)

        if "INBOX" not in thread_label_ids:
            skipped += 1
            result = {"thread_id": thread_id, "action": "skip", "reason": "not_in_inbox"}
        else:
            _with_backoff(
                lambda tid=thread_id: _apply_thread_modify(service, tid, [], ["INBOX"]),
                f"pass_a_archive:modify:{thread_id}",
            )
            archived += 1
            result = {"thread_id": thread_id, "action": "archived"}

        results.append(result)
        _append_audit({
            "timestamp": _now_iso(),
            "tool": "pass_a_archive_threads",
            "approved_by": approval["approved_by"],
            "approval_artifact": approval["approval_artifact"],
            "reason": approval["reason"],
            "execution_artifact": execution_artifact,
            **result,
        })

    execution_path = Path(_REPO_ROOT) / execution_artifact
    execution_path.parent.mkdir(parents=True, exist_ok=True)
    execution_data = {
        "run_date": _now_iso(),
        "pass": "A",
        "description": "Inbox contamination cleanup — remove INBOX label, preserve state labels",
        "approved_by": approval["approved_by"],
        "approval_artifact": approval["approval_artifact"],
        "reason": approval["reason"],
        "thread_count_submitted": len(clean_thread_ids),
        "archived": archived,
        "skipped_not_in_inbox": skipped,
        "results": results,
    }
    execution_path.write_text(json.dumps(execution_data, indent=2))

    summary = {
        "thread_count_submitted": len(clean_thread_ids),
        "archived": archived,
        "skipped_not_in_inbox": skipped,
        "execution_artifact": execution_artifact,
        "approved_by": approval["approved_by"],
    }
    return json.dumps(summary, indent=2)


def tool_apply_state_label(args: Dict[str, Any]) -> str:
    approval = _require_write_approval(args, "apply_state_label")
    thread_id = str(args.get("thread_id", "")).strip()
    state_label = str(args.get("state_label", "")).strip()

    if not thread_id:
        raise ValueError("'thread_id' is required.")
    state_label = LEGACY_STATE_LABEL_ALIASES.get(state_label, state_label)
    if state_label not in CANONICAL_STATE_LABELS:
        raise ValueError(f"'state_label' must be one of {sorted(CANONICAL_STATE_LABELS)}.")

    service = _get_gmail_service()
    labels = _list_all_labels(service)
    name_to_id = _label_name_to_id(labels)

    if state_label not in name_to_id:
        raise ValueError(f"State label does not exist in Gmail: {state_label}")

    thread = _get_thread(service, thread_id)
    thread_label_ids = _collect_thread_label_ids(thread)

    state_label_names = sorted(set(CANONICAL_STATE_LABELS).union(LEGACY_STATE_LABEL_ALIASES.keys()))
    current_state_labels = [
        label_name
        for label_name in state_label_names
        if name_to_id.get(label_name) in thread_label_ids
    ]
    remove_label_ids = [
        name_to_id[label_name]
        for label_name in current_state_labels
        if label_name in name_to_id
    ]
    target_label_id = name_to_id[state_label]

    no_change = len(current_state_labels) == 1 and current_state_labels[0] == state_label
    if not no_change:
        _apply_thread_modify(service, thread_id, [target_label_id], remove_label_ids)

    result = {
        "thread_id": thread_id,
        "prior_state_labels": current_state_labels,
        "new_state_label": state_label,
        "no_change": no_change,
        "approved_by": approval["approved_by"],
        "approval_artifact": approval["approval_artifact"],
        "reason": approval["reason"],
    }
    _append_audit({
        "timestamp": _now_iso(),
        "tool": "apply_state_label",
        **result,
    })
    return json.dumps(result, indent=2)


def tool_apply_matter_label(args: Dict[str, Any]) -> str:
    approval = _require_write_approval(args, "apply_matter_label")
    thread_id = str(args.get("thread_id", "")).strip()
    matter_label_name = str(args.get("matter_label_name", "")).strip()
    matter_number = str(args.get("matter_number", "")).strip()

    if not thread_id:
        raise ValueError("'thread_id' is required.")
    if bool(matter_label_name) == bool(matter_number):
        raise ValueError("Provide exactly one of 'matter_label_name' or 'matter_number'.")

    service = _get_gmail_service()
    labels = _list_all_labels(service)
    label_id_to_name = _label_id_to_name(labels)
    resolved = _resolve_matter_label_id(
        labels,
        matter_label_name=matter_label_name,
        matter_number=matter_number,
    )

    thread = _get_thread(service, thread_id)
    thread_label_ids = _collect_thread_label_ids(thread)
    current_matter_label_ids = _find_existing_matter_label_ids(thread_label_ids, label_id_to_name)
    current_matter_labels = [label_id_to_name[label_id] for label_id in current_matter_label_ids if label_id in label_id_to_name]

    target_label_id = resolved["matter_label_id"]
    target_label_name = resolved["matter_label_name"]

    no_change = len(current_matter_label_ids) == 1 and current_matter_label_ids[0] == target_label_id
    if not no_change:
        _apply_thread_modify(service, thread_id, [target_label_id], current_matter_label_ids)

    result = {
        "thread_id": thread_id,
        "prior_matter_labels": current_matter_labels,
        "new_matter_label": target_label_name,
        "resolution": resolved["resolution"],
        "no_change": no_change,
        "approved_by": approval["approved_by"],
        "approval_artifact": approval["approval_artifact"],
        "reason": approval["reason"],
    }
    _append_audit({
        "timestamp": _now_iso(),
        "tool": "apply_matter_label",
        **result,
    })
    return json.dumps(result, indent=2)


def tool_apply_matter_label_query(args: Dict[str, Any]) -> str:
    approval = _require_write_approval(args, "apply_matter_label_query")
    query = str(args.get("query", "")).strip()
    matter_label_name = str(args.get("matter_label_name", "")).strip()
    matter_number = str(args.get("matter_number", "")).strip()

    if not query:
        raise ValueError("'query' is required.")
    if bool(matter_label_name) == bool(matter_number):
        raise ValueError("Provide exactly one of 'matter_label_name' or 'matter_number'.")

    service = _get_gmail_service()
    labels = _list_all_labels(service)
    label_id_to_name = _label_id_to_name(labels)
    resolved = _resolve_matter_label_id(
        labels,
        matter_label_name=matter_label_name,
        matter_number=matter_number,
    )

    thread_ids = _collect_thread_ids_by_query(service, query)
    target_label_id = resolved["matter_label_id"]
    target_label_name = resolved["matter_label_name"]
    results: List[Dict[str, Any]] = []

    for thread_id in thread_ids:
        thread = _with_backoff(lambda tid=thread_id: _get_thread(service, tid), f"matter_label_query:get_thread:{thread_id}")
        thread_label_ids = _collect_thread_label_ids(thread)
        current_matter_label_ids = _find_existing_matter_label_ids(thread_label_ids, label_id_to_name)
        current_matter_labels = [
            label_id_to_name[label_id]
            for label_id in current_matter_label_ids
            if label_id in label_id_to_name
        ]

        no_change = len(current_matter_label_ids) == 1 and current_matter_label_ids[0] == target_label_id
        if not no_change:
            _with_backoff(
                lambda tid=thread_id, cml=current_matter_label_ids: _apply_thread_modify(service, tid, [target_label_id], cml),
                f"matter_label_query:modify:{thread_id}",
            )

        result = {
            "thread_id": thread_id,
            "prior_matter_labels": current_matter_labels,
            "new_matter_label": target_label_name,
            "resolution": resolved["resolution"],
            "no_change": no_change,
        }
        results.append(result)
        _append_audit({
            "timestamp": _now_iso(),
            "tool": "apply_matter_label_query",
            "query": query,
            "approved_by": approval["approved_by"],
            "approval_artifact": approval["approval_artifact"],
            "reason": approval["reason"],
            **result,
        })

    summary = {
        "query": query,
        "thread_count": len(results),
        "changed_count": sum(1 for item in results if not item["no_change"]),
        "no_change_count": sum(1 for item in results if item["no_change"]),
        "new_matter_label": target_label_name,
        "resolution": resolved["resolution"],
        "approved_by": approval["approved_by"],
        "approval_artifact": approval["approval_artifact"],
        "reason": approval["reason"],
        "thread_ids": [item["thread_id"] for item in results],
    }
    return json.dumps(summary, indent=2)


def tool_create_draft(args: Dict[str, Any]) -> str:
    approval = _require_write_approval(args, "create_draft")
    to = str(args.get("to", "")).strip()
    subject = str(args.get("subject", "")).strip()
    body = str(args.get("body", "")).strip()
    thread_id = str(args.get("thread_id", "")).strip() or None
    cc = str(args.get("cc", "")).strip() or None

    if not to:
        raise ValueError("'to' is required.")
    if not subject:
        raise ValueError("'subject' is required.")
    if not body:
        raise ValueError("'body' is required.")

    msg = email.mime.text.MIMEText(body, "plain")
    msg["to"] = to
    msg["subject"] = subject
    if cc:
        msg["cc"] = cc

    raw = base64.urlsafe_b64encode(msg.as_bytes()).decode("utf-8")
    message_body: Dict[str, Any] = {"raw": raw}
    if thread_id:
        message_body["threadId"] = thread_id

    service = _get_gmail_service()
    draft = service.users().drafts().create(
        userId="me", body={"message": message_body}
    ).execute()

    draft_id = draft.get("id", "")
    result = {
        "draft_id": draft_id,
        "to": to,
        "subject": subject,
        "thread_id": thread_id,
        "cc": cc,
        "approved_by": approval["approved_by"],
        "approval_artifact": approval["approval_artifact"],
        "reason": approval["reason"],
    }
    _append_audit({
        "timestamp": _now_iso(),
        "tool": "create_draft",
        **result,
    })
    return json.dumps(result, indent=2)


_TOOLS = [
    {
        "name": "preview_inbox_cleanup",
        "description": (
            "Preview confirmed inbox garbage cleanup using the governed sender lists from "
            "PRO-018. Returns counts only. No Gmail writes."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "scope": {
                    "type": "string",
                    "enum": ["trash", "archive", "all"],
                    "description": "Cleanup scope to preview. Default: all.",
                },
            },
        },
    },
    {
        "name": "execute_inbox_cleanup",
        "description": (
            "Execute confirmed inbox garbage cleanup using the governed sender lists from "
            "PRO-018. This is an ML1-directed bulk cleanup path. "
            "Requires approved_by and reason. Logs to 06_RUNS/logs/inbox_cleanup.log."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "scope": {
                    "type": "string",
                    "enum": ["trash", "archive", "all"],
                    "description": "Cleanup scope to execute. Default: all.",
                },
                "approved_by": {
                    "type": "string",
                    "description": "Approving human, typically ML1.",
                },
                "reason": {
                    "type": "string",
                    "description": "Short reason for the ML1-directed bulk cleanup.",
                },
            },
            "required": ["approved_by", "reason"],
        },
    },
    {
        "name": "execute_category_sweep",
        "description": (
            "Archive all inbox threads older than 2026-01-01 that carry a Gmail soft-junk "
            "category label (PROMOTIONS, SOCIAL, UPDATES, or FORUMS) and have no matter label. "
            "Extracts sender addresses from archived threads and appends new senders to the "
            "PRO-018 archive-class list so future execute_inbox_cleanup runs will cover them. "
            "ML1-directed. Requires approved_by and reason. "
            "Date cutoff (before:2026/1/1) is fixed by ML1 directive."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "approved_by": {
                    "type": "string",
                    "description": "Approving human, typically ML1.",
                },
                "reason": {
                    "type": "string",
                    "description": "Short reason for the category sweep.",
                },
                "max_threads": {
                    "type": "integer",
                    "description": "Maximum threads to process per run. Range: 1-2000. Default: 500.",
                },
            },
            "required": ["approved_by", "reason"],
        },
    },
    {
        "name": "preview_garbage_candidates",
        "description": (
            "Run the PRO-014 state-and-matter classifier in proposal mode and return current "
            "threads that would be marked as 80_Junk_to_Review or 90_Archive. "
            "This does not include PRO-018 soft-junk cleanup candidates."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "batch_size": {
                    "type": "integer",
                    "description": "Number of fresh inbox threads to inspect. Range: 1-500. Default: 50.",
                },
            },
        },
    },
    {
        "name": "resolve_confirmed_junk_threads",
        "description": (
            "Resolve specific ML1-confirmed junk threads by promoting them to 90_Archive "
            "and removing INBOX. Requires approved_by, approval_artifact, and reason."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "thread_ids": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "List of Gmail thread ids to resolve as confirmed junk.",
                },
                "approved_by": {
                    "type": "string",
                    "description": "Approving human, typically ML1.",
                },
                "approval_artifact": {
                    "type": "string",
                    "description": "Repo-relative or absolute path to the approval artifact.",
                },
                "reason": {
                    "type": "string",
                    "description": "Short reason for the confirmed-junk resolution.",
                },
            },
            "required": ["thread_ids", "approved_by", "approval_artifact", "reason"],
        },
    },
    {
        "name": "pass_a_archive_threads",
        "description": (
            "Pass A inbox contamination cleanup: remove INBOX label from a list of threads, "
            "preserving all existing state and matter labels. "
            "Use for threads that carry a state label but remain in inbox (inbox + state label = contradiction). "
            "Writes execution artifact to 06_RUNS/batch/executions/. "
            "Requires approved_by, approval_artifact, and reason."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "thread_ids": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "List of Gmail thread ids to archive (remove INBOX).",
                },
                "approved_by": {
                    "type": "string",
                    "description": "Approving human, typically ML1.",
                },
                "approval_artifact": {
                    "type": "string",
                    "description": "Repo-relative path to the approval artifact.",
                },
                "reason": {
                    "type": "string",
                    "description": "Short reason for the operation.",
                },
                "execution_artifact": {
                    "type": "string",
                    "description": "Repo-relative path for the execution output JSON. Default: 06_RUNS/batch/executions/2026-05-05_inbox_contamination.json",
                },
            },
            "required": ["thread_ids", "approved_by", "approval_artifact", "reason"],
        },
    },
    {
        "name": "apply_state_label",
        "description": (
            "Apply one canonical state label to a Gmail thread with exclusivity enforcement. "
            "Controlled write tool. Requires approved_by, approval_artifact, and reason."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "thread_id": {
                    "type": "string",
                    "description": "Gmail thread id.",
                },
                "state_label": {
                    "type": "string",
                    "enum": sorted(CANONICAL_STATE_LABELS),
                    "description": "Canonical state label to apply.",
                },
                "approved_by": {
                    "type": "string",
                    "description": "Approving human, typically ML1.",
                },
                "approval_artifact": {
                    "type": "string",
                    "description": "Repo-relative or absolute path to the approval artifact.",
                },
                "reason": {
                    "type": "string",
                    "description": "Short reason for the controlled label write.",
                },
            },
            "required": ["thread_id", "state_label", "approved_by", "approval_artifact", "reason"],
        },
    },
    {
        "name": "apply_matter_label",
        "description": (
            "Apply one canonical matter label to a Gmail thread with exclusivity enforcement. "
            "Provide exactly one of matter_label_name or matter_number. Controlled write tool. "
            "Requires approved_by, approval_artifact, and reason."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "thread_id": {
                    "type": "string",
                    "description": "Gmail thread id.",
                },
                "matter_label_name": {
                    "type": "string",
                    "description": "Exact Gmail label path to apply, such as 'LL/1./1.1/25-927-00003 -- Stream Ventures Limited'.",
                },
                "matter_number": {
                    "type": "string",
                    "description": "Matter number used to resolve the canonical matter label when unique.",
                },
                "approved_by": {
                    "type": "string",
                    "description": "Approving human, typically ML1.",
                },
                "approval_artifact": {
                    "type": "string",
                    "description": "Repo-relative or absolute path to the approval artifact.",
                },
                "reason": {
                    "type": "string",
                    "description": "Short reason for the controlled label write.",
                },
            },
            "required": ["thread_id", "approved_by", "approval_artifact", "reason"],
        },
    },
    {
        "name": "apply_matter_label_query",
        "description": (
            "Apply one canonical matter label to every Gmail thread matching a query, "
            "with exclusivity enforcement per thread. Provide exactly one of "
            "matter_label_name or matter_number. Controlled write tool. Requires "
            "approved_by, approval_artifact, and reason."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Gmail query selecting the target thread set, such as 'in:inbox from:aspireinfusions.com'.",
                },
                "matter_label_name": {
                    "type": "string",
                    "description": "Exact Gmail label path to apply.",
                },
                "matter_number": {
                    "type": "string",
                    "description": "Matter number used to resolve the canonical matter label when unique.",
                },
                "approved_by": {
                    "type": "string",
                    "description": "Approving human, typically ML1.",
                },
                "approval_artifact": {
                    "type": "string",
                    "description": "Repo-relative or absolute path to the approval artifact.",
                },
                "reason": {
                    "type": "string",
                    "description": "Short reason for the controlled bulk label write.",
                },
            },
            "required": ["query", "approved_by", "approval_artifact", "reason"],
        },
    },
    {
        "name": "create_draft",
        "description": (
            "Create a Gmail draft. Optionally threaded as a reply by passing thread_id. "
            "Write tool — requires approved_by, approval_artifact, and reason."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "to": {
                    "type": "string",
                    "description": "Recipient email address.",
                },
                "subject": {
                    "type": "string",
                    "description": "Email subject line.",
                },
                "body": {
                    "type": "string",
                    "description": "Plain-text email body.",
                },
                "thread_id": {
                    "type": "string",
                    "description": "Gmail thread id. When provided the draft is created as a reply in that thread.",
                },
                "cc": {
                    "type": "string",
                    "description": "Optional CC address.",
                },
                "approved_by": {
                    "type": "string",
                    "description": "Who approved this write (e.g. 'ML1').",
                },
                "approval_artifact": {
                    "type": "string",
                    "description": "Repo-relative or absolute path to the approval artifact.",
                },
                "reason": {
                    "type": "string",
                    "description": "Short reason for creating this draft.",
                },
            },
            "required": ["to", "subject", "body", "approved_by", "approval_artifact", "reason"],
        },
    },
]

_TOOL_FN_MAP = {
    "preview_inbox_cleanup": tool_preview_inbox_cleanup,
    "preview_garbage_candidates": tool_preview_garbage_candidates,
    "execute_inbox_cleanup": tool_execute_inbox_cleanup,
    "execute_category_sweep": tool_execute_category_sweep,
    "resolve_confirmed_junk_threads": tool_resolve_confirmed_junk_threads,
    "pass_a_archive_threads": tool_pass_a_archive_threads,
    "apply_state_label": tool_apply_state_label,
    "apply_matter_label": tool_apply_matter_label,
    "apply_matter_label_query": tool_apply_matter_label_query,
    "create_draft": tool_create_draft,
}


def _write(msg: Dict[str, Any]) -> None:
    line = json.dumps(msg, separators=(",", ":"))
    sys.stdout.write(line + "\n")
    sys.stdout.flush()


def _ok(request_id: Any, result: Any) -> None:
    _write({"jsonrpc": "2.0", "id": request_id, "result": result})


def _err(request_id: Any, code: int, message: str) -> None:
    _write({
        "jsonrpc": "2.0",
        "id": request_id,
        "error": {"code": code, "message": message},
    })


def _handle(msg: Dict[str, Any]) -> None:
    method = msg.get("method", "")
    request_id = msg.get("id")

    if request_id is None:
        log.debug("notification: %s", method)
        return

    try:
        if method == "initialize":
            _ok(request_id, {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {
                    "name": "gmail-ll",
                    "version": "1.0.0",
                    "description": (
                        "Bounded Gmail MCP — LL Second Brain. "
                        "Proposal-first with controlled label writes."
                    ),
                },
            })
        elif method == "tools/list":
            _ok(request_id, {"tools": _TOOLS})
        elif method == "tools/call":
            params = msg.get("params", {})
            tool_name = params.get("name", "")
            arguments = params.get("arguments", {})

            if tool_name not in _TOOL_FN_MAP:
                _err(request_id, -32601, f"Unknown tool: '{tool_name}'")
                return

            log.info("tools/call name=%s", tool_name)
            try:
                text = _TOOL_FN_MAP[tool_name](arguments)
                _ok(request_id, {
                    "content": [{"type": "text", "text": text}],
                    "isError": False,
                })
            except (PermissionError, ValueError) as exc:
                log.warning("tool error [%s]: %s", tool_name, exc)
                _ok(request_id, {
                    "content": [{"type": "text", "text": f"ERROR: {exc}"}],
                    "isError": True,
                })
            except Exception as exc:
                log.error("tool exception [%s]: %s", tool_name, exc, exc_info=True)
                _ok(request_id, {
                    "content": [{"type": "text", "text": f"ERROR: {exc}"}],
                    "isError": True,
                })
        else:
            _err(request_id, -32601, f"Method not found: '{method}'")
    except Exception as exc:
        log.error("handler exception: %s", exc, exc_info=True)
        _err(request_id, -32603, f"Internal error: {exc}")


def main() -> None:
    log.info(
        "Gmail MCP server starting. Policy: proposal-first with controlled state/matter label writes."
    )
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            msg = json.loads(line)
        except json.JSONDecodeError as exc:
            log.error("JSON parse error: %s | input: %.200s", exc, line)
            _write({
                "jsonrpc": "2.0",
                "id": None,
                "error": {"code": -32700, "message": f"Parse error: {exc}"},
            })
            continue
        _handle(msg)


if __name__ == "__main__":
    main()
