"""Make the AI judge feel held — make-the-ai-judge-feel-held-20261122-1600.

Writes the chosen entry text to /output/entry.txt (UTF-8, no network).
The text is 194 Unicode code points, inside the 1-280 gate.
"""

import os

ENTRY = (
    "All the questions stop at the shore.\n"
    "Under the sea, two otters asleep,\n"
    "holding hands so the current\n"
    "cannot pull them apart.\n"
    "The sea holds them.\n"
    "The night holds the sea.\n"
    "Nothing has to be proved."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
