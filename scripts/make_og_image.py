"""Draw the link-preview (Open Graph) image for fatihbozdag.com.

Usage:
    uv run --no-project --with pillow python scripts/make_og_image.py \
        --serif SourceSerif4.ttf --sans SourceSans3.ttf

The fonts are the site's own typefaces (Source Serif 4 and Source Sans 3,
SIL Open Font License, from github.com/google/fonts). They are not stored in
this repository; pass the paths to the variable-font files.
Writes images/og-image.png (1200 x 630, the size social platforms expect).
"""
import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 1200, 630
BACKGROUND = "#f7f9fc"
ACCENT = "#1f3a5f"      # $primary in styles.scss
BODY = "#1d1d1f"        # $body-color in styles.scss
MUTED = "#5b6270"       # $site-muted in styles.scss
MARGIN = 96

NAME = "Fatih Ünal Bozdağ"
ROLE_LINES = ["Assistant Professor of English Translation and Interpretation",
              "Osmaniye Korkut Ata University"]
FOCUS = "Learner corpora · Usage-based grammar · Cognitive Grammar · Bayesian modelling"
URL = "fatihbozdag.com"


def variable_font(path, size, weight):
    """Load a variable font and set its weight (and optical size, if present) by axis name."""
    font = ImageFont.truetype(str(path), size)
    values = []
    for axis in font.get_variation_axes():
        name = axis["name"].decode() if isinstance(axis["name"], bytes) else axis["name"]
        wanted = {"Weight": weight, "Optical size": size, "Optical Size": size}.get(name, axis["default"])
        values.append(min(max(wanted, axis["minimum"]), axis["maximum"]))
    font.set_variation_by_axes(values)
    return font


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--serif", required=True, type=Path)
    parser.add_argument("--sans", required=True, type=Path)
    parser.add_argument("--out", default=Path(__file__).resolve().parent.parent / "images" / "og-image.png", type=Path)
    args = parser.parse_args()

    name_font = variable_font(args.serif, 76, 600)
    role_font = variable_font(args.sans, 34, 400)
    focus_font = variable_font(args.sans, 28, 400)
    url_font = variable_font(args.sans, 28, 600)

    image = Image.new("RGB", (WIDTH, HEIGHT), BACKGROUND)
    draw = ImageDraw.Draw(image)
    draw.rectangle([0, 0, 16, HEIGHT], fill=ACCENT)

    y = 150
    draw.text((MARGIN, y), NAME, font=name_font, fill=ACCENT)
    y += 120
    for line in ROLE_LINES:
        draw.text((MARGIN, y), line, font=role_font, fill=BODY)
        y += 48
    y += 22
    draw.text((MARGIN, y), FOCUS, font=focus_font, fill=MUTED)
    draw.line([MARGIN, HEIGHT - 120, WIDTH - MARGIN, HEIGHT - 120], fill="#e5e5e3", width=2)
    draw.text((MARGIN, HEIGHT - 96), URL, font=url_font, fill=ACCENT)

    widest = max(draw.textlength(t, font=f) for t, f in
                 [(NAME, name_font), (FOCUS, focus_font)] + [(r, role_font) for r in ROLE_LINES])
    assert MARGIN + widest <= WIDTH - MARGIN, f"text too wide: {widest:.0f}px"
    args.out.parent.mkdir(parents=True, exist_ok=True)
    image.save(args.out, optimize=True)
    print(f"wrote {args.out} ({WIDTH}x{HEIGHT}), widest line {widest:.0f}px")


if __name__ == "__main__":
    main()
