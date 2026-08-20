"""Write sitemap.xml and robots.txt.

Pages marked noindex are left out, so holding pages do not turn up in search
results. Re-run after adding or promoting a page:

    python tools/make_sitemap.py
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from media_common import REPO, html_files

SITE = "https://daniel.bryars.com"


def last_modified(page: Path) -> str:
    """The date of the last commit that touched this file, for <lastmod>."""
    result = subprocess.run(
        ["git", "log", "-1", "--format=%cs", "--", str(page)],
        cwd=REPO, capture_output=True, text=True,
    )
    return result.stdout.strip()


def url_for(page: Path) -> str:
    rel = page.relative_to(REPO).as_posix()
    if rel == "index.html":
        return f"{SITE}/"
    if rel.endswith("/index.html"):
        return f"{SITE}/{rel[: -len('index.html')]}"
    return f"{SITE}/{rel}"


def main() -> int:
    entries = []
    skipped = []
    for page in html_files():
        text = page.read_text(encoding="utf-8")
        if 'name="robots"' in text and "noindex" in text:
            skipped.append(page.relative_to(REPO).as_posix())
            continue
        entries.append((url_for(page), last_modified(page)))

    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for url, lastmod in sorted(entries):
        lines.append("  <url>")
        lines.append(f"    <loc>{url}</loc>")
        if lastmod:
            lines.append(f"    <lastmod>{lastmod}</lastmod>")
        lines.append("  </url>")
    lines.append("</urlset>")
    (REPO / "sitemap.xml").write_text("\n".join(lines) + "\n", encoding="utf-8")

    (REPO / "robots.txt").write_text(
        "User-agent: *\n"
        "Allow: /\n"
        "Disallow: /derived/\n"
        f"\nSitemap: {SITE}/sitemap.xml\n",
        encoding="utf-8",
    )

    print(f"sitemap.xml: {len(entries)} page(s)")
    for item in skipped:
        print(f"  excluded (noindex): {item}")
    print("robots.txt written")
    return 0


if __name__ == "__main__":
    sys.exit(main())
