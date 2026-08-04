# Quant & AI Maths Course

Rebuilding maths from A-level up to working quant-trading / AI-ML level. Code-first:
every concept gets implemented in Python/NumPy. ~45–60 min daily.

**The master plan lives in [PLAN.md](PLAN.md).** Sessions get logged in
[PROGRESS.md](PROGRESS.md). The original course-plan PDF is archived in
[docs/](docs/).

## Layout

```
PLAN.md          master plan — Month 1 detailed, Months 2+ expanded as I reach them
PROGRESS.md      one row per study session
exercises/       weekly exercise sets (week-01/, week-02/, …)
  week-NN/solutions/   spoilers — only open after attempting
projects/        bigger builds (PCA on returns, autodiff engine, backtest, …)
notes/           monthly reflections (month-01.md, …)
```

## Setup

```sh
uv sync                                        # install env (numpy, matplotlib, jupyterlab)
uv run jupyter lab                             # notebooks
uv run python exercises/week-01/bisection.py   # run an exercise's self-checks
```

## Working rhythm

1. Open this week's `exercises/week-NN/README.md` and work through it.
2. Exercises are skeletons with self-checks — make the checks pass, peek at
   `solutions/` only afterwards.
3. Append a row to `PROGRESS.md` each session.
4. At each month boundary, ask Claude Code to expand the next month in `PLAN.md`
   (prompts are at the bottom of PLAN.md).

## Fork your own run

The course is reusable. Personal state lives only in `PLAN.md` (its checkboxes,
roadmap statuses, and the Owner/Goal lines), `PROGRESS.md`, and `notes/` —
everything else is course content. To start your own:

1. Fork this repo, then `uv sync`.
2. `uv run python scripts/fresh_start.py --name "Your Name"` — unticks the plan,
   resets the roadmap statuses and Owner line, and empties the progress log and
   notes. Exercises, solutions, and tests stay. (Reword PLAN.md's **Goal:** line
   yourself — it should describe *your* starting point.)
3. Commit it: `git add -A && git commit -m "Fresh start"`.
4. Track your progress with PRs **in your fork**: `git checkout -b week-01`, work,
   push, open the PR *with your fork as the base* (GitHub defaults the base to this
   upstream repo — switch it), and merge when the week's checkpoint passes. The PR
   template has the weekly checklist.

PRs to this repo are welcome for course improvements — better exercises, plan fixes,
clearer solutions. Personal progress belongs in your fork.
