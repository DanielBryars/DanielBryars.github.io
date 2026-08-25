# AGENTS.md

Guidance for AI coding agents working in this repository.

## What this is

The personal site of Daniel Bryars, at `daniel.bryars.com`. Static HTML and CSS
on GitHub Pages, no framework and no build step. It supports job applications,
so it has to look considered and load quickly, but it is a personal site first
and should sound like a person.

## The premise

**The site does not explain what category of engineer Daniel is. It demonstrates
that categorising him is difficult.**

That is the editorial rule everything else serves. He has done Formula One R&D,
founded and sold a SaaS company, taken an MSc in AI, and built a spiral
staircase, a drift trike and a house with curved walls. A positioning statement
makes that career sound narrower than it is; the evidence makes it sound as odd
as it actually is.

Consequences:

- The homepage headline is **"I build things."** Do not replace it with a
  grand tagline. The previous one ("systems where software has to survive
  contact with the physical world") was killed for being competent-sounding
  LinkedIn language.
- Photographs go high. The differentiator is that these objects exist, so the
  `.evidence-strip` sits directly under the hero, above any prose.
- Lead with the extraordinary: &pound;8M ARR and the exit, Formula One, the MSc
  Distinction, robot learning. They are the story, not supporting detail.
- **"How do we know this is really working?"** is the recurring motif. It ties
  F1, SaaS reliability, AI evaluation and robotics together. It appears in the
  homepage terminal panel, the About through-line and the CV summary.
- What a reader should think after ten minutes: *he has done a lot of very
  different things, and there is a common thread &mdash; he understands systems
  deeply, wants to know how they really work, and builds rather than talks.*

## Register per page

- **Home and projects**: his corner of the internet. Character, photographs,
  and things that are here because they are cool.
- **About**: the narrative. BBC Micro &rarr; mechatronics &rarr; motorsport
  &rarr; F1 &rarr; SaaS founder &rarr; exit &rarr; MSc AI &rarr; robotics
  &rarr; workshop. Keep the BBC Micro origin story; never professionalise it
  into "always been passionate about technology".
- **CV**: brutally useful to someone deciding whether to hire him. Keep a
  little personality, but let the rest of the site carry the eccentricity.
  Accomplishments first, technology second &mdash; the keyword list lives in
  one `.tool-list` block low on the page so it does not colour the document.

## Structure

- `index.html` - landing page: hero, career signal strip, selected projects, contact
- `cv.html` - CV; `@media print` in `styles.css` makes it save to a decent PDF
- `about.html` - background
- `projects/index.html` - project index: written-up projects as cards, the
  rest as a plain `.backlog` list
- `projects/<project>/index.html` - one folder per project, holding the page and
  its media together. Source photos, clips and supporting files go in
  `images/`, `videos/` and `files/`; generated web media lands in `media/` and
  is never edited by hand. MSc module pages live under
  `msc-ai/<module>/index.html` and share the programme-level folders.
- `danfest.html` - photographs from Daniel's 50th. Marked `noindex`: it is full
  of identifiable guests and is for friends, not for search engines or
  recruiters. Built by `tools/build_danfest.py`, which resizes the originals on
  import (they are ~400MB in OneDrive and must not be committed at full size).
  The invitation itself lives at `danfest.bryars.com`, a separate site.

  Three things make the gallery work, and all three are load-bearing:
  the `.photo-grid` tiles use the 480/960 derivatives; each `<figure>` carries
  an inline base64 16px version of its own frame as a background, so a blurred
  version of the right photograph is there before anything downloads; and each
  `<img>` has `data-full` pointing at the 2400px import, which
  `image-lightbox.js` prefers over the srcset when you click. `check_site.py`
  validates `data-full` like any other link.
- `styles.css` - every rule for the main site; `fonts.css` holds `@font-face`

There is one easter egg, in the homepage footer: a very faint line of shipping
forecast sea areas that plays `ShippingForecast.1stMin.ulaw.8k.wav` when
clicked. It is meant to be almost invisible. Do not "improve" its contrast,
label it, or explain it.

## Design system

Colours are custom properties at the top of `styles.css` (`--ink`, `--muted`,
`--paper`, `--line`, `--green`, `--cyan`, `--yellow`, `--pink`). Headings use
Pixelify Sans; terminal panels use VT323; body copy is a plain sans.

Recurring components: `.site-header` / `.top-nav`, `.hero`, `.signal-strip`,
`.project-card`, `.directory-card`, `.artifact-hero`, `.media-feature`,
`.video-strip`, `.artifact-gallery`, `.artifact-story`, `.cv-panel`,
`.spec-sheet`, `.backlog`, `.contact-band`, `.screen-bar`.

Reuse these before inventing new ones. Check `python tools/find_dead_css.py`
after removing markup.

## Tone

This is the part most easily got wrong.

**Judge every line on its own. Do not apply the rules below as a filter.**

An earlier revision ran pattern-based passes over the whole site - "objects do
not have feelings", "headings are labels", "cull the wry ending" - and they
destroyed as many good lines as bad ones, because a rule cannot tell a joke
that makes a point from a joke that is only decoration. Daniel's correction:

    "A robot arm, because simulated robots are too well behaved."
    ->  "A robot arm, because simulated robots are ... well, too perfect."

He did not want it removed. He wanted the ending fixed. **The test is: does
this line make a point, and does it sound like a person?** If yes, keep it and
sharpen the wording. Only flatten a line that was carrying nothing.

Character is wanted. "Building the printer that prints the next problem",
"The kitchen was not finished. The steel was.", "Deeply unnecessary, which is
not the same thing as wrong" - all keepers, all technically matching a banned
pattern. Everything below is a description of habits to watch for, not a
list of strings to search and destroy.

The reference is three rewrites Daniel did by hand. Match these before writing
anything:

| Too wordy | His version |
| --- | --- |
| "There is no lesson here. It looks fantastic, so I filmed it. That is the entire reason this page exists." | "There is no lesson here. Posted because I want to, it looks awesome" |
| "No report, no write-up, no retrospective. It finishes with a child on the grass going sideways, which is the only outcome anyone involved cared about." | "Child on the grass going sideways, the only outcome I really care about." |
| "The desk is fine. The better part was building it with my son: measuring, checking, and disagreeing about which way round the top should go." | "Desk is fine. Getting my son involved in building 'real things away from the virtual world' - awesome." |

What those show:

- **Half the words.** Mean paragraph length across the project pages is ~22
  words. Cut every framing clause: "It finishes with", "The better part was",
  "That is the reason", "This is the part where".
- **Stop at the point.** Do not add a closing sentence explaining what you just
  said. That closer is the single most reliable tell.
- **Telegraphic.** "Desk is fine", not "The desk is fine". Drop articles and
  subject pronouns wherever someone jotting a note would.
- **First person, present tense, owned.** "the only outcome I really care
  about", not "anyone involved cared about". Do not hide in the passive.
- **Loose punctuation.** Comma splices and dashes are fine. Terminal full stops
  on short fragments are optional.
- **Enthusiasm is wanted.** "awesome" is his word. The ban is on self-praise,
  not on warmth - an earlier pass stripped both and left the site flat.
- **No tricolons, no colon-lists of process verbs.** That rhythm is not his.
- Dry, specific, understated. British. First person.
- **Never self-congratulate.** This is the one that keeps coming back. The copy
  must not award itself marks: nothing is done "properly", no project is
  "exactly the kind of project I like", nothing is "satisfying", and an
  unfinished thing is never "already full of useful lessons". Prefer admitting
  the cost. Daniel's own correction is the reference:

      "Still in progress, already full of useful lessons."
      ->  "Still in progress. And taking longer than I thought!"

- **No sentences that sound meaningful and say nothing.** "I like that this
  project goes from simulation to physical work without changing personality"
  is the canonical example of what not to write. If a sentence would survive
  being moved to a different project's page, delete it.
- **Headings are labels, not epigrams.** The site once had 149 headings that
  were all short fragments ending in a full stop. Default to a plain noun
  phrase with no full stop, naming the actual thing ("Cycloidal reducers",
  "Building the steam box"). A handful of epigrams survive on purpose; check
  `python tools/heading_shapes.py` before adding another.
- **Jokes are seasoning, not structure.** Roughly one in four captions should
  be plainly descriptive. Never reuse a joke shape: objects do not "have
  opinions", "choose violence", or exhibit "perfectly normal X behaviour".
- Ban the "not just X, it is Y" construction outright. It is always inflation.
- Prefer a real fact to a wry observation. "24 V, 500 W hub motor" beats
  "the useful end of the machine". Describe the thing, not the category of
  thing: name the part, the choice and what it cost.
- Never write copy addressed to a future editor, and never write about the page
  itself: no "add photos here", no "later we can", no "the raw footage is", no
  "I have kept the selection small", no "we". If content is missing, say so once
  in the reader's terms or say nothing.
- `python tools/voice_check.py` counts these tics; run it after editing copy.

## Content rules

- Every project page should carry a `.spec-sheet` block. Placeholders show
  `DRAFT` in the screen bar and `class="tbc"` on unfilled values. Daniel fills
  these in by hand; do not invent specifications, costs or timings.
- Pages with no real content get `<meta name="robots" content="noindex">` and
  stay out of the project index until they have something to show.
- Factual claims must agree across pages. Career length is derived from the CV
  timeline starting in 1997.

## Media

Originals live in `projects/<project>/images/`, `videos/` and `files/`. Never
reference them directly from a page and never resize them in place. Instead:

```bash
python tools/make_derivatives.py    # 480/960/1600px JPEG, 720p MP4 -> media/
python tools/rewrite_media.py       # srcset, sizes, width/height, loading
```

Generated project media lands in `projects/<project>/media/`. Site-level and
danfest media still use the older `derived/` mirror, alongside the originals in
`project-assets/danfest/`.

`rewrite_media.py` points every `<img>` at the generated copy, adds intrinsic
dimensions, marks the first image on a page `eager`/`fetchpriority=high` and
everything else `lazy`, and switches `<video>` to the 720p transcode with
`preload="none"`.

## Head and accessibility

`tools/rewrite_head.py` owns the block between `<!-- head:meta -->` and
`<!-- /head:meta -->`: canonical URL, Open Graph, Twitter card, icons, and the
Person JSON-LD on the landing page. Edit the script, not the generated block.
Per-page share images are registered in its `PAGE_IMAGES` map.

`tools/rewrite_skiplink.py` adds the skip link and `id="main"`.

Keep: visible `:focus-visible` outlines, the `prefers-reduced-motion` block
(`bbcb-demo.html` has its own copy for its blink and flash animations), and
alt text on every image that carries meaning.

All four rewrite scripts are idempotent. Run them over the whole site after
adding pages.

## The printed CV

`cv.html` has a full `@media print` treatment that sets it like a LaTeX thesis:
A4, serif face, justified with hyphenation, numbered sections, and a centred
title block (`.print-titleblock`, hidden on screen) carrying name and contact
details. Everything screen-only is removed.

The screen rules are specific enough that print overrides need `!important` on
sizes, and `main, main *` forces the serif face &mdash; otherwise Pixelify Sans
leaks into headings, dates and definition terms.

Check changes by rendering, not by reading:

```bash
"/c/Program Files (x86)/Microsoft/Edge/Application/msedge.exe" \
  --headless=new --disable-gpu --no-pdf-header-footer \
  --print-to-pdf=out.pdf file:///absolute/path/to/cv.html
```

The same binary screenshots pages with `--screenshot --window-size=1400,1200`,
which is the only way to catch layout bugs in this repo.

## Deployment

Push to `master`; GitHub Pages does the rest. Run `./update-build-info.sh`
first so the footer stamp matches the commit.

## Repository size

The originals under `projects/<project>/images/` and `project-assets/danfest/`
run to several hundred MB, with the generated copies on top. Import large
photographs at 2400px rather than full camera resolution, as
`tools/build_danfest.py` does. Before adding a large batch, consider whether the
originals belong in the repository at all.
