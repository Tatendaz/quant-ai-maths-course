# Session: Fork support

**Branch:** main
**Date:** 2026-08-04

## Prompts

1. "Can you make it such that when someone forks this repo they dont use my progress
   and they can create PRs and merge in their own progress."

## Steps taken

- Wrote `scripts/fresh_start.py` (untick/reset/set-owner/wipe-notes as pure,
  testable functions + CLI) and `tests/test_fresh_start.py`
- Verified end-to-end on a scratchpad copy of the repo (0 boxes left ticked,
  statuses reset, PROGRESS emptied, `.gitkeep` preserved)
- Added README "Fork your own run" section and `.github/PULL_REQUEST_TEMPLATE.md`
- Removed the `(8/30, 2026-08-04)` annotation from PLAN.md to establish the
  "scores live in PROGRESS.md/notes, not PLAN.md" convention

## Decisions

- Reset derives the clean state from the live PLAN.md mechanically instead of
  keeping a second template copy — a template would drift as months get expanded
- Personal-progress PRs merge into the fork (base = fork, called out because GitHub
  defaults PR base to upstream); upstream PRs reserved for course improvements
- `docs/` survives the reset — it's plan history/rationale, not personal progress
- Owner's own workflow unchanged (direct commits to main through the local gate)
