#!/usr/bin/env python3
"""
validate_matter_yaml.py — Matter Schema Validation

Scans 05_MATTERS/ and validates each matter against the schema defined in
00_SYSTEM/schemas/SCHEMAS.md.

Usage:
    python scripts/validate_matter_yaml.py [--fix-missing] [--verbose]

Options:
    --fix-missing   Create missing MATTER.yaml files with placeholder values
    --verbose       Show details for passing matters too

Exit codes:
    0 = All matters valid
    1 = Validation errors found
"""

import os
import sys
import yaml
from pathlib import Path
from datetime import datetime

# Schema definition per 00_SYSTEM/schemas/SCHEMAS.md
REQUIRED_FIELDS = {
    'matter_id': str,
    'matter_name': str,
    'status': str,
    'delivery_status': str,
    'fulfillment_status': str,
    'created_date': str,
}

STATUS_VALUES = ['Open', 'Pending', 'Closed']
DELIVERY_STATUS_VALUES = ['Essential', 'Strategic', 'Standard', 'normal', 'Parked']
FULFILLMENT_STATUS_VALUES = ['urgent', 'active', 'closing', 'keep in view', 'inactive']
SERVICE_TYPE_VALUES = ['solution', 'strategy']
LEGACY_SERVICE_FIELDS = {'solutions': 'solution', 'strategies': 'strategy'}

MATTERS_ROOT = Path(__file__).parent.parent / '05_MATTERS'


def normalize_token(value: str) -> str:
    return str(value or '').strip().lower()


def validate_services(data: dict, result: dict):
    """Validate canonical services model and legacy aliases."""
    services = data.get('services')
    if services is not None and not isinstance(services, list):
        result['valid'] = False
        result['errors'].append("services must be a list when present")
        services = []

    normalized_services = 0
    if isinstance(services, list):
        for idx, entry in enumerate(services):
            if isinstance(entry, str):
                if not entry.strip():
                    result['warnings'].append(f"services[{idx}] is empty string")
                else:
                    result['warnings'].append(
                        f"services[{idx}] is shorthand string; use object with service_type/service_name"
                    )
                    normalized_services += 1
                continue

            if not isinstance(entry, dict):
                result['valid'] = False
                result['errors'].append(f"services[{idx}] must be a map or string")
                continue

            service_type = str(entry.get('service_type') or entry.get('type') or '').strip().lower()
            service_name = str(entry.get('service_name') or entry.get('name') or '').strip()
            if not service_type:
                result['valid'] = False
                result['errors'].append(f"services[{idx}].service_type is required")
            elif service_type not in SERVICE_TYPE_VALUES:
                result['valid'] = False
                result['errors'].append(
                    f"services[{idx}].service_type '{service_type}' not in {SERVICE_TYPE_VALUES}"
                )

            if not service_name:
                result['valid'] = False
                result['errors'].append(f"services[{idx}].service_name is required")
            else:
                normalized_services += 1

    legacy_count = 0
    for field_name, forced_type in LEGACY_SERVICE_FIELDS.items():
        raw = data.get(field_name)
        if raw is None:
            continue
        if not isinstance(raw, list):
            result['valid'] = False
            result['errors'].append(f"{field_name} must be a list when present")
            continue

        legacy_count += len(raw)
        for idx, entry in enumerate(raw):
            if isinstance(entry, str):
                if not entry.strip():
                    result['warnings'].append(f"{field_name}[{idx}] is empty string")
                continue
            if not isinstance(entry, dict):
                result['valid'] = False
                result['errors'].append(f"{field_name}[{idx}] must be a map or string")
                continue
            service_name = str(entry.get('service_name') or entry.get('name') or '').strip()
            if not service_name:
                result['valid'] = False
                result['errors'].append(f"{field_name}[{idx}] missing service_name/name")
            service_type = str(entry.get('service_type') or entry.get('type') or forced_type).strip().lower()
            if service_type != forced_type:
                result['warnings'].append(
                    f"{field_name}[{idx}] service_type '{service_type}' normalized to '{forced_type}'"
                )

    if legacy_count and services is None:
        result['warnings'].append("Legacy service fields present without canonical services field")

    status = normalize_token(data.get('status', ''))
    delivery_status = normalize_token(data.get('delivery_status', ''))
    fulfillment_status = normalize_token(data.get('fulfillment_status', ''))
    is_delivery_active = (
        status in {'open', 'pending'}
        and delivery_status in {'essential', 'strategic', 'standard'}
        and fulfillment_status in {'urgent', 'active'}
    )

    service_total = normalized_services + legacy_count
    if is_delivery_active and service_total == 0:
        result['warnings'].append("ML Active matter has no services defined")


def validate_matter(matter_path: Path) -> dict:
    """Validate a single matter directory."""
    result = {
        'path': str(matter_path),
        'matter_id': matter_path.name,
        'valid': True,
        'errors': [],
        'warnings': [],
    }

    yaml_path = matter_path / 'MATTER.yaml'
    readme_path = matter_path / 'README.md'

    # Check MATTER.yaml exists
    if not yaml_path.exists():
        result['valid'] = False
        result['errors'].append('Missing MATTER.yaml')
        if readme_path.exists():
            result['warnings'].append('Has README.md but no MATTER.yaml')
        return result

    # Parse YAML
    try:
        with open(yaml_path, 'r') as f:
            data = yaml.safe_load(f)
    except yaml.YAMLError as e:
        result['valid'] = False
        result['errors'].append(f'Invalid YAML: {e}')
        return result

    if data is None:
        result['valid'] = False
        result['errors'].append('Empty MATTER.yaml')
        return result

    # Check required fields
    for field, field_type in REQUIRED_FIELDS.items():
        if field not in data:
            result['valid'] = False
            result['errors'].append(f'Missing required field: {field}')
        elif not isinstance(data[field], field_type):
            result['valid'] = False
            result['errors'].append(f'Invalid type for {field}: expected {field_type.__name__}')

    # Validate enum values
    if 'status' in data and data['status'] not in STATUS_VALUES:
        result['warnings'].append(f"status '{data['status']}' not in standard values: {STATUS_VALUES}")

    if 'delivery_status' in data and data['delivery_status'] not in DELIVERY_STATUS_VALUES:
        result['valid'] = False
        result['errors'].append(f"delivery_status '{data['delivery_status']}' not in: {DELIVERY_STATUS_VALUES}")

    if 'fulfillment_status' in data and data['fulfillment_status'] not in FULFILLMENT_STATUS_VALUES:
        result['warnings'].append(f"fulfillment_status '{data['fulfillment_status']}' not standard: {FULFILLMENT_STATUS_VALUES}")

    # Check folder placement matches delivery_status
    if 'delivery_status' in data:
        expected_folder = data['delivery_status'].upper()
        actual_folder = matter_path.parent.name
        if expected_folder != actual_folder:
            result['valid'] = False
            result['errors'].append(f"Folder mismatch: delivery_status='{data['delivery_status']}' but in {actual_folder}/")

    # Check matter_id matches folder name
    if 'matter_id' in data and data['matter_id'] != matter_path.name:
        result['warnings'].append(f"matter_id '{data['matter_id']}' != folder name '{matter_path.name}'")

    validate_services(data, result)

    return result


def find_all_matters() -> list:
    """Find all matter directories."""
    matters = []
    for delivery_folder in ['ESSENTIAL', 'STRATEGIC', 'STANDARD', 'NORMAL', 'PARKED']:
        folder = MATTERS_ROOT / delivery_folder
        if folder.exists():
            for item in folder.iterdir():
                if item.is_dir() and not item.name.startswith('.'):
                    matters.append(item)
    return sorted(matters)


def create_placeholder_yaml(matter_path: Path, delivery_status: str):
    """Create a placeholder MATTER.yaml file."""
    yaml_path = matter_path / 'MATTER.yaml'

    # Try to extract name from README.md
    readme_path = matter_path / 'README.md'
    matter_name = matter_path.name
    if readme_path.exists():
        with open(readme_path, 'r') as f:
            first_line = f.readline().strip()
            if first_line.startswith('# '):
                matter_name = first_line[2:]

    # Determine year from matter_id
    year_prefix = matter_path.name[:2]
    if year_prefix.isdigit():
        year = f"20{year_prefix}"
    else:
        year = "2025"

    data = {
        'matter_id': matter_path.name,
        'matter_name': matter_name,
        'status': 'Open',
        'delivery_status': delivery_status.capitalize(),
        'fulfillment_status': 'active' if delivery_status != 'PARKED' else 'inactive',
        'created_date': f'{year}-01-01',
    }

    with open(yaml_path, 'w') as f:
        yaml.dump(data, f, default_flow_style=False, sort_keys=False)

    return yaml_path


def main():
    verbose = '--verbose' in sys.argv
    fix_missing = '--fix-missing' in sys.argv

    print("=" * 60)
    print("MATTER.yaml Validation Report")
    print(f"Generated: {datetime.now().isoformat()}")
    print("=" * 60)
    print()

    matters = find_all_matters()
    print(f"Found {len(matters)} matter directories\n")

    results = []
    for matter in matters:
        result = validate_matter(matter)
        results.append(result)

    # Summary counts
    valid_count = sum(1 for r in results if r['valid'])
    invalid_count = len(results) - valid_count
    missing_yaml = sum(1 for r in results if 'Missing MATTER.yaml' in r['errors'])

    # Print errors
    print("VALIDATION ERRORS")
    print("-" * 40)
    error_results = [r for r in results if not r['valid']]
    if error_results:
        for r in error_results:
            print(f"\n{r['matter_id']} ({r['path']})")
            for err in r['errors']:
                print(f"  ERROR: {err}")
            for warn in r['warnings']:
                print(f"  WARN:  {warn}")

            # Fix missing if requested
            if fix_missing and 'Missing MATTER.yaml' in r['errors']:
                delivery = Path(r['path']).parent.name
                created = create_placeholder_yaml(Path(r['path']), delivery)
                print(f"  FIXED: Created {created}")
    else:
        print("None")

    # Print warnings for valid matters
    print("\n\nWARNINGS (valid matters)")
    print("-" * 40)
    warning_results = [r for r in results if r['valid'] and r['warnings']]
    if warning_results:
        for r in warning_results:
            print(f"\n{r['matter_id']}")
            for warn in r['warnings']:
                print(f"  WARN: {warn}")
    else:
        print("None")

    # Verbose: show passing
    if verbose:
        print("\n\nPASSING MATTERS")
        print("-" * 40)
        for r in results:
            if r['valid'] and not r['warnings']:
                print(f"  OK: {r['matter_id']}")

    # Summary
    print("\n")
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Total matters:    {len(results)}")
    print(f"Valid:            {valid_count}")
    print(f"Invalid:          {invalid_count}")
    print(f"Missing YAML:     {missing_yaml}")
    print()

    if invalid_count > 0:
        print("STATUS: FAIL")
        return 1
    else:
        print("STATUS: PASS")
        return 0


if __name__ == '__main__':
    sys.exit(main())
