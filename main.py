#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers.

Writes one original fortune-cookie line for a software developer to
``entry.txt`` inside the output directory.

The output directory is ``$MAKEFUN_OUTPUT_DIR`` when set, otherwise
``/output``.  Standard library only; the program takes no input, reads no
other file, and writes exactly one line of text.
"""

import os
import sys

# The entry: one original fortune-cookie line, 120 characters or fewer.
# Angle: git blame as a mirror — the person it points at is never a
# stranger, only an earlier version of the reader.
ENTRY = "git blame never accuses a stranger; it only introduces you to an earlier you."


def main() -> int:
    """Write ENTRY to entry.txt in the output directory."""
    # Gate check, mirroring the competition gate: one line, 1-120 chars.
    if not 1 <= len(ENTRY) <= 120 or "\n" in ENTRY or not ENTRY.strip():
        print("entry fails the 1-120 character single-line gate", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
