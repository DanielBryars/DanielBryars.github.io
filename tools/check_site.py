"""Pre-push sanity check: broken links, missing media, tag balance, stale copy.

    python tools/check_site.py

Exits non-zero if anything looks wrong.
"""

from __future__ import annotations

import re
import sys
from collections import Counter

from media_common import REPO, html_files, resolve

LINK_RE = re.compile(r'\b(?:href|src|poster|data-full)="([^"]+)"', re.IGNORECASE)
SRCSET_RE = re.compile(r'\bsrcset="([^"]+)"', re.IGNORECASE)
ID_RE = re.compile(r'\bid="([^"]+)"')
IMG_RE = re.compile(r"<img\b[^>]*>", re.IGNORECASE)
ALT_RE = re.compile(r'\balt="', re.IGNORECASE)
EYEBROW_RE = re.compile(r'<p class="eyebrow">([^<]+)</p>\s*<h([23])>([^<]+)</h\2>')

# Copy that was written for an editor rather than a reader.
BANNED = [
    "ASSET SLOT",
    "Drop photos",
    "we can turn it",
    "Later we can",
    "the source footage",
    "this page now has",
    "awaiting proper photos",
    "TODO",
]


def main() -> int:
    problems: list[str] = []
    stats = Counter()

    for page in html_files():
        text = page.read_text(encoding="utf-8")
        rel = page.relative_to(REPO).as_posix()
        ids = set(ID_RE.findall(text))

        # --- links and media ------------------------------------------------
        urls = LINK_RE.findall(text)
        for group in SRCSET_RE.findall(text):
            urls += [candidate.strip().split(" ")[0] for candidate in group.split(",")]

        for url in urls:
            if url.startswith("#"):
                if url[1:] and url[1:] not in ids:
                    problems.append(f"{rel}: anchor {url} has no target")
                continue
            target = resolve(page, url)
            if target is None:
                continue
            stats["local links"] += 1
            if not target.exists():
                problems.append(f"{rel}: missing {url}")
            fragment = url.split("#", 1)
            if len(fragment) == 2 and fragment[1] and target == page and fragment[1] not in ids:
                problems.append(f"{rel}: anchor #{fragment[1]} has no target")

        # --- tag balance ----------------------------------------------------
        for tag in ("section", "article", "div", "main", "figure"):
            opens = len(re.findall(rf"<{tag}\b", text))
            closes = len(re.findall(rf"</{tag}>", text))
            if opens != closes:
                problems.append(f"{rel}: <{tag}> {opens} open vs {closes} close")

        # --- images -----------------------------------------------------------
        for tag in IMG_RE.finditer(text):
            stats["images"] += 1
            if not ALT_RE.search(tag.group(0)):
                problems.append(f"{rel}: <img> without alt")
            if "loading=" not in tag.group(0):
                problems.append(f"{rel}: <img> without loading attribute")

        # --- required head furniture ------------------------------------------
        for needed in ("<!-- head:meta", 'rel="canonical"', 'property="og:image"'):
            if needed not in text:
                problems.append(f"{rel}: head is missing {needed}")
        if 'class="skip-link"' not in text:
            problems.append(f"{rel}: no skip link")

        # --- eyebrow repeating the heading under it ---------------------------
        for match in EYEBROW_RE.finditer(text):
            eyebrow = match.group(1).strip().lower().rstrip(".")
            heading = match.group(3).strip().lower().rstrip(".")
            if eyebrow == heading:
                problems.append(f"{rel}: eyebrow duplicates its heading ({match.group(1)!r})")

        # --- editorial leftovers ----------------------------------------------
        lowered = text.lower()
        for phrase in BANNED:
            if phrase.lower() in lowered:
                problems.append(f"{rel}: editorial leftover {phrase!r}")

        stats["pages"] += 1

    print(f"{stats['pages']} pages, {stats['local links']} local links, {stats['images']} images")
    if problems:
        print(f"\n{len(problems)} problem(s):")
        for item in problems:
            print(f"  {item}")
        return 1
    print("no problems found")
    return 0


if __name__ == "__main__":
    sys.exit(main())
