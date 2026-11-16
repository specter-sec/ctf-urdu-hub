#!/usr/bin/env python3
"""Generate a deterministic, fictional HTML source-inspection practice page."""

from pathlib import Path


def main() -> None:
    # Resolve output relative to this script, never to the caller's working directory.
    output_dir = Path(__file__).resolve().parent / "work" / "web-source"
    output_dir.mkdir(parents=True, exist_ok=True)

    page = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Northstar Garden Club - Welcome</title>
  <style>
    body { max-width: 42rem; margin: 3rem auto; padding: 0 1rem; font-family: sans-serif; }
    main { border: 1px solid #bbb; border-radius: 0.5rem; padding: 1.5rem; }
  </style>
</head>
<body>
  <main>
    <h1>Northstar Garden Club</h1>
    <p>Welcome to our tiny fictional practice page.</p>
    <p>Today's activity: plant a seed and watch it grow.</p>
  </main>
  <!-- Demo clue for this offline exercise: CTFURDU{source_is_public} -->
</body>
</html>
"""
    (output_dir / "index.html").write_text(page, encoding="utf-8", newline="\n")
    print(f"Created {output_dir / 'index.html'}")


if __name__ == "__main__":
    main()
