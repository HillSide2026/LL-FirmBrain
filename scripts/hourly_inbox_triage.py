#!/usr/bin/env python3
"""
Inbox Triage Agent
==================
AI Agent Spec — Hourly Inbox Triage Agent + Morning Run (approved 2026-04-13)

Two scheduled modes of the same script:

  --mode intraday  (default)
      Runs every hour 09:00–17:00, Sun–Fri.
      Review window: threads updated since the last intraday run.
      For each thread: apply matter label (if matched) + one canonical state label.

  --mode morning
      Runs once at 08:00, Sun–Fri.
      Review window: 17:01 previous business day → 08:00 today.
      Same classification logic as intraday.
      Outbound queue send: NOT YET IMPLEMENTED (future slice).

Business day definition: Sunday–Friday (Saturday is the only non-business day).

Classification rules (both modes):
  1. Resolve thread → matter via matter_identity_map + existing matter labels
  2. If matched: apply matter label + one state label (single API call)
  3. If not matched: apply one state label only
  4. Low confidence → 00_Triage + needs_review flag in log
  Priority tier (Essential/Strategic) is recorded in the log via the matched
  matter label's tier prefix; no new priority Gmail labels are created.

Authority: ML1 approval per Hourly Inbox Triage Agent spec (2026-04-13)
Policy: POL-042 Inbox Governance Policy
Skill:   agents/inbox-agent/skill.md  (decision order, invariants, failure bias)
"""

import argparse
import datetime
import json
import logging
import sys
import time
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

# ── Repo paths ─────────────────────────────────────────────────────────────────

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "gmail_governance"))

# ── Shared imports from gmail_governance ──────────────────────────────────────

from state_enforcement import get_gmail_service, CANONICAL_LABELS, INBOX_EXIT_LABELS
from matter_enforcement import (
    get_matter_labels,
    MATTER_TIER_PREFIXES,
    MATTER_LEAF_PATTERN,
)
from batch_classifier import (
    classify_thread,
    get_matter_signal_confidence,
    resolve_thread_matter,
)

# ── Constants ──────────────────────────────────────────────────────────────────

AGENT_VERSION = "inbox-triage-v1.1"
APPROVAL_ARTIFACT = "AI Agent Spec — Hourly Inbox Triage Agent (2026-04-13)"
APPROVAL_BY = "ML1"
SKILL_DOC = REPO_ROOT / "agents" / "inbox-agent" / "skill.md"

# Matter label tier prefix → priority classification (for logging only)
TIER_TO_PRIORITY: Dict[str, str] = {
    "LL/1./1.1/": "ESSENTIAL_MATTER",
    "LL/1./1.2/": "STRATEGIC_MATTER",
    "LL/1./1.3/": "STANDARD_MATTER",
    "LL/1./1.4/": "PARKED_MATTER",
}

# Confidence thresholds
CONFIDENCE_LOW = 0.65   # Below → 00_Triage + needs_review=True
CONFIDENCE_AUTO = 0.75  # Below → needs_review=True in log

# Fallback lookback window for intraday mode if no prior run state exists (minutes)
INTRADAY_FALLBACK_MINUTES = 70

# File paths
STATE_DIR = REPO_ROOT / "06_RUNS" / "INBOX_TRIAGE" / "state"
LOG_DIR = REPO_ROOT / "06_RUNS" / "INBOX_TRIAGE" / "logs"
RUN_LOG_FILE = LOG_DIR / "hourly_triage_run.ndjson"


def _state_file(mode: str) -> Path:
    return STATE_DIR / f"last_run_{mode}.json"


# ── Business day calendar (Sun–Fri; Sat is the only non-business day) ──────────

def is_business_day(d: datetime.date) -> bool:
    """Return True if d is a business day (Sunday–Friday)."""
    return d.weekday() != 5  # 5 = Saturday


def previous_business_day(d: datetime.date) -> datetime.date:
    """Return the most recent business day strictly before d."""
    candidate = d - datetime.timedelta(days=1)
    while not is_business_day(candidate):
        candidate -= datetime.timedelta(days=1)
    return candidate


# ── Review window calculation ──────────────────────────────────────────────────

def morning_review_window() -> Tuple[int, int]:
    """
    Return (start_epoch, end_epoch) for the morning run:
      start = 17:01:00 local time on the previous business day
      end   = 08:00:00 local time today
    Uses local system time (matches launchd fire time).
    """
    today = datetime.date.today()
    prev_bd = previous_business_day(today)

    local_start = datetime.datetime(
        prev_bd.year, prev_bd.month, prev_bd.day, 17, 1, 0
    )
    local_end = datetime.datetime(
        today.year, today.month, today.day, 8, 0, 0
    )

    start_epoch = int(local_start.timestamp())
    end_epoch = int(local_end.timestamp())
    return start_epoch, end_epoch


def intraday_review_window(last_run_epoch: Optional[int]) -> int:
    """
    Return the after_epoch for the intraday Gmail query.
    Falls back to INTRADAY_FALLBACK_MINUTES if no prior run.
    """
    if last_run_epoch:
        return last_run_epoch
    return int(time.time()) - (INTRADAY_FALLBACK_MINUTES * 60)


# ── Gmail label utilities ──────────────────────────────────────────────────────

def get_full_label_map(service) -> Dict[str, str]:
    """Return full label name → label ID map for the Gmail account."""
    results = service.users().labels().list(userId="me").execute()
    return {lbl["name"]: lbl["id"] for lbl in results.get("labels", [])}


def get_matter_label_ids_on_thread(
    current_label_ids: set, label_id_to_name: Dict[str, str]
) -> List[str]:
    """
    Return the IDs of any canonical matter labels (LL/1./x.x/...) currently
    on the thread. Used to remove old matter labels before applying a new one.
    """
    result = []
    for lid in current_label_ids:
        name = label_id_to_name.get(lid, "")
        if not any(name.startswith(p) for p in MATTER_TIER_PREFIXES):
            continue
        parts = name.split("/")
        if len(parts) >= 4 and MATTER_LEAF_PATTERN.match(parts[-1]):
            result.append(lid)
    return result


# ── Thread fetching ────────────────────────────────────────────────────────────

def fetch_threads_in_window(service, after_epoch: int, before_epoch: Optional[int] = None) -> List[Dict]:
    """
    Return thread stubs for threads with new messages after after_epoch.
    Optional before_epoch constrains the upper bound (morning mode).
    """
    query = f"after:{after_epoch}"
    if before_epoch:
        query += f" before:{before_epoch}"

    threads, page_token = [], None
    while True:
        params: Dict[str, Any] = {"userId": "me", "q": query, "maxResults": 100}
        if page_token:
            params["pageToken"] = page_token
        resp = service.users().threads().list(**params).execute()
        threads.extend(resp.get("threads", []))
        page_token = resp.get("nextPageToken")
        if not page_token:
            break
    return threads


def fetch_thread_detail(
    service, thread_id: str, label_id_to_name: Dict[str, str]
) -> Optional[Dict[str, Any]]:
    """
    Fetch thread metadata needed for classification:
    subject, sender, last_sender, snippet, current_labels, message_count.
    """
    thread = service.users().threads().get(
        userId="me",
        id=thread_id,
        format="metadata",
        metadataHeaders=["Subject", "From"],
    ).execute()

    messages = thread.get("messages", [])
    if not messages:
        return None

    first_msg = messages[0]
    last_msg = messages[-1]

    def hdr(msg, name):
        for h in msg.get("payload", {}).get("headers", []):
            if h["name"] == name:
                return h["value"]
        return ""

    all_label_ids: set = set()
    for msg in messages:
        all_label_ids.update(msg.get("labelIds", []))

    current_labels = [
        label_id_to_name[lid] for lid in all_label_ids if lid in label_id_to_name
    ]

    return {
        "thread_id": thread_id,
        "subject": hdr(first_msg, "Subject") or "(No Subject)",
        "sender": hdr(first_msg, "From") or "(Unknown)",
        "last_sender": hdr(last_msg, "From"),
        "snippet": first_msg.get("snippet", "")[:300],
        "current_labels": current_labels,
        "all_label_ids": all_label_ids,
        "message_count": len(messages),
        "is_unread": "UNREAD" in all_label_ids,
        "latest_message_at": last_msg.get("internalDate", ""),
    }


# ── Classification ─────────────────────────────────────────────────────────────

def classify_thread_full(
    thread_detail: Dict[str, Any],
    matter_labels: Dict,
) -> Dict[str, Any]:
    """
    Full classification result for a thread.

    Returns a dict with:
      matter_number:      matched Clio matter ID or None
      matter_label_name:  full Gmail label path or None
      matter_label_id:    Gmail label ID or None
      priority:           'ESSENTIAL_MATTER' | 'STRATEGIC_MATTER' | 'STANDARD_MATTER' |
                          'PARKED_MATTER' | 'NON_PRIORITY'
      state_label:        one of CANONICAL_LABELS
      confidence:         float
      needs_review:       bool
      reason:             str
    """
    # skill.md § Decision Order: attempt matter detection first.
    # skill.md § Matter Authority Rule: existing matter labels are authoritative;
    #   do not override without strong contradictory evidence.
    matter = resolve_thread_matter(
        subject=thread_detail["subject"],
        sender=thread_detail["sender"],
        snippet=thread_detail["snippet"],
        current_labels=thread_detail["current_labels"],
        matter_labels=matter_labels,
    )

    matter_matched = matter["status"] == "matched"
    matter_number = matter.get("matter_number") if matter_matched else None
    matter_label_name = matter.get("proposed_label") if matter_matched else None
    matter_label_id = matter.get("proposed_label_id") if matter_matched else None

    signal = matter.get("signal", "")
    confidence = {
        "determinative": 0.99,
        "high": 0.90,
        "medium": 0.75,
        "none": 0.50,
    }.get(get_matter_signal_confidence(signal), 0.70) if matter_matched else 0.90

    # Priority tier from matter label path (for logging)
    priority = "NON_PRIORITY"
    if matter_label_name:
        for tier_prefix, priority_key in TIER_TO_PRIORITY.items():
            if matter_label_name.startswith(tier_prefix):
                priority = priority_key
                break

    # State label — pass has_matter_association so classifier steers toward
    # 10_Action_Matthew for matched threads rather than falling to 00_Triage
    has_matter = matter_matched and confidence >= CONFIDENCE_AUTO
    raw_state = classify_thread(
        subject=thread_detail["subject"],
        sender=thread_detail["sender"],
        snippet=thread_detail["snippet"],
        current_labels=thread_detail["current_labels"],
        last_sender=thread_detail["last_sender"],
        message_count=thread_detail["message_count"],
        has_matter_association=has_matter,
    )

    # skill.md § Failure Bias: when uncertain, assign 00_Triage; do not guess a matter.
    state_label = "00_Triage" if confidence < CONFIDENCE_LOW else raw_state
    needs_review = confidence < CONFIDENCE_AUTO

    # Reason string
    if matter_number:
        reason = f"Matter {matter_number} ({priority.lower().replace('_', ' ')}) → {state_label}"
    else:
        reason = f"non_priority → {state_label}"
    if confidence < CONFIDENCE_LOW:
        reason += " [low confidence → triage]"

    return {
        "matter_number": matter_number,
        "matter_label_name": matter_label_name,
        "matter_label_id": matter_label_id,
        "priority": priority,
        "state_label": state_label,
        "confidence": confidence,
        "needs_review": needs_review,
        "reason": reason,
    }


# ── Label application ──────────────────────────────────────────────────────────

def apply_labels_to_thread(
    service,
    thread_id: str,
    matter_label_id: Optional[str],
    state_label_name: str,
    label_map: Dict[str, str],
    label_id_to_name: Dict[str, str],
    current_label_ids: set,
) -> bool:
    """
    Apply matter label (if provided) + one canonical state label in a single
    threads.modify call. Removes:
      - all existing matter labels (if applying a new matter label)
      - all competing canonical state labels

    Does NOT touch any other labels on the thread.
    """
    if state_label_name not in CANONICAL_LABELS:
        logging.error(f"'{state_label_name}' is not a canonical state label")
        return False

    state_label_id = label_map.get(state_label_name)
    if not state_label_id:
        logging.error(f"State label '{state_label_name}' not found in Gmail")
        return False

    add_ids: List[str] = [state_label_id]
    remove_ids: set = set()

    # State exclusivity: remove all other canonical state labels
    canonical_ids = {label_map[n] for n in CANONICAL_LABELS if n in label_map}
    remove_ids.update(current_label_ids & canonical_ids - {state_label_id})

    # Inbox exit: remove INBOX atomically when applying a terminal/routing label (POL-042 §4)
    if state_label_name in INBOX_EXIT_LABELS:
        remove_ids.add("INBOX")

    # Matter label: add new, remove old
    if matter_label_id:
        old_matter_ids = get_matter_label_ids_on_thread(current_label_ids, label_id_to_name)
        remove_ids.update(mid for mid in old_matter_ids if mid != matter_label_id)
        if matter_label_id not in current_label_ids:
            add_ids.append(matter_label_id)

    remove_list = list(remove_ids)

    # Idempotent: nothing to add or remove
    if all(aid in current_label_ids for aid in add_ids) and not remove_list:
        return True

    service.users().threads().modify(
        userId="me",
        id=thread_id,
        body={"addLabelIds": add_ids, "removeLabelIds": remove_list},
    ).execute()
    return True


# ── Inbox presence violation scan ─────────────────────────────────────────────

VIOLATIONS_REPORT = REPO_ROOT / "05_MATTERS" / "DASHBOARDS" / "INBOX_STATE_VIOLATIONS.md"


def scan_inbox_violations(service, label_map: Dict[str, str], run_id: str) -> int:
    """
    Detect threads carrying INBOX + an inbox-exit state label (invalid per POL-042 §4).
    Writes a report to INBOX_STATE_VIOLATIONS.md. Read-only — no Gmail writes.
    Returns the violation count.
    """
    violations: List[Dict[str, str]] = []
    for label_name in sorted(INBOX_EXIT_LABELS):
        label_id = label_map.get(label_name)
        if not label_id:
            continue
        try:
            resp = service.users().threads().list(
                userId="me",
                labelIds=["INBOX", label_id],
                maxResults=100,
            ).execute()
            for stub in resp.get("threads", []):
                violations.append({"thread_id": stub["id"], "invalid_label": label_name})
        except Exception as exc:
            logging.warning(f"Inbox violation scan skipped for {label_name}: {exc}")

    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    lines = [
        "# Inbox State Violations",
        "",
        f"Generated at: {now}",
        f"Run ID: {run_id}",
        "",
        "Threads carrying INBOX and an inbox-exit state label simultaneously.",
        "Invalid per POL-042 §4. Requires ML1 review — no auto-resolution.",
        "",
    ]
    if violations:
        lines += [
            "| Thread ID | Invalid Label |",
            "| --- | --- |",
        ] + [f"| {v['thread_id']} | {v['invalid_label']} |" for v in violations]
        logging.warning(f"Inbox presence violations: {len(violations)} — see INBOX_STATE_VIOLATIONS.md")
    else:
        lines.append("No violations detected.")
    lines.append("")
    VIOLATIONS_REPORT.write_text("\n".join(lines))
    return len(violations)


# ── Logging ────────────────────────────────────────────────────────────────────

def write_log_entry(entry: Dict[str, Any]):
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    with open(RUN_LOG_FILE, "a") as f:
        f.write(json.dumps(entry) + "\n")


def build_thread_log(
    run_id: str,
    mode: str,
    thread_detail: Dict[str, Any],
    classification: Dict[str, Any],
    action_taken: str,
) -> Dict[str, Any]:
    return {
        "run_id": run_id,
        "mode": mode,
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "agent_version": AGENT_VERSION,
        "thread_id": thread_detail["thread_id"],
        "subject": thread_detail["subject"][:120],
        "sender": thread_detail["sender"][:80],
        "latest_message_at": thread_detail.get("latest_message_at"),
        "is_unread": thread_detail.get("is_unread", False),
        "existing_labels": thread_detail["current_labels"],
        "priority_classification": classification["priority"].lower(),
        "matter_number": classification["matter_number"],
        "matter_label": classification["matter_label_name"],
        "state_label": classification["state_label"],
        "confidence": round(classification["confidence"], 3),
        "reason_summary": classification["reason"],
        "action_taken": action_taken,
        "needs_review": classification["needs_review"],
        "approval_artifact": APPROVAL_ARTIFACT,
        "approved_by": APPROVAL_BY,
    }


# ── Run state ──────────────────────────────────────────────────────────────────

def load_run_state(mode: str) -> Dict[str, Any]:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    sf = _state_file(mode)
    if sf.exists():
        with open(sf) as f:
            return json.load(f)
    return {}


def save_run_state(mode: str, run_id: str, thread_count: int, extra: Optional[Dict] = None):
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    state = {
        "mode": mode,
        "last_run_id": run_id,
        "last_run_timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "last_run_epoch": int(time.time()),
        "threads_processed": thread_count,
    }
    if extra:
        state.update(extra)
    with open(_state_file(mode), "w") as f:
        json.dump(state, f, indent=2)


# ── Thread processing loop (shared by both modes) ─────────────────────────────

def process_threads(
    service,
    raw_threads: List[Dict],
    matter_labels: Dict,
    label_map: Dict[str, str],
    label_id_to_name: Dict[str, str],
    run_id: str,
    mode: str,
    stats: Dict[str, Any],
):
    for thread_stub in raw_threads:
        thread_id = thread_stub["id"]
        try:
            detail = fetch_thread_detail(service, thread_id, label_id_to_name)
            if not detail:
                stats["skipped"] += 1
                continue

            classification = classify_thread_full(detail, matter_labels)

            apply_labels_to_thread(
                service=service,
                thread_id=thread_id,
                matter_label_id=classification["matter_label_id"],
                state_label_name=classification["state_label"],
                label_map=label_map,
                label_id_to_name=label_id_to_name,
                current_label_ids=detail["all_label_ids"],
            )

            # Stats
            priority = classification["priority"]
            if priority == "ESSENTIAL_MATTER":
                stats["essential_matter"] += 1
            elif priority == "STRATEGIC_MATTER":
                stats["strategic_matter"] += 1
            else:
                stats["non_priority"] += 1

            if classification["needs_review"] and classification["confidence"] < CONFIDENCE_LOW:
                stats["low_confidence"] += 1

            if classification["matter_label_name"]:
                stats["matter_labels_applied"] += 1

            stats["by_state"][classification["state_label"]] += 1

            action = f"apply_state:{classification['state_label']}"
            if classification["matter_label_id"]:
                action = f"apply_matter+state:{classification['matter_label_name']}+{classification['state_label']}"

            write_log_entry(build_thread_log(run_id, mode, detail, classification, action))

        except Exception as exc:
            stats["errors"] += 1
            logging.error(f"Thread {thread_id}: {exc}")
            write_log_entry({
                "run_id": run_id,
                "mode": mode,
                "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                "thread_id": thread_id,
                "error": str(exc),
                "action_taken": "error",
            })


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Inbox Triage Agent")
    parser.add_argument(
        "--mode",
        choices=["intraday", "morning"],
        default="intraday",
        help="Run mode: intraday (default) or morning",
    )
    args = parser.parse_args()
    mode = args.mode

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
    )

    run_id = datetime.datetime.now(datetime.timezone.utc).strftime(f"triage-{mode}-%Y%m%d-%H%M%S")
    run_start = datetime.datetime.now(datetime.timezone.utc)

    logging.info(f"=== Inbox Triage Agent | mode={mode} | run={run_id} ===")
    if SKILL_DOC.exists():
        logging.info(f"Skill: {SKILL_DOC}")
    else:
        logging.warning(f"Skill doc not found: {SKILL_DOC}")

    prior_state = load_run_state(mode)
    service = get_gmail_service()
    label_map = get_full_label_map(service)
    label_id_to_name = {v: k for k, v in label_map.items()}
    matter_labels = get_matter_labels(service)

    # ── Review window ─────────────────────────────────────────────────────────
    before_epoch: Optional[int] = None
    checkpoint_extra: Dict[str, Any] = {}

    if mode == "morning":
        start_epoch, end_epoch = morning_review_window()
        before_epoch = end_epoch
        after_epoch = start_epoch
        window_start_iso = datetime.datetime.fromtimestamp(start_epoch).isoformat()
        window_end_iso = datetime.datetime.fromtimestamp(end_epoch).isoformat()
        logging.info(f"Morning window: {window_start_iso} → {window_end_iso}")
        checkpoint_extra = {
            "covered_start": window_start_iso,
            "covered_end": window_end_iso,
        }
    else:
        after_epoch = intraday_review_window(prior_state.get("last_run_epoch"))

    raw_threads = fetch_threads_in_window(service, after_epoch, before_epoch)
    logging.info(f"Fetched {len(raw_threads)} threads")

    stats: Dict[str, Any] = {
        "total": len(raw_threads),
        "essential_matter": 0,
        "strategic_matter": 0,
        "non_priority": 0,
        "matter_labels_applied": 0,
        "low_confidence": 0,
        "errors": 0,
        "skipped": 0,
        "by_state": {lbl: 0 for lbl in CANONICAL_LABELS},
    }

    process_threads(
        service, raw_threads, matter_labels,
        label_map, label_id_to_name,
        run_id, mode, stats,
    )

    violation_count = scan_inbox_violations(service, label_map, run_id)
    stats["inbox_violations"] = violation_count

    save_run_state(mode, run_id, len(raw_threads), checkpoint_extra)

    duration = (datetime.datetime.now(datetime.timezone.utc) - run_start).total_seconds()

    print(f"\n{'='*56}")
    print(f"  Inbox Triage  |  mode={mode}  |  {run_id}")
    print(f"{'='*56}")
    print(f"  Duration:          {duration:.1f}s")
    print(f"  Threads total:     {stats['total']}")
    print(f"  Essential matters: {stats['essential_matter']}")
    print(f"  Strategic matters: {stats['strategic_matter']}")
    print(f"  Non-priority:      {stats['non_priority']}")
    print(f"  Matter labels:     {stats['matter_labels_applied']}")
    print(f"  Low confidence:    {stats['low_confidence']}")
    print(f"  Errors:            {stats['errors']}")
    print(f"  Skipped:           {stats['skipped']}")
    print(f"  Inbox violations:  {stats['inbox_violations']}")
    active_states = {k: v for k, v in stats["by_state"].items() if v > 0}
    if active_states:
        print(f"\n  State label breakdown:")
        for lbl, count in sorted(active_states.items()):
            print(f"    {lbl}: {count}")
    if mode == "morning" and checkpoint_extra:
        print(f"\n  Window: {checkpoint_extra.get('covered_start')} → {checkpoint_extra.get('covered_end')}")
    print(f"\n  Log:   {RUN_LOG_FILE}")
    print(f"  State: {_state_file(mode)}")
    print(f"{'='*56}\n")


if __name__ == "__main__":
    main()
