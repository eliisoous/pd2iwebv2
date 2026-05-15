#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate terms-of-sale HTML pages from existing legal.html templates."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

import cgv_data  # noqa: E402


def replace_main(html: str, new_main_inner: str) -> str:
    return re.sub(
        r"<main>[\s\S]*?</main>",
        f"<main>\n{new_main_inner}\n    </main>",
        html,
        count=1,
    )


def patch_head_generic(html: str, lang: str) -> str:
    """Update only the <head> block so footer links to legal.html stay intact."""
    m = cgv_data.META[lang]
    mo = re.search(r"<head>[\s\S]*?</head>", html)
    if not mo:
        return html
    head = mo.group(0)
    head = head.replace("legal.html", "terms-of-sale.html")
    head = re.sub(
        r"<title>.*?</title>",
        f"<title>{m['title']}</title>",
        head,
        count=1,
    )
    head = re.sub(
        r'<meta name="description" content="[^"]*"',
        f'<meta name="description" content="{m["description"]}"',
        head,
        count=1,
    )
    if 'property="og:title"' in head:
        head = re.sub(
            r'<meta property="og:title" content="[^"]*"',
            f'<meta property="og:title" content="{m["title"]}"',
            head,
            count=1,
        )
    if 'property="og:description"' in head:
        head = re.sub(
            r'<meta property="og:description" content="[^"]*"',
            f'<meta property="og:description" content="{m["description"]}"',
            head,
            count=1,
        )
    return html[: mo.start()] + head + html[mo.end() :]


def patch_breadcrumb(html: str, lang: str) -> str:
    name = cgv_data.META[lang]["breadcrumb"]
    base = "https://www.pd2i.com"
    if lang == "fr":
        url = f"{base}/fr/terms-of-sale.html"
    elif lang == "zh":
        url = f"{base}/zh/terms-of-sale.html"
    else:
        url = f"{base}/terms-of-sale.html"
    new, n = re.subn(
        r'"name": "[^"]+",\s*"item": "https://www\.pd2i\.com(/fr|/zh)?/legal\.html"',
        f'"name": "{name}",\n          "item": "{url}"',
        html,
        count=1,
    )
    return new if n else html


def patch_footer_bottom_root(html: str) -> str:
    old = """            bottomLinks: [
                { label: 'Cookies', href: 'cookies.html' },
                { label: 'Privacy policy', href: 'privacy.html' },
                { label: 'Legal Informations', href: 'legal.html' }
            ],"""
    new = """            bottomLinks: [
                { label: 'Cookies', href: 'cookies.html' },
                { label: 'Privacy policy', href: 'privacy.html' },
                { label: 'Legal Informations', href: 'legal.html' },
                { label: 'General Terms of Sale', href: 'terms-of-sale.html' }
            ],"""
    if old not in html:
        raise RuntimeError("root bottomLinks pattern not found")
    return html.replace(old, new, 1)


def patch_footer_bottom_fr(html: str) -> str:
    old = """            bottomLinks: [
                { label: 'Cookies', href: 'cookies.html' },
                { label: 'Politique de confidentialité', href: 'privacy.html' },
                { label: 'Mentions légales', href: 'legal.html' }
            ],"""
    new = """            bottomLinks: [
                { label: 'Cookies', href: 'cookies.html' },
                { label: 'Politique de confidentialité', href: 'privacy.html' },
                { label: 'Mentions légales', href: 'legal.html' },
                { label: 'Conditions générales de vente', href: 'terms-of-sale.html' }
            ],"""
    if old not in html:
        raise RuntimeError("FR bottomLinks pattern not found")
    return html.replace(old, new, 1)


def patch_console_log(html: str, lang: str) -> str:
    msg = cgv_data.META[lang]["console_msg"]
    new, n = re.subn(
        r"console\.log\('[^']*'\)",
        f"console.log('{msg}')",
        html,
        count=1,
    )
    return new if n else html


def build_root_en() -> None:
    src = (ROOT / "legal.html").read_text(encoding="utf-8")
    main = cgv_data.build_main_html("en")
    out = replace_main(src, main)
    out = patch_head_generic(out, "en")
    out = patch_breadcrumb(out, "en")
    out = patch_footer_bottom_root(out)
    out = patch_console_log(out, "en")
    (ROOT / "terms-of-sale.html").write_text(out, encoding="utf-8")
    print("Wrote terms-of-sale.html")


def build_fr() -> None:
    src = (ROOT / "fr" / "legal.html").read_text(encoding="utf-8")
    main = cgv_data.build_main_html("fr")
    out = replace_main(src, main)
    out = patch_head_generic(out, "fr")
    out = patch_breadcrumb(out, "fr")
    out = patch_footer_bottom_fr(out)
    out = patch_console_log(out, "fr")
    (ROOT / "fr" / "terms-of-sale.html").write_text(out, encoding="utf-8")
    print("Wrote fr/terms-of-sale.html")


def build_zh() -> None:
    src = (ROOT / "zh" / "legal.html").read_text(encoding="utf-8")
    main = cgv_data.build_main_html("zh")
    out = replace_main(src, main)
    out = patch_head_generic(out, "zh")
    out = patch_breadcrumb(out, "zh")
    out = patch_console_log(out, "zh")
    (ROOT / "zh" / "terms-of-sale.html").write_text(out, encoding="utf-8")
    print("Wrote zh/terms-of-sale.html")


if __name__ == "__main__":
    build_root_en()
    build_fr()
    build_zh()
