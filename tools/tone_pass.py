"""Thin out the jokes so the surviving ones land.

Nearly every heading and caption on the site was a wry one-liner, and several
reached for the same gag (objects "having opinions", things being "perfectly
normal X behaviour"). This flattens the weaker ones into plain description and
leaves the good ones alone.

Exact-string replacements, applied across every page. Anything already changed
by hand is simply skipped.

    python tools/tone_pass.py
"""

from __future__ import annotations

import sys

from media_common import REPO, html_files

REPLACEMENTS = {
    # --- Drift Trike ---------------------------------------------------------
    "<h2>Actual green welding, no impostors.</h2>":
        "<h2>First pass, seen through the filter.</h2>",
    "<h2>A tighter pass through green glass.</h2>":
        "<h2>A tighter, slower pass.</h2>",
    "<h2>Making bracket edges less objectionable.</h2>":
        "<h2>Deburring the bracket edges.</h2>",
    "<h2>Clean holes, because the bolts care.</h2>":
        "<h2>Clean holes for the mount bolts.</h2>",
    "<h2>Motor, axle and the useful end of the machine.</h2>":
        "<h2>Motor and axle assembly.</h2>",
    "<h2>Making the heavy wires behave.</h2>":
        "<h2>Making up the high-current wiring.</h2>",
    "<h2>Not just a frame with wheels.</h2>":
        "<h2>The electronics are half the build.</h2>",
    "<figcaption>The proper acceptance test.</figcaption>":
        "<figcaption>Lincoln on the grass, first proper run.</figcaption>",
    "<figcaption>Drive-end hardware doing the honest work.</figcaption>":
        "<figcaption>Motor, sprocket and axle at the drive end.</figcaption>",
    "<figcaption>Finished weld detail, post-green-glow.</figcaption>":
        "<figcaption>Finished weld on the frame.</figcaption>",
    "<figcaption>The welding filter earns its keep.</figcaption>":
        "<figcaption>The view through the welding filter.</figcaption>",

    # --- Corten balustrade ---------------------------------------------------
    "<h2>The kitchen was not finished. The steel was.</h2>":
        "<h2>Fabricating in a half-built house.</h2>",
    "<figcaption>Welding table in the unfinished kitchen. Normal house-building behaviour.</figcaption>":
        "<figcaption>The welding table lived in the unfinished kitchen for a while.</figcaption>",
    "<figcaption>A tiny maker&#x27;s mark, because obviously.</figcaption>":
        "<figcaption>A small maker&#x27;s mark on the end post.</figcaption>",
    "<figcaption>A tiny maker's mark, because obviously.</figcaption>":
        "<figcaption>A small maker's mark on the end post.</figcaption>",
    "<figcaption>The finished curve doing what curves do best: making straight lines feel slightly lazy.</figcaption>":
        "<figcaption>The finished curve, following the terrace edge.</figcaption>",
    "<figcaption>The last few fixings lined up, which is when a repetitive job starts to feel merciful.</figcaption>":
        "<figcaption>The last few posts, lined up ready to fix.</figcaption>",
    "<h2>A curved edge is not a straight problem.</h2>":
        "<h2>A curved edge is not a straight problem.</h2>",

    # --- Curving skirting board ---------------------------------------------
    "<figcaption>A steam box on the terrace, because the skirting board had chosen violence.</figcaption>":
        "<figcaption>A steam box on the terrace. Straight timber, curved wall, one option.</figcaption>",
    "<figcaption>Steam box on the terrace. Perfectly normal skirting-board behaviour.</figcaption>":
        "<figcaption>The steam box set up outside, well away from anything finished.</figcaption>",
    "<h2>Foil, hose, heat and optimism.</h2>":
        "<h2>Foil, hose, heat and a wallpaper stripper.</h2>",
    "<figcaption>Fixing it before springback has opinions.</figcaption>":
        "<figcaption>Fixed while still hot, before springback pulls it back.</figcaption>",
    "<figcaption>Small brass fitting, big responsibility.</figcaption>":
        "<figcaption>The brass steam inlet fitting.</figcaption>",
    "<h2>Offer it up before it changes its mind.</h2>":
        "<h2>Straight from the box to the wall.</h2>",

    # --- Spiral staircase ----------------------------------------------------
    "<figcaption>Finished detail, with timber trying to steal the photograph.</figcaption>":
        "<figcaption>Finished handrail detail against the pergola.</figcaption>",
    "<h2>Nothing is ever just one object.</h2>":
        "<h2>A stair is never just a stair.</h2>",

    # --- Mega bookcase -------------------------------------------------------
    "<figcaption>Provisional hero until the final beauty shots arrive. Still: a lot of bookcase.</figcaption>":
        "<figcaption>The finished wall, loaded.</figcaption>",
    "<figcaption>Loaded shelves, ladder still lurking nearby.</figcaption>":
        "<figcaption>Loaded shelves, ladder parked at the end of its rail.</figcaption>",
    "<figcaption>Ladder installed, room officially upgraded.</figcaption>":
        "<figcaption>The ladder installed on its rail.</figcaption>",
    "<figcaption>Because furniture can still have cables.</figcaption>":
        "<figcaption>Cable routing inside the console.</figcaption>",
    "<h2>Making the big flat bits behave.</h2>":
        "<h2>Breaking down the sheet goods.</h2>",
    "<h2>Obviously it needed a ladder.</h2>":
        "<h2>Then it needed a ladder.</h2>",

    # --- Vintage string lights ----------------------------------------------
    "<figcaption>Warm bulbs, black beams, twisted cable. Charm-per-amp successfully increased.</figcaption>":
        "<figcaption>Warm bulbs, black beams, twisted cable.</figcaption>",
    "<figcaption>The sky decided to join in.</figcaption>":
        "<figcaption>Lights on, just after sunset.</figcaption>",
    "<h2>Make the useful thing characterful.</h2>":
        "<h2>Lighting that earns its place.</h2>",

    # --- Lathe sparks --------------------------------------------------------
    "<figcaption>Hardened steel, CBN insert, old lathe, extremely unnecessary beauty.</figcaption>":
        "<figcaption>Hardened steel, CBN insert, and a lathe older than I am.</figcaption>",
    "<figcaption>Sideways spark weather.</figcaption>":
        "<figcaption>Sparks thrown sideways off the tool.</figcaption>",
    "<figcaption>Old-machine charm.</figcaption>":
        "<figcaption>The headstock.</figcaption>",

    # --- Belly board ---------------------------------------------------------
    "<figcaption>The correct natural habitat.</figcaption>":
        "<figcaption>The beach the course was built around.</figcaption>",
    "<figcaption>Course/shop atmosphere.</figcaption>":
        "<figcaption>Inside the workshop.</figcaption>",
    "<figcaption>Board racks and local colour.</figcaption>":
        "<figcaption>Board racks in the shop.</figcaption>",

    # --- Standing desk -------------------------------------------------------
    "<figcaption>Finished top, shared inspection, banana for scale. Engineering standards maintained.</figcaption>":
        "<figcaption>Finished top, with the obligatory banana for scale.</figcaption>",
    "<figcaption>Two-person measuring department.</figcaption>":
        "<figcaption>Measuring up, two pairs of hands.</figcaption>",
    "<h2>Useful, physical, shared.</h2>":
        "<h2>Why build one at all.</h2>",
}


def main() -> int:
    changed = 0
    hits = 0
    for page in html_files():
        text = page.read_text(encoding="utf-8")
        original = text
        for old, new in REPLACEMENTS.items():
            if old in text and old != new:
                text = text.replace(old, new)
                hits += 1
        if text != original:
            page.write_text(text, encoding="utf-8")
            changed += 1
            print(f"  tone {page.relative_to(REPO)}")

    print(f"{changed} page(s), {hits} replacement(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
