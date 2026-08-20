"""Add a build-spec block to each written-up project page.

The pages are strong on atmosphere and silent on engineering: a reader cannot
tell what motor, what steel, what process or what went wrong. This inserts a
consistent spec sheet just below the hero, with the field labels chosen per
project and the values left to be filled in by hand.

The screen bar reads DRAFT while any field is still a placeholder. When a page
is done, replace the values, drop class="tbc", and change DRAFT to LOGGED.
Find the remaining ones with:

    grep -l 'data-spec="draft"' cool-projects/*.html

    python tools/add_spec_sheets.py
"""

from __future__ import annotations

import re
import sys

from media_common import REPO, html_files

HERO_END_RE = re.compile(r"(</section>\n)", re.DOTALL)

# Field labels per project. Six rows keeps the block scannable; the labels are
# chosen so the answers are things a reader actually wants to know.
SPECS = {
    "DriftTrike.html": [
        "Frame", "Motor and drive", "Controller and battery",
        "Wheels and tyres", "Build time", "Cost",
    ],
    "CortenBalustrade.html": [
        "Material", "Sections", "Welding process",
        "Design check", "Run length", "Build time",
    ],
    "SpiralStairCase.html": [
        "Material", "Rise and going", "Fabrication",
        "Finish", "Regs and constraints", "Build time",
    ],
    "LatheSparks.html": [
        "Machine", "Workpiece", "Tooling",
        "Speeds and feeds", "Depth of cut", "Why it sparks",
    ],
    "MegaBookCase.html": [
        "Timber", "Dimensions", "Joinery",
        "Ladder hardware", "Finish", "Build time",
    ],
    "MotorisedStandingDesk.html": [
        "Timber", "Top dimensions", "Lifting frame",
        "Joinery", "Finish", "Build time",
    ],
    "CurvingSkirtingBoard.html": [
        "Timber", "Steam box", "Steam time",
        "Bend radius", "Springback", "Fixing method",
    ],
    "VintageStringLights.html": [
        "Bulbs", "Cable", "Fittings",
        "Run length", "Control and dimming", "Build time",
    ],
    "BellyBoard.html": [
        "Timber", "Dimensions", "Shaping",
        "Finish", "Where", "Time",
    ],
    "CVInABox.html": [
        "Box format", "Artwork", "Print process",
        "Contents", "Print run", "Cost per box",
    ],
    "RobotArm.html": [
        "Structure", "Joints and reduction", "Motors and control",
        "Bus and firmware", "Payload and reach", "Build time",
    ],
    "3DPrinters.html": [
        "Printers", "Modifications", "Materials",
        "Typical settings", "What it makes", "Running cost",
    ],
}

NOTES = {
    "DriftTrike.html": ("What went wrong", "What I would change"),
    "CortenBalustrade.html": ("What the FEA actually said", "What I would change"),
    "SpiralStairCase.html": ("The awkward bit", "What I would change"),
    "LatheSparks.html": ("Why hardened steel behaves like this", "What I would try next"),
    "MegaBookCase.html": ("What went wrong", "What I would change"),
    "MotorisedStandingDesk.html": ("What went wrong", "What I would change"),
    "CurvingSkirtingBoard.html": ("What went wrong", "What I would change"),
    "VintageStringLights.html": ("What went wrong", "What I would change"),
    "BellyBoard.html": ("What I learned", "What I would change"),
    "CVInABox.html": ("Did it work", "What I would change"),
    "RobotArm.html": ("Where the simulation lied", "What I would change"),
    "3DPrinters.html": ("What went wrong", "What I would change"),
}


def block(page_name: str) -> str:
    rows = "\n".join(
        f"""                        <div>
                            <dt>{label}</dt>
                            <dd class="tbc">&mdash;</dd>
                        </div>"""
        for label in SPECS[page_name]
    )
    first_note, second_note = NOTES[page_name]
    return f"""
            <section class="spec-sheet" data-spec="draft" aria-label="Build specification">
                <div class="screen-bar">
                    <span>BUILD SPEC</span>
                    <span>DRAFT</span>
                </div>
                <div class="spec-body">
                    <dl>
{rows}
                    </dl>
                    <div class="spec-notes">
                        <h3>{first_note}</h3>
                        <p class="tbc">To be written up.</p>
                        <h3>{second_note}</h3>
                        <p class="tbc">To be written up.</p>
                    </div>
                </div>
            </section>
"""


def main() -> int:
    changed = 0
    for page in html_files():
        if page.name not in SPECS:
            continue
        text = page.read_text(encoding="utf-8")
        if 'class="spec-sheet"' in text:
            print(f"  already has one: {page.relative_to(REPO)}")
            continue

        # Insert immediately after the hero section so the engineering is
        # visible before the reader has to scroll through the media.
        match = HERO_END_RE.search(text, text.index("<main"))
        if not match:
            print(f"  !! no hero section: {page.relative_to(REPO)}")
            continue

        insert_at = match.end()
        text = text[:insert_at] + block(page.name) + text[insert_at:]
        page.write_text(text, encoding="utf-8")
        changed += 1
        print(f"  spec {page.relative_to(REPO)}")

    print(f"{changed} page(s) updated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
