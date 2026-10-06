# Verification — 6 October 2026

- Generated all six pages with Python 3 and ran `scripts/verify.py`: passed. Checked local links, fragment targets, image dimensions/alt attributes, titles/descriptions, public contact and sitemap.
- `node --check site/assets/site.js`: passed.
- Served the site locally under `/DiscariumWebPage/`, matching the future GitHub Pages project prefix.
- In Chromium, visited home, support, privacy, formats and source at **1440, 768, 390 and 320 px** viewport widths. All 20 page/layout combinations had one main heading and no horizontal page overflow.
- Clicked gallery choices, changed one with **keyboard Enter**, and checked selected state and loaded image. Opened a support FAQ. No script errors or failed HTTP responses during these checks.
- Inspected screenshots of the desktop and phone landing page, mobile format table, support/contact page and gallery. Screenshot evidence is local in ignored `build/`; original app screenshots in `site/assets/` are committed.
- Tested navigation, support contact, privacy content and FAQ with **JavaScript disabled**; essential content remains accessible. Gallery enhancement is optional.
- Reduced-motion preference is supported in CSS. There is no timed motion or auto-advancing carousel.

These are local Chromium checks, not a test of the deployed GitHub site or a physical phone. After deploying, check the actual HTTPS pages in a signed-out/private browser window and confirm the public mailbox receives messages.
