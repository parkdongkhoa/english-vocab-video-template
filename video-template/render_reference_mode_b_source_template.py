from __future__ import annotations

import argparse
import shutil
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageFilter

from reference_modes_data import MODE_B_CARDS, ROOT
from reference_timing import mode_b_timeline


W, H = 1080, 1920
FPS = 30
TIMELINE = mode_b_timeline()
DURATION = float(TIMELINE["duration"])
REGULAR = r"C:\Windows\Fonts\segoeui.ttf"
BOLD = r"C:\Windows\Fonts\segoeuib.ttf"
CUTOUT_DIR = ROOT / "source_research" / "reference_b_cutouts"
CLOCK_CHECK_ICON = ROOT / "clock_check_3d.png"


def face(path: str, size: int):
    return ImageFont.truetype(path, size)


def centered(draw, xy, text, font_obj, fill, **kwargs):
    draw.text(xy, text, font=font_obj, fill=fill, anchor="mm", **kwargs)


def fit(draw, text, max_width, size, path=BOLD):
    while size >= 18:
        font_obj = face(path, size)
        if draw.textbbox((0, 0), text, font=font_obj)[2] <= max_width:
            return font_obj
        size -= 2
    return face(path, 18)


def paper_background() -> Image.Image:
    base = Image.new("RGB", (W, H), (247, 247, 243))
    noise = Image.effect_noise((W, H), 8).convert("L")
    noise = noise.filter(ImageFilter.GaussianBlur(0.35))
    texture = Image.new("RGB", (W, H), (232, 232, 226))
    base = Image.blend(base, texture, 0.075)
    # Very soft warm center keeps the source's paper feel without competing
    # with the pair visuals.
    overlay = Image.new("RGBA", (W, H), (255, 253, 246, 0))
    od = ImageDraw.Draw(overlay, "RGBA")
    od.ellipse((80, 260, 1000, 1660), fill=(255, 255, 250, 34))
    return Image.alpha_composite(base.convert("RGBA"), overlay).convert("RGB")


BG = paper_background()


def real_cutout(canvas: Image.Image, name: str, center: tuple[int, int], max_size: tuple[int, int]) -> None:
    """Paste a user-supplied licensed visual, or a clear placeholder if absent."""
    asset_path = CUTOUT_DIR / name
    if not asset_path.exists():
        width, height = max_size
        x1 = int(center[0] - width / 2)
        y1 = int(center[1] - height / 2)
        d = ImageDraw.Draw(canvas, "RGBA")
        d.rounded_rectangle(
            (x1 + 20, y1 + 22, x1 + width - 20, y1 + height - 22),
            radius=28,
            fill=(239, 241, 237, 185),
            outline=(119, 139, 128, 210),
            width=3,
        )
        d.rounded_rectangle(
            (center[0] - 38, center[1] - 52, center[0] + 38, center[1] + 18),
            radius=12,
            outline=(93, 121, 108, 255),
            width=5,
        )
        d.ellipse((center[0] + 12, center[1] - 40, center[0] + 25, center[1] - 27), fill=(93, 121, 108, 255))
        d.line(
            (center[0] - 26, center[1] + 6, center[0] - 5, center[1] - 16, center[0] + 7, center[1] - 2, center[0] + 27, center[1] - 22),
            fill=(93, 121, 108, 255),
            width=5,
            joint="curve",
        )
        centered(d, (center[0], center[1] + 58), "THÊM HÌNH CÓ QUYỀN DÙNG", face(BOLD, 15), (65, 82, 73, 255))
        return
    source = Image.open(asset_path).convert("RGBA")
    source.thumbnail(max_size, Image.Resampling.LANCZOS)
    x = int(center[0] - source.width / 2)
    y = int(center[1] - source.height / 2)
    # A restrained shadow separates the real object from the paper texture.
    shadow = Image.new("RGBA", source.size, (0, 0, 0, 0))
    shadow.putalpha(source.getchannel("A").filter(ImageFilter.GaussianBlur(10)))
    shadow_layer = Image.new("RGBA", source.size, (30, 30, 30, 0))
    shadow_layer.putalpha(shadow.getchannel("A").point(lambda value: int(value * 0.20)))
    canvas.alpha_composite(shadow_layer, (x + 5, y + 8))
    canvas.alpha_composite(source, (x, y))


def timer_icon(canvas: Image.Image, center: tuple[int, int]) -> None:
    if not CLOCK_CHECK_ICON.exists():
        return
    source = Image.open(CLOCK_CHECK_ICON).convert("RGBA")
    source.thumbnail((155, 155), Image.Resampling.LANCZOS)
    x = int(center[0] - source.width / 2)
    y = int(center[1] - source.height / 2)
    canvas.alpha_composite(source, (x, y))


def explanation_box(canvas: Image.Image, text: str) -> None:
    d = ImageDraw.Draw(canvas, "RGBA")
    box = (110, 1510, 970, 1725)
    d.rounded_rectangle(box, radius=24, fill=(231, 247, 238, 245), outline=(39, 155, 95, 210), width=3)
    centered(d, (540, 1555), "GIẢI THÍCH", face(BOLD, 24), (35, 125, 77, 255))
    body = fit(d, text, 740, 30, REGULAR)
    centered(d, (540, 1630), text, body, (38, 46, 43, 255), spacing=8)


def line_segment(progress: float, target: str) -> tuple[float, float]:
    """Shrink the timer symmetrically so both ends meet at screen center."""
    full_left, full_right = 225.0, 855.0
    p = max(0.0, min(1.0, progress))
    return (
        full_left + (540.0 - full_left) * p,
        full_right - (full_right - 540.0) * p,
    )


def cta_frame() -> Image.Image:
    img = BG.copy().convert("RGBA")
    d = ImageDraw.Draw(img, "RGBA")
    red = (197, 29, 48, 255)
    green = (35, 139, 83, 255)
    black = (28, 30, 38, 255)
    centered(d, (540, 150), "EVERYDAY ENGLISH", face(BOLD, 26), red)
    centered(d, (544, 520), "NICE WORK!", face(BOLD, 76), black, stroke_width=8, stroke_fill=(255, 255, 255, 255))
    centered(d, (540, 510), "NICE WORK!", face(BOLD, 76), red, stroke_width=5, stroke_fill=(255, 255, 255, 255))
    centered(d, (540, 690), f"{len(MODE_B_CARDS)} CẶP TỪ ĐÃ ĐƯỢC ÔN LẠI", face(BOLD, 32), black)
    panel = (120, 850, 960, 1195)
    d.rounded_rectangle(panel, radius=32, fill=(231, 247, 238, 245), outline=(39, 155, 95, 220), width=4)
    centered(d, (540, 930), "LƯU VIDEO", face(BOLD, 34), green)
    centered(d, (540, 1025), "LUYỆN LẠI", face(BOLD, 34), green)
    centered(d, (540, 1120), "THEO DÕI KÊNH", face(BOLD, 34), green)
    centered(d, (540, 1355), "Học một chút mỗi ngày — nói tự tin hơn.", face(REGULAR, 30), black)
    d.line((275, 1430, 805, 1430), fill=green, width=8)
    centered(d, (540, 1510), "HẸN GẶP LẠI Ở VIDEO TIẾP THEO", face(BOLD, 28), red)
    return img


def frame_at(t: float) -> Image.Image:
    if t >= float(TIMELINE["cta_start"]):
        return cta_frame()
    img = BG.copy().convert("RGBA")
    d = ImageDraw.Draw(img, "RGBA")
    red = (197, 29, 48, 255)
    black = (28, 30, 38, 255)
    muted = (106, 111, 120, 255)

    centered(d, (540, 150), "EVERYDAY ENGLISH", face(BOLD, 26), red)
    title = "BẠN NGHE ĐƯỢC TỪ NÀO?"
    centered(d, (544, 452), title, fit(d, title, 940, 62), (26, 26, 30, 255), stroke_width=8, stroke_fill=(26, 26, 30, 255))
    centered(d, (540, 444), title, fit(d, title, 940, 62), red, stroke_width=6, stroke_fill=(255, 255, 255, 255))

    cards = TIMELINE["cards"]
    assert isinstance(cards, list)
    card_info = next(info for info in cards if t < float(info["end"]))
    index = int(card_info["index"])
    start = float(card_info["start"])
    reveal_start = float(card_info["reveal_start"])
    card = MODE_B_CARDS[index]
    target_side = "left" if card["target"] == card["left"] else "right"
    progress = (t - start) / max(0.01, reveal_start - start)
    highlight = t >= reveal_start

    real_cutout(img, card["left_asset"], (360, 815), (290, 270))
    real_cutout(img, card["right_asset"], (720, 815), (290, 270))
    left_fill = red if highlight and target_side == "left" else black
    right_fill = red if highlight and target_side == "right" else black
    centered(d, (360, 1075), card["left"], fit(d, card["left"], 300, 45), left_fill)
    centered(d, (720, 1075), card["right"], fit(d, card["right"], 300, 45), right_fill)

    x1, x2 = line_segment(progress, target_side)
    timer_green = (35, 174, 105, 255)
    d.line((x1, 1180, x2, 1180), fill=timer_green, width=8)
    timer_icon(img, (540, 1365))
    if highlight:
        explanation_box(img, card["explanation"])
    return img


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default=str(ROOT / "reference_mode_b_source_template_silent.mp4"))
    args = parser.parse_args()
    frame_dir = ROOT / "reference_mode_b_source_template_frames"
    frame_dir.mkdir(exist_ok=True)
    cards = TIMELINE["cards"]
    assert isinstance(cards, list)
    states: list[tuple[float, float]] = []
    for info in cards:
        start = float(info["start"])
        reveal_start = float(info["reveal_start"])
        end = float(info["end"])
        for offset, hold in ((0.01, 1.0), (1.0, 1.0), (2.0, 1.0), (3.0, 1.2)):
            states.append((hold, start + offset))
        # Hold the listening state through the final 0.8s before the reveal;
        # the complete card must add up to MODE_B_CARD_DURATION exactly.
        states.append((reveal_start - (start + 4.2), start + 4.2))
        states.append((end - reveal_start, reveal_start))
    cta_start = float(TIMELINE["cta_start"])
    cta_duration = float(TIMELINE["cta_duration"])
    states.append((cta_duration, cta_start))
    frame_paths: list[Path] = []
    concat_lines: list[str] = []
    for index, (duration, start) in enumerate(states):
        path = frame_dir / f"frame_{index:02d}.png"
        frame_at(min(start, DURATION - 0.01)).save(path, format="PNG", optimize=True)
        frame_paths.append(path)
        concat_lines.extend([f"file '{path.as_posix()}'", f"duration {duration:.3f}"])
    concat_lines.append(f"file '{frame_paths[-1].as_posix()}'")
    concat = frame_dir / "concat.txt"
    concat.write_text("\n".join(concat_lines) + "\n", encoding="utf-8")
    ffmpeg = shutil.which("ffmpeg") or "ffmpeg"
    subprocess.run([
        ffmpeg, "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(concat),
        "-vf", f"fps={FPS},fade=t=out:st={max(0.0, DURATION - 0.35):.3f}:d=0.35", "-t", f"{DURATION:.3f}",
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-profile:v", "high", "-crf", "18", "-movflags", "+faststart", args.out,
    ], check=True)
    print(args.out)


if __name__ == "__main__":
    main()
