#!/opt/miniforge3/bin/python
from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EN_DOCS = ROOT / "site_src" / "docs" / "en"
TARGET = "robots: noindex, nofollow\n"


def main() -> int:
    scanned = 0
    changed = 0

    for path in sorted(EN_DOCS.rglob("*.md")):
        scanned += 1
        text = path.read_text(encoding="utf-8")
        if TARGET not in text:
            continue
        path.write_text(text.replace(TARGET, ""), encoding="utf-8")
        changed += 1

    print(f"english_markdown_scanned={scanned}")
    print(f"english_markdown_released={changed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
