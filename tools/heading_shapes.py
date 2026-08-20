"""How many headings are the same shape?

The site's signature move is a short declarative fragment ending in a full
stop, used as a heading. One or two are a style. A hundred is a template.

    python tools/heading_shapes.py
"""

from __future__ import annotations

import re
import sys
from collections import Counter

from media_common import REPO, html_files

HEADING_RE = re.compile(r"<h([23])>(?:<a[^>]*>)?([^<]+)", re.IGNORECASE)


def main() -> int:
    shapes = Counter()
    examples: dict[str, list[str]] = {}
    per_page = Counter()

    for page in html_files():
        for match in HEADING_RE.finditer(page.read_text(encoding="utf-8")):
            heading = match.group(2).strip()
            if not heading:
                continue
            words = len(heading.split())
            ends_in_stop = heading.endswith(".")
            if ends_in_stop and words <= 9:
                shape = "epigram (short fragment ending in a full stop)"
                per_page[page.relative_to(REPO).as_posix()] += 1
            elif ends_in_stop:
                shape = "full sentence ending in a full stop"
            else:
                shape = "plain label (no full stop)"
            shapes[shape] += 1
            examples.setdefault(shape, []).append(heading)

    total = sum(shapes.values())
    print(f"{total} headings\n")
    for shape, count in shapes.most_common():
        print(f"  {count:4} ({count / total:4.0%})  {shape}")
        for sample in examples[shape][:4]:
            print(f"           - {sample}")
        print()

    print("worst pages for epigram headings:")
    for name, count in per_page.most_common(8):
        print(f"  {count:3}  {name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
