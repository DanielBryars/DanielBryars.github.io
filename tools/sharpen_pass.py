"""Cut the copy down to Daniel's actual voice.

Three rewrites he did by hand, which are the reference for everything else:

    "There is no lesson here. It looks fantastic, so I filmed it. That is the
     entire reason this page exists."
    ->  "There is no lesson here. Posted because I want to, it looks awesome"

    "No report, no write-up, no retrospective. It finishes with a child on the
     grass going sideways, which is the only outcome anyone involved cared about."
    ->  "Child on the grass going sideways, the only outcome I really care about."

    "The desk is fine. The better part was building it with my son: measuring,
     checking, and disagreeing about which way round the top should go."
    ->  "Desk is fine. Getting my son involved in building 'real things away from
         the virtual world' - awesome."

What that shows:

- About half the words. Every framing clause goes ("It finishes with", "The
  better part was", "That is the reason").
- No closing sentence explaining the point just made. Stop at the point.
- Telegraphic: "Desk is fine", not "The desk is fine". Drop articles and
  subject pronouns wherever a person taking notes would.
- First person, present tense, owned: "the only outcome I really care about",
  not "anyone involved cared about".
- Loose punctuation. Comma splices and dashes are fine, terminal full stops on
  short fragments are optional.
- Enthusiasm is welcome. "awesome" is his word. The ban is on self-praise, not
  on warmth - a previous pass stripped both and left it flat.
- No tricolons and no colon-lists of process verbs. That rhythm is not his.

cv.html is deliberately untouched: it is read by recruiters and wants the more
formal register it already has.

    python tools/sharpen_pass.py
"""

from __future__ import annotations

import sys

from media_common import REPO, html_files
from textedit import apply_paragraphs

PARAGRAPHS = {
    # --- Daniel's own three, verbatim --------------------------------------
    "There is no lesson here. It looks fantastic, so I filmed it. That is the entire reason this "
    "page exists.":
        "There is no lesson here. Posted because I want to, it looks awesome",

    "No report, no write-up, no retrospective. It finishes with a child on the grass going "
    "sideways, which is the only outcome anyone involved cared about.":
        "Child on the grass going sideways, the only outcome I really care about.",

    "The desk is fine. The better part was building it with my son: measuring, checking, and "
    "disagreeing about which way round the top should go.":
        "Desk is fine. Getting my son involved in building 'real things away from the virtual "
        "world' - awesome.",

    # --- 3D printers -------------------------------------------------------
    "A Christmas build of an Original Prusa MK4 kit: rods, printed brackets, bearings, wiring, "
    "screen and calibration, assembled one subassembly at a time over about two days.":
        "Original Prusa MK4 kit, built over Christmas. Two days of rods, bearings, brackets and "
        "wiring, one subassembly at a time.",

    "3D printers sit between software, mechanics and electronics, with immediate consequences. You "
    "can think in CAD in the morning and hold a useful bracket by the evening. Dangerous, frankly.":
        "CAD in the morning, a bracket in your hand by the evening. Dangerous, frankly.",

    "Five short clips: unboxing, rods and rails, frame assembly, wiring, and the finished machine. "
    "The full build is several hours of sorting screws into piles.":
        "Five short clips. The full build is hours of sorting screws into little piles.",

    "A printer is a lovely little reminder that software cannot rescue bad geometry forever. Rods, "
    "bearings, belts and leadscrews all have to move cleanly before the clever bits get their turn.":
        "Software cannot rescue bad geometry. Rods, bearings, belts and leadscrews have to move "
        "cleanly first.",

    "The wiring took longer than the rest of the assembly. Route it, strain-relieve it, check it, "
    "and then be nervous about the first power-on anyway.":
        "Wiring took longer than everything else put together. Route it, strain-relieve it, check "
        "it, still be nervous at first power-on.",

    "Bed, nozzle, belts and axes are all part of one feedback loop. Assembling it is the easy half; "
    "the useful half is learning how the machine reports its own state, and which of those reports "
    "to believe.":
        "Bed, nozzle, belts and axes are one feedback loop. Assembly is the easy half. The hard "
        "half is learning which of the machine's own reports to believe.",

    "For robot parts, brackets, fixtures, jigs and weird one-off workshop needs, a reliable printer "
    "changes the rhythm of a project. The idea gets physical faster.":
        "Robot parts, brackets, fixtures, jigs. A reliable printer changes the pace of everything "
        "else - ideas get physical the same day.",

    # --- Belly board -------------------------------------------------------
    "I won a competition for a day course to make a wooden belly board. Which is a pleasingly "
    "specific prize: part woodworking, part seaside engineering, part excuse to spend a day making "
    "something with a proper curve in it.":
        "Won a competition, prize was a day course making a wooden belly board. Pleasingly "
        "specific. Part woodwork, part seaside engineering, part excuse to spend a day on a proper "
        "curve.",

    "A belly board is about as direct as a project gets: wood, curve, edge, grain, water. It is "
    "small, and it still punishes rushing the last few decisions.":
        "Wood, curve, edge, grain, water. Small project, still punishes you for rushing the last "
        "few decisions.",

    # --- Ben Eater ---------------------------------------------------------
    "A build of Ben Eater's 8-bit computer, so I could trace the abstractions through actual wires "
    "instead of taking them on trust.":
        "Ben Eater's 8-bit computer, built so I could trace the abstractions through actual wire "
        "instead of trusting them.",

    "A CPU on breadboards, built from Ben Eater's series: clock, registers, memory, bus and "
    "control logic. None of it was new in theory. Doing it with actual wire was slower and more "
    "confusing than I expected, which was rather the point.":
        "Clock, registers, memory, bus, control logic. None of it new to me in theory. Doing it in "
        "wire was slower and more confusing than I expected - which was the point.",

    # --- Clock -------------------------------------------------------------
    "A custom clock build. Apparently showing the time is simple, right up until you start caring "
    "about how it is built.":
        "A custom clock. Telling the time is simple right up until you care how it is built.",

    "A clock, built as an object rather than a circuit with a display bolted on. The electronics "
    "were the easy half; the case, the typography and the decision about what it should do at 3am "
    "took much longer.":
        "Built as an object, not a circuit with a display bolted on. Electronics were the easy "
        "half. The case, the typography, and what it should do at 3am took much longer.",

    # --- Corten balustrade -------------------------------------------------
    "A curved terrace balustrade I designed, checked with FEA, fabricated from box section and "
    "installed outside so the weather could finish the job properly.":
        "Curved terrace balustrade. Designed it, checked it with FEA, fabricated it from box "
        "section, then left it outside to rust on purpose.",

    "It sits in the awkward overlap between architecture, structural judgement and a great deal of "
    "repetitive welding. A bought-in railing would have taken an afternoon.":
        "Architecture, structural judgement, and a lot of repetitive welding. A bought-in railing "
        "would have taken an afternoon.",

    "I used a finite element model to sanity-check the post design and deflection under load "
    "before making a long row of identical mistakes in expensive steel. The screenshot shows a "
    "displacement result, with the maximum at the loaded end.":
        "FEA on the post design and deflection under load, before making a long row of identical "
        "mistakes in expensive steel. Screenshot shows displacement, worst at the loaded end.",

    "The terrace wall curves, so the design had to follow the geometry without looking fussy. The "
    "repeated vertical sections make the curve legible, while the rusting surface gives the whole "
    "thing a softer, more natural relationship with the garden and fields.":
        "The wall curves, so the balustrade had to follow it without looking fussy. Repeated "
        "verticals make the curve readable. The rust softens it against the fields.",

    "Model the loads, make the parts, check the fit, weld it up, and then let the weather do the "
    "last finishing pass for you. Corten is the only material I have used where rusting is the "
    "intended outcome.":
        "Model the loads, make the parts, check the fit, weld it up. Then the weather does the "
        "last finishing pass. Corten is the only material I have used where rusting is the plan.",

    "Some of the fabrication happened on a welding table in the unfinished kitchen, which feels "
    "very on-brand for this house build: dinner in the background, steel on the table, tools "
    "everywhere, and a balustrade slowly becoming inevitable.":
        "Some of it was welded on a table in the unfinished kitchen. Very on-brand for this house "
        "build. Dinner in the background, steel on the table, tools everywhere.",

    "My favourite photos of it are not the fabrication shots. They are the ones with people "
    "leaning on it, talking, looking out across the fields.":
        "My favourite photos are not the fabrication ones. They are the ones with people leaning "
        "on it, talking, looking at the fields.",

    # --- Curving skirting board -------------------------------------------
    "Because I built a house with curved walls. A normal length of skirting board took one look at "
    "the curve and declined to cooperate, so the answer became: build a steam box, bend the "
    "timber, fix it while it still remembered the shape, then make the whole thing look like it "
    "was obvious.":
        "I built a house with curved walls. Skirting board took one look and declined. So: build a "
        "steam box, bend the timber, fix it while it still remembers the shape.",

    "It is a small domestic detail on the surface, but underneath it is all geometry, moisture, "
    "heat, timing, clamps, wall fixings and the quiet terror of snapping the piece after all that "
    "work.":
        "Small domestic detail on the surface. Underneath: geometry, moisture, heat, timing, and "
        "the quiet terror of snapping it after all that work.",

    "Bending the skirting was the easy part to describe and the hard part to do. Heat and moisture "
    "have to get into a long piece of timber evenly, or it splits, springs back, or becomes "
    "expensive firewood.":
        "Easy to describe, hard to do. Heat and moisture have to get right through a long piece "
        "evenly, or it splits, springs back, or becomes expensive firewood.",

    "The wall was already curved, because the house was designed that way. The skirting had to "
    "follow the architecture rather than fight it, which turned a trim job into a bending problem.":
        "The wall was curved because the house was designed that way. The skirting had to follow "
        "it, which turned a trim job into a bending problem.",

    "Steam bending works by briefly making the timber more compliant. The awkward bit is that the "
    "clock starts as soon as it comes out of the box, so the wall, tools and fixings all have to "
    "be ready.":
        "Steam makes the timber briefly compliant. The clock starts the moment it leaves the box, "
        "so the wall, tools and fixings all have to be ready and waiting.",

    "If it is done well, visitors see skirting board and think nothing at all. Weeks of work, "
    "invisible by design.":
        "Done well, visitors see skirting board and think nothing at all. Weeks of work, invisible "
        "on purpose.",

    # --- CV in a box -------------------------------------------------------
    "A physical CV packaged like old software. Completely unnecessary, and it took far longer than "
    "writing a CV would have. I wanted to find out whether something people pick up beats "
    "something people skim.":
        "A CV packaged like old software. Completely unnecessary, took far longer than writing a "
        "CV. I wanted to know whether something people pick up beats something people skim.",

    "A short video showing the design work behind the box. The premise is silly; the execution is "
    "deliberately not silly. That tension is basically the whole project.":
        "Short video of the design work. Premise is silly, execution deliberately is not.",

    "A normal CV lists what you have done. This one also shows that I will take a daft idea all "
    "the way through artwork, print, assembly and photography before admitting it was a lot of "
    "work for a joke.":
        "A normal CV lists what you did. This one shows I will take a daft idea all the way "
        "through artwork, print and assembly before admitting it was a lot of work for a joke.",

    "The box is a small protest against every application looking the same. The back of it lists "
    "the real things - software engineering, Linux, Python, technical leadership - in the format "
    "of a 1990s feature list, which is either charming or a warning sign.":
        "A small protest against every application looking the same. The back lists the real "
        "things - software engineering, Linux, Python - as a 1990s feature list. Charming or a "
        "warning sign, not sure which.",

    "It sits on a shelf between actual software boxes, and people pick it up to see what it is. "
    "That was the only thing I wanted it to do.":
        "Sits on a shelf between actual software boxes. People pick it up to see what it is. That "
        "was the only thing I wanted.",

    # --- Drift trike -------------------------------------------------------
    "An electric drift trike built from workshop fabrication, motor-mount problem solving, "
    "controller wiring, welding-filter footage and the extremely important requirement that it "
    "makes a child grin while going sideways.":
        "Electric drift trike. Fabrication, motor mounts, controller wiring, and the important "
        "requirement: it has to make a child grin while going sideways.",

    "Steel, wheels, motors and wiring, and a machine that has to survive an enthusiastic child "
    "rather than just look plausible on the bench. Several things I was confident about turned out "
    "to be wrong.":
        "Steel, wheels, motors, wiring. Has to survive an enthusiastic child, not just look "
        "plausible on the bench. Several things I was confident about turned out wrong.",

    "The specification was: go, turn, slide, and make him grin. This is the clip where I found out "
    "whether it did.":
        "Spec was: go, turn, slide, make him grin. Here is where I found out.",

    "Motor, chain, controller, wiring and display, run together on the bench before any of it goes "
    "near a rider. This is the cheap place to find out that a connector is undersized.":
        "Motor, chain, controller, wiring and display, run together on the bench before any of it "
        "goes near a rider. Cheap place to find out a connector is undersized.",

    "Shot through the auto-darkening filter, which is the only way to see the arc, the puddle and "
    "the filler rod at the same time. Everything a beginner needs to watch is in here: puddle "
    "size, travel speed, and how far ahead of the bead you are looking.":
        "Shot through the auto-darkening filter - the only way to see arc, puddle and filler rod "
        "at once. Puddle size, travel speed, how far ahead of the bead you look. All of it is in "
        "here.",

    "The motor mount is the part that decides whether any of the rest works. Alignment, chain "
    "tension, clearance, fastener access and how you service it after the first failure all have "
    "to be settled here, before anything gets welded.":
        "The motor mount decides whether any of the rest works. Alignment, chain tension, "
        "clearance, fastener access, and how you service it after the first failure. All settled "
        "before anything gets welded.",

    "It still needs the same thinking as a bigger machine: mechanical structure, drivetrain, "
    "wiring, controls, packaging, testing and the awkward business of making everything survive "
    "vibration and enthusiastic use.":
        "Small machine, same thinking as a big one. Structure, drivetrain, wiring, controls, "
        "packaging, and making all of it survive vibration and enthusiastic use.",

    "Cutting, drilling, welding, tapping and mounting all have to happen in a sequence you can "
    "still recover from. Weld too early and you lose the adjustment you needed; leave it too late "
    "and you are welding around finished parts.":
        "Cut, drill, weld, tap, mount - in an order you can still recover from. Weld too early and "
        "you lose the adjustment. Leave it too late and you are welding around finished parts.",

    "The controller and wiring took about as long as the frame. Vibration, chafe and connector "
    "choice are what decide whether it still works on the tenth run rather than the first.":
        "Controller and wiring took about as long as the frame. Vibration, chafe and connector "
        "choice decide whether it still works on the tenth run.",

    # --- Lathe sparks ------------------------------------------------------
    "Machining hardened steel with a CBN insert on an old Colchester Chipmaster lathe. This is not "
    "pretending to be a complicated project page. This is mainly sparks. Beautiful, slightly "
    "alarming sparks.":
        "Hardened steel, CBN insert, old Colchester Chipmaster. Not pretending to be a complicated "
        "project page. Mainly sparks. Beautiful, slightly alarming sparks.",

    "This is the short one and probably the prettiest: the tool cuts, the spindle blurs, and the "
    "sparks make little orange orbits like the lathe has briefly become a small industrial "
    "planetarium.":
        "Short one, probably the prettiest. Tool cuts, spindle blurs, sparks go into little orange "
        "orbits like a small industrial planetarium.",

    "The machine is a Colchester Chipmaster: proper old British workshop machinery, heavy in all "
    "the useful places. The cut is on hardened steel using a CBN insert, which is why the footage "
    "looks less like normal turning and more like metal fireworks.":
        "Colchester Chipmaster - proper old British machinery, heavy in all the useful places. "
        "Cutting hardened steel with a CBN insert, which is why it looks less like turning and "
        "more like fireworks.",

    # --- Mega bookcase -----------------------------------------------------
    "A wall-sized bookcase, built in sections, fitted around a window, extended into a low console, "
    "filled with books, and then given a rolling ladder because apparently shelves can always "
    "become more unreasonable.":
        "Wall-sized bookcase. Built in sections, fitted round a window, extended into a low "
        "console, filled with books, then given a rolling ladder because shelves can always get "
        "more unreasonable.",

    "It turned into a campaign rather than a project: panel work, carcasses, wall fixing, shelf "
    "runs, drawers, cable routing, and then a ladder that needed its own machining and welding.":
        "Turned into a campaign rather than a project. Panels, carcasses, wall fixing, shelf runs, "
        "drawers, cable routing, then a ladder that needed its own machining and welding.",

    "The early work is the quiet, repetitive part: cutting panels, making carcasses, keeping edges "
    "straight, and gradually turning flat sheet goods into something big enough to change the room.":
        "The early work is quiet and repetitive. Cut panels, make carcasses, keep the edges "
        "straight, slowly turn flat sheet into something big enough to change the room.",

    "The ladder was not necessary. It also turned into its own mechanical sub-project: rollers, "
    "brackets and rails, and an excuse to use the lathe for something that ends up in the living "
    "room.":
        "The ladder was not necessary. It became its own sub-project - rollers, brackets, rails - "
        "and an excuse to use the lathe for something that ends up in the living room.",

    "A lot of measuring before anything looks like furniture. Lay it out, check it, check it "
    "again, because the next cut is the expensive one.":
        "A lot of measuring before anything looks like furniture. Lay it out, check it, check it "
        "again. The next cut is the expensive one.",

    "A small cabinet can be a little forgiving. A full-height bookcase across a wall is less kind: "
    "every small error has somewhere to travel. The build is really about controlling that creep.":
        "A small cabinet forgives you. A full-height wall does not - every small error has "
        "somewhere to travel. The whole build is about controlling that creep.",

    "It had to frame the existing window, leave the console usable underneath, and line up with "
    "the steel-and-glass doors that were already there.":
        "Had to frame the existing window, leave the console usable underneath, and line up with "
        "the steel-and-glass doors already there.",

    "Once the shelves went high enough, the ladder became both practical and irresistible. A "
    "normal person might have bought one. This version acquired custom hardware, machining and "
    "welding.":
        "Once the shelves went high enough the ladder became irresistible. A normal person buys "
        "one. This one got custom hardware, machining and welding.",

    "Loaded with books, it stopped reading as furniture and started reading as part of the room. "
    "It also swallowed an entire wall, which had been the idea.":
        "Loaded with books it stopped being furniture and started being part of the room. Also "
        "swallowed an entire wall, which was the idea.",

    # --- Standing desk -----------------------------------------------------
    "A height-adjustable desk I built with my son: part furniture, part workshop problem-solving, "
    "part excuse to spend a day making something useful together.":
        "Height-adjustable desk, built with my son. Part furniture, part workshop problem, part "
        "excuse to spend a day making something together.",

    "Phone footage, taken while working: measuring, cutting, test-fitting, and a workshop that was "
    "in no state to be filmed.":
        "Phone footage, shot while working. Measuring, cutting, test-fitting, and a workshop in no "
        "state to be filmed.",

    "Checking the frame, marking out the top and working through the alignment. This is the part "
    "where you find out how far out of square the frame really is.":
        "Checking the frame, marking out the top, working the alignment. This is where you find "
        "out how far out of square the frame really is.",

    "I like projects that have to survive daily use. This one is half furniture making and half "
    "fitting a motorised frame to a top heavy enough to need it, in a way that still works after a "
    "thousand cycles.":
        "I like things that have to survive daily use. Half furniture making, half fitting a "
        "motorised frame to a top heavy enough to need it, still working after a thousand cycles.",

    # --- Robot arm ---------------------------------------------------------
    "A home-built arm for running robot-learning experiments on something that is not a simulator. "
    "Printed structure, cycloidal reducers, servo drives, and the wiring and calibration that a "
    "simulated robot never makes you think about. It is unfinished, and will probably stay that "
    "way for a while.":
        "Home-built arm for running robot-learning experiments on something that is not a "
        "simulator. Printed structure, cycloidal reducers, servo drives, and all the wiring and "
        "calibration a simulated robot lets you ignore. Unfinished, and likely to stay that way a "
        "while.",

    "It picks up directly from my MSc work - MuJoCo simulation, OpenVR teleoperation, data "
    "capture, policy training - and asks the one question a simulator cannot answer: how much of "
    "this survives contact with a real, slightly wrong machine?":
        "Picks up from my MSc work - MuJoCo, OpenVR teleoperation, data capture, policy training - "
        "and asks the thing a simulator cannot: how much survives contact with a real, slightly "
        "wrong machine?",

    "Structure and joints are printed, so a revision costs an evening rather than a machine shop. "
    "The trade is stiffness: printed parts flex, and flex shows up as position error at the end of "
    "a long arm.":
        "Structure and joints are printed, so a revision costs an evening instead of a machine "
        "shop. The trade is stiffness. Printed parts flex, and flex becomes position error at the "
        "end of a long arm.",

    "Each joint uses a printed cycloidal reducer rather than a belt drive or a bought harmonic "
    "drive: high ratio, compact, and printable at home. The cost is backlash, which I have not "
    "measured properly yet.":
        "Printed cycloidal reducer at each joint rather than belts or a bought harmonic drive. "
        "High ratio, compact, printable at home. Costs you backlash, which I have not measured "
        "properly yet.",

    "Motor drives, position feedback, power and connectors, per joint, routed through a moving "
    "structure. The part worth building carefully is the instrumentation: without it, a bad "
    "connector and a bad control loop look identical.":
        "Motor drive, position feedback, power and connectors, per joint, routed through a moving "
        "structure. Build the instrumentation carefully - without it a bad connector and a bad "
        "control loop look identical.",

    "The point is to have somewhere to run policies that were trained in MuJoCo and find out what "
    "the simulator was wrong about. Reality gap, measured rather than discussed.":
        "Somewhere to run policies trained in MuJoCo and find out what the simulator got wrong. "
        "Reality gap, measured rather than discussed.",

    "Short clips from the build: printing parts, laying out the actuator components, bench "
    "electronics, hand-testing a joint, and assembling the larger structure.":
        "Short clips: printing parts, laying out actuators, bench electronics, hand-testing a "
        "joint, assembling the structure.",

    "Still in progress. Every one of these steps took longer than the plan said it would, which is "
    "roughly the pattern for the whole build.":
        "Still in progress. Every step took longer than the plan said, which is the pattern for "
        "the whole build.",

    "Motor control on the bench: cables, boards, meters and the familiar ritual of checking what "
    "is actually moving.":
        "Motor control on the bench. Cables, boards, meters, and the usual checking of what is "
        "actually moving.",

    # --- Spiral staircase --------------------------------------------------
    "A spiral staircase and courtyard access project: steel, curves, handrail work, fitting around "
    "walls and pergola posts, in a courtyard with no straight lines to measure from.":
        "Spiral staircase into the courtyard. Steel, curves, handrail work, fitted round walls and "
        "pergola posts, in a courtyard with no straight line to measure from.",

    "The finished stair looks calm, which usually means the difficult bits are well hidden. "
    "Getting there was measuring, cutting, grinding and test-fitting against a courtyard that was "
    "already built and nowhere near square.":
        "Looks calm, which usually means the hard bits are well hidden. Getting there was "
        "measuring, cutting, grinding and test-fitting against a courtyard that was already built "
        "and nowhere near square.",

    "The footage starts with the red steel staircase that was there before. Nothing about this job "
    "started from a blank sheet: existing building, existing levels, existing walls.":
        "Footage starts with the red staircase that was there before. Nothing here started from a "
        "blank sheet - existing building, existing levels, existing walls.",

    "Spiral staircases are compact and beautiful, but they do not leave much room for fuzzy "
    "thinking. The handrail, treads, clearances and surrounding structure all have to agree, "
    "especially when the staircase is being made to live in an existing courtyard.":
        "Spirals are compact and beautiful and leave no room for fuzzy thinking. Handrail, treads, "
        "clearances and surrounding structure all have to agree, especially in a courtyard that "
        "already exists.",

    "There is no single difficult operation, just a long loop of marking, cutting, grinding and "
    "checking the fit, with each piece coming out slightly better than the last.":
        "No single difficult operation. Just a long loop of marking, cutting, grinding and "
        "checking the fit, each piece slightly better than the last.",

    "The aim was for it to look like it had always been there, rather than like something that had "
    "been solved.":
        "Wanted it to look like it had always been there, rather than like something that got "
        "solved.",

    "The staircase sits beside timber, masonry, glazing, railings and garden access. That is the "
    "fun part: the engineering has to work, but the object also has to make visual sense in the "
    "larger mess of a real place.":
        "It sits against timber, masonry, glazing, railings and the garden. The engineering has to "
        "work and the thing also has to look right in the middle of a real, messy place.",

    # --- Vintage string lights ---------------------------------------------
    "Custom string lights for the house: twisted cable, warm filament bulbs, little made parts, "
    "ceiling beams, and enough workshop faff to make buying the dull version feel like surrender.":
        "String lights for the house. Twisted cable, warm filament bulbs, little made parts, "
        "ceiling beams, and enough workshop faff that buying them would have felt like surrender.",

    "Off-the-shelf lighting would have lit the room. These make it feel like somewhere specific, "
    "with the cable and bulbs sitting comfortably against the steel beams and timber.":
        "Shop-bought would have lit the room. These make it feel like somewhere specific, cable "
        "and bulbs sitting against the steel beams and timber.",

    "The build starts in the workshop: cutting little blocks, laying out parts, wiring holders, "
    "testing bulbs, then turning a pile of electrical bits into something that belongs in the room.":
        "Starts in the workshop. Cutting little blocks, laying out parts, wiring holders, testing "
        "bulbs.",

    "Lights are easy to buy. But a run of lighting across a room changes the feeling of the space, "
    "so it was worth making something that felt deliberate: warm, slightly industrial, and not too "
    "polished.":
        "Lights are easy to buy. A run of them across a room changes how the space feels, so it "
        "was worth making something deliberate - warm, slightly industrial, not too polished.",

    "Cut, mark, assemble, test, install, adjust, repeat. Perhaps forty times, for a job I had "
    "estimated at an afternoon.":
        "Cut, mark, assemble, test, install, adjust, repeat. About forty times, for a job I had "
        "estimated at an afternoon.",

    # --- Holding pages -----------------------------------------------------
    "Living with an electric car and being unable to leave it alone: charging behaviour, home "
    "energy data, and the slow realisation that the interesting system is the one spanning "
    "vehicle, charger, tariff and house.":
        "Living with an electric car and being unable to leave it alone. Charging behaviour, home "
        "energy data, and the slow realisation that the interesting system spans vehicle, charger, "
        "tariff and house.",

    "A wooden surfboard from an Otter course: outline, shaping, glassing and finish. Mostly a long "
    "lesson in the fact that removing material is a one-way operation.":
        "Wooden surfboard from an Otter course. Outline, shaping, glassing, finish. Mostly a long "
        "lesson in the fact that removing material is a one-way operation.",

    "An experiment in using light, shadow and geometry as a printing process. Playful, but with "
    "real constraints: the physics decides what is possible and the setup decides whether you can "
    "repeat it.":
        "Using light, shadow and geometry as a printing process. Playful, with real constraints - "
        "the physics decides what is possible, the setup decides whether you can repeat it.",

    "A boat, built to go fast. Hull shape, weight distribution and finish all stop being aesthetic "
    "choices the moment the thing is planing, which is most of the appeal.":
        "A boat, built to go fast. Hull shape, weight and finish stop being aesthetic choices the "
        "moment it is planing, which is most of the appeal.",

    "A lighting installation for a space that deserved better than a grid of downlights. Design "
    "constraints, a lot of cable, and a room that reads completely differently after dark.":
        "Lighting for a space that deserved better than a grid of downlights. Design constraints, "
        "a lot of cable, and a room that reads completely differently after dark.",

    # --- About and home ----------------------------------------------------
    "I have always liked the bit where computers meet the real world. The BBC Micro started it, "
    "mechatronics formalised it, motorsport made it noisy, SaaS made it serious, and AI/robotics "
    "has dragged all of it back into one place.":
        "I have always liked the bit where computers meet the real world. BBC Micro started it, "
        "mechatronics formalised it, motorsport made it noisy, SaaS made it serious. AI and "
        "robotics dragged all of it back into one place.",

    "I like problems that start slightly ridiculous and then become engineering. A hovercraft at "
    "GCSE, a robot CD player at A level, an award-winning robotic chessboard at university, "
    "Formula One sensors and telemetry, production systems at scale, and now robot learning. "
    "Different tools, same itch.":
        "I like problems that start slightly ridiculous and then turn into engineering. Hovercraft "
        "at GCSE. Robot CD player at A level. Robotic chessboard at university. Then F1 sensors, "
        "production systems at scale, and now robot learning.",

    "I like the point where code, data, electronics, mechanisms and people all have to agree. That "
    "has meant debugging car-stopping motorsport problems, keeping production platforms alive and "
    "building robots in a workshop. The question is always the same one: how do we know this is "
    "really working?":
        "I like the point where code, data, electronics, mechanisms and people all have to agree. "
        "Car-stopping motorsport problems, production platforms, robots in a workshop. Always the "
        "same question: how do we know this is really working?",
}


def main() -> int:
    changed = 0
    for page in html_files():
        if page.name == "cv.html":
            continue
        original = page.read_text(encoding="utf-8")
        text = apply_paragraphs(original, PARAGRAPHS)
        if text != original:
            page.write_text(text, encoding="utf-8")
            changed += 1
            print(f"  sharpen {page.relative_to(REPO)}")

    print(f"{changed} page(s) updated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
