"""Tests for the Week 1 reference solutions (run with: uv run pytest)."""

import math
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent / "exercises" / "week-01" / "solutions"))

from bisection_solution import bisection_solve


def test_sqrt2():
    assert bisection_solve(lambda x: x**2 - 2, 0, 2) == pytest.approx(math.sqrt(2), abs=1e-8)


def test_cos_root():
    assert bisection_solve(math.cos, 0, 3) == pytest.approx(math.pi / 2, abs=1e-8)


def test_log_root():
    assert bisection_solve(lambda x: math.log(x) - 1, 1, 5) == pytest.approx(math.e, abs=1e-8)


def test_endpoint_root():
    assert bisection_solve(lambda x: x, 0, 1) == 0


def test_non_bracketing_interval_raises():
    with pytest.raises(ValueError):
        bisection_solve(lambda x: x**2 + 1, -1, 1)
