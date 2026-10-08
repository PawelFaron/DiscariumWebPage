#!/usr/bin/env python3
"""Generate the GitHub Pages site. Python 3 standard library only."""
from html import escape
from pathlib import Path
from urllib.parse import quote
import json

ROOT = Path(__file__).resolve().parents[1]
PAGES = {
    "index": ("Discarium — Your collection. A private performance.", "Lossless audio, original-quality video and compatible Blu-ray and DVD menus. Your own music and film collection, on Apple TV.", "home"),
    "compatibility": ("Formats & compatibility — Discarium", "Audio, video and disc formats supported by Discarium on Apple TV, including lossless surround sound, HDR10 and original disc menus.", "document"),
    "support": ("Support — Discarium", "Set up your collection, connect your receiver and get help with Discarium for Apple TV. Contact the developer directly.", "document"),
    "updates": ("Updates — Discarium", "What's new in Discarium for Apple TV. Disc playback, surround sound, subtitles and video improvements, with version-by-version notes.", "document"),
    "privacy": ("Privacy policy — Discarium", "How Discarium handles your library, network connections, playback history and support requests. Privacy choices and data deletion.", "document"),
    "404": ("Page not found — Discarium", "Find Discarium support, privacy information and supported formats.", "document"),
}


def main():
    config = json.loads((ROOT / "src/config.json").read_text())
    base = config["base_url"]
    assert base.startswith("https://") and base.endswith("/"), "Use an HTTPS URL ending in /"
    template = (ROOT / "src/template.html").read_text()
    mail = config["support_email"]
    # A public contact is required before deployment; verify.py enforces it.
    contact = (f'<a class="contact-email" href="mailto:{quote(mail, safe="@.+")}">{escape(mail)}</a>'
               if mail else '<p class="contact-pending">Public support contact is being configured.</p>')
    for slug, (title, description, style) in PAGES.items():
        values = {
            **{key: escape(str(value), quote=True) for key, value in config.items()},
            "title": escape(title), "description": escape(description, quote=True),
            "canonical": base + ("" if slug == "index" else slug + ".html"),
            "page_class": style, "contact": contact,
            "home_current": ' aria-current="page"' if slug == "index" else "",
            "support_current": ' aria-current="page"' if slug == "support" else "",
            "compatibility_current": ' aria-current="page"' if slug == "compatibility" else "",
        }
        content = (ROOT / f"src/pages/{slug}.html").read_text()
        for key, value in values.items():
            content = content.replace("{{" + key + "}}", value)
        page = template.replace("{{content}}", content)
        for key, value in values.items():
            page = page.replace("{{" + key + "}}", value)
        assert "{{" not in page, f"Unresolved token in {slug}"
        # GitHub Pages serves 404.html at any depth, so its relative links need a base.
        if slug == "404":
            page = page.replace('<meta charset="utf-8">', '<meta charset="utf-8">\n  <base href="' + escape(base) + '">\n  <meta name="robots" content="noindex">')
        (ROOT / f"site/{slug}.html").write_text(page)
    urls = [base + ("" if slug == "index" else slug + ".html") for slug in PAGES if slug != "404"]
    (ROOT / "site/sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'  <url><loc>{escape(url)}</loc></url>\n' for url in urls) + '</urlset>\n')
    (ROOT / "site/.nojekyll").touch()
    print(f"Built {len(PAGES)} pages for {base}")


if __name__ == "__main__":
    main()
