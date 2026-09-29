"""Build the self-contained proposal HTML.

Subsets Noto Sans JP (400/700) to exactly the characters used in
src/proposal.html (markup, CSS content and JS strings), embeds the fonts as
base64 WOFF2, and fails if any character is missing from the subset.

Usage:
  python3 build.py --font-regular NotoSansJP-Regular.ttf --font-bold NotoSansJP-Bold.ttf
Requires: pip install fonttools brotli
"""
import argparse
import base64
import html
import io
import pathlib
import re
import string

from fontTools import subset
from fontTools.ttLib import TTFont

ROOT = pathlib.Path(__file__).parent
SRC = ROOT / "src" / "proposal.html"
OUT = ROOT / "FLEX_gaia_proposal.html"
MARK = "/*@@FONTS@@*/"


def used_chars(text: str) -> set[str]:
    text = html.unescape(text)
    chars = set(text) | set(string.printable) | set("0123456789,.％%／")
    # numbers produced at runtime by the calculator (toLocaleString output)
    chars |= set("0123456789,.―")
    return {c for c in chars if c.isprintable() and c not in "\t\n\r\x0b\x0c"}


def subset_font(path: str, chars: set[str]) -> tuple[bytes, set[int]]:
    font = TTFont(path)
    opts = subset.Options()
    opts.flavor = "woff2"
    opts.layout_features = ["*"]
    opts.name_IDs = ["*"]
    opts.notdef_outline = True
    sub = subset.Subsetter(opts)
    sub.populate(unicodes=[ord(c) for c in chars])
    sub.subset(font)
    buf = io.BytesIO()
    font.flavor = "woff2"
    font.save(buf)
    return buf.getvalue(), set(font.getBestCmap())


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--font-regular", required=True)
    ap.add_argument("--font-bold", required=True)
    a = ap.parse_args()

    src = SRC.read_text(encoding="utf-8")
    chars = used_chars(src)
    faces = []
    for weight, path in (("400", a.font_regular), ("700", a.font_bold)):
        data, cmap = subset_font(path, chars)
        missing = sorted(c for c in chars if ord(c) not in cmap and not c.isspace())
        if missing:
            raise SystemExit(f"weight {weight}: glyphs missing for {''.join(missing)!r}")
        b64 = base64.b64encode(data).decode()
        faces.append(
            '@font-face{font-family:"Noto Sans JP";font-style:normal;'
            f"font-weight:{weight};font-display:block;"
            f'src:url(data:font/woff2;base64,{b64}) format("woff2")}}'
        )
        print(f"weight {weight}: {len(cmap)} glyphs, {len(data) / 1024:.0f} KiB")
    assert MARK in src
    OUT.write_text(src.replace(MARK, "".join(faces)), encoding="utf-8")
    print(f"wrote {OUT.name} ({OUT.stat().st_size / 1024:.0f} KiB), {len(chars)} chars")


if __name__ == "__main__":
    main()
