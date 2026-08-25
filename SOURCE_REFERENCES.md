# Source references

> Project folder note: on 2026-08-25 the public project pages moved from `cool-projects/*.html` to `projects/<slug>/index.html`. Project source media now lives beside each page in `images/`, `videos/` or `files/`, with generated web media in `media/`. The old `cool-projects/` folder has been removed.

This file records where the raw material came from for the project and academic pages assembled during the Codex/ChatGPT site-building session. It is intentionally practical: local paths, network shares, repo links, and notes about conversion or curation.

Do not publish files from the source folders blindly. Some sources are personal media, some are course material, and some include third-party papers or assignment briefs. The website should use only curated outputs, original photographs/videos, generated diagrams, or short descriptions.

## Site-wide work

### Home page, projects index, about page, CV page and shared styling

- Site repo: `E:\git\DanielBryars.github.io`
- Main pages: `index.html`, `about.html`, `cv.html`, `projects\index.html`
- Shared stylesheet: `styles.css`
- Notes: visual styling and page structure were updated in-place in the site repo. Treat this repo as the source of record for the final HTML/CSS, with project-specific sources listed below.

### Cross-chat references reviewed

- `Improve Website Copy` chat: supplied the main site-positioning direction now used on the home/about pages: "Engineer. Programmer. Founder.", "I build things.", the BBC Micro to mechatronics to motorsport/F1 to SaaS to AI/robots arc, and the recurring "How do we know this is really working?" theme.
- `Website tagline comparison` chat: reinforced the unfinished-project tone, especially "Still in progress" rather than over-selling incomplete work.
- `Topping to Hypex Debug` chat: useful future material for the active-speakers/ESP32 controller project. Details include vinyl -> preamp -> miniDSP -> Toslink -> Topping -> XLR -> Hypex, XLR/RCA input debugging, Hypex input selection, mute/volume state, and using Wireshark/reverse engineering around the USB controller.
- `EV Charger Near TA15` chat and current job-search/site chat: useful future material for the MG EV / smart-lead project. Published page now mentions the ESP32/custom-circuit-board smart-lead idea; the charger-location chat itself is travel context, not build evidence.
- `Pilot hole advice` chat: useful future material for house/pergola writeups if they appear. It mentions 6mm Timberwolf structural timber screws, C24 softwood, and pergola-sized timbers.
- `Interview Prep` chat: useful for future CV/interview positioning around robot learning, but be careful with it on the website. It includes final-project/dissertation details such as VLA-style ambitions, local inference limits, simplifying toward ACT, spatial coordinates, debugging tooling, simulated-to-real evaluation and physical benchmark thinking. Do not paste this into the MSc module pages without Daniel explicitly deciding to publish final-project material.
- `Explain VLA Models` and `Explain DDP FSDP DeepSpeed` chats: useful learning notes for Daniel, but not original project evidence. Treat them as background only unless a future page explicitly explains what Daniel studied.
- `URScript result returns` chat: useful future material for professional robotics/control notes. It discusses using URScript return values internally, socket result messages, and RTDE registers for command/result state.

### Extra media expansion pass

- Extraction recipe: `tools\enrich_project_media.py`
- Output folder: `derived\project-assets`
- Notes: this script records the raw video path, timestamp and output filename for the extra clips and still frames added during the broad media expansion pass. It was used for Lathe Sparks, Motorised Standing Desk, Vintage String Lights, Spiral Staircase, Curving Skirting Board, Mega Book Case, Robot Arm and Drift Trike.

## Workshop and build projects

### CV in a Box

- Page: `projects\cv-in-a-box\index.html`
- Curated assets: `projects\cv-in-a-box\images`
- Known source material now in repo:
  - `projects\cv-in-a-box\images\BoxedSoftwareDesign.mp4`
  - `projects\cv-in-a-box\images\Software Box Front.pdf`
  - `projects\cv-in-a-box\images\Software Box V2 Front Page.svg`
  - `projects\cv-in-a-box\images\Software Box V2 Back Page.svg`
  - `projects\cv-in-a-box\images\DSC09233.JPG`, `DSC09234.JPG`, `DSC09240.JPG`, `DSC09244.JPG`
- Notes: source appears to have been supplied directly into the asset folder during the session.

### 3D Printers - filament storage

- Page: `projects\3d-printers\index.html`
- Curated assets: `projects\3d-printers\images\filament-storage`
- Source: camera originals `DSC09789.JPG`, `DSC09792.JPG`, `DSC09795.JPG`, `DSC09796.JPG`,
  6000px and roughly 10MB each. Imported at 2400px under descriptive names, following the
  same rule as the danfest gallery: full-size camera files are not committed. The camera
  originals have been deleted; the 2400px imports are the copies of record here.

### Belly Board

- Page: `projects\belly-board\index.html`
- Curated assets: `projects\belly-board\images`
- Known source material: user-added `belly-board` asset folder in the site repo.
- Notes: images were significantly reduced/curated; unused images were removed after selection. External raw folder was not specified in the chat.

### Lathe Sparks

- Page: `projects\lathe-sparks\index.html`
- Curated assets: `projects\lathe-sparks\images`
- Original media source: `\\192.168.1.13\Public\Video\Daniel\Lathe`
- Earlier local/user-added media folder: `projects\lathe-sparks\images`
- Video tools mentioned by user: `C:\ffmpeg`, `C:\ffmpeg-shared`
- Notes: initial lathe clips were converted for the web; user later noted the first converted clips had no sound and pointed back to the originals on the network share.

### Motorised Standing Desk

- Page: `projects\motorised-standing-desk\index.html`
- Curated assets: `projects\motorised-standing-desk\images`
- Original media source: `F:\video\desk-project`
- Cross-chat source: `Standing desk design specs` (`691860c7-e7d0-8325-99d4-d60b397c9619`)
  - Original design discussion covered a more ambitious DIY sit-stand mechanism before the bought-frame build: linear actuator on each leg versus a pulley/gear/screw arrangement, cable-routing holes, programmable heights, optional tilt, desk size, height range and load capacity.
  - Follow-up spec considered very heavy glass or concrete tops: approximately 35-40kg for 12mm toughened glass, around 110-120kg for a 40mm concrete slab, realistic moving mass around 160-180kg, and a design target around 250kg dynamic / 400kg static.
  - Mechanical notes included four lifting points, a rigid perimeter frame, bracing against racking, uniform support for concrete, spreader pads for glass, and slower/heavier actuation if the top became a serious slab.
- Cross-chat source: `Cool Desk Ideas` (`698de958-e150-8394-bfae-cf9a1189ac55`)
  - Surface-material exploration before/during the desk work: glass plus an interstitial layer plus orange linoleum, then a simpler Marmoleum-on-plywood direction.
  - Practical details discussed: furniture/cabinet-grade birch ply, BB/BB plywood being suitable under linoleum, 18-24mm thickness depending on span, R3-R5 edge round-over, R25 corners, raw sanded plywood under the adhesive, underside sealing, threaded inserts, linoleum adhesives, J-roller use and A2/B1-style trowel notch sizing.
  - Public page keeps this as a design-process detour only. The actual published build currently says 32mm plywood with laminate flooring as the working surface.
- Important correction: the media labelled "Motor wiring" was actually robot-arm work, not the desk project, and should not be used as desk evidence.
- Cross-chat/session correction: `derived\projects\motorised-standing-desk\images\extra-finished-detail.jpg` was also identified as robot-arm/VR work rather than desk work and was removed from the public desk page.
- Current task chat notes: standing-desk page was specifically critiqued against the sharpened 3D-printer page. The public page keeps the short hero line "Height-adjustable desk.", the father/son workshop angle, 32mm plywood, laminate-flooring work surface, 1800mm x 800mm top, curved corners, Desktronic dual-motor frame, routed laminate edge and visible lacquered ply edge.
- Notes: page was assembled from mixed photos/videos and curated into a smaller set.

### Active Speakers ESP32 Controller

- Page: `projects\active-speakers\index.html`
- Curated assets: `projects\active-speakers\images`
- Primary media sources:
  - `F:\video\speakers`
  - `C:\Users\bryar\OneDrive\Documents\Projects\Speakers`
  - `\\192.168.1.13\YouTubeVideo\Daniel\Speakers`
  - `D:\git\KingRO4Y`
- Current media expansion notes: additional short clips and stills were selected from
  `F:\video\speakers`, mainly routing, rear-baffle work, sanding, plate-amp fitting,
  driver fitting and finished measurement photos. The imported stills were resized
  before committing; clip transcodes preserve stereo AAC audio.
- Cross-chat source: `RCA to XLR Converters`
  - Sonifex RB-UL2 gain matching and unity-gain calibration notes.
  - DAC/preamp selection notes around Topping E70, DacMagic 200M, SMSL DL200 and Topping DX5 II.
  - Audio chain notes: DJM/miniDSP/Toslink/Topping/balanced XLR/Hypex.
- Cross-chat source: `Topping to Hypex Debug`
  - Hypex active-speaker debugging notes: XLR/RCA selection, mute/volume state, Topping analogue output testing and isolating the silent-speaker fault.
  - Specific debug chain from the old chat: `Vinyl -> PreAmp -> MiniDSP -> TosLink -> Topping -> XLR -> Hypex`, with the Topping showing good levels but the Hypex silent. Suggested isolation steps included selecting XLR explicitly on the Hypex, checking Hypex mute/volume state, disconnecting the USB controller while testing, playing a fixed 100Hz/1kHz tone and measuring AC voltage across XLR pins 2 and 3, then trying Topping RCA into Hypex RCA.
  - Thread ID: `6a81ff7e-f550-83ed-9743-10d7a5ff4a2a`.
  - ESP32/Hypex USB-controller context: reverse-engineered USB protocol with Wireshark and a physical volume/input controller.
- Cross-chat source: `Mini USB Cable Length`
  - Hypex FA503 controller note: the amplifier is a USB peripheral, so the controller can expose USB-C and use a USB-C to Mini-USB cable to the FA503; USB 2.0 only needs D+, D-, VBUS and ground plus the USB-C CC handling.
- Notes: public project page now covers the active speaker build, measurement work
  and in-progress controller work. It still needs a short FreeCAD screen recording.

### Corten Balustrade

- Page: `projects\corten-balustrade\index.html`
- Curated assets: `projects\corten-balustrade\images`
- Known source material: user-added Corten balustrade folder/assets in the site repo.
- User-requested originals/frames:
  - `_MG_8675.CR2` converted by user to JPEG
  - `_MG_8924.jpg`
  - `20191116_215127.jpg`
  - `20191102_142400.jpg`
  - `LastFew.jpg`
  - `Screenshot 2025-03-27 201258.png` for the FEA/design check
- Notes: selected images were organised and unused images removed after the CR2 was converted.
- Cross-chat source: `.NET Expertise Summary` (`68008fa0-0214-8001-80bf-ff6067dfdd40`)
  - Short CV/project evidence: bespoke Corten steel balustrade, including FEA and structural sign-off.
- Cross-chat source: `CV: Programming Skills Highlighted` (`80ac0fa4-b756-405e-97b0-a405555de456`)
  - Earlier CV wording describes Daniel designing and TIG welding the balustrade as part of the family-home build.

### Vintage String Lights

- Page: `projects\vintage-string-lights\index.html`
- Curated assets: `projects\vintage-string-lights\images`
- Original media source: `\\192.168.1.13\YouTubeVideo\Daniel\Vintage String Lights`
- Notes: user added two finished photos; additional frames and clips were sampled from video to show making and installation.

### Spiral Staircase

- Page: `projects\spiral-staircase\index.html`
- Curated assets: `projects\spiral-staircase\images`
- Original media source: `\\192.168.1.13\Public\Video\Daniel\SpiralStairCase`
- Notes: user had already supplied a few finished photos in the asset folder; additional frames and clips were sampled from the network-share videos.

### Mega Book Case

- Page: `projects\mega-book-case\index.html`
- Curated assets: `projects\mega-book-case\images`
- Original media source: `\\192.168.1.13\Public\Video\Daniel\Book Case`
- Cross-chat source: `CV Assistance: Structure, Content` (`dbf9778f-2880-485a-8ead-391e237bb605`)
  - Daniel described the bookcase as part of a broader interests/hobbies section alongside the family house, home automation, TIG-welded balustrade and curved wooden stairs.
  - The older CV wording called it a recent "massive set of bookcases" with a sliding ladder, around 3.6m tall. The public page keeps the later site-session measurement of 5m x 3.4m.
- Current task chat/site notes: the page already carries the main design/build detail extracted during the site session: 5m x 3.4m full-height case, MDF carcass, oak shelves, hollow 18mm/18mm/18mm uprights, Rigifix M8 wall anchors, Domino DF500 joinery, sprayed Dulux MDF primer and anthracite eggshell, low console, cable routing, existing window constraint, and the rolling ladder as its own sub-project.
- Ladder details: bought ladder reinforced with angle iron and painted to match; rail made from 25mm steel bar welded to angle-iron brackets; Delrin rollers turned on the Chipmaster; inline skate wheels; under GBP 100 for the homemade hardware.
- Notes: this was treated as a large project page with multiple construction stages, videos and photos. User planned to add more final hero photos later.

### Curving Skirting Board

- Page: `projects\curving-skirting-board\index.html`
- Curated assets: `projects\curving-skirting-board\images`
- Original media source: `\\192.168.1.13\Public\Video\Daniel\Curved Skirtingboard`
- Notes: source included steam-box construction, timber bending, and fitting skirting board to the curved wall.

### Drift Trike

- Page: `projects\drift-trike\index.html`
- Curated assets: `projects\drift-trike\images`
- Original media source: `\\192.168.1.13\Public\Video\Daniel\Drift Trike`
- User-directed clip references:
  - `Finished2\C1251.MP4`, from `00:30` to `01:00`: Lincoln driving it
  - `20230102_001732.MOV`, around `05:00`: Lincoln putting wheels on
  - `C1032.MP4`, from `00:53` to `01:14`: green welding
  - `C1033.MP4`, around `00:32`: finished weld frame
  - `C1046.MP4`: making wires
  - `C1058.MP4`, around `06:28`: initial motor-electronics test
  - `C1065.MP4`, from `01:20` to `01:58`: welding
  - `C1066.MP4`, from `14:05` to `14:25`
  - `C1701.MP4`, from `01:17` to `01:53`
  - `C1702.MP4`, from `00:42` to `01:52`
  - `C1078.MP4`, from `08:46` to `09:00`: Lincoln learning to tap
  - `C1097.MP4`, around `04:40`: slow-motion drilling
  - `C1103.MP4`, around `01:57`
  - `C1106.MP4`, around `01:02`: belt sanding
  - `C1126.MP4`, from `04:28` to `04:40`: plasma cutting
- Notes: the first green welding candidate did not show enough welding; user then supplied better clip/time references.
- Cross-chat source: `.NET Expertise Summary` (`68008fa0-0214-8001-80bf-ff6067dfdd40`)
  - Short CV/project evidence: drift trike built with Daniel's son, incorporating electronics, inrush protection and hands-on engineering education.

### 3D Printer Build

- Page: `projects\3d-printers\index.html`
- Curated assets: `project-assets\3d-printers`
- Original media source: `\\192.168.1.13\Public\Video\Daniel\3dPrinter`
- Original photo source: `\\192.168.1.13\Public\Video\Daniel\3dPrinter\Photos`
- Selected photos:
  - `DSC03389.JPG` -> `01-prusa-mk4-toolhead.jpg`
  - `DSC03391.JPG` -> `02-heated-bed-closeup.jpg`
  - `DSC03396.JPG` -> `03-frame-and-print-head.jpg`
  - `DSC03399.JPG` -> `04-toolhead-rods-detail.jpg`
  - `DSC03409.JPG` -> `05-extruder-hinges-detail.jpg`
  - `DSC03411.JPG` -> `06-leadscrew-orange-block.jpg`
  - `DSC03414.JPG` -> `07-control-screen.jpg`
- Additional detail photos:
  - `DSC03390.JPG` -> `08-toolhead-front-fan.jpg`
  - `DSC03392.JPG` -> `09-heatbed-print-surface.jpg`
  - `DSC03395.JPG` -> `10-rear-cable-exit.jpg`
  - `DSC03397.JPG` -> `11-belt-and-rod-perspective.jpg`
  - `DSC03400.JPG` -> `12-toolhead-depth-of-field.jpg`
  - `DSC03405.JPG` -> `13-nozzle-over-bed.jpg`
  - `DSC03410.JPG` -> `14-extruder-motor-detail.jpg`
  - `DSC03412.JPG` -> `15-leadscrew-thread-detail.jpg`
  - `DSC03415.JPG` -> `16-control-display-closeup.jpg`
- Selected clips:
  - `C0330.MP4`, around `00:00:50`, 30 seconds -> `clip-unboxing.mp4`
  - `C0331.MP4`, around `00:06:45`, 30 seconds -> `clip-rods-on-bench.mp4`
  - `C0331.MP4`, from `00:01:35`, 45 seconds -> `clip-decoration-fixing-720.mp4`
  - `C0331.MP4`, from `00:16:25`, 45 seconds -> `clip-decoration-welding-720.mp4`
  - `C0347.MP4`, around `00:06:50`, 30 seconds -> `clip-frame-assembly.mp4`
  - `C0359.MP4`, around `00:00:50`, 30 seconds -> `clip-wiring-electronics.mp4`
  - `C0381.MP4`, around `00:00:55`, 30 seconds -> `clip-finished-printer.mp4`
- Additional detail clips added after full video scan:
  - `C0335.MP4`, from `00:20:10`, 60 seconds -> `clip-main-frame-uprights-720.mp4`
  - `C0340.MP4`, from `00:15:45`, 30 seconds -> `clip-stepper-connector-detail-720.mp4`
  - `C0341.MP4`, from `00:00:14`, 120 seconds -> `clip-bearing-macro-720.mp4`
  - `C0342.MP4`, from `00:12:00`, 45 seconds -> `clip-orange-parts-assembly-720.mp4`
  - `C0344.MP4`, from `00:15:40`, 30 seconds -> `clip-x-axis-carriage-720.mp4`
  - `C0348.MP4`, from `00:19:35`, 30 seconds -> `clip-toolhead-install-720.mp4`
  - `C0353.MP4`, from `00:08:55`, 60 seconds -> `clip-hotend-small-parts-720.mp4`
  - `C0356.MP4`, from `00:17:08`, 30 seconds -> `clip-extruder-fan-detail-720.mp4`
  - `C0357.MP4`, from `00:01:55`, 30 seconds -> `clip-toolhead-mounted-720.mp4`
  - `C0361.MP4`, from `00:02:10`, 30 seconds -> `clip-heatbed-wiring-720.mp4`
  - `C0379.MP4`, from `00:21:10`, 30 seconds -> `clip-rear-loom-routing-720.mp4`
  - `C0380.MP4`, from `00:12:15`, 30 seconds -> `clip-final-cable-routing-720.mp4`
  - `C0380.MP4`, from `00:10:45`, 45 seconds -> `clip-late-underframe-detail-720.mp4`
  - `C0381.MP4`, from `00:44:40`, 60 seconds -> `clip-final-bench-rotation-720.mp4`
  - Poster frames generated from the same source clips into `projects\3d-printers\media`.
- Related firmware-debugging references:
  - `https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/4465#issuecomment-2660022554`
  - `https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/4487#issuecomment-2665450594`
  - `https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/4465#issuecomment-2700234456`
- GitHub attachment images copied locally from Daniel's ARCTOS gear comment:
  - `https://github.com/user-attachments/assets/63b1e905-b220-405f-a598-9b13e7cc0005` -> `project-assets\3d-printers\firmware-62-layer-shift-result.jpg`
  - `https://github.com/user-attachments/assets/7ecef519-a56e-4b9f-b573-c4b864e5a49c` -> `project-assets\3d-printers\firmware-613-success-result.jpg`
  - `https://github.com/user-attachments/assets/c96e7413-e60a-4282-b1a5-038f58956f53` -> `project-assets\3d-printers\firmware-arctos-gears-comparison.jpg`
  - Web versions generated in `projects\3d-printers\media` at 480px, 960px and 1600px widths.
- FreeCAD/source notes: Daniel reported multiple FreeCAD/3D-printing conversations. The logged-in ChatGPT chat-history search later found several relevant old chats:
  - `3D Printing with FreeCAD` (`6a6cad90-b728-83eb-aec4-fdcb216d7c14`): importing SVG as geometry, using Inkscape to clean SVG paths, FreeCAD Draft/Part workflows, extruding faces into printable plaques, and the Body-vs-Part "Selected object must belong to the active body" trap.
  - `Side Hole in Cylinder` (`69877019-7a00-8387-a52a-41d5c79d7e58`): radial side holes, datum-plane confusion, projecting cylinder axes, pocket direction, symmetric through-cuts, pads for bosses, and using `Up to face` plus offset for bosses protruding from curved surfaces.
  - `Barbed hose bung FreeCAD` (`689f220b-baec-8331-b556-1e1e94fd060e`): single-sketch-and-revolve workflow for a barbed hose bung, including barb angles, small oversize for sealing, PETG/TPU material choice and 100% infill.
  - `Thicken Edges in PrusaSlicer` (`696c17a6-38cc-832b-a7d5-16de472e1c0f`): reinforcing insert holes with modifier meshes, high perimeters and 100% infill, while noting that proper bosses and chamfers are better done in CAD first.
- Public FreeCAD section also uses site/session facts already present here: Daniel draws his own parts in FreeCAD; prints robot parts, brackets, workshop jigs, dust-extractor adapters, cabinet fittings and repairs; uses heat-set inserts; prefers open tools; and chose Prusa over Bambu partly because the Prusa ecosystem remains more inspectable.
- Notes: source footage is very large 4K XAVC-style MP4; web clips were transcoded to 1280px-wide H.264/AAC with fast-start metadata.

### Robot Arm

- Page: `projects\robot-arm\index.html`
- Curated assets: `projects\robot-arm\images`
- Original media source: `\\192.168.1.13\Public\Video\Daniel\RobotArm`
- Original source folders inspected:
  - `\\192.168.1.13\Public\Video\Daniel\RobotArm\Pictures`
  - `\\192.168.1.13\Public\Video\Daniel\RobotArm\Printing`
  - `\\192.168.1.13\Public\Video\Daniel\RobotArm\ServoMotors`
  - `\\192.168.1.13\Public\Video\Daniel\RobotArm\Smaller Cycloidal`
  - `\\192.168.1.13\Public\Video\Daniel\RobotArm\A AXIS`
  - `\\192.168.1.13\Public\Video\Daniel\RobotArm\NotSure`
- Selected photos:
  - `Pictures\DSC09186.JPG` -> `01-printer-making-arm-parts.jpg`
  - `Pictures\DSC09190.JPG` -> `02-printed-coupler-on-bed.jpg`
  - `Pictures\DSC09193.JPG` -> `03-printer-in-progress.jpg`
  - `Pictures\DSC09218.JPG` -> `04-workshop-context.jpg`
  - `Pictures\DSC09219.JPG` -> `05-workshop-wide.jpg`
  - `Pictures\DSC09221.JPG` -> `06-rods-and-fasteners.jpg`
  - `Pictures\DSC09222.JPG` -> `07-cycloidal-joint-closeup.jpg`
  - `Pictures\DSC09223.JPG` -> `08-joint-side-by-side.jpg`
- Selected clips:
  - `Printing\C1339.MP4`, around `00:00:28`, 12 seconds -> `clip-printing-arm-parts.mp4`
  - `ServoMotors\C1365.MP4`, around `00:01:55`, 14 seconds -> `clip-servo-electronics.mp4`
  - `Smaller Cycloidal\C1381.MP4`, around `00:01:55`, 14 seconds -> `clip-cycloidal-layout.mp4`
  - `Smaller Cycloidal\C1403.MP4`, around `00:00:55`, 14 seconds -> `clip-joint-hand-test.mp4`
  - `Smaller Cycloidal\C1424.MP4`, around `00:05:55`, 14 seconds -> `clip-arm-assembly.mp4`
  - `NotSure\C1503.MP4`, around `00:29:55`, 12 seconds -> `clip-metalwork-welding.mp4`
- Notes: this page is intentionally framed as work in progress. Avoid implying the robot arm is a finished product until more completion/demo media is added.
- Cross-chat source: `Makerbase CAN baud rate` (`67c05191-8510-8001-bf1d-66f92dc55c77`)
  - Hardware/control note for the robot-arm page: Daniel was investigating Makerbase closed-loop stepper drivers over CAN bus, including the practical problem that the default baud rate was not obvious and might need to be discovered by trying common CAN rates or using the vendor configuration tools.
  - Keep this as a modest electronics/control note. Richer robot-learning chats were found, but many overlap with MSc final-project/dissertation/CORL work and should not be published unless Daniel explicitly chooses to expose that material.

### MG EV Project / Smart Lead

- Page: `projects\mg-ev-project\index.html`
- Curated assets: `projects\mg-ev-project\images`
- Placeholder assets: `project-assets\ev-charger-smart-lead`
- Cross-chat source: `Crimp vs Solder Terminals` (`6a60927d-0a14-83eb-9322-df0e1c1cab7c`)
  - Smart-lead details: Duosida Type 2 contacts, CP/PP signal contacts, 2.5mm and 6mm power conductors, ratchet crimper versus hydraulic crimper versus soldering, and the Duosida/Evalbo guidance around non-insulated terminal tooling.
  - Practical process notes: good solder wetting, avoiding solder wicking too far up the conductor, proper strain relief, no excess solder on the contact, pull-testing, sectioning a crimp when using a new tool, and staged thermal/current testing at 10-16A before 32A.
- Cross-chat source: `Fake Battery Load Methods` (`6a6132bb-a3e4-83ed-abd1-9bb84c680067`)
  - The useful direction was a fake EV rather than a fake battery: Type 2 EVSE testing only needs CP/PP behaviour for AC charging, with selectable States A/B/C, a switched diode, PP cable-rating resistance, and optional ESP32 measurement of pilot voltage, PWM duty cycle and advertised current.
  - IEC 61851 detail captured for future writeup: EVSE uses a +/-12V 1kHz control-pilot signal; duty cycle advertises current limit; voltage level/resistor state indicates whether the vehicle is connected and ready.
- Cross-chat source: `OpenEVSE Wiring Issue` (`6a677096-b6d0-83eb-82f7-3d9ca8895ce6`)
  - Fault-finding notes: OpenEVSE detected the EV and closed the contactor before reporting GFCI. Likely checks included Live and Neutral both passing through the GFCI toroid once, Earth/CP/PP not passing through the toroid, CT connector placement, Type 2 soldering inspection, and continuity/isolation checks around PE, L, N, CP and PP.
- Current task/site notes: page remains noindex and sketch-like; public copy should treat the ESP32/custom PCB smart-lead as an in-progress idea, not a finished product.

## Academic and AI work

### MSc Artificial Intelligence overview

- Overview page: `projects\msc-ai\index.html`
- Module pages:
  - `projects\msc-ai\programming-for-data-science\index.html`
  - `projects\msc-ai\data-science\index.html`
  - `projects\msc-ai\algorithms\index.html`
  - `projects\msc-ai\machine-learning\index.html`
  - `projects\msc-ai\knowledge-representation\index.html`
  - `projects\msc-ai\ethics\index.html`
  - `projects\msc-ai\deep-learning\index.html`
  - `projects\msc-ai\data-mining-text-analytics\index.html`
  - `projects\msc-ai\robotics\index.html`
- Curated assets: `projects\msc-ai\images`
- Original academic source folder: `C:\Users\bryar\OneDrive\Documents\Leeds`
- Explicit exclusion: do not include Final Project, dissertation, CORL material, course handouts, assignment briefs, or Leeds teaching material.
- Notes: pages describe modules and show selected figures from Daniel's own assessments/notebooks/outputs only.

### Programming for Data Science

- Page: `projects\msc-ai\programming-for-data-science\index.html`
- Curated assets:
  - `projects\msc-ai\images\p4ds-architecture-pipeline.jpg`
  - `projects\msc-ai\images\p4ds-project-gutenberg-export.jpg`
  - `projects\msc-ai\images\p4ds-letter-frequencies.jpg`
- Source: `C:\Users\bryar\OneDrive\Documents\Leeds`, Programming for Data Science module/assessment files.
- Notes: Project Gutenberg/text-processing assessment outputs only; avoid publishing brief/course PDFs.

### Data Science

- Page: `projects\msc-ai\data-science\index.html`
- Curated assets: `projects\msc-ai\images\data-science-output-01.jpg` through `data-science-output-06.jpg`
- Source: `C:\Users\bryar\OneDrive\Documents\Leeds`, Data Science module/assessment files.
- Notes: fraud/classification/cost-analysis outputs selected from Daniel's own work.

### Algorithms

- Page: `projects\msc-ai\algorithms\index.html`
- Source: `C:\Users\bryar\OneDrive\Documents\Leeds`, Algorithms module material.
- Notes: descriptive page only; no teaching material or problem sheets should be published.

### Machine Learning

- Page: `projects\msc-ai\machine-learning\index.html`
- Curated assets:
  - `projects\msc-ai\images\ml-initial-gpr.jpg`
  - `projects\msc-ai\images\ml-mars-loops.jpg`
  - `projects\msc-ai\images\ml-final-orbit-plot.jpg`
  - `projects\msc-ai\images\ml-neural-network-diagram.jpg`
- Source: `C:\Users\bryar\OneDrive\Documents\Leeds`, Machine Learning module/assessment files.
- Notes: Mars/JPL/orbit regression assessment outputs from Daniel's own submitted work.

### Knowledge Representation and Reasoning

- Page: `projects\msc-ai\knowledge-representation\index.html`
- Curated assets:
  - `projects\msc-ai\images\krr-sandwich-counterexample.jpg`
  - `projects\msc-ai\images\krr-protege-ontology.jpg`
- Source: `C:\Users\bryar\OneDrive\Documents\Leeds`, KRR module/assessment files.
- Notes: sandwich ontology, OWL/Protege, description logic and reasoning outputs from Daniel's own work.

### Ethics of AI

- Page: `projects\msc-ai\ethics\index.html`
- Source: `C:\Users\bryar\OneDrive\Documents\Leeds`, Ethics of AI module/assessment files.
- Notes: descriptive page only; do not publish teaching material.

### Deep Learning

- Page: `projects\msc-ai\deep-learning\index.html`
- Curated assets:
  - `projects\msc-ai\images\dl-encoder-decoder.jpg`
  - `projects\msc-ai\images\dl-bleu-bad-model.jpg`
  - `projects\msc-ai\images\dl-cosine-similarity.jpg`
  - `projects\msc-ai\images\dl-resnet152-diagram.jpg`
- Source: `C:\Users\bryar\OneDrive\Documents\Leeds`, Deep Learning module/assessment files.
- Notes: image-captioning assessment outputs from Daniel's own work.

### Data Mining and Text Analytics

- Page: `projects\msc-ai\data-mining-text-analytics\index.html`
- Curated assets:
  - `projects\msc-ai\images\dmta-generating-podcast.jpg`
  - `projects\msc-ai\images\dmta-persona-scores.jpg`
  - `projects\msc-ai\images\dmta-chatgpt-text-improvement.jpg`
- Source: `C:\Users\bryar\OneDrive\Documents\Leeds`, Data Mining and Text Analytics module/assessment files.
- Specific source for the "Muppet test": `OCOM5204M Data Mining and Text Analytics\Assessment2\Research Proposal.docx` and exported/submitted PDF in the Leeds folder.
- Notes: include only small, humorous/generated excerpts and Daniel's own synopsis; do not republish the proposal wholesale.

### Robotics

- Page: `projects\msc-ai\robotics\index.html`
- Curated assets:
  - `projects\msc-ai\images\robotics-rviz.jpg`
  - `projects\msc-ai\images\robotics-reward-function.jpg`
  - `projects\msc-ai\images\robotics-sarsa-learning.jpg`
  - `projects\msc-ai\images\robotics-world.jpg`
- Source: `C:\Users\bryar\OneDrive\Documents\Leeds`, Robotics module/assessment files.
- Related local repos:
  - `E:\git\Introduction-to-Autonomous-Robots-Labs`
  - `E:\git\turtlebot-as2`
- Notes: ROS/Gazebo/TurtleBot outputs from Daniel's own work; keep final-project/dissertation/CORL material separate.

### MLX course projects

- Page: `projects\msc-ai\mlx-course-projects\index.html`
- Generated asset: `projects\msc-ai\images\mlx-course-architecture.jpg`
- GitHub profile: `https://github.com/DanielBryars`
- MLX course website: `https://ml.institute/`
- Source repos:
  - Local checkout: `E:\git\MLX3-VisionTransformers`
  - Public repo: `https://github.com/DanielBryars/MLX3-VisionTransformers`
  - Public repo: `https://github.com/DanielBryars/MLX4-Decoder-Visual-Captioning`
  - Public repo: `https://github.com/DanielBryars/MLX5-Audio-Processing`
  - Public repo: `https://github.com/DanielBryars/MLX6-fine-tuning`
  - Public repo: `https://github.com/DanielBryars/predicting_hackernews_upvotes`
  - Local checkout/public repo: `E:\git\two-towers-search`, `https://github.com/DanielBryars/two-towers-search`
  - Related public repo: `https://github.com/DanielBryars/word2vec`
- Notes: source used was README/code/repo metadata, not course PDFs. The architecture image was generated specifically for the site as an original summary graphic.

### Shadow Printing

- Page: `projects\shadow-printing\index.html`
- Curated assets: `projects\shadow-printing\images`
- Cross-chat source: `New Toy Idea` (`61a1dfda-4513-4bd2-b4ed-c26f0e30e2ce`)
  - Original idea: choose a picture, use software to calculate 3D-printable block geometry, then illuminate it with a torch or the sun so the cast shadow reveals the chosen silhouette.
  - Related clock variant: cast clock digits or hands as shadows, with possible naming directions including LightCast and TimeInShadows.
- Notes: page remains noindex/draft until actual generated models, prints or photos exist.

### Home Assistant

- Page: `projects\home-assistant\index.html`
- Curated assets: `projects\home-assistant\images`
- Known source material: relay-panel photographs that were previously sitting
  under `projects\home-assistant`.
- Notes: these are not decorative lighting photos. They show the relay-panel
  installation used to control the house lights through Home Assistant. Page is
  still noindex and needs a fuller write-up.

## Empty project folders prepared for later

These remaining project asset folders were created as placeholders so images/media can be dropped in later. They do not yet have a meaningful raw-source trail in this file:

- `project-assets\arduino-inverted-pendulum`
- `project-assets\bbc-micro-teletext`
- `project-assets\ben-eater-8-bit-computer`
- `projects\clock-project\images`
- `project-assets\diffvantage`
- `project-assets\house-build`
- `project-assets\otter-surfboard`
- `project-assets\physical-design-and-analysis`
- `project-assets\robot-learning-msc`
- `projects\speed-boat\images`
