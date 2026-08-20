"""Cull the wry twist tacked onto the end of a list.

The move is: name three or four real things, then close with a joke.

    "...robot arms, ESP32s, 3D printers, inverted pendulums and things that
     usually need a better enclosure."

Daniel likes that one, which is exactly why it cannot be the shape of every
other sentence on the site. It was in most card descriptions, most captions and
a good share of the paragraphs, so the joke had stopped registering as a joke.

Kept, deliberately and spread out:

    "...inverted pendulums and things that usually need a better enclosure."   (CV)
    "Getting my son involved in building 'real things away from the virtual
     world' - awesome."                                                        (desk)
    "There is no lesson here. Posted because I want to, it looks awesome"      (lathe)
    "And yes, I also have a Myford. Obviously. Who does not need two lathes?"  (lathe)
    "Dangerous, frankly."                                                      (printers)
    "A bought-in railing would have taken an afternoon."                       (corten)
    "Curved walls are lovely. They also send you outside to build strange
     foil tubes."                                                              (skirting)
    "About forty times, for a job I had estimated at an afternoon."            (lights)
    "...before admitting it was a lot of work for a joke."                     (CV in a box)
    "...half a dozen things that were supposed to take one weekend."           (CV)

Everything else in the family is flattened to the plain version.

    python tools/cull_pass.py
"""

from __future__ import annotations

import sys

from media_common import REPO, html_files
from textedit import apply_paragraphs, apply_snippets

PARAGRAPHS = {
    # --- card descriptions, duplicated across index.html and the project index
    "Hardened steel, a CBN insert, an old Colchester Chipmaster, and absolutely no shortage of "
    "orange drama.":
        "Hardened steel, a CBN insert and an old Colchester Chipmaster.",

    "A wall-sized bookcase with console, full-height shelves, custom rolling ladder and an "
    "alarming number of sub-projects.":
        "A wall-sized bookcase with a low console, full-height shelves and a custom rolling ladder.",

    "A Christmas Prusa MK4 kit build: rods, frame, wiring, calibration detail and some thoroughly "
    "gratuitous printer glamour shots.":
        "A Christmas Prusa MK4 kit build: rods, frame, wiring and calibration.",

    "An electric drift trike build with motor-mount fabrication, controller wiring, welding-filter "
    "footage and a very important test driver.":
        "An electric drift trike. Motor-mount fabrication, controller wiring, and a lot of welding.",

    "Custom string lights with warm bulbs, twisted cable, workshop footage and a room that looks "
    "better for it.":
        "Custom string lights: warm filament bulbs, twisted cable and made fittings.",

    "Curved steel, courtyard constraints, handrail work and a finished stair that looks like it "
    "belongs there.":
        "Curved steel, courtyard constraints and handrail work.",

    "Because I built a house with curved walls: steam box, bent timber, wall fitting, and trim "
    "that had to follow a wall with no straight edge.":
        "I built a house with curved walls. Steam box, bent timber, and skirting that had to "
        "follow them.",

    "Ceefax-inspired pages, shipping forecast audio, old-computer charm and a healthy refusal to "
    "be beige.":
        "Ceefax-inspired pages, shipping forecast audio and old-computer charm.",

    "ESP32, reverse-engineered USB protocols, home automation, audio hardware and the occasional "
    "inverted pendulum.":
        "ESP32, reverse-engineered USB protocols, home automation and audio hardware.",

    "A ridiculous object that took a suspicious amount of effort, with the box art to prove it.":
        "A physical CV packaged like old software. Took far longer than writing one.",

    "A custom surfboard build with shape, craft, finish and likely more sanding than originally "
    "forecast.":
        "A custom surfboard build: shape, craft and finish.",

    "A custom lighting installation: design, wiring, atmosphere and making a space feel less "
    "ordinary.":
        "A custom lighting installation: design, wiring and atmosphere.",

    "A custom speed boat project. Hydrodynamics: when woodworking learns consequences.":
        "A custom speed boat. Hull, propulsion and rather more water than a bookcase.",

    "Robots, vehicles, furniture, electronics, simulations, strange presentation formats, retro "
    "computing experiments and workshop archaeology. Steel, timber, wire and code, in roughly that "
    "order of stubbornness.":
        "Robots, vehicles, furniture, electronics, simulations, retro computing experiments and "
        "workshop archaeology.",

    "A mix of recent AI work, robots, electronics, simulations and workshop builds. Some are "
    "polished, some are gloriously in-progress. That is part of the point.":
        "A mix of recent AI work, robots, electronics, simulations and workshop builds. Some are "
        "finished, some are not.",

    # --- project pages -----------------------------------------------------
    "Small domestic detail on the surface. Underneath: geometry, moisture, heat, timing, and the "
    "quiet terror of snapping it after all that work.":
        "Small domestic detail on the surface. Underneath: geometry, moisture, heat, timing, and a "
        "real chance of snapping it at the last moment.",

    "Electric drift trike. Fabrication, motor mounts, controller wiring, and the important "
    "requirement: it has to make a child grin while going sideways.":
        "Electric drift trike. Fabrication, motor mounts, controller wiring. It has to make a "
        "child grin while going sideways.",

    "Small machine, same thinking as a big one. Structure, drivetrain, wiring, controls, "
    "packaging, and making all of it survive vibration and enthusiastic use.":
        "Small machine, same thinking as a big one. Structure, drivetrain, wiring, controls, "
        "packaging. All of it has to survive vibration.",

    "Wall-sized bookcase. Built in sections, fitted round a window, extended into a low console, "
    "filled with books, then given a rolling ladder because shelves can always get more "
    "unreasonable.":
        "Wall-sized bookcase. Built in sections, fitted round a window, extended into a low "
        "console, filled with books, then given a rolling ladder.",

    "The ladder was not necessary. It became its own sub-project - rollers, brackets, rails - and "
    "an excuse to use the lathe for something that ends up in the living room.":
        "The ladder was not necessary. It became its own sub-project: rollers, brackets, rails and "
        "lathe work.",

    "Opening the boxes and finding the comforting promise of individually bagged parts.":
        "Opening the boxes. Everything individually bagged.",

    "Cable routing, controller wiring and the quiet hope that every connector is exactly where it "
    "should be.":
        "Cable routing and controller wiring.",

    "The finished MK4 on the bench, ready to become part of the rest of the workshop ecosystem.":
        "The finished MK4 on the bench.",

    "Won a competition, prize was a day course making a wooden belly board. Pleasingly specific. "
    "Part woodwork, part seaside engineering, part excuse to spend a day on a proper curve.":
        "Won a competition, prize was a day course making a wooden belly board. A blank, a shape "
        "to get right, and a day to do it in.",

    "String lights for the house. Twisted cable, warm filament bulbs, little made parts, ceiling "
    "beams, and enough workshop faff that buying them would have felt like surrender.":
        "String lights for the house. Twisted cable, warm filament bulbs, little made parts, "
        "ceiling beams.",

    "Bearings, printed lobes, fasteners and the little mechanical puzzle at the centre of the "
    "joint.":
        "Bearings, printed lobes and fasteners, laid out.",

    "Motor control on the bench. Cables, boards, meters, and the usual checking of what is "
    "actually moving.":
        "Motor control on the bench. Cables, boards, meters, and checking what is actually moving.",

    "A small protest against every application looking the same. The back lists the real things - "
    "software engineering, Linux, Python - as a 1990s feature list. Charming or a warning sign, "
    "not sure which.":
        "A small protest against every application looking the same. The back lists the real "
        "things - software engineering, Linux, Python - as a 1990s feature list.",

    "A height-adjustable desk built with my son: timber, test-fitting, short build clips and a "
    "great deal of sawdust.":
        "A height-adjustable desk built with my son: timber, test-fitting and short build clips.",

    "Phone footage, shot while working. Measuring, cutting, test-fitting, and a workshop in no "
    "state to be filmed.":
        "Phone footage, shot while working. Measuring, cutting, test-fitting.",
}

SNIPPETS = {
    # --- captions ----------------------------------------------------------
    "<figcaption>Orange plastic, black hardware and the beginning of a very useful domestic manufacturing problem</figcaption>":
        "<figcaption>Orange plastic and black hardware, straight out of the box</figcaption>",
    "<figcaption>Frame, rods and toolhead: the machine starting to look like itself</figcaption>":
        "<figcaption>Frame, rods and toolhead</figcaption>",
    "<figcaption>Small hardware, big consequences</figcaption>":
        "<figcaption>Extruder hardware detail</figcaption>",
    "<figcaption>Blank to board: the nice bit where the shape starts looking inevitable</figcaption>":
        "<figcaption>Blank to board</figcaption>",
    "<figcaption>Curved terrace, weathering steel, countryside view. Not a bad place to over-engineer a railing.</figcaption>":
        "<figcaption>Curved terrace, weathering steel, countryside view</figcaption>",
    "<figcaption>People, scale, and weathering steel doing its job</figcaption>":
        "<figcaption>People at the balustrade, for scale</figcaption>",
    "<figcaption>The foil-wrapped timber sauna</figcaption>":
        "<figcaption>The foil-wrapped steam box</figcaption>",
    "<figcaption>Tools ready before the hot bit</figcaption>":
        "<figcaption>Tools ready before steaming</figcaption>",
    "<figcaption>Curved wall, tools, and the next awkward bit</figcaption>":
        "<figcaption>Curved wall, tools, next section</figcaption>",
    "<figcaption>Final persuasion pass</figcaption>":
        "<figcaption>Final trimming pass</figcaption>",
    # These two were meant to go in an earlier pass but the keys still carried
    # a full stop that the caption clean-up had already removed.
    "<figcaption>Presented as if it belonged on a shelf next to machine learning books, which frankly it does</figcaption>":
        "<figcaption>On the shelf, next to the machine learning books</figcaption>",
    "<figcaption>Finished enough for the only test that matters: hand it to the test driver</figcaption>":
        "<figcaption>Finished enough to hand over to the test driver</figcaption>",
    "<figcaption>On-shelf camouflage</figcaption>": "<figcaption>On the shelf</figcaption>",
    "<figcaption>The control box living where the rider can actually use it</figcaption>":
        "<figcaption>Control box, within reach of the rider</figcaption>",
    "<figcaption>Finished top, sunlight, workshop chaos, father-and-son project energy</figcaption>":
        "<figcaption>Finished top, in the sun</figcaption>",
    "<figcaption>The Victorian inventor's shed, but with better stepper drivers</figcaption>":
        "<figcaption>The workshop end of the bench</figcaption>",
    "<figcaption>The MK4 earning its keep by printing robot-arm parts</figcaption>":
        "<figcaption>The MK4 printing robot-arm parts</figcaption>",
    "<figcaption>Finished black spiral staircase, tucked into the courtyard like it was always meant to be there</figcaption>":
        "<figcaption>The finished black spiral stair</figcaption>",
    "<figcaption>Grinding back towards the right answer</figcaption>":
        "<figcaption>Grinding to fit</figcaption>",
    "<figcaption>Cutting curved steel, where straight thinking is only partly useful</figcaption>":
        "<figcaption>Cutting curved steel</figcaption>",
    "<figcaption>The hero shot. Gratuitous, yes. Wrong, no.</figcaption>":
        "<figcaption>The hero shot</figcaption>",
    "<figcaption>Hardened steel, CBN insert, and a lathe older than I am</figcaption>":
        "<figcaption>Hardened steel, CBN insert, Colchester Chipmaster</figcaption>",
    "<figcaption>The wall of books doing its job</figcaption>":
        "<figcaption>The finished wall in use</figcaption>",
    "<figcaption>Boards, tools and the early campaign</figcaption>":
        "<figcaption>Boards and tools at the start</figcaption>",
    "<figcaption>The wall frame taking over</figcaption>":
        "<figcaption>The wall frame going up</figcaption>",
    "<figcaption>Parts laid out, plan becoming real</figcaption>":
        "<figcaption>Parts laid out</figcaption>",
    "<figcaption>First glow. Always a good moment.</figcaption>":
        "<figcaption>First glow</figcaption>",
    "<figcaption>ROS and RViz: useful, powerful, and occasionally a character-building exercise</figcaption>":
        "<figcaption>ROS and RViz: powerful, and a steep learning curve</figcaption>",
}


def main() -> int:
    changed = 0
    for page in html_files():
        original = page.read_text(encoding="utf-8")
        text = apply_paragraphs(original, PARAGRAPHS)
        text = apply_snippets(text, SNIPPETS)
        if text != original:
            page.write_text(text, encoding="utf-8")
            changed += 1
            print(f"  cull {page.relative_to(REPO)}")

    print(f"{changed} page(s) updated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
