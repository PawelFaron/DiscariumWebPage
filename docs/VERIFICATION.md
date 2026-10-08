# Verification

## Copy cleanup — 8 October 2026

- Removed public review/approval statuses and "Coming in" labels from Updates, the homepage, formats and page metadata.
- Removed the Open source page, its footer link and sitemap entry; adjusted the generator and verifier to the six remaining pages.
- Kept version-specific feature notes and the verified App Store link.
- Regenerated the site and verified local links, anchors, contact details, metadata and JavaScript syntax.

## Release information update — 8 October 2026

- Confirmed the public App Store product URL returns HTTP 200. Apple's public lookup API for Poland identifies **Discarium: Lossless Player**, version **1.0**, released 8 October 2026.
- Added App Store links, a release summary on the homepage and `updates.html`. Version **1.1 (28)** is explicitly awaiting App Review; it is not presented as already released.
- Updated support and format information for disc chapters, shared video buffering, PGS subtitle seeking, multichannel PCM and the **Mixed to 5.1** indicator. Help identifies features introduced in 1.1 and retains the old disc-opening label for 1.0 users.
- Generated all **seven pages**. `python3 scripts/verify.py`, `node --check site/assets/site.js` and `git diff --check` passed. Checked links, anchors, page metadata, image attributes, public contacts and sitemap.
- Reviewed home, updates, support, formats and source in Chromium at **1440, 768, 390 and 320 px**. Desktop and mobile screenshots were inspected for the homepage and updates. No missing loaded images or duplicate main headings were found.
- Mobile emulation found an existing 2 px overflow from the homepage's decorative glow. Constrained that glow on small screens and confirmed both 320 px and 390 px layouts have equal document/client widths. Other checked pages had no horizontal overflow.
- Opened the new 5.1 mixing, disc chapter and Blu-ray subtitle FAQs and checked their displayed content. No browser console errors or warnings were reported during this interaction check.
- The privacy policy's effective date and content remain unchanged. The shared footer now links to Updates. Push and deployment remain the owner's next steps; no production deployment was performed for this update.

## Initial site — 6 October 2026

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
