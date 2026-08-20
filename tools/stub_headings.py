"""Give each holding page its own heading and footer line.

Nine pages carrying the identical joke is how a running gag stops being one.

    python tools/stub_headings.py
"""

from __future__ import annotations

import re
import sys

from media_common import REPO, html_files

HEADINGS = {
    "3DPrinters.html": ("Machines that make the other machines.", "Printers, mods and a lot of brackets."),
    "BenEater8BitComputer.html": ("A CPU you can point at.", "Breadboards, LEDs and first principles."),
    "ClockProject.html": ("An object, not a circuit with a display.", "Electronics, enclosure, typography."),
    "HiscotsLights.html": ("A room that changes after dark.", "Lighting design and a lot of cable."),
    "MGEVProject.html": ("The car turned out to be the small part.", "Vehicle, charger, tariff and house."),
    "OtterSurfboard.html": ("Wood, water, and no undo button.", "Outline, shaping, glassing, finish."),
    "RobotArm.html": ("Where the simulation stops agreeing.", "CAN steppers, MuJoCo, teleoperation, policies."),
    "ShadowPrinting.html": ("Light doing the printing.", "Optics, geometry and repeatability."),
    "SpeedBoat.html": ("Hydrodynamics, learned the direct way.", "Hull shape, weight and water."),
}

H2_RE = re.compile(r"<h2>Built\. Photographed badly\. Still owed a write-up\.</h2>")
FOOTER_RE = re.compile(r"<span>Project notes waiting for the good bits\.</span>")


def main() -> int:
    changed = 0
    for page in html_files():
        entry = HEADINGS.get(page.name)
        if not entry:
            continue
        heading, footer = entry
        text = page.read_text(encoding="utf-8")
        updated = H2_RE.sub(f"<h2>{heading}</h2>", text)
        updated = FOOTER_RE.sub(f"<span>{footer}</span>", updated)
        if updated != text:
            page.write_text(updated, encoding="utf-8")
            changed += 1
            print(f"  heading {page.relative_to(REPO)}")

    print(f"{changed} page(s) updated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
