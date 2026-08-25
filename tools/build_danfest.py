"""Import the DanFest party photographs and build danfest.html.

The originals live in OneDrive and total ~400MB across 68 files. Committing
those would push the repository past what GitHub Pages will serve, so this
resizes them to a sensible maximum on the way in; `derived/` then does its
usual job on top. Point SOURCE at the folder and run:

    python tools/build_danfest.py
"""

from __future__ import annotations

import base64
import io
import re
import sys
from pathlib import Path

from PIL import Image, ImageOps

from media_common import REPO

SOURCE = Path(r"C:\Users\bryar\OneDrive\Pictures\2026 DanFest\Final_Cropped")
DEST = REPO / "project-assets" / "danfest"

# Big enough to fill a laptop screen properly when the lightbox opens it. The
# grid never loads this size - it uses the 480/960/1600 derivatives - so the
# cost is only paid by someone who actually clicks a photograph.
MAX_EDGE = 2400
QUALITY = 82

# A 16px-wide version of each frame, inlined as a base64 background on the
# figure. It arrives with the HTML, so every tile shows a blurred version of
# the right photograph immediately and the real one paints over it.
LQIP_WIDTH = 16
LQIP_QUALITY = 35

# Ordered so the page runs roughly chronologically: setting up, the daylight
# hours, food and drink, the people, then the evening. Captions come from what
# is actually in the frame; nothing invented.
SECTIONS: list[tuple[str, str, list[tuple[str, str]]]] = [
    ("Setting up", "The day before, and the morning of.", [
        ("20260807_081036.jpg", "Kegs arriving the day before"),
        ("20260807_105809.jpg", "The car, doing its bit"),
        ("DanFest.png", "The sign"),
        ("WebSite.png", "The invitation: a working Ceefax service, page 501"),
    ]),
    ("Daylight", "Open house, kids welcome, weather behaving.", [
        ("_MG_8718.jpg", "Along the corten"),
        ("_MG_8702.jpg", "On the terrace steps"),
        ("_MG_8743.jpg", "Heading out through the doors"),
        ("_MG_8731.jpg", "Pool, indoors, quieter"),
        ("_MG_8889.jpg", "Leaning on the balustrade"),
        ("_MG_8901.jpg", "The view, and the fields"),
        ("_MG_8882.jpg", "Sunglasses weather"),
        ("Football.png", "Football, obviously"),
        ("Running.png", "Running, at speed"),
        ("LincolnHat.png", "Lincoln, and a hat"),
        ("DaddyAndDaughter.png", "Straw bales and a sit down"),
    ]),
    ("Food and drink", "A bar, a barbecue, a paella the size of a table.", [
        ("Bar.png", "The bar, before it got busy"),
        ("Beer.png", "The bins did a lot of work"),
        ("MarcusPullsAPint.png", "Marcus pulls a pint"),
        ("PerfectPour.png", "The perfect pour"),
        ("OwenPaella.jpg", "Owen and the paella"),
        ("Rice.jpg", "It fed everyone"),
        ("Aspall.png", "Cider, under the lights"),
        ("_MG_8786.jpg", "Digging about in the ice"),
    ]),
    ("Everyone", "The actual point of the whole thing.", [
        ("Dan.png", "Me, in the shirt"),
        ("DanAndEmma.png", "Dan and Emma"),
        ("Recreated.png", "A photograph, recreated properly"),
        ("Kiss.png", "Hello again"),
        ("Gang1.png", "The gang"),
        ("GoodChat.png", "A good chat"),
        ("InConversation.png", "In conversation"),
        ("JakeAndDom.png", "Jake and Dom"),
        ("JamesAndDan.jpg", "James and Dan"),
        ("KandSJ.png", "K and SJ"),
        ("KanesAndMatt.png", "The Kanes and Matt"),
        ("KarieAndSJ.png", "Karie and SJ"),
        ("KateAndPolly.png", "Kate and Polly"),
        ("KeithKeepingAwake.png", "Keith, keeping awake"),
        ("Kim.png", "Kim"),
        ("KristinAndJane.png", "Kristin and Jane"),
        ("Ladies.jpg", "By the bar"),
        ("MikeAndJim.png", "Mike and Jim"),
        ("MonacoChallenge.jpg", "The Monaco challenge"),
        ("Nat.png", "Nat"),
        ("OwenAndMarcus.png", "Owen and Marcus"),
        ("Patrick.png", "Patrick"),
        ("Saunders.jpg", "Saunders"),
        ("Sean.jpg", "Sean, and a guitar"),
        ("Serious.png", "Very serious indeed"),
        ("Focus.png", "Focus"),
        ("ImTired.png", "One guest had had enough"),
        ("ELLIOT.png", "Elliot, fully committed"),
        ("_MG_8809.jpg", "Standing about, talking"),
        ("_MG_8870.jpg", "Mid-anecdote"),
        ("_MG_8924.jpg", "Laughing at something"),
        ("_MG_8932.jpg", "The terrace, filling up"),
        ("_MG_8973.jpg", "Good company"),
        ("_MG_8977.jpg", "As the light went"),
        ("_MG_8980.jpg", "Garlands were issued"),
        ("WhatsApp Image 2026-08-09 at 11.41.45 (1).jpg", "Sent the morning after"),
        ("WhatsApp Image 2026-08-09 at 11.41.45 (2).jpg", "Also sent the morning after"),
        ("WhatsApp Image 2026-08-10 at 10.19.50.jpg", "Two days later, still going"),
    ]),
    ("After dark", "DJs, a laser, and the lights I made earlier.", [
        ("DJJim.png", "DJ Jim"),
        ("Party.png", "The dancing started"),
        ("Party2.png", "And carried on"),
        ("Laser.png", "The laser earned its keep"),
        ("Lights.png", "The house, at night"),
        ("_MG_9021.jpg", "Under the UV"),
        ("_MG_9038.jpg", "Late"),
    ]),
]


def slug(name: str) -> str:
    stem = Path(name).stem
    stem = re.sub(r"[^A-Za-z0-9]+", "-", stem)
    stem = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "-", stem)
    return re.sub(r"-+", "-", stem).strip("-").lower()


def make_lqip(im: Image.Image) -> str:
    """A base64 data URI of a tiny version of the frame, for the blur-up."""
    tiny = im.copy()
    height = max(1, round(tiny.height * LQIP_WIDTH / tiny.width))
    tiny = tiny.resize((LQIP_WIDTH, height), Image.LANCZOS)
    buffer = io.BytesIO()
    tiny.save(buffer, "JPEG", quality=LQIP_QUALITY, optimize=True)
    return "data:image/jpeg;base64," + base64.b64encode(buffer.getvalue()).decode("ascii")


def import_photos() -> dict[str, tuple[str, str]]:
    DEST.mkdir(parents=True, exist_ok=True)
    mapping: dict[str, tuple[str, str]] = {}
    for _, _, entries in SECTIONS:
        for original, _caption in entries:
            source = SOURCE / original
            if not source.exists():
                print(f"  !! missing source: {original}")
                continue
            target = DEST / f"{slug(original)}.jpg"
            with Image.open(source) as im:
                im = ImageOps.exif_transpose(im).convert("RGB")
                im.thumbnail((MAX_EDGE, MAX_EDGE), Image.LANCZOS)
                if not target.exists():
                    im.save(target, "JPEG", quality=QUALITY, optimize=True, progressive=True)
                    print(f"  photo {target.name}")
                mapping[original] = (target.name, make_lqip(im))
    return mapping


PAGE_HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Photographs from DanFest, Daniel Bryars' 50th birthday party, August 2026.">
    <!-- Private-ish: friends and family, not search engines. -->
    <meta name="robots" content="noindex">
    <title>DanFest - Daniel Bryars</title>
    <link rel="stylesheet" href="fonts.css">
    <link rel="stylesheet" href="styles.css">
</head>
<body class="project-detail-page">
    <a class="skip-link" href="#main">Skip to content</a>
    <div class="home-shell">
        <header class="site-header" aria-label="Primary">
            <a class="brand" href="index.html">
                <span class="brand-mark">DB</span>
                <span>
                    <strong>Daniel Bryars</strong>
                    <small>danfest / the photographs</small>
                </span>
            </a>
            <nav class="top-nav">
                <a href="index.html">Home</a>
                <a href="projects/index.html">Projects</a>
                <a href="cv.html">CV</a>
                <a href="https://danfest.bryars.com" target="_blank" rel="noreferrer">Page 501</a>
            </nav>
        </header>

        <main id="main" tabindex="-1">
            <section class="projects-hero">
                <p class="eyebrow">8 August 2026 &middot; noon till midnight</p>
                <h1>DanFest</h1>
                <p>
                    I turned 50, so I built a Ceefax service to invite everyone, put a bar in the garden and
                    a DJ in the barn, and asked people to come for the day. They did. These are the
                    photographs.
                </p>
                <div class="hero-actions">
                    <a class="button primary" href="https://danfest.bryars.com" target="_blank" rel="noreferrer">The invitation</a>
                    <a class="button" href="#photographs">The photographs</a>
                </div>
            </section>
"""

PAGE_TAIL = """        </main>

        <footer class="site-footer">
            <div>
                <strong>DanFest</strong>
                <span>Thank you, all of you.</span>
            </div>
            <div class="footer-links">
                <a href="index.html">Home</a>
                <a href="https://danfest.bryars.com" target="_blank" rel="noreferrer">Page 501</a>
                <a href="mailto:danfest@bryars.com">danfest@bryars.com</a>
            </div>
        </footer>
    </div>

    <script src="image-lightbox.js"></script>
</body>
</html>
"""


def build_page(mapping: dict[str, str]) -> None:
    parts = [PAGE_HEAD]
    first = True
    for title, blurb, entries in SECTIONS:
        anchor = ' id="photographs"' if first else ""
        parts.append(f"""
            <section class="project-section-title photo-section"{anchor} aria-label="{title}">
                <p class="eyebrow">{title}</p>
                <h2>{blurb}</h2>
            </section>

            <section class="photo-grid" aria-label="{title} photographs">
""")
        for original, caption in entries:
            entry = mapping.get(original)
            if not entry:
                continue
            name, lqip = entry
            full = f"project-assets/danfest/{name}"
            alt = caption[0].lower() + caption[1:] if caption[:1].isupper() else caption
            parts.append(
                f'                <figure style="background-image:url({lqip})">\n'
                f'                    <img src="{full}" data-full="{full}" '
                f'alt="DanFest: {alt}.">\n'
                f"                    <figcaption>{caption}</figcaption>\n"
                f"                </figure>\n"
            )
        parts.append("            </section>\n")
        first = False
    parts.append(PAGE_TAIL)

    target = REPO / "danfest.html"
    target.write_text("".join(parts).replace("\n", "\r\n"), encoding="utf-8", newline="")
    print(f"wrote {target.name}")


def main() -> int:
    if not SOURCE.exists():
        print(f"source folder not found: {SOURCE}")
        return 1
    mapping = import_photos()
    build_page(mapping)
    total = sum(f.stat().st_size for f in DEST.iterdir())
    print(f"{len(mapping)} photos, {total / 1048576:.1f} MB in {DEST.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
