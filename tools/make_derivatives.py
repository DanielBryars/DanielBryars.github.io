"""Generate web-sized images and videos into derived/.

Originals stay exactly where they are; nothing here is destructive. Run after
dropping new media into project-assets/ and then run tools/rewrite_media.py.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageOps

from media_common import (
    DERIVED,
    IMAGE_WIDTHS,
    RASTER_SUFFIXES,
    REPO,
    VIDEO_SUFFIXES,
    derived_path,
    referenced_media,
)

MANIFEST = REPO / "tools" / "media-manifest.json"

# Long-edge cap and quality for the largest derivative.
JPEG_QUALITY = 82

# Video: 720p, reasonably aggressive, faststart so it can begin before download.
VIDEO_HEIGHT = 720
VIDEO_CRF = 28


def build_image(source: Path, manifest: dict) -> None:
    key = str(source.relative_to(REPO)).replace("\\", "/")
    with Image.open(source) as im:
        im = ImageOps.exif_transpose(im)
        width, height = im.size
        entry = {"width": width, "height": height, "widths": []}

        for target_width in IMAGE_WIDTHS:
            if target_width > width:
                continue
            out = derived_path(source, f"-{target_width}.jpg")
            entry["widths"].append(target_width)
            if out.exists() and out.stat().st_mtime >= source.stat().st_mtime:
                continue
            out.parent.mkdir(parents=True, exist_ok=True)
            target_height = round(height * target_width / width)
            resized = im.convert("RGB").resize(
                (target_width, target_height), Image.LANCZOS
            )
            resized.save(out, "JPEG", quality=JPEG_QUALITY, optimize=True, progressive=True)
            print(f"  image {out.relative_to(REPO)}")

    manifest[key] = entry


def build_video(source: Path, manifest: dict) -> None:
    key = str(source.relative_to(REPO)).replace("\\", "/")
    out = derived_path(source, "-720.mp4")
    manifest[key] = {"web": str(out.relative_to(REPO)).replace("\\", "/")}
    if out.exists() and out.stat().st_mtime >= source.stat().st_mtime:
        return
    out.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        "ffmpeg", "-y", "-loglevel", "error", "-i", str(source),
        "-vf", f"scale=-2:'min({VIDEO_HEIGHT},ih)'",
        "-c:v", "libx264", "-crf", str(VIDEO_CRF), "-preset", "slow",
        "-pix_fmt", "yuv420p", "-profile:v", "high", "-level", "4.0",
        "-c:a", "aac", "-b:a", "96k", "-movflags", "+faststart",
        str(out),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"  !! ffmpeg failed for {source.name}: {result.stderr.strip()[:200]}")
        return
    print(f"  video {out.relative_to(REPO)}")


def main() -> int:
    manifest: dict = {}
    if MANIFEST.exists():
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))

    images: set[Path] = set()
    videos: set[Path] = set()
    missing: set[str] = set()

    for page, kind, url, target in referenced_media():
        if not target.exists():
            missing.add(f"{page.relative_to(REPO)} -> {url}")
            continue
        if DERIVED in target.parts:
            continue
        if target.suffix.lower() in RASTER_SUFFIXES:
            images.add(target)
        elif target.suffix.lower() in VIDEO_SUFFIXES:
            videos.add(target)

    print(f"{len(images)} images, {len(videos)} videos referenced")

    for source in sorted(images):
        build_image(source, manifest)
    for source in sorted(videos):
        build_video(source, manifest)

    MANIFEST.write_text(json.dumps(manifest, indent=2, sort_keys=True), encoding="utf-8")

    if missing:
        print("\nreferenced but missing:")
        for item in sorted(missing):
            print(f"  {item}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
