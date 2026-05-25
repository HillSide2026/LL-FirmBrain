#!/usr/bin/env python3
"""
Daily Full Sweep Runner

Orchestrates the end-to-end daily chain:
  1. Matter Admin  (scripts/run_matter_admin.py)
  2. Portfolio Agents  (00_SYSTEM/scripts/run_ll_portfolio_agents.py)
  3. Chief of Staff Synthesis  (LLM-001, via OpenRouter API or claude CLI fallback)

Writes a run log to:
  06_RUNS/${run_id}/daily_sweep/RUN_LOG.md
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from textwrap import dedent
from typing import Dict, Optional

import requests


REPO_ROOT = Path(__file__).resolve().parents[2]
RUN_LOG_DIR = REPO_ROOT / "06_RUNS"

MATTER_ADMIN_SCRIPT = REPO_ROOT / "scripts" / "run_matter_admin.py"
PORTFOLIO_AGENTS_SCRIPT = REPO_ROOT / "00_SYSTEM" / "scripts" / "run_ll_portfolio_agents.py"

CLAUDE_SEARCH_PATHS = [
    Path.home() / "Library" / "Application Support" / "Claude" / "claude-code",
]

# Timeout for LLM-001 synthesis step (seconds)
LLM001_TIMEOUT = 120

OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"
DEFAULT_COS_MODEL = "google/gemini-2.0-flash-001"

# Input files LLM-001 reads (relative to REPO_ROOT)
LLM001_INPUT_FILES = {
    "PROJECT_HEALTH_ROLLUP.md":
        "04_INITIATIVES/LL_PORTFOLIO/03_FIRM_OPERATIONS/LLP-043/PROJECT_HEALTH_ROLLUP.md",
    "PORTFOLIO_STATUS_DASHBOARD.md":
        "04_INITIATIVES/LL_PORTFOLIO/03_FIRM_OPERATIONS/LLP-042/PORTFOLIO_STATUS_DASHBOARD.md",
    "PROJECT_PRIORITY_MATRIX.md":
        "04_INITIATIVES/LL_PORTFOLIO/03_FIRM_OPERATIONS/LLP-042/PROJECT_PRIORITY_MATRIX.md",
    "SEQUENCING_RECOMMENDATIONS.md":
        "04_INITIATIVES/LL_PORTFOLIO/03_FIRM_OPERATIONS/LLP-042/SEQUENCING_RECOMMENDATIONS.md",
    "BOTTLENECK_ANALYSIS.md":
        "04_INITIATIVES/LL_PORTFOLIO/03_FIRM_OPERATIONS/LLP-042/BOTTLENECK_ANALYSIS.md",
    "RESOURCE_COLLISION_REPORT.md":
        "04_INITIATIVES/LL_PORTFOLIO/03_FIRM_OPERATIONS/LLP-042/RESOURCE_COLLISION_REPORT.md",
    "WIP_LOAD_ANALYSIS.md":
        "04_INITIATIVES/LL_PORTFOLIO/03_FIRM_OPERATIONS/LLP-042/WIP_LOAD_ANALYSIS.md",
    "GOVERNANCE_COMPLIANCE_AUDIT.md":
        "04_INITIATIVES/LL_PORTFOLIO/03_FIRM_OPERATIONS/PORTFOLIO_GOVERNANCE/GOVERNANCE_COMPLIANCE_AUDIT.md",
    "STAGE_GATE_VIOLATION_REPORT.md":
        "04_INITIATIVES/LL_PORTFOLIO/03_FIRM_OPERATIONS/PORTFOLIO_GOVERNANCE/STAGE_GATE_VIOLATION_REPORT.md",
    "APPROVAL_GAP_REPORT.md":
        "04_INITIATIVES/LL_PORTFOLIO/03_FIRM_OPERATIONS/PORTFOLIO_GOVERNANCE/APPROVAL_GAP_REPORT.md",
    "DOCTRINE_DRIFT_REPORT.md":
        "04_INITIATIVES/LL_PORTFOLIO/03_FIRM_OPERATIONS/PORTFOLIO_GOVERNANCE/DOCTRINE_DRIFT_REPORT.md",
    "CONTRADICTION_ALERTS.md":
        "04_INITIATIVES/LL_PORTFOLIO/03_FIRM_OPERATIONS/PORTFOLIO_GOVERNANCE/CONTRADICTION_ALERTS.md",
}

COS_OUTPUT_DIR = REPO_ROOT / "04_INITIATIVES/LL_PORTFOLIO/CHIEF_OF_STAFF"


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def generate_run_id() -> str:
    stamp = datetime.now(timezone.utc).strftime("%H%M%SZ")
    date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    return f"RUN-{date}-DAILY-SWEEP-{stamp}"


def load_dotenv() -> None:
    """Load .env from repo root into os.environ (no external dependency)."""
    env_path = REPO_ROOT / ".env"
    if not env_path.exists():
        return
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


def find_claude_binary() -> Optional[str]:
    """Locate the claude CLI binary."""
    import shutil
    if shutil.which("claude"):
        return "claude"
    for base in CLAUDE_SEARCH_PATHS:
        if not base.is_dir():
            continue
        candidates = sorted(
            (v / "claude" for v in base.iterdir() if v.is_dir()),
            key=lambda p: p.parent.name,
            reverse=True,
        )
        for candidate in candidates:
            if candidate.is_file() and os.access(candidate, os.X_OK):
                return str(candidate)
    return None


def run_python_script(script: Path, label: str) -> Dict:
    """Run a Python script as a subprocess. Returns result dict."""
    print(f"[daily_sweep] Starting: {label}")
    result = subprocess.run(
        [sys.executable, str(script)],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    status = "ok" if result.returncode == 0 else "failed"
    print(f"[daily_sweep] {label}: {status} (rc={result.returncode})")
    if result.stderr.strip():
        print(f"[daily_sweep] {label} stderr: {result.stderr.strip()[:500]}")
    return {
        "label": label,
        "script": str(script.relative_to(REPO_ROOT)),
        "return_code": result.returncode,
        "status": status,
        "stdout": result.stdout.strip(),
        "stderr": result.stderr.strip(),
    }


def read_llm001_inputs() -> Dict[str, str]:
    """Read all LLM-001 input files. Returns filename -> content (or error string)."""
    contents = {}
    for name, rel_path in LLM001_INPUT_FILES.items():
        path = REPO_ROOT / rel_path
        if path.exists():
            contents[name] = path.read_text(encoding="utf-8")
        else:
            contents[name] = f"[FILE NOT FOUND: {rel_path}]"
    return contents


def build_llm001_api_prompt(run_id: str, today: str, input_files: Dict[str, str]) -> str:
    """Build a self-contained prompt for the OpenRouter API call."""
    file_block = "\n\n".join(
        f"### {name}\n```\n{content}\n```"
        for name, content in input_files.items()
    )
    return dedent(f"""\
        You are LLM-001, the Chief of Staff agent for Levine Law's second brain system.

        Today: {today}
        Run ID: {run_id}

        Your job: synthesize the 12 management-agent output files below into three output files
        for ML1 (Matthew Levine). You coordinate — you do not decide. All outputs are advisory.

        Authority rules:
        - Do NOT approve any stage gate, metric, scope change, or doctrine
        - Do NOT issue binding instructions
        - Do NOT override ML1 decisions
        - Flag any missing or stale inputs rather than proceeding past them

        Ranking priority: cash flow first. Items that directly affect near-term revenue
        (F01 intake, F02 launch, matter volume, billing capacity) rank above governance work.
        LL incentives are primary; HillSide linkage is secondary.

        ## Input Files

        {file_block}

        ## Output Instructions

        Produce exactly three files. Use the delimiter format below — no other text outside it:

        ===FILE: COS_BRIEF.md===
        <write COS_BRIEF.md here — narrative prose, no tables, readable in under 3 minutes.
        Sections: Portfolio Health Summary, Cash Flow Priority Top Actions,
        What Requires ML1 Input (ML1_REQUIRED items), What the System Can Handle (SYSTEM_CAN_HANDLE),
        Cross-Agent Conflicts, Governance Holds, Flow Bottlenecks, Doctrine Drift Signal, Deferred Items.
        Header: Generated: {today}T00:00:00Z | Agent: LLM-001 | Run: {run_id}
        Footer: > Advisory output. ML1 approval required before any action is taken.>

        ===FILE: ML1_DECISION_QUEUE.md===
        <write ML1_DECISION_QUEUE.md here — ranked table:
        | Rank | Project | Decision Needed | Cash Flow Impact | ML1 or System | Urgency | Blocking | Source |
        Rank by: (1) cash-flow-direct + ML1_REQUIRED, (2) cross-agent conflicts, (3) approval blocks,
        (4) stage gate violations, (5) sequencing decisions, (6) other flags.
        Header and advisory footer same as above.>

        ===FILE: CROSS_AGENT_CONFLICTS.md===
        <write CROSS_AGENT_CONFLICTS.md here — for each conflict where LLM-005 recommends
        advancement on a project that LLM-006 has flagged: project name, LLM-005 signal,
        LLM-006 signal, conflict type, ML1 decision needed.
        If none: state "No cross-agent conflicts detected in this run."
        Header and advisory footer same as above.>
    """)


def parse_cos_sections(raw: str) -> Dict[str, str]:
    """Parse the three ===FILE: name=== sections from model output."""
    sections: Dict[str, str] = {}
    pattern = re.compile(r"===FILE:\s*(\S+\.md)===\s*\n(.*?)(?====FILE:|\Z)", re.DOTALL)
    for match in pattern.finditer(raw):
        filename = match.group(1).strip()
        content = match.group(2).strip()
        sections[filename] = content + "\n"
    return sections


def invoke_llm001_openrouter(run_id: str, api_key: str) -> Dict:
    """Invoke LLM-001 Chief of Staff via OpenRouter API."""
    label = "LLM-001 Chief of Staff"
    model = os.environ.get("OPENROUTER_COS_MODEL", DEFAULT_COS_MODEL)
    print(f"[daily_sweep] Starting: {label} (OpenRouter / {model})")

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    input_files = read_llm001_inputs()
    missing = [name for name, content in input_files.items() if content.startswith("[FILE NOT FOUND")]
    if missing:
        print(f"[daily_sweep] {label}: missing input files: {missing}")

    prompt = build_llm001_api_prompt(run_id, today, input_files)

    try:
        response = requests.post(
            OPENROUTER_API_URL,
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
                "HTTP-Referer": "https://github.com/HillSide2026/ll-secondbrain",
            },
            json={
                "model": model,
                "messages": [{"role": "user", "content": prompt}],
            },
            timeout=LLM001_TIMEOUT,
        )
        response.raise_for_status()
    except requests.Timeout:
        msg = f"OpenRouter request timed out after {LLM001_TIMEOUT}s"
        print(f"[daily_sweep] {label}: {msg}")
        return {"label": label, "status": "timeout", "error": msg}
    except requests.RequestException as exc:
        msg = f"OpenRouter request failed: {exc}"
        print(f"[daily_sweep] {label}: {msg}")
        return {"label": label, "status": "failed", "error": msg}

    raw = response.json()["choices"][0]["message"]["content"]
    sections = parse_cos_sections(raw)

    COS_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    if not sections:
        # Save raw output for debugging if parsing failed
        raw_path = COS_OUTPUT_DIR / f"raw_output_{run_id}.txt"
        raw_path.write_text(raw, encoding="utf-8")
        msg = f"Could not parse output sections — raw output saved to {raw_path.relative_to(REPO_ROOT)}"
        print(f"[daily_sweep] {label}: {msg}")
        return {"label": label, "status": "failed", "error": msg}

    for filename, content in sections.items():
        (COS_OUTPUT_DIR / filename).write_text(content, encoding="utf-8")
        print(f"[daily_sweep] {label}: wrote {filename}")

    print(f"[daily_sweep] {label}: ok ({len(sections)} files written)")
    return {"label": label, "status": "ok", "return_code": 0}


def invoke_llm001_claude_cli(run_id: str) -> Dict:
    """Invoke LLM-001 Chief of Staff via the claude CLI (fallback)."""
    label = "LLM-001 Chief of Staff"
    print(f"[daily_sweep] Starting: {label} (claude CLI)")

    claude_bin = find_claude_binary()
    if not claude_bin:
        msg = "claude binary not found — skipping LLM-001 synthesis"
        print(f"[daily_sweep] WARNING: {msg}")
        return {"label": label, "status": "skipped", "error": msg}

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    input_files = read_llm001_inputs()
    prompt = build_llm001_api_prompt(run_id, today, input_files)

    try:
        result = subprocess.run(
            [claude_bin, "--dangerously-skip-permissions", "--print", "-p", prompt],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
            timeout=LLM001_TIMEOUT,
        )
        status = "ok" if result.returncode == 0 else "failed"
        print(f"[daily_sweep] {label}: {status} (rc={result.returncode})")
        return {
            "label": label,
            "return_code": result.returncode,
            "status": status,
            "stdout": result.stdout.strip()[:2000],
            "stderr": result.stderr.strip()[:500],
        }
    except subprocess.TimeoutExpired:
        msg = f"timed out after {LLM001_TIMEOUT}s"
        print(f"[daily_sweep] {label}: {msg}")
        return {"label": label, "status": "timeout", "error": msg}


def invoke_llm001(run_id: str, force_claude: bool = False) -> Dict:
    """Invoke LLM-001: use OpenRouter if key is available, else fall back to claude CLI."""
    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if api_key and not force_claude:
        return invoke_llm001_openrouter(run_id, api_key)
    return invoke_llm001_claude_cli(run_id)


def write_run_log(run_root: Path, steps: list[Dict]) -> None:
    run_root.mkdir(parents=True, exist_ok=True)
    overall = "ok" if all(s["status"] in ("ok", "skipped") for s in steps) else "partial"

    lines = [
        "# RUN LOG — Daily Full Sweep",
        "",
        f"Generated: {utc_now()}",
        f"Overall status: {overall}",
        "",
    ]
    for step in steps:
        rc = step.get("return_code", "—")
        lines += [
            f"## {step['label']}",
            f"- Status: {step['status']}",
            f"- Return code: {rc}",
        ]
        if step.get("error"):
            lines.append(f"- Error: {step['error']}")
        lines.append("")

    (run_root / "RUN_LOG.md").write_text("\n".join(lines), encoding="utf-8")

    provenance = {
        "run_id": run_root.parent.name,
        "generated_at": utc_now(),
        "steps": steps,
    }
    (run_root / "provenance.json").write_text(json.dumps(provenance, indent=2), encoding="utf-8")
    print(f"[daily_sweep] Run log written: {run_root}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the daily full sweep.")
    parser.add_argument("--run-id", help="Override run ID (default: auto)")
    parser.add_argument("--skip-cos", action="store_true", help="Skip LLM-001 synthesis step")
    parser.add_argument("--use-claude", action="store_true", help="Force claude CLI for LLM-001 (skip OpenRouter)")
    args = parser.parse_args()

    run_id = args.run_id or generate_run_id()
    run_root = RUN_LOG_DIR / run_id / "daily_sweep"

    print(f"[daily_sweep] Starting run: {run_id}")
    steps: list[Dict] = []

    # Step 1: Matter Admin
    result = run_python_script(MATTER_ADMIN_SCRIPT, "Matter Admin")
    steps.append(result)
    if result["status"] == "failed":
        write_run_log(run_root, steps)
        print("[daily_sweep] Aborting: matter admin failed (required for downstream steps)")
        return 1

    # Step 2: Portfolio Agents
    result = run_python_script(PORTFOLIO_AGENTS_SCRIPT, "Portfolio Agents (LLM-004/005/006)")
    steps.append(result)
    if result["status"] == "failed":
        write_run_log(run_root, steps)
        print("[daily_sweep] Aborting: portfolio agents failed (required for LLM-001)")
        return 1

    # Step 3: Chief of Staff Synthesis
    if args.skip_cos:
        steps.append({"label": "LLM-001 Chief of Staff", "status": "skipped", "return_code": "—"})
    else:
        result = invoke_llm001(run_id, force_claude=args.use_claude)
        steps.append(result)

    write_run_log(run_root, steps)
    overall = all(s["status"] in ("ok", "skipped") for s in steps)
    print(f"[daily_sweep] Daily full sweep complete: {run_root}")
    return 0 if overall else 1


if __name__ == "__main__":
    raise SystemExit(main())
