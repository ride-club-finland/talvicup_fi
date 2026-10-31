"""Render the site's images and web fonts from the TalviCup identity kit.

Run from the workspace root: py -3.11 talvicup_fi/tyokalut/tee_kuvat.py
Needs the sibling repos rcf_mediatehdas (K24 kit) and rideclubfinland_materiaalipankki (fonts).
"""
import sys
from pathlib import Path

from fontTools import subset
from PIL import Image

SITE = Path(__file__).resolve().parents[1] / "docs" / "assets"
WORKSPACE = SITE.parents[2]
sys.path.insert(0, str(WORKSPACE / "rcf_mediatehdas" / "kokeet" / "K24_talvicup_ilme"))
import ilme  # noqa: E402
import recraft_vedos as rv  # noqa: E402

FONT_SRC = WORKSPACE / "rideclubfinland_materiaalipankki" / "brandi" / "fontit" / "saira_condensed"
LATIN = "U+0020-007E,U+00A0-00FF,U+2013,U+2014,U+2019,U+2026,U+2192,U+00B7"


def fonts():
    for weight in ("Black", "Bold", "SemiBold", "Medium", "Regular"):
        out = SITE / "fontit" / f"SairaCondensed-{weight}.woff"
        subset.main([str(FONT_SRC / f"SairaCondensed-{weight}.ttf"), f"--unicodes={LATIN}", "--flavor=woff",
                     "--layout-features=*", f"--output-file={out}"])


def images():
    # Cabin small and far right so the headline stays on open sky at laptop widths.
    rv.ilta((2000, 1125), .76, .76, .36, 130).save(SITE / "hero.webp", quality=80, method=6)
    rv.ilta((1080, 1500), .84, .5, .66, 90).save(SITE / "hero_pysty.webp", quality=78, method=6)
    ilme.wordmark_img(1000).save(SITE / "sanamerkki.webp", quality=92, method=6)
    full = rv.flake_from_arm()
    full.resize((640, 640), Image.LANCZOS).save(SITE / "hiutale.webp", quality=90, method=6)
    for r in ilme.RACES:
        rv.flake_from_arm((r["n"],)).resize((240, 240), Image.LANCZOS).save(SITE / f"hiutale_{r['n']}.webp", quality=88, method=6)

    share = rv.ilta((1200, 630), .78, .74, .4, 90).convert("RGBA")
    mark = ilme.wordmark_img(560)
    share.alpha_composite(mark, (64, 96))
    share.convert("RGB").save(SITE / "jako.jpg", quality=84, optimize=True)

    tile = Image.new("RGBA", (180, 180), ilme.POLAR + (255,))
    tile.alpha_composite(full.resize((156, 156), Image.LANCZOS), (12, 12))
    tile.convert("RGB").save(SITE / "apple-touch-icon.png", optimize=True)
    tile.resize((48, 48), Image.LANCZOS).convert("RGB").save(SITE / "favicon.png", optimize=True)


if __name__ == "__main__":
    fonts()
    images()
