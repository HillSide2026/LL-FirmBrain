---
id: 04_initiatives_ll_portfolio_08_marketing_04_website_website_backlog_md
title: Website Backlog
owner: ML1
status: draft
created_date: 2026-05-18
last_updated: 2026-05-18
tags: []
---

# Website Backlog

## 1. Confirm Browser-Level Thrive Access Before Any Further Live Thrive Editing
- Problem: browser-valid Thrive editing access is not yet a clean, confirmed working path for Codex, even though WordPress credentials exist in `.env`.
- Why it matters: Thrive-built pages cannot be treated like ordinary REST-editable WordPress pages. Before any live copy work, the editing path itself needs to be proven end-to-end in the real visual editor.
- Current known blocker: the browser login attempt using `WP_ADMIN_USERNAME` and `WP_ADMIN_PASSWORD` failed in WordPress, so the Thrive editor load path is not yet verified.
- Initial action direction: before any further live Thrive copy edits, require:
  1. confirmed browser-valid wp-admin credentials,
  2. browser-level editing access (local Playwright or equivalent GUI control),
  3. screenshot-first verification of login, dashboard load, and Thrive load,
  4. a duplicate/staging or rollback checkpoint before text changes,
  5. no production edits through REST-only fallback paths.
- Test page:
  - `https://levinelegal.ca/apprentice-registration-page/`
- Key refs:
  - `.env`
  - `screenshots/01-login-page.png`
  - `screenshots/99-error.png`
  - `scripts/wp_post_draft.py`
