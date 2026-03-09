#!/opt/miniforge3/bin/python
from __future__ import annotations

import os
import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path("/home/zhou/MyCodes/majhang_site")
MKDOCS = ROOT / "site_src" / "mkdocs.yml"
DOCS_ROOT = ROOT / "site_src" / "docs"

NAV_START = "<!-- PAGE NAV START -->"
NAV_END = "<!-- PAGE NAV END -->"


@dataclass
class Page:
    section: str
    title: str
    path: str

    @property
    def is_home(self) -> bool:
        return self.path == "index.md"

    @property
    def is_section_index(self) -> bool:
        return self.path.endswith("/index.md")

    @property
    def html_path(self) -> str:
        return self.path[:-3] + ".html"


def parse_nav() -> list[Page]:
    lines = MKDOCS.read_text(encoding="utf-8").splitlines()
    in_nav = False
    current_section = ""
    pages: list[Page] = []

    for line in lines:
        if not in_nav:
            if line.strip() == "nav:":
                in_nav = True
            continue

        if line and not line.startswith(" "):
            break

        top = re.match(r"^  - ([^:]+):(?:\s*(\S.*))?$", line)
        if top:
            title = top.group(1).strip()
            value = top.group(2)
            if value:
                pages.append(Page(section=title, title=title, path=value.strip()))
                current_section = ""
            else:
                current_section = title
            continue

        child = re.match(r"^    - ([^:]+):\s*(\S.*)$", line)
        if child and current_section:
            pages.append(
                Page(
                    section=current_section,
                    title=child.group(1).strip(),
                    path=child.group(2).strip(),
                )
            )

    return pages


def rel_html_path(current: Page, target: Page) -> str:
    current_dir = os.path.dirname(current.html_path) or "."
    return os.path.relpath(target.html_path, current_dir).replace("\\", "/")


def nav_label(current: Page, target: Page, is_prev: bool) -> str:
    if target.is_home:
        return "返回首页"

    if target.is_section_index:
        if target.section == current.section:
            return f"返回导读：{target.section}"
        prefix = "上一章" if is_prev else "下一章"
        return f"{prefix}：{target.section}"

    if target.section == current.section:
        prefix = "上一节" if is_prev else "下一节"
        return f"{prefix}：{target.title}"

    prefix = "上一章" if is_prev else "下一章"
    return f"{prefix}：{target.section}"


def nav_html(current: Page, prev_page: Page | None, next_page: Page | None) -> str:
    prev_html = (
        f'<a class="page-nav__link page-nav__link--prev" href="{rel_html_path(current, prev_page)}">{nav_label(current, prev_page, True)}</a>'
        if prev_page
        else '<span class="page-nav__spacer"></span>'
    )
    next_html = (
        f'<a class="page-nav__link page-nav__link--next" href="{rel_html_path(current, next_page)}">{nav_label(current, next_page, False)}</a>'
        if next_page
        else '<span class="page-nav__spacer"></span>'
    )

    return (
        f"{NAV_START}\n"
        '<div class="page-nav" markdown="0">\n'
        f"  {prev_html}\n"
        f"  {next_html}\n"
        "</div>\n"
        f"{NAV_END}"
    )


def update_page(page: Page, prev_page: Page | None, next_page: Page | None) -> None:
    file_path = DOCS_ROOT / page.path
    text = file_path.read_text(encoding="utf-8")
    block = nav_html(page, prev_page, next_page)

    pattern = re.compile(
        rf"\n?{re.escape(NAV_START)}.*?{re.escape(NAV_END)}\n?",
        re.DOTALL,
    )
    if pattern.search(text):
        text = pattern.sub("\n" + block + "\n", text).rstrip() + "\n"
    else:
        text = text.rstrip() + "\n\n" + block + "\n"

    file_path.write_text(text, encoding="utf-8")


def main() -> None:
    pages = parse_nav()
    for index, page in enumerate(pages):
        prev_page = pages[index - 1] if index > 0 else None
        next_page = pages[index + 1] if index + 1 < len(pages) else None
        update_page(page, prev_page, next_page)
    print(f"Updated page nav for {len(pages)} pages.")


if __name__ == "__main__":
    main()
