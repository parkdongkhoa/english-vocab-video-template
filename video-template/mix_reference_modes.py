from __future__ import annotations

import argparse
import shutil
import subprocess
from pathlib import Path

from reference_modes_data import MODE_A_ITEMS, MODE_B_CARDS, ROOT
from reference_timing import audio_duration, audio_path, mode_a_timeline, mode_b_timeline


FFMPEG = shutil.which("ffmpeg") or "ffmpeg"


def delayed_voice(
    input_index: int,
    delay_seconds: float,
    duration: float,
    volume: float,
    label: str,
    tempo_factor: float | None = None,
) -> str:
    delay_ms = max(0, int(round(delay_seconds * 1000)))
    tempo = ""
    if tempo_factor is not None:
        # atempo < 1 slows the short spoken digit so it occupies exactly one
        # visual second; this removes the silent tail before the reveal.
        tempo = f"atempo={tempo_factor:.6f},"
    return (
        f"[{input_index}:a]{tempo}adelay={delay_ms}|{delay_ms},apad,"
        f"atrim=duration={duration:.3f},volume={volume:.2f}[{label}]"
    )


def finish_mix(filters: list[str], labels: list[str], duration: float, inputs: list[Path], video: Path, output: Path) -> Path:
    cmd = [FFMPEG, "-y", "-loglevel", "error"]
    for path in inputs:
        cmd.extend(["-i", str(path)])
    fade_start = max(0.0, duration - 0.35)
    filters.append(
        f"{''.join(labels)}amix=inputs={len(labels)}:duration=longest:dropout_transition=0:"
        f"normalize=0,volume=-3dB[mix];[mix]afade=t=out:st={fade_start:.3f}:d=0.35,"
        "alimiter=limit=0.90:level=false[a]"
    )
    cmd.extend(
        [
            "-filter_complex",
            ";".join(filters),
            "-map",
            "0:v:0",
            "-map",
            "[a]",
            "-c:v",
            "copy",
            "-c:a",
            "aac",
            "-b:a",
            "192k",
            "-t",
            f"{duration:.3f}",
            "-movflags",
            "+faststart",
            str(output),
        ]
    )
    subprocess.run(cmd, check=True)
    return output


def run_mode_a() -> Path:
    timeline = mode_a_timeline()
    duration = float(timeline["duration"])
    items = timeline["items"]
    assert isinstance(items, list)
    video = ROOT / "reference_mode_a_sample_layout_hybrid_silent.mp4"
    inputs: list[Path] = [video, ROOT / "module03_music.wav", ROOT / "mode_a_tick.wav"]
    filters = [
        f"[1:a]volume=0.24,afade=t=in:st=0:d=1.20,atrim=duration={duration:.3f}[music]",
    ]
    labels = ["[music]"]

    vi_indices: dict[int, int] = {}
    en_indices: dict[int, int] = {}
    for index in range(1, 11):
        vi_indices[index - 1] = len(inputs)
        inputs.append(audio_path(f"mode_a_q{index:02d}_vi"))
        en_indices[index - 1] = len(inputs)
        inputs.append(audio_path(f"mode_a_q{index:02d}_sentence"))
    intro_index = len(inputs)
    inputs.append(audio_path("mode_a_intro"))
    cta_index = len(inputs)
    inputs.append(audio_path("mode_a_cta"))
    filters.append(delayed_voice(intro_index, 0.0, duration, 0.82, "intro"))
    labels.append("[intro]")
    filters.append(delayed_voice(cta_index, float(timeline["cta_start"]), duration, 0.82, "cta"))
    labels.append("[cta]")
    tick_index = 2
    for row, info in enumerate(items):
        start = float(info["start"])
        countdown_start = float(info["countdown_start"])
        answer_start = float(info["answer_start"])
        vi_label = f"a_vi{row}"
        en_label = f"a_en{row}"
        filters.append(delayed_voice(vi_indices[row], start, duration, 0.88, vi_label))
        filters.append(delayed_voice(en_indices[row], answer_start, duration, 0.90, en_label))
        labels.extend([f"[{vi_label}]", f"[{en_label}]"])
        for offset_index, offset in enumerate((0.0, 1.0, 2.0)):
            tick_label = f"a_tick{row}_{offset_index}"
            filters.append(delayed_voice(tick_index, countdown_start + offset, duration, 0.34, tick_label))
            labels.append(f"[{tick_label}]")
        reveal_label = f"a_reveal{row}"
        filters.append(delayed_voice(tick_index, answer_start, duration, 0.42, reveal_label))
        labels.append(f"[{reveal_label}]")

    return finish_mix(
        filters,
        labels,
        duration,
        inputs,
        video,
        ROOT / "reference_mode_a_sample_layout_hybrid.mp4",
    )


def run_mode_b() -> Path:
    timeline = mode_b_timeline()
    duration = float(timeline["duration"])
    cards = timeline["cards"]
    assert isinstance(cards, list)
    video = ROOT / "reference_mode_b_source_template_silent.mp4"
    inputs: list[Path] = [video, ROOT / "module03_music.wav", ROOT / "mode_a_tick.wav"]
    filters = [
        # Keep the generated starter bed audible but well below the narration.
        f"[1:a]volume=1.45,afade=t=in:st=0:d=1.20,atrim=duration={duration:.3f}[music]",
    ]
    labels = ["[music]"]

    target_indices: dict[int, int] = {}
    for index, card in enumerate(MODE_B_CARDS):
        target_indices[index] = len(inputs)
        inputs.append(audio_path(f"mode_b_{card['target']}_en"))
    intro_index = len(inputs)
    inputs.append(audio_path("mode_b_intro"))
    cta_index = len(inputs)
    inputs.append(audio_path("mode_b_cta"))

    filters.append(delayed_voice(intro_index, 0.0, duration, 0.82, "intro"))
    labels.append("[intro]")
    cta_label = "b_cta"
    filters.append(delayed_voice(cta_index, float(timeline["cta_start"]), duration, 0.86, cta_label))
    labels.append(f"[{cta_label}]")
    for index, info in enumerate(cards):
        target_start = float(info["target_start"])
        target_label = f"b_target{index}"
        filters.append(delayed_voice(target_indices[index], target_start, duration, 0.90, target_label))
        labels.append(f"[{target_label}]")
        reveal_label = f"b_reveal{index}"
        filters.append(delayed_voice(2, float(info["reveal_start"]), duration, 0.24, reveal_label))
        labels.append(f"[{reveal_label}]")

    return finish_mix(
        filters,
        labels,
        duration,
        inputs,
        video,
        ROOT / "reference_mode_b_source_template_hybrid.mp4",
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["a", "b", "both"], default="b")
    args = parser.parse_args()
    if args.mode in {"a", "both"}:
        print(run_mode_a())
    if args.mode in {"b", "both"}:
        print(run_mode_b())


if __name__ == "__main__":
    main()
