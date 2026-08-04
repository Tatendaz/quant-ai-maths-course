# Week 1 — Algebra, functions & setup

From [PLAN.md](../../PLAN.md) Month 1. Tick things off there as you finish.

## 1. Setup — done ✅

Repo, uv env, Jupyter, NumPy + Matplotlib are installed. Sanity check:

```sh
uv run python -c "import numpy, matplotlib; print('env ok')"
```

## 2. Diagnostic (~30 min)

Take the Khan Academy **Algebra II course challenge**
(khanacademy.org → Algebra 2 → "Course challenge"), or the Math Academy placement if
you'd rather pay for adaptive. Record your score in [PROGRESS.md](../../PROGRESS.md) —
it's the baseline the whole course measures against.

## 3. Refresh topics

Work through (Khan Academy units, any order):

- Solving equations & inequalities (linear, quadratic, rational)
- Exponentials & logarithms — laws of logs, solving `a^x = b`, `ln` vs `log`
- Function transformations — what `3·f(x−1) + 4` does to a graph

## 4. Code exercises

Both files are skeletons with self-checks at the bottom — implement until the checks
pass:

```sh
uv run python exercises/week-01/plot_functions.py   # plot function families
uv run python exercises/week-01/bisection.py        # bisection root-finder
```

Prefer a notebook? `uv run jupyter lab` and build the plots there instead.

## 5. Checkpoint — 10 mixed problems, no notes

Pen and paper, closed book. Answers with worked steps are in
[`solutions/checkpoint-solutions.md`](solutions/checkpoint-solutions.md) — **only open
after attempting all ten.**

1. Solve `3x² − 5x − 2 = 0`.
2. Solve the inequality `x² − 4x + 3 < 0`.
3. Simplify `log₂ 48 − log₂ 3`.
4. Solve `2^(3x−1) = 5`. Give the exact answer using `ln`, then a decimal to 3 s.f.
5. Solve `ln x + ln(x − 1) = ln 6`.
6. Describe the sequence of transformations taking the graph of `y = f(x)` to
   `y = 3·f(x − 1) + 4`.
7. Find the points where the line `y = 2x − 3` meets the parabola `y = x² − 2x`.
8. Solve `e^(2x) − 5e^x + 6 = 0`. (Hint: substitute `u = e^x`.)
9. Given `log_a b = 3` and `log_a c = 2`, evaluate `log_a (a·b² / c)`.
10. A quantity decays as `Q(t) = Q₀·e^(−kt)`. Its half-life is 12 hours. Find `k`,
    then how long until only 10% remains.

**Pass bar:** 8/10 without notes. Below that, spend one more day on the refresh topics
before moving to Week 2.
