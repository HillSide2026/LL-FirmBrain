#!/usr/bin/env python3
"""
Lexaro Mode 1 — read-only connectivity smoke test.

Discovers the API, authenticates, and calls read-only external endpoints.
Prints status codes and redacted sample responses. Never writes to Lexaro.

Usage:
    python3 scripts/lexaro_smoke_test.py

Requires .env in the repo root with:
    Lexaro_Key_ID: <value>
    Lexaro_API_Secret: <value>

Note: .env uses YAML-style `: ` separators for the Lexaro block (not `=`).
"""

from __future__ import annotations

import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Union

BASE_URL = "https://app.lexaro.ca"

# Read-only external API endpoints to probe
SMOKE_ENDPOINTS = [
    "/api/external/v1/matters",
    "/api/external/v1/clients",
    "/api/external/v1/tasks",
    "/api/external/v1/documents",
]


def load_env(path: Path) -> dict:
    """Parse .env file that mixes KEY=value and YAML Key: value lines."""
    env: dict = {}
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        # Standard dotenv format
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_]*)=(.*)$", line)
        if m:
            env[m.group(1)] = m.group(2).strip()
            continue
        # YAML-style: Key: value (used by Lexaro block in .env)
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_]*)\s*:\s*(.+)$", line)
        if m:
            env[m.group(1)] = m.group(2).strip()
    return env


def get_credentials(env: dict) -> tuple[str, str]:
    key_id = env.get("Lexaro_Key_ID") or env.get("LEXARO_KEY_ID")
    secret = env.get("Lexaro_API_Secret") or env.get("LEXARO_API_SECRET")
    if not key_id or not secret:
        sys.exit(
            "ERROR: Lexaro_Key_ID and Lexaro_API_Secret not found in .env.\n"
            "Expected either 'Lexaro_Key_ID: <value>' or 'LEXARO_KEY_ID=<value>'."
        )
    return key_id, secret


def redact(text: str, key_id: str, secret: str) -> str:
    return text.replace(key_id, "[KEY_ID_REDACTED]").replace(secret, "[SECRET_REDACTED]")


def get_json(url: str, key_id: str, secret: str, timeout: int = 10) -> tuple[int, dict | str]:
    headers = {
        "Accept": "application/json",
        "User-Agent": "LL-SecondBrain/1.0 (read-only smoke test)",
        "X-Api-Key": key_id,
        "X-Api-Secret": secret,
    }
    req = urllib.request.Request(url, headers=headers)
    try:
        resp = urllib.request.urlopen(req, timeout=timeout)
        body = resp.read(4000).decode(errors="replace")
        try:
            return resp.status, json.loads(body)
        except json.JSONDecodeError:
            return resp.status, body
    except urllib.error.HTTPError as e:
        body = e.read(1000).decode(errors="replace")
        try:
            return e.code, json.loads(body)
        except json.JSONDecodeError:
            return e.code, body
    except urllib.error.URLError as e:
        sys.exit(f"Network error reaching {url}: {e.reason}")


def summarize_response(data: dict | str, key_id: str, secret: str) -> str:
    """Return a short redacted summary of the response."""
    if isinstance(data, str):
        return redact(data[:300], key_id, secret)

    safe = json.dumps(data, indent=2)
    safe = redact(safe, key_id, secret)

    if "data" in data and isinstance(data["data"], list):
        count = len(data["data"])
        sample = data["data"][:2] if count > 0 else []
        preview = json.dumps({"count": count, "sample_first_2": sample}, indent=2)
        return redact(preview, key_id, secret)

    return safe[:600]


def check_unauthenticated_error(status: int, data: dict | str) -> str | None:
    """Return a human-readable diagnosis if the response is an auth failure."""
    if isinstance(data, dict):
        msg = data.get("message", "")
        if "Missing API credentials" in msg:
            return "Auth headers not recognized by the external API middleware."
        if "Unauthenticated" in msg:
            return "Credentials rejected (regular API guard — wrong endpoint prefix)."
        if "Server Error" in msg and status == 500:
            return (
                "Server Error 500. Lexaro's external API middleware throws an unhandled "
                "exception when credentials are processed. This is a known Lexaro-side bug "
                "in the /api/external/v1/* middleware — it 500s on both valid and invalid "
                "credentials. Contact Lexaro support to verify credentials and bug status."
            )
    return None


def run_smoke_test():
    env_path = Path(__file__).parent.parent / ".env"
    if not env_path.exists():
        sys.exit(f"ERROR: .env not found at {env_path}")

    env = load_env(env_path)
    key_id, secret = get_credentials(env)

    print("=" * 60)
    print("Lexaro Mode 1 — Read-Only Connectivity Smoke Test")
    print("=" * 60)
    print(f"Base URL : {BASE_URL}")
    print(f"Key ID   : {key_id[:7]}...  ({len(key_id)} chars)")
    print(f"Secret   : {'*' * 8}  ({len(secret)} chars)")
    print(f"Auth     : X-Api-Key + X-Api-Secret headers")
    print()

    any_success = False

    for endpoint in SMOKE_ENDPOINTS:
        url = BASE_URL + endpoint
        print(f"GET {endpoint}")
        status, data = get_json(url, key_id, secret)

        diagnosis = check_unauthenticated_error(status, data)
        if status == 200:
            any_success = True
            print(f"  Status : {status} OK")
            print(f"  Sample :\n{summarize_response(data, key_id, secret)}")
        else:
            print(f"  Status : {status}")
            if diagnosis:
                print(f"  Diagnosis: {diagnosis}")
            else:
                print(f"  Response : {summarize_response(data, key_id, secret)}")
        print()

    print("=" * 60)
    if any_success:
        print("RESULT: PASS — At least one read-only endpoint returned 200.")
    else:
        print("RESULT: FAIL — No endpoint returned 200.")
        print()
        print("KNOWN ISSUE:")
        print("  Lexaro's external API middleware (/api/external/v1/*) returns HTTP 500")
        print("  for any request that includes both X-Api-Key and X-Api-Secret headers,")
        print("  regardless of whether the credentials are valid or not.")
        print("  This is a server-side bug in Lexaro's code.")
        print()
        print("NEXT STEPS:")
        print("  1. Confirm credentials are active: Settings > API Access in the Lexaro UI.")
        print("  2. Report the 500 error to Lexaro support (api/external/v1/* middleware).")
        print("  3. Ask Lexaro support for the correct auth header format for external API keys.")
        print("  4. Re-run this script once Lexaro confirms the correct format.")
    print("=" * 60)


if __name__ == "__main__":
    run_smoke_test()
