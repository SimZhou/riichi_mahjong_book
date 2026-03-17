#!/opt/miniforge3/bin/python
from __future__ import annotations

import argparse
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS_SRC = ROOT / "site_src" / "docs"
EN_SRC = DOCS_SRC / "en"
DOCS_OUT = ROOT / "docs" / "en"

ASSET_RE = re.compile(r"(?P<prefix>(?:\.\./)+)(?P<kind>hai|images)/")
HTML_RE = re.compile(r"""(?P<attr>src|href)=["'](?P<prefix>(?:\.\./)+)(?P<kind>hai|images)/""")


def expected_prefix(path: Path, base: Path) -> str:
    depth = len(path.relative_to(base).parent.parts)
    return "../" * depth


def normalize_text(text: str, target_prefix: str) -> tuple[str, int]:
    replacements = 0

    def replace(match: re.Match[str]) -> str:
        nonlocal replacements
        prefix = match.group("prefix")
        kind = match.group("kind")
        if prefix == target_prefix:
            return match.group(0)
        replacements += 1
        return f"{target_prefix}{kind}/"

    return ASSET_RE.sub(replace, text), replacements


def fix_markdown_files(apply: bool) -> tuple[int, int, int]:
    files_scanned = 0
    files_changed = 0
    replacements = 0

    for path in sorted(EN_SRC.rglob("*.md")):
        files_scanned += 1
        text = path.read_text(encoding="utf-8")
        new_text, count = normalize_text(text, expected_prefix(path, DOCS_SRC))
        if count:
            files_changed += 1
            replacements += count
            if apply:
                path.write_text(new_text, encoding="utf-8")

    return files_scanned, files_changed, replacements


def check_built_html() -> list[str]:
    problems: list[str] = []

    if not DOCS_OUT.exists():
        return ["docs/en does not exist yet; build the site before running HTML checks."]

    for path in sorted(DOCS_OUT.rglob("*.html")):
        text = path.read_text(encoding="utf-8")
        want = expected_prefix(path, ROOT / "docs")
        for match in HTML_RE.finditer(text):
            prefix = match.group("prefix")
            kind = match.group("kind")
            if prefix != want:
                problems.append(
                    f"{path.relative_to(ROOT)}: expected {want}{kind}/ but found {prefix}{kind}/"
                )

    return problems


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check and optionally fix local hai/images relative paths in English markdown pages."
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Rewrite English markdown files in place when bad local asset prefixes are found.",
    )
    parser.add_argument(
        "--check-built",
        action="store_true",
        help="Also validate generated docs/en HTML asset prefixes after a site build.",
    )
    args = parser.parse_args()

    scanned, changed, replacements = fix_markdown_files(apply=args.apply)
    mode = "fixed" if args.apply else "checked"
    print(f"{mode} {scanned} English markdown files")
    print(f"files with asset-prefix updates: {changed}")
    print(f"asset-prefix replacements: {replacements}")

    if args.check_built:
        problems = check_built_html()
        if problems:
            print("built HTML path issues found:")
            for line in problems:
                print(f" - {line}")
            return 1
        print("built HTML asset-prefix check passed")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
