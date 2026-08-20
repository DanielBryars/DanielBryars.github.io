"""Shared helpers for the site media tooling.

The site is a plain static GitHub Pages site with no build step. These scripts
are run by hand when new photos or clips are added:

    python tools/make_derivatives.py     # resize images, transcode videos
    python tools/rewrite_media.py        # add srcset/width/height/lazy to HTML

Both are idempotent, so re-running them after adding a new project page is
safe and is the intended workflow.
"""

from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

# Widths we generate for responsive <img srcset>.
IMAGE_WIDTHS = (480, 960, 1600)

# Everything generated lands under this mirror tree so it can be deleted and
# rebuilt in one go without touching the original camera files.
DERIVED = "derived"

RASTER_SUFFIXES = {".jpg", ".jpeg", ".png"}
VIDEO_SUFFIXES = {".mp4"}

IMG_SRC_RE = re.compile(r'<img\b[^>]*?\bsrc="([^"]+)"', re.IGNORECASE)
POSTER_RE = re.compile(r'\bposter="([^"]+)"', re.IGNORECASE)
VIDEO_SRC_RE = re.compile(r'<source\b[^>]*?\bsrc="([^"]+)"', re.IGNORECASE)


# Directories that hold copies of the site rather than the site itself.
# .claude/worktrees in particular contains whole checkouts, and rewriting the
# pages in there would stamp them with nonsense canonical URLs.
EXCLUDED_DIRS = {".git", ".claude", DERIVED, "node_modules"}


def html_files() -> list[Path]:
    """Every page on the site, in a stable order.

    Matching is on the path *relative to the repo*, so this still works when
    the repo itself lives under an excluded name - which it does inside a
    .claude worktree.
    """
    return sorted(
        p
        for p in REPO.rglob("*.html")
        if not EXCLUDED_DIRS.intersection(p.relative_to(REPO).parts)
    )


def resolve(page: Path, url: str) -> Path | None:
    """Turn an href/src found in `page` into a repo path, or None if external."""
    url = url.split("#")[0].split("?")[0]
    if not url or url.startswith(("http://", "https://", "mailto:", "data:", "//")):
        return None
    from urllib.parse import unquote

    url = unquote(url)
    if url.startswith("/"):
        return REPO / url.lstrip("/")
    return (page.parent / url).resolve()


def derived_path(source: Path, suffix: str) -> Path:
    """derived/ mirror of `source` with `suffix` appended to the stem."""
    rel = source.relative_to(REPO)
    return REPO / DERIVED / rel.parent / f"{rel.stem}{suffix}"


def rel_url(from_page: Path, target: Path) -> str:
    """A relative URL from `from_page` to `target`, using forward slashes.

    Percent-encodes spaces and friends: a raw space is tolerated in `src` but
    silently breaks `srcset`, where space is the delimiter.
    """
    import os
    from urllib.parse import quote

    relative = os.path.relpath(target, from_page.parent).replace("\\", "/")
    return quote(relative, safe="/-._~")


def referenced_media(pages: list[Path] | None = None):
    """Yield (page, kind, url, resolved_path) for every local media reference."""
    for page in pages or html_files():
        text = page.read_text(encoding="utf-8")
        for kind, pattern in (
            ("img", IMG_SRC_RE),
            ("poster", POSTER_RE),
            ("video", VIDEO_SRC_RE),
        ):
            for match in pattern.finditer(text):
                url = match.group(1)
                target = resolve(page, url)
                if target is not None:
                    yield page, kind, url, target
