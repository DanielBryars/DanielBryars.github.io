"""Generate the favicon raster and the social-share (Open Graph) card.

Run once, or again if the source photo or the wording changes:

    python tools/make_branding.py
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps

REPO = Path(__file__).resolve().parent.parent

YELLOW = "#ffe55c"
CYAN = "#53d8ff"
INK = "#f5f2dc"
BLACK = "#050505"

OG_SOURCE = REPO / "project-assets" / "lathe-sparks" / "05-sparks-hero.jpg"
OG_OUT = REPO / "images" / "og-cover.jpg"
ICON_OUT = REPO / "images" / "apple-touch-icon.png"

WINDOWS_FONTS = Path("C:/Windows/Fonts")


def font(name: str, size: int) -> ImageFont.FreeTypeFont:
    path = WINDOWS_FONTS / name
    if path.exists():
        return ImageFont.truetype(str(path), size)
    return ImageFont.load_default(size)


def make_icon() -> None:
    """A raster version of favicon.svg, for iOS home screens."""
    size = 180
    img = Image.new("RGB", (size, size), BLACK)
    draw = ImageDraw.Draw(img)
    draw.rectangle([28, 28, size - 12, size - 12], fill=CYAN)
    draw.rectangle([12, 12, size - 28, size - 28], fill=BLACK, outline=YELLOW, width=8)
    f = font("consolab.ttf", 72)
    draw.text(((size - 16) / 2, (size - 16) / 2), "DB", font=f, fill=YELLOW, anchor="mm")
    img.save(ICON_OUT, "PNG", optimize=True)
    print(f"wrote {ICON_OUT.relative_to(REPO)}")


def make_og_card() -> None:
    """1200x630 card shown when the site is pasted into LinkedIn, Slack, email."""
    width, height = 1200, 630
    with Image.open(OG_SOURCE) as src:
        src = ImageOps.exif_transpose(src).convert("RGB")
        card = ImageOps.fit(src, (width, height), Image.LANCZOS, centering=(0.5, 0.5))

    # Darken the lower half so the type stays readable over the sparks.
    shade = Image.new("L", (width, height), 0)
    shade_draw = ImageDraw.Draw(shade)
    for y in range(height):
        # transparent at the top, ~78% black at the bottom
        shade_draw.line([(0, y), (width, y)], fill=int(200 * (y / height) ** 1.6))
    card = Image.composite(Image.new("RGB", (width, height), BLACK), card, shade)

    draw = ImageDraw.Draw(card)
    draw.text((72, 396), "DANIEL BRYARS", font=font("consolab.ttf", 76), fill=INK)
    draw.text((72, 486), "AI / ROBOTICS / SYSTEMS", font=font("consolab.ttf", 40), fill=YELLOW)
    draw.text((72, 540), "daniel.bryars.com", font=font("consola.ttf", 32), fill=CYAN)
    draw.rectangle([0, height - 12, width, height], fill=CYAN)

    card.save(OG_OUT, "JPEG", quality=88, optimize=True, progressive=True)
    print(f"wrote {OG_OUT.relative_to(REPO)}")


if __name__ == "__main__":
    make_icon()
    make_og_card()
