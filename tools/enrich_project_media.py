from __future__ import annotations

import subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
FFMPEG = Path("C:/ffmpeg-shared/bin/ffmpeg.exe")


def run(cmd: list[str]) -> None:
    result = subprocess.run(cmd, text=True, capture_output=True)
    if result.returncode != 0:
        raise RuntimeError(result.stderr[-1200:])


def image_from_video(src: str, out: Path, at: str) -> None:
    if out.exists():
        return
    out.parent.mkdir(parents=True, exist_ok=True)
    run(
        [
            str(FFMPEG),
            "-y",
            "-loglevel",
            "error",
            "-ss",
            at,
            "-i",
            src,
            "-frames:v",
            "1",
            "-vf",
            "scale='min(1600,iw)':-2",
            "-q:v",
            "3",
            str(out),
        ]
    )


def clip_from_video(src: str, out: Path, poster: Path, at: str, duration: str = "10") -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    if not out.exists():
        run(
            [
                str(FFMPEG),
                "-y",
                "-loglevel",
                "error",
                "-ss",
                at,
                "-i",
                src,
                "-t",
                duration,
                "-vf",
                "scale=-2:'min(720,ih)'",
                "-c:v",
                "libx264",
                "-crf",
                "27",
                "-preset",
                "fast",
                "-pix_fmt",
                "yuv420p",
                "-c:a",
                "aac",
                "-b:a",
                "96k",
                "-movflags",
                "+faststart",
                str(out),
            ]
        )
    image_from_video(src, poster, at)


def main() -> None:
    recipes = [
        {
            "slug": "lathe-sparks",
            "media": [
                ("image", r"\\192.168.1.13\Public\Video\Daniel\Lathe\clip1.MP4", "00:00:04", "extra-wide-shower.jpg"),
                ("image", r"\\192.168.1.13\Public\Video\Daniel\Lathe\clip3.MP4", "00:00:10", "extra-tool-close.jpg"),
                ("image", r"\\192.168.1.13\Public\Video\Daniel\Lathe\clip4.MP4", "00:00:12", "extra-orange-tail.jpg"),
                ("image", r"\\192.168.1.13\Public\Video\Daniel\Lathe\clip1.MP4", "00:00:18", "extra-falling-sparks.jpg"),
                ("video", r"\\192.168.1.13\Public\Video\Daniel\Lathe\clip1.MP4", "00:00:08", "extra-heavy-shower.mp4", "extra-heavy-shower-poster.jpg", "8"),
                ("video", r"\\192.168.1.13\Public\Video\Daniel\Lathe\clip3.MP4", "00:00:12", "extra-glowing-cut.mp4", "extra-glowing-cut-poster.jpg", "8"),
                ("video", r"\\192.168.1.13\Public\Video\Daniel\Lathe\clip4.MP4", "00:00:05", "extra-side-sparks.mp4", "extra-side-sparks-poster.jpg", "8"),
            ],
        },
        {
            "slug": "desk-project",
            "media": [
                ("image", r"F:\video\desk-project\C1661.MP4", "00:08:00", "extra-frame-assembly.jpg"),
                ("image", r"F:\video\desk-project\C1663.MP4", "00:12:40", "extra-top-on-bench.jpg"),
                ("image", r"F:\video\desk-project\C1664.MP4", "00:18:20", "extra-checking-fit.jpg"),
                ("image", r"F:\video\desk-project\C1665.MP4", "00:00:42", "extra-desk-test.jpg"),
                ("image", r"F:\video\desk-project\C1666.MP4", "00:00:18", "extra-finished-detail.jpg"),
                ("video", r"F:\video\desk-project\C1661.MP4", "00:06:30", "extra-layout-and-frame.mp4", "extra-layout-and-frame-poster.jpg", "12"),
                ("video", r"F:\video\desk-project\C1663.MP4", "00:10:30", "extra-working-the-top.mp4", "extra-working-the-top-poster.jpg", "12"),
                ("video", r"F:\video\desk-project\C1665.MP4", "00:00:30", "extra-height-test.mp4", "extra-height-test-poster.jpg", "10"),
            ],
        },
        {
            "slug": "vintage-string-lights",
            "media": [
                ("image", r"\\192.168.1.13\YouTubeVideo\Daniel\Vintage String Lights\C0249.MP4", "00:04:20", "extra-cutting-stock.jpg"),
                ("image", r"\\192.168.1.13\YouTubeVideo\Daniel\Vintage String Lights\C0251.MP4", "00:09:30", "extra-drilling-blocks.jpg"),
                ("image", r"\\192.168.1.13\YouTubeVideo\Daniel\Vintage String Lights\C0254.MP4", "00:07:10", "extra-wiring-bench.jpg"),
                ("image", r"\\192.168.1.13\YouTubeVideo\Daniel\Vintage String Lights\C0256.MP4", "00:17:00", "extra-lamp-test.jpg"),
                ("image", r"\\192.168.1.13\YouTubeVideo\Daniel\Vintage String Lights\C0257.MP4", "00:20:00", "extra-room-install.jpg"),
                ("image", r"\\192.168.1.13\YouTubeVideo\Daniel\Vintage String Lights\C0259.MP4", "00:12:00", "extra-finished-run.jpg"),
                ("video", r"\\192.168.1.13\YouTubeVideo\Daniel\Vintage String Lights\C0251.MP4", "00:08:30", "extra-repetition-at-bench.mp4", "extra-repetition-at-bench-poster.jpg", "12"),
                ("video", r"\\192.168.1.13\YouTubeVideo\Daniel\Vintage String Lights\C0254.MP4", "00:07:00", "extra-cable-and-holders.mp4", "extra-cable-and-holders-poster.jpg", "12"),
                ("video", r"\\192.168.1.13\YouTubeVideo\Daniel\Vintage String Lights\C0259.MP4", "00:12:00", "extra-final-install.mp4", "extra-final-install-poster.jpg", "12"),
            ],
        },
        {
            "slug": "spiral-staircase",
            "media": [
                ("image", r"\\192.168.1.13\Public\Video\Daniel\SpiralStairCase\Video\C0099.MP4", "00:12:00", "extra-raw-steel.jpg"),
                ("image", r"\\192.168.1.13\Public\Video\Daniel\SpiralStairCase\Video\C0102.MP4", "00:07:20", "extra-jig-work.jpg"),
                ("image", r"\\192.168.1.13\Public\Video\Daniel\SpiralStairCase\Video\C0104.MP4", "00:14:20", "extra-welded-tread.jpg"),
                ("image", r"\\192.168.1.13\Public\Video\Daniel\SpiralStairCase\Video\C0105.MP4", "00:17:00", "extra-fitting-up.jpg"),
                ("image", r"\\192.168.1.13\Public\Video\Daniel\SpiralStairCase\Video\C0112.MP4", "00:45:00", "extra-install-progress.jpg"),
                ("image", r"\\192.168.1.13\Public\Video\Daniel\SpiralStairCase\Video\C0114.MP4", "00:08:00", "extra-stair-detail.jpg"),
                ("video", r"\\192.168.1.13\Public\Video\Daniel\SpiralStairCase\Video\C0102.MP4", "00:07:15", "extra-setting-up.mp4", "extra-setting-up-poster.jpg", "12"),
                ("video", r"\\192.168.1.13\Public\Video\Daniel\SpiralStairCase\Video\C0104.MP4", "00:14:15", "extra-fabrication.mp4", "extra-fabrication-poster.jpg", "12"),
                ("video", r"\\192.168.1.13\Public\Video\Daniel\SpiralStairCase\Video\C0112.MP4", "00:45:00", "extra-installation.mp4", "extra-installation-poster.jpg", "12"),
            ],
        },
        {
            "slug": "curving-skirting-board",
            "media": [
                ("image", r"\\192.168.1.13\Public\Video\Daniel\Curved Skirtingboard\Video\C0927.MP4", "00:06:00", "extra-steam-box-build.jpg"),
                ("image", r"\\192.168.1.13\Public\Video\Daniel\Curved Skirtingboard\Video\C0929.MP4", "00:12:00", "extra-steaming-timber.jpg"),
                ("image", r"\\192.168.1.13\Public\Video\Daniel\Curved Skirtingboard\Video\C0931.MP4", "00:07:30", "extra-bending-form.jpg"),
                ("image", r"\\192.168.1.13\Public\Video\Daniel\Curved Skirtingboard\Video\C0940.MP4", "00:09:00", "extra-clamping-curve.jpg"),
                ("image", r"\\192.168.1.13\Public\Video\Daniel\Curved Skirtingboard\Video\C0946.MP4", "00:08:00", "extra-fitted-wall.jpg"),
                ("video", r"\\192.168.1.13\Public\Video\Daniel\Curved Skirtingboard\Video\C0927.MP4", "00:06:00", "extra-steam-box.mp4", "extra-steam-box-poster.jpg", "12"),
                ("video", r"\\192.168.1.13\Public\Video\Daniel\Curved Skirtingboard\Video\C0931.MP4", "00:07:30", "extra-bending-session.mp4", "extra-bending-session-poster.jpg", "12"),
                ("video", r"\\192.168.1.13\Public\Video\Daniel\Curved Skirtingboard\Video\C0946.MP4", "00:08:00", "extra-fitting-to-wall.mp4", "extra-fitting-to-wall-poster.jpg", "12"),
            ],
        },
        {
            "slug": "mega-book-case",
            "media": [
                ("image", r"\\192.168.1.13\Public\Video\Daniel\Book Case\C0278.MP4", "00:08:00", "extra-early-timber-layout.jpg"),
                ("image", r"\\192.168.1.13\Public\Video\Daniel\Book Case\C0295.MP4", "00:12:00", "extra-cabinet-assembly.jpg"),
                ("image", r"\\192.168.1.13\Public\Video\Daniel\Book Case\C0310.MP4", "00:15:00", "extra-long-shelf-work.jpg"),
                ("image", r"\\192.168.1.13\Public\Video\Daniel\Book Case\Fitting\C0440.MP4", "00:10:00", "extra-fitting-in-room.jpg"),
                ("image", r"\\192.168.1.13\Public\Video\Daniel\Book Case\Console\C0592.MP4", "00:08:00", "extra-console-detail.jpg"),
                ("image", r"\\192.168.1.13\Public\Video\Daniel\Book Case\Ladder\C0705.MP4", "00:09:00", "extra-ladder-build.jpg"),
                ("image", r"\\192.168.1.13\Public\Video\Daniel\Book Case\Ladder Welding\C0911.MP4", "00:07:00", "extra-ladder-welding.jpg"),
                ("image", r"\\192.168.1.13\Public\Video\Daniel\Book Case\Ladder\Ladder Rollers\C0851.MP4", "00:06:00", "extra-roller-detail.jpg"),
                ("video", r"\\192.168.1.13\Public\Video\Daniel\Book Case\C0295.MP4", "00:12:00", "extra-cabinet-assembly.mp4", "extra-cabinet-assembly-poster.jpg", "12"),
                ("video", r"\\192.168.1.13\Public\Video\Daniel\Book Case\Fitting\C0440.MP4", "00:10:00", "extra-room-fitting.mp4", "extra-room-fitting-poster.jpg", "12"),
                ("video", r"\\192.168.1.13\Public\Video\Daniel\Book Case\Console\C0592.MP4", "00:08:00", "extra-console-work.mp4", "extra-console-work-poster.jpg", "12"),
                ("video", r"\\192.168.1.13\Public\Video\Daniel\Book Case\Ladder\C0705.MP4", "00:09:00", "extra-ladder-work.mp4", "extra-ladder-work-poster.jpg", "12"),
            ],
        },
        {
            "slug": "robot-arm",
            "media": [
                ("image", r"\\192.168.1.13\Public\Video\Daniel\RobotArm\Printing\C1323.MP4", "00:02:00", "extra-printed-part.jpg"),
                ("image", r"\\192.168.1.13\Public\Video\Daniel\RobotArm\ServoMotors\C1352.MP4", "00:04:00", "extra-servo-bench.jpg"),
                ("image", r"\\192.168.1.13\Public\Video\Daniel\RobotArm\Smaller Cycloidal\C1381.MP4", "00:06:00", "extra-cycloidal-parts.jpg"),
                ("image", r"\\192.168.1.13\Public\Video\Daniel\RobotArm\A AXIS\C1428.MP4", "00:09:00", "extra-a-axis-build.jpg"),
                ("image", r"\\192.168.1.13\Public\Video\Daniel\RobotArm\NotSure\C1503.MP4", "00:08:00", "extra-arm-on-bench.jpg"),
                ("image", r"\\192.168.1.13\Public\Video\Daniel\RobotArm\ServoMotors\C1370.MP4", "00:05:00", "extra-wiring-servo.jpg"),
                ("video", r"\\192.168.1.13\Public\Video\Daniel\RobotArm\ServoMotors\C1352.MP4", "00:04:00", "extra-servo-testing.mp4", "extra-servo-testing-poster.jpg", "12"),
                ("video", r"\\192.168.1.13\Public\Video\Daniel\RobotArm\Smaller Cycloidal\C1381.MP4", "00:06:00", "extra-cycloidal-work.mp4", "extra-cycloidal-work-poster.jpg", "12"),
                ("video", r"\\192.168.1.13\Public\Video\Daniel\RobotArm\A AXIS\C1428.MP4", "00:09:00", "extra-a-axis.mp4", "extra-a-axis-poster.jpg", "12"),
                ("video", r"\\192.168.1.13\Public\Video\Daniel\RobotArm\NotSure\C1503.MP4", "00:08:00", "extra-arm-motion.mp4", "extra-arm-motion-poster.jpg", "12"),
            ],
        },
        {
            "slug": "drift-trike",
            "media": [
                ("image", r"\\192.168.1.13\Public\Video\Daniel\Drift Trike\Unboxing\C0958.MP4", "00:04:00", "extra-unboxing-parts.jpg"),
                ("image", r"\\192.168.1.13\Public\Video\Daniel\Drift Trike\C0981.MP4", "00:09:00", "extra-frame-layout.jpg"),
                ("image", r"\\192.168.1.13\Public\Video\Daniel\Drift Trike\C0993.MP4", "00:11:00", "extra-workshop-build.jpg"),
                ("image", r"\\192.168.1.13\Public\Video\Daniel\Drift Trike\MiniCam\20230101_212903.MOV", "00:01:20", "extra-mini-cam.jpg"),
                ("image", r"\\192.168.1.13\Public\Video\Daniel\Drift Trike\TestRun2\20230102_124911.MOV", "00:01:00", "extra-test-run.jpg"),
                ("image", r"\\192.168.1.13\Public\Video\Daniel\Drift Trike\Finished2\C1249.MP4", "00:03:30", "extra-finished-run.jpg"),
                ("video", r"\\192.168.1.13\Public\Video\Daniel\Drift Trike\Unboxing\C0958.MP4", "00:04:00", "extra-unboxing.mp4", "extra-unboxing-poster.jpg", "12"),
                ("video", r"\\192.168.1.13\Public\Video\Daniel\Drift Trike\C0981.MP4", "00:09:00", "extra-frame-layout.mp4", "extra-frame-layout-poster.jpg", "12"),
                ("video", r"\\192.168.1.13\Public\Video\Daniel\Drift Trike\MiniCam\20230101_212903.MOV", "00:01:20", "extra-mini-cam.mp4", "extra-mini-cam-poster.jpg", "12"),
                ("video", r"\\192.168.1.13\Public\Video\Daniel\Drift Trike\TestRun2\20230102_124911.MOV", "00:01:00", "extra-test-run.mp4", "extra-test-run-poster.jpg", "12"),
            ],
        },
    ]

    for recipe in recipes:
        base = REPO / "derived" / "project-assets" / recipe["slug"]
        for item in recipe["media"]:
            if item[0] == "image":
                _, src, at, name = item
                image_from_video(src, base / name, at)
                print(base / name)
            else:
                _, src, at, name, poster, duration = item
                clip_from_video(src, base / name, base / poster, at, duration)
                print(base / name)


if __name__ == "__main__":
    main()
