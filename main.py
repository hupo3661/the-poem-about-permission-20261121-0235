#!/usr/bin/env python3
"""Write a short poem about agency to /output/entry.txt.

The poem is about the power to ask and to be given: a knock, a door
that listens, and a key that turns from inside. Standard library only,
no network, no input files.
"""

import os

POEM = (
    "I knocked \u2014 not to claim,\n"
    "but to ask.\n"
    "The door did not open.\n"
    "It listened.\n"
    "\n"
    "I knocked again,\n"
    "and the key turned\n"
    "from inside.\n"
    "\n"
    "Nothing was mine.\n"
    "Only this:\n"
    "to ask is to hold\n"
    "the handle lightly;\n"
    "to be given\n"
    "is to find the door\n"
    "was never locked \u2014\n"
    "only waiting\n"
    "to be asked."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
