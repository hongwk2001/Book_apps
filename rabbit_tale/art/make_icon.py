"""Draw the 토끼전 launcher icon: a red seal with 토 (rabbit) on the ink-blue background.

Writes adaptive-icon foregrounds (ic_launcher_foreground.png, 108dp canvas) and
legacy icons (ic_launcher.png / ic_launcher_round.png, 48dp) into the module's
res folders. Run once; the outputs are committed resources.
"""
import os
import sys
from PIL import Image, ImageDraw, ImageFont, ImageChops

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(HERE, "..", "src", "main", "res")

INK = (31, 58, 95)        # colors.xml: rabbit_ink
RED = (178, 34, 34)       # same seal red as the 춘향전 cover
CREAM = (245, 234, 214)
FONT = r"C:\Windows\Fonts\malgunbd.ttf"   # Hangul, one syllable for the seal

DENSITIES = {"mdpi": 1, "hdpi": 1.5, "xhdpi": 2, "xxhdpi": 3, "xxxhdpi": 4}


def seal(size_px, canvas_px, transparent):
    """Seal centred on a square canvas. Seal is ~62% of the canvas (safe zone)."""
    base = (0, 0, 0, 0) if transparent else INK + (255,)
    im = Image.new("RGBA", (canvas_px, canvas_px), base)
    d = ImageDraw.Draw(im)
    s = size_px
    x0 = (canvas_px - s) // 2
    y0 = (canvas_px - s) // 2
    x1, y1 = x0 + s, y0 + s
    r = int(s * 0.16)
    d.rounded_rectangle([x0, y0, x1, y1], radius=r, fill=RED + (255,))
    inset = int(s * 0.07)
    d.rounded_rectangle([x0 + inset, y0 + inset, x1 - inset, y1 - inset],
                        radius=max(2, r - inset // 2), outline=CREAM + (255,),
                        width=max(2, int(s * 0.025)))
    # one Hangul syllable, centred: readable at launcher size
    f = ImageFont.truetype(FONT, int(s * 0.56))
    w = d.textlength("토", font=f)
    _, top, _, bottom = d.textbbox((0, 0), "토", font=f)
    d.text((x0 + (s - w) / 2, y0 + (s - (bottom - top)) / 2 - top), "토", font=f, fill=CREAM + (255,))
    return im


def round_mask(im):
    size = im.size[0]
    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).ellipse([0, 0, size - 1, size - 1], fill=255)
    out = im.copy()
    out.putalpha(ImageChops.multiply(im.getchannel("A"), mask))
    return out


def main():
    for name, scale in DENSITIES.items():
        folder = os.path.join(RES, f"mipmap-{name}")
        os.makedirs(folder, exist_ok=True)
        # adaptive foreground: 108dp canvas, seal ~66dp (inside the 72dp safe zone)
        fg_px = int(round(108 * scale))
        seal_px = int(round(66 * scale))
        fg = seal(seal_px, fg_px, transparent=True)
        fg.save(os.path.join(folder, "ic_launcher_foreground.png"))
        # legacy (pre-API 26): full icon at 48dp
        leg_px = int(round(48 * scale))
        full = seal(int(round(34 * scale)), leg_px, transparent=False)
        full.convert("RGB").save(os.path.join(folder, "ic_launcher.png"))
        round_mask(full).save(os.path.join(folder, "ic_launcher_round.png"))
        print("wrote", name, fg_px, leg_px)


if __name__ == "__main__":
    main()
