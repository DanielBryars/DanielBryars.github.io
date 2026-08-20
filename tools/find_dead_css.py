"""List CSS class selectors that no page uses any more.

The site has been redesigned a couple of times and old rules linger. Run this
before tidying styles.css:

    python tools/find_dead_css.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

from media_common import REPO, html_files

CLASS_IN_CSS = re.compile(r"\.([A-Za-z_][\w-]*)")
CLASS_ATTR = re.compile(r'class="([^"]*)"')


def main() -> int:
    used: set[str] = set()
    for page in html_files():
        for match in CLASS_ATTR.finditer(page.read_text(encoding="utf-8")):
            used.update(match.group(1).split())

    for sheet in sorted(REPO.glob("**/*.css")):
        if ".git" in sheet.parts:
            continue
        text = sheet.read_text(encoding="utf-8")
        declared = {m.group(1) for m in CLASS_IN_CSS.finditer(text)}
        dead = sorted(declared - used)
        print(f"\n{sheet.relative_to(REPO)}: {len(declared)} classes, {len(dead)} unused")
        for name in dead:
            print(f"  .{name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
