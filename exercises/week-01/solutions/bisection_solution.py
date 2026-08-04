"""Reference implementation for the Week 1 bisection exercise (spoiler)."""


def bisection_solve(f, a, b, tol=1e-10, max_iter=200):
    """Return x in [a, b] with f(x) ≈ 0, given f(a) and f(b) have opposite signs."""
    fa, fb = f(a), f(b)
    if fa == 0:
        return a
    if fb == 0:
        return b
    if fa * fb > 0:
        raise ValueError(f"f(a) and f(b) must have opposite signs: f({a})={fa}, f({b})={fb}")

    for _ in range(max_iter):
        mid = (a + b) / 2
        fmid = f(mid)
        if fmid == 0 or (b - a) / 2 < tol:
            return mid
        if fa * fmid < 0:
            b = mid
        else:
            a, fa = mid, fmid
    return (a + b) / 2
