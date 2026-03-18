#!/opt/miniforge3/bin/python
from __future__ import annotations

import gzip
from pathlib import Path
from urllib.parse import urlparse
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
SITEMAP = DOCS / "sitemap.xml"
SITEMAP_GZ = DOCS / "sitemap.xml.gz"
ZH_SITEMAP = DOCS / "sitemap-zh.xml"
EN_SITEMAP = DOCS / "sitemap-en.xml"
NS = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}


def html_path_for_loc(loc: str) -> Path | None:
    parsed = urlparse(loc)
    path = parsed.path
    prefix = "/riichi_mahjong_book/"
    if not path.startswith(prefix):
        return None
    rel = path[len(prefix) :].lstrip("/")
    return DOCS / rel


def is_noindex_page(html_path: Path | None) -> bool:
    if html_path is None or not html_path.exists():
        return False
    text = html_path.read_text(encoding="utf-8", errors="ignore").lower()
    return 'name="robots" content="noindex' in text or "404.html" in html_path.name


def load_entries() -> list[tuple[str, str | None]]:
    tree = ET.parse(SITEMAP)
    root = tree.getroot()
    entries: list[tuple[str, str | None]] = []
    for url in root.findall("sm:url", NS):
        loc = url.findtext("sm:loc", default="", namespaces=NS).strip()
        lastmod = url.findtext("sm:lastmod", default="", namespaces=NS).strip() or None
        if not loc:
            continue
        if is_noindex_page(html_path_for_loc(loc)):
            continue
        entries.append((loc, lastmod))
    return entries


def write_sitemap(path: Path, entries: list[tuple[str, str | None]]) -> None:
    urlset = ET.Element("urlset", xmlns=NS["sm"])
    for loc, lastmod in entries:
        url = ET.SubElement(urlset, "url")
        ET.SubElement(url, "loc").text = loc
        if lastmod:
            ET.SubElement(url, "lastmod").text = lastmod
    ET.ElementTree(urlset).write(path, encoding="utf-8", xml_declaration=True)


def gzip_main_sitemap() -> None:
    with SITEMAP.open("rb") as src, gzip.open(SITEMAP_GZ, "wb") as dst:
        dst.write(src.read())


def main() -> int:
    entries = load_entries()
    zh_entries = [item for item in entries if "/riichi_mahjong_book/en/" not in item[0]]
    en_entries = [item for item in entries if "/riichi_mahjong_book/en/" in item[0]]

    write_sitemap(SITEMAP, entries)
    write_sitemap(ZH_SITEMAP, zh_entries)
    write_sitemap(EN_SITEMAP, en_entries)
    gzip_main_sitemap()

    print(f"sitemap_all_entries={len(entries)}")
    print(f"sitemap_zh_entries={len(zh_entries)}")
    print(f"sitemap_en_entries={len(en_entries)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
