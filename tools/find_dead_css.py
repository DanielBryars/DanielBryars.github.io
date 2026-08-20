"""List CSS class selectors that no page uses any more.

The site has been redesigned a couple of times and old rules linger. Run this
before tidying styles.css:

    python tools/find_dead_css.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

from media_common import EXCLUDED_DIRS, REPO, html_files

CLASS_IN_CSS = re.compile(r"\.([A-Za-z_][\w-]*)")
CLASS_ATTR = re.compile(r'class="([^"]*)"')
# Any quoted string in a script might be a class name handed to className or
# classList; over-matching here only costs a few false "used" entries.
JS_STRING_RE = re.compile(r"""['"]([A-Za-z_][\w -]*)['"]""")


def main() -> int:
    used: set[str] = set()
    for page in html_files():
        for match in CLASS_ATTR.finditer(page.read_text(encoding="utf-8")):
            used.update(match.group(1).split())

    # Some classes only ever exist because a script creates the element, so
    # scan the JavaScript too rather than reporting those as dead.
    for script in sorted(REPO.rglob("*.js")):
        if EXCLUDED_DIRS.intersection(script.relative_to(REPO).parts):
            continue
        text = script.read_text(encoding="utf-8")
        for match in CLASS_ATTR.finditer(text):
            used.update(match.group(1).split())
        for match in JS_STRING_RE.finditer(text):
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
