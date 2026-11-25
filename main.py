#!/usr/bin/env python3
"""Write one office joke to entry.txt.

The joke is a single line about office life: a setup (the printer
that always jams at the worst moment) with a turn at the end, where
the punchline lands last.
"""

import os


JOKE = (
    "The office printer only ever jams when I'm already late "
    "\u2014 turns out it's the most punctual employee we have."
)


def main():
    # This entry needs no input files, but honour the harness env var
    # so the program follows the same input/output contract as the
    # other entries in this wave.
    _input_dir = os.environ.get("MAKEFUN_INPUT_DIR") or "/input"
    _ = _input_dir
    if not 1 <= len(JOKE) <= 200 or not JOKE.strip():
        raise ValueError("joke must be 1 to 200 non-blank characters")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(JOKE)


if __name__ == "__main__":
    main()
