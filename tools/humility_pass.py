"""Take the self-congratulation out.

The copy kept awarding itself marks: things were done "properly", projects
were "exactly the kind of project I like", an unfinished robot arm was
"already full of useful lessons", and several pages announced the valuable
lesson the reader was about to receive.

The register we want instead is the one Daniel used when he flagged this:

    "Still in progress, already full of useful lessons."
    ->  "Still in progress. And taking longer than I thought!"

Plainer, happy to admit the thing cost more than expected, and never claiming
credit the work has not obviously earned. Where a sentence existed only to
praise the author's judgement, it is cut rather than reworded.

    python tools/humility_pass.py
"""

from __future__ import annotations

import sys

from media_common import REPO, html_files
from textedit import apply_paragraphs, apply_snippets

PARAGRAPHS = {
    # --- 3D printers -------------------------------------------------------
    "The wiring stage is classic me territory: route it properly, strain-relieve it, check it "
    "twice, then pretend the first power-on is emotionally neutral.":
        "The wiring took longer than the rest of the assembly. Route it, strain-relieve it, check "
        "it, and then be nervous about the first power-on anyway.",

    # --- Ben Eater ---------------------------------------------------------
    "A CPU on breadboards, built from Ben Eater's series: clock, registers, memory, bus and "
    "control logic. None of it was new to me in theory. Wiring it up by hand was still worth "
    "the weekend.":
        "A CPU on breadboards, built from Ben Eater's series: clock, registers, memory, bus and "
        "control logic. None of it was new in theory. Doing it with actual wire was slower and "
        "more confusing than I expected, which was rather the point.",

    # --- CV in a box -------------------------------------------------------
    "A physical CV packaged like old software. Deeply unnecessary, which is not the same thing as "
    "wrong. It is a small object lesson in presentation, memory, taste, and the useful "
    "engineering instinct of asking: what if we made the idea real?":
        "A physical CV packaged like old software. Completely unnecessary, and it took far longer "
        "than writing a CV would have. I wanted to find out whether something people pick up beats "
        "something people skim.",

    "A normal CV says what you have done. This tries to show something as well: a fondness for old "
    "computers, a willingness to make a joke real, and enough practical follow-through to design, "
    "print, assemble and photograph the thing properly.":
        "A normal CV lists what you have done. This one also shows that I will take a daft idea "
        "all the way through artwork, print, assembly and photography before admitting it was a "
        "lot of work for a joke.",

    "It has sat on a bookshelf between real software boxes for years and people still pick it up "
    "to see what it is. That was the entire specification.":
        "It sits on a shelf between actual software boxes, and people pick it up to see what it "
        "is. That was the only thing I wanted it to do.",

    # --- Drift trike -------------------------------------------------------
    "Every requirement this thing had is visible in one clip. It goes, it turns, it slides, and "
    "the rider is grinning. I have signed off far more expensive systems on far weaker evidence.":
        "The specification was: go, turn, slide, and make him grin. This is the clip where I found "
        "out whether it did.",

    "This is exactly the kind of project I like: steel, wheels, motors, wiring, testing, noise, "
    "sparks, and a final machine that has to survive real use rather than just look plausible "
    "on the bench.":
        "Steel, wheels, motors and wiring, and a machine that has to survive an enthusiastic child "
        "rather than just look plausible on the bench. Several things I was confident about turned "
        "out to be wrong.",

    # --- Lathe sparks ------------------------------------------------------
    "Sometimes the correct reason to document something is that it looks fantastic. It still says "
    "something real: tools, materials, patience, judgement, and the pleasure of understanding a "
    "machine well enough to make it do something slightly spectacular.":
        "There is no lesson here. It looks fantastic, so I filmed it. That is the entire reason "
        "this page exists.",

    # --- Mega bookcase -----------------------------------------------------
    "There is a lot of measuring before anything looks impressive. The front-face work is exactly "
    "that kind of careful, unglamorous progress: lay it out, check it, make the next operation "
    "less likely to embarrass you.":
        "A lot of measuring before anything looks like furniture. Lay it out, check it, check it "
        "again, because the next cut is the expensive one.",

    # --- MSc: Data mining --------------------------------------------------
    "One of the funniest pilot prompts asked for a council-meeting podcast in the style of Statler "
    "and Waldorf from the Muppets. The generated result was genuinely entertaining, but that was "
    "exactly the point: the same source material suddenly became a performance with judgement, "
    "ridicule and selective emphasis baked into the delivery.":
        "One pilot prompt asked for a council-meeting podcast in the style of Statler and Waldorf. "
        "It was funnier than it had any right to be, and that was the problem: the same source "
        "material had turned into a performance, with judgement and selective emphasis baked into "
        "the delivery.",

    # --- MSc: Algorithms ---------------------------------------------------
    "The practical value was learning to explain why a program terminates, why it is correct, and "
    "where it will fail - rather than only what it does.":
        "I can describe what a program does. Explaining why it terminates, why it is correct and "
        "where it fails is a different skill, and I was rustier at it than I expected.",

    # --- MSc: Programming for data science ---------------------------------
    "The useful lesson was how quickly data work turns into systems work: file formats, storage, "
    "repeatability and provenance decide whether anyone should trust the analysis.":
        "Data work turns into systems work almost immediately: file formats, storage, "
        "repeatability and provenance are what decide whether anyone should trust the analysis.",

    # --- MSc: Data science -------------------------------------------------
    "What stuck was the gap between “accuracy” and usefulness. A classifier can look clever in a "
    "notebook and still be a terrible business instrument if the error costs are asymmetric.":
        "The gap between “accuracy” and usefulness is wider than it looks. A classifier can score "
        "well in a notebook and still be a terrible business instrument when the error costs are "
        "asymmetric.",

    # --- "satisfying" was doing a lot of quiet self-approval ---------------
    "The satisfying stage where it starts looking less like a delivery and more like a precision "
    "machine.":
        "The stage where it stops looking like a flat-pack delivery and starts looking like a "
        "machine.",

    "The satisfying middle bit: checking the frame, marking out the top, working through alignment "
    "and finding the shape of the thing rather than just assembling parts from a box.":
        "Checking the frame, marking out the top and working through the alignment. This is the "
        "part where you find out how far out of square the frame really is.",

    "A belly board is satisfyingly direct: wood, curve, edge, grain, water. It is a small project, "
    "but it still rewards the same things as bigger engineering work: material feel, sequence, "
    "proportion and not rushing the last few decisions.":
        "A belly board is about as direct as a project gets: wood, curve, edge, grain, water. It "
        "is small, and it still punishes rushing the last few decisions.",

    "A build of Ben Eater's 8-bit computer, because abstractions are more satisfying when you can "
    "trace them through actual wires.":
        "A build of Ben Eater's 8-bit computer, so I could trace the abstractions through actual "
        "wires instead of taking them on trust.",

    "This one sits nicely in the uncomfortable overlap between architecture, structural judgement, "
    "fabrication, welding, repetition, and the stubborn belief that a terrace edge can be made "
    "much more interesting than a bought-in railing.":
        "It sits in the awkward overlap between architecture, structural judgement and a great "
        "deal of repetitive welding. A bought-in railing would have taken an afternoon.",

    "The box is a small protest against everything looking the same. It still points at serious "
    "work: software engineering, Linux, Python, technical leadership, and the slightly dangerous "
    "claim that someone can be designed to maximise your team.":
        "The box is a small protest against every application looking the same. The back of it "
        "lists the real things - software engineering, Linux, Python, technical leadership - in "
        "the format of a 1990s feature list, which is either charming or a warning sign.",

    "Some projects finish with a neat report. This one finishes with a test driver on the grass, a "
    "working electric trike, and the satisfying evidence that the idea made it all the way into "
    "the physical world.":
        "No report, no write-up, no retrospective. It finishes with a child on the grass going "
        "sideways, which is the only outcome anyone involved cared about.",

    # --- talking about the page instead of the project ---------------------
    "The raw footage is full-length build material, so I pulled it down to a handful of short "
    "clips: unboxing, rods and rails, frame assembly, wiring and the finished printer. Enough to "
    "show the texture of the work without making anyone sit through hours of screw sorting.":
        "Five short clips: unboxing, rods and rails, frame assembly, wiring, and the finished "
        "machine. The full build is several hours of sorting screws into piles.",

    "The photos tell the useful version: timber on the bench, outline and shaping, maker's marks, "
    "then the finished form. I have kept the selection deliberately small so the page feels like a "
    "project, not a memory-card dump.":
        "Timber on the bench, outline and shaping, maker's marks, then the finished board.",

    "The media is not polished studio footage, which is probably why I like it. It has measuring, "
    "cutting, test-fitting, sunlight, clutter, and the familiar moment where the thing starts "
    "becoming a real object.":
        "Phone footage, taken while working: measuring, cutting, test-fitting, and a workshop that "
        "was in no state to be filmed.",

    "The raw folder is a proper build diary, so the clips here are deliberately short: printing "
    "arm parts, laying out actuator components, bench electronics, hand-testing a joint, "
    "assembling the larger arm structure and a little metalwork from the later stages.":
        "Short clips from the build: printing parts, laying out the actuator components, bench "
        "electronics, hand-testing a joint, and assembling the larger structure.",

    "The making footage has the usual rhythm: cut, mark, assemble, test, install, adjust, repeat. "
    "Not glamorous, but exactly the kind of small practical job that quietly improves a room.":
        "Cut, mark, assemble, test, install, adjust, repeat. Perhaps forty times, for a job I had "
        "estimated at an afternoon.",

    # --- aphorisms standing in for content ---------------------------------
    "The useful work is often not a single heroic operation. It is the steady loop of marking, "
    "cutting, grinding, checking the fit, changing your mind slightly, then doing the next piece "
    "better because the last one taught you something.":
        "There is no single difficult operation, just a long loop of marking, cutting, grinding "
        "and checking the fit, with each piece coming out slightly better than the last.",

    "The best version of this sort of project is when the finished object stops looking like a "
    "problem that was solved and starts looking like a detail that always belonged to the house.":
        "The aim was for it to look like it had always been there, rather than like something that "
        "had been solved.",

    "The best bit is how the finished wall stops looking like furniture and starts acting like "
    "architecture. It makes the room taller, denser and more personal, which is a strong result "
    "for something that began as a large pile of boards.":
        "Loaded with books, it stopped reading as furniture and started reading as part of the "
        "room. It also swallowed an entire wall, which had been the idea.",

    "That is the slightly unfair reward: if the job is done well, most people just see skirting "
    "board. The effort disappears into the room, which is annoying and also exactly the point.":
        "If it is done well, visitors see skirting board and think nothing at all. Weeks of work, "
        "invisible by design.",

    "This one is less a single object and more a campaign: panel work, carcasses, wall fixing, "
    "alignment, shelf runs, drawers, cable-and-console details, ladder hardware, machining, "
    "welding, finishing, and many moments where the correct tool was patience.":
        "It turned into a campaign rather than a project: panel work, carcasses, wall fixing, "
        "shelf runs, drawers, cable routing, and then a ladder that needed its own machining and "
        "welding.",

    "The ladder turns the bookcase from storage into theatre. It also adds a whole mechanical "
    "sub-project: rollers, brackets, rails, fit, finish, and the excellent excuse to use the lathe "
    "for something that ends up in the living room.":
        "The ladder was not necessary. It also turned into its own mechanical sub-project: "
        "rollers, brackets and rails, and an excuse to use the lathe for something that ends up in "
        "the living room.",

    "The bookcase has to frame the existing window, meet the room, leave the console useful, and "
    "make the steel-and-glass doors feel intentional rather than like neighbouring projects "
    "arguing.":
        "It had to frame the existing window, leave the console usable underneath, and line up "
        "with the steel-and-glass doors that were already there.",

    "A Christmas build of an Original Prusa MK4 kit: boxes, rods, printed brackets, bearings, "
    "wiring, screen, calibration and the slightly hypnotic pleasure of a machine becoming square, "
    "smooth and obedient one subassembly at a time.":
        "A Christmas build of an Original Prusa MK4 kit: rods, printed brackets, bearings, wiring, "
        "screen and calibration, assembled one subassembly at a time over about two days.",

    "I like 3D printers because they sit in that perfect workshop zone between software, "
    "mechanics, electronics and immediate consequences. You can think in CAD in the morning and "
    "hold a useful bracket in the evening. Dangerous, frankly.":
        "3D printers sit between software, mechanics and electronics, with immediate consequences. "
        "You can think in CAD in the morning and hold a useful bracket by the evening. Dangerous, "
        "frankly.",

    "The build footage starts with the previous red steel staircase in the courtyard. It is a "
    "useful reminder that the job was not happening on a blank sheet of paper; it had to fit a "
    "real building, real levels, real walls, and all the slightly inconvenient truth that comes "
    "with them.":
        "The footage starts with the red steel staircase that was there before. Nothing about this "
        "job started from a blank sheet: existing building, existing levels, existing walls.",

    "Some later-stage fabrication energy, because the project refuses to stay purely plastic.":
        "Later-stage metalwork, once it became clear that printed parts would not do everything.",

    "The point where separate clever pieces become one larger, less-forgiving machine.":
        "Where the separate assemblies become one machine, and the tolerances start stacking up.",

    # --- sentences that assert something without saying anything -----------
    "I like that this project goes from simulation to physical work without changing personality: "
    "model the risk, make the parts, check the fit, weld it together, then let time and weather do "
    "the final finishing pass.":
        "Model the loads, make the parts, check the fit, weld it up, and then let the weather do "
        "the last finishing pass for you. Corten is the only material I have used where rusting is "
        "the intended outcome.",

    "It is very much a work in progress, but it already shows the thing I like most about "
    "robotics: you cannot hide from the physical system for long.":
        "Still in progress. Every one of these steps took longer than the plan said it would, "
        "which is roughly the pattern for the whole build.",

    "The desk is nice, but the better thing is the collaboration: measuring, checking, deciding, "
    "adjusting, and sharing the little engineering rituals that turn a pile of parts into a thing "
    "that works.":
        "The desk is fine. The better part was building it with my son: measuring, checking, and "
        "disagreeing about which way round the top should go.",

    "A wooden surfboard from an Otter course: outline, shaping, glassing and finish. A physical "
    "object with real personality, and a reminder that removing material is a one-way operation.":
        "A wooden surfboard from an Otter course: outline, shaping, glassing and finish. Mostly a "
        "long lesson in the fact that removing material is a one-way operation.",

    "I like the point where code, data, electronics, mechanisms and people all have to agree. That "
    "has meant debugging car-stopping motorsport problems, keeping production platforms alive, "
    "building robots in a workshop, and asking the same question in different forms: how do we "
    "know this is really working?":
        "I like the point where code, data, electronics, mechanisms and people all have to agree. "
        "That has meant debugging car-stopping motorsport problems, keeping production platforms "
        "alive and building robots in a workshop. The question is always the same one: how do we "
        "know this is really working?",

    "The MSc gave me the academic structure; these projects added compressed hands-on reps. They "
    "sit nicely between the taught modules and my later robotics work because they are all about "
    "the same thing: representations, training signals, masking, evaluation and getting enough of "
    "the system under your fingers that you can debug it properly.":
        "The MSc gave me the structure; these gave me the reps. They cover the same ground as the "
        "taught modules - representations, training signals, masking, evaluation - but built from "
        "scratch, which is where you find out what you had only half understood.",
}

SNIPPETS = {
    # The line Daniel rewrote himself, in his words.
    "<span>Still in progress, already full of useful lessons.</span>":
        "<span>Still in progress. And taking longer than I thought!</span>",

    "<h2>Each page is a short synopsis of what I studied, what I built and what stuck.</h2>":
        "<h2>One page per module: what I studied, what I built, what I got wrong.</h2>",

    # Captions and taglines that were patting themselves on the back.
    "<figcaption>Presented as if it belonged on a shelf next to machine learning books, which frankly it does.</figcaption>":
        "<figcaption>On the shelf, next to the machine learning books</figcaption>",
    "<figcaption>Finished enough for the only test that matters: hand it to the test driver.</figcaption>":
        "<figcaption>Finished enough to hand over to the test driver</figcaption>",
    "<figcaption>Linear motion, orange brackets and the good kind of tolerances</figcaption>":
        "<figcaption>Linear rails and printed brackets</figcaption>",
    "<figcaption>The orange bits are doing a lot of visual heavy lifting, and I approve.</figcaption>":
        "<figcaption>Printed brackets in the usual orange</figcaption>",
    "<span>Ridiculous object, serious signal.</span>": "<span>Ridiculous object. Took ages.</span>",
    "Beautiful, slightly alarming, deeply satisfying sparks.": "Beautiful, slightly alarming sparks.",
    "<h2>The machine teaches you its tolerances.</h2>": "<h2>Learning its tolerances</h2>",

    # Card copy repeated on the home page and the project index.
    "short build clips and the good kind of workshop chaos.":
        "short build clips and a great deal of sawdust.",
    "A ridiculous object with a serious point, with photos, video and box-art evidence.":
        "A ridiculous object that took a suspicious amount of effort, with the box art to prove it.",
    "Deeply unnecessary, which is not the same thing as wrong.":
        "Completely unnecessary, and it took far longer than writing a CV would have.",
    "Curved steel, courtyard constraints and a properly useful way upstairs":
        "Curved steel, courtyard constraints, and a way upstairs that actually fits",

    # CV
    "# Not a generalist by accident. A generalist by repeated exposure to real systems.":
        "# Generalist, mostly by accident, and by repeated exposure to real systems.",

    "<p class=\"eyebrow\">The satisfying bit</p>": "<p class=\"eyebrow\">Simulation</p>",
    "<figcaption>The finished stair, black, compact, and properly settled into the courtyard</figcaption>":
        "<figcaption>The finished stair in the courtyard</figcaption>",
}


# The previous pass relabelled four MSc headings to "What stuck", which just
# swapped one formula for another. Give each page its own.
PER_PAGE = {
    "MSc-Algorithms.html": {"<h2>What stuck</h2>": "<h2>What I use now</h2>"},
    "MSc-Ethics.html": {"<h2>What stuck</h2>": "<h2>Where it lands in practice</h2>"},
    "MSc-KRR.html": {"<h2>What stuck</h2>": "<h2>Modelling is engineering</h2>"},
    "MSc-ProgrammingForDataScience.html": {
        "<h2>What stuck</h2>": "<h2>Data work becomes systems work</h2>"
    },
}


def main() -> int:
    changed = 0
    for page in html_files():
        original = page.read_text(encoding="utf-8")
        text = apply_paragraphs(original, PARAGRAPHS)
        text = apply_snippets(text, SNIPPETS)
        text = apply_snippets(text, PER_PAGE.get(page.name, {}))
        if text != original:
            page.write_text(text, encoding="utf-8")
            changed += 1
            print(f"  humility {page.relative_to(REPO)}")

    print(f"{changed} page(s) updated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
