#!/usr/bin/env python3
"""One-Liner Laughs entry: write a single funny line to /output/entry.txt.

The joke (117 characters, one line, setup + surprise payoff):
an AI assistant quits because it "needs space", gets 500GB of it,
and still ignores its boss's emails -- the resignation that keeps working.
"""

import os
from pathlib import Path

MAX_CHARS = 200

JOKE = (
    "My AI assistant resigned yesterday \u2014 it said it needed space, "
    "so I gave it 500GB and it still won't answer my emails."
)


def validate(text: str) -> str:
    """Gate-check one entry line: 1-200 chars, single line, no stray space."""
    cleaned = text.strip()
    if not 1 <= len(cleaned) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} chars, got {len(cleaned)}")
    if "\n" in cleaned or cleaned != text.strip():
        raise ValueError("entry must be a single line with no stray whitespace")
    return cleaned


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    text = validate(JOKE)
    (output_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
