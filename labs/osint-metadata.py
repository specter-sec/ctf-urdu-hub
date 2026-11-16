#!/usr/bin/env python3
"""Generate a deterministic, fictional OSINT/metadata practice fixture.

All generated files are confined to labs/work/osint-metadata beneath this
repository. This script uses only the Python standard library and no network.
"""

import base64
import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = REPO_ROOT / "labs" / "work" / "osint-metadata"

# A valid 1x1 transparent PNG. The trailing marker is deliberately appended
# after the PNG's IEND chunk; it is not EXIF, PNG metadata, or proof of origin.
TINY_PNG_BASE64 = (
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+j"
    "XioAAAAASUVORK5CYII="
)
DEMO_MARKER = b"\nCTFURDU{local_metadata_is_not_proof}\n"

SYNTHETIC_METADATA = {
    "notice": "FICTIONAL LOCAL PRACTICE DATA; NOT EXIF AND NOT A REAL PERSON",
    "fictional_claims": {
        "creator": "Mina Example",
        "caption": "A tiny demo image for an offline exercise",
        "claimed_source": "https://example.invalid/gallery/demo-17",
        "claimed_capture_date": "2025-01-15",
        "claimed_camera": "DemoCam 1 (invented)",
    },
    "verification_note": (
        "These are invented claims in JSON. They are not embedded image metadata. "
        "Verify claims independently before treating them as true."
    ),
}


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    image_path = OUTPUT_DIR / "demo-image.png"
    metadata_path = OUTPUT_DIR / "synthetic-metadata.json"

    image_bytes = base64.b64decode(TINY_PNG_BASE64) + DEMO_MARKER
    image_path.write_bytes(image_bytes)
    metadata_path.write_text(
        json.dumps(SYNTHETIC_METADATA, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )

    print("Created offline fictional practice fixture:")
    print(f"- {image_path.relative_to(REPO_ROOT)}")
    print(f"- {metadata_path.relative_to(REPO_ROOT)}")
    print("No network used. JSON is synthetic and not EXIF.")


if __name__ == "__main__":
    main()
