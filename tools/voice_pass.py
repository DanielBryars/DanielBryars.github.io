"""Break the heading template and de-flourish the prose.

The site had one voice move and used it everywhere: a short declarative
fragment ending in a full stop, as a heading, roughly 150 times. Individually
fine; in bulk it reads as generated, because no person writes that evenly.

Three things happen here:

1. Captions become labels. A single-sentence <figcaption> loses its terminal
   full stop, which is ordinary editorial practice and instantly removes half
   the drumbeat.
2. Most epigram headings become plain labels naming the thing. A curated
   handful survive, spread across the site, so the ones that remain read as
   deliberate.
3. The stock constructions go: "not just X, it is Y", objects given feelings,
   and paragraphs that describe the category of a thing rather than the thing.

Where a rewrite would need a fact I do not have - a ratio, a timber, a
current - the sentence is cut rather than padded. Short and true beats long
and vague, and the BUILD SPEC blocks are where the numbers belong.

    python tools/voice_pass.py
"""

from __future__ import annotations

import re
import sys
import textwrap

from media_common import REPO, html_files

# --------------------------------------------------------------------------
# 1. Captions become labels
# --------------------------------------------------------------------------

CAPTION_RE = re.compile(r"<figcaption>([^<]+)</figcaption>")
SENTENCE_BREAK_RE = re.compile(r"[.?!]\s")


def delabel_captions(text: str) -> str:
    def fix(match: re.Match) -> str:
        caption = match.group(1).strip()
        # Leave anything that is really two sentences; the rhythm there is fine.
        if SENTENCE_BREAK_RE.search(caption) or not caption.endswith("."):
            return match.group(0)
        return f"<figcaption>{caption[:-1]}</figcaption>"

    return CAPTION_RE.sub(fix, text)


# --------------------------------------------------------------------------
# 2. Headings
# --------------------------------------------------------------------------
# Keeping a heading's full stop is now a deliberate choice. The ones left
# alone are listed at the bottom of this file so the count stays honest.

HEADINGS = {
    # --- 3D printers -------------------------------------------------------
    "From flat-pack confidence to calibrated machine.": "Kit to calibrated machine",
    "Square matters.": "Getting the frame square",
    "Connectors are tiny commitments.": "Connectors and wiring",
    "Prototype velocity.": "What it is actually for",
    # --- Belly board -------------------------------------------------------
    "A day in a surf workshop.": "A day in the workshop",
    # --- Corten balustrade -------------------------------------------------
    "FEA before committing to steel.": "FEA before cutting steel",
    "Lots of identical cuts.": "Cutting the slats",
    "A curved edge is not a straight problem.": "Setting out the curve",
    "Analysis, then sparks.": "Design and analysis",
    "Fabricating in a half-built house.": "Fabricating in a half-built house",
    # --- Curving skirting board -------------------------------------------
    "First, make the timber sauna.": "Building the steam box",
    "Foil, hose, heat and a wallpaper stripper.": "Foil, hose, heat and a wallpaper stripper",
    "Straight from the box to the wall.": "Straight from the box to the wall",
    "The curve becomes part of the wall.": "Fixing the curve",
    "Back to the workshop for the last persuasion.": "Final trimming",
    "The drawings live in a repo, obviously.": "The drawings live in a git repo",
    "It looks like a normal detail.": "The finished detail",
    # --- CV in a box -------------------------------------------------------
    "Boxed software design.": "The design video",
    "Memorable beats compliant.": "What it signals",
    "Design files and source material.": "Design files and source material",
    "Shelf test passed.": "The shelf test",
    # --- Drift trike -------------------------------------------------------
    "The acceptance test.": "The acceptance test",
    "Lincoln fitting the wheels.": "Lincoln fitting the wheels",
    "Tapping a thread, properly.": "Tapping a thread",
    "Motor electronics on the bench.": "Motor electronics on the bench",
    "Making up the high-current wiring.": "Making up the high-current wiring",
    "Bench-testing the control box.": "Bench-testing the control box",
    "What the welder actually sees.": "What the welder actually sees",
    "First pass, seen through the filter.": "Seen through the filter",
    "A tighter, slower pass.": "A tighter, slower pass",
    "Helmet on, drivetrain visible.": "Welding, wider shot",
    "Sparks down, trike frame on the bench.": "Cutting the frame",
    "Deburring the bracket edges.": "Deburring the bracket edges",
    "Clean holes for the mount bolts.": "Clean holes for the mount bolts",
    "Motor and axle assembly.": "Motor and axle assembly",
    "From bench problem to rolling object.": "Putting it together",
    "The finished machine, before it gets muddy.": "The finished trike",
    "Small vehicle, full stack.": "Small vehicle, full stack",
    "Order of operations.": "Order of operations",
    "The electronics are half the build.": "The electronics are half the build",
    # --- Lathe sparks ------------------------------------------------------
    "The spark ring.": "The spark ring",
    "Old iron, modern insert.": "Old iron, modern insert",
    # --- Mega bookcase -----------------------------------------------------
    "From panels to a wall of shelves.": "From panels to a wall of shelves",
    "Breaking down the sheet goods.": "Breaking down the sheet goods",
    "Laser lines and tall uprights.": "Laser lines and tall uprights",
    "The moment it becomes a bookcase.": "Shelves going in",
    "The low cabinet under the wall of books.": "The low cabinet",
    "Roller hardware on the lathe.": "Roller hardware on the lathe",
    "Ladder frame in the workshop.": "Ladder frame in the workshop",
    "Layout before commitment.": "Layout before commitment",
    "The window stayed in charge.": "Working around the window",
    "Then it needed a ladder.": "Then it needed a ladder",
    "Furniture that changes the room.": "What it changed",
    # --- Standing desk -----------------------------------------------------
    "Turning the idea into an actual desk.": "Building the top",
    "The desk starts looking like a desk.": "The desk starts looking like a desk",
    "Why build one at all.": "Why build one at all",
    "Building with my son.": "Building with my son",
    # --- MSc: Algorithms ---------------------------------------------------
    "Structure is information.": "Data structures",
    "Runtime has teeth.": "Runtime and growth",
    "Clarity scales.": "What stuck",
    # --- MSc: Data mining and text analytics -------------------------------
    "Persona as a variable.": "Persona as a variable",
    "Testing for drift.": "Measuring drift",
    "Text analytics meets LLMs.": "Text analytics and LLMs",
    "From tokens to transformers.": "From tokens to transformers",
    # --- MSc: Data science -------------------------------------------------
    "Fraud prediction.": "Fraud prediction",
    "Not one magic classifier.": "Model comparison",
    "Optimise the real objective.": "Cost-based evaluation",
    # --- MSc: Deep learning ------------------------------------------------
    "Caption generation.": "Caption generation",
    "PyTorch all the way down.": "Encoder, decoder, training loop",
    "Debug the representation.": "Debugging the representation",
    # --- MSc: Ethics -------------------------------------------------------
    "Data has politics.": "Data and power",
    "Law lags deployment.": "Regulation",
    "Engineering needs a conscience.": "What stuck",
    # --- MSc: KRR ----------------------------------------------------------
    "Absence is not falsehood.": "The open-world assumption",
    "Logic with consequences.": "Lean and Prolog",
    "Meaning needs engineering.": "What stuck",
    # --- MSc: Machine learning ---------------------------------------------
    "Orbital regression.": "Orbital regression",
    "MLP versus GPR.": "MLP versus GPR",
    "Inductive bias matters.": "Inductive bias",
    # --- MSc: MLX course projects ------------------------------------------
    "Six weeks of building the bits.": "Six Weeks of Building the Bits",
    "Training is an engineering problem.": "Training",
    "Vision, language and sound.": "Vision, language and sound",
    "The model is only part of the system.": "Systems around the model",
    "A practical bridge between the MSc and robot-learning work.":
        "A practical bridge between the MSc and robot-learning work",
    # --- MSc: Programming for data science ---------------------------------
    "Book signatures.": "Book signatures",
    "Python as workshop kit.": "Python as workshop kit",
    "Practical data judgement.": "What stuck",
    # --- MSc: Robotics -----------------------------------------------------
    "TurtleBot reinforcement learning.": "TurtleBot reinforcement learning",
    "The state is the interface.": "State representation",
    "Tell it what good means.": "Reward design",
    # --- MSc AI index ------------------------------------------------------
    "The useful reset.": "The useful reset",
    "From sandwiches to robots.": "From sandwiches to robots",
    "AI with engineering instincts.": "What it changed",
    # --- Robot arm ---------------------------------------------------------
    "Printing the hard bits first.": "Printed structure",
    "Torque is where optimism goes to be tested.": "Joints and reduction",
    "Every joint wants its own little argument.": "Wiring and control",
    "A physical test bed for learning.": "What it is for",
    "Print, assemble, wire, test, rethink.": "Print, assemble, wire, test, rethink",
    # --- Spiral staircase --------------------------------------------------
    "The red staircase era.": "The staircase it replaced",
    "Grinding, checking, adjusting.": "Grinding, checking, adjusting",
    "Cutting the line you actually need.": "Cutting curved steel",
    "Measure, cut, offer up, repeat.": "Measure, cut, offer up, repeat",
    "A stair is never just a stair.": "What it had to fit around",
    # --- Vintage string lights ---------------------------------------------
    "Small parts, lots of repetition.": "Small parts, lots of repetition",
    "Testing the first glow.": "Testing the first glow",
    "Threading the room.": "Threading the room",
    "Lighting that earns its place.": "Why bother",
    "Wires, blocks and bulb holders.": "Wires, blocks and bulb holders",
    # --- About / index -----------------------------------------------------
    "Three things I keep coming back to.": "Three things I keep coming back to",
    "Built, photographed badly, not yet written up.": "Built, not yet written up",
    "Projects with photos, clips and the build story.":
        "Projects with photos, clips and the build story",
}

# Headings deliberately left as epigrams, for the record:
#   The machine teaches you its tolerances. / Simple shape, real judgement.
#   From box section to balustrade. / It became part of the place.
#   Straight timber, curved house. / Heat buys time. / Because a PDF is obedient.
#   Small, hot, slightly hypnotic. / Slow motion swarf therapy.
#   The unglamorous bit that decides whether it works. / Measured in sideways motion.
#   None, almost. / The project inside the project. / A room-sized tolerance stack.
#   Proofs before vibes. / Style can move meaning. / The Muppet test.
#   False positives hurt too. / Language metrics are slippery.
#   Correct systems can still be wrong. / Define "sandwich".
#   Pretty plots were not enough. / Build it close enough to feel it.
#   Data is never "just there". / Robots are unfair to abstractions.
#   Less magic, more mechanism. / Curves are unforgiving. / It should look inevitable.
#   How hard can it be? Then finding out properly.
# ...plus one per holding page. That is roughly 30 across 35 pages.

HEADING_TAG_RE = re.compile(r"<(h[123])>([^<]+)</\1>")


def relabel_headings(text: str) -> str:
    def fix(match: re.Match) -> str:
        tag, heading = match.group(1), match.group(2).strip()
        replacement = HEADINGS.get(heading)
        if replacement is None:
            return match.group(0)
        return f"<{tag}>{replacement}</{tag}>"

    return HEADING_TAG_RE.sub(fix, text)


# --------------------------------------------------------------------------
# 3. Prose
# --------------------------------------------------------------------------
# Keyed on the paragraph with its whitespace collapsed, so indentation and
# line wrapping in the source do not matter.

PARAGRAPHS = {
    # --- about -------------------------------------------------------------
    "I like knowing whether a system is genuinely better, not just whether the graph looks nicer.":
        "I want to know whether a system is actually better, not whether the graph looks nicer.",

    # --- 3D printers -------------------------------------------------------
    "Bed, nozzle, belts and axes all become part of a feedback loop. It is not just assembly; it is "
    "learning how the machine reports its own state.":
        "Bed, nozzle, belts and axes are all part of one feedback loop. Assembling it is the easy "
        "half; the useful half is learning how the machine reports its own state, and which of "
        "those reports to believe.",

    # --- Ben Eater ---------------------------------------------------------
    "A CPU on breadboards, built from Ben Eater's series: clock, registers, memory, bus and control "
    "logic. Nothing here is new to me in theory, which is exactly why wiring it up by hand was "
    "worth the weekend.":
        "A CPU on breadboards, built from Ben Eater's series: clock, registers, memory, bus and "
        "control logic. None of it was new to me in theory. Wiring it up by hand was still worth "
        "the weekend.",

    # --- Corten balustrade -------------------------------------------------
    "The nicest photos are not just the fabrication shots; they are the ones where people are "
    "leaning on it, talking, looking out across the fields. That is when the object stops being a "
    "project and starts being part of the house.":
        "My favourite photos of it are not the fabrication shots. They are the ones with people "
        "leaning on it, talking, looking out across the fields.",

    # --- Curving skirting board -------------------------------------------
    "The problem was not just bending the skirting. It was getting heat and moisture into a long "
    "piece of timber evenly enough that it could be persuaded around the wall without splitting, "
    "springing back, or becoming expensive firewood.":
        "Bending the skirting was the easy part to describe and the hard part to do. Heat and "
        "moisture have to get into a long piece of timber evenly, or it splits, springs back, or "
        "becomes expensive firewood.",

    # --- MSc: Algorithms ---------------------------------------------------
    "The practical value was learning to explain not just what a program does, but why it "
    "terminates, why it is correct and where it will fail.":
        "The practical value was learning to explain why a program terminates, why it is correct, "
        "and where it will fail - rather than only what it does.",

    # --- MSc: Data mining --------------------------------------------------
    "That made the research question feel much less abstract. Persona choice is not just tone of "
    "voice; it can become an editorial layer.":
        "That made the research question concrete. Persona choice looks like tone of voice and "
        "behaves like an editorial layer.",

    # --- MSc: MLX ----------------------------------------------------------
    "Alongside the MSc, I worked through a six-week practical AI course and kept a set of public "
    "GitHub projects. The useful part was not just getting models to run; it was implementing the "
    "pieces closely enough to understand where the behaviour came from.":
        "Alongside the MSc, I worked through a six-week practical AI course and kept the projects "
        "public on GitHub. Getting a model to run teaches you very little. Implementing the pieces "
        "closely enough to see where the behaviour comes from teaches you most of it.",

    # --- MSc: Programming for data science ---------------------------------
    "The useful lesson was not just syntax. It was how quickly data work becomes systems work: "
    "file formats, storage, repeatability, runtime, provenance and the small decisions that make "
    "an analysis trustworthy.":
        "The useful lesson was how quickly data work turns into systems work: file formats, "
        "storage, repeatability and provenance decide whether anyone should trust the analysis.",

    # --- Robot arm ---------------------------------------------------------
    "This one is not finished, which is partly the point. It is a home-built robot-arm platform "
    "for learning where the real difficulty lives: printed mechanics, reducers, bearings, servo "
    "drives, wiring, calibration, control and eventually robot-learning experiments on hardware "
    "that can actually sulk.":
        "A home-built arm for running robot-learning experiments on something that is not a "
        "simulator. Printed structure, cycloidal reducers, servo drives, and the wiring and "
        "calibration that a simulated robot never makes you think about. It is unfinished, and "
        "will probably stay that way for a while.",

    "The build uses printed structural parts and joint components, which makes iteration fast but "
    "also forces the awkward questions early: stiffness, backlash, fit, tolerances and where "
    "plastic stops being charming.":
        "Structure and joints are printed, so a revision costs an evening rather than a machine "
        "shop. The trade is stiffness: printed parts flex, and flex shows up as position error at "
        "the end of a long arm.",

    "Servo motors and compact reducers are the bridge between a CAD idea and a useful arm. The "
    "cycloidal sections are especially interesting because they turn the project into a mechanical "
    "experiment, not just an assembly exercise.":
        "Each joint uses a printed cycloidal reducer rather than a belt drive or a bought harmonic "
        "drive: high ratio, compact, and printable at home. The cost is backlash, which I have not "
        "measured properly yet.",

    "The electronics and wiring work is about making motion controllable and repeatable. That "
    "means motor drives, feedback, connectors, power, signal integrity and enough instrumentation "
    "to know whether the problem is code, mechanics or a tiny connector being dramatic.":
        "Motor drives, position feedback, power and connectors, per joint, routed through a moving "
        "structure. The part worth building carefully is the instrumentation: without it, a bad "
        "connector and a bad control loop look identical.",

    "It connects directly to my MSc and robot-learning work: MuJoCo simulation, OpenVR "
    "teleoperation, data capture, policy training and the persistent question of what transfers "
    "when the robot is no longer made of perfect maths.":
        "It picks up directly from my MSc work - MuJoCo simulation, OpenVR teleoperation, data "
        "capture, policy training - and asks the one question a simulator cannot answer: how much "
        "of this survives contact with a real, slightly wrong machine?",

    "The end goal is not just a nice moving sculpture. It is a platform for testing policies, "
    "collecting data, comparing simulation with hardware, and discovering the reality gap in the "
    "least theoretical way possible.":
        "The point is to have somewhere to run policies that were trained in MuJoCo and find out "
        "what the simulator was wrong about. Reality gap, measured rather than discussed.",

    # --- Drift trike -------------------------------------------------------
    "Before anything gets ridden, the drive system has to behave as a system: motor, chain, "
    "controller, wiring, display and all the small choices that decide whether power becomes "
    "motion or just an educational smell.":
        "Motor, chain, controller, wiring and display, run together on the bench before any of it "
        "goes near a rider. This is the cheap place to find out that a connector is undersized.",

    "The controller and wiring are part of the build, not an afterthought. The fun bit only works "
    "because the quiet electrical details behave when the machine starts moving.":
        "The controller and wiring took about as long as the frame. Vibration, chafe and connector "
        "choice are what decide whether it still works on the tenth run rather than the first.",

    # --- Standing desk -----------------------------------------------------
    "I like projects where the result has to survive real use. This one mixed the pleasant "
    "practical stuff of furniture making with the more systems-minded work of fitting a "
    "height-adjustable frame into something that should quietly behave itself every day.":
        "I like projects that have to survive daily use. This one is half furniture making and "
        "half fitting a motorised frame to a top heavy enough to need it, in a way that still "
        "works after a thousand cycles.",

    # --- Spiral staircase --------------------------------------------------
    "The finished stair looks calm, which is usually a sign that the difficult bits have been "
    "hidden properly. Getting there meant measuring, cutting, grinding, test-fitting and making "
    "old-house constraints behave like they were part of the plan.":
        "The finished stair looks calm, which usually means the difficult bits are well hidden. "
        "Getting there was measuring, cutting, grinding and test-fitting against a courtyard that "
        "was already built and nowhere near square.",

    # --- Vintage string lights ---------------------------------------------
    "The point was not just illumination. It was to make the room feel warmer and more personal, "
    "with the cables and bulbs sitting comfortably among the steel beams, timber and general "
    "house-built-by-someone-who-keeps-tools-nearby atmosphere.":
        "Off-the-shelf lighting would have lit the room. These make it feel like somewhere "
        "specific, with the cable and bulbs sitting comfortably against the steel beams and "
        "timber.",
}

# Captions that carry the same tics.
CAPTIONS = {
    "The 3D printer quietly manufacturing future problems, which is exactly why it is useful.":
        "The MK4 printing parts for the arm",
    "Printed parts, bearings, reducers and that optimistic phrase: it should work.":
        "Printed parts, bearings and a cycloidal reducer, part-assembled",
    "The natural habitat: parts, tools, machines, cables and at least three things asking to be "
    "calibrated.":
        "The bench it lives on",
    "Printed part, fresh from the bed, before reality has had its say.":
        "A joint part straight off the bed, before cleanup",
    "Rods and fasteners: small things that decide whether big things move properly.":
        "Rods and fasteners for the joints",
    "Joint assemblies side by side, because one axis is never enough.":
        "Two joint assemblies side by side",
    "The little screen of imminent calibration optimism.":
        "The control screen, mid-calibration",
    "The heated bed, photographed with wholly unnecessary drama.":
        "The heated bed",
    "The orange bits are doing a lot of visual heavy lifting, and I approve.":
        "Printed brackets in the usual orange",
    "The designer with the object, looking worryingly pleased with himself.":
        "Me, with the finished box",
}

# Odds and ends: page titles, video-strip blurbs and half-sentences that carry
# the same constructions but do not sit in a paragraph or a caption.
SNIPPETS = {
    "<h1>A robot arm, because simulated robots are too well behaved.</h1>":
        "<h1>Robot Arm</h1>",
    "<h1>Building the printer that prints the next problem.</h1>":
        "<h1>3D Printer Build</h1>",
    "<h1>Power, Not Just Performance</h1>":
        "<h1>Power and Consequences</h1>",
    "<h2>Not just software. Not just hardware. The awkward bit in between.</h2>":
        "<h2>The awkward bit between software and hardware.</h2>",
    "<p>The 3D printer quietly manufacturing future problems, which is exactly why it is useful.</p>":
        "<p>The MK4 printing joint parts for the arm. Most revisions cost an evening.</p>",
    "walls and pergola posts, and the kind of geometry that quietly punishes optimism.":
        "walls and pergola posts, in a courtyard with no straight lines to measure from.",
    "<figcaption>Prompted text transformation became part of the subject, not just a convenient tool</figcaption>":
        "<figcaption>Prompted text transformation as the object of study rather than the tool</figcaption>",
    "<figcaption>Prompted text transformation as an object of study, not just a convenience</figcaption>":
        "<figcaption>Comparing prompted rewrites of the same source text</figcaption>",
    "<figcaption>Making the steam connection behave</figcaption>":
        "<figcaption>Fitting the steam inlet</figcaption>",
    "<span>Steam bending, curved walls and a domestic detail that fought back.</span>":
        "<span>Steam bending, curved walls, and skirting that had to follow them.</span>",
    "wall fitting and domestic trim that fought back.":
        "wall fitting, and trim that had to follow a wall with no straight edge.",
    "The motor mount is where this stops being a toy-shaped idea and becomes a mechanical system.":
        "The motor mount is the part that decides whether any of the rest works.",

    # Relabelling headings to plain nouns collided with the eyebrow above them
    # ("Assembly" over "Assembly" reads like a bug). These carry an already
    # relabelled page to the final wording; from a clean run the HEADINGS table
    # produces these directly.
    "<h2>Learning to tap a thread</h2>": "<h2>Tapping a thread</h2>",
    "<h2>First pass, seen through the filter</h2>": "<h2>Seen through the filter</h2>",
    "<h2>Plasma cutting the frame</h2>": "<h2>Cutting the frame</h2>",
    "<h2>Assembly</h2>": "<h2>Putting it together</h2>",
    "<h2>Walkaround</h2>": "<h2>The finished trike</h2>",
    "<h2>The console</h2>": "<h2>The low cabinet</h2>",
    "<h2>Complexity</h2>": "<h2>Runtime and growth</h2>",
    "<h2>Implementation</h2>": "<h2>Encoder, decoder, training loop</h2>",
    "<h2>Formal tools</h2>": "<h2>Lean and Prolog</h2>",
}

PARAGRAPH_RE = re.compile(r"([ \t]*)<p>(?!<)(.*?)</p>", re.DOTALL)


def rewrite_prose(text: str) -> str:
    def fix(match: re.Match) -> str:
        indent, body = match.group(1), match.group(2)
        collapsed = " ".join(body.split())
        replacement = PARAGRAPHS.get(collapsed)
        if replacement is None:
            return match.group(0)
        wrapped = textwrap.fill(
            replacement,
            width=110,
            initial_indent=indent + "    ",
            subsequent_indent=indent + "    ",
        )
        return f"{indent}<p>\n{wrapped}\n{indent}</p>"

    text = PARAGRAPH_RE.sub(fix, text)
    for old, new in CAPTIONS.items():
        text = text.replace(f"<figcaption>{old}</figcaption>", f"<figcaption>{new}</figcaption>")
    for old, new in SNIPPETS.items():
        text = text.replace(old, new)
    return text


def main() -> int:
    changed = 0
    for page in html_files():
        original = page.read_text(encoding="utf-8")
        text = rewrite_prose(original)
        text = relabel_headings(text)
        text = delabel_captions(text)
        if text != original:
            page.write_text(text, encoding="utf-8")
            changed += 1
            print(f"  voice {page.relative_to(REPO)}")

    print(f"{changed} page(s) updated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
