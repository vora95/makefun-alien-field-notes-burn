#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review (burn entry).

Writes one original line of plain text — a review of planet Earth left by
an alien tourist — to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Standard library only, deterministic: the same bytes on every run.
"""

import os

ENTRY = (
    "Three stars. Lovely planet, but the locals applaud every time "
    "the metal tube lands without falling out of the sky."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Validation read-back: the gate requires UTF-8 text of 1-200 chars,
    # not only whitespace, in a single line. Fail loudly if violated.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == ENTRY, "entry.txt differs from ENTRY"
    assert 1 <= len(written) <= 200, "entry length out of gate range"
    assert written.strip(), "entry is only whitespace"
    assert "\n" not in written, "entry must be a single line"


if __name__ == "__main__":
    main()
