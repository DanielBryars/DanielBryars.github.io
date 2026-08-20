"""Daniel's explicit picks, chosen line by line.

This table outranks every other pass in tools/. When the automated passes and
this file disagree, this file is right - these are choices he made looking at
the two versions side by side.

The pattern that emerged as he chose: **section headings stay plain labels,
captions are allowed character.** He took the flat option for headings
("Fabricating in a half-built house", "Connectors and wiring", "Joints and
reduction", "State representation") and the funny option for captions ("The
Victorian inventor's shed", "The little screen of imminent calibration
optimism"). Two captions he wrote himself.

    python tools/choices_pass.py
"""

from __future__ import annotations

import sys

from media_common import REPO, html_files
from textedit import apply_snippets

CHOICES = {
    # --- headings: he picked plain every time -------------------------------
    "<h2>The kitchen was not finished. The steel was.</h2>":
        "<h2>Fabricating in a half-built house</h2>",
    "<h2>Connectors are tiny commitments</h2>": "<h2>Connectors and wiring</h2>",
    "<h2>Torque is where the optimism runs out</h2>": "<h2>Joints and reduction</h2>",
    "<h2>The state is the interface</h2>": "<h2>State representation</h2>",
    "<h2>Structure is information</h2>": "<h2>Data structures</h2>",
    "<h2>Runtime has teeth</h2>": "<h2>Runtime and growth</h2>",
    "<h2>Not one magic classifier</h2>": "<h2>Model comparison</h2>",
    "<h2>Optimise the real objective</h2>": "<h2>Cost-based evaluation</h2>",
    # kept as an assertion by his choice: "Tell it what good means" (reward design),
    # "Data has politics" and "Engineering needs a conscience" (both MSc Ethics)
    "<h1>Power, Not Performance</h1>": "<h1>Ethics of AI</h1>",
    "<h2>Law lags deployment</h2>": "<h2>Tech ships before the rules do.</h2>",
    "<h2>Absence is not falsehood</h2>": "<h2>Do not mistake absence for falsehood</h2>",
    "<h2>The model is only part of the system</h2>": "<h2>Systems around the model</h2>",
    # kept as assertions by his choice: "Meaning needs engineering" (KRR),
    # "Training is an engineering problem" (MLX)

    # --- captions: he picked character, or wrote his own --------------------
    # kept as-is: "The Victorian inventor's shed, but with better stepper drivers"
    # kept as-is: "The little screen of imminent calibration optimism"
    "<figcaption>The designer with the object, looking worryingly pleased with himself</figcaption>":
        "<figcaption>If this doesn't work, I don't want to work for you</figcaption>",
    "<figcaption>But will it work?</figcaption>":
        "<figcaption>If this doesn't work, I don't want to work for you</figcaption>",
    "<figcaption>The hero shot. Gratuitous, yes. Wrong, no.</figcaption>":
        "<figcaption>Gratuitous photo</figcaption>",

    # --- CV in a Box hero: he preferred the plainer opening -----------------
    "A CV packaged like old software. Deeply unnecessary, which is not the same thing as\n"
    "                        wrong. It took far longer than writing a CV.":
        "A CV packaged like old software. Completely unnecessary, took far longer than writing\n"
        "                        a CV.",
    "<p>A physical CV packaged like old software. Deeply unnecessary, which is not the same thing "
    "as wrong.</p>":
        "<p>A physical CV packaged like old software. Completely unnecessary, and it took far "
        "longer than writing a CV would have.</p>",
}


def main() -> int:
    changed = 0
    for page in html_files():
        original = page.read_text(encoding="utf-8")
        text = apply_snippets(original, CHOICES)
        if text != original:
            page.write_text(text, encoding="utf-8")
            changed += 1
            print(f"  choice {page.relative_to(REPO)}")

    print(f"{changed} page(s) updated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
