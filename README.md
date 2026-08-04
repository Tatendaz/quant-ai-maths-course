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
