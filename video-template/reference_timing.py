from __future__ import annotations

import json
from pathlib import Path

from reference_modes_data import MODE_A_ITEMS, MODE_B_CARDS, ROOT


AUDIO_DIR = ROOT / "audio_cit"
HYBRID_AUDIO_DIR = ROOT / "audio_hybrid"
MANIFEST = AUDIO_DIR / "manifest.json"
HYBRID_MANIFEST = HYBRID_AUDIO_DIR / "manifest.json"

# These values are deliberately explicit so the visual and audio timelines use
# the same source of truth. Every countdown digit occupies exactly one second.
MODE_A_INTRO = 2.70
MODE_A_VI_GAP = 0.0
MODE_A_COUNTDOWN = 3.0
MODE_A_ANSWER_GAP = 0.0
MODE_A_SENTENCE_TAIL = 0.0
# Keep the CTA visible until its full spoken line finishes, then hold briefly
# so the ending does not feel clipped.
MODE_A_CTA_TAIL = 0.35

MODE_B_INTRO = 2.20
MODE_B_TARGET_OFFSET = 0.35
MODE_B_TARGET_GAP = 0.22
MODE_B_CARD_DURATION = 6.25
MODE_B_REVEAL_AT = 5.00
MODE_B_CTA_TAIL = 0.55


def _manifest() -> dict[str, object]:
    if not MANIFEST.exists():
        raise FileNotFoundError(f"Missing CIT voice manifest: {MANIFEST}")
    return json.loads(MANIFEST.read_text(encoding="utf-8"))


def _manifest_for(name: str) -> dict[str, object]:
    if (name.startswith("mode_a_") or name.startswith("mode_b_") or name.startswith("countdown_")) and HYBRID_MANIFEST.exists():
        return json.loads(HYBRID_MANIFEST.read_text(encoding="utf-8"))
    return _manifest()


def audio_duration(name: str) -> float:
    data = _manifest_for(name)["files"]
    assert isinstance(data, dict)
    item = data[name]
    assert isinstance(item, dict)
    value = item.get("duration_header")
    if value is None:
        raise ValueError(f"No duration recorded for CIT asset {name}")
    return float(value)


def audio_path(name: str) -> Path:
    if (name.startswith("mode_a_") or name.startswith("mode_b_") or name.startswith("countdown_")) and HYBRID_AUDIO_DIR.exists():
        candidate = HYBRID_AUDIO_DIR / f"{name}.wav"
        if candidate.exists():
            return candidate
    return AUDIO_DIR / f"{name}.wav"


def mode_a_timeline() -> dict[str, object]:
    cursor = MODE_A_INTRO
    items: list[dict[str, float | int]] = []
    for index, _item in enumerate(MODE_A_ITEMS, 1):
        vi_duration = audio_duration(f"mode_a_q{index:02d}_vi")
        en_duration = audio_duration(f"mode_a_q{index:02d}_sentence")
        start = cursor
        countdown_start = start + vi_duration + MODE_A_VI_GAP
        answer_start = countdown_start + MODE_A_COUNTDOWN + MODE_A_ANSWER_GAP
        end = answer_start + en_duration + MODE_A_SENTENCE_TAIL
        items.append(
            {
                "index": index - 1,
                "start": start,
                "vi_duration": vi_duration,
                "en_duration": en_duration,
                "countdown_start": countdown_start,
                "answer_start": answer_start,
                "end": end,
            }
        )
        cursor = end
    cta_start = cursor
    cta_audio_duration = audio_duration("mode_a_cta")
    cta_duration = cta_audio_duration + MODE_A_CTA_TAIL
    return {
        "intro": MODE_A_INTRO,
        "items": items,
        "cta_start": cta_start,
        "cta_audio_duration": cta_audio_duration,
        "cta_duration": cta_duration,
        "duration": cta_start + cta_duration,
    }


def mode_b_timeline() -> dict[str, object]:
    cursor = 0.0
    cards: list[dict[str, float | int]] = []
    for index, card in enumerate(MODE_B_CARDS):
        target_duration = audio_duration(f"mode_b_{card['target']}_en")
        start = cursor
        # The first card stays on screen while the Vietnamese intro plays;
        # subsequent cards begin with a short, consistent listening lead-in.
        target_start = start + (MODE_B_INTRO + 0.10 if index == 0 else MODE_B_TARGET_OFFSET)
        reveal_start = start + MODE_B_REVEAL_AT
        end = start + MODE_B_CARD_DURATION
        cards.append(
            {
                "index": index,
                "start": start,
                "target_duration": target_duration,
                "target_start": target_start,
                "reveal_start": reveal_start,
                "end": end,
            }
        )
        cursor = end
    cta_start = cursor
    cta_audio_duration = audio_duration("mode_b_cta")
    cta_duration = cta_audio_duration + MODE_B_CTA_TAIL
    return {
        "intro": MODE_B_INTRO,
        "cards": cards,
        "cta_start": cta_start,
        "cta_audio_duration": cta_audio_duration,
        "cta_duration": cta_duration,
        "duration": cta_start + cta_duration,
    }
