# Derived Media

Generated site-level and DanFest web media lives here.

Do not edit these files by hand. They are produced from source media by:

```bash
python tools/make_derivatives.py
python tools/rewrite_media.py
```

Images are resized to 480, 960 and sometimes 1600 pixels wide. Videos are
transcoded to 720p MP4 for the site.

Project-specific generated files now live in `../projects/<project>/media/`.
