#!/usr/bin/env python3
"""Matter Command and Control runner (transitional Matter Admin + Matter File Admin bundle).

Slice 1 includes:
- Clio Matter Index Agent
- Inbox to Matter Router (label-first)
- Firm Matter Digest compiler (minimal)

Slice 2 currently includes the active Matter File Administration step:
- SharePoint document index per matter
- SharePoint delta reporting per matter
- Firm-wide SharePoint gaps dashboard

Authority boundary:
- Read connectors only
- No broad or unapproved writes to Clio/Gmail/SharePoint
- Controlled Gmail state-label writes require explicit ML1 approval
- ML2 stores derived artifacts and source pointers only
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from functools import lru_cache
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

import yaml


REPO_ROOT = Path(__file__).resolve().parent.parent
CONFIG_DIR = REPO_ROOT / "00_SYSTEM" / "CONFIG"
MATTERS_ROOT = REPO_ROOT / "05_MATTERS"
DASHBOARD_DIR = REPO_ROOT / "05_MATTERS" / "DASHBOARDS"
RUN_LOG_DIR = REPO_ROOT / "06_RUNS" / "logs" / "matter_admin"
CACHE_DIR = REPO_ROOT / "cache"

DEFAULT_CLIO_CACHE = CACHE_DIR / "clio_matters.json"
DEFAULT_GMAIL_CACHE = CACHE_DIR / "gmail_threads.json"
DEFAULT_SHAREPOINT_CACHE = CACHE_DIR / "sharepoint_files.json"
DEFAULT_RUN_STATE = CACHE_DIR / "run_state.json"
DEFAULT_GMAIL_FALLBACK = REPO_ROOT / "06_RUNS" / "ops" / "gmail_fetch_latest.json"
DEFAULT_SHAREPOINT_METADATA_ROOT = (
    REPO_ROOT / "09_INBOX" / "_sources" / "sharepoint" / "metadata" / "legalmatters_library"
)
DEFAULT_SHAREPOINT_RAW_ROOT = REPO_ROOT / "09_INBOX" / "_sources" / "sharepoint" / "raw" / "legalmatters_library"
DEFAULT_MATTER_SHAREPOINT_MAP = REPO_ROOT / "05_MATTERS" / "_REGISTRY" / "matter_sharepoint_map.yml"
DEFAULT_MATTER_IDENTITY_MAP = REPO_ROOT / "00_SYSTEM" / "matters" / "matter_identity_map.yaml"
DEFAULT_MATTER_FOLDER_RULES = CONFIG_DIR / "matter_folder_rules.yml"
DEFAULT_MATTER_DELIVERY_TAXONOMY = CONFIG_DIR / "matter_delivery_taxonomy.yml"
DEFAULT_DISCOVERY_GAPS = REPO_ROOT / "09_INBOX" / "_sources" / "sharepoint" / "discovery" / "gaps.md"
DEFAULT_MAX_THREADS = 25
DEFAULT_SHAREPOINT_SIGNAL_TEXT_EXTENSIONS = {".doc", ".docx", ".txt", ".md"}
DEFAULT_SHAREPOINT_SIGNAL_TEXT_CHAR_LIMIT = 12000
DEFAULT_SHAREPOINT_SIGNAL_TEXT_DOC_LIMIT = 12
BATCH_PROPOSALS_DIR = REPO_ROOT / "06_RUNS" / "batch" / "proposals"
BATCH_EXECUTIONS_DIR = REPO_ROOT / "06_RUNS" / "batch" / "executions"

MATTER_INDEX_PATH = DASHBOARD_DIR / "MATTER_INDEX.md"
INBOX_UNMAPPED_PATH = DASHBOARD_DIR / "INBOX_UNMAPPED.md"
MATTER_DIGEST_PATH = DASHBOARD_DIR / "MATTER_DIGEST.md"
SHAREPOINT_GAPS_PATH = DASHBOARD_DIR / "SHAREPOINT_GAPS.md"

MATTER_TIERS = ("ESSENTIAL", "STRATEGIC", "STANDARD", "NORMAL", "PARKED")
CANONICAL_STATE_LABELS = (
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
)
LEGACY_STATE_LABEL_ALIASES = {
    "08_Junk_to_Review": "80_Junk_to_Review",
    "80_Junk (Pending Review)": "80_Junk_to_Review",
}
MATTHEW_EMAILS = {"matthew@levinelegal.ca", "matthew@levine-law.ca"}
TEAM_SIGNALS = {
    "levinelegalservices.com",
    "lino@levinelegal.ca",
    "grace@levinelegal.ca",
    "lino@levine-law.ca",
    "grace@levine-law.ca",
}
ADMIN_SIGNALS = {
    "telus.com",
    "connect.telus.com",
    "soulpepper.com",
    "amazon.ca",
    "amazon.com",
    "regus.com",
}
LEGAL_SIGNALS = {
    "cra-arc.gc.ca",
    "hamlins.com",
    "clio.com",
    "mail.hellosign.com",
    "dropbox.com",
    "cassels.com",
    "rousseaumazzuca.com",
    "docuseal.com",
    "cestlavielaw.ca",
    "asana.com",
}
AUTOMATED_SENDER_SIGNALS = (
    "noreply",
    "no-reply",
    "donotreply",
    "do_not_reply",
    "notifications@",
    "automated@",
    "system@",
)
CALENDAR_SENDER = "calendar-notification@google.com"
DEFAULT_GMAIL_REVIEW_QUERY = "in:inbox"
GENERIC_IDENTITY_KEYS = {
    "alerts",
    "archive",
    "agreement",
    "agreements",
    "amendment",
    "application",
    "articles",
    "authorizing",
    "board",
    "business",
    "certificate",
    "client",
    "clients",
    "closing",
    "company",
    "compliance",
    "consent",
    "construction",
    "corporation",
    "corporations",
    "connect",
    "delivery",
    "director",
    "directors",
    "document",
    "documents",
    "docs",
    "draft",
    "drafts",
    "email",
    "filing",
    "financial",
    "forms",
    "gmail",
    "guidance",
    "holdings",
    "hello",
    "info",
    "inc",
    "incorporated",
    "incorporation",
    "index",
    "instructions",
    "intent",
    "limited",
    "llp",
    "matter",
    "matters",
    "marketing",
    "matthew",
    "matthewsimac",
    "ml1",
    "month",
    "notice",
    "ontario",
    "operations",
    "package",
    "payment",
    "payments",
    "policy",
    "purchase",
    "register",
    "registration",
    "received",
    "release",
    "releaseagreement",
    "report",
    "reports",
    "request",
    "resignation",
    "resolution",
    "review",
    "schedule",
    "services",
    "share",
    "shareholder",
    "shareholders",
    "sharepurchase",
    "sports",
    "support",
    "street",
    "strategy",
    "systems",
    "text",
    "today",
    "true",
    "updated",
    "vendor",
    "work",
    "year",
}
TEXT_PHRASE_GENERIC_WORDS = {
    "account",
    "accounts",
    "adjusted",
    "admin",
    "agreement",
    "agreements",
    "amount",
    "analysis",
    "ancillary",
    "application",
    "applications",
    "approval",
    "assessment",
    "board",
    "broker",
    "business",
    "centre",
    "closing",
    "comment",
    "connect",
    "date",
    "days",
    "director",
    "directors",
    "document",
    "documents",
    "draft",
    "drafts",
    "filing",
    "filings",
    "first",
    "form",
    "forms",
    "guidance",
    "incident",
    "index",
    "instructions",
    "intent",
    "monthly",
    "notice",
    "onboarding",
    "operations",
    "package",
    "payment",
    "payments",
    "period",
    "policy",
    "program",
    "questionnaire",
    "register",
    "registration",
    "report",
    "reports",
    "request",
    "response",
    "review",
    "risk",
    "schedule",
    "schedules",
    "second",
    "services",
    "sheet",
    "sheets",
    "subject",
    "supervision",
    "system",
    "third",
    "this",
    "training",
    "transaction",
    "transactions",
    "update",
    "updates",
    "view",
    "wire",
}
PROPER_PHRASE_PATTERN = re.compile(
    r"\b(?:[A-Z][A-Za-z0-9&'.-]{2,}|[A-Z]{2,})(?:\s+(?:[A-Z][A-Za-z0-9&'.-]{2,}|[A-Z]{2,}|[0-9]{2,})){0,3}\b"
)


@dataclass(frozen=True)
class ServiceRef:
    service_type: str
    service_name: str
    status: str
    playbook_ref: str


@dataclass(frozen=True)
class MatterRef:
    clio_matter_id: str
    matter_number: str
    name: str
    status: str
    delivery_status: str
    fulfillment_status: str
    services: Tuple[ServiceRef, ...]
    responsible: str
    client: str
    source_pointer: str


@dataclass(frozen=True)
class ThreadRef:
    thread_id: str
    subject: str
    participants: Tuple[str, ...]
    last_message_at: str
    labels: Tuple[str, ...]
    latest_snippet: str
    source_pointer: str
    sender: str = ""
    last_sender: str = ""
    message_count: int = 0
    state_labels: Tuple[str, ...] = tuple()


@dataclass(frozen=True)
class DocRef:
    drive_item_id: str
    path: str
    name: str
    modified_at: str
    size: int
    web_url: str
    author: str
    drive_id: str
    is_folder: bool
    source_pointer: str


DEFAULT_DELIVERY_TAXONOMY: Dict[str, Any] = {
    "delivery_categories": {
        "delivery_active": {
            "label": "ML Active",
            "status_include": ["Open", "Pending"],
            "delivery_status_include": ["Essential", "Strategic", "Standard"],
            "fulfillment_status_include": ["urgent", "active"],
        },
        "delivery_watch": {
            "label": "ML Watch",
            "status_include": ["Open", "Pending"],
            "delivery_status_include": ["Parked"],
            "fulfillment_status_include": ["keep in view", "active", "urgent"],
        },
    },
    "service_model": {
        "canonical_field": "services",
        "accepted_service_types": ["solution", "strategy"],
        "legacy_alias_fields": {
            "solutions": "solution",
            "strategies": "strategy",
        },
    },
}


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def utc_iso(dt: Optional[datetime] = None) -> str:
    dt = dt or utc_now()
    return dt.replace(microsecond=0).isoformat().replace("+00:00", "Z")


def parse_timestamp(value: Any) -> Optional[datetime]:
    """Parse ISO timestamp or Gmail epoch-ms string to UTC datetime."""
    if value is None:
        return None

    if isinstance(value, int):
        try:
            return datetime.fromtimestamp(value / 1000, tz=timezone.utc)
        except Exception:
            return None

    raw = str(value).strip()
    if not raw:
        return None

    if raw.isdigit():
        try:
            return datetime.fromtimestamp(int(raw) / 1000, tz=timezone.utc)
        except Exception:
            return None

    normalized = raw.replace("Z", "+00:00")
    try:
        dt = datetime.fromisoformat(normalized)
        if dt.tzinfo is None:
            return dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc)
    except Exception:
        return None


def load_yaml(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {}
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    return data if isinstance(data, dict) else {}


def load_json(path: Path) -> Any:
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None


def load_matter_identity_payload() -> Dict[str, Any]:
    if not DEFAULT_MATTER_IDENTITY_MAP.exists():
        return {}

    with DEFAULT_MATTER_IDENTITY_MAP.open("r", encoding="utf-8") as handle:
        raw = yaml.safe_load(handle) or {}
    return raw if isinstance(raw, dict) else {}


def normalize_identity_token(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", (value or "").lower())


def is_viable_signal_token(token: str) -> bool:
    if len(token) < 4:
        return False
    if token in GENERIC_IDENTITY_KEYS:
        return False
    if not re.search(r"[a-z]", token):
        return False
    if token.endswith(("doc", "docx", "pdf", "msg", "xlsx", "pptx")):
        return False
    return True


def tokenize_identity_text(value: str) -> set[str]:
    return {
        token
        for token in re.split(r"[^a-z0-9]+", (value or "").lower())
        if token
    }


def extract_sender_email(sender: str) -> str:
    sender_low = (sender or "").strip().lower()
    match = re.search(r"[\w.+-]+@[\w.-]+\.\w+", sender_low)
    return match.group(0) if match else ""


def extract_sender_domain(sender: str) -> str:
    email = extract_sender_email(sender)
    if "@" not in email:
        return ""
    return email.split("@", 1)[1]


def merge_identity_indexes(*indexes: Dict[str, Dict[str, set[str]]]) -> Dict[str, Dict[str, set[str]]]:
    sender_map: Dict[str, set[str]] = {}
    domain_map: Dict[str, set[str]] = {}
    name_key_map: Dict[str, set[str]] = {}

    for current in indexes:
        for token, matters in (current.get("senders") or {}).items():
            sender_map.setdefault(token, set()).update(matters)
        for token, matters in (current.get("domains") or {}).items():
            domain_map.setdefault(token, set()).update(matters)
        for token, matters in (current.get("name_keys") or {}).items():
            name_key_map.setdefault(token, set()).update(matters)

    return {
        "senders": sender_map,
        "domains": domain_map,
        "name_keys": name_key_map,
    }


@lru_cache(maxsize=1)
def load_base_matter_identity_indexes() -> Dict[str, Dict[str, set[str]]]:
    raw = load_matter_identity_payload()

    sender_map: Dict[str, set[str]] = {}
    domain_map: Dict[str, set[str]] = {}
    name_key_map: Dict[str, set[str]] = {}

    for matter in raw.get("matters", []):
        matter_id = str(matter.get("matter_id") or "").strip()
        if not matter_id:
            continue
        aliases = (((matter.get("aliases") or {}).get("email")) or {})

        for sender in aliases.get("senders", []) or []:
            sender_norm = str(sender).strip().lower()
            if sender_norm:
                sender_map.setdefault(sender_norm, set()).add(matter_id)

        for domain in aliases.get("domains", []) or []:
            domain_norm = str(domain).strip().lower()
            if domain_norm:
                domain_map.setdefault(domain_norm, set()).add(matter_id)

        for name_key in aliases.get("name_keys", []) or []:
            token = normalize_identity_token(str(name_key))
            if token and token not in GENERIC_IDENTITY_KEYS:
                name_key_map.setdefault(token, set()).add(matter_id)

    return {
        "senders": sender_map,
        "domains": domain_map,
        "name_keys": name_key_map,
    }


@lru_cache(maxsize=1)
def load_brief_matter_signal_indexes() -> Dict[str, Dict[str, set[str]]]:
    raw = load_matter_identity_payload()
    name_key_map: Dict[str, set[str]] = defaultdict(set)

    for matter in raw.get("matters", []):
        if not isinstance(matter, dict):
            continue
        matter_id = str(matter.get("matter_id") or "").strip()
        if not matter_id:
            continue
        brief = matter.get("brief") if isinstance(matter.get("brief"), dict) else {}
        if not isinstance(brief, dict):
            brief = {}

        source_strings: List[str] = []
        matter_name = str(brief.get("matter_name") or "").strip()
        if matter_name:
            source_strings.append(matter_name)

        for list_key in ("client", "third_parties", "related_parties"):
            raw_values = brief.get(list_key)
            if not isinstance(raw_values, list):
                continue
            source_strings.extend(str(value).strip() for value in raw_values if str(value).strip())

        for source in source_strings:
            tokens = extract_path_signal_tokens(source)
            tokens.update(extract_text_signal_tokens(source))
            for token in tokens:
                if is_viable_signal_token(token):
                    name_key_map[token].add(matter_id)

    return {
        "senders": {},
        "domains": {},
        "name_keys": dict(name_key_map),
    }


def _add_signal_variants(target: set[str], raw_tokens: Iterable[str]) -> None:
    normalized_words = [normalize_identity_token(raw) for raw in raw_tokens if normalize_identity_token(raw)]
    filtered: List[str] = []
    for raw in raw_tokens:
        token = normalize_identity_token(raw)
        if not is_viable_signal_token(token):
            continue
        filtered.append(token)
        target.add(token)

    for left, right in zip(normalized_words, normalized_words[1:]):
        combo = normalize_identity_token(left + right)
        if is_viable_signal_token(combo):
            target.add(combo)

    if len(filtered) >= 2:
        combined = normalize_identity_token("".join(filtered))
        if is_viable_signal_token(combined):
            target.add(combined)


def extract_path_signal_tokens(value: str) -> set[str]:
    tokens: set[str] = set()
    cleaned = re.sub(r"\b\d{2}-\d{3,4}-\d{5}\b", " ", value or "")
    for phrase in PROPER_PHRASE_PATTERN.findall(cleaned):
        words = re.findall(r"[A-Za-z0-9&'.-]+", phrase)
        _add_signal_variants(tokens, words)
    for piece in re.split(r"[^A-Za-z0-9]+", cleaned):
        _add_signal_variants(tokens, [piece])
    return tokens


def extract_text_signal_tokens(value: str) -> set[str]:
    tokens: set[str] = set()
    cleaned = (value or "").replace("\u2028", " ").replace("\u2029", " ")
    for phrase in PROPER_PHRASE_PATTERN.findall(cleaned):
        words = re.findall(r"[A-Za-z0-9&'.-]+", phrase)
        if len(words) == 1:
            phrase_token = normalize_identity_token(words[0])
            if not (phrase.isupper() or re.search(r"[a-z].*[A-Z]|[A-Z].*[a-z].*[A-Z]", phrase)):
                continue
            if not is_viable_signal_token(phrase_token):
                continue
            tokens.add(phrase_token)
            continue

        normalized_words = [
            normalize_identity_token(word)
            for word in words
            if is_viable_signal_token(normalize_identity_token(word))
        ]
        if len(normalized_words) < 2:
            continue

        for left, right in zip(normalized_words, normalized_words[1:]):
            combo = normalize_identity_token(left + right)
            if is_viable_signal_token(combo):
                tokens.add(combo)

        full = normalize_identity_token("".join(normalized_words))
        if is_viable_signal_token(full):
            tokens.add(full)

        if not any(word in TEXT_PHRASE_GENERIC_WORDS for word in normalized_words):
            for word in normalized_words:
                if is_viable_signal_token(word):
                    tokens.add(word)
    return tokens


@lru_cache(maxsize=1)
def load_matter_related_numbers() -> Dict[str, set[str]]:
    matter_pattern = re.compile(r"\b\d{2}-\d{3,4}-\d{5}\b")
    related: Dict[str, set[str]] = {}

    for readme_path in MATTERS_ROOT.glob("**/README.md"):
        matter_number = readme_path.parent.name
        if not matter_pattern.fullmatch(matter_number):
            continue
        text = readme_path.read_text(encoding="utf-8")
        references = set(extract_matter_numbers(text, matter_pattern))
        references.discard(matter_number)
        if references:
            related[matter_number] = references

    return related


def extract_readme_description(text: str) -> str:
    lines = text.splitlines()
    for idx, line in enumerate(lines):
        if line.strip() != "## Description":
            continue
        for candidate in lines[idx + 1 :]:
            stripped = candidate.strip()
            if not stripped:
                continue
            if stripped.startswith("## "):
                return ""
            return stripped
    return ""


@lru_cache(maxsize=1)
def load_readme_matter_signal_indexes() -> Dict[str, Dict[str, set[str]]]:
    name_key_map: Dict[str, set[str]] = defaultdict(set)
    matter_pattern = re.compile(r"^\d{2}-\d{3,4}-\d{5}$")

    for readme_path in MATTERS_ROOT.glob("**/README.md"):
        matter_number = readme_path.parent.name
        if not matter_pattern.fullmatch(matter_number):
            continue

        text = readme_path.read_text(encoding="utf-8")
        title_match = re.search(r"(?m)^title:\s*(.+?)\s*$", text)
        heading_match = re.search(r"(?m)^#\s+(.+?)\s*$", text)
        description = extract_readme_description(text)

        source_strings = [
            value.strip()
            for value in (
                title_match.group(1) if title_match else "",
                heading_match.group(1) if heading_match else "",
                description,
            )
            if value and value.strip()
        ]

        for source in source_strings:
            tokens = extract_path_signal_tokens(source)
            tokens.update(extract_text_signal_tokens(source))
            for token in tokens:
                if is_viable_signal_token(token):
                    name_key_map[token].add(matter_number)

    return {
        "senders": {},
        "domains": {},
        "name_keys": dict(name_key_map),
    }


@lru_cache(maxsize=512)
def extract_sharepoint_text(path_str: str) -> str:
    path = Path(path_str)
    if not path.exists() or path.suffix.lower() not in DEFAULT_SHAREPOINT_SIGNAL_TEXT_EXTENSIONS:
        return ""
    try:
        result = subprocess.run(
            ["textutil", "-convert", "txt", "-stdout", str(path)],
            check=False,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="ignore",
        )
    except Exception:
        return ""
    if result.returncode != 0:
        return ""
    return result.stdout[:DEFAULT_SHAREPOINT_SIGNAL_TEXT_CHAR_LIMIT]


@lru_cache(maxsize=1)
def load_sharepoint_signal_indexes() -> Dict[str, Dict[str, set[str]]]:
    if not DEFAULT_SHAREPOINT_RAW_ROOT.exists():
        return {"senders": {}, "domains": {}, "name_keys": {}}

    raw = load_matter_identity_payload()
    matters = [entry for entry in raw.get("matters", []) if isinstance(entry, dict)]
    matter_numbers = {str(entry.get("matter_id") or "").strip() for entry in matters if str(entry.get("matter_id") or "").strip()}
    if not matter_numbers:
        return {"senders": {}, "domains": {}, "name_keys": {}}

    base_indexes = load_base_matter_identity_indexes()
    related_numbers = load_matter_related_numbers()
    matter_pattern = re.compile(r"\b\d{2}-\d{3,4}-\d{5}\b")

    alias_to_matters: Dict[str, set[str]] = defaultdict(set)
    for matter_number in matter_numbers:
        alias_to_matters[matter_number].add(matter_number)
        for alias in related_numbers.get(matter_number, set()):
            alias_to_matters[alias].add(matter_number)

    path_counts: Dict[str, Counter[str]] = defaultdict(Counter)
    text_counts: Dict[str, Counter[str]] = defaultdict(Counter)
    text_docs_loaded: Dict[str, int] = defaultdict(int)

    for raw_path in sorted(DEFAULT_SHAREPOINT_RAW_ROOT.rglob("*")):
        if not raw_path.is_file():
            continue

        display = display_path(raw_path)
        associated_matters: set[str] = set()
        for alias in extract_matter_numbers(display, matter_pattern):
            associated_matters.update(alias_to_matters.get(alias, set()))

        path_tokens = extract_path_signal_tokens(display)
        if not associated_matters and path_tokens:
            matched_by_name_key = {
                candidate
                for token in path_tokens
                for candidate in base_indexes["name_keys"].get(token, set())
                if candidate in matter_numbers
            }
            if len(matched_by_name_key) == 1:
                associated_matters = matched_by_name_key

        if not associated_matters:
            continue

        for matter_number in associated_matters:
            path_counts[matter_number].update(path_tokens)

        if raw_path.suffix.lower() not in DEFAULT_SHAREPOINT_SIGNAL_TEXT_EXTENSIONS:
            continue
        if not any(text_docs_loaded[matter_number] < DEFAULT_SHAREPOINT_SIGNAL_TEXT_DOC_LIMIT for matter_number in associated_matters):
            continue

        doc_text = extract_sharepoint_text(str(raw_path))
        if not doc_text.strip():
            continue
        text_tokens = extract_text_signal_tokens(doc_text)
        if not text_tokens:
            continue

        for matter_number in associated_matters:
            if text_docs_loaded[matter_number] >= DEFAULT_SHAREPOINT_SIGNAL_TEXT_DOC_LIMIT:
                continue
            text_counts[matter_number].update(text_tokens)
            text_docs_loaded[matter_number] += 1

    name_key_map: Dict[str, set[str]] = defaultdict(set)
    for matter_number in matter_numbers:
        selected_tokens = {
            token
            for token, count in path_counts[matter_number].items()
            if count >= 1 and token not in GENERIC_IDENTITY_KEYS
        }
        selected_tokens.update(
            token
            for token, count in text_counts[matter_number].items()
            if token not in GENERIC_IDENTITY_KEYS
            and (count >= 2 or token in path_counts[matter_number])
        )
        for token in selected_tokens:
            name_key_map[token].add(matter_number)

    return {
        "senders": {},
        "domains": {},
        "name_keys": dict(name_key_map),
    }


@lru_cache(maxsize=1)
def load_matter_identity_indexes() -> Dict[str, Dict[str, set[str]]]:
    return merge_identity_indexes(
        load_base_matter_identity_indexes(),
        load_brief_matter_signal_indexes(),
        load_readme_matter_signal_indexes(),
        load_sharepoint_signal_indexes(),
    )


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def display_path(path: Path) -> str:
    """Return repo-relative path when possible, else absolute path string."""
    try:
        return str(path.resolve().relative_to(REPO_ROOT.resolve()))
    except Exception:
        return str(path)


def normalize_token(value: str) -> str:
    return str(value or "").strip().lower()


def merge_delivery_taxonomy(raw_config: Dict[str, Any]) -> Dict[str, Any]:
    merged = json.loads(json.dumps(DEFAULT_DELIVERY_TAXONOMY))
    if not isinstance(raw_config, dict):
        return merged

    for section_key in ("delivery_categories", "service_model"):
        section = raw_config.get(section_key)
        if not isinstance(section, dict):
            continue
        target = merged.setdefault(section_key, {})
        for key, value in section.items():
            if isinstance(value, dict) and isinstance(target.get(key), dict):
                target[key].update(value)
            else:
                target[key] = value
    return merged


def service_alias_map(delivery_taxonomy: Dict[str, Any]) -> Dict[str, str]:
    model = delivery_taxonomy.get("service_model") if isinstance(delivery_taxonomy, dict) else {}
    legacy = model.get("legacy_alias_fields") if isinstance(model, dict) else {}
    if not isinstance(legacy, dict):
        legacy = {}

    normalized = {str(field): str(service_type) for field, service_type in legacy.items()}
    if not normalized:
        normalized = {"solutions": "solution", "strategies": "strategy"}
    return normalized


def accepted_service_types(delivery_taxonomy: Dict[str, Any]) -> set[str]:
    model = delivery_taxonomy.get("service_model") if isinstance(delivery_taxonomy, dict) else {}
    raw_types = model.get("accepted_service_types") if isinstance(model, dict) else []
    if not isinstance(raw_types, list):
        raw_types = []
    normalized = {normalize_token(entry) for entry in raw_types if str(entry).strip()}
    if not normalized:
        normalized = {"solution", "strategy"}
    return normalized


def normalize_services(raw: Dict[str, Any], delivery_taxonomy: Dict[str, Any]) -> Tuple[ServiceRef, ...]:
    alias_fields = service_alias_map(delivery_taxonomy)
    valid_types = accepted_service_types(delivery_taxonomy)
    entries: List[ServiceRef] = []

    def parse_entry(entry: Any, default_type: str) -> Optional[ServiceRef]:
        if isinstance(entry, dict):
            service_type = str(entry.get("service_type") or entry.get("type") or default_type).strip().lower()
            service_name = str(entry.get("service_name") or entry.get("name") or entry.get("id") or "").strip()
            status = str(entry.get("status") or "active").strip().lower()
            playbook_ref = str(entry.get("playbook_ref") or entry.get("playbook") or "").strip()
        elif isinstance(entry, str):
            service_type = default_type.strip().lower()
            service_name = entry.strip()
            status = "active"
            playbook_ref = ""
        else:
            return None

        if not service_name:
            return None
        if valid_types and service_type not in valid_types:
            service_type = default_type.strip().lower() or "solution"
        if service_type not in valid_types:
            service_type = "solution"

        return ServiceRef(
            service_type=service_type,
            service_name=service_name,
            status=status or "active",
            playbook_ref=playbook_ref,
        )

    canonical_field = str(
        ((delivery_taxonomy.get("service_model") or {}).get("canonical_field"))
        or "services"
    )
    raw_services = raw.get(canonical_field)
    if isinstance(raw_services, list):
        for entry in raw_services:
            parsed = parse_entry(entry, "solution")
            if parsed:
                entries.append(parsed)

    for field_name, forced_type in alias_fields.items():
        raw_field = raw.get(field_name)
        if not isinstance(raw_field, list):
            continue
        for entry in raw_field:
            parsed = parse_entry(entry, forced_type)
            if parsed:
                entries.append(parsed)

    deduped: Dict[Tuple[str, str, str, str], ServiceRef] = {}
    for entry in entries:
        key = (
            normalize_token(entry.service_type),
            normalize_token(entry.service_name),
            normalize_token(entry.status),
            normalize_token(entry.playbook_ref),
        )
        deduped[key] = entry

    return tuple(
        sorted(
            deduped.values(),
            key=lambda ref: (
                ref.service_type.lower(),
                ref.service_name.lower(),
                ref.status.lower(),
                ref.playbook_ref.lower(),
            ),
        )
    )


def merge_services(*service_groups: Tuple[ServiceRef, ...]) -> Tuple[ServiceRef, ...]:
    deduped: Dict[Tuple[str, str, str, str], ServiceRef] = {}
    for group in service_groups:
        for service in group:
            key = (
                normalize_token(service.service_type),
                normalize_token(service.service_name),
                normalize_token(service.status),
                normalize_token(service.playbook_ref),
            )
            deduped[key] = service
    return tuple(
        sorted(
            deduped.values(),
            key=lambda ref: (
                ref.service_type.lower(),
                ref.service_name.lower(),
                ref.status.lower(),
                ref.playbook_ref.lower(),
            ),
        )
    )


def service_summary(services: Tuple[ServiceRef, ...], max_items: int = 3) -> str:
    if not services:
        return "0"

    labels = [f"{entry.service_type}:{entry.service_name}" for entry in services]
    shown = labels[:max_items]
    suffix = ""
    if len(labels) > max_items:
        suffix = f"; +{len(labels) - max_items} more"
    return f"{len(labels)} ({'; '.join(shown)}{suffix})"


def matter_matches_rule(matter: MatterRef, rule: Dict[str, Any]) -> bool:
    def _as_set(name: str) -> set[str]:
        raw_values = rule.get(name)
        if not isinstance(raw_values, list):
            return set()
        return {normalize_token(value) for value in raw_values if str(value).strip()}

    status_set = _as_set("status_include")
    delivery_set = _as_set("delivery_status_include")
    fulfillment_set = _as_set("fulfillment_status_include")

    status_value = normalize_token(matter.status)
    delivery_value = normalize_token(matter.delivery_status)
    fulfillment_value = normalize_token(matter.fulfillment_status)

    if status_set and status_value not in status_set:
        return False
    if delivery_set and delivery_value not in delivery_set:
        return False
    if fulfillment_set and fulfillment_value not in fulfillment_set:
        return False
    return True


def classify_delivery_category(matter: MatterRef, delivery_taxonomy: Dict[str, Any]) -> Tuple[str, str]:
    categories = delivery_taxonomy.get("delivery_categories") if isinstance(delivery_taxonomy, dict) else {}
    if not isinstance(categories, dict):
        categories = {}

    for category_key, category_rule in categories.items():
        if not isinstance(category_rule, dict):
            continue
        if matter_matches_rule(matter, category_rule):
            label = str(category_rule.get("label") or category_key).strip() or category_key
            return category_key, label

    return "other", "Other"


def extract_participants(raw_participants: Any, fallback_from: str = "", fallback_to: str = "") -> Tuple[str, ...]:
    participants: List[str] = []

    if isinstance(raw_participants, list):
        for item in raw_participants:
            if isinstance(item, dict):
                email = str(item.get("email") or "").strip()
                name = str(item.get("name") or "").strip()
                if email:
                    participants.append(email.lower())
                elif name:
                    participants.append(name)
            elif isinstance(item, str):
                item = item.strip()
                if item:
                    participants.append(item.lower())

    for fallback in (fallback_from, fallback_to):
        if fallback:
            participants.append(fallback.lower())

    unique = sorted({p for p in participants if p})
    return tuple(unique)


def header_value(headers: Any, name: str) -> str:
    if not isinstance(headers, list):
        return ""
    for header in headers:
        if not isinstance(header, dict):
            continue
        if str(header.get("name") or "").lower() == name.lower():
            return str(header.get("value") or "").strip()
    return ""


def derive_state_labels(labels: Iterable[str]) -> Tuple[str, ...]:
    normalized = {
        LEGACY_STATE_LABEL_ALIASES.get(label, label)
        for label in labels
    }
    return tuple(sorted({label for label in normalized if label in CANONICAL_STATE_LABELS}))


def is_automated_sender(sender: str) -> bool:
    sender_low = sender.lower()
    return any(signal in sender_low for signal in AUTOMATED_SENDER_SIGNALS)


def classify_review_state(thread: ThreadRef, has_matter: bool) -> Tuple[str, str]:
    sender_low = thread.sender.lower()
    label_names_low = {label.lower() for label in thread.labels}

    if CALENDAR_SENDER in sender_low:
        return "50_Calendar", "calendar_sender"

    if has_matter:
        if is_automated_sender(thread.sender):
            return "60_Filing", "matter_thread_automated_sender"
        return "10_Action_Matthew", "matter_thread_human_sender"

    if any(signal in sender_low for signal in TEAM_SIGNALS):
        return "20_Action_Team", "team_sender"

    if any(signal in sender_low for signal in ADMIN_SIGNALS):
        return "20_Action_Team", "admin_vendor_sender"

    if "category_promotions" in label_names_low:
        return "80_Junk_to_Review", "promotions_category"

    if thread.last_sender and thread.last_sender.lower() in MATTHEW_EMAILS and thread.message_count >= 2:
        return "40_Replied_Awaiting_Response", "ml1_replied_last"

    if any(signal in sender_low for signal in LEGAL_SIGNALS):
        return "10_Action_Matthew", "legal_sender_signal"

    return "00_Triage", "default_triage"


def is_review_candidate(thread: ThreadRef) -> bool:
    if len(thread.state_labels) > 1:
        return True
    if not thread.state_labels:
        return True
    return thread.state_labels == ("00_Triage",)


def normalize_live_thread(thread: Dict[str, Any], label_id_to_name: Dict[str, str]) -> ThreadRef:
    messages = thread.get("messages", []) if isinstance(thread.get("messages"), list) else []
    first = messages[0] if messages else {}
    last = messages[-1] if messages else {}
    first_headers = ((first.get("payload") or {}).get("headers")) if isinstance(first, dict) else []
    last_headers = ((last.get("payload") or {}).get("headers")) if isinstance(last, dict) else []

    label_ids = set()
    for message in messages:
        if not isinstance(message, dict):
            continue
        for label_id in message.get("labelIds", []) or []:
            label_ids.add(str(label_id))

    label_names = tuple(sorted({label_id_to_name.get(label_id, label_id) for label_id in label_ids if label_id}))
    subject = header_value(last_headers, "Subject") or header_value(first_headers, "Subject") or "(no subject)"
    sender = header_value(first_headers, "From") or header_value(last_headers, "From")
    last_sender = header_value(last_headers, "From") or sender
    to_value = header_value(last_headers, "To") or header_value(first_headers, "To")
    last_message_raw = ""
    if isinstance(last, dict):
        last_message_raw = str(last.get("internalDate") or "").strip()
    last_message_at = utc_iso(parse_timestamp(last_message_raw)) if last_message_raw else ""

    return ThreadRef(
        thread_id=str(thread.get("id") or "").strip(),
        subject=subject,
        participants=extract_participants([], fallback_from=sender, fallback_to=to_value),
        last_message_at=last_message_at,
        labels=label_names,
        latest_snippet=str(thread.get("snippet") or "").strip(),
        source_pointer=f"gmail://thread/{str(thread.get('id') or '').strip()}",
        sender=sender,
        last_sender=last_sender,
        message_count=len(messages),
        state_labels=derive_state_labels(label_names),
    )


def load_live_gmail_threads(query: str, max_review_threads: int) -> Tuple[List[ThreadRef], str, Dict[str, Any]]:
    from gmail_mcp_server import _get_gmail_service, _label_id_to_name, _list_all_labels

    service = _get_gmail_service()
    labels = _list_all_labels(service)
    label_id_to_name = _label_id_to_name(labels)

    selected: List[ThreadRef] = []
    page_token: Optional[str] = None
    listed_threads = 0
    inspected_threads = 0
    capped = max_review_threads > 0
    max_inspected = max(max_review_threads * 10, 100) if capped else None

    while True:
        if max_inspected is not None and listed_threads >= max_inspected:
            break

        kwargs: Dict[str, Any] = {
            "userId": "me",
            "q": query,
            "maxResults": min(((max_inspected - listed_threads) if max_inspected is not None else 100), 100),
        }
        if page_token:
            kwargs["pageToken"] = page_token

        response = service.users().threads().list(**kwargs).execute()
        thread_stubs = response.get("threads", [])
        if not thread_stubs:
            break

        for stub in thread_stubs:
            thread_id = str(stub.get("id") or "").strip()
            if not thread_id:
                continue

            listed_threads += 1
            thread = service.users().threads().get(userId="me", id=thread_id).execute()
            normalized = normalize_live_thread(thread, label_id_to_name)
            inspected_threads += 1

            if not is_review_candidate(normalized):
                if capped and max_inspected is not None and listed_threads >= max_inspected:
                    break
                continue

            selected.append(normalized)
            if capped and len(selected) >= max_review_threads:
                break

        if capped and len(selected) >= max_review_threads:
            break

        page_token = response.get("nextPageToken")
        if not page_token:
            break

    selection_summary = {
        "query": query,
        "listed_threads": listed_threads,
        "inspected_threads": inspected_threads,
        "reviewed_threads": len(selected),
    }
    return selected, f"live:{query}", selection_summary


def discover_local_matter_paths() -> Dict[str, Path]:
    """Map matter number to local `05_MATTERS/<tier>/<matter>` path."""
    mapping: Dict[str, Path] = {}

    for tier in MATTER_TIERS:
        tier_dir = MATTERS_ROOT / tier
        if not tier_dir.exists():
            continue
        for matter_dir in sorted(p for p in tier_dir.iterdir() if p.is_dir()):
            matter_yaml = matter_dir / "MATTER.yaml"
            matter_number = matter_dir.name
            if matter_yaml.exists():
                data = yaml.safe_load(matter_yaml.read_text(encoding="utf-8")) or {}
                matter_number = str(data.get("matter_id") or matter_number).strip() or matter_number
            mapping[matter_number] = matter_dir

    return mapping


def load_local_matter_overlay(delivery_taxonomy: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    """Load local matter metadata from MATTER.yaml for deterministic enrichment."""
    overlay: Dict[str, Dict[str, Any]] = {}

    for matter_yaml in sorted(MATTERS_ROOT.glob("*/**/MATTER.yaml")):
        if matter_yaml.parent.parent.name not in MATTER_TIERS:
            continue
        data = yaml.safe_load(matter_yaml.read_text(encoding="utf-8")) or {}
        matter_number = str(data.get("matter_id") or matter_yaml.parent.name).strip()
        if not matter_number:
            continue

        name = str(data.get("matter_name") or data.get("name") or matter_yaml.parent.name).strip() or matter_number
        status = str(data.get("status") or "unknown").strip()
        delivery_status = str(data.get("delivery_status") or matter_yaml.parent.parent.name.title()).strip()
        fulfillment_status = str(data.get("fulfillment_status") or "unknown").strip()
        services = normalize_services(data, delivery_taxonomy)
        source_pointer = f"repo://{display_path(matter_yaml)}"

        overlay[matter_number] = {
            "name": name,
            "status": status,
            "delivery_status": delivery_status,
            "fulfillment_status": fulfillment_status,
            "services": services,
            "client": name,
            "source_pointer": source_pointer,
        }

    return overlay


def normalize_matter_record(raw: Dict[str, Any], source_pointer: str, delivery_taxonomy: Dict[str, Any]) -> Optional[MatterRef]:
    matter_number = str(
        raw.get("matter_number")
        or raw.get("display_number")
        or raw.get("matter_id")
        or raw.get("id")
        or ""
    ).strip()
    if not matter_number:
        return None

    clio_matter_id = str(raw.get("clio_matter_id") or raw.get("id") or matter_number).strip()
    name = str(raw.get("name") or raw.get("description") or raw.get("matter_name") or "").strip() or matter_number
    status = str(raw.get("status") or "unknown").strip()
    delivery_status = str(raw.get("delivery_status") or "unknown").strip()
    fulfillment_status = str(raw.get("fulfillment_status") or "unknown").strip()
    services = normalize_services(raw, delivery_taxonomy)
    responsible = str(raw.get("responsible") or raw.get("responsible_attorney") or "unassigned").strip()
    client = str(raw.get("client") or raw.get("matter_name") or name).strip()

    return MatterRef(
        clio_matter_id=clio_matter_id,
        matter_number=matter_number,
        name=name,
        status=status,
        delivery_status=delivery_status,
        fulfillment_status=fulfillment_status,
        services=services,
        responsible=responsible,
        client=client,
        source_pointer=source_pointer,
    )


def load_clio_matters(clio_cache_path: Path, write_cache: bool, delivery_taxonomy: Dict[str, Any]) -> Tuple[List[MatterRef], str]:
    """Load normalized MatterRef records from cache or repo fallback."""
    matters: List[MatterRef] = []
    local_overlay = load_local_matter_overlay(delivery_taxonomy)
    cache_payload = load_json(clio_cache_path)

    if cache_payload is not None:
        records = cache_payload.get("matters") if isinstance(cache_payload, dict) else cache_payload
        if isinstance(records, list):
            for idx, record in enumerate(records):
                if not isinstance(record, dict):
                    continue
                pointer = str(record.get("source_pointer") or f"cache://clio_matters.json#{idx}")
                normalized = normalize_matter_record(record, pointer, delivery_taxonomy)
                if normalized:
                    matters.append(normalized)
        source = f"cache:{display_path(clio_cache_path)}"
        if isinstance(cache_payload, dict):
            declared_source = str(cache_payload.get("source") or "").strip()
            if declared_source:
                source = f"{source} ({declared_source})"
    else:
        # Repo fallback: derive MatterRef from local MATTER.yaml files.
        for matter_yaml in sorted(MATTERS_ROOT.glob("*/**/MATTER.yaml")):
            if matter_yaml.parent.parent.name not in MATTER_TIERS:
                continue
            data = yaml.safe_load(matter_yaml.read_text(encoding="utf-8")) or {}
            pointer = f"repo://{display_path(matter_yaml)}"
            normalized = normalize_matter_record(data, pointer, delivery_taxonomy)
            if normalized:
                matters.append(normalized)
        source = "repo_fallback:05_MATTERS"

        if write_cache:
            payload = {
                "generated_at": utc_iso(),
                "source": source,
                "matters": [
                    {
                        "clio_matter_id": m.clio_matter_id,
                        "matter_number": m.matter_number,
                        "name": m.name,
                        "status": m.status,
                        "delivery_status": m.delivery_status,
                        "fulfillment_status": m.fulfillment_status,
                        "services": [
                            {
                                "service_type": service.service_type,
                                "service_name": service.service_name,
                                "status": service.status,
                                "playbook_ref": service.playbook_ref,
                            }
                            for service in m.services
                        ],
                        "responsible": m.responsible,
                        "client": m.client,
                        "source_pointer": m.source_pointer,
                    }
                    for m in matters
                ],
            }
            write_json(clio_cache_path, payload)

    # Clio/cache records are not always complete and may retain stale matter
    # numbers. Keep the dashboard inventory aligned to local MATTER.yaml files.
    if local_overlay:
        matters = [matter for matter in matters if matter.matter_number in local_overlay]

    # Treat local MATTER.yaml files as additive fallback records so dashboards
    # remain repo-complete.
    cached_numbers = {matter.matter_number for matter in matters}
    added_local = 0
    for matter_number, overlay in sorted(local_overlay.items()):
        if matter_number in cached_numbers:
            continue
        normalized = normalize_matter_record(
            {
                "matter_number": matter_number,
                "clio_matter_id": matter_number,
                "name": overlay.get("name"),
                "status": overlay.get("status"),
                "delivery_status": overlay.get("delivery_status"),
                "fulfillment_status": overlay.get("fulfillment_status"),
                "services": overlay.get("services"),
                "client": overlay.get("client"),
                "source_pointer": overlay.get("source_pointer"),
            },
            str(overlay.get("source_pointer") or f"repo://05_MATTERS/{matter_number}/MATTER.yaml"),
            delivery_taxonomy,
        )
        if normalized:
            matters.append(normalized)
            added_local += 1

    if added_local:
        source = f"{source} + repo_fallback:05_MATTERS"

    # Deduplicate by matter_number deterministically.
    deduped: Dict[str, MatterRef] = {}
    for matter in matters:
        deduped[matter.matter_number] = matter

    ordered = sorted(deduped.values(), key=lambda m: (m.matter_number, m.clio_matter_id))
    enriched: List[MatterRef] = []
    for matter in ordered:
        overlay = local_overlay.get(matter.matter_number, {})
        overlay_name = str(overlay.get("name") or "").strip()
        overlay_status = str(overlay.get("status") or "").strip()
        overlay_delivery = str(overlay.get("delivery_status") or "").strip()
        overlay_fulfillment = str(overlay.get("fulfillment_status") or "").strip()
        overlay_services = overlay.get("services") if isinstance(overlay.get("services"), tuple) else tuple()
        overlay_client = str(overlay.get("client") or "").strip()
        overlay_pointer = str(overlay.get("source_pointer") or "").strip()

        enriched.append(
            MatterRef(
                clio_matter_id=matter.clio_matter_id,
                matter_number=matter.matter_number,
                name=(matter.name if matter.name and matter.name != matter.matter_number else overlay_name or matter.name),
                status=(matter.status if matter.status and matter.status.lower() != "unknown" else overlay_status or matter.status),
                delivery_status=(
                    matter.delivery_status
                    if matter.delivery_status and matter.delivery_status.lower() != "unknown"
                    else overlay_delivery or matter.delivery_status
                ),
                fulfillment_status=(
                    matter.fulfillment_status
                    if matter.fulfillment_status and matter.fulfillment_status.lower() != "unknown"
                    else overlay_fulfillment or matter.fulfillment_status
                ),
                services=merge_services(matter.services, overlay_services),
                responsible=matter.responsible,
                client=(matter.client if matter.client and matter.client != matter.name else overlay_client or matter.client),
                source_pointer=overlay_pointer or matter.source_pointer,
            )
        )

    return enriched, source


def normalize_cached_threads(raw_threads: Iterable[Any], default_pointer_prefix: str) -> List[ThreadRef]:
    threads: List[ThreadRef] = []

    for idx, raw in enumerate(raw_threads):
        if not isinstance(raw, dict):
            continue

        thread_id = str(raw.get("thread_id") or raw.get("id") or "").strip()
        if not thread_id:
            continue

        subject = str(raw.get("subject") or "").strip()
        labels_raw = raw.get("labels") or raw.get("label_ids") or []
        labels = tuple(sorted({str(label).strip() for label in labels_raw if str(label).strip()}))

        participants = extract_participants(
            raw.get("participants"),
            fallback_from=str(raw.get("from") or ""),
            fallback_to=str(raw.get("to") or ""),
        )

        ts = parse_timestamp(raw.get("last_message_at") or raw.get("last_internal_date") or raw.get("internal_date"))
        last_message_at = utc_iso(ts) if ts else ""

        latest_snippet = str(raw.get("latest_snippet") or raw.get("snippet") or "").strip()
        source_pointer = str(raw.get("source_pointer") or f"{default_pointer_prefix}#{thread_id or idx}")
        state_labels = derive_state_labels(labels)

        threads.append(
            ThreadRef(
                thread_id=thread_id,
                subject=subject,
                participants=participants,
                last_message_at=last_message_at,
                labels=labels,
                latest_snippet=latest_snippet,
                source_pointer=source_pointer,
                sender=str(raw.get("sender") or raw.get("from") or "").strip(),
                last_sender=str(raw.get("last_sender") or raw.get("sender") or raw.get("from") or "").strip(),
                message_count=int(raw.get("message_count") or 0),
                state_labels=state_labels,
            )
        )

    # Latest first, then thread ID for deterministic tie-break.
    return sorted(threads, key=lambda t: (t.last_message_at, t.thread_id), reverse=True)


def normalize_threads_from_email_dump(email_dump: Dict[str, Any], pointer_path: Path) -> List[ThreadRef]:
    emails = email_dump.get("emails") if isinstance(email_dump, dict) else None
    if not isinstance(emails, list):
        return []

    grouped: Dict[str, List[Dict[str, Any]]] = {}
    for email in emails:
        if not isinstance(email, dict):
            continue
        thread_id = str(
            email.get("thread_id")
            or email.get("threadId")
            or email.get("id")
            or email.get("message_id")
            or ""
        ).strip()
        if not thread_id:
            continue
        grouped.setdefault(thread_id, []).append(email)

    threads: List[ThreadRef] = []
    for thread_id, items in grouped.items():
        items_sorted = sorted(
            items,
            key=lambda entry: (
                parse_timestamp(entry.get("internal_date") or entry.get("date")) or datetime.fromtimestamp(0, tz=timezone.utc),
                str(entry.get("id") or ""),
            ),
        )
        latest = items_sorted[-1]

        labels: List[str] = []
        participants: List[str] = []
        for entry in items_sorted:
            for label in entry.get("labels", []) or entry.get("label_ids", []) or []:
                label_value = str(label).strip()
                if label_value:
                    labels.append(label_value)

            part_tuple = extract_participants(
                entry.get("participants"),
                fallback_from=str(entry.get("from") or ""),
                fallback_to=str(entry.get("to") or ""),
            )
            participants.extend(part_tuple)

        dt = parse_timestamp(latest.get("internal_date") or latest.get("date"))
        last_message_at = utc_iso(dt) if dt else ""
        state_labels = derive_state_labels(labels)

        threads.append(
            ThreadRef(
                thread_id=thread_id,
                subject=str(latest.get("subject") or "").strip(),
                participants=tuple(sorted(set(participants))),
                last_message_at=last_message_at,
                labels=tuple(sorted(set(labels))),
                latest_snippet=str(latest.get("snippet") or latest.get("body") or "").strip(),
                source_pointer=f"repo://{display_path(pointer_path)}#thread:{thread_id}",
                sender=str(items_sorted[0].get("from") or "").strip(),
                last_sender=str(latest.get("from") or "").strip(),
                message_count=len(items_sorted),
                state_labels=state_labels,
            )
        )

    return sorted(threads, key=lambda t: (t.last_message_at, t.thread_id), reverse=True)


def load_gmail_threads(
    gmail_cache_path: Path,
    gmail_fallback_path: Path,
    write_cache: bool,
) -> Tuple[List[ThreadRef], str]:
    """Load normalized ThreadRef records from cache or local Gmail dump."""
    cache_payload = load_json(gmail_cache_path)
    if cache_payload is not None:
        records = cache_payload.get("threads") if isinstance(cache_payload, dict) else cache_payload
        threads = normalize_cached_threads(records or [], "cache://gmail_threads.json")
        return threads, f"cache:{display_path(gmail_cache_path)}"

    fallback_payload = load_json(gmail_fallback_path)
    if fallback_payload is None:
        return [], "none"

    threads = normalize_threads_from_email_dump(fallback_payload, gmail_fallback_path)
    source = f"repo:{display_path(gmail_fallback_path)}"

    if write_cache:
        payload = {
            "generated_at": utc_iso(),
            "source": source,
            "threads": [
                {
                    "thread_id": t.thread_id,
                    "subject": t.subject,
                    "participants": list(t.participants),
                    "last_message_at": t.last_message_at,
                    "labels": list(t.labels),
                    "latest_snippet": t.latest_snippet,
                    "source_pointer": t.source_pointer,
                }
                for t in threads
            ],
        }
        write_json(gmail_cache_path, payload)

    return threads, source


def normalize_sharepoint_record(raw: Dict[str, Any], source_pointer: str) -> Optional[DocRef]:
    drive_item_id = str(raw.get("drive_item_id") or raw.get("id") or "").strip()
    name = str(raw.get("name") or "").strip()
    if not drive_item_id and not name:
        return None

    raw_path = str(raw.get("path") or "").strip().strip("/")
    if raw_path and name and raw_path.endswith("/" + name):
        full_path = raw_path
    elif raw_path and (raw_path == name):
        full_path = raw_path
    else:
        parent_path = ""
        parent_reference = raw.get("parentReference") if isinstance(raw.get("parentReference"), dict) else {}
        if isinstance(parent_reference, dict):
            parent_path = str(parent_reference.get("path") or "").strip()
        if ":" in parent_path:
            parent_path = parent_path.split(":", 1)[1]
        parent_path = parent_path.strip().strip("/")
        full_path = "/".join(part for part in (parent_path, name) if part)

    modified_raw = raw.get("modified_at") or raw.get("lastModifiedDateTime") or raw.get("last_modified")
    modified_dt = parse_timestamp(modified_raw)
    modified_at = utc_iso(modified_dt) if modified_dt else str(modified_raw or "").strip()

    size_raw = raw.get("size") if raw.get("size") is not None else raw.get("size_bytes")
    try:
        size = int(size_raw or 0)
    except Exception:
        size = 0

    author = str(raw.get("author") or "").strip()
    if not author:
        last_modified_by = raw.get("lastModifiedBy") if isinstance(raw.get("lastModifiedBy"), dict) else {}
        user = last_modified_by.get("user") if isinstance(last_modified_by, dict) else {}
        if isinstance(user, dict):
            author = str(user.get("displayName") or user.get("email") or "").strip()

    parent_reference = raw.get("parentReference") if isinstance(raw.get("parentReference"), dict) else {}
    drive_id = str(raw.get("drive_id") or parent_reference.get("driveId") or "").strip()
    web_url = str(raw.get("web_url") or raw.get("webUrl") or "").strip()

    is_folder = bool(raw.get("is_folder"))
    if not is_folder and isinstance(raw.get("folder"), dict):
        is_folder = True

    return DocRef(
        drive_item_id=drive_item_id or full_path or name,
        path=full_path or name or drive_item_id,
        name=name or full_path or drive_item_id,
        modified_at=modified_at,
        size=size,
        web_url=web_url,
        author=author,
        drive_id=drive_id,
        is_folder=is_folder,
        source_pointer=source_pointer,
    )


def normalize_sharepoint_docs_from_records(raw_docs: Iterable[Any], default_pointer_prefix: str) -> List[DocRef]:
    docs: List[DocRef] = []
    for idx, raw in enumerate(raw_docs):
        if not isinstance(raw, dict):
            continue
        pointer = str(raw.get("source_pointer") or f"{default_pointer_prefix}#{idx}")
        normalized = normalize_sharepoint_record(raw, pointer)
        if normalized:
            docs.append(normalized)
    deduped: Dict[str, DocRef] = {}
    for doc in docs:
        key = f"{doc.drive_item_id}|{doc.path}"
        deduped[key] = doc
    return sorted(deduped.values(), key=lambda d: (d.path.lower(), d.drive_item_id))


def load_sharepoint_docs_from_metadata(metadata_root: Path) -> Tuple[List[DocRef], str]:
    if not metadata_root.exists():
        return [], "none"
    json_files = sorted(metadata_root.glob("*.json"))
    if not json_files:
        return [], "none"

    docs: List[DocRef] = []
    for meta_path in json_files:
        payload = load_json(meta_path)
        if not isinstance(payload, dict):
            continue
        pointer = f"repo://{display_path(meta_path)}"
        drive_item_id = str(payload.get("id") or "").strip()
        if drive_item_id:
            pointer = f"{pointer}#item:{drive_item_id}"
        normalized = normalize_sharepoint_record(payload, pointer)
        if normalized:
            docs.append(normalized)

    deduped: Dict[str, DocRef] = {}
    for doc in docs:
        key = f"{doc.drive_item_id}|{doc.path}"
        deduped[key] = doc

    return (
        sorted(deduped.values(), key=lambda d: (d.path.lower(), d.drive_item_id)),
        f"repo:{display_path(metadata_root)}",
    )


def load_sharepoint_docs_from_cache_payload(cache_payload: Any) -> List[DocRef]:
    records: Any = []
    if isinstance(cache_payload, dict):
        if isinstance(cache_payload.get("docs"), list):
            records = cache_payload.get("docs")
        elif isinstance(cache_payload.get("files"), list):
            records = cache_payload.get("files")
    elif isinstance(cache_payload, list):
        records = cache_payload

    if not isinstance(records, list):
        return []
    return normalize_sharepoint_docs_from_records(records, "cache://sharepoint_files.json")


def load_sharepoint_docs(
    sharepoint_cache_path: Path,
    metadata_root: Path,
) -> Tuple[List[DocRef], List[DocRef], str, str, str]:
    cache_payload = load_json(sharepoint_cache_path)
    previous_docs = load_sharepoint_docs_from_cache_payload(cache_payload)
    previous_generated_at = (
        str(cache_payload.get("generated_at") or "").strip()
        if isinstance(cache_payload, dict)
        else ""
    )
    cache_source = f"cache:{display_path(sharepoint_cache_path)}" if previous_docs else "none"

    current_docs, current_source = load_sharepoint_docs_from_metadata(metadata_root)
    if current_docs:
        return current_docs, previous_docs, current_source, cache_source, previous_generated_at

    if previous_docs:
        return previous_docs, previous_docs, cache_source, cache_source, previous_generated_at

    return [], [], "none", "none", previous_generated_at


def load_matter_sharepoint_map(path: Path) -> List[Dict[str, str]]:
    payload = load_yaml(path)
    records = payload.get("mappings") if isinstance(payload, dict) else []
    if not isinstance(records, list):
        return []

    normalized: List[Dict[str, str]] = []
    for entry in records:
        if not isinstance(entry, dict):
            continue
        matter_number = str(entry.get("matter_number") or "").strip()
        if not matter_number:
            continue
        normalized.append(
            {
                "matter_number": matter_number,
                "drive_item_id": str(entry.get("drive_item_id") or "").strip(),
                "path": str(entry.get("path") or "").strip().strip("/"),
                "web_url": str(entry.get("web_url") or "").strip(),
            }
        )

    return sorted(
        normalized,
        key=lambda row: (
            row["matter_number"],
            row["path"],
            row["drive_item_id"],
            row["web_url"],
        ),
    )


def load_expected_sharepoint_folders(path: Path) -> List[str]:
    payload = load_yaml(path)
    sharepoint_mapping = payload.get("sharepoint_mapping") if isinstance(payload, dict) else {}
    expected = sharepoint_mapping.get("expected_subfolders") if isinstance(sharepoint_mapping, dict) else []
    if not isinstance(expected, list):
        return []
    return [str(value).strip() for value in expected if str(value).strip()]


def map_sharepoint_docs_to_matters(
    docs: List[DocRef],
    matter_numbers: set[str],
    matter_pattern: re.Pattern[str],
    explicit_mappings: List[Dict[str, str]],
    single_matter_scope: Optional[str],
) -> Tuple[List[Dict[str, Any]], List[Dict[str, str]], List[Dict[str, str]]]:
    resolved_rows: List[Dict[str, Any]] = []
    unmapped_rows: List[Dict[str, str]] = []
    ambiguous_rows: List[Dict[str, str]] = []

    mappings_by_item_id: Dict[str, List[Dict[str, str]]] = defaultdict(list)
    path_mappings: List[Dict[str, str]] = []
    web_mappings: List[Dict[str, str]] = []
    for mapping in explicit_mappings:
        drive_item_id = mapping.get("drive_item_id", "")
        if drive_item_id:
            mappings_by_item_id[drive_item_id].append(mapping)
        if mapping.get("path"):
            path_mappings.append(mapping)
        if mapping.get("web_url"):
            web_mappings.append(mapping)

    path_mappings = sorted(path_mappings, key=lambda row: len(row.get("path", "")), reverse=True)
    web_mappings = sorted(web_mappings, key=lambda row: len(row.get("web_url", "")), reverse=True)

    prefix_pattern = re.compile(r"^(?P<matter>\d{2}-\d{3,4}-\d{5})\b")

    for doc in docs:
        mapped_matter = ""
        mapping_rule = ""
        reason = ""

        item_mappings = [m for m in mappings_by_item_id.get(doc.drive_item_id, []) if m.get("matter_number") in matter_numbers]
        if len(item_mappings) == 1:
            mapped_matter = item_mappings[0]["matter_number"]
            mapping_rule = "explicit_map_drive_item_id"
            reason = "deterministic map by drive_item_id"
        elif len(item_mappings) > 1:
            reason = "ambiguous explicit mapping: multiple matter numbers for drive_item_id"
        else:
            path_hits = [
                mapping
                for mapping in path_mappings
                if mapping.get("matter_number") in matter_numbers
                and doc.path.lower().startswith(mapping.get("path", "").lower())
            ]
            if len(path_hits) == 1:
                mapped_matter = path_hits[0]["matter_number"]
                mapping_rule = "explicit_map_path_prefix"
                reason = "deterministic map by configured path prefix"
            elif len(path_hits) > 1:
                reason = "ambiguous explicit mapping: multiple path prefixes matched"
            else:
                web_hits = [
                    mapping
                    for mapping in web_mappings
                    if mapping.get("matter_number") in matter_numbers
                    and doc.web_url
                    and doc.web_url.lower().startswith(mapping.get("web_url", "").lower())
                ]
                if len(web_hits) == 1:
                    mapped_matter = web_hits[0]["matter_number"]
                    mapping_rule = "explicit_map_web_url_prefix"
                    reason = "deterministic map by configured web_url prefix"
                elif len(web_hits) > 1:
                    reason = "ambiguous explicit mapping: multiple web_url prefixes matched"
                else:
                    path_candidates = [
                        candidate
                        for candidate in extract_matter_numbers(doc.path, matter_pattern)
                        if candidate in matter_numbers
                    ]
                    path_candidates = list(dict.fromkeys(path_candidates))
                    if len(path_candidates) == 1:
                        mapped_matter = path_candidates[0]
                        mapping_rule = "path_contains_matter_number"
                        reason = "single canonical matter number found in SharePoint path"
                    elif len(path_candidates) > 1:
                        prefix_candidates: List[str] = []
                        for segment in doc.path.split("/"):
                            segment = segment.strip()
                            if not segment:
                                continue
                            match = prefix_pattern.match(segment)
                            if not match:
                                continue
                            candidate = match.group("matter")
                            if candidate in matter_numbers and candidate not in prefix_candidates:
                                prefix_candidates.append(candidate)
                        if len(prefix_candidates) == 1:
                            mapped_matter = prefix_candidates[0]
                            mapping_rule = "folder_prefix_matter_number"
                            reason = "single canonical folder-prefix matter number found"
                        elif len(prefix_candidates) > 1:
                            reason = "ambiguous: multiple matter numbers found in folder path"
                        else:
                            reason = "ambiguous: multiple matter numbers found in path"
                    else:
                        name_candidates = [
                            candidate
                            for candidate in extract_matter_numbers(doc.name, matter_pattern)
                            if candidate in matter_numbers
                        ]
                        name_candidates = list(dict.fromkeys(name_candidates))
                        if len(name_candidates) == 1:
                            mapped_matter = name_candidates[0]
                            mapping_rule = "name_contains_matter_number"
                            reason = "single canonical matter number found in file/folder name"
                        elif len(name_candidates) > 1:
                            reason = "ambiguous: multiple matter numbers found in name"
                        else:
                            reason = "no confident matter number match"

        if single_matter_scope and mapped_matter and mapped_matter != single_matter_scope:
            continue

        if single_matter_scope and not mapped_matter:
            scope_token = single_matter_scope.lower()
            text_blob = f"{doc.path} {doc.name}".lower()
            if scope_token not in text_blob:
                continue

        record: Dict[str, Any] = {
            "drive_item_id": doc.drive_item_id,
            "path": doc.path,
            "name": doc.name,
            "modified_at": doc.modified_at,
            "size": doc.size,
            "web_url": doc.web_url,
            "author": doc.author,
            "drive_id": doc.drive_id,
            "is_folder": doc.is_folder,
            "matter_number": mapped_matter,
            "mapping_rule": mapping_rule or "unmapped",
            "reason": reason,
            "source_pointer": doc.source_pointer,
        }
        resolved_rows.append(record)

        if mapped_matter:
            continue

        issue_row = {
            "modified_at": doc.modified_at,
            "drive_item_id": doc.drive_item_id,
            "path": doc.path,
            "name": doc.name,
            "reason": reason,
            "source_pointer": doc.source_pointer,
        }
        if "ambiguous" in reason:
            ambiguous_rows.append(issue_row)
        else:
            unmapped_rows.append(issue_row)

    resolved_rows = sorted(
        resolved_rows,
        key=lambda row: (
            str(row.get("matter_number") or ""),
            str(row.get("path") or "").lower(),
            str(row.get("drive_item_id") or ""),
        ),
    )
    unmapped_rows = sorted(
        unmapped_rows,
        key=lambda row: (row.get("modified_at", ""), row.get("drive_item_id", "")),
        reverse=True,
    )
    ambiguous_rows = sorted(
        ambiguous_rows,
        key=lambda row: (row.get("modified_at", ""), row.get("drive_item_id", "")),
        reverse=True,
    )
    return resolved_rows, unmapped_rows, ambiguous_rows


def serialize_doc_rows(rows: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    ordered_rows: List[Dict[str, Any]] = []
    for row in rows:
        ordered_rows.append(
            {
                "drive_item_id": str(row.get("drive_item_id") or ""),
                "path": str(row.get("path") or ""),
                "name": str(row.get("name") or ""),
                "modified_at": str(row.get("modified_at") or ""),
                "size": int(row.get("size") or 0),
                "web_url": str(row.get("web_url") or ""),
                "author": str(row.get("author") or ""),
                "drive_id": str(row.get("drive_id") or ""),
                "is_folder": bool(row.get("is_folder")),
                "matter_number": str(row.get("matter_number") or ""),
                "mapping_rule": str(row.get("mapping_rule") or ""),
                "reason": str(row.get("reason") or ""),
                "source_pointer": str(row.get("source_pointer") or ""),
            }
        )
    return ordered_rows


def compile_matter_regex(gmail_label_rules: Dict[str, Any]) -> re.Pattern[str]:
    label_rules = gmail_label_rules.get("label_rules") or {}
    raw = str(label_rules.get("matter_number_regex") or r"\b\d{2}-\d{3,4}-\d{5}\b")
    return re.compile(raw)


def extract_matter_numbers(text: str, pattern: re.Pattern[str]) -> List[str]:
    if not text:
        return []
    matches = [m.group(0) for m in pattern.finditer(text)]
    # Keep deterministic order while deduplicating.
    seen = set()
    ordered: List[str] = []
    for match in matches:
        if match not in seen:
            ordered.append(match)
            seen.add(match)
    return ordered


def resolve_thread_identity_matter(
    thread: ThreadRef,
    matter_numbers: set[str],
) -> Tuple[str, str, str]:
    indexes = load_matter_identity_indexes()

    def scoped_candidates(values: Iterable[str], index: Dict[str, set[str]]) -> List[str]:
        candidates: set[str] = set()
        for value in values:
            if not value:
                continue
            candidates.update(candidate for candidate in index.get(value, set()) if candidate in matter_numbers)
        return sorted(candidates)

    def decide(candidates: List[str], matched_by: str, ambiguous_by: str) -> Tuple[str, str, str]:
        if len(candidates) == 1:
            return candidates[0], matched_by, f"single matter matched by {matched_by}"
        if len(candidates) > 1:
            return "", "", f"ambiguous: multiple matter candidates found by {ambiguous_by}"
        return "", "", ""

    sender_candidates = scoped_candidates(
        [extract_sender_email(thread.sender), extract_sender_email(thread.last_sender)],
        indexes["senders"],
    )
    mapped_matter, routing_rule, reason = decide(
        sender_candidates,
        "identity_sender_exact",
        "identity_sender_exact",
    )
    if mapped_matter or reason:
        return mapped_matter, routing_rule, reason

    participant_email_candidates = scoped_candidates(
        [extract_sender_email(participant) for participant in thread.participants],
        indexes["senders"],
    )
    mapped_matter, routing_rule, reason = decide(
        participant_email_candidates,
        "identity_participant_email_exact",
        "identity_participant_email_exact",
    )
    if mapped_matter or reason:
        return mapped_matter, routing_rule, reason

    domain_candidates = scoped_candidates(
        [extract_sender_domain(thread.sender), extract_sender_domain(thread.last_sender)],
        indexes["domains"],
    )
    mapped_matter, routing_rule, reason = decide(
        domain_candidates,
        "identity_sender_domain",
        "identity_sender_domain",
    )
    if mapped_matter or reason:
        return mapped_matter, routing_rule, reason

    participant_domain_candidates = scoped_candidates(
        [extract_sender_domain(participant) for participant in thread.participants],
        indexes["domains"],
    )
    mapped_matter, routing_rule, reason = decide(
        participant_domain_candidates,
        "identity_participant_domain",
        "identity_participant_domain",
    )
    if mapped_matter or reason:
        return mapped_matter, routing_rule, reason

    token_sources = [
        thread.subject,
        thread.sender,
        thread.last_sender,
        thread.latest_snippet,
        " ".join(thread.participants),
    ]
    matched_name_keys = {
        candidate
        for token_source in token_sources
        for token in tokenize_identity_text(token_source)
        for candidate in indexes["name_keys"].get(normalize_identity_token(token), set())
        if candidate in matter_numbers
    }
    name_key_candidates = sorted(matched_name_keys)
    mapped_matter, routing_rule, reason = decide(
        name_key_candidates,
        "identity_name_key",
        "identity_name_key",
    )
    if mapped_matter or reason:
        return mapped_matter, routing_rule, reason

    return "", "", ""


def route_threads_to_matters(
    threads: List[ThreadRef],
    matter_numbers: set[str],
    matter_pattern: re.Pattern[str],
    single_matter_scope: Optional[str],
) -> Tuple[Dict[str, List[Dict[str, str]]], List[Dict[str, str]], List[Dict[str, str]]]:
    """Route threads to matter numbers with label-first then fallback heuristics.

    Returns:
    - mapped_by_matter
    - unmapped_threads
    - review_required_threads
    """
    mapped: Dict[str, List[Dict[str, str]]] = {}
    unmapped: List[Dict[str, str]] = []
    review_required: List[Dict[str, str]] = []

    for thread in threads:
        mapped_matter = ""
        routing_rule = ""
        reason = ""

        label_candidates: List[str] = []
        for label in thread.labels:
            label_candidates.extend(extract_matter_numbers(label, matter_pattern))
        label_candidates = [candidate for candidate in label_candidates if candidate in matter_numbers]

        if len(label_candidates) == 1:
            mapped_matter = label_candidates[0]
            routing_rule = "label_path_contains_matter_number"
            reason = "single canonical matter number found in label"
        elif len(label_candidates) > 1:
            reason = "ambiguous: multiple matter numbers found in labels"
        else:
            fallback_text = " ".join(part for part in (thread.subject, thread.latest_snippet) if part)
            fallback_candidates = [
                candidate for candidate in extract_matter_numbers(fallback_text, matter_pattern)
                if candidate in matter_numbers
            ]
            if len(fallback_candidates) == 1:
                mapped_matter = fallback_candidates[0]
                routing_rule = "subject_or_snippet_contains_matter_number"
                reason = "single fallback matter number found in subject/snippet"
            elif len(fallback_candidates) > 1:
                reason = "ambiguous: multiple matter numbers found in subject/snippet"
            else:
                mapped_matter, routing_rule, reason = resolve_thread_identity_matter(thread, matter_numbers)
                if not mapped_matter and not reason:
                    reason = "no confident matter or identity match"

        if single_matter_scope and mapped_matter and mapped_matter != single_matter_scope:
            continue

        thread_record = {
            "thread_id": thread.thread_id,
            "subject": thread.subject or "(no subject)",
            "last_message_at": thread.last_message_at,
            "labels": ", ".join(thread.labels),
            "routing_rule": routing_rule or "unmapped",
            "reason": reason,
            "source_pointer": thread.source_pointer,
        }

        if mapped_matter:
            mapped.setdefault(mapped_matter, []).append(thread_record)
            if routing_rule != "label_path_contains_matter_number":
                review_required.append(thread_record | {"matter_number": mapped_matter})
        else:
            if not single_matter_scope:
                unmapped.append(thread_record)

    for matter_number in mapped:
        mapped[matter_number] = sorted(
            mapped[matter_number],
            key=lambda row: (row["last_message_at"], row["thread_id"]),
            reverse=True,
        )

    unmapped_sorted = sorted(unmapped, key=lambda row: (row["last_message_at"], row["thread_id"]), reverse=True)
    review_sorted = sorted(
        review_required,
        key=lambda row: (row["last_message_at"], row["thread_id"]),
        reverse=True,
    )
    return mapped, unmapped_sorted, review_sorted


def build_state_review_batch(
    threads: List[ThreadRef],
    mapped: Dict[str, List[Dict[str, str]]],
    generated_at: str,
    gmail_query: str,
    selection_summary: Dict[str, Any],
    single_matter_scope: Optional[str],
) -> Dict[str, Any]:
    batch_stamp = generated_at.replace("-", "").replace(":", "").replace("T", "_")
    batch_id = f"matter_admin_review_{batch_stamp}"

    thread_to_matter: Dict[str, str] = {}
    thread_to_routing_rule: Dict[str, str] = {}
    for matter_number, rows in mapped.items():
        for row in rows:
            thread_id = str(row.get("thread_id") or "")
            if not thread_id:
                continue
            thread_to_matter[thread_id] = matter_number
            thread_to_routing_rule[thread_id] = str(row.get("routing_rule") or "")

    review_rows: List[Dict[str, Any]] = []
    for thread in threads:
        mapped_matter = thread_to_matter.get(thread.thread_id, "")
        proposed_state_label, signal_basis = classify_review_state(thread, has_matter=bool(mapped_matter))
        current_state_labels = list(thread.state_labels)
        disposition = "apply"
        if len(current_state_labels) == 1 and current_state_labels[0] == proposed_state_label:
            disposition = "no_change"

        review_rows.append(
            {
                "thread_id": thread.thread_id,
                "subject": thread.subject or "(no subject)",
                "last_message_at": thread.last_message_at,
                "sender": thread.sender,
                "last_sender": thread.last_sender,
                "message_count": thread.message_count,
                "labels": list(thread.labels),
                "existing_state_labels": current_state_labels,
                "proposed_state_label": proposed_state_label,
                "state_signal_basis": signal_basis,
                "matter_number": mapped_matter,
                "routing_rule": thread_to_routing_rule.get(thread.thread_id, ""),
                "confidence": "high" if proposed_state_label != "00_Triage" or mapped_matter else "medium",
                "disposition": disposition,
                "source_pointer": thread.source_pointer,
            }
        )

    return {
        "batch_id": batch_id,
        "project_id": "LLP-023",
        "generated_at": generated_at,
        "gmail_query": gmail_query,
        "single_matter_scope": single_matter_scope or "",
        "selection_summary": selection_summary,
        "threads_reviewed": len(review_rows),
        "threads": review_rows,
    }


def execute_state_review_batch(
    batch_payload: Dict[str, Any],
    approval_artifact_text: str,
    approved_by: str,
    reason: str,
) -> Dict[str, Any]:
    from gmail_mcp_server import (
        _append_audit,
        _apply_thread_modify,
        _collect_thread_label_ids,
        _get_gmail_service,
        _get_thread,
        _label_name_to_id,
        _list_all_labels,
        _now_iso,
        _resolve_approval_artifact,
    )

    approval_artifact = _resolve_approval_artifact(approval_artifact_text)
    if not approval_artifact.exists():
        raise FileNotFoundError(f"approval_artifact not found: {approval_artifact}")

    service = _get_gmail_service()
    labels = _list_all_labels(service)
    name_to_id = _label_name_to_id(labels)
    state_label_names = tuple(
        sorted(set(CANONICAL_STATE_LABELS).union(LEGACY_STATE_LABEL_ALIASES.keys()))
    )

    required_state_labels = sorted(
        {
            LEGACY_STATE_LABEL_ALIASES.get(
                str(row.get("proposed_state_label") or "").strip(),
                str(row.get("proposed_state_label") or "").strip(),
            )
            for row in batch_payload.get("threads", [])
            if LEGACY_STATE_LABEL_ALIASES.get(
                str(row.get("proposed_state_label") or "").strip(),
                str(row.get("proposed_state_label") or "").strip(),
            ) in CANONICAL_STATE_LABELS
        }
    )
    missing_state_labels = [label for label in required_state_labels if label not in name_to_id]
    if missing_state_labels:
        raise RuntimeError(
            f"Missing required state labels in Gmail for this batch: {missing_state_labels}"
        )

    executed_rows: List[Dict[str, Any]] = []
    for row in batch_payload.get("threads", []):
        thread_id = str(row.get("thread_id") or "").strip()
        target_state_label = LEGACY_STATE_LABEL_ALIASES.get(
            str(row.get("proposed_state_label") or "").strip(),
            str(row.get("proposed_state_label") or "").strip(),
        )
        if not thread_id or target_state_label not in CANONICAL_STATE_LABELS:
            continue

        thread = _get_thread(service, thread_id)
        thread_label_ids = _collect_thread_label_ids(thread)
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
        target_label_id = name_to_id[target_state_label]

        no_change = len(current_state_labels) == 1 and current_state_labels[0] == target_state_label
        if not no_change:
            _apply_thread_modify(service, thread_id, [target_label_id], remove_label_ids)

        audit_row = {
            "timestamp": _now_iso(),
            "tool": "llp023_apply_state_label",
            "thread_id": thread_id,
            "prior_state_labels": current_state_labels,
            "new_state_label": target_state_label,
            "no_change": no_change,
            "approved_by": approved_by,
            "approval_artifact": str(approval_artifact),
            "reason": reason,
            "project_id": "LLP-023",
            "batch_id": str(batch_payload.get("batch_id") or ""),
        }
        _append_audit(audit_row)
        executed_rows.append(audit_row)

    return {
        "batch_id": str(batch_payload.get("batch_id") or ""),
        "project_id": "LLP-023",
        "executed_at": utc_iso(),
        "approved_by": approved_by,
        "approval_artifact": str(approval_artifact),
        "reason": reason,
        "thread_count": len(executed_rows),
        "changed_count": sum(1 for row in executed_rows if not row.get("no_change")),
        "no_change_count": sum(1 for row in executed_rows if row.get("no_change")),
        "threads": executed_rows,
    }


def format_table(headers: List[str], rows: List[List[str]]) -> str:
    if not rows:
        return ""
    out = ["| " + " | ".join(headers) + " |", "| " + " | ".join(["---"] * len(headers)) + " |"]
    for row in rows:
        escaped = [cell.replace("\n", " ").replace("|", "\\|") for cell in row]
        out.append("| " + " | ".join(escaped) + " |")
    return "\n".join(out)


def write_matter_index(
    markdown_path: Path,
    matters: List[MatterRef],
    source: str,
    generated_at: str,
    delivery_taxonomy: Dict[str, Any],
    dry_run: bool,
) -> None:
    rows = [
        [
            matter.matter_number,
            matter.name,
            matter.status,
            classify_delivery_category(matter, delivery_taxonomy)[1],
            matter.delivery_status,
            matter.fulfillment_status,
            service_summary(matter.services),
            matter.responsible,
            matter.client,
            matter.source_pointer,
        ]
        for matter in matters
    ]

    body = [
        "# Matter Index",
        "",
        f"Generated at: {generated_at}",
        f"Connector source: `{source}`",
        "",
        "## Role",
        "",
        "This is a system tracking and visibility artifact for ML1.",
        "",
        "Doctrine source: `repo://00_SYSTEM/matters/MATTER_TASK_AND_DASHBOARD_DOCTRINE.md`.",
        "",
        "It answers: what matters exist, how are they classified, and where do we look next?",
        "",
        "It does not answer: what exact legal steps must be taken, whether ML1 has failed to do something, "
        "whether a draft is substantively good, or what the actual next legal step is.",
        "",
    ]

    table = format_table(
        [
            "Matter Number",
            "Name",
            "Status",
            "Category",
            "Delivery",
            "Fulfillment",
            "Services",
            "Responsible",
            "Client",
            "Source Pointer",
        ],
        rows,
    )
    if table:
        body.append(table)
    else:
        body.append("No matter records available.")

    if not dry_run:
        write_text(markdown_path, "\n".join(body))


def write_unmapped_dashboard(path: Path, unmapped: List[Dict[str, str]], generated_at: str, dry_run: bool) -> None:
    body = [
        "# Inbox Unmapped",
        "",
        f"Generated at: {generated_at}",
        "",
        "Threads that could not be deterministically routed to a matter number.",
        "",
    ]

    if unmapped:
        rows = [
            [
                row["last_message_at"],
                row["thread_id"],
                row["subject"],
                row["reason"],
                row["labels"],
                row["source_pointer"],
            ]
            for row in unmapped
        ]
        body.append(
            format_table(
                ["Last Message (UTC)", "Thread ID", "Subject", "Reason", "Labels", "Source Pointer"],
                rows,
            )
        )
    else:
        body.append("No unmapped threads in scope.")

    if not dry_run:
        write_text(path, "\n".join(body))


def write_matter_status_files(
    mapped: Dict[str, List[Dict[str, str]]],
    matter_lookup: Dict[str, MatterRef],
    local_matter_paths: Dict[str, Path],
    generated_at: str,
    dry_run: bool,
) -> List[str]:
    missing_paths: List[str] = []

    for matter_number, thread_rows in sorted(mapped.items()):
        matter_path = local_matter_paths.get(matter_number)
        if matter_path is None:
            missing_paths.append(matter_number)
            continue

        matter = matter_lookup.get(matter_number)
        name = matter.name if matter else matter_number
        status = matter.status if matter else "unknown"
        delivery_status = matter.delivery_status if matter else "unknown"
        fulfillment_status = matter.fulfillment_status if matter else "unknown"
        responsible = matter.responsible if matter else "unassigned"
        client = matter.client if matter else name
        services = matter.services if matter else tuple()

        lines = [
            f"# Matter Status — {matter_number}",
            "",
            f"Generated at: {generated_at}",
            "",
            "## Snapshot",
            f"- Matter: {name}",
            f"- Clio status: {status}",
            f"- Delivery status: {delivery_status}",
            f"- Fulfillment status: {fulfillment_status}",
            f"- Services: {service_summary(services, max_items=5)}",
            f"- Responsible: {responsible}",
            f"- Client: {client}",
            "",
            "## Routed Threads",
            "",
        ]

        if thread_rows:
            rows = [
                [
                    row["last_message_at"],
                    row["thread_id"],
                    row["subject"],
                    row["routing_rule"],
                    row["source_pointer"],
                ]
                for row in thread_rows
            ]
            lines.append(
                format_table(
                    ["Last Message (UTC)", "Thread ID", "Subject", "Routing Rule", "Source Pointer"],
                    rows,
                )
            )
        else:
            lines.append("No routed threads in this run scope.")

        if not dry_run:
            write_text(matter_path / "MATTER_STATUS.md", "\n".join(lines))

    return missing_paths


def sharepoint_row_key(row: Dict[str, Any]) -> str:
    drive_item_id = str(row.get("drive_item_id") or "").strip()
    if drive_item_id:
        return drive_item_id
    return str(row.get("path") or "").strip()


def sharepoint_row_fingerprint(row: Dict[str, Any]) -> str:
    bits = [
        str(row.get("path") or ""),
        str(row.get("name") or ""),
        str(row.get("modified_at") or ""),
        str(row.get("size") or 0),
        str(row.get("web_url") or ""),
        str(row.get("author") or ""),
        str(row.get("matter_number") or ""),
        "folder" if row.get("is_folder") else "file",
    ]
    return "|".join(bits)


def build_sharepoint_doc_views(
    current_rows: List[Dict[str, Any]],
    previous_rows: List[Dict[str, Any]],
) -> Tuple[Dict[str, Any], Dict[str, List[Dict[str, Any]]], Dict[str, Dict[str, Any]]]:
    current_by_key: Dict[str, Dict[str, Any]] = {}
    for row in current_rows:
        key = sharepoint_row_key(row)
        if key:
            current_by_key[key] = row

    previous_by_key: Dict[str, Dict[str, Any]] = {}
    for row in previous_rows:
        key = sharepoint_row_key(row)
        if key:
            previous_by_key[key] = row

    current_keys = set(current_by_key)
    previous_keys = set(previous_by_key)

    added_keys = sorted(current_keys - previous_keys)
    removed_keys = sorted(previous_keys - current_keys)
    common_keys = sorted(current_keys & previous_keys)

    added = [current_by_key[key] for key in added_keys]
    removed = [previous_by_key[key] for key in removed_keys]
    changed: List[Dict[str, Any]] = []

    for key in common_keys:
        current = current_by_key[key]
        previous = previous_by_key[key]
        if sharepoint_row_fingerprint(current) != sharepoint_row_fingerprint(previous):
            changed.append({"current": current, "previous": previous})

    added = sorted(added, key=lambda row: (str(row.get("path") or "").lower(), str(row.get("drive_item_id") or "")))
    removed = sorted(removed, key=lambda row: (str(row.get("path") or "").lower(), str(row.get("drive_item_id") or "")))
    changed = sorted(
        changed,
        key=lambda row: (
            str((row.get("current") or {}).get("path") or "").lower(),
            str((row.get("current") or {}).get("drive_item_id") or ""),
        ),
    )

    current_files = [row for row in current_rows if not row.get("is_folder")]
    added_files = [row for row in added if not row.get("is_folder")]
    removed_files = [row for row in removed if not row.get("is_folder")]
    changed_files = [
        row for row in changed
        if not (row.get("current") or {}).get("is_folder")
        or not (row.get("previous") or {}).get("is_folder")
    ]

    summary = {
        "current_items": len(current_rows),
        "current_files": len(current_files),
        "current_folders": len(current_rows) - len(current_files),
        "mapped_items": sum(1 for row in current_rows if row.get("matter_number")),
        "unmapped_items": sum(1 for row in current_rows if not row.get("matter_number")),
        "added_items": len(added),
        "changed_items": len(changed),
        "removed_items": len(removed),
        "added_files": len(added_files),
        "changed_files": len(changed_files),
        "removed_files": len(removed_files),
        "file_changes": len(added_files) + len(changed_files) + len(removed_files),
    }

    docs_by_matter: Dict[str, List[Dict[str, Any]]] = {}
    for row in current_rows:
        matter_number = str(row.get("matter_number") or "").strip()
        if not matter_number:
            continue
        docs_by_matter.setdefault(matter_number, []).append(row)

    for matter_number in docs_by_matter:
        docs_by_matter[matter_number] = sorted(
            docs_by_matter[matter_number],
            key=lambda row: (
                str(row.get("modified_at") or ""),
                str(row.get("path") or "").lower(),
                str(row.get("drive_item_id") or ""),
            ),
            reverse=True,
        )

    deltas_by_matter: Dict[str, Dict[str, Any]] = {}

    def _matter_delta_bucket(matter_number: str) -> Dict[str, Any]:
        bucket = deltas_by_matter.get(matter_number)
        if bucket is None:
            bucket = {"added": [], "changed": [], "removed": []}
            deltas_by_matter[matter_number] = bucket
        return bucket

    for row in added:
        matter_number = str(row.get("matter_number") or "").strip()
        if not matter_number:
            continue
        _matter_delta_bucket(matter_number)["added"].append(row)

    for row in removed:
        matter_number = str(row.get("matter_number") or "").strip()
        if not matter_number:
            continue
        _matter_delta_bucket(matter_number)["removed"].append(row)

    for pair in changed:
        current = pair.get("current") or {}
        previous = pair.get("previous") or {}
        current_matter = str(current.get("matter_number") or "").strip()
        previous_matter = str(previous.get("matter_number") or "").strip()

        if current_matter:
            _matter_delta_bucket(current_matter)["changed"].append(pair)
        if previous_matter and previous_matter != current_matter:
            _matter_delta_bucket(previous_matter)["changed"].append(pair)

    for matter_number, bucket in deltas_by_matter.items():
        bucket["added"] = sorted(
            bucket["added"],
            key=lambda row: (str(row.get("path") or "").lower(), str(row.get("drive_item_id") or "")),
        )
        bucket["removed"] = sorted(
            bucket["removed"],
            key=lambda row: (str(row.get("path") or "").lower(), str(row.get("drive_item_id") or "")),
        )
        bucket["changed"] = sorted(
            bucket["changed"],
            key=lambda row: (
                str(((row.get("current") or {}).get("path") or "")).lower(),
                str((row.get("current") or {}).get("drive_item_id") or ""),
            ),
        )

    return summary, docs_by_matter, deltas_by_matter


def detect_duplicate_file_names(rows: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    by_name: Dict[str, List[Dict[str, Any]]] = {}
    for row in rows:
        if row.get("is_folder"):
            continue
        name = str(row.get("name") or "").strip()
        if not name:
            continue
        by_name.setdefault(name.lower(), []).append(row)

    duplicates: List[Dict[str, Any]] = []
    for entries in by_name.values():
        if len(entries) < 2:
            continue
        entries_sorted = sorted(
            entries,
            key=lambda row: (str(row.get("path") or "").lower(), str(row.get("drive_item_id") or "")),
        )
        duplicates.append(
            {
                "name": str(entries_sorted[0].get("name") or ""),
                "count": len(entries_sorted),
                "paths": [str(row.get("path") or "") for row in entries_sorted],
                "source_pointers": [str(row.get("source_pointer") or "") for row in entries_sorted],
            }
        )

    return sorted(duplicates, key=lambda row: (-int(row.get("count") or 0), str(row.get("name") or "").lower()))


def detect_missing_expected_folders(rows: List[Dict[str, Any]], expected_folders: List[str]) -> List[str]:
    if not expected_folders:
        return []
    present = set()
    for row in rows:
        path = str(row.get("path") or "")
        for segment in path.split("/"):
            segment = segment.strip()
            if segment:
                present.add(segment.lower())
    missing = [folder for folder in expected_folders if folder.lower() not in present]
    return sorted(missing, key=lambda value: value.lower())


def write_sharepoint_matter_files(
    matters: List[MatterRef],
    local_matter_paths: Dict[str, Path],
    docs_by_matter: Dict[str, List[Dict[str, Any]]],
    deltas_by_matter: Dict[str, Dict[str, Any]],
    expected_folders: List[str],
    generated_at: str,
    source: str,
    baseline_generated_at: str,
    dry_run: bool,
) -> List[str]:
    missing_paths: List[str] = []

    for matter in sorted(matters, key=lambda m: m.matter_number):
        matter_number = matter.matter_number
        matter_path = local_matter_paths.get(matter_number)
        if matter_path is None:
            missing_paths.append(matter_number)
            continue

        rows = docs_by_matter.get(matter_number, [])
        files = [row for row in rows if not row.get("is_folder")]
        folders = [row for row in rows if row.get("is_folder")]

        index_lines = [
            f"# Document Index — {matter_number}",
            "",
            f"Generated at: {generated_at}",
            f"Connector source: `{source}`",
            "",
            "## Summary",
            f"- Total mapped items: {len(rows)}",
            f"- Files: {len(files)}",
            f"- Folders: {len(folders)}",
            f"- Matter source pointer: {matter.source_pointer}",
            "",
        ]

        if rows:
            index_rows = [
                [
                    str(row.get("modified_at") or ""),
                    "folder" if row.get("is_folder") else "file",
                    str(row.get("name") or ""),
                    str(row.get("path") or ""),
                    str(row.get("size") or 0),
                    str(row.get("author") or ""),
                    str(row.get("source_pointer") or ""),
                ]
                for row in rows
            ]
            index_lines.append(
                format_table(
                    ["Modified (UTC)", "Type", "Name", "Path", "Size (bytes)", "Author", "Source Pointer"],
                    index_rows,
                )
            )
        else:
            index_lines.append("No SharePoint items mapped to this matter in current snapshot.")

        delta_bucket = deltas_by_matter.get(matter_number) or {"added": [], "changed": [], "removed": []}
        added = delta_bucket.get("added") or []
        changed = delta_bucket.get("changed") or []
        removed = delta_bucket.get("removed") or []
        duplicate_names = detect_duplicate_file_names(rows)
        missing_expected = detect_missing_expected_folders(rows, expected_folders)

        delta_lines = [
            f"# Document Deltas — {matter_number}",
            "",
            f"Generated at: {generated_at}",
            f"Baseline snapshot: `{baseline_generated_at or 'none'}`",
            "",
            "## Summary",
            f"- Added items: {len(added)}",
            f"- Changed items: {len(changed)}",
            f"- Removed items: {len(removed)}",
            f"- Duplicate file names: {len(duplicate_names)}",
            f"- Missing expected folders: {len(missing_expected)}",
            "",
        ]

        delta_lines.extend(["## Added"])
        if added:
            added_rows = [
                [
                    str(row.get("modified_at") or ""),
                    "folder" if row.get("is_folder") else "file",
                    str(row.get("name") or ""),
                    str(row.get("path") or ""),
                    str(row.get("source_pointer") or ""),
                ]
                for row in added
            ]
            delta_lines.append(
                format_table(["Modified (UTC)", "Type", "Name", "Path", "Source Pointer"], added_rows)
            )
        else:
            delta_lines.append("- None")

        delta_lines.extend(["", "## Changed"])
        if changed:
            changed_rows = [
                [
                    str((pair.get("previous") or {}).get("modified_at") or ""),
                    str((pair.get("current") or {}).get("modified_at") or ""),
                    str((pair.get("current") or {}).get("name") or ""),
                    str((pair.get("previous") or {}).get("path") or ""),
                    str((pair.get("current") or {}).get("path") or ""),
                    str((pair.get("current") or {}).get("source_pointer") or ""),
                ]
                for pair in changed
            ]
            delta_lines.append(
                format_table(
                    ["Prev Modified", "Current Modified", "Name", "Prev Path", "Current Path", "Source Pointer"],
                    changed_rows,
                )
            )
        else:
            delta_lines.append("- None")

        delta_lines.extend(["", "## Removed"])
        if removed:
            removed_rows = [
                [
                    str(row.get("modified_at") or ""),
                    "folder" if row.get("is_folder") else "file",
                    str(row.get("name") or ""),
                    str(row.get("path") or ""),
                    str(row.get("source_pointer") or ""),
                ]
                for row in removed
            ]
            delta_lines.append(
                format_table(["Modified (UTC)", "Type", "Name", "Path", "Source Pointer"], removed_rows)
            )
        else:
            delta_lines.append("- None")

        delta_lines.extend(["", "## Duplicate File Names"])
        if duplicate_names:
            for duplicate in duplicate_names:
                delta_lines.append(f"- {duplicate['name']} ({duplicate['count']} files)")
                for path_value, pointer in zip(duplicate["paths"], duplicate["source_pointers"]):
                    delta_lines.append(f"  - {path_value} ({pointer})")
        else:
            delta_lines.append("- None")

        delta_lines.extend(["", "## Missing Expected Folders"])
        if expected_folders:
            if missing_expected:
                config_pointer = f"repo://{display_path(DEFAULT_MATTER_FOLDER_RULES)}#sharepoint_mapping.expected_subfolders"
                for folder_name in missing_expected:
                    delta_lines.append(f"- {folder_name} ({config_pointer})")
            else:
                delta_lines.append("- None")
        else:
            delta_lines.append("- Not configured")

        if not dry_run:
            write_text(matter_path / "DOC_INDEX.md", "\n".join(index_lines))
            write_text(matter_path / "DOC_DELTAS.md", "\n".join(delta_lines))

    return missing_paths


def write_sharepoint_gaps_dashboard(
    path: Path,
    generated_at: str,
    source: str,
    summary: Dict[str, Any],
    unmapped_rows: List[Dict[str, str]],
    ambiguous_rows: List[Dict[str, str]],
    matters_without_docs: List[MatterRef],
    dry_run: bool,
) -> None:
    lines = [
        "# SharePoint Gaps",
        "",
        f"Generated at: {generated_at}",
        f"Connector source: `{source}`",
        "",
        "## Summary",
        f"- Total items scanned: {summary.get('current_items', 0)}",
        f"- Mapped items: {summary.get('mapped_items', 0)}",
        f"- Unmapped items: {summary.get('unmapped_items', 0)}",
        f"- Ambiguous mapping items: {len(ambiguous_rows)}",
        f"- Matters with zero mapped SharePoint items: {len(matters_without_docs)}",
        "",
    ]

    lines.extend(["## Unmapped Items"])
    if unmapped_rows:
        rows = [
            [
                row.get("modified_at", ""),
                row.get("drive_item_id", ""),
                row.get("name", ""),
                row.get("path", ""),
                row.get("reason", ""),
                row.get("source_pointer", ""),
            ]
            for row in unmapped_rows
        ]
        lines.append(
            format_table(
                ["Modified (UTC)", "Drive Item ID", "Name", "Path", "Reason", "Source Pointer"],
                rows,
            )
        )
    else:
        lines.append("No unmapped SharePoint items.")

    lines.extend(["", "## Ambiguous Mapping Items"])
    if ambiguous_rows:
        rows = [
            [
                row.get("modified_at", ""),
                row.get("drive_item_id", ""),
                row.get("name", ""),
                row.get("path", ""),
                row.get("reason", ""),
                row.get("source_pointer", ""),
            ]
            for row in ambiguous_rows
        ]
        lines.append(
            format_table(
                ["Modified (UTC)", "Drive Item ID", "Name", "Path", "Reason", "Source Pointer"],
                rows,
            )
        )
    else:
        lines.append("No ambiguous SharePoint mappings.")

    lines.extend(["", "## Matters With Zero SharePoint Items"])
    if matters_without_docs:
        for matter in matters_without_docs:
            lines.append(f"- {matter.matter_number} :: {matter.name} ({matter.source_pointer})")
    else:
        lines.append("- None")

    if DEFAULT_DISCOVERY_GAPS.exists():
        lines.extend(
            [
                "",
                "## Discovery Baseline",
                f"- Reference: `repo://{display_path(DEFAULT_DISCOVERY_GAPS)}`",
            ]
        )

    if not dry_run:
        write_text(path, "\n".join(lines))


def load_run_state(path: Path) -> Dict[str, Any]:
    payload = load_json(path)
    return payload if isinstance(payload, dict) else {}


def build_digest(
    matters: List[MatterRef],
    mapped: Dict[str, List[Dict[str, str]]],
    unmapped: List[Dict[str, str]],
    review_required: List[Dict[str, str]],
    run_state: Dict[str, Any],
    generated_at: str,
    stalled_days: int,
    active_window_days: int,
    delivery_taxonomy: Dict[str, Any],
    sharepoint_summary: Optional[Dict[str, Any]] = None,
    sharepoint_ambiguous_count: int = 0,
    sharepoint_unmapped_count: int = 0,
    matters_without_sharepoint: int = 0,
) -> Tuple[str, Dict[str, Any]]:
    now = parse_timestamp(generated_at) or utc_now()
    previous_latest: Dict[str, str] = run_state.get("matter_latest_thread_at", {}) if isinstance(run_state.get("matter_latest_thread_at"), dict) else {}
    sharepoint_summary = sharepoint_summary or {}

    current_latest: Dict[str, str] = {}
    moved: List[str] = []
    waiting_external: List[str] = []
    matter_lookup = {matter.matter_number: matter for matter in matters}
    inbox_signal_rows: List[Dict[str, str]] = []

    for matter_number, rows in mapped.items():
        if not rows:
            continue
        latest = rows[0].get("last_message_at") or ""
        if latest:
            current_latest[matter_number] = latest

        previous = previous_latest.get(matter_number, "")
        if latest and (not previous or latest > previous):
            moved.append(matter_number)

        subject = rows[0].get("subject", "").lower()
        if any(token in subject for token in ("waiting", "awaiting", "pending", "hold")):
            waiting_external.append(matter_number)

        latest_dt = parse_timestamp(latest)
        if not latest_dt:
            continue

        age_days = max(0, (now - latest_dt).days)
        if age_days > active_window_days:
            continue

        matter = matter_lookup.get(matter_number)
        inbox_signal_rows.append(
            {
                "matter_number": matter_number,
                "matter_name": (matter.name if matter else matter_number),
                "thread_count": str(len(rows)),
                "last_activity_at": utc_iso(latest_dt),
                "age_days": str(age_days),
                "latest_subject": (rows[0].get("subject") or "(no subject)"),
                "source_pointer": rows[0].get("source_pointer") or "",
            }
        )

    matter_numbers = [matter.matter_number for matter in matters]
    stalled: List[str] = []
    for matter_number in matter_numbers:
        last_seen_raw = current_latest.get(matter_number) or previous_latest.get(matter_number)
        if not last_seen_raw:
            stalled.append(matter_number)
            continue
        last_seen_dt = parse_timestamp(last_seen_raw)
        if not last_seen_dt:
            stalled.append(matter_number)
            continue
        age_days = (now - last_seen_dt).days
        if age_days >= stalled_days:
            stalled.append(matter_number)

    moved = sorted(set(moved))
    stalled = sorted(set(stalled))
    waiting_external = sorted(set(waiting_external))
    inbox_signal_rows = sorted(
        inbox_signal_rows,
        key=lambda row: (row["last_activity_at"], row["matter_number"]),
        reverse=True,
    )

    delivery_priority = {
        "essential": 0,
        "strategic": 1,
        "standard": 2,
        "parked": 3,
    }
    fulfillment_priority = {
        "urgent": 0,
        "active": 1,
        "keep in view": 2,
        "unknown": 3,
        "paused": 4,
        "pausing": 4,
        "inactive": 5,
        "dormant": 6,
    }

    categories = delivery_taxonomy.get("delivery_categories") if isinstance(delivery_taxonomy, dict) else {}
    categories = categories if isinstance(categories, dict) else {}
    active_category_key = "delivery_active"
    watch_category_key = "delivery_watch"
    active_label = str(((categories.get(active_category_key) or {}).get("label")) or "ML Active")
    watch_label = str(((categories.get(watch_category_key) or {}).get("label")) or "ML Watch")

    delivery_active_rows: List[Dict[str, str]] = []
    delivery_watch_rows: List[Dict[str, str]] = []

    for matter in matters:
        category_key, category_label = classify_delivery_category(matter, delivery_taxonomy)
        delivery_value = matter.delivery_status.strip() or "unknown"
        fulfillment_value = matter.fulfillment_status.strip() or "unknown"
        services_value = service_summary(matter.services, max_items=4)

        row = {
            "matter_number": matter.matter_number,
            "matter_name": matter.name,
            "status": matter.status or "unknown",
            "delivery_status": delivery_value,
            "fulfillment_status": fulfillment_value,
            "category_label": category_label,
            "service_count": str(len(matter.services)),
            "services": services_value,
            "source_pointer": matter.source_pointer,
        }

        if category_key == active_category_key:
            delivery_active_rows.append(row)
        elif category_key == watch_category_key:
            delivery_watch_rows.append(row)

    def _delivery_sort(row: Dict[str, str]) -> Tuple[int, int, str]:
        return (
            delivery_priority.get(str(row.get("delivery_status") or "").lower(), 9),
            fulfillment_priority.get(str(row.get("fulfillment_status") or "").lower(), 9),
            str(row.get("matter_number") or ""),
        )

    delivery_active_rows = sorted(delivery_active_rows, key=_delivery_sort)
    delivery_watch_rows = sorted(delivery_watch_rows, key=_delivery_sort)
    active_service_gaps = [row for row in delivery_active_rows if int(row.get("service_count") or "0") == 0]
    urgent_fulfillment_rows = sorted(
        [
            row
            for row in (delivery_active_rows + delivery_watch_rows)
            if str(row.get("fulfillment_status") or "").strip().lower() == "urgent"
        ],
        key=_delivery_sort,
    )

    def _latest_signal_for_matter(matter_number: str) -> str:
        return str(current_latest.get(matter_number) or previous_latest.get(matter_number) or "").strip()

    row_lookup: Dict[str, Dict[str, str]] = {
        row["matter_number"]: row for row in (delivery_active_rows + delivery_watch_rows)
    }
    stalled_detail_rows: List[Dict[str, str]] = []
    for matter_number in stalled:
        row = row_lookup.get(matter_number)
        if row is None:
            matter = matter_lookup.get(matter_number)
            if matter is None:
                row = {
                    "matter_number": matter_number,
                    "matter_name": matter_number,
                    "status": "unknown",
                    "delivery_status": "unknown",
                    "fulfillment_status": "unknown",
                    "category_label": "Other",
                    "service_count": "0",
                    "services": "0",
                    "source_pointer": "",
                }
            else:
                _, category_label = classify_delivery_category(matter, delivery_taxonomy)
                row = {
                    "matter_number": matter.matter_number,
                    "matter_name": matter.name,
                    "status": matter.status or "unknown",
                    "delivery_status": matter.delivery_status.strip() or "unknown",
                    "fulfillment_status": matter.fulfillment_status.strip() or "unknown",
                    "category_label": category_label,
                    "service_count": str(len(matter.services)),
                    "services": service_summary(matter.services, max_items=4),
                    "source_pointer": matter.source_pointer,
                }
        stalled_detail_rows.append(
            {
                **row,
                "last_signal_at": _latest_signal_for_matter(matter_number) or "none",
            }
        )

    stalled_detail_rows = sorted(stalled_detail_rows, key=_delivery_sort)

    ml1_review_lines: List[str] = []
    if review_required:
        ml1_review_lines.append(f"- Fallback-routed threads requiring review: {len(review_required)}")
    if unmapped:
        ml1_review_lines.append(f"- Unmapped threads requiring routing decision: {len(unmapped)}")
    if urgent_fulfillment_rows:
        ml1_review_lines.append(f"- Fulfillment escalation candidates (urgent): {len(urgent_fulfillment_rows)}")

    operational_gap_lines: List[str] = []
    if active_service_gaps:
        operational_gap_lines.append(f"- {active_label} matters missing service definitions: {len(active_service_gaps)}")
    if sharepoint_ambiguous_count:
        operational_gap_lines.append(f"- SharePoint ambiguous mapping items: {sharepoint_ambiguous_count}")
    if sharepoint_unmapped_count:
        operational_gap_lines.append(f"- SharePoint unmapped items: {sharepoint_unmapped_count}")

    lines = [
        "# Firm Matter Digest",
        "",
        f"Generated at: {generated_at}",
        "",
        "## Role",
        "",
        "This is a system tracking and visibility artifact for ML1.",
        "",
        "Doctrine source: `repo://00_SYSTEM/matters/MATTER_TASK_AND_DASHBOARD_DOCTRINE.md`.",
        "",
        "It answers: what matters must be handled, based on emails, calendar, SharePoint, and Clio / Lexaro signals.",
        "",
        "It does not answer: what exact legal steps must be taken, whether ML1 has failed to do something, "
        "whether a draft is substantively good, or what the actual next legal step is. Those require looking at "
        "the matter folder, recent emails, attachments, live client context, and ML1 judgment.",
        "",
        "Use `ML1 monitoring point` for a matter-linked signal that ML1 must keep visible, but where the exact "
        "legal step still requires matter-folder, email-thread, attachment, client-context, or ML1 judgment.",
        "",
        "## Summary",
        f"- Moved matters: {len(moved)}",
        f"- {active_label} matters: {len(delivery_active_rows)}",
        f"- {active_label} matters with zero services: {len(active_service_gaps)}",
        f"- {watch_label} matters: {len(delivery_watch_rows)}",
        f"- Fulfillment escalation candidates (urgent): {len(urgent_fulfillment_rows)}",
        f"- Inbox-linked active matters (last {active_window_days} days): {len(inbox_signal_rows)}",
        f"- Inbox-signal stalled matters: {len(stalled)}",
        "- Due soon: 0 (Deadline Extractor not active in Slice 1)",
        f"- Unmapped inbox threads: {len(unmapped)}",
        f"- SharePoint file changes: {int(sharepoint_summary.get('file_changes') or 0)}",
        "",
        "## Needs ML1 Review Today",
    ]

    if ml1_review_lines:
        lines.extend(ml1_review_lines)
    else:
        lines.append("- None")

    lines.extend(["", "### Fulfillment Escalation Candidates"])
    if urgent_fulfillment_rows:
        for row in urgent_fulfillment_rows:
            latest_signal = _latest_signal_for_matter(row["matter_number"])
            latest_fragment = f"; latest signal={latest_signal}" if latest_signal else ""
            lines.append(
                f"- {row['matter_number']} :: {row['matter_name']} "
                f"(delivery={row['delivery_status']}; fulfillment={row['fulfillment_status']}; "
                f"services={row['service_count']}{latest_fragment}; {row['source_pointer']})"
            )
    else:
        lines.append("- None")

    lines.extend(["", "## Operational Gaps (Not automatic ML1 review)"])
    if operational_gap_lines:
        lines.extend(operational_gap_lines)
    else:
        lines.append("- None")

    standard_review_overlays = sorted(DASHBOARD_DIR.glob("STANDARD_MATTER_REVIEW_*.md"), reverse=True)
    if standard_review_overlays:
        lines.extend(
            [
                "",
                "## Manual ML1 Monitoring Overlay",
                f"- Standard delivery review: `repo://{display_path(standard_review_overlays[0])}`",
            ]
        )

    lines.extend(
        [
            "",
            "## ML1 Visibility Context",
            f"- Taxonomy contract: `repo://{display_path(DEFAULT_MATTER_DELIVERY_TAXONOMY)}`",
            "",
            f"### {active_label} Queue",
        ]
    )
    if delivery_active_rows:
        rows = [
            [
                row["matter_number"],
                row["matter_name"],
                row["category_label"],
                row["delivery_status"],
                row["fulfillment_status"],
                row["services"],
                row["status"],
                row["source_pointer"],
            ]
            for row in delivery_active_rows
        ]
        lines.append(
            format_table(
                ["Matter Number", "Matter", "Category", "Delivery", "Fulfillment", "Services", "Status", "Source Pointer"],
                rows,
            )
        )
    else:
        lines.append(f"- No {active_label.lower()} matters found.")

    lines.extend(["", f"### {watch_label} Queue"])
    if delivery_watch_rows:
        rows = [
            [
                row["matter_number"],
                row["matter_name"],
                row["category_label"],
                row["delivery_status"],
                row["fulfillment_status"],
                row["services"],
                row["status"],
                row["source_pointer"],
            ]
            for row in delivery_watch_rows
        ]
        lines.append(
            format_table(
                ["Matter Number", "Matter", "Category", "Delivery", "Fulfillment", "Services", "Status", "Source Pointer"],
                rows,
            )
        )
    else:
        lines.append("- None")

    lines.extend(["", f"### {active_label} Service Coverage Gaps"])
    if active_service_gaps:
        for row in active_service_gaps:
            lines.append(
                f"- {row['matter_number']} :: {row['matter_name']} "
                f"(services={row['service_count']}; {row['source_pointer']})"
            )
    else:
        lines.append("- None")

    lines.extend(["", f"## Inbox Signal (Signal 2: Matter-Linked Comms, Last {active_window_days} Days)"])
    if inbox_signal_rows:
        rows = [
            [
                row["matter_number"],
                row["matter_name"],
                row["thread_count"],
                row["last_activity_at"],
                row["age_days"],
                row["latest_subject"],
                row["source_pointer"],
            ]
            for row in inbox_signal_rows
        ]
        lines.append(
            format_table(
                [
                    "Matter Number",
                    "Matter",
                    "Routed Threads",
                    "Last Activity (UTC)",
                    "Age (days)",
                    "Latest Subject",
                    "Source Pointer",
                ],
                rows,
            )
        )
    else:
        lines.append("- No matter-linked comms activity in this time window.")

    lines.extend(["", "## Waiting External"])
    if waiting_external:
        lines.extend([f"- {matter_number}" for matter_number in waiting_external])
    else:
        lines.append("- None flagged in Slice 1 heuristics")

    lines.extend(["", "## Due Soon"])
    lines.append("- Not available in Slice 1 (activate Deadline Extractor in Slice 3)")

    lines.extend(["", "## Document Control"])
    lines.append(f"- SharePoint mapped items: {int(sharepoint_summary.get('mapped_items') or 0)}")
    lines.append(f"- SharePoint unmapped items: {sharepoint_unmapped_count}")
    lines.append(f"- Matters with zero mapped SharePoint items: {matters_without_sharepoint}")

    lines.extend(["", "## Inbox Signal Stalled (Overlay)"])
    lines.append("- `stalled` is an inbox-signal overlay, not a replacement for delivery status.")
    if stalled_detail_rows:
        rows = [
            [
                row["matter_number"],
                row["matter_name"],
                row["category_label"],
                row["delivery_status"],
                row["fulfillment_status"],
                row["last_signal_at"],
                row["source_pointer"],
            ]
            for row in stalled_detail_rows
        ]
        lines.append(
            format_table(
                [
                    "Matter Number",
                    "Matter",
                    "Category",
                    "Delivery",
                    "Fulfillment",
                    "Last Signal (UTC)",
                    "Source Pointer",
                ],
                rows,
            )
        )
    else:
        lines.append("- None")

    lines.extend(["", "## Unmapped Comms Intake"])
    if unmapped:
        for row in unmapped[:20]:
            lines.append(f"- {row['thread_id']} :: {row['subject']} ({row['source_pointer']})")
        if len(unmapped) > 20:
            lines.append(f"- ... {len(unmapped) - 20} more")
    else:
        lines.append("- None")

    next_state = {
        "last_run_at": generated_at,
        "matter_latest_thread_at": current_latest,
        "unmapped_thread_count": len(unmapped),
        "delivery_summary": {
            "active_matters": len(delivery_active_rows),
            "parked_watch_matters": len(delivery_watch_rows),
            "active_without_services": len(active_service_gaps),
            "active_category_key": active_category_key,
            "active_category_label": active_label,
            "watch_category_key": watch_category_key,
            "watch_category_label": watch_label,
        },
        "ml1_triage": {
            "fallback_review_required": len(review_required),
            "unmapped_threads": len(unmapped),
            "fulfillment_escalation_candidates": len(urgent_fulfillment_rows),
            "operational_service_gaps": len(active_service_gaps),
            "sharepoint_ambiguous_items": int(sharepoint_ambiguous_count or 0),
            "sharepoint_unmapped_items": int(sharepoint_unmapped_count or 0),
        },
        "sharepoint_summary": {
            "current_items": int(sharepoint_summary.get("current_items") or 0),
            "mapped_items": int(sharepoint_summary.get("mapped_items") or 0),
            "unmapped_items": int(sharepoint_summary.get("unmapped_items") or 0),
            "file_changes": int(sharepoint_summary.get("file_changes") or 0),
        },
    }
    return "\n".join(lines), next_state


def write_runlog(path: Path, payload: Dict[str, Any], dry_run: bool) -> None:
    if dry_run:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run Matter Command and Control (transitional Matter Admin + Matter File Admin bundle)"
    )
    parser.add_argument("--mode", choices=("daily", "one"), default="daily")
    parser.add_argument("--matter-number", help="Required for --mode one")
    parser.add_argument("--live-gmail", action="store_true", help="Read live Gmail threads for the review pass instead of cache/fallback data.")
    parser.add_argument("--gmail-query", default=DEFAULT_GMAIL_REVIEW_QUERY, help="Gmail query for the live review pass. Defaults to in:inbox.")
    parser.add_argument("--execute-state-labels", action="store_true", help="Apply governed Gmail state labels for the reviewed threads.")
    parser.add_argument("--approval-artifact", default="", help="Approval artifact required for --execute-state-labels.")
    parser.add_argument("--approved-by", default="", help="Approver name required for --execute-state-labels.")
    parser.add_argument("--reason", default="", help="Reason required for --execute-state-labels.")
    parser.add_argument("--clio-cache", default=str(DEFAULT_CLIO_CACHE))
    parser.add_argument("--gmail-cache", default=str(DEFAULT_GMAIL_CACHE))
    parser.add_argument("--sharepoint-cache", default=str(DEFAULT_SHAREPOINT_CACHE))
    parser.add_argument("--sharepoint-metadata-root", default=str(DEFAULT_SHAREPOINT_METADATA_ROOT))
    parser.add_argument("--matter-sharepoint-map", default=str(DEFAULT_MATTER_SHAREPOINT_MAP))
    parser.add_argument("--matter-folder-rules", default=str(DEFAULT_MATTER_FOLDER_RULES))
    parser.add_argument("--run-state", default=str(DEFAULT_RUN_STATE))
    parser.add_argument("--gmail-fallback", default=str(DEFAULT_GMAIL_FALLBACK))
    parser.add_argument("--write-cache", action="store_true", help="Write normalized cache snapshots")
    parser.add_argument("--dry-run", action="store_true", help="Compute outputs but do not write files")
    parser.add_argument("--strict", action="store_true", help="Exit non-zero if no connector records loaded")
    parser.add_argument(
        "--max-threads",
        type=int,
        default=DEFAULT_MAX_THREADS,
        help="Optional cap for threads in scope. Defaults to 25; set 0 for uncapped.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    if args.mode == "one" and not args.matter_number:
        raise SystemExit("--matter-number is required when --mode one is used")
    if args.execute_state_labels and (not args.approval_artifact or not args.approved_by or not args.reason):
        raise SystemExit(
            "--execute-state-labels requires --approval-artifact, --approved-by, and --reason."
        )
    if args.execute_state_labels and args.dry_run:
        raise SystemExit("--execute-state-labels cannot be combined with --dry-run.")
    if args.execute_state_labels:
        from gmail_mcp_server import _resolve_approval_artifact

        approval_path = _resolve_approval_artifact(args.approval_artifact)
        if not approval_path.exists():
            raise SystemExit(f"approval_artifact not found: {approval_path}")

    generated_at = utc_iso()

    # Load config contracts.
    gmail_label_rules = load_yaml(CONFIG_DIR / "gmail_label_rules.yml")
    run_schedule = load_yaml(CONFIG_DIR / "run_schedule.yml")
    delivery_taxonomy = merge_delivery_taxonomy(load_yaml(DEFAULT_MATTER_DELIVERY_TAXONOMY))
    stalled_days = int((run_schedule.get("digest") or {}).get("stalled_days") or 14)
    active_window_days = int((run_schedule.get("digest") or {}).get("active_window_days") or 7)

    matter_pattern = compile_matter_regex(gmail_label_rules)
    gmail_query = str(
        args.gmail_query
        or (((run_schedule.get("runs") or {}).get("daily") or {}).get("scope") or {}).get("gmail_query")
        or DEFAULT_GMAIL_REVIEW_QUERY
    ).strip() or DEFAULT_GMAIL_REVIEW_QUERY

    clio_cache = Path(args.clio_cache)
    gmail_cache = Path(args.gmail_cache)
    run_state_path = Path(args.run_state)
    gmail_fallback = Path(args.gmail_fallback)

    matters, clio_source = load_clio_matters(
        clio_cache,
        write_cache=args.write_cache,
        delivery_taxonomy=delivery_taxonomy,
    )
    live_gmail = bool(args.live_gmail or args.execute_state_labels)
    thread_selection_summary: Dict[str, Any] = {}
    if live_gmail:
        threads, gmail_source, thread_selection_summary = load_live_gmail_threads(
            query=gmail_query,
            max_review_threads=args.max_threads,
        )
    else:
        threads, gmail_source = load_gmail_threads(
            gmail_cache,
            gmail_fallback,
            write_cache=args.write_cache,
        )
        if args.max_threads > 0:
            threads = threads[: args.max_threads]
        thread_selection_summary = {
            "query": gmail_query,
            "listed_threads": len(threads),
            "inspected_threads": len(threads),
            "reviewed_threads": len(threads),
        }

    if args.strict and (not matters or not threads):
        print("Strict mode failure: missing matter or thread records")
        return 2

    if args.mode == "one" and args.matter_number:
        scoped = {args.matter_number}
        matters = [matter for matter in matters if matter.matter_number == args.matter_number]
    else:
        scoped = set(matter.matter_number for matter in matters)

    mapped, unmapped, review_required = route_threads_to_matters(
        threads=threads,
        matter_numbers=scoped,
        matter_pattern=matter_pattern,
        single_matter_scope=args.matter_number if args.mode == "one" else None,
    )

    if args.mode == "one":
        scoped_thread_ids = {
            str(row.get("thread_id") or "")
            for rows in mapped.values()
            for row in rows
        }
        scoped_thread_ids.update(str(row.get("thread_id") or "") for row in unmapped)
        scoped_thread_ids.update(str(row.get("thread_id") or "") for row in review_required)
        threads = [thread for thread in threads if thread.thread_id in scoped_thread_ids]
        thread_selection_summary["reviewed_threads"] = len(threads)

    matter_lookup = {matter.matter_number: matter for matter in matters}
    local_matter_paths = discover_local_matter_paths()
    state_review_batch = build_state_review_batch(
        threads=threads,
        mapped=mapped,
        generated_at=generated_at,
        gmail_query=gmail_query,
        selection_summary=thread_selection_summary,
        single_matter_scope=args.matter_number if args.mode == "one" else None,
    )
    proposal_path: Optional[Path] = None
    execution_path: Optional[Path] = None
    state_review_execution: Dict[str, Any] = {}

    if live_gmail:
        proposal_path = BATCH_PROPOSALS_DIR / f"{state_review_batch['batch_id']}.json"
    if proposal_path and not args.dry_run:
        write_json(proposal_path, state_review_batch)
    if args.execute_state_labels:
        execution_path = BATCH_EXECUTIONS_DIR / f"{state_review_batch['batch_id']}.json"
        state_review_execution = execute_state_review_batch(
            batch_payload=state_review_batch,
            approval_artifact_text=args.approval_artifact,
            approved_by=args.approved_by,
            reason=args.reason,
        )
        if execution_path and not args.dry_run:
            write_json(execution_path, state_review_execution)

    # Agent 1 output: matter index
    write_matter_index(
        MATTER_INDEX_PATH,
        matters,
        clio_source,
        generated_at,
        delivery_taxonomy=delivery_taxonomy,
        dry_run=args.dry_run,
    )

    # Agent 2 output: unmapped dashboard + per-matter thread status
    write_unmapped_dashboard(INBOX_UNMAPPED_PATH, unmapped, generated_at, dry_run=args.dry_run)
    missing_matter_paths = write_matter_status_files(
        mapped=mapped,
        matter_lookup=matter_lookup,
        local_matter_paths=local_matter_paths,
        generated_at=generated_at,
        dry_run=args.dry_run,
    )

    # Agent 4 output: SharePoint document index + deltas + gaps
    sharepoint_cache = Path(args.sharepoint_cache)
    sharepoint_metadata_root = Path(args.sharepoint_metadata_root)
    matter_sharepoint_map_path = Path(args.matter_sharepoint_map)
    matter_folder_rules_path = Path(args.matter_folder_rules)
    explicit_mappings = load_matter_sharepoint_map(matter_sharepoint_map_path)
    expected_folders = load_expected_sharepoint_folders(matter_folder_rules_path)

    current_docs, previous_docs, sharepoint_source, sharepoint_cache_source, sharepoint_baseline_generated_at = load_sharepoint_docs(
        sharepoint_cache,
        sharepoint_metadata_root,
    )
    sharepoint_rows, sharepoint_unmapped, sharepoint_ambiguous = map_sharepoint_docs_to_matters(
        docs=current_docs,
        matter_numbers=scoped,
        matter_pattern=matter_pattern,
        explicit_mappings=explicit_mappings,
        single_matter_scope=args.matter_number if args.mode == "one" else None,
    )
    previous_rows, _, _ = map_sharepoint_docs_to_matters(
        docs=previous_docs,
        matter_numbers=scoped,
        matter_pattern=matter_pattern,
        explicit_mappings=explicit_mappings,
        single_matter_scope=args.matter_number if args.mode == "one" else None,
    )
    sharepoint_summary, docs_by_matter, deltas_by_matter = build_sharepoint_doc_views(
        current_rows=sharepoint_rows,
        previous_rows=previous_rows,
    )
    matters_without_sharepoint_docs = [
        matter
        for matter in sorted(matters, key=lambda m: m.matter_number)
        if not docs_by_matter.get(matter.matter_number)
    ]

    missing_sharepoint_matter_paths = write_sharepoint_matter_files(
        matters=matters,
        local_matter_paths=local_matter_paths,
        docs_by_matter=docs_by_matter,
        deltas_by_matter=deltas_by_matter,
        expected_folders=expected_folders,
        generated_at=generated_at,
        source=sharepoint_source,
        baseline_generated_at=sharepoint_baseline_generated_at,
        dry_run=args.dry_run,
    )
    write_sharepoint_gaps_dashboard(
        path=SHAREPOINT_GAPS_PATH,
        generated_at=generated_at,
        source=sharepoint_source,
        summary=sharepoint_summary,
        unmapped_rows=sharepoint_unmapped,
        ambiguous_rows=sharepoint_ambiguous,
        matters_without_docs=matters_without_sharepoint_docs,
        dry_run=args.dry_run,
    )

    if args.write_cache and not args.dry_run:
        sharepoint_cache_payload = {
            "generated_at": generated_at,
            "source": sharepoint_source,
            "summary": sharepoint_summary,
            "docs": serialize_doc_rows(sharepoint_rows),
        }
        write_json(sharepoint_cache, sharepoint_cache_payload)

    prior_state = load_run_state(run_state_path)
    digest_markdown, next_state = build_digest(
        matters=matters,
        mapped=mapped,
        unmapped=unmapped,
        review_required=review_required,
        run_state=prior_state,
        generated_at=generated_at,
        stalled_days=stalled_days,
        active_window_days=active_window_days,
        delivery_taxonomy=delivery_taxonomy,
        sharepoint_summary=sharepoint_summary,
        sharepoint_ambiguous_count=len(sharepoint_ambiguous),
        sharepoint_unmapped_count=len(sharepoint_unmapped),
        matters_without_sharepoint=len(matters_without_sharepoint_docs),
    )

    exceptions_lines: List[str] = []
    if missing_matter_paths:
        exceptions_lines.extend(
            [
                "- Missing local matter folder for routed matter(s):",
                *[f"  - {matter_number}" for matter_number in sorted(missing_matter_paths)],
            ]
        )
    if missing_sharepoint_matter_paths:
        exceptions_lines.extend(
            [
                "- Missing local matter folder for SharePoint packet generation:",
                *[f"  - {matter_number}" for matter_number in sorted(missing_sharepoint_matter_paths)],
            ]
        )
    if exceptions_lines:
        digest_markdown += "\n\n## Exceptions\n"
        digest_markdown += "\n".join(exceptions_lines)

    if not args.dry_run:
        write_text(MATTER_DIGEST_PATH, digest_markdown)
        write_json(run_state_path, next_state)

    runlog = {
        "generated_at": generated_at,
        "mode": args.mode,
        "matter_number": args.matter_number or "",
        "sources": {
            "clio": clio_source,
            "gmail": gmail_source,
            "sharepoint": sharepoint_source,
            "sharepoint_baseline": sharepoint_cache_source,
        },
        "counts": {
            "matters": len(matters),
            "delivery_active_matters": int((next_state.get("delivery_summary") or {}).get("active_matters") or 0),
            "delivery_watch_matters": int((next_state.get("delivery_summary") or {}).get("parked_watch_matters") or 0),
            "delivery_active_without_services": int((next_state.get("delivery_summary") or {}).get("active_without_services") or 0),
            "threads": len(threads),
            "reviewed_threads": int(state_review_batch.get("threads_reviewed") or 0),
            "mapped_threads": sum(len(rows) for rows in mapped.values()),
            "unmapped_threads": len(unmapped),
            "review_required_threads": len(review_required),
            "state_label_changed_threads": int(state_review_execution.get("changed_count") or 0),
            "state_label_no_change_threads": int(state_review_execution.get("no_change_count") or 0),
            "missing_local_matter_paths": len(missing_matter_paths),
            "sharepoint_items": int(sharepoint_summary.get("current_items") or 0),
            "sharepoint_mapped_items": int(sharepoint_summary.get("mapped_items") or 0),
            "sharepoint_unmapped_items": int(sharepoint_summary.get("unmapped_items") or 0),
            "sharepoint_ambiguous_items": len(sharepoint_ambiguous),
            "sharepoint_added_items": int(sharepoint_summary.get("added_items") or 0),
            "sharepoint_changed_items": int(sharepoint_summary.get("changed_items") or 0),
            "sharepoint_removed_items": int(sharepoint_summary.get("removed_items") or 0),
            "sharepoint_missing_local_matter_paths": len(missing_sharepoint_matter_paths),
        },
        "outputs": {
            "matter_index": display_path(MATTER_INDEX_PATH),
            "matter_digest": display_path(MATTER_DIGEST_PATH),
            "inbox_unmapped": display_path(INBOX_UNMAPPED_PATH),
            "sharepoint_gaps": display_path(SHAREPOINT_GAPS_PATH),
            "state_review_batch": display_path(proposal_path) if proposal_path else "",
            "state_review_execution": display_path(execution_path) if execution_path else "",
        },
    }

    timestamp_compact = generated_at.replace(":", "").replace("-", "")
    write_runlog(RUN_LOG_DIR / f"run_{timestamp_compact}.json", runlog, dry_run=args.dry_run)

    print(
        "Matter admin run complete: "
        f"matters={len(matters)} "
        f"threads={len(threads)} "
        f"reviewed={int(state_review_batch.get('threads_reviewed') or 0)} "
        f"unmapped={len(unmapped)} "
        f"state_label_changes={int(state_review_execution.get('changed_count') or 0)} "
        f"sharepoint_items={int(sharepoint_summary.get('current_items') or 0)} "
        f"sharepoint_unmapped={len(sharepoint_unmapped)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
