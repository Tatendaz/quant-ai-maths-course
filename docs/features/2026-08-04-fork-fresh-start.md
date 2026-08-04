# Feature: Fork support — fresh-start reset and weekly-PR workflow

**Branch:** main
**Date:** 2026-08-04

## Summary

Lets anyone fork the course without inheriting the owner's progress: a one-command
reset script, a README fork guide, and a PR template for the weekly merge rhythm.

## Motivation

The repo doubles as a reusable course, but PLAN.md checkboxes, PROGRESS.md, and
notes/ carry the owner's personal state. Forkers need a clean slate plus a defined
way to track their own progress (branch per week → PR → merge in their fork).

## What changed

- `scripts/fresh_start.py` — idempotent reset: unticks PLAN.md checkboxes, resets
  roadmap Status cells, rewrites the Owner line (`--name`), empties PROGRESS.md,
  wipes `notes/*.md` (keeps `.gitkeep`); course content untouched
- `tests/test_fresh_start.py` — unit tests for every transformation
- README "Fork your own run" section — fork → `uv sync` → reset → commit → weekly
  branch/PR/merge in the fork (with the base-repo gotcha called out)
- `.github/PULL_REQUEST_TEMPLATE.md` — weekly progress checklist
- Convention change: scores/dates live only in PROGRESS.md and notes/, never as
  annotations in PLAN.md — keeps the reset purely mechanical (removed the one
  existing `(8/30, 2026-08-04)` annotation)

## Notes

Upstream PRs remain for course improvements; personal progress merges into the
fork. The reset script deliberately leaves `docs/` (plan history and rationale).
