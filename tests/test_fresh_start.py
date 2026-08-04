"""Tests for the fork reset script (run with: uv run pytest)."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from fresh_start import FRESH_PROGRESS, reset_status, set_owner, untick, wipe_notes


def test_untick_resets_checked_boxes_only():
    text = "- [x] done\n  - [X] nested\n- [ ] todo\nprose with `[x]` inline"
    out = untick(text)
    assert out.count("- [ ]") == 3
    assert "[x]" not in out.split("\n")[0]
    assert "prose with `[x]` inline" in out


def test_reset_status_only_touches_table_rows():
    text = "| 0 | 1 | topic | ⏳ in progress |\n| 1 | 2 | other | ✅ done |\nprose ⏳ in progress stays"
    out = reset_status(text)
    assert "| 0 | 1 | topic | ☐ |" in out
    assert "| 1 | 2 | other | ☐ |" in out
    assert "prose ⏳ in progress stays" in out


def test_reset_status_preserves_states_in_non_status_cells():
    text = "| 5 | 8 | build a '✅ done' tracker | ⏳ in progress |"
    out = reset_status(text)
    assert out == "| 5 | 8 | build a '✅ done' tracker | ☐ |"


def test_set_owner_replaces_owner_line():
    text = "# Title\n\n**Owner:** Tatenda · **Started:** August 2026\n**Goal:** x"
    out = set_owner(text, "Ada", "September 2026")
    assert "**Owner:** Ada · **Started:** September 2026" in out
    assert "Tatenda" not in out
    assert "**Goal:** x" in out


def test_set_owner_treats_name_literally():
    text = "**Owner:** Tatenda · **Started:** August 2026"
    out = set_owner(text, r"A\1 O'\g<0>Brien", "May 2027")
    assert r"A\1 O'\g<0>Brien" in out


def test_set_owner_raises_when_no_owner_line():
    import pytest

    with pytest.raises(ValueError, match="found 0"):
        set_owner("# A plan with no owner line", "Ada", "May 2027")


def test_set_owner_raises_on_duplicate_owner_lines():
    import pytest

    text = "**Owner:** A · **Started:** May 2026\n\n**Owner:** B · **Started:** June 2026"
    with pytest.raises(ValueError, match="found 2"):
        set_owner(text, "Ada", "May 2027")


def test_fresh_progress_is_an_empty_table():
    table_lines = [line for line in FRESH_PROGRESS.strip().split("\n") if line.startswith("|")]
    assert len(table_lines) == 2  # header + separator, no data rows
    assert "2026" not in FRESH_PROGRESS


def test_wipe_notes_keeps_gitkeep(tmp_path):
    (tmp_path / "month-01.md").write_text("reflections")
    (tmp_path / "diagnostic.md").write_text("8/30")
    (tmp_path / ".gitkeep").write_text("")
    removed = wipe_notes(tmp_path)
    assert removed == ["diagnostic.md", "month-01.md"]
    assert (tmp_path / ".gitkeep").exists()
    assert list(tmp_path.glob("*.md")) == []
