"""Week 1 — bisection root-finder.

Implement bisection_solve so every check at the bottom passes:

    uv run python exercises/week-01/bisection.py

The idea: if f is continuous and f(a), f(b) have opposite signs, a root lies
between them. Evaluate f at the midpoint, keep the half that still brackets the
sign change, repeat until the interval is smaller than tol.
"""


def bisection_solve(f, a, b, tol=1e-10, max_iter=200):
    """Return x in [a, b] with f(x) ≈ 0, given f(a) and f(b) have opposite signs.

    Raise ValueError if f(a) and f(b) have the same sign.
    """
    # TODO: implement me
    raise NotImplementedError


if __name__ == "__main__":
    import math

    root = bisection_solve(lambda x: x**2 - 2, 0, 2)
    assert abs(root - math.sqrt(2)) < 1e-6, f"√2 check failed: {root}"

    root = bisection_solve(math.cos, 0, 3)
    assert abs(root - math.pi / 2) < 1e-6, f"cos check failed: {root}"

    root = bisection_solve(lambda x: math.log(x) - 1, 1, 5)
    assert abs(root - math.e) < 1e-6, f"log check failed: {root}"

    try:
        bisection_solve(lambda x: x**2 + 1, -1, 1)  # no root — same sign at both ends
        raise AssertionError("expected ValueError for a non-bracketing interval")
    except ValueError:
        pass

    print("all checks passed ✔")
