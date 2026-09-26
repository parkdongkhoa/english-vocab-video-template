"""Create original, lightweight starter music and reveal-cue WAV files."""

from __future__ import annotations

import math
import struct
import wave
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SAMPLE_RATE = 22_050
MAX_SAMPLE = 32_767
CHORDS = (
    (261.63, 329.63, 392.00, 493.88),
    (220.00, 261.63, 329.63, 392.00),
    (174.61, 220.00, 261.63, 349.23),
    (196.00, 246.94, 293.66, 392.00),
)


def clamp_sample(value: float) -> int:
    return max(-MAX_SAMPLE, min(MAX_SAMPLE, int(value * MAX_SAMPLE)))


def write_mono(path: Path, samples) -> None:
    with wave.open(str(path), "wb") as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(SAMPLE_RATE)
        block = bytearray()
        for sample in samples:
            block.extend(struct.pack("<h", clamp_sample(sample)))
        wav.writeframes(block)


def chord_sample(time_s: float, chord: tuple[float, ...]) -> float:
    return sum(
        math.sin(2.0 * math.pi * frequency * time_s + index * 0.37)
        for index, frequency in enumerate(chord)
    ) / len(chord)


def music_samples(duration_s: float = 70.0):
    total = int(SAMPLE_RATE * duration_s)
    fade_s = 1.5
    for index in range(total):
        time_s = index / SAMPLE_RATE
        section = int(time_s // 8.0) % len(CHORDS)
        within = time_s % 8.0
        current = chord_sample(time_s, CHORDS[section])
        next_chord = chord_sample(time_s, CHORDS[(section + 1) % len(CHORDS)])
        blend = max(0.0, min(1.0, (within - 7.25) / 0.75))
        pad = current * (1.0 - blend) + next_chord * blend
        breath = 0.82 + 0.12 * math.sin(2.0 * math.pi * time_s / 11.0)
        edge = min(1.0, time_s / fade_s, (duration_s - time_s) / fade_s)
        yield pad * 0.19 * breath * max(0.0, edge)


def cue_samples(duration_s: float = 0.24):
    total = int(SAMPLE_RATE * duration_s)
    for index in range(total):
        time_s = index / SAMPLE_RATE
        envelope = math.exp(-24.0 * time_s)
        tone = math.sin(2.0 * math.pi * 1_050 * time_s)
        overtone = 0.28 * math.sin(2.0 * math.pi * 1_570 * time_s)
        yield 0.72 * envelope * (tone + overtone) * min(1.0, time_s * 100.0)


def main() -> None:
    write_mono(ROOT / "module03_music.wav", music_samples())
    write_mono(ROOT / "mode_a_tick.wav", cue_samples())
    print("Created original starter music and cue WAV files.")


if __name__ == "__main__":
    main()
