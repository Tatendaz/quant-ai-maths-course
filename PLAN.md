# Quant & AI Maths — Living Course Plan

**Owner:** Tatenda · **Started:** August 2026
**Goal:** Rebuild maths from A-level (last touched ~16 years ago) to a working level for quantitative trading and AI/ML.
**Method:** Code-first — every concept gets implemented in Python/NumPy. Target ~45–60 min daily; consistency beats binges.

> **How to use this file with Claude Code:** This is the master plan. Month 1 is fully
> detailed; Months 2+ are skeletons. At the start of each month, ask Claude Code to read
> this file plus the Progress Log ([PROGRESS.md](PROGRESS.md)) and expand the next month
> to the same detail as Month 1. Tick checkboxes as you go. Keep code in
> `exercises/week-NN/`, bigger builds in `projects/`, reflections in `notes/`.

## Full roadmap (skeleton)

| Phase | Months | Topic                                                      | Status         |
| ----- | ------ | ---------------------------------------------------------- | -------------- |
| 0     | 1      | A-level refresh + tooling                                  | ⏳ in progress |
| 1     | 2–3    | Linear algebra                                             | ☐              |
| 2     | 4      | Multivariable calculus + optimization                      | ☐              |
| 3     | 5–6    | Probability                                                | ☐              |
| 4     | 7      | Statistics                                                 | ☐              |
| 5a    | 8+     | Quant fork: time series, stochastic processes, Monte Carlo | ☐              |
| 5b    | 8+     | AI fork: matrix calculus, information theory, convex optimization | ☐       |

Phases 5a/5b can run in parallel or one after the other — decide when you get there.

## Session habits

- **First 5 minutes: spaced review.** Re-derive one item from an earlier week's
  checkpoint (rotate through them). As you finish each week, add its key formulas to
  `notes/formula-sheet.md` — or an Anki deck if that sticks better.
- **Weekly, ~5 min: explain it out loud.** Record yourself explaining the week's
  hardest concept from memory; gaps surface the moment you have to narrate.
- **Pacing is provisional.** Month boundaries flex: the diagnostic score and
  `notes/month-NN.md` drive each month's expansion. Stretching a month is normal,
  not failure.

---

## Month 1 — A-level refresh + tooling (detailed)

**Goal:** shake off the rust on algebra, functions, trig, and calculus, and set up the
coding workflow that carries the whole course.

**Daily shape:** ~30 min lessons + pen-and-paper problems, ~20 min implementing the
day's idea in code.

### Week 1 — Algebra, functions & setup

- [x] Set up the repo, Python env, Jupyter, NumPy + Matplotlib
- [x] Take a diagnostic: Math Academy placement, or Khan Academy "course challenge" for
      Algebra II — record the result in the Progress Log
- [ ] Refresh: solving equations and inequalities, exponentials & logarithms, function
      transformations
- [ ] **Code:** plot function families (polynomials, exp, log); write a
      `bisection_solve(f, a, b)` root-finder
- [ ] **Checkpoint:** solve 10 mixed algebra/log problems without notes

### Week 2 — Trig, sequences & series

- [ ] Refresh: radians, sin/cos/tan, the key identities
- [ ] Refresh: arithmetic & geometric sequences and series, sum formulas
- [ ] **Code:** compound interest and discounted cash flow via geometric series (first
      finance link); Taylor-approximate sin(x) and plot it against the true curve
- [ ] **Checkpoint:** derive and code the geometric series sum; explain why it converges
      when |r| < 1

### Week 3 — Differentiation

- [ ] Refresh: the limit idea, derivative rules, chain/product/quotient rules
- [ ] Refresh: stationary points, max/min word problems
- [ ] **Code:** finite-difference numerical derivative; 1-D gradient descent to find a
      function's minimum (first ML link)
- [ ] **Checkpoint:** hand-differentiate 8 functions and verify each one numerically in
      code

### Week 4 — Integration + first probability

- [ ] Refresh: integration as antiderivative and as area; definite integrals
- [ ] Intro: sample spaces, expected value (A-level stats territory)
- [ ] **Code (mini-project):** Monte Carlo integration — estimate π by random sampling,
      then integrate an arbitrary f(x); plot error vs. sample count (first quant link)
- [ ] **Checkpoint / Month-1 milestone:** write `notes/month-01.md` — what came back
      easily, what didn't, and how the daily rhythm felt

### Month 1 resources

- **Khan Academy** (free): Algebra II, Trigonometry, AP Calculus AB units 1–6
- **Math Academy** (paid, adaptive): Mathematical Foundations sequence — strong option
  if you want the placement test to drive everything
- **3Blue1Brown** — *Essence of Calculus*, watch alongside Weeks 3–4

---

## Months 2+ (skeletons — expand with Claude Code)

### Months 2–3 — Linear algebra

Vectors, matrices, linear maps, eigenvalues/eigenvectors, SVD — plus the numerical
side: LU/QR factorizations, conditioning, and solving least-squares stably (used more
day-to-day than eigenvalue theory). Anchors: 3Blue1Brown *Essence of Linear Algebra*,
MIT 18.06 (Strang), *Mathematics for Machine Learning* ch. 2–4. Projects: matrix ops
from scratch, then PCA on real stock or crypto returns — fetch (yfinance/CCXT), clean,
and compute log-returns yourself; every later project uses real data.

### Month 4 — Multivariable calculus & optimization

Partial derivatives, gradients, Jacobians, chain rule, Lagrange multipliers, gradient
descent variants. Projects: 2-D gradient descent visualizer; a tiny autodiff engine.

### Months 5–6 — Probability

Distributions, conditional probability, Bayes, law of large numbers, CLT. Anchor:
Blitzstein's Stat 110 (free lectures + book). Projects: simulate the CLT; a Bayesian
A/B test. End with a bridge week — random walks → discrete-time martingales → simulate
Brownian motion — so the quant fork's Itô material doesn't arrive cold.

### Month 7 — Statistics

Regression from scratch (OLS via your linear algebra), hypothesis testing, maximum
likelihood. Project: OLS with diagnostics on market data.

### Months 8+ — The fork

- **Quant:** time series (stationarity, ARIMA, GARCH, cointegration), random walks &
  Brownian motion, a taste of Itô, Monte Carlo pricing. **Capstone:** pairs-trading
  backtest — crypto data is an easy, familiar sandbox — with transaction costs and
  walk-forward validation, not just an in-sample fit.
- **AI:** matrix calculus, information theory (entropy, KL divergence, cross-entropy),
  convex optimization. **Capstone:** a NumPy-only neural net trained end-to-end on a
  small dataset, with proper train/val/test splits and a scikit-learn baseline to beat.

---

## Reference shelf

- *Mathematics for Machine Learning* — Deisenroth, Faisal, Ong (free PDF)
- *Introduction to Probability* — Blitzstein & Hwang
- *Introduction to Linear Algebra* — Strang
- Quant side, for later: *Paul Wilmott Introduces Quantitative Finance*; Ernie Chan's
  *Quantitative Trading* (practical strategy framing); Zhou's *A Practical Guide to
  Quantitative Finance Interviews* (the "green book")

## Progress log

Lives in [PROGRESS.md](PROGRESS.md) — append a row per session.

## Prompts for future Claude Code sessions

- "Read PLAN.md and the Progress Log; expand Month 2 into a week-by-week plan at the
  same detail as Month 1."
- "Generate this week's exercise set into `exercises/week-NN/`, with solutions in a
  separate file I can't see by accident."
- "Quiz me on last week's checkpoints before unlocking this week."
- "Review my `notes/month-NN.md` and adjust next month's pacing accordingly."
