"""Put back the lines the rule-based passes should never have touched.

The earlier passes applied patterns - "objects do not have feelings", "headings
are labels", "cull the wry list-ender" - and rules cannot tell a joke that
makes a point from a joke that is just decoration. Daniel's correction:

    "A robot arm, because simulated robots are too well behaved."
    ->  "A robot arm, because simulated robots are ... well too perfect."

He did not want it deleted. He wanted the ending fixed. The test is not
"does this match a banned pattern" but "does this line make a point, and does
it sound like a person".

So: restored where the line carried an idea, sharpened where the idea was good
and the wording was the problem, and left flat where it really was decoration
("Sideways spark weather", "Course/shop atmosphere", "Old-machine charm").

    python tools/restore_pass.py
"""

from __future__ import annotations

import sys

from media_common import REPO, html_files
from textedit import apply_snippets

# current text -> restored text
RESTORE = {
    # --- Daniel's own rewrite ----------------------------------------------
    "<h1>Robot Arm</h1>":
        "<h1>A robot arm, because simulated robots are &hellip; well, too perfect.</h1>",

    # --- the printer-makes-more-problems joke, which he called gold ---------
    # I removed this twice while keeping the h1 that says the same thing.
    "<p>The MK4 printing joint parts for the arm. Most revisions cost an evening.</p>":
        "<p>The MK4, quietly manufacturing the next batch of problems. Most revisions cost an "
        "evening.</p>",
    "<figcaption>Orange plastic and black hardware, straight out of the box</figcaption>":
        "<figcaption>Orange plastic, black hardware, and the beginning of a very useful domestic "
        "manufacturing problem</figcaption>",
    "<figcaption>The MK4 printing robot-arm parts</figcaption>":
        "<figcaption>The MK4 earning its keep, printing robot-arm parts</figcaption>",

    # --- lines that carried an engineering point ---------------------------
    "<h2>Joints and reduction</h2>": "<h2>Torque is where the optimism runs out</h2>",
    "<h2>Wiring and control</h2>": "<h2>Six joints, six separate arguments</h2>",
    "<h2>Connectors and wiring</h2>": "<h2>Connectors are tiny commitments</h2>",
    "<h2>Learning its tolerances</h2>": "<h2>The machine teaches you its tolerances</h2>",
    "<h2>Kit to calibrated machine</h2>": "<h2>From flat-pack confidence to calibrated machine</h2>",
    "<h2>Setting out the curve</h2>": "<h2>A curved edge is not a straight problem</h2>",
    "<h2>Design and analysis</h2>": "<h2>Analysis, then sparks</h2>",
    "<h2>Cutting the slats</h2>": "<h2>Lots and lots of identical cuts</h2>",
    "<h2>Fabricating in a half-built house</h2>": "<h2>The kitchen was not finished. The steel was.</h2>",
    "<h2>Building the steam box</h2>": "<h2>First, build the timber sauna</h2>",
    "<h2>Final trimming</h2>": "<h2>Back to the workshop for the last persuasion</h2>",
    "<h2>The drawings live in a git repo</h2>": "<h2>The drawings live in a git repo, obviously</h2>",
    "<h2>Working around the window</h2>": "<h2>The window stayed in charge</h2>",
    "<h2>Shelves going in</h2>": "<h2>The moment it becomes a bookcase</h2>",
    "<h2>What it changed</h2>": "<h2>Furniture that changes the room</h2>",
    "<h2>Cutting curved steel</h2>": "<h2>Cutting the line you actually need</h2>",
    "<h2>The staircase it replaced</h2>": "<h2>The red staircase era</h2>",
    "<h2>What it had to fit around</h2>": "<h2>A stair is never only a stair</h2>",
    "<h2>Putting it together</h2>": "<h2>From bench problem to rolling object</h2>",
    "<h2>The finished trike</h2>": "<h2>The finished machine, before it gets muddy</h2>",
    "<h2>What it signals</h2>": "<h2>Memorable beats compliant</h2>",

    # --- MSc headings that were assertions, not decoration ------------------
    "<h2>Data structures</h2>": "<h2>Structure is information</h2>",
    "<h2>Runtime and growth</h2>": "<h2>Runtime has teeth</h2>",
    "<h2>Model comparison</h2>": "<h2>Not one magic classifier</h2>",
    "<h2>Cost-based evaluation</h2>": "<h2>Optimise the real objective</h2>",
    "<h2>Data and power</h2>": "<h2>Data has politics</h2>",
    "<h2>Regulation</h2>": "<h2>Law lags deployment</h2>",
    "<h2>Where it lands in practice</h2>": "<h2>Engineering needs a conscience</h2>",
    "<h2>The open-world assumption</h2>": "<h2>Absence is not falsehood</h2>",
    "<h2>Modelling is engineering</h2>": "<h2>Meaning needs engineering</h2>",
    "<h2>State representation</h2>": "<h2>The state is the interface</h2>",
    "<h2>Reward design</h2>": "<h2>Tell it what good means</h2>",
    "<h2>Training</h2>": "<h2>Training is an engineering problem</h2>",
    "<h2>Systems around the model</h2>": "<h2>The model is only part of the system</h2>",
    "<h1>Power and Consequences</h1>": "<h1>Power, Not Performance</h1>",

    # --- captions with a joke that lands ------------------------------------
    "<figcaption>The workshop end of the bench</figcaption>":
        "<figcaption>The Victorian inventor's shed, but with better stepper drivers</figcaption>",
    "<figcaption>The hero shot</figcaption>":
        "<figcaption>The hero shot. Gratuitous, yes. Wrong, no.</figcaption>",
    "<figcaption>Hardened steel, CBN insert, Colchester Chipmaster</figcaption>":
        "<figcaption>Hardened steel, CBN insert, and a lathe older than I am</figcaption>",
    "<figcaption>Extruder hardware detail</figcaption>":
        "<figcaption>Small hardware, big consequences</figcaption>",
    "<figcaption>Linear rails and printed brackets</figcaption>":
        "<figcaption>Linear motion, orange brackets, and the good kind of tolerances</figcaption>",
    "<figcaption>The control screen, mid-calibration</figcaption>":
        "<figcaption>The little screen of imminent calibration optimism</figcaption>",
    "<figcaption>The heated bed</figcaption>":
        "<figcaption>The heated bed, photographed with wholly unnecessary drama</figcaption>",
    "<figcaption>Printed brackets in the usual orange</figcaption>":
        "<figcaption>The orange bits doing a lot of visual heavy lifting</figcaption>",
    "<figcaption>Me, with the finished box</figcaption>":
        "<figcaption>The designer with the object, looking worryingly pleased with himself</figcaption>",
    "<figcaption>On the shelf</figcaption>": "<figcaption>On-shelf camouflage</figcaption>",
    "<figcaption>Frame, rods and toolhead</figcaption>":
        "<figcaption>Frame, rods and toolhead: the machine starting to look like itself</figcaption>",
    "<figcaption>Blank to board</figcaption>":
        "<figcaption>Blank to board: the nice bit where the shape starts looking inevitable</figcaption>",
    "<figcaption>Curved terrace, weathering steel, countryside view</figcaption>":
        "<figcaption>Curved terrace, weathering steel, countryside view. Not a bad place to "
        "over-engineer a railing.</figcaption>",
    "<figcaption>The foil-wrapped steam box</figcaption>":
        "<figcaption>The foil-wrapped timber sauna</figcaption>",
    "<figcaption>Tools ready before steaming</figcaption>":
        "<figcaption>Tools ready before the hot bit</figcaption>",
    "<figcaption>Curved wall, tools, next section</figcaption>":
        "<figcaption>Curved wall, tools, and the next awkward bit</figcaption>",
    "<figcaption>Final trimming pass</figcaption>":
        "<figcaption>Final persuasion pass</figcaption>",
    "<figcaption>Grinding to fit</figcaption>":
        "<figcaption>Grinding back towards the right answer</figcaption>",
    "<figcaption>Cutting curved steel</figcaption>":
        "<figcaption>Cutting curved steel, where straight thinking is only partly useful</figcaption>",
    "<figcaption>Boards and tools at the start</figcaption>":
        "<figcaption>Boards, tools and the early campaign</figcaption>",
    "<figcaption>The wall frame going up</figcaption>":
        "<figcaption>The wall frame taking over</figcaption>",
    "<figcaption>First glow</figcaption>":
        "<figcaption>First glow. Always a good moment.</figcaption>",
    "<figcaption>ROS and RViz: powerful, and a steep learning curve</figcaption>":
        "<figcaption>ROS and RViz: useful, powerful, and occasionally a character-building "
        "exercise</figcaption>",
    "<figcaption>Measuring up, two pairs of hands</figcaption>":
        "<figcaption>The two-person measuring department</figcaption>",
    "<figcaption>Cable routing inside the console</figcaption>":
        "<figcaption>Because furniture can still have cables</figcaption>",
    "<figcaption>The brass steam inlet fitting</figcaption>":
        "<figcaption>Small brass fitting, big responsibility</figcaption>",
    "<figcaption>Fixed while still hot, before springback pulls it back</figcaption>":
        "<figcaption>Fixed while still hot, before springback wins</figcaption>",
    "<figcaption>The last few posts, lined up ready to fix</figcaption>":
        "<figcaption>The last few posts. By now a repetitive job starts to feel merciful.</figcaption>",
    "<figcaption>The finished wall, loaded</figcaption>":
        "<figcaption>The finished wall, loaded. A lot of bookcase.</figcaption>",

    # --- sentences whose idea I threw out with the wording ------------------
    "The motor mount is the part that decides whether any of the rest works.":
        "The motor mount is where this stops being a toy-shaped idea.",
    "in a courtyard with no straight lines to measure from.":
        "and the kind of geometry that punishes optimism.",
    # "not the same thing as wrong" was killed by the ban on "not just X".
    # It is the best line on the page and it makes the argument.
    "A CV packaged like old software. Completely unnecessary, took far longer than writing\n"
    "                        a CV.":
        "A CV packaged like old software. Deeply unnecessary, which is not the same thing as\n"
        "                        wrong. It took far longer than writing a CV.",
    "<p>A physical CV packaged like old software. Completely unnecessary, and it took far longer "
    "than writing a CV would have.</p>":
        "<p>A physical CV packaged like old software. Deeply unnecessary, which is not the same "
        "thing as wrong.</p>",
    "<h2>Built, not yet written up</h2>": "<h2>Built, photographed badly, not yet written up</h2>",
    "<h2>The awkward bit between software and hardware.</h2>":
        "<h2>Not software. Not hardware. The awkward bit in between.</h2>",
    "<h2>Straight from the box to the wall</h2>":
        "<h2>Offer it up before it changes its mind</h2>",
    "<h2>Then it needed a ladder</h2>": "<h2>Obviously, it needed a ladder</h2>",
}


def main() -> int:
    changed = 0
    for page in html_files():
        original = page.read_text(encoding="utf-8")
        text = apply_snippets(original, RESTORE)
        if text != original:
            page.write_text(text, encoding="utf-8")
            changed += 1
            print(f"  restore {page.relative_to(REPO)}")

    print(f"{changed} page(s) updated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
