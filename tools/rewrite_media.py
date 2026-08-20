"""Point the pages at the web-sized media in derived/ and make loading lazy.

For every <img> this sets src/srcset/sizes to the generated derivatives, adds
the intrinsic width/height so the page stops reflowing as photos arrive, and
marks everything below the fold loading="lazy". For every <video> it swaps the
source to the 720p transcode and the poster to a web-sized still.

Idempotent - re-run after adding pages or media:

    python tools/make_derivatives.py && python tools/rewrite_media.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from media_common import REPO, derived_path, html_files, rel_url, resolve

MANIFEST = json.loads((REPO / "tools" / "media-manifest.json").read_text(encoding="utf-8"))

IMG_TAG_RE = re.compile(r"<img\b[^>]*>", re.IGNORECASE)
VIDEO_BLOCK_RE = re.compile(r"<video\b[^>]*>.*?</video>", re.IGNORECASE | re.DOTALL)
ATTR_RE = re.compile(r'\s+(?:srcset|sizes|width|height|loading|decoding|fetchpriority)="[^"]*"', re.IGNORECASE)
SRC_RE = re.compile(r'\bsrc="([^"]+)"', re.IGNORECASE)
POSTER_RE = re.compile(r'\bposter="([^"]+)"', re.IGNORECASE)

# The `sizes` hint depends on how much of the layout the image occupies, which
# is decided by the enclosing <section> (and sometimes the <figure>), not by
# whatever happens to sit near the tag in the source.
WIDE_MARKERS = ("artifact-hero-image", "gallery-wide", "about-hero", "hero-panel",
                "project-feature lead", "artifact-hero")
THUMB_MARKERS = ("evidence-strip",)
SIZES_WIDE = "(max-width: 900px) 100vw, 600px"
SIZES_GRID = "(max-width: 620px) 100vw, (max-width: 900px) 46vw, 30vw"
SIZES_THUMB = "(max-width: 620px) 50vw, (max-width: 900px) 33vw, 20vw"

BLOCK_RE = re.compile(r"<(/?)(?:section|article|figure|aside)\b([^>]*)>", re.IGNORECASE)
CLASS_RE = re.compile(r'class="([^"]*)"', re.IGNORECASE)


def layout_context(text: str, position: int) -> str:
    """Class names of the block elements actually containing `position`.

    A byte window before the tag is not good enough: the fifth thumbnail in a
    strip is thousands of characters from the <section> that sizes it, and a
    plain <figure> in a gallery would otherwise inherit the class of the wide
    one above it. So keep a real stack of open ancestors.
    """
    stack: list[str] = []
    for match in BLOCK_RE.finditer(text, 0, position):
        if match.group(1):
            if stack:
                stack.pop()
        else:
            found = CLASS_RE.search(match.group(2))
            stack.append(found.group(1) if found else "")
    return " ".join(stack)


# A page that has already been rewritten points at derived/, so map those paths
# back to the original they came from. Without this the script would quietly
# stop touching pages after its first run.
BY_DERIVED_STEM: dict[str, str] = {}
for _key in MANIFEST:
    _source = Path(_key)
    BY_DERIVED_STEM[f"derived/{_source.parent.as_posix()}/{_source.stem}"] = _key

DERIVED_SUFFIX_RE = re.compile(r"-(?:\d+|720)$")


def lookup(target: Path) -> tuple[Path, dict] | tuple[None, None]:
    """Resolve a referenced path to (original file, manifest entry)."""
    try:
        key = str(target.relative_to(REPO)).replace("\\", "/")
    except ValueError:
        return None, None
    if key in MANIFEST:
        return target, MANIFEST[key]

    as_path = Path(key)
    stem = DERIVED_SUFFIX_RE.sub("", as_path.stem)
    original = BY_DERIVED_STEM.get(f"{as_path.parent.as_posix()}/{stem}")
    if original:
        return REPO / original, MANIFEST[original]
    return None, None


def rewrite_img(tag: str, page: Path, is_first: bool, context: str) -> str:
    src_match = SRC_RE.search(tag)
    if not src_match:
        return tag
    referenced = resolve(page, src_match.group(1))
    if referenced is None:
        return tag
    target, entry = lookup(referenced)
    if not entry or "width" not in entry:
        return tag

    tag = ATTR_RE.sub("", tag)

    widths = entry.get("widths", [])
    if widths:
        srcset = ", ".join(
            f"{rel_url(page, derived_path(target, f'-{w}.jpg'))} {w}w" for w in widths
        )
        fallback = rel_url(page, derived_path(target, f"-{max(widths)}.jpg"))
        if any(m in context for m in THUMB_MARKERS):
            sizes = SIZES_THUMB
        elif any(m in context for m in WIDE_MARKERS):
            sizes = SIZES_WIDE
        else:
            sizes = SIZES_GRID
        tag = SRC_RE.sub(lambda _: f'src="{fallback}"', tag, count=1)
        extra = f' srcset="{srcset}" sizes="{sizes}"'
    else:
        extra = ""

    extra += f' width="{entry["width"]}" height="{entry["height"]}"'
    # The first image on a page is the one the visitor is waiting for.
    extra += ' loading="eager" fetchpriority="high"' if is_first else ' loading="lazy"'
    extra += ' decoding="async"'

    return tag[:-1].rstrip() + extra + ">"


def rewrite_video(block: str, page: Path) -> str:
    def swap_source(match: re.Match) -> str:
        referenced = resolve(page, match.group(1))
        _, entry = lookup(referenced) if referenced else (None, None)
        if not entry or "web" not in entry:
            return match.group(0)
        return f'src="{rel_url(page, REPO / entry["web"])}"'

    def swap_poster(match: re.Match) -> str:
        referenced = resolve(page, match.group(1))
        target, entry = lookup(referenced) if referenced else (None, None)
        if not entry or not entry.get("widths"):
            return match.group(0)
        width = 960 if 960 in entry["widths"] else max(entry["widths"])
        return f'poster="{rel_url(page, derived_path(target, f"-{width}.jpg"))}"'

    block = SRC_RE.sub(swap_source, block)
    block = POSTER_RE.sub(swap_poster, block)

    # A poster is showing, so there is no reason to fetch anything until play.
    block = re.sub(r'\s+preload="[^"]*"', "", block, flags=re.IGNORECASE)
    block = re.sub(r"\s+playsinline", "", block, flags=re.IGNORECASE)
    block = block.replace("<video ", '<video preload="none" playsinline ', 1)
    return block


def main() -> int:
    changed = 0
    for page in html_files():
        text = page.read_text(encoding="utf-8")
        original = text

        text = VIDEO_BLOCK_RE.sub(lambda m: rewrite_video(m.group(0), page), text)

        seen_first = False
        out: list[str] = []
        cursor = 0
        for match in IMG_TAG_RE.finditer(text):
            out.append(text[cursor : match.start()])
            context = layout_context(text, match.start())
            out.append(rewrite_img(match.group(0), page, not seen_first, context))
            seen_first = True
            cursor = match.end()
        out.append(text[cursor:])
        text = "".join(out)

        if text != original:
            page.write_text(text, encoding="utf-8")
            changed += 1
            print(f"  media {page.relative_to(REPO)}")

    print(f"{changed} page(s) updated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
