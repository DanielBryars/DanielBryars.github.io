"""Flatten the restored lines that were not actually funny.

Daniel's instruction after reviewing 21 of them by hand: "Flatten them unless
they are witty and funny, any you are unsure of ask me."

So this is a triage, not a rule. Anything that raised a smile stays; anything
that was merely flavoured - an aphorism, a mild bit of colour, a phrase doing
the job of a label - goes plain. The genuinely borderline ones were put to him
separately rather than guessed at.

Kept as witty, for the record: "First, build the timber sauna" / "The drawings
live in a git repo, obviously" / "Offer it up before it changes its mind" /
"The window stayed in charge" / "Obviously, it needed a ladder" / "The red
staircase era" / "The finished machine, before it gets muddy" / "Six joints,
six separate arguments" / "Built, photographed badly, not yet written up" /
"Orange plastic, black hardware, and the beginning of a very useful domestic
manufacturing problem" / "The heated bed, photographed with wholly unnecessary
drama" / "The orange bits doing a lot of visual heavy lifting" / "Curved
terrace... Not a bad place to over-engineer a railing." / "The foil-wrapped
timber sauna" / "Final persuasion pass" / "ROS and RViz: ...occasionally a
character-building exercise" / "The two-person measuring department" / "The
last few posts. By now a repetitive job starts to feel merciful." / "The
finished wall, loaded. A lot of bookcase." / "On-shelf camouflage" / "The motor
mount is where this stops being a toy-shaped idea." / "...geometry that
punishes optimism."

    python tools/triage_pass.py
"""

from __future__ import annotations

import sys

from media_common import REPO, html_files
from textedit import apply_snippets

FLATTEN = {
    # --- headings: aphorisms and labels wearing a hat ----------------------
    "<h2>The machine teaches you its tolerances</h2>": "<h2>Learning its tolerances</h2>",
    "<h2>Lots and lots of identical cuts</h2>": "<h2>Cutting the slats</h2>",
    "<h2>The moment it becomes a bookcase</h2>": "<h2>Shelves going in</h2>",
    "<h2>Furniture that changes the room</h2>": "<h2>What it changed</h2>",
    "<h2>Cutting the line you actually need</h2>": "<h2>Cutting curved steel</h2>",
    "<h2>A stair is never only a stair</h2>": "<h2>What it had to fit around</h2>",
    "<h2>From bench problem to rolling object</h2>": "<h2>Putting it together</h2>",

    # --- captions: colour without a joke ------------------------------------
    "<figcaption>The MK4 earning its keep, printing robot-arm parts</figcaption>":
        "<figcaption>The MK4 printing robot-arm parts</figcaption>",
    "<figcaption>Small hardware, big consequences</figcaption>":
        "<figcaption>Extruder hardware detail</figcaption>",
    "<figcaption>Frame, rods and toolhead: the machine starting to look like itself</figcaption>":
        "<figcaption>Frame, rods and toolhead</figcaption>",
    "<figcaption>Blank to board: the nice bit where the shape starts looking inevitable</figcaption>":
        "<figcaption>Blank to board</figcaption>",
    "<figcaption>Tools ready before the hot bit</figcaption>":
        "<figcaption>Tools ready before steaming</figcaption>",
    "<figcaption>Curved wall, tools, and the next awkward bit</figcaption>":
        "<figcaption>Curved wall, tools, next section</figcaption>",
    "<figcaption>Grinding back towards the right answer</figcaption>":
        "<figcaption>Grinding to fit</figcaption>",
    "<figcaption>Cutting curved steel, where straight thinking is only partly useful</figcaption>":
        "<figcaption>Cutting curved steel</figcaption>",
    "<figcaption>Boards, tools and the early campaign</figcaption>":
        "<figcaption>Boards and tools at the start</figcaption>",
    "<figcaption>The wall frame taking over</figcaption>":
        "<figcaption>The wall frame going up</figcaption>",
    "<figcaption>First glow. Always a good moment.</figcaption>":
        "<figcaption>First glow</figcaption>",
    "<figcaption>Because furniture can still have cables</figcaption>":
        "<figcaption>Cable routing inside the console</figcaption>",
    "<figcaption>Small brass fitting, big responsibility</figcaption>":
        "<figcaption>The brass steam inlet fitting</figcaption>",
}


def main() -> int:
    changed = 0
    for page in html_files():
        original = page.read_text(encoding="utf-8")
        text = apply_snippets(original, FLATTEN)
        if text != original:
            page.write_text(text, encoding="utf-8")
            changed += 1
            print(f"  triage {page.relative_to(REPO)}")

    print(f"{changed} page(s) updated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
