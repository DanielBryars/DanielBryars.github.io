"""Dump every heading and figcaption, grouped by page, for editing."""

from __future__ import annotations

import re
import sys

from media_common import REPO, html_files

RE = re.compile(r"<(h[123]|figcaption)>(?:<a[^>]*>)?([^<]+)", re.IGNORECASE)


def main() -> int:
    only = sys.argv[1] if len(sys.argv) > 1 else None
    for page in html_files():
        name = page.relative_to(REPO).as_posix()
        if only and only not in name:
            continue
        items = [
            (m.group(1).lower(), m.group(2).strip())
            for m in RE.finditer(page.read_text(encoding="utf-8"))
        ]
        if not items:
            continue
        print(f"\n### {name}")
        for tag, text in items:
            mark = "*" if text.endswith(".") and len(text.split()) <= 9 else " "
            print(f"{mark} [{tag}] {text}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
