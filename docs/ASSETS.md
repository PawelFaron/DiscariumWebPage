# Assets

- `site/assets/mark.svg` is the approved Discarium three-ring logo, copied from the application's `branding/mark.svg`. Its amber dot and silver rings are unchanged.
- `audio.webp`, `album.webp`, `player.webp`, `details.webp` come from the real Apple TV screenshots of Discarium 1.0 used for build 22's store materials. They show the original bundled demo library. Web versions are resized to 1920×1080 and compressed for page loading; these are marketing images, not media playback output.
- `social.jpg` is an original 1200×630 link-preview composition using the Audio collection screenshot and brand palette. Regenerate it with `python3 scripts/generate_social.py` (Pillow required for this optional authoring step). It uses the selected headline: “Your collection. A private performance.”
- The disc illustration and television frame are CSS, not stock photos or borrowed hardware images. They are decorative, not screenshots of a disc menu.
- All page images and fonts are served locally or use installed system fonts. No external CDN, image tracking, web-font request or embedded video service.

Screenshots and the Discarium name/mark belong to this project. No rights to third-party films, albums or trademarks are implied. Apple TV is a trademark of Apple Inc.; no endorsement is claimed.
