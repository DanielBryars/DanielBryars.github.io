# AGENTS.md

Guidance for AI coding agents working in this repository.

## What this is

The personal site of Daniel Bryars, at `daniel.bryars.com`. Static HTML and CSS
on GitHub Pages, no framework and no build step. It supports job applications,
so it has to look considered and load quickly, but it is a personal site first
and should sound like a person.

## Structure

- `index.html` - landing page: hero, career signal strip, selected projects, contact
- `cv.html` - CV; `@media print` in `styles.css` makes it save to a decent PDF
- `about.html` - background
- `cool-projects/index.html` - project index: written-up projects as cards, the
  rest as a plain `.backlog` list
- `cool-projects/*.html` - one page per project
- `bbcb-demo.html` - self-contained teletext page with its own inline styles
- `styles.css` - every rule for the main site; `fonts.css` holds `@font-face`

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

- Dry, specific, understated. British. First person.
- **Jokes are seasoning, not structure.** An earlier revision put a wry
  one-liner in every single heading and caption, and the effect was numbing.
  Roughly one in four captions should be plainly descriptive.
- Never reuse a joke shape. Objects do not "have opinions", "choose violence",
  or exhibit "perfectly normal X behaviour". If a construction already appears
  once on the site, find a different one.
- Prefer a real fact to a wry observation. "24 V, 500 W hub motor" beats
  "the useful end of the machine".
- Never write copy addressed to a future editor: no "add photos here", no
  "later we can", no "this page now has the right shape", no "we". If content
  is missing, say so once in the reader's terms or say nothing.

## Content rules

- Every project page should carry a `.spec-sheet` block. Placeholders show
  `DRAFT` in the screen bar and `class="tbc"` on unfilled values. Daniel fills
  these in by hand; do not invent specifications, costs or timings.
- Pages with no real content get `<meta name="robots" content="noindex">` and
  stay out of the project index until they have something to show.
- Factual claims must agree across pages. Career length is derived from the CV
  timeline starting in 1997.

## Media

Originals live in `project-assets/<project>/`. Never reference them directly
from a page and never resize them in place. Instead:

```bash
python tools/make_derivatives.py    # 480/960/1600px JPEG, 720p MP4 -> derived/
python tools/rewrite_media.py       # srcset, sizes, width/height, loading
```

`rewrite_media.py` points every `<img>` at `derived/`, adds intrinsic
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

## Deployment

Push to `master`; GitHub Pages does the rest. Run `./update-build-info.sh`
first so the footer stamp matches the commit.

## Repository size

`project-assets/` holds full-size originals and is already several hundred MB,
with `derived/` on top. Before adding a large batch, consider whether the
originals belong in the repository at all.
