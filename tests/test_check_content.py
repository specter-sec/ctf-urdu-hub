from __future__ import annotations

import importlib.util
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("check_content", REPO_ROOT / "scripts" / "check_content.py")
assert SPEC and SPEC.loader
checker = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = checker
SPEC.loader.exec_module(checker)


class FrontmatterTests(unittest.TestCase):
    def test_accepts_mapping_with_title_description_and_tags(self) -> None:
        errors = checker.check_frontmatter(Path("sample.md"), "---\ntitle: Sample\ndescription: Notes\ntags:\n  - beginner\n---\n# Hi\n", "sample.md")
        self.assertEqual(errors, [])

    def test_rejects_unclosed_frontmatter(self) -> None:
        errors = checker.check_frontmatter(Path("sample.md"), "---\ntitle: Sample\n", "sample.md")
        self.assertTrue(any("no closing" in error.message for error in errors))

    def test_rejects_non_mapping_and_invalid_tags(self) -> None:
        non_mapping = checker.check_frontmatter(Path("sample.md"), "---\n- item\n---\n", "sample.md")
        bad_tags = checker.check_frontmatter(Path("sample.md"), "---\ntags: web\n---\n", "sample.md")
        self.assertTrue(any("mapping" in error.message for error in non_mapping))
        self.assertTrue(any("YAML list" in error.message for error in bad_tags))

    def test_rejects_duplicate_tags_and_malformed_yaml(self) -> None:
        duplicate = checker.check_frontmatter(Path("sample.md"), "---\ntags: [web, web]\n---\n", "sample.md")
        malformed = checker.check_frontmatter(Path("sample.md"), "---\ntitle: [unterminated\n---\n", "sample.md")
        self.assertTrue(any("duplicates" in error.message for error in duplicate))
        self.assertTrue(any("invalid YAML" in error.message for error in malformed))


class LinkTests(unittest.TestCase):
    def test_resolves_relative_markdown_link(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "docs" / "guide").mkdir(parents=True)
            source = root / "docs" / "guide" / "index.md"
            source.write_text("[next](../next.md)\n", encoding="utf-8")
            (root / "docs" / "next.md").write_text("# next\n", encoding="utf-8")
            self.assertEqual(checker.check_links(root, source, source.read_text(encoding="utf-8")), [])

    def test_reports_missing_internal_link_and_screenshot(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "README.md"
            text = "[missing](docs/nope.md) ![desktop](docs/screenshots/desktop.png)\n"
            source.write_text(text, encoding="utf-8")
            issues = checker.check_links(root, source, text)
            self.assertEqual(len(issues), 2)
            self.assertIn("docs/nope.md", issues[0].message)
            self.assertIn("docs/screenshots/desktop.png", issues[1].message)

    def test_strips_fenced_code_before_link_scan(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "README.md"
            text = "```md\n[example](does-not-exist.md)\n```\n"
            source.write_text(text, encoding="utf-8")
            self.assertEqual(checker.check_links(root, source, text), [])


class AdditionalLinkTests(unittest.TestCase):
    def test_existing_screenshot_is_accepted(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            image = root / "docs/screenshots/desktop.png"
            image.parent.mkdir(parents=True)
            image.write_bytes(b"fictional test asset")
            self.assertEqual(checker.check_links(root, root / "README.md", "![view](docs/screenshots/desktop.png)"), [])

    def test_missing_raw_html_link_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.assertTrue(checker.check_links(root, root / "index.md", '<a href="missing/">next</a>'))

    def test_pretty_html_link_resolves_to_markdown(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "guide.md").write_text("# Guide\n")
            self.assertEqual(checker.check_links(root, root / "index.md", '<a href="guide/">next</a>'), [])


class WriteupMetadataTests(unittest.TestCase):
    def test_frontmatter_is_required(self) -> None:
        self.assertTrue(checker.check_writeup_metadata("# Notes", "notes.md"))

    def test_metadata_fields_are_required(self) -> None:
        issues = checker.check_writeup_metadata("---\ntitle: Test\n---\n# Test", "notes.md")
        self.assertEqual(len(issues), 5)

    def test_complete_metadata_is_accepted(self) -> None:
        content = "---\ntitle: Test\ndescription: Local practice\ncategory: Web\ndifficulty: Beginner\nplatform: picoCTF\ntags: [web]\n---\n# Test"
        self.assertEqual(checker.check_writeup_metadata(content, "notes.md"), [])


class SafetyPatternTests(unittest.TestCase):
    def test_detects_platform_flag_and_secret_patterns(self) -> None:
        flag_examples = ("sample picoCTF" + "{" + "not-a-real-flag}", "sample THM" + "{" + "not-a-real-flag}")
        for text in flag_examples:
            self.assertTrue(any("flag" in issue.message for issue in checker.check_sensitive_text(REPO_ROOT / "README.md", text)))
        secret_reference = "{" + "{secret:account.token}}"
        self.assertTrue(any("secret" in issue.message for issue in checker.check_sensitive_text(REPO_ROOT / "README.md", secret_reference)))
        self.assertEqual(checker.check_sensitive_text(REPO_ROOT / "README.md", "CTFURDU{fictional_local_demo}"), [])


class RequiredContentTests(unittest.TestCase):
    def test_validator_lists_missing_required_pages(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.md").write_text("# Minimal\n", encoding="utf-8")
            issues = checker.validate(root)
            missing = {issue.path for issue in issues if "required project file" in issue.message}
            self.assertIn("docs/writeups/web/source-pehchano.md", missing)
            self.assertIn("docs/guides/getting-started.md", missing)
            self.assertIn("labs/osint-metadata.py", missing)


class LabGeneratorTests(unittest.TestCase):
    """Run each generator exactly once in an isolated temporary repository."""

    EXPECTED_OUTPUTS = {
        "web-source.py": {"labs/work/web-source/index.html"},
        "crypto-rot13.py": {"labs/work/crypto-rot13/ciphertext.txt"},
        "forensics-strings.py": {"labs/work/forensics-strings/garden.png"},
        "linux-find.py": {
            "labs/work/linux-find/README.txt",
            "labs/work/linux-find/field-notes/today.txt",
            "labs/work/linux-find/field-notes/archive/index.txt",
            "labs/work/linux-find/field-notes/archive/clue.txt",
        },
        "osint-metadata.py": {
            "labs/work/osint-metadata/demo-image.png",
            "labs/work/osint-metadata/synthetic-metadata.json",
        },
    }

    def test_generators_run_once_and_write_only_inside_their_fixture_tree(self) -> None:
        source_dir = REPO_ROOT / "labs"
        with tempfile.TemporaryDirectory(prefix="ctf-urdu-hub-labs-") as temp_dir:
            isolated_root = Path(temp_dir)
            isolated_labs = isolated_root / "labs"
            isolated_labs.mkdir()
            for filename in self.EXPECTED_OUTPUTS:
                shutil.copy2(source_dir / filename, isolated_labs / filename)

            for filename in self.EXPECTED_OUTPUTS:
                result = subprocess.run(
                    [sys.executable, str(isolated_labs / filename)],
                    cwd=isolated_root,
                    text=True,
                    capture_output=True,
                    timeout=30,
                    check=False,
                )
                self.assertEqual(result.returncode, 0, f"{filename} failed:\n{result.stdout}\n{result.stderr}")
                self.assertEqual(result.stderr, "", f"{filename} wrote unexpected stderr")
            observed = {
                path.relative_to(isolated_root).as_posix()
                for path in isolated_labs.rglob("*")
                if path.is_file() and "work" in path.parts
            }
            expected = set().union(*self.EXPECTED_OUTPUTS.values())
            self.assertEqual(observed, expected)
            self.assertTrue(all((isolated_root / item).is_file() for item in expected))
            all_files = {path.relative_to(isolated_root).as_posix() for path in isolated_root.rglob("*") if path.is_file()}
            copied_scripts = {f"labs/{filename}" for filename in self.EXPECTED_OUTPUTS}
            self.assertEqual(all_files, copied_scripts | expected)


class SolutionTests(unittest.TestCase):
    def test_local_solutions_and_determinism(self) -> None:
        import codecs
        import hashlib
        import re
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            labs = root / "labs"
            labs.mkdir()
            for name in LabGeneratorTests.EXPECTED_OUTPUTS:
                shutil.copy2(REPO_ROOT / "labs" / name, labs / name)
                subprocess.run([sys.executable, str(labs / name)], cwd=root, capture_output=True, check=True, timeout=15)
            def snapshot():
                return {p.relative_to(root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in (labs / "work").rglob("*") if p.is_file()}
            before = snapshot()
            for name in LabGeneratorTests.EXPECTED_OUTPUTS:
                subprocess.run([sys.executable, str(labs / name)], cwd=root, capture_output=True, check=True, timeout=15)
            self.assertEqual(before, snapshot())
            web = (labs / "work/web-source/index.html").read_text()
            self.assertEqual(re.search(r"CTFURDU\{[^}]+\}", web).group(), "CTFURDU{source_is_public}")
            cipher = (labs / "work/crypto-rot13/ciphertext.txt").read_text().strip()
            self.assertEqual(codecs.decode(cipher, "rot_13"), "CTFURDU{modulo_wraps_letters}")
            self.assertIn(b"CTFURDU{garden_strings_are_printable}", (labs / "work/forensics-strings/garden.png").read_bytes())
            self.assertIn("CTFURDU{", (labs / "work/linux-find/field-notes/archive/clue.txt").read_text())
            self.assertTrue((labs / "work/osint-metadata/demo-image.png").read_bytes().endswith(b"\nCTFURDU{local_metadata_is_not_proof}\n"))


if __name__ == "__main__":
    unittest.main()
