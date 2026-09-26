from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path
from urllib.request import Request, urlopen

import requests

from reference_modes_data import MODE_B_CARDS, MODE_B_CTA_TEXT, MODE_B_INTRO_TEXT, ROOT


ENV_FILE = Path(__file__).resolve().parent / ".env"


def load_local_env() -> None:
    """Load simple KEY=VALUE settings without exposing them in logs."""
    if not ENV_FILE.exists():
        return
    for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        name, value = line.split("=", 1)
        os.environ.setdefault(name.strip(), value.strip().strip('"').strip("'"))


load_local_env()
CIT_BASE_URL = os.environ.get("CIT_BASE_URL", "http://127.0.0.1:8001").rstrip("/")
CIT_VOICE_ID = os.environ.get("CIT_VOICE_ID", "Đoan Trang")
ELEVEN_VOICE_ID = os.environ.get("ELEVENLABS_VOICE_ID", "XrExE9yKIg1WjnnlVkGX")
ELEVEN_MODEL_ID = os.environ.get("ELEVENLABS_MODEL_ID", "eleven_v3")
OUT_DIR = ROOT / "audio_hybrid"
MANIFEST_PATH = OUT_DIR / "manifest.json"


def cit_generate(text: str, output_path: Path) -> dict[str, object]:
    if not CIT_VOICE_ID.strip():
        raise RuntimeError("CIT_VOICE_ID is not configured; enter a voice ID assigned by your CIT Voice Studio service")
    payload = json.dumps(
        {
            "text": text,
            "voice_id": CIT_VOICE_ID,
            "speed": 1.0,
            "temperature": 0.7,
            "format": "wav",
            "use_pronunciation_dict": True,
        },
        ensure_ascii=False,
    ).encode("utf-8")
    headers = {"Accept": "audio/wav", "Content-Type": "application/json; charset=utf-8"}
    cit_api_key = os.environ.get("CIT_API_KEY", "").strip()
    if cit_api_key:
        headers["X-API-Key"] = cit_api_key
    request = Request(
        f"{CIT_BASE_URL}/api/tts/generate",
        data=payload,
        headers=headers,
        method="POST",
    )
    with urlopen(request, timeout=300) as response:
        audio = response.read()
        duration = response.headers.get("X-Duration-Seconds")
    output_path.write_bytes(audio)
    return {"path": str(output_path), "text": text, "voice_id": CIT_VOICE_ID, "duration_header": duration}


def eleven_key() -> str:
    key = os.environ.get("ELEVENLABS_API_KEY", "").strip()
    if key:
        return key
    raise RuntimeError("ELEVENLABS_API_KEY is not configured; add it to the project .env file")


def eleven_generate(text: str, output_path: Path, key: str) -> dict[str, object]:
    response = requests.post(
        f"https://api.elevenlabs.io/v1/text-to-speech/{ELEVEN_VOICE_ID}",
        params={"output_format": "mp3_44100_128"},
        headers={"xi-api-key": key, "Content-Type": "application/json"},
        json={
            "text": text,
            "model_id": ELEVEN_MODEL_ID,
            "language_code": "en",
            "voice_settings": {
                "stability": 0.70,
                "similarity_boost": 0.88,
                "style": 0.10,
                "use_speaker_boost": True,
            },
        },
        timeout=120,
    )
    response.raise_for_status()
    temp_mp3 = output_path.with_suffix(".mp3")
    temp_mp3.write_bytes(response.content)
    subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", str(temp_mp3), "-ar", "48000", "-ac", "1", str(output_path)], check=True)
    temp_mp3.unlink(missing_ok=True)
    duration = subprocess.check_output(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=nw=1:nk=1", str(output_path)],
        text=True,
    ).strip()
    return {"path": str(output_path), "text": text, "voice_id": ELEVEN_VOICE_ID, "model_id": ELEVEN_MODEL_ID, "duration_header": duration}


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    manifest: dict[str, object] = {"cit_voice_id": CIT_VOICE_ID, "english_voice_id": ELEVEN_VOICE_ID, "english_model_id": ELEVEN_MODEL_ID, "files": {}}
    if MANIFEST_PATH.exists():
        existing = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        if isinstance(existing, dict):
            manifest.update({k: v for k, v in existing.items() if k != "files"})
            if isinstance(existing.get("files"), dict):
                manifest["files"] = existing["files"]
    files = manifest["files"]
    assert isinstance(files, dict)
    key = eleven_key()
    jobs: list[tuple[str, str, str]] = [
        ("mode_b_intro", "vi", MODE_B_INTRO_TEXT),
        ("mode_b_cta", "vi", MODE_B_CTA_TEXT),
    ]
    for card in MODE_B_CARDS:
        jobs.append((f"mode_b_{card['target']}_en", "en", card["target"]))
    for name, language, text in jobs:
        output_path = OUT_DIR / f"{name}.wav"
        result = cit_generate(text, output_path) if language == "vi" else eleven_generate(text, output_path, key)
        files[name] = result
        print(json.dumps(result, ensure_ascii=False))
    MANIFEST_PATH.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"wrote {MANIFEST_PATH}")


if __name__ == "__main__":
    main()
