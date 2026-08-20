"""Count the writing tics that make the copy read as machine-generated.

Not a linter for good prose - just a way to see where the same handful of
constructions are piling up, and to check whether an edit actually reduced them.

    python tools/voice_check.py
"""

from __future__ import annotations

import re
import sys

from media_common import REPO, html_files

TICS = {
    "not just X / is not X, it is Y": r"\bnot just\b|\bis not (?:just|only)\b",
    "which is exactly/partly the point": (
        r"\bwhich is (?:exactly|partly|precisely|basically)\b"
        r"|\bthat is part of the point\b|\bwhich is the whole\b"
    ),
    "object given feelings": (
        r"\b(?:sulk|being dramatic|has opinions|have opinions|wants its own|fought back"
        r"|punishes optimism|stops being charming|behave itself|too well behaved"
        r"|chose violence|earns its keep)\b"
    ),
    "abstract flourish": (
        r"\bwhere .{3,30} (?:lives|goes to be|stops being)\b"
        r"|\bthe (?:least|most) \w+ way possible\b|\bmade of perfect \w+\b"
    ),
    "pile-up of five or more nouns": r"(?:\b[\w-]+, ){4,}[\w-]+ and [\w-]+",
    "sentence-initial 'It is' / 'That is'": r"(?:^|\. )(?:It|That) is\b",
}


def main() -> int:
    rows = []
    totals: dict[str, int] = {}

    for page in html_files():
        text = re.sub(r"<[^>]+>", " ", page.read_text(encoding="utf-8"))
        counts = {name: len(re.findall(rx, text, re.I)) for name, rx in TICS.items()}
        words = len(text.split())
        if words < 200:
            continue
        total = sum(counts.values())
        rows.append((total / (words / 1000), total, page.relative_to(REPO).as_posix()))
        for name, count in counts.items():
            totals[name] = totals.get(name, 0) + count

    rows.sort(reverse=True)
    print(f"{'page':46}{'tics':>6}{'per 1k words':>14}")
    for rate, total, name in rows:
        print(f"{name:46}{total:6}{rate:14.1f}")

    print("\nby construction:")
    for name, count in sorted(totals.items(), key=lambda item: -item[1]):
        print(f"  {count:4}  {name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
