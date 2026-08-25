# daniel.bryars.com

Personal site of Daniel Bryars: CV, project write-ups and a workshop full of
things that were supposed to take one weekend.

Static HTML and CSS, no framework, no build step. Hosted on GitHub Pages at
[daniel.bryars.com](https://daniel.bryars.com) (see `CNAME`), deployed
automatically on every push to `master`.

## Layout

| Path | What it is |
| --- | --- |
| `index.html` | Site landing page: intro, selected projects, contact |
| `cv.html` | CV, with a print stylesheet so it saves to a sensible PDF |
| `about.html` | Background and origin story |
| `projects/index.html` | Projects landing page: the list/grid of project write-ups |
| `projects/<project>/index.html` | One folder per project, with the page and its media together |
| `bbcb-demo.html` | A Ceefax-style teletext page, standalone styles |
| `styles.css` | Every stylesheet rule for the main site |
| `fonts.css` | Local `@font-face` declarations (VT323) |
| `projects/<project>/images/`, `videos/`, `files/` | Original project photos, clips and supporting files |
| `projects/<project>/media/` | Generated web-sized project media (do not edit by hand) |
| `project-assets/` | Remaining non-project source assets, currently DanFest |
| `derived/` | Generated site-level and DanFest media (do not edit by hand) |
| `tools/` | Python maintenance scripts, see below |
| `images/` | Site-level images, share card, touch icon |
| `ontology/`, `video/`, `*.wav` | Odds and ends used by individual pages |

## Design

Dark editorial layout: Pixelify Sans headings, VT323 for terminal panels, a
yellow/cyan/green accent set defined as custom properties at the top of
`styles.css`. The retro-computing references are deliberate but kept to a few
places, so they read as a choice rather than a theme.

## Adding a project

1. Create `projects/<project-name>/`.
2. Drop the original photos and clips into `images/`, `videos/` or `files/`
   inside that project folder.
3. Copy an existing `projects/<project-name>/index.html` as a starting point,
   and add a card to `projects/index.html`.
4. Regenerate and wire up the media:

   ```bash
   python tools/make_derivatives.py    # resize images, transcode video
   python tools/rewrite_media.py       # srcset, width/height, lazy loading
   python tools/rewrite_head.py        # canonical, share card, icons
   python tools/rewrite_skiplink.py    # skip-to-content link
   ```

   All four are idempotent, so running them over the whole site is safe.
5. Fill in the `BUILD SPEC` block. Pages still carrying placeholders are listed
   by `rg -l 'data-spec="draft"' projects`.
6. Refresh the footer build stamp with `./update-build-info.sh`.

## Tools

| Script | Does |
| --- | --- |
| `make_derivatives.py` | Writes 480/960/1600px JPEGs and 720p MP4s into `derived/` |
| `rewrite_media.py` | Points `<img>`/`<video>` at the derivatives, adds dimensions and lazy loading |
| `rewrite_head.py` | Canonical URL, Open Graph and Twitter cards, icons, JSON-LD |
| `rewrite_skiplink.py` | Adds the skip link and `id="main"` |
| `find_dead_css.py` | Lists CSS classes no page uses any more |
| `add_spec_sheets.py` | Inserts the build-spec block into a project page |
| `tone_pass.py`, `stub_copy.py`, `stub_headings.py` | One-off copy edits, kept for reference |

Requires Python with Pillow, and `ffmpeg` on the path for video.

## Local preview

```bash
python -m http.server
```

Then open <http://localhost:8000>. Opening the files directly works too, but
root-relative paths and `fetch` for the build stamp will not.

## Licence

Content and design © Daniel Bryars.
