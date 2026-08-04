# Feature: Fold Grok critique adoptions into the plan

**Branch:** main
**Date:** 2026-08-04

## Summary

Adopts six suggestions from an external Grok review of the course plan
(`docs/grok-share-critique-export.md`) into `PLAN.md`, without changing the plan's
structure or the 45–60 min/day budget.

## Motivation

Grok's critique flagged real gaps: no numerical linear algebra, no retention
mechanism over an 8+ month timeline, a cliff into Itô calculus, and capstones with
no out-of-sample discipline. The suggestions that fit the plan's constraints were
folded in; the rest (pre-slowed pacing, interview track, ODE module, bi-weekly
review buffers) were deliberately rejected — pacing is handled by the monthly
expansion ritual, not upfront pessimism.

## What changed

- New **Session habits** section: 5-min spaced review to open each session (+
  `notes/formula-sheet.md`), weekly explain-it-out-loud recording, pacing-is-provisional
  note
- Months 2–3 skeleton: numerical LA (LU/QR, conditioning, stable least-squares) and
  real-data hygiene (yfinance/CCXT, cleaning, log-returns) on the PCA project
- Months 5–6 skeleton: bridge week (random walks → martingales → Brownian motion sim)
  before the fork
- Quant capstone: transaction costs + walk-forward validation; AI capstone:
  train/val/test splits + scikit-learn baseline
- Reference shelf: Ernie Chan's *Quantitative Trading*
- Grok's exported critique committed at `docs/grok-share-critique-export.md`

## Notes

Rejected and deferred suggestions, with reasons, are recorded in the session summary
for this date.
