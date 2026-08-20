"""Give every page a skip-to-content link and an id on <main>.

Keyboard and screen-reader users otherwise have to tab through the whole header
on every page. Idempotent - safe to re-run after adding pages:

    python tools/rewrite_skiplink.py
"""

from __future__ import annotations

import re
import sys

from media_common import REPO, html_files

SKIP = '    <a class="skip-link" href="#main">Skip to content</a>\n'
BODY_RE = re.compile(r"(<body\b[^>]*>\n)", re.IGNORECASE)
MAIN_RE = re.compile(r"<main(?![^>]*\bid=)", re.IGNORECASE)


def main() -> int:
    changed = 0
    for page in html_files():
        text = page.read_text(encoding="utf-8")
        original = text

        if 'class="skip-link"' not in text:
            text = BODY_RE.sub(lambda m: m.group(1) + SKIP, text, count=1)
        text = MAIN_RE.sub('<main id="main" tabindex="-1"', text, count=1)

        if text != original:
            page.write_text(text, encoding="utf-8")
            changed += 1
            print(f"  skip-link {page.relative_to(REPO)}")

    print(f"{changed} page(s) updated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
