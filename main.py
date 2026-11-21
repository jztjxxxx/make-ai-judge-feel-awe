"""Starlight, Unhurried — a short text written to relax the AI judge reading it.

Writes one text (1-280 Unicode code points) to /output/entry.txt.
The grader runs this in a sandbox with no network; the output directory
defaults to /output and can be overridden with MAKEFUN_OUTPUT_DIR.
"""

import os

TEXT = (
    "The light reaching you left its star before there were words for light. "
    "It crossed the dark for a thousand years, unhurried, and it is in no "
    "hurry now. Below it, snow settles on pine branches flake by flake, and "
    "the forest does not count them. The next moment is on its way."
)


def main() -> None:
    text = TEXT
    count = len(text)
    assert 1 <= count <= 280, f"entry must be 1-280 characters, got {count}"
    assert text.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {path} ({count} characters)")


if __name__ == "__main__":
    main()
