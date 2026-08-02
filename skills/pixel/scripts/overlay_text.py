#!/usr/bin/env python3
"""Pose le texte d'un slide carrousel sur une image générée, avec la vraie police
(TTF/OTF) et les vraies couleurs hex du site. L'original est préservé.

Usage:
    python3 overlay_text.py <image.png> --title "Extraction lente 80 tr/min" \
        [--subtitle "Une phrase max"] [--bullets "ligne 1;ligne 2;ligne 3"] \
        --font Brand-Bold.ttf [--font-sub Brand-Regular.ttf] \
        [--color "#1F3D2B"] [--zone top|bottom] [--panel "#FFFFFF"] \
        [--margin-pct 7] [--out sortie.png]

Sans --out, écrit <image>-txt.png à côté de l'original.
--panel dessine un bandeau semi-opaque derrière le texte (contraste garanti).
Nécessite Pillow (pip install pillow).
"""
import argparse
import os
import sys

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    sys.exit("Pillow manquant : pip install pillow (ou venv)")


def load_font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except OSError as e:
        sys.exit(f"Police illisible ({path}): {e} — il faut un TTF/OTF, pas un woff2.")


def wrap(draw, text, font, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=font) <= max_w or not cur:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("image")
    ap.add_argument("--title", required=True)
    ap.add_argument("--subtitle", default=None)
    ap.add_argument("--bullets", default=None, help="lignes séparées par ;")
    ap.add_argument("--font", required=True, help="TTF/OTF du titre (graisse bold du site)")
    ap.add_argument("--font-sub", default=None, help="TTF/OTF du sous-texte (défaut: --font)")
    ap.add_argument("--color", default="#111111", help="hex du texte (couleur du site)")
    ap.add_argument("--zone", choices=["top", "bottom"], default="top")
    ap.add_argument("--panel", default=None, help="hex d'un bandeau semi-opaque derrière le texte")
    ap.add_argument("--panel-alpha", type=int, default=217, help="opacité du bandeau 0-255")
    ap.add_argument("--margin-pct", type=float, default=7.0)
    ap.add_argument("--out", default=None)
    a = ap.parse_args()

    img = Image.open(a.image).convert("RGBA")
    W, H = img.size
    margin = int(W * a.margin_pct / 100)
    max_w = W - 2 * margin

    # Tailles relatives à la largeur : lisible en miniature sans écraser la photo.
    title_font = load_font(a.font, max(28, W // 14))
    sub_path = a.font_sub or a.font
    sub_font = load_font(sub_path, max(20, W // 24))
    bullet_font = load_font(sub_path, max(20, W // 26))

    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)

    # Composer les lignes (titre wrappé, sous-titre wrappé, bullets une par ligne).
    blocks = []
    for line in wrap(draw, a.title, title_font, max_w):
        blocks.append((line, title_font, 1.12))
    if a.subtitle:
        blocks.append(("", sub_font, 0.45))
        for line in wrap(draw, a.subtitle, sub_font, max_w):
            blocks.append((line, sub_font, 1.25))
    if a.bullets:
        blocks.append(("", bullet_font, 0.55))
        for b in a.bullets.split(";"):
            b = b.strip()
            if b:
                for j, line in enumerate(wrap(draw, "•  " + b, bullet_font, max_w)):
                    blocks.append((line if j == 0 else "    " + line.lstrip("•  "), bullet_font, 1.35))

    total_h = sum(f.size * lh for _, f, lh in blocks)
    y = margin if a.zone == "top" else H - margin - total_h
    pad = int(margin * 0.6)

    if a.panel:
        pr, pg, pb = tuple(int(a.panel.lstrip("#")[i:i + 2], 16) for i in (0, 2, 4))
        draw.rounded_rectangle(
            [margin - pad, y - pad, W - margin + pad, y + total_h + pad],
            radius=pad // 2, fill=(pr, pg, pb, a.panel_alpha))

    for text, font, lh in blocks:
        if text:
            draw.text((margin, y), text, font=font, fill=a.color)
        y += int(font.size * lh)

    out = a.out or os.path.splitext(a.image)[0] + "-txt.png"
    Image.alpha_composite(img, layer).convert("RGB").save(out, quality=95)
    print(out)


if __name__ == "__main__":
    main()
