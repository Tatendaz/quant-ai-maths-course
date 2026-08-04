# Week 1 checkpoint — worked solutions

**1.** `3x² − 5x − 2 = 0` factors as `(3x + 1)(x − 2) = 0`, so **x = −1/3 or x = 2**.
(Or the quadratic formula: x = (5 ± √(25 + 24))/6 = (5 ± 7)/6.)

**2.** `x² − 4x + 3 = (x − 1)(x − 3)`. A upward parabola is negative *between* its
roots, so **1 < x < 3**.

**3.** `log₂ 48 − log₂ 3 = log₂ (48/3) = log₂ 16 = **4**`.

**4.** Take ln of both sides: `(3x − 1) ln 2 = ln 5`, so
`x = (1 + ln 5 / ln 2) / 3` — exact. Numerically `ln 5/ln 2 ≈ 2.322`, so
**x ≈ 1.11** (3 s.f.).

**5.** `ln x + ln(x−1) = ln[x(x−1)] = ln 6` → `x² − x − 6 = 0` → `(x − 3)(x + 2) = 0`.
The domain needs `x > 1` (both logs defined), so **x = 3** only.

**6.** `y = 3·f(x − 1) + 4`: **shift right 1**, then **stretch vertically ×3**, then
**shift up 4**. (The stretch must come before the +4: the 4 is added *after*
multiplying by 3.)

**7.** Set equal: `x² − 2x = 2x − 3` → `x² − 4x + 3 = 0` → `x = 1 or 3`. Substitute
back: **(1, −1) and (3, 3)**.

**8.** Let `u = e^x`: `u² − 5u + 6 = (u − 2)(u − 3) = 0` → `u = 2 or 3`, so
**x = ln 2 or x = ln 3**. (Both valid — u is positive in each case.)

**9.** `log_a (a·b²/c) = log_a a + 2 log_a b − log_a c = 1 + 2·3 − 2 = **5**`.

**10.** Half-life: `e^(−12k) = ½` → **k = ln 2 / 12 ≈ 0.0578 per hour**.
For 10%: `e^(−kt) = 0.1` → `t = ln 10 / k = 12·ln 10 / ln 2 ≈ **39.9 hours**`.
(Neat check: 0.1 ≈ 2^(−3.32), so ~3.32 half-lives ≈ 3.32 × 12 h.)
