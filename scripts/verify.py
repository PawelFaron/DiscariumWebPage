#!/usr/bin/env python3
"""Check public pages, contact details and every local link before deployment."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse
import json
import re

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"


class Document(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path = path
        self.ids = set()
        self.links = []
        self.h1 = 0
        self.title = 0
        self.lang = None
        self.description = False
        self.feed(path.read_text())

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get("id"):
            assert a["id"] not in self.ids, f"Duplicate ID in {self.path}: {a['id']}"
            self.ids.add(a["id"])
        if tag == "html": self.lang = a.get("lang")
        if tag == "h1": self.h1 += 1
        if tag == "title": self.title += 1
        if tag == "meta" and a.get("name") == "description": self.description = bool(a.get("content"))
        if tag == "img":
            assert "alt" in a, f"Image without alt in {self.path}"
            assert "width" in a and "height" in a, f"Image dimensions missing in {self.path}"
        for key in ("href", "src", "data-gallery-image"):
            if a.get(key): self.links.append(a[key])


def main():
    config = json.loads((ROOT / "src/config.json").read_text())
    email = config["support_email"]
    assert re.fullmatch(r"[^\s@]+@[^\s@]+\.[^\s@]+", email), "Set a real public support email before deployment"
    docs = {p.resolve(): Document(p) for p in SITE.glob("*.html")}
    assert len(docs) >= 5, "Missing public pages"
    for path, doc in docs.items():
        assert doc.h1 == 1 and doc.title == 1 and doc.lang == "en" and doc.description, f"Missing page metadata: {path}"
        raw = path.read_text()
        assert "{{" not in raw and "contact-pending" not in raw, f"Draft content: {path}"
        for link in doc.links:
            url = urlparse(link)
            if url.scheme:
                assert url.scheme in {"https", "mailto"}, f"Unexpected URL scheme: {link}"
                continue
            assert not url.netloc and not url.path.startswith("/"), f"Use project-relative links: {link}"
            target = (path.parent / unquote(url.path)).resolve() if url.path else path
            if target.is_dir(): target /= "index.html"
            assert target.is_relative_to(SITE), f"Link outside site: {link}"
            assert target.is_file(), f"Broken link in {path.name}: {link}"
            if url.fragment and target in docs:
                assert unquote(url.fragment) in docs[target].ids, f"Broken anchor in {path.name}: {link}"
    for page in ("support", "privacy"):
        assert f"mailto:{email}" in (SITE / f"{page}.html").read_text(), f"Missing public contact in {page}"
    for asset in ("social.jpg", "mark.svg", "site.css", "site.js"):
        assert (SITE / "assets" / asset).is_file(), f"Missing asset: {asset}"
    assert (SITE / ".nojekyll").exists() and (SITE / "sitemap.xml").is_file()
    forbidden = ("google-analytics", "googletagmanager", "facebook.net", "fonts.googleapis", "localStorage", "document.cookie")
    for path in SITE.rglob("*"):
        if path.suffix in {".html", ".css", ".js"}:
            assert not any(item in path.read_text() for item in forbidden), f"Unexpected tracker/storage in {path}"
    print(f"PASS: {len(docs)} pages; local links, anchors, image dimensions, metadata and public contacts verified.")


if __name__ == "__main__":
    main()
