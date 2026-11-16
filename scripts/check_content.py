#!/usr/bin/env python3
"""Validate required project content and safe Markdown references."""
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml

ROOT = Path(__file__).resolve().parents[1]
WRITEUPS = (
    "docs/writeups/web/source-pehchano.md",
    "docs/writeups/crypto/rot13-ka-raaz.md",
    "docs/writeups/forensics/image-ke-andar.md",
    "docs/writeups/linux/file-dhoondo.md",
    "docs/writeups/osint/metadata-ka-nishan.md",
)
GUIDES = (
    "docs/guides/getting-started.md",
    "docs/guides/tools.md",
    "docs/guides/roadmap.md",
)
LABS = (
    "labs/web-source.py",
    "labs/crypto-rot13.py",
    "labs/forensics-strings.py",
    "labs/linux-find.py",
    "labs/osint-metadata.py",
)
CATEGORIES = (
    "web",
    "crypto",
    "forensics",
    "pwn",
    "reverse",
    "osint",
    "beginner-linux",
)
REQUIRED = (
    "docs/index.md",
    "docs/tags.md",
    "docs/template.md",
    "docs/ethics.md",
    *(f"docs/categories/{name}.md" for name in CATEGORIES),
    *GUIDES,
    *WRITEUPS,
    *LABS,
    "docs/screenshots/desktop.png",
    "docs/screenshots/mobile.png",
)
FRONTMATTER_TAG = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_-]*$")
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(\s*(?:<([^>]+)>|([^\s)]+))(?:\s+[^)]*)?\)")
FENCE = re.compile(r"^\s{0,3}(`{3,}|~{3,})")
FLAG_PATTERNS = (
    re.compile(r"\bpicoCTF\s*\{[^}\r\n]*\}", re.IGNORECASE),
    re.compile(r"\bTHM\s*\{[^}\r\n]*\}", re.IGNORECASE),
)
SECRET_PATTERNS = (
    re.compile(r"\{\{\s*secret\s*:", re.IGNORECASE),
    re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9_]{20,}|github_pat_[A-Za-z0-9_]{20,})\b"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"\b(?:api[_-]?key|access[_-]?token|client[_-]?secret)\s*[:=]\s*['\"]?[A-Za-z0-9._~+/=-]{16,}", re.IGNORECASE),
)


@dataclass(frozen=True)
class Issue:
    path: str
    message: str
    line: int | None = None

    def __str__(self) -> str:
        location = f":{self.line}" if self.line is not None else ""
        return f"{self.path}{location}: {self.message}"


def markdown_files(root: Path) -> list[Path]:
    """Return tracked-style project Markdown sources, excluding generated output."""
    found = list(root.glob("*.md"))
    for base in (root / "docs", root / ".github"):
        if base.exists():
            found.extend(path for path in base.rglob("*.md") if "site" not in path.parts)
    return sorted({p for p in found if p.is_file()})


def strip_fenced_code(text: str) -> str:
    """Remove fenced code blocks so sample commands are not mistaken for links."""
    output: list[str] = []
    fence_char: str | None = None
    fence_size = 0
    for line in text.splitlines():
        match = FENCE.match(line)
        if match:
            marker = match.group(1)
            if fence_char is None:
                fence_char, fence_size = marker[0], len(marker)
            elif marker[0] == fence_char and len(marker) >= fence_size:
                fence_char, fence_size = None, 0
            continue
        if fence_char is None:
            output.append(line)
    return "\n".join(output)


def check_frontmatter(path: Path, text: str, display_path: str) -> list[Issue]:
    """Validate YAML frontmatter when present; prose-only pages remain supported."""
    lines = text.lstrip("\ufeff").splitlines()
    if not lines or lines[0].strip() != "---":
        return []
    end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
    if end is None:
        return [Issue(display_path, "frontmatter starts with --- but has no closing ---", 1)]
    raw = "\n".join(lines[1:end])
    try:
        metadata = yaml.safe_load(raw)
    except yaml.YAMLError as exc:
        return [Issue(display_path, f"invalid YAML frontmatter: {exc}", 2)]
    if not isinstance(metadata, dict):
        return [Issue(display_path, "frontmatter must be a YAML mapping", 2)]
    issues: list[Issue] = []
    for key in ("title", "description"):
        if key in metadata and (not isinstance(metadata[key], str) or not metadata[key].strip()):
            issues.append(Issue(display_path, f"frontmatter {key!r} must be a non-empty string", 2))
    if "tags" in metadata:
        tags = metadata["tags"]
        if not isinstance(tags, list) or not tags:
            issues.append(Issue(display_path, "frontmatter 'tags' must be a non-empty YAML list", 2))
        elif any(not isinstance(tag, str) or not FRONTMATTER_TAG.fullmatch(tag) for tag in tags):
            issues.append(Issue(display_path, "each tag must contain only letters, digits, _ or -", 2))
        elif len(set(tags)) != len(tags):
            issues.append(Issue(display_path, "frontmatter tags must not contain duplicates", 2))
    return issues


def link_target_file(root: Path, source: Path, target: str) -> Path | None:
    """Resolve a relative local Markdown target to its source file if possible."""
    parsed = urlsplit(target)
    if parsed.scheme or parsed.netloc or target.startswith("//"):
        return None
    decoded = unquote(parsed.path)
    if not decoded:
        return source
    candidate = (root / decoded.lstrip("/")) if decoded.startswith("/") else (source.parent / decoded)
    candidate = candidate.resolve()
    try:
        candidate.relative_to(root.resolve())
    except ValueError:
        return candidate
    if candidate.is_dir():
        for index_name in ("index.md", "README.md", "index.html"):
            index = candidate / index_name
            if index.is_file():
                return index
        return candidate
    if candidate.suffix == "" and not candidate.exists():
        for suffix in (".md", ".html"):
            alternative = candidate.with_suffix(suffix)
            if alternative.is_file():
                return alternative
    return candidate


class HTMLReferences(HTMLParser):
    """Collect explicit raw-HTML links, which MkDocs does not rewrite from .md."""

    def __init__(self) -> None:
        super().__init__()
        self.targets: list[tuple[str, int]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr_name = {"a": "href", "link": "href", "img": "src", "script": "src"}.get(tag)
        if attr_name is None:
            return
        values = dict(attrs)
        target = values.get(attr_name)
        if target:
            self.targets.append((target, self.getpos()[0]))


def check_writeup_metadata(text: str, display_path: str) -> list[Issue]:
    """Require discoverability/provenance metadata on published sample writeups."""
    lines = text.lstrip("\ufeff").splitlines()
    if not lines or lines[0].strip() != "---":
        return [Issue(display_path, "sample writeup requires YAML frontmatter", 1)]
    end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
    if end is None:
        return []  # The general frontmatter check reports malformed syntax.
    try:
        metadata = yaml.safe_load("\n".join(lines[1:end]))
    except yaml.YAMLError:
        return []
    if not isinstance(metadata, dict):
        return []
    issues = []
    for field in ("title", "description", "category", "difficulty", "platform"):
        if not isinstance(metadata.get(field), str) or not metadata[field].strip():
            issues.append(Issue(display_path, f"sample writeup requires non-empty {field!r}", 2))
    if "tags" not in metadata:
        issues.append(Issue(display_path, "sample writeup requires tags", 2))
    return issues


def check_links(root: Path, path: Path, text: str) -> list[Issue]:
    issues: list[Issue] = []
    content = strip_fenced_code(text)
    parser = HTMLReferences()
    parser.feed(content)
    references = [(match.group(1) or match.group(2) or "", content.count("\n", 0, match.start()) + 1) for match in MARKDOWN_LINK.finditer(content)]
    references.extend(parser.targets)
    for target, line in references:
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc or target.startswith("//") or target.startswith("#"):
            continue
        candidate = link_target_file(root, path, target)
        if candidate is None:
            continue
        try:
            rel_target = candidate.relative_to(root.resolve()).as_posix()
        except ValueError:
            issues.append(Issue(path.relative_to(root).as_posix(), f"local link escapes repository: {target!r}"))
            continue
        if not candidate.exists():
            issues.append(Issue(path.relative_to(root).as_posix(), f"missing local link or asset {target!r}", line))
    return issues


def check_sensitive_text(path: Path, text: str) -> list[Issue]:
    issues: list[Issue] = []
    try:
        display_path = path.relative_to(ROOT).as_posix()
    except ValueError:
        display_path = path.as_posix()
    for pattern in FLAG_PATTERNS:
        for match in pattern.finditer(text):
            issues.append(Issue(display_path, "platform challenge flag pattern is not allowed", text.count("\n", 0, match.start()) + 1))
    for pattern in SECRET_PATTERNS:
        for match in pattern.finditer(text):
            issues.append(Issue(display_path, "possible secret, token, or private-key reference", text.count("\n", 0, match.start()) + 1))
    return issues


def validate(root: Path = ROOT) -> list[Issue]:
    """Collect required-file, YAML, link, flag, and secret-reference issues."""
    issues: list[Issue] = []
    for name in REQUIRED:
        if not (root / name).is_file():
            issues.append(Issue(name, "required project file is missing"))
    pages = markdown_files(root)
    for path in pages:
        display = path.relative_to(root).as_posix()
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as exc:
            issues.append(Issue(display, f"could not read UTF-8 Markdown: {exc}"))
            continue
        issues.extend(check_frontmatter(path, text, display))
        if display in WRITEUPS:
            issues.extend(check_writeup_metadata(text, display))
        issues.extend(check_links(root, path, text))
        issues.extend(check_sensitive_text(path, text))
    # Also scan Python lab source for accidental real-platform flags/secrets.
    labs_dir = root / "labs"
    if labs_dir.is_dir():
        for path in sorted(labs_dir.glob("*.py")):
            try:
                text = path.read_text(encoding="utf-8")
            except (OSError, UnicodeDecodeError) as exc:
                issues.append(Issue(path.relative_to(root).as_posix(), f"could not read UTF-8 source: {exc}"))
                continue
            issues.extend(check_sensitive_text(path, text))
    return issues


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help="project root (defaults to this repository)")
    args = parser.parse_args(argv)
    root = args.root.resolve()
    issues = validate(root)
    if issues:
        print(f"Content check failed: {len(issues)} issue(s).", file=sys.stderr)
        for issue in issues:
            print(f"- {issue}", file=sys.stderr)
        return 1
    print("Content check passed: required pages, frontmatter, local links/assets, flags, and secret patterns are valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
