# Source references

What each published asset was made from, so it can be found again and re-cut
without hunting for it.

Pages live at `projects/<slug>/index.html`. Source photos, clips and documents
sit beside the page in `images/`, `videos/` and `files/`. Generated web copies
land in `media/` and are never edited by hand — regenerate them with
`tools/make_derivatives.py`, then `tools/rewrite_media.py`.

Clip extraction recipes, with timecodes, live in `tools/enrich_project_media.py`.

## Where the raw material lives

| Project | Raw source |
| --- | --- |
| 3D Printers | `\\192.168.1.13\Public\Video\Daniel\3dPrinter` (photos in `\Photos`) |
| Active Speakers | `F:\video\speakers`, `\\192.168.1.13\YouTubeVideo\Daniel\Speakers`, `C:\Users\bryar\OneDrive\Documents\Projects\Speakers`, code in `D:\git\KingRO4Y` |
| Belly Board | supplied directly into the repo; no external folder recorded |
| Corten Balustrade | **not recorded** — see Unresolved below |
| Curving Skirting Board | `\\192.168.1.13\Public\Video\Daniel\Curved Skirtingboard` |
| CV in a Box | supplied directly into the repo |
| Drift Trike | `\\192.168.1.13\Public\Video\Daniel\Drift Trike` |
| Home Assistant | relay-panel photographs supplied into the repo |
| Lathe Sparks | `\\192.168.1.13\Public\Video\Daniel\Lathe` |
| Mega Book Case | `\\192.168.1.13\Public\Video\Daniel\Book Case` |
| Motorised Standing Desk | `F:\video\desk-project` |
| Robot Arm | `\\192.168.1.13\Public\Video\Daniel\RobotArm` |
| Spiral Staircase | `\\192.168.1.13\Public\Video\Daniel\SpiralStairCase\Video` |
| Vintage String Lights | `\\192.168.1.13\YouTubeVideo\Daniel\Vintage String Lights` |
| MSc modules | `C:\Users\bryar\OneDrive\Documents\Leeds` |
| MLX course projects | GitHub repos, listed below |

## 3D Printer Build

Photos, from `\3dPrinter\Photos`:

| Source | Asset |
| --- | --- |
| `DSC03389.JPG` | `01-prusa-mk4-toolhead.jpg` |
| `DSC03390.JPG` | `08-toolhead-front-fan.jpg` |
| `DSC03391.JPG` | `02-heated-bed-closeup.jpg` |
| `DSC03392.JPG` | `09-heatbed-print-surface.jpg` |
| `DSC03395.JPG` | `10-rear-cable-exit.jpg` |
| `DSC03396.JPG` | `03-frame-and-print-head.jpg` |
| `DSC03397.JPG` | `11-belt-and-rod-perspective.jpg` |
| `DSC03399.JPG` | `04-toolhead-rods-detail.jpg` |
| `DSC03400.JPG` | `12-toolhead-depth-of-field.jpg` |
| `DSC03405.JPG` | `13-nozzle-over-bed.jpg` |
| `DSC03409.JPG` | `05-extruder-hinges-detail.jpg` |
| `DSC03410.JPG` | `14-extruder-motor-detail.jpg` |
| `DSC03411.JPG` | `06-leadscrew-orange-block.jpg` |
| `DSC03412.JPG` | `15-leadscrew-thread-detail.jpg` |
| `DSC03414.JPG` | `07-control-screen.jpg` |
| `DSC03415.JPG` | `16-control-display-closeup.jpg` |

Clips, first pass. Only six of these were kept as sources in `videos/`; the
rest exist in the repo solely as the 720p copy in `media/`, so re-cutting them
at a different length means going back to the share.

Clips, first pass:

| Source | From | Length | Asset |
| --- | --- | --- | --- |
| `C0330.MP4` | `00:00:50` | 30s | `clip-unboxing.mp4` |
| `C0331.MP4` | `00:01:35` | 45s | `clip-decoration-fixing.mp4` |
| `C0331.MP4` | `00:06:45` | 30s | `clip-rods-on-bench.mp4` |
| `C0331.MP4` | `00:16:25` | 45s | `clip-decoration-welding.mp4` |
| `C0335.MP4` | `00:20:10` | 60s | `clip-main-frame-uprights.mp4` |
| `C0340.MP4` | `00:15:45` | 30s | `clip-stepper-connector-detail.mp4` |
| `C0341.MP4` | `00:00:14` | 120s | `clip-bearing-macro.mp4` |
| `C0342.MP4` | `00:12:00` | 45s | `clip-orange-parts-assembly.mp4` |
| `C0344.MP4` | `00:15:40` | 30s | `clip-x-axis-carriage.mp4` |
| `C0347.MP4` | `00:06:50` | 30s | `clip-frame-assembly.mp4` |
| `C0348.MP4` | `00:19:35` | 30s | `clip-toolhead-install.mp4` |
| `C0353.MP4` | `00:08:55` | 60s | `clip-hotend-small-parts.mp4` (re-cut; first pass had no audio) |
| `C0356.MP4` | `00:17:08` | 30s | `clip-extruder-fan-detail.mp4` |
| `C0357.MP4` | `00:01:55` | 30s | `clip-toolhead-mounted.mp4` |
| `C0359.MP4` | `00:00:50` | 30s | `clip-wiring-electronics.mp4` |
| `C0361.MP4` | `00:02:10` | 30s | `clip-heatbed-wiring.mp4` |
| `C0379.MP4` | `00:21:10` | 30s | `clip-rear-loom-routing.mp4` |
| `C0380.MP4` | `00:10:45` | 45s | `clip-late-underframe-detail.mp4` |
| `C0380.MP4` | `00:12:15` | 30s | `clip-final-cable-routing.mp4` |
| `C0381.MP4` | `00:00:55` | 30s | `clip-finished-printer.mp4` |
| `C0381.MP4` | `00:44:40` | 60s | `clip-final-bench-rotation.mp4` |

Clips, second pass from previously unused footage:

| Source | From | Length | Asset |
| --- | --- | --- | --- |
| `C0332.MP4` | `00:00:05` | 40s | `extra-piece-to-camera.mp4` |
| `C0333.MP4` | `00:00:45` | 35s | `extra-unboxing-overhead.mp4` |
| `C0336.MP4` | `00:04:30` | 30s | `extra-frame-uprights-overhead.mp4` |
| `C0339.MP4` | `00:20:30` | 30s | `extra-electronics-board.mp4` |
| `C0343.MP4` | `00:07:20` | 30s | `extra-bearings-on-rods.mp4` |
| `C0345.MP4` | `00:01:20` | 30s | `extra-x-axis-overhead.mp4` |
| `C0346.MP4` | `00:02:30` | 30s | `extra-orange-parts-overhead.mp4` |
| `C0349.MP4` | `00:14:30` | 40s | `extra-loom-connectors.mp4` |
| `C0355.MP4` | `00:15:30` | 35s | `extra-extruder-assembly.mp4` |
| `C0355.MP4` | `00:18:20` | 30s | `extra-extruder-mounting.mp4` |
| `C0358.MP4` | `00:19:00` | 40s | `extra-display-module.mp4` |
| `C0360.MP4` | `00:00:15` | 30s | `extra-machine-complete.mp4` |
| `C0378.MP4` | `00:06:30` | 30s | `extra-heatbed-wiring-overhead.mp4` |

Not used: `C0334`, `C0337`, `C0338`, `C0350`, `C0351` are 3-11 second fragments;
`C0377` is camera-rig repositioning; `C0352` is unwrapping bagged parts; `C0354`
duplicates the hotend parts covered by `C0353`.

Filament storage photos: camera originals `DSC09789.JPG`, `DSC09792.JPG`,
`DSC09795.JPG`, `DSC09796.JPG`, imported at 2400px into
`images/filament-storage/`. The 6000px originals were deleted.

Firmware regression evidence, saved from Daniel's own GitHub comments:

- `firmware-62-layer-shift-result.jpg`, `firmware-613-success-result.jpg`,
  `firmware-arctos-gears-comparison.jpg`
- Prusa-Firmware-Buddy issues
  [4465](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/4465#issuecomment-2660022554),
  [4487](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/4487#issuecomment-2665450594),
  [6.2.2 fix](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/4465#issuecomment-2700234456)

## Robot Arm

Photos, from `\RobotArm\Pictures`:

| Source | Asset |
| --- | --- |
| `DSC09186.JPG` | `01-printer-making-arm-parts.jpg` |
| `DSC09190.JPG` | `02-printed-coupler-on-bed.jpg` |
| `DSC09193.JPG` | `03-printer-in-progress.jpg` |
| `DSC09218.JPG` | `04-workshop-context.jpg` |
| `DSC09219.JPG` | `05-workshop-wide.jpg` |
| `DSC09221.JPG` | `06-rods-and-fasteners.jpg` |
| `DSC09222.JPG` | `07-cycloidal-joint-closeup.jpg` |
| `DSC09223.JPG` | `08-joint-side-by-side.jpg` |

Clips, paths relative to `\RobotArm`:

| Source | From | Length | Asset |
| --- | --- | --- | --- |
| `Printing\C1339.MP4` | `00:00:28` | 12s | `clip-printing-arm-parts.mp4` |
| `ServoMotors\C1365.MP4` | `00:01:55` | 14s | `clip-servo-electronics.mp4` |
| `Smaller Cycloidal\C1381.MP4` | `00:01:55` | 14s | `clip-cycloidal-layout.mp4` |
| `Smaller Cycloidal\C1403.MP4` | `00:00:55` | 14s | `clip-joint-hand-test.mp4` |
| `Smaller Cycloidal\C1424.MP4` | `00:05:55` | 14s | `clip-arm-assembly.mp4` |
| `NotSure\C1503.MP4` | `00:29:55` | 12s | `clip-metalwork-welding.mp4` |

Other folders on the share: `\A AXIS`, `\Printing`, `\ServoMotors`,
`\Smaller Cycloidal`, `\NotSure`, `\Pictures`.

## Drift Trike

Clip references supplied by Daniel, relative to `\Drift Trike`:

| Source | Timecode | What it shows |
| --- | --- | --- |
| `Finished2\C1251.MP4` | `00:30`-`01:00` | Lincoln driving it |
| `20230102_001732.MOV` | `05:00` | Lincoln putting the wheels on |
| `C1032.MP4` | `00:53`-`01:14` | welding, through the filter |
| `C1033.MP4` | `00:32` | finished welded frame |
| `C1046.MP4` | — | making up wires |
| `C1058.MP4` | `06:28` | first motor and electronics test |
| `C1065.MP4` | `01:20`-`01:58` | welding |
| `C1066.MP4` | `14:05`-`14:25` | — |
| `C1078.MP4` | `08:46`-`09:00` | Lincoln learning to tap a thread |
| `C1097.MP4` | `04:40` | slow-motion drilling |
| `C1103.MP4` | `01:57` | — |
| `C1106.MP4` | `01:02` | belt sanding |
| `C1126.MP4` | `04:28`-`04:40` | plasma cutting |
| `C1701.MP4` | `01:17`-`01:53` | — |
| `C1702.MP4` | `00:42`-`01:52` | — |

## Spiral Staircase

Clips, from `\SpiralStairCase\Video`. Sources identified by frame matching in
August 2026, when the originals were found to have no audio track and were
re-cut.

| Source | From | Length | Asset |
| --- | --- | --- | --- |
| `C0099.MP4` | `00:06:45` | 22s | `clip-overhead-before.mp4` |
| `C0108.MP4` | `00:10:55` | 28s | `clip-working-on-handrail.mp4` |
| `C0114.MP4` | `00:07:45` | 28s | `clip-cutting-curved-rail.mp4` |

## Vintage String Lights

Clips, re-cut with audio in August 2026 after the originals were found silent.

| Source | From | Length | Asset |
| --- | --- | --- | --- |
| `C0249.MP4` | `00:00:38` | 18s | `clip-cutting-blocks.mp4` |
| `C0252.MP4` | `00:07:50` | 22s | `clip-wiring-and-test.mp4` |
| `C0254.MP4` | `00:04:45` | 25s | `clip-installing-lights.mp4` |

## Motorised Standing Desk

| Source | From | Length | Asset |
| --- | --- | --- | --- |
| `C1665.MP4` | `00:00:38` | 28s | `clip-finished-top.mp4` |

`clip-tabletop-build.mp4` is still silent: no confident match was found in
`F:ideo\desk-project`.

## Active Speakers

FreeCAD walkthrough: screen recording `2026-08-25 18-07-08.mp4`, 1724x720,
106 seconds, imported as `freecad-walkthrough.mp4`. It arrived at -52.5 LUFS,
about 36dB below a normal web level, so the audio was normalised to -16 LUFS
with a two-pass EBU R128 pass and the video stream copied untouched. The source
targets -3 dBTP rather than -1.5: at -1.5 the 96k AAC web copy overshot to
0 dBTP, and the extra headroom leaves the derived copy at -1.1. Full length, no
trim. Poster frame from `00:00:10`.

Build clips and stills came from `F:\video\speakers`: routing, rear-baffle work,
sanding, plate-amp fitting, driver fitting and finished measurement photos.

## Corten Balustrade

Stills supplied by Daniel:

- `_MG_8675.CR2` (converted to JPEG), `_MG_8924.jpg`, `20191116_215127.jpg`,
  `20191102_142400.jpg`, `LastFew.jpg`
- `Screenshot 2025-03-27 201258.png` for the FEA design check

## Belly Board

`projects/belly-board/files/selected/README.md` maps each `DSC0____.JPG` to its
published image.

## Lathe Sparks

`projects/lathe-sparks/files/README.md` lists the selected stills and the three
1080p clips kept for the page. Raw originals were removed after selection.

## MSc Artificial Intelligence

Module pages at `projects/msc-ai/<module>/index.html`. All module material comes
from `C:\Users\bryar\OneDrive\Documents\Leeds`, in each module's assessment
folder.

The Data Mining and Text Analytics "Muppet test" comes specifically from
`OCOM5204M Data Mining and Text Analytics\Assessment2\Research Proposal.docx`
and its submitted PDF.

## MLX course projects

Page: `projects/msc-ai/mlx-course-projects/index.html`. Built from repo READMEs
and code, not course material. The architecture diagram was drawn for the site.

- `E:\git\MLX3-VisionTransformers` / https://github.com/DanielBryars/MLX3-VisionTransformers
- https://github.com/DanielBryars/MLX4-Decoder-Visual-Captioning
- https://github.com/DanielBryars/MLX5-Audio-Processing
- https://github.com/DanielBryars/MLX6-fine-tuning
- https://github.com/DanielBryars/predicting_hackernews_upvotes
- `E:\git\two-towers-search` / https://github.com/DanielBryars/two-towers-search
- https://github.com/DanielBryars/word2vec
- MLX course: https://ml.institute/

## No source trail yet

Add one when material arrives: Arduino Inverted Pendulum, BBC Micro Teletext,
Ben Eater 8-Bit Computer, Chess Board, Clock Project, Diffvantage, House Build,
Otter Surfboard, Physical Design and Analysis, Robot Learning MSc, Shadow
Printing, Speed Boat.

## Unresolved

- **Corten Balustrade footage.** `clip-cutting-slats.mp4` (chop saw) and
  `clip-welding-frame.mp4` (TIG welding) have no audio track and no recorded
  source folder, so they cannot be re-cut with sound until the raw footage is
  found. It is not under `\\192.168.1.13\Public\Video\Daniel\`.
