#!/usr/bin/env python3
"""
validate_matter_registry.py — Matter Registry Integrity Check

Validates that MATTER_REGISTRY.md and the repo MATTER.yaml files are in sync:
  1. No duplicate matter IDs in MATTER_REGISTRY.md
  2. Every MATTER.yaml folder appears in MATTER_REGISTRY.md
  3. Every MATTER_REGISTRY.md entry has a corresponding MATTER.yaml folder
  4. Row counts match across: MATTER_REGISTRY.md, MATTER.yaml dirs, DASHBOARDS/MATTER_INDEX.md

Usage:
    python scripts/validate_matter_registry.py [--verbose]

Exit codes:
    0 = All checks pass
    1 = Integrity errors found
"""

import re
import sys
from pathlib import Path
from datetime import datetime

REPO_ROOT = Path(__file__).resolve().parent.parent
MATTERS_ROOT = REPO_ROOT / "05_MATTERS"
REGISTRY_PATH = MATTERS_ROOT / "MATTER_REGISTRY.md"
DASHBOARD_INDEX_PATH = MATTERS_ROOT / "DASHBOARDS" / "MATTER_INDEX.md"
DELIVERY_FOLDERS = ["ESSENTIAL", "STRATEGIC", "STANDARD", "NORMAL", "PARKED"]

MATTER_ID_PATTERN = re.compile(r"^\d{2}-\d{3,4}-\d{5}$")


def parse_registry() -> list[dict]:
    """Parse matter IDs and names from MATTER_REGISTRY.md table rows."""
    if not REGISTRY_PATH.exists():
        return []
    entries = []
    with open(REGISTRY_PATH) as f:
        for line in f:
            line = line.strip()
            if not line.startswith("|"):
                continue
            parts = [p.strip() for p in line.split("|") if p.strip()]
            if len(parts) < 3:
                continue
            matter_id = parts[0]
            if not MATTER_ID_PATTERN.match(matter_id):
                continue
            entries.append({"matter_id": matter_id, "name": parts[1], "delivery": parts[2]})
    return entries


def find_yaml_matters() -> list[str]:
    """Find all matter IDs that have a MATTER.yaml under 05_MATTERS/."""
    ids = []
    for folder in DELIVERY_FOLDERS:
        tier_path = MATTERS_ROOT / folder
        if not tier_path.exists():
            continue
        for item in tier_path.iterdir():
            if item.is_dir() and not item.name.startswith("."):
                if (item / "MATTER.yaml").exists():
                    ids.append(item.name)
    return sorted(ids)


def parse_dashboard_count() -> int:
    """Count data rows in DASHBOARDS/MATTER_INDEX.md table."""
    if not DASHBOARD_INDEX_PATH.exists():
        return -1
    count = 0
    in_table = False
    with open(DASHBOARD_INDEX_PATH) as f:
        for line in f:
            line = line.strip()
            if line.startswith("| ---") or line.startswith("|---"):
                in_table = True
                continue
            if in_table and line.startswith("|"):
                count += 1
            elif in_table and not line.startswith("|"):
                break
    return count


def main() -> int:
    verbose = "--verbose" in sys.argv

    print("=" * 60)
    print("Matter Registry Integrity Check")
    print(f"Generated: {datetime.now().isoformat()}")
    print("=" * 60)
    print()

    errors: list[str] = []
    warnings: list[str] = []

    # --- Parse inputs ---
    registry_entries = parse_registry()
    yaml_ids = find_yaml_matters()
    dashboard_count = parse_dashboard_count()

    registry_ids = [e["matter_id"] for e in registry_entries]
    registry_id_set = set(registry_ids)
    yaml_id_set = set(yaml_ids)

    # --- Check 1: Duplicates in MATTER_REGISTRY.md ---
    seen: set[str] = set()
    duplicates: list[str] = []
    for mid in registry_ids:
        if mid in seen:
            duplicates.append(mid)
        seen.add(mid)

    if duplicates:
        for mid in duplicates:
            errors.append(f"DUPLICATE in MATTER_REGISTRY.md: {mid}")
    elif verbose:
        print("PASS: No duplicates in MATTER_REGISTRY.md")

    # --- Check 2: MATTER.yaml folders missing from registry ---
    missing_from_registry = yaml_id_set - registry_id_set
    for mid in sorted(missing_from_registry):
        errors.append(f"MATTER.yaml exists but NOT in registry: {mid}")

    # --- Check 3: Registry entries missing a MATTER.yaml ---
    missing_yaml = registry_id_set - yaml_id_set
    for mid in sorted(missing_yaml):
        errors.append(f"In registry but NO MATTER.yaml folder: {mid}")

    # --- Check 4: Count consistency ---
    yaml_count = len(yaml_ids)
    registry_count = len(registry_entries)

    if yaml_count != registry_count:
        errors.append(
            f"COUNT MISMATCH: {yaml_count} MATTER.yaml dirs vs "
            f"{registry_count} MATTER_REGISTRY.md rows"
        )
    elif verbose:
        print(f"PASS: Counts match ({yaml_count} matters)")

    if dashboard_count >= 0 and dashboard_count != yaml_count:
        warnings.append(
            f"DASHBOARD COUNT: {dashboard_count} rows in MATTER_INDEX.md "
            f"vs {yaml_count} MATTER.yaml dirs (may be stale snapshot)"
        )

    # --- Report ---
    print(f"MATTER.yaml dirs:         {yaml_count}")
    print(f"MATTER_REGISTRY.md rows:  {registry_count}")
    print(f"DASHBOARDS/MATTER_INDEX:  {dashboard_count if dashboard_count >= 0 else 'not found'}")
    print()

    if errors:
        print("ERRORS")
        print("-" * 40)
        for e in errors:
            print(f"  ERROR: {e}")
        print()

    if warnings:
        print("WARNINGS")
        print("-" * 40)
        for w in warnings:
            print(f"  WARN:  {w}")
        print()

    if not errors and not warnings:
        print("All registry checks passed.")
        print()

    print("=" * 60)
    if errors:
        print("STATUS: FAIL")
        return 1
    else:
        print("STATUS: PASS")
        return 0


if __name__ == "__main__":
    sys.exit(main())
