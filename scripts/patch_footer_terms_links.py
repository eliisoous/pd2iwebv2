#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert terms-of-sale link into explicit bottomLinks arrays across HTML files."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def already_patched(block: str) -> bool:
    return "terms-of-sale.html" in block


def patch_bottom_links_section(m: re.Match) -> str:
    block = m.group(0)
    if already_patched(block):
        return block

    # EN /en/ — link to root English terms page (closing `]` of array; comma may follow outside match)
    b, n = re.subn(
        r"(?P<ind>[\t ]*)\{ label: 'Legal Informations', href: '\.\./legal\.html' \}\s*\n(?P<c>[\t ]+)\]",
        r"\g<ind>{ label: 'Legal Informations', href: '../legal.html' },\n\g<ind>{ label: 'General Terms of Sale', href: '../terms-of-sale.html' }\n\g<c>]",
        block,
        count=1,
    )
    if n:
        return b

    # EN root & pages using English labels with local hrefs
    b, n = re.subn(
        r"(?P<ind>[\t ]*)\{ label: 'Legal Informations', href: 'legal\.html' \}\s*\n(?P<c>[\t ]+)\]",
        r"\g<ind>{ label: 'Legal Informations', href: 'legal.html' },\n\g<ind>{ label: 'General Terms of Sale', href: 'terms-of-sale.html' }\n\g<c>]",
        block,
        count=1,
    )
    if n:
        return b

    # FR
    b, n = re.subn(
        r"(?P<ind>[\t ]*)\{ label: 'Mentions légales', href: 'legal\.html' \}\s*\n(?P<c>[\t ]+)\]",
        r"\g<ind>{ label: 'Mentions légales', href: 'legal.html' },\n\g<ind>{ label: 'Conditions générales de vente', href: 'terms-of-sale.html' }\n\g<c>]",
        block,
        count=1,
    )
    if n:
        return b

    # ZH
    b, n = re.subn(
        r"(?P<ind>[\t ]*)\{ label: '法律信息', href: 'legal\.html' \}\s*\n(?P<c>[\t ]+)\]",
        r"\g<ind>{ label: '法律信息', href: 'legal.html' },\n\g<ind>{ label: '销售条款与条件', href: 'terms-of-sale.html' }\n\g<c>]",
        block,
        count=1,
    )
    if n:
        return b

    return block


def patch_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if "bottomLinks:" not in text:
        return False

    new_text, count = re.subn(
        r"bottomLinks:\s*\[(?:\s*\{[^}]+\},?)+\s*\]",
        patch_bottom_links_section,
        text,
        count=0,
    )
    if new_text != text:
        path.write_text(new_text, encoding="utf-8")
        return True
    return False


def main() -> None:
    n = 0
    for path in sorted(ROOT.rglob("*.html")):
        if patch_file(path):
            print("patched", path.relative_to(ROOT))
            n += 1
    print("total", n, "files")


if __name__ == "__main__":
    main()
