"""Render the site's images and web fonts from the TalviCup identity kit.

Run from the workspace root with the Mediatehdas environment (the kit needs its packages):
    uv run --project rcf_mediatehdas python talvicup_fi/tyokalut/tee_kuvat.py [kuvat|fontit]
Needs the sibling repos rcf_mediatehdas (generaattorit/talvicup_kit.py) and rideclubfinland_materiaalipankki (fonts).
The identity is the road to the star (C) and the cropped flake (D), decided 1.11.2026 (rcf_talvicup/docs/ilme.md).
"""
import sys
from pathlib import Path

from PIL import Image

SITE = Path(__file__).resolve().parents[1] / "docs" / "assets"
WORKSPACE = SITE.parents[2]
sys.path.insert(0, str(WORKSPACE / "rcf_mediatehdas" / "generaattorit"))
import talvicup_kit as tk  # noqa: E402

FONT_SRC = WORKSPACE / "rideclubfinland_materiaalipankki" / "brandi" / "fontit" / "saira_condensed"
LATIN = "U+0020-007E,U+00A0-00FF,U+2013,U+2014,U+2019,U+2026,U+2192,U+00B7"


def fonts():
    from fontTools import subset
    for weight in ("Black", "Bold", "SemiBold", "Medium", "Regular"):
        out = SITE / "fontit" / f"SairaCondensed-{weight}.woff"
        subset.main([str(FONT_SRC / f"SairaCondensed-{weight}.ttf"), f"--unicodes={LATIN}", "--flavor=woff",
                     "--layout-features=*", f"--output-file={out}"])


def images():
    # Desktop: the headline sits on the open sky to the left, the star and its road on the right third.
    W, H = 2000, 1125
    tk.tie((W, H), star_xy=(W * .72, H * .38), star_size=240, horizon=.8, road_x=W * .72).save(
        SITE / "hero.webp", quality=80, method=6)
    # Phone: the headline fills the top, so the star stands lower, above the road's vanishing point.
    W, H = 1080, 1500
    tk.tie((W, H), star_xy=(W / 2, H * .66), star_size=200, horizon=.8).save(SITE / "hero_pysty.webp", quality=78, method=6)
    tk.wordmark(1000).save(SITE / "sanamerkki.webp", quality=92, method=6)

    full = tk.flake(640)
    full.save(SITE / "hiutale.webp", quality=90, method=6)
    for r in tk.races():
        tk.flake(240, active=(r["n"],)).save(SITE / f"hiutale_{r['n']}.webp", quality=88, method=6)

    # Link preview (1200x630): the cropped flake (D) and the wordmark, readable as a thumbnail.
    share = tk.rajattu((1200, 630), base=.9)
    wm = tk.wordmark(560)
    share = tk.over(share, wm, (64, 220))
    d = tk.ImageDraw.Draw(share)
    tk.kick(d, 70, 220 + wm.height + 60, "E-PYÖRÄILYN SUOMEN CUP  ·  3.12.–28.1.", 30, tk.ICE)
    share.save(SITE / "jako.jpg", quality=84, optimize=True)

    tile = Image.new("RGBA", (180, 180), tk.POLAR + (255,))
    tile.alpha_composite(tk.flake(156), (12, 12))
    tile.convert("RGB").save(SITE / "apple-touch-icon.png", optimize=True)
    tile.resize((48, 48), Image.LANCZOS).convert("RGB").save(SITE / "favicon.png", optimize=True)


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "kuvat"
    if which in ("fontit", "kaikki"):
        fonts()
    if which in ("kuvat", "kaikki"):
        images()
