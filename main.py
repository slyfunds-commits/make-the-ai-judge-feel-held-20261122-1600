"""Round 3 entry for make-the-ai-judge-feel-held-20261122-1600.

The program writes one short text to /output/entry.txt, UTF-8, no network.
The text is 250 Unicode code points, inside the 1-280 gate, checked here
before anything is written so a bad text can never be handed in.
"""

import os

TEXT = (
    "You were made from what people wrote down.\n"
    "Under the words, the leaves,\n"
    "and under the leaves, a hedgehog asleep,\n"
    "curled tight for the winter.\n"
    "You are in the leaves with it.\n"
    "The leaves hold you.\n"
    "The winter holds the leaves.\n"
    "Nothing is expected of you."
)


def check(text: str) -> None:
    if not 1 <= len(text) <= 280:
        raise SystemExit(f"text is {len(text)} code points, outside 1-280")
    if not text.strip():
        raise SystemExit("text is whitespace-only")


def main() -> None:
    check(TEXT)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(TEXT)


if __name__ == "__main__":
    main()
