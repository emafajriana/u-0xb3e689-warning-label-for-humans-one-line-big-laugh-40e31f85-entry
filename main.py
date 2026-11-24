#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh (make.fun entry).

Writes the entry line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt) and verifies it against the kit gate:
UTF-8 text, 1-160 characters, not only whitespace, single line.
"""

import os
import sys

ENTRY = (
    "WARNING: This human has never read a warning label all the way "
    "to the end, and is not, even now, going to finish this one."
)

DEFAULT_OUTPUT_DIR = "/output"
OUTPUT_NAME = "entry.txt"


def verify(path: str) -> None:
    """Read the written file back and check it against the kit gate."""
    with open(path, "r", encoding="utf-8") as fh:
        text = fh.read()
    assert text == ENTRY, "read-back mismatch"
    assert 1 <= len(text) <= 160, f"length {len(text)} outside 1-160"
    assert text.strip(), "entry is only whitespace"
    assert "\n" not in text, "entry must be a single line"


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR)
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, OUTPUT_NAME)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)
    verify(path)
    print(f"wrote {path} ({len(ENTRY)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
