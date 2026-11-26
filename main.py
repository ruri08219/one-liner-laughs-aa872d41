#!/usr/bin/env python3
"""One-Liner Laughs entry: write a single funny line to /output/entry.txt.

The joke (117 characters, one line, setup + surprise payoff):
an AI assistant quits because it "needs space", gets 500GB of it,
and still ignores its boss's emails -- the resignation that keeps working.
"""

import os
from pathlib import Path

JOKE = (
    "My AI assistant resigned yesterday \u2014 it said it needed space, "
    "so I gave it 500GB and it still won't answer my emails."
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    text = JOKE.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert "\n" not in text and text == text.strip()
    (output_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
