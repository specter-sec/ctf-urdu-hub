#!/usr/bin/env python3
"""Generate the CTF Urdu Hub original offline ROT13 practice fixture."""

from pathlib import Path


PLAINTEXT = "CTFURDU{modulo_wraps_letters}"
LOWER = "abcdefghijklmnopqrstuvwxyz"
UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def rot13(text: str) -> str:
    """Rotate ASCII English letters by 13; preserve all other characters."""
    result = []
    for character in text:
        if character in LOWER:
            result.append(LOWER[(LOWER.index(character) + 13) % 26])
        elif character in UPPER:
            result.append(UPPER[(UPPER.index(character) + 13) % 26])
        else:
            result.append(character)
    return "".join(result)


def main() -> None:
    lab_dir = Path(__file__).resolve().parent
    work_root = lab_dir / "work"
    if work_root.is_symlink():
        raise RuntimeError("Refusing to write through a symlink at labs/work")
    work_root.mkdir(parents=True, exist_ok=True)
    if work_root.resolve().parent != lab_dir:
        raise RuntimeError("Refusing to write outside labs/work")

    output_dir = work_root / "crypto-rot13"
    if output_dir.is_symlink():
        raise RuntimeError("Refusing to write through a symlink at labs/work/crypto-rot13")
    output_dir.mkdir(parents=True, exist_ok=True)
    if output_dir.resolve().parent != work_root.resolve():
        raise RuntimeError("Refusing to write outside labs/work/crypto-rot13")

    ciphertext = rot13(PLAINTEXT)
    fixture = output_dir / "ciphertext.txt"
    if fixture.is_symlink():
        raise RuntimeError("Refusing to write through a symlink at ciphertext.txt")
    fixture.write_text(ciphertext + "\n", encoding="ascii")
    print("Created local practice fixture: labs/work/crypto-rot13/ciphertext.txt")
    print(f"Ciphertext: {ciphertext}")


if __name__ == "__main__":
    main()
