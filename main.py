"""The Vacuum's Alibi: one-line excuse a robot vacuum gives for missing a spot.

Writes the entry text to <OUTPUT_DIR>/entry.txt (default /output).
"""

import os

ENTRY = "The dust in that corner unionized. Negotiations are ongoing. I refuse to cross a picket line."
# Ladder verdict (~/workspace/makefun/vacuum-alibi-ladder.md): candidate #10,
# tightened ("has formed a union" -> "unionized", "will not" -> "refuse").
# 6-0 in the pairwise tournament vs the six-style panel; highest LOW (+1),
# no loss to any style. Twist: the vacuum sides with the dust and refuses to
# cross its picket line. 93 characters, one line.


def write_entry(output_dir: str) -> str:
    """Write the entry line to entry.txt inside output_dir; return its path."""
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    return path


def main() -> None:
    write_entry(os.environ.get("OUTPUT_DIR", "/output"))


if __name__ == "__main__":
    main()
