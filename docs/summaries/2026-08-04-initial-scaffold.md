# Session: Initial course scaffold

**Branch:** main (initial commit)
**Date:** 2026-08-04

## Prompts

1. "can you help me create a repo and setup /Users/tatendazhou/Downloads/quant-ai-maths-course.pdf so I can start learning"

## Steps taken

- Read the 5-page course-plan PDF; it self-describes the repo layout and method
- `uv init` + added numpy, matplotlib, jupyterlab, pytest (dev)
- Converted the PDF to `PLAN.md`; split the progress log into `PROGRESS.md`
- Generated the Week 1 exercise set: README (diagnostic, refresh topics, 10-problem
  checkpoint), `bisection.py` + `plot_functions.py` skeletons with self-checks,
  worked solutions under `exercises/week-01/solutions/`
- Added pytest suite for the reference solution; archived the original PDF in `docs/`
- Created the GitHub repo (private) and pushed through the pre-push gate

## Decisions

- Repo named `quant-ai-maths-course` (matches the PDF) rather than the PDF's generic
  `maths-course` suggestion
- Private visibility to start — flip with `gh repo edit --visibility public` if
  learning in public later
- Solutions live in a `solutions/` subfolder per week ("can't see by accident"), with
  a spoiler-warning README
- Progress log kept as its own file so `PLAN.md` diffs stay readable month to month
