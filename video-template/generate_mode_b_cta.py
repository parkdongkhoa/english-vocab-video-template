from __future__ import annotations

import json

from generate_reference_mode_b_hybrid_voice import MANIFEST_PATH, OUT_DIR, cit_generate
from reference_modes_data import MODE_B_CTA_TEXT


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    output = OUT_DIR / "mode_b_cta.wav"
    result = cit_generate(MODE_B_CTA_TEXT, output)
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    files = manifest.setdefault("files", {})
    files["mode_b_cta"] = result
    MANIFEST_PATH.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
