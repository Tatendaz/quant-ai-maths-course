# Security routine 2026-11-19

**Branch:** security/routine-2026-11-19
**Date:** 2026-11-19

## Steps taken
- `osv-scanner` and `pip-audit` on `uv.lock`: tornado 6.5.9 has four advisories. One of them, GHSA-5cjw-f85j-cv6r (CVE-2026-126347, open redirect via triple-slash paths, published 2026-11-13), is only fixed in 6.6.1.
- Bumped tornado to 6.6.1 (published 2026-11-09) with `uv lock --upgrade-package tornado==6.6.1`, using uv 0.13.7 so the lockfile format stays the same.
- `uv run pytest`: 14 passed.

## Decisions
- This replaces PR #5, which stops at 6.6 and misses the newer advisory.
- soupsieve is left to PR #7.
