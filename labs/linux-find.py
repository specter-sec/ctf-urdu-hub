#!/usr/bin/env python3
"""Build a tiny deterministic, offline file-finding practice tree."""

from pathlib import Path
import shutil


def main() -> None:
    repo_root = Path(__file__).resolve().parent.parent
    labs_dir = repo_root / "labs"
    work_dir = labs_dir / "work"
    output_dir = work_dir / "linux-find"

    # Do not follow a pre-existing link where cleanup or creation is expected.
    if labs_dir.is_symlink() or work_dir.is_symlink() or output_dir.is_symlink():
        raise SystemExit("Refusing to use a symlink in the fixed lab output path.")

    if output_dir.exists():
        if not output_dir.is_dir():
            raise SystemExit("The fixed lab output path exists but is not a directory.")
        shutil.rmtree(output_dir)

    output_dir.mkdir(parents=True, exist_ok=True)
    archive_dir = output_dir / "field-notes" / "archive"
    archive_dir.mkdir(parents=True, exist_ok=True)

    files = {
        output_dir / "README.txt": (
            "Offline practice tree for CTF Urdu Hub.\n"
            "Search below this folder for clue.txt.\n"
        ),
        output_dir / "field-notes" / "today.txt": (
            "A note for practice: not every file is the one you need.\n"
        ),
        archive_dir / "index.txt": (
            "Archive index: inspect filenames, then read the matching file.\n"
        ),
        archive_dir / "clue.txt": (
            "Demo marker: CTFURDU{find_then_read_local_file}\n"
            "This marker is fictional and belongs only to this local exercise.\n"
        ),
    }

    for path, text in files.items():
        path.write_text(text, encoding="utf-8", newline="\n")

    print("Created offline practice files in labs/work/linux-find")


if __name__ == "__main__":
    main()
