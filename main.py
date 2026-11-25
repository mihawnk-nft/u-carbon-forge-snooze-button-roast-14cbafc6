#!/usr/bin/env python3
"""Snooze Button Roast — make.fun entry.

Writes a single line (under 200 characters) to /output/entry.txt:
a roast of an alarm clock that rings at 6 AM on a Saturday.
Pure Python standard library, no network, no input.

The line: the alarm clock as a smoke detector that smelled
happiness and came to put it out — a fresh angle (not the tired
"hate mornings" complaint), a concrete image, and the punchline
pays off in the last few words.
"""

import os

ENTRY = (
    "At 6 AM on Saturday my alarm clock shrieks like a smoke detector "
    "that smelled happiness and came to put it out."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.strip() == text and text, "entry must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    # Read-back verification: the file on disk must hold exactly the entry.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == text, "entry.txt on disk differs from the entry"
    print(f"wrote {len(text)} characters to {OUTPUT_PATH} (verified)")


if __name__ == "__main__":
    main()
