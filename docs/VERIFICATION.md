# Verification — 6 October 2026

- Generated all six pages with Python 3 and ran `scripts/verify.py`: passed. Checked local links, fragment targets, image dimensions/alt attributes, titles/descriptions, public contact and sitemap.
- `node --check site/assets/site.js`: passed.
- Served the site locally under `/DiscariumWebPage/`, matching the future GitHub Pages project prefix.
- In Chromium, visited home, support, privacy, formats and source at **1440, 768, 390 and 320 px** viewport widths. All 20 page/layout combinations had one main heading and no horizontal page overflow.
- Clicked gallery choices, changed one with **keyboard Enter**, and checked selected state and loaded image. Opened a support FAQ. No script errors or failed HTTP responses during these checks.
- Inspected screenshots of the desktop and phone landing page, mobile format table, support/contact page and gallery. Screenshot evidence is local in ignored `build/`; original app screenshots in `site/assets/` are committed.
- Tested navigation, support contact, privacy content and FAQ with **JavaScript disabled**; essential content remains accessible. Gallery enhancement is optional.
- Reduced-motion preference is supported in CSS. There is no timed motion or auto-advancing carousel.

These layout checks use Chromium viewport emulation, not a physical phone. Confirm separately that the public mailbox receives messages.

## Production deployment

On 6 October 2026, GitHub Pages was serving a Jekyll rendering of the repository README because its source was `main / (root)`. Changed Pages `build_type` from `legacy` to `workflow`, then deployed the already-pushed commit `bc92bc0` using **Deploy GitHub Pages**. No Git push was performed.

[Deployment run 37484389227](https://github.com/PawelFaron/DiscariumWebPage/actions/runs/37484389227) completed successfully. A fresh, signed-out browser context loaded the public homepage, support, privacy, compatibility and source pages: all returned HTTP 200 and their expected product headings. Images and the interactive gallery loaded; no JavaScript errors were reported. Inspected the deployed homepage screenshot in `build/deployed-fixed.png`.
