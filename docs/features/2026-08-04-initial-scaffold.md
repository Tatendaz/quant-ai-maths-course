# Feature: Initial course scaffold

**Branch:** main (initial commit)
**Date:** 2026-08-04

## Summary

Turns the "Quant & AI Maths — Living Course Plan" PDF into a working repo: the plan as
markdown, a Python env, and a ready-to-start Week 1 exercise set.

## Motivation

The course plan PDF describes exactly this layout (`PLAN.md`, `exercises/week-NN/`,
`projects/`, `notes/`) and a code-first method that needs NumPy/Matplotlib/Jupyter on
tap. This commit sets all of that up so study time goes to maths, not tooling.

## What changed

- `PLAN.md` — full markdown conversion of the PDF (roadmap, detailed Month 1, skeleton
  Months 2+, reference shelf, future-session prompts)
- `PROGRESS.md` — session log, split out of the plan so plan diffs stay clean
- `exercises/week-01/` — Week 1 README with diagnostic + 10-problem checkpoint,
  `bisection.py` and `plot_functions.py` skeletons with self-checks, worked solutions
  in `solutions/` (spoiler-guarded)
- `tests/` — pytest suite over the Week 1 reference solution
- uv-managed env: numpy, matplotlib, jupyterlab (+ pytest as dev dep)
- Original PDF archived at `docs/quant-ai-maths-course-original.pdf`

## Notes

Exercise skeletons (`exercises/week-NN/*.py`) intentionally raise `NotImplementedError`
— they are the learner's workout, not shipped code. Tests cover the reference
solutions instead.
