"""Replace the notes-to-self bullet lists on the holding pages with real copy.

The bullets were an editorial checklist ("add build photos", "this should be a
visual page") rather than anything a reader wants. One honest sentence about
what the project is beats three instructions to a future editor.

    python tools/stub_copy.py
"""

from __future__ import annotations

import re
import sys

from media_common import REPO, html_files

LIST_RE = re.compile(r"\s*<ul>\s*(?:<li>.*?</li>\s*)+</ul>", re.DOTALL)

COPY = {
    "3DPrinters.html": (
        "Several printers, endlessly modified. They started as the project and ended up as "
        "the machine that makes the brackets, fixtures, enclosures and one-off parts for "
        "everything else on this list."
    ),
    "BenEater8BitComputer.html": (
        "A CPU on breadboards, built from Ben Eater's series: clock, registers, memory, bus "
        "and control logic. Nothing here is new to me in theory, which is exactly why wiring "
        "it up by hand was worth the weekend."
    ),
    "ClockProject.html": (
        "A clock, built as an object rather than a circuit with a display bolted on. The "
        "electronics were the easy half; the case, the typography and the decision about what "
        "it should do at 3am took much longer."
    ),
    "HiscotsLights.html": (
        "A lighting installation for a space that deserved better than a grid of downlights. "
        "Design constraints, a lot of cable, and a room that reads completely differently "
        "after dark."
    ),
    "MGEVProject.html": (
        "Living with an electric car and being unable to leave it alone: charging behaviour, "
        "home energy data, and the slow realisation that the interesting system is the one "
        "spanning vehicle, charger, tariff and house."
    ),
    "OtterSurfboard.html": (
        "A wooden surfboard from an Otter course: outline, shaping, glassing and finish. A "
        "physical object with real personality, and a reminder that removing material is a "
        "one-way operation."
    ),
    "RobotArm.html": (
        "A 3D-printed arm with closed-loop steppers over CAN, paired with MuJoCo simulation, "
        "OpenVR teleoperation, recorded datasets and PyTorch policies. The interesting part is "
        "the reality gap: calibration, resets, evaluation and the failures that only show up "
        "on hardware."
    ),
    "ShadowPrinting.html": (
        "An experiment in using light, shadow and geometry as a printing process. Playful, "
        "but with real constraints: the physics decides what is possible and the setup decides "
        "whether you can repeat it."
    ),
    "SpeedBoat.html": (
        "A boat, built to go fast, which is where woodworking stops being decorative and starts "
        "having opinions about hull shape, weight and water."
    ),
}


def main() -> int:
    changed = 0
    for page in html_files():
        copy = COPY.get(page.name)
        if not copy or "Still owed a write-up" not in page.read_text(encoding="utf-8"):
            continue
        text = page.read_text(encoding="utf-8")
        replacement = f"\n                    <p>{copy}</p>"
        updated = LIST_RE.sub(lambda _: replacement, text, count=1)
        if updated != text:
            page.write_text(updated, encoding="utf-8")
            changed += 1
            print(f"  copy {page.relative_to(REPO)}")

    print(f"{changed} page(s) updated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
