"""Build the 홍길동전 covers in the same layout as the 춘향전 covers.

Background: the cover page of the 1917 Jeonju printing (WDL 4166, public domain),
rendered from the PDF in the scratch folder. Output: cover_en.jpg, cover_ko.jpg,
cover_bilingual.jpg next to this script.
"""
import os
import sys
from PIL import Image, ImageDraw, ImageFilter, ImageFont

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
BG = r"C:\Users\hongw\AppData\Local\Temp\claude\ead8ac6bdee9208a\25da40cf-9400-4ecc-96dc-5a85ea1f04d5\scratchpad\wdl4166\pages\p-01.png"

W, H = 1600, 2560
CREAM = (245, 234, 214)
RED = (178, 34, 34)
FONT_KO_BOLD = r"C:\Windows\Fonts\malgunbd.ttf"
FONT_KO = r"C:\Windows\Fonts\malgun.ttf"
FONT_EN_BOLD = r"C:\Windows\Fonts\georgiab.ttf"
FONT_EN = r"C:\Windows\Fonts\georgia.ttf"


def background():
    im = Image.open(BG).convert("RGB")
    # cover page is portrait; fill the canvas width and crop to height
    # fill the full height, then crop the width to the centre
    scale = H / im.height
    im = im.resize((int(im.width * scale), H), Image.LANCZOS)
    left = (im.width - W) // 2
    im = im.crop((left, 0, left + W, H))
    # dark gradient over the lower part, as on the 춘향전 covers
    grad = Image.new("L", (1, H))
    for y in range(H):
        t = max(0.0, min(1.0, (y - H * 0.42) / (H * 0.40)))
        grad.putpixel((0, y), int(255 * t))
    mask = grad.resize((W, H))
    dark = Image.new("RGB", (W, H), (22, 24, 34))
    im = Image.composite(dark, im, mask)
    return im


def font_for(text, _size):
    """Use a Hangul-capable font whenever the line contains Hangul."""
    has_hangul = any("가" <= ch <= "힣" for ch in text)
    return FONT_KO if has_hangul else FONT_EN


def text_center(draw, y, text, font, fill=CREAM):
    w = draw.textlength(text, font=font)
    draw.text(((W - w) / 2, y), text, font=font, fill=fill)
    left, top, right, bottom = draw.textbbox(((W - w) / 2, y), text, font=font)
    return bottom


def rule(draw, y):
    draw.line([(W * 0.32, y), (W * 0.68, y)], fill=CREAM, width=3)


def seal(im, label):
    draw = ImageDraw.Draw(im)
    x0, y0, x1, y1 = W - 400, 110, W - 130, 390
    draw.rounded_rectangle([x0, y0, x1, y1], radius=28, fill=RED)
    draw.rounded_rectangle([x0 + 22, y0 + 22, x1 - 22, y1 - 22], radius=18, outline=CREAM, width=4)
    f = ImageFont.truetype(FONT_KO_BOLD, 92)
    lines = label.split("\n")
    for i, line in enumerate(lines):
        w = draw.textlength(line, font=f)
        draw.text((x0 + (x1 - x0 - w) / 2, y0 + 45 + i * 100), line, font=f, fill=CREAM)


def make(name, title, subtitle_lines, note_lines, publisher="TKPROF LLC", title_font=None):
    im = background()
    seal(im, "洪\n童")
    draw = ImageDraw.Draw(im)
    y = 1270
    y = text_center(draw, y, title[0], title_font or ImageFont.truetype(FONT_EN_BOLD, 180))
    if len(title) > 1:
        y = text_center(draw, y + 10, title[1], ImageFont.truetype(FONT_EN, 120))
    y += 40
    rule(draw, y)
    y += 60
    for line in subtitle_lines:
        f = ImageFont.truetype(font_for(line, 64), 64)
        y = text_center(draw, y, line, f) + 26
    y += 40
    for line in note_lines:
        f = ImageFont.truetype(font_for(line, 50), 50)
        y = text_center(draw, y, line, f) + 18
    f = ImageFont.truetype(FONT_EN, 46)
    text_center(draw, H - 230, publisher, f)
    path = os.path.join(HERE, name)
    im.save(path, quality=92)
    print("wrote", path)


make(
    "cover_en.jpg",
    ["THE STORY OF", "HONG GILDONG"],
    ["Korea's Classic Tale of a Hero Outlaw,", "Retold in Simple English"],
    ["From the 1917 Jeonju woodblock edition"],
)
make(
    "cover_ko.jpg",
    ["홍길동전"],
    ["의적 홍길동 이야기", "완판 36장본 현대어 옮김"],
    ["13세 이상 독자를 위한 현대어 재화"],
    title_font=ImageFont.truetype(FONT_KO_BOLD, 230),
)
make(
    "cover_bilingual.jpg",
    ["HONG GILDONG"],
    ["홍길동전 · The Story of Hong Gildong", "한국어 · English 대역"],
    ["완판 36장본 기준 · Based on the 36-leaf Wanpan text"],
    title_font=ImageFont.truetype(FONT_EN_BOLD, 150),
)
