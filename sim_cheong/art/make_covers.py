"""Build the 심청전 covers in the same layout as the other covers.

No scan background here: the cover is a dark ink gradient with a red seal, so no
extra download is needed. Output: cover_en.jpg, cover_ko.jpg, cover_bilingual.jpg
next to this script.
"""
import os
import sys
from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))

W, H = 1600, 2560
CREAM = (245, 234, 214)
RED = (178, 34, 34)
INK_TOP = (31, 58, 95)
INK_BOTTOM = (14, 18, 30)
FONT_KO_BOLD = r"C:\Windows\Fonts\malgunbd.ttf"
FONT_KO = r"C:\Windows\Fonts\malgun.ttf"
FONT_EN_BOLD = r"C:\Windows\Fonts\georgiab.ttf"
FONT_EN = r"C:\Windows\Fonts\georgia.ttf"


def background():
    im = Image.new("RGB", (W, H), INK_TOP)
    draw = ImageDraw.Draw(im)
    for y in range(H):
        t = y / (H - 1)
        color = tuple(int(INK_TOP[i] + (INK_BOTTOM[i] - INK_TOP[i]) * t) for i in range(3))
        draw.line([(0, y), (W, y)], fill=color)
    return im


def font_for(text, size):
    """Use a Hangul-capable font whenever the line contains Hangul."""
    has_hangul = any("가" <= ch <= "힣" for ch in text)
    return ImageFont.truetype(FONT_KO if has_hangul else FONT_EN, size)


def text_center(draw, y, text, font, fill=CREAM):
    w = draw.textlength(text, font=font)
    draw.text(((W - w) / 2, y), text, font=font, fill=fill)
    _, _, _, bottom = draw.textbbox(((W - w) / 2, y), text, font=font)
    return bottom


def rule(draw, y):
    draw.line([(W * 0.32, y), (W * 0.68, y)], fill=CREAM, width=3)


def seal(im, label):
    draw = ImageDraw.Draw(im)
    x0, y0, x1, y1 = W - 400, 110, W - 130, 390
    draw.rounded_rectangle([x0, y0, x1, y1], radius=28, fill=RED)
    draw.rounded_rectangle([x0 + 22, y0 + 22, x1 - 22, y1 - 22], radius=18, outline=CREAM, width=4)
    f = ImageFont.truetype(FONT_KO_BOLD, 92)
    for i, line in enumerate(label.split("\n")):
        w = draw.textlength(line, font=f)
        draw.text((x0 + (x1 - x0 - w) / 2, y0 + 45 + i * 100), line, font=f, fill=CREAM)


def make(name, title, subtitle_lines, note_lines, title_font, publisher="TKPROF LLC"):
    im = background()
    seal(im, "沈\n淸")
    draw = ImageDraw.Draw(im)
    y = 1270
    for t in title:
        y = text_center(draw, y, t, title_font) + 10
    y += 30
    rule(draw, y)
    y += 60
    for line in subtitle_lines:
        y = text_center(draw, y, line, font_for(line, 64)) + 26
    y += 40
    for line in note_lines:
        y = text_center(draw, y, line, font_for(line, 50)) + 18
    text_center(draw, H - 230, publisher, ImageFont.truetype(FONT_EN, 46))
    path = os.path.join(HERE, name)
    im.save(path, quality=92)
    print("wrote", path)


make(
    "cover_en.jpg",
    ["THE STORY OF", "SHIM CHEONG"],
    ["A Daughter’s Love and a Sea Voyage,", "Retold in Simple English"],
    ["Based on the 1917 Wanpan text (public domain)"],
    title_font=ImageFont.truetype(FONT_EN_BOLD, 150),
)
make(
    "cover_ko.jpg",
    ["심청전"],
    ["효녀 심청 이야기", "완판 71장본 현대어 옮김"],
    ["13세 이상 독자를 위한 현대어 재화"],
    title_font=ImageFont.truetype(FONT_KO_BOLD, 230),
)
make(
    "cover_bilingual.jpg",
    ["SHIM CHEONG"],
    ["심청전 · The Story of Shim Cheong", "한국어 · English 대역"],
    ["완판 71장본 기준 · Based on the Wanpan 71-leaf text"],
    title_font=ImageFont.truetype(FONT_EN_BOLD, 150),
)
