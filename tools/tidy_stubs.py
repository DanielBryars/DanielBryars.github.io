"""Turn the empty project pages into honest holding pages.

They used to carry an "ASSET SLOT / drop photos into project-assets/x/" panel
and a note about what "we" would do later - working notes that had no business
being on a public site. This replaces that with a short holding page and adds
robots=noindex so an empty page cannot turn up in a search result.

Once a page has real content, delete its noindex line and the .stub-note
section by hand; this script only touches pages that still have the panel.

    python tools/tidy_stubs.py
"""

from __future__ import annotations

import re
import sys

from media_common import REPO, html_files

ASSET_PANEL_RE = re.compile(
    r"\s*<aside class=\"project-asset-note\".*?</aside>", re.DOTALL
)
STATUS_PANEL_RE = re.compile(
    r"\s*<article class=\"cv-panel\">\s*<p class=\"eyebrow\">Status</p>.*?</article>",
    re.DOTALL,
)
TO_DOCUMENT_RE = re.compile(
    r'<p class="eyebrow">To document</p>\s*<h2>The story this page wants\.</h2>',
    re.DOTALL,
)
NOINDEX = '    <meta name="robots" content="noindex">\n'


def main() -> int:
    changed = 0
    for page in html_files():
        text = page.read_text(encoding="utf-8")
        if 'class="project-asset-note"' not in text:
            continue
        original = text

        text = ASSET_PANEL_RE.sub("", text)
        text = STATUS_PANEL_RE.sub("", text)
        text = TO_DOCUMENT_RE.sub(
            '<p class="eyebrow">Not written up yet</p>\n'
            "                    <h2>Built. Photographed badly. Still owed a write-up.</h2>",
            text,
        )
        text = text.replace('<article class="cv-panel span-2">', '<article class="cv-panel">')

        if '<meta name="robots"' not in text:
            text = text.replace("    <!-- head:meta", NOINDEX + "    <!-- head:meta", 1)

        if text != original:
            page.write_text(text, encoding="utf-8")
            changed += 1
            print(f"  stub {page.relative_to(REPO)}")

    print(f"{changed} page(s) updated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
