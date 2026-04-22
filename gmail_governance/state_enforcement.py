"""
LL Inbox Governance - Phase 1: State Enforcement
Enforces canonical state exclusivity for Gmail threads.
"""

import os
import json
from dotenv import load_dotenv
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

load_dotenv()

# Canonical state labels (immutable)
# Source of truth: POL-042 / PRO-014
CANONICAL_LABELS = {
    "00_Triage",
    "10_Action_Matthew",
    "20_Action_Team",
    "30_Waiting_External",
    "40_Replied_Awaiting_Response",
    "50_Calendar",
    "60_Filing",
    "70_Filed",
    "80_Junk_to_Review",
    "90_Archive"
}

# State labels that imply the thread has exited triage.
# Applying any of these must atomically remove INBOX in the same operation.
# Source of truth: POL-042 §4 / PRO-014 §3
INBOX_EXIT_LABELS = {
    "50_Calendar",
    "60_Filing",
    "70_Filed",
    "90_Archive",
}


def get_gmail_service():
    """
    Initialize Gmail API service using existing OAuth token.
    """
    token_path = os.getenv("GOOGLE_OAUTH_TOKEN_PATH", "config/google_oauth_tokens.json")

    if not os.path.exists(token_path):
        raise FileNotFoundError(
            f"OAuth token not found at {token_path}.\n"
            f"Run: python scripts/google_connect.py"
        )

    with open(token_path, 'r') as f:
        creds_data = json.load(f)

    creds = Credentials.from_authorized_user_info(creds_data)

    if creds.expired and creds.refresh_token:
        creds.refresh(Request())

    return build('gmail', 'v1', credentials=creds)


def get_label_id_map(service):
    """
    Retrieve canonical label name to ID mapping.
    """
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    label_map = {}
    for label in labels:
        if label['name'] in CANONICAL_LABELS:
            label_map[label['name']] = label['id']

    return label_map


def apply_state(thread_id, new_state_label):
    """
    Apply canonical state to thread with exclusivity enforcement.

    Args:
        thread_id: Gmail thread ID
        new_state_label: One of CANONICAL_LABELS

    Returns:
        dict with success, prior_state, new_state, thread_id
    """
    if new_state_label not in CANONICAL_LABELS:
        raise ValueError(f"Label '{new_state_label}' is not a canonical state label")

    service = get_gmail_service()
    label_map = get_label_id_map(service)

    if new_state_label not in label_map:
        raise ValueError(f"Label '{new_state_label}' does not exist in Gmail account")

    # Get thread
    thread = service.users().threads().get(userId='me', id=thread_id).execute()

    # Collect current label IDs
    current_label_ids = set()
    for message in thread.get('messages', []):
        current_label_ids.update(message.get('labelIds', []))

    # Identify canonical labels to remove
    canonical_label_ids_to_remove = []
    prior_state = None
    current_canonical_labels = []

    for label_name, label_id in label_map.items():
        if label_id in current_label_ids:
            canonical_label_ids_to_remove.append(label_id)
            current_canonical_labels.append(label_name)
            prior_state = label_name

    # Idempotency check: if thread already has target label as only canonical label, skip
    if len(current_canonical_labels) == 1 and current_canonical_labels[0] == new_state_label:
        return {
            'success': True,
            'prior_state': new_state_label,
            'new_state': new_state_label,
            'thread_id': thread_id,
            'no_change': True
        }

    # Apply modification
    new_state_label_id = label_map[new_state_label]

    remove_ids = list(canonical_label_ids_to_remove)
    if new_state_label in INBOX_EXIT_LABELS:
        remove_ids.append("INBOX")

    modify_body = {
        'addLabelIds': [new_state_label_id],
        'removeLabelIds': remove_ids
    }

    service.users().threads().modify(
        userId='me',
        id=thread_id,
        body=modify_body
    ).execute()

    return {
        'success': True,
        'prior_state': prior_state,
        'new_state': new_state_label,
        'thread_id': thread_id
    }


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python state_enforcement.py <thread_id> <new_state_label>")
        print(f"Valid labels: {', '.join(sorted(CANONICAL_LABELS))}")
        sys.exit(1)

    thread_id = sys.argv[1]
    new_state = sys.argv[2]

    try:
        result = apply_state(thread_id, new_state)
        print(json.dumps(result, indent=2))
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
