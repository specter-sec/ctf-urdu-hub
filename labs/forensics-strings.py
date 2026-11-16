#!/usr/bin/env python3
"""Create a deterministic, fictional PNG fixture for offline strings practice."""

import base64
from pathlib import Path


PNG_BASE64 = (
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNQKFjwHwAEFAIwzR/GZQAA"
    "AABJRU5ErkJggg=="
)
DEMO_MARKER = b"\nCTFURDU{garden_strings_are_printable}\n"


def main():
    repo_root = Path(__file__).resolve().parent.parent
    output_dir = repo_root / "labs" / "work" / "forensics-strings"
    output_dir.mkdir(parents=True, exist_ok=True)

    png_data = base64.b64decode(PNG_BASE64)
    if not png_data.startswith(b"\x89PNG\r\n\x1a\n"):
        raise ValueError("Embedded fixture does not have a PNG signature")

    output_path = output_dir / "garden.png"
    output_path.write_bytes(png_data + DEMO_MARKER)
    print(f"Created fictional offline fixture: {output_path.relative_to(repo_root)}")
    print("The demo marker is appended after the PNG data for printable-string practice.")


if __name__ == "__main__":
    main()
