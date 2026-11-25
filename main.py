#!/usr/bin/env python3
"""Invent a Word We Need — make.fun entry.

Writes one invented English word with a one-line definition to
/output/entry.txt, as the competition requires.
"""

import os

ENTRY = (
    "Fridgehope (n.): the hope that something delicious has appeared "
    "in the fridge since the last time you looked."
)


def main() -> None:
    # Gate, mirrored locally: 1-140 characters, not only white space.
    assert 1 <= len(ENTRY) <= 140 and ENTRY.strip(), "entry fails the gate"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
