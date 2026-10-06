#!/usr/bin/env python3
"""Regenerate the committed link preview. Optional authoring dependency: Pillow."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "site/assets"


def font(size, italic=False):
    paths = (
        ["/System/Library/Fonts/Supplemental/Georgia Italic.ttf",
         "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Italic.ttf"] if italic else
        ["/System/Library/Fonts/Supplemental/Arial.ttf",
         "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]
    )
    return ImageFont.truetype(next(path for path in paths if Path(path).is_file()), size)


def main():
    image = Image.new("RGB", (1200, 630), "#101111")
    draw = ImageDraw.Draw(image)
    draw.text((70, 50), "Discarium", font=font(29), fill="#f1eee6")
    draw.text((70, 135), "Your collection.", font=font(64), fill="#f1eee6")
    draw.text((70, 213), "A private", font=font(64), fill="#f1eee6")
    draw.text((70, 284), "performance.", font=font(66, italic=True), fill="#e1b574")
    draw.text((73, 431), "LOSSLESS. SURROUND. YOURS.", font=font(16), fill="#e1b574")
    draw.text((73, 482), "Discs, music and video. Made for Apple TV.", font=font(23), fill="#b3b5ae")
    draw.line((70, 566, 1130, 566), fill="#343830", width=1)
    draw.text((73, 585), "DISCARIUM · LOSSLESS PLAYER", font=font(12), fill="#b3b5ae")
    with Image.open(ASSETS / "audio.webp") as screen:
        screen.thumbnail((482, 272))
        image.paste(screen, (663, 193))
    draw.rectangle((658, 188, 1149, 469), outline="#464a42", width=3)
    image.save(ASSETS / "social.jpg", quality=94)


if __name__ == "__main__":
    main()
