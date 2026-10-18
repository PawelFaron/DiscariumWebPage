# Verification

## App Store 1.3 website refresh — 19 October 2026

- Apple's public lookup API confirms **Discarium: Lossless Player 1.3**, released **14 October 2026**, in Poland and the United States. The public app link is `https://apps.apple.com/app/id6819356965`. Recorded the response fields in `docs/app-store-release.json`.
- The live homepage still said “Currently in TestFlight” because GitHub Pages served the 6 October deployment (`bc92bc0`). Later pushes ran **Check website** only. The deployment workflow is manual; successful checks do not publish a new site.
- Updated the homepage, formats, support and release history for compatible BD-J menus, CUE albums, NFS/FTP/FTPES/FTPS/SFTP/WebDAV, embedded disc covers, chapter navigation, subtitle synchronization, collections and resumable downloads. Added an App Store link to every public page.
- MilkDrop, the new speaker meters, the simplified animation gallery and queue/navigation improvements are explicitly a **development preview**, separate from the released 1.3 features. No Apple review status is used as marketing copy.
- Updated privacy facts for additional connections, accepted SFTP server identities and user-requested rename/delete actions. The policy date changes because its contents changed, not because the app version changed.
- `python3 scripts/build.py`, `python3 scripts/verify.py`, `node --check site/assets/site.js` and `git diff --check` passed. The verifier now requires App Store links, rejects the obsolete status text, and rejects a regenerated source-code page.
- Chromium: all six pages at **1440, 390 and 320 px** passed (18 layout checks): HTTP 200, one main heading, no horizontal overflow, no obsolete status, and working App Store links. Gallery click and keyboard selection worked; the CUE support FAQ opened. No JavaScript errors were observed.
- Inspected screenshots of the desktop and phone homepage, mobile format table and the new development-preview section. Local evidence is in ignored `build/site-refresh/`.
- With JavaScript disabled, the homepage, support and privacy pages remained readable at 390 px, App Store links were present, and the support FAQ still opened.
- The owner explicitly authorized push and publication after these checks. Publish this commit with **Deploy GitHub Pages**, then verify the public pages; a local build or successful push alone does not establish deployment success.

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
