"""Reset personal progress so a forked copy starts clean.

Usage:
    uv run python scripts/fresh_start.py --name "Your Name"

What it does (idempotent):
- PLAN.md     — untick every checkbox, reset roadmap Status cells, put your name
                and the current month on the Owner line
- PROGRESS.md — replace with an empty log
- notes/      — delete all notes (they're the previous owner's reflections)

Course content — exercises, solutions, tests, docs/ — is left untouched.

Safety: it preflights all inputs before mutating, computes every new file before
writing any, and writes atomically. Everything it touches is tracked by git, so
`git checkout -- .` undoes a reset (including deleted notes) — which is also why
note deletion needs no staged-rollback machinery of its own. Review with
`git diff`, then commit.
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

FRESH_PROGRESS = """\
# Progress log

One row per session. Newest at the bottom.

| Date | What I did | Time | Notes / blockers |
| ---- | ---------- | ---- | ---------------- |
"""


def untick(text: str) -> str:
    """Reset '- [x]' list checkboxes to '- [ ]' (any indentation, x or X)."""
    return re.sub(r"^(\s*- )\[[xX]\]", r"\1[ ]", text, flags=re.MULTILINE)


def reset_status(text: str) -> str:
    """Reset roadmap Status cells to unchecked — only the last cell of table rows."""
    def reset_line(line: str) -> str:
        stripped = line.rstrip()
        if not stripped.lstrip().startswith("|") or not stripped.endswith("|"):
            return line
        head, _, status_cell = stripped[:-1].rpartition("|")
        for state in ("⏳ in progress", "✅ done"):
            status_cell = status_cell.replace(state, "☐")
        return f"{head}|{status_cell}|"

    return "\n".join(reset_line(line) for line in text.split("\n"))


def set_owner(text: str, name: str, started: str) -> str:
    """Rewrite the '**Owner:** … **Started:** …' line for the new owner.

    Raises ValueError if the plan doesn't contain exactly one Owner line, so a
    reshaped PLAN.md fails loudly instead of silently keeping the old owner.
    """
    new_text, n = re.subn(
        r"^\*\*Owner:\*\*.*$",
        lambda _: f"**Owner:** {name} · **Started:** {started}",
        text,
        flags=re.MULTILINE,
    )
    if n != 1:
        raise ValueError(
            f"expected exactly one '**Owner:**' line in PLAN.md, found {n} — was it reformatted?"
        )
    return new_text


def wipe_notes(notes_dir: Path) -> list[str]:
    """Delete all markdown notes; keep the directory (and .gitkeep)."""
    removed = []
    for f in sorted(notes_dir.glob("*.md")):
        f.unlink()
        removed.append(f.name)
    return removed


def _atomic_write(path: Path, text: str) -> None:
    """Write via a temp file + rename so a crash never leaves a half-written file."""
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(text, encoding="utf-8")
    tmp.replace(path)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Reset personal progress after forking the course repo."
    )
    parser.add_argument(
        "--name", required=True, help="your name for PLAN.md's Owner line"
    )
    args = parser.parse_args()
    if not args.name.strip():
        parser.error("--name must not be blank")

    plan, progress, notes = ROOT / "PLAN.md", ROOT / "PROGRESS.md", ROOT / "notes"
    for required in (plan, progress, notes):
        if not required.exists():
            sys.exit(f"error: {required} not found — run from a full course checkout")

    started = datetime.now().strftime("%B %Y")
    try:
        new_plan = set_owner(
            reset_status(untick(plan.read_text(encoding="utf-8"))), args.name, started
        )
    except ValueError as e:
        sys.exit(f"error: {e}")

    _atomic_write(plan, new_plan)
    print(f"PLAN.md      — checkboxes unticked, statuses reset, owner → {args.name}")

    _atomic_write(progress, FRESH_PROGRESS)
    print("PROGRESS.md  — emptied")

    removed = wipe_notes(notes)
    print(f"notes/       — removed {len(removed)} file(s): {', '.join(removed) or 'none'}")

    print("\nFresh start ready. Two follow-ups:")
    print("  1. Edit PLAN.md's **Goal:** line to describe your own starting point")
    print('  2. Review with `git diff`, then: git add -A && git commit -m "Fresh start"')


if __name__ == "__main__":
    main()
