#!/usr/bin/env python3
"""Bundle index.html into one self-contained HTML fragment for a Claude artifact
preview: CSS inlined, fonts and images as data URIs, site-absolute links pointed
at the live site. Output starts with <title> and <style> (no html/head/body),
which is what the Artifact tool expects.

Usage: python3 tools/build-preview.py [out.html]
"""
import base64
import mimetypes
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LIVE = "https://ankitamat.com"
out = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "preview.html"


def data_uri(path: Path) -> str:
    mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    if path.suffix == ".woff2":
        mime = "font/woff2"
    return f"data:{mime};base64,{base64.b64encode(path.read_bytes()).decode()}"


html = (ROOT / "index.html").read_text()
css = (ROOT / "css" / "site.css").read_text()

# fonts referenced from css/ as ../fonts/x.woff2
css = re.sub(r'url\("\.\./(fonts/[^"]+)"\)', lambda m: f'url("{data_uri(ROOT / m.group(1))}")', css)

# body only
body = re.search(r"<body>(.*)</body>", html, re.S).group(1)
title = re.search(r"<title>(.*?)</title>", html).group(1)

# images
body = re.sub(r'src="(img/[^"]+)"', lambda m: f'src="{data_uri(ROOT / m.group(1))}"', body)

# site-absolute links -> live site; in-page anchors stay
body = re.sub(r'href="/([^"]*)"', lambda m: f'href="{LIVE}/{m.group(1)}"', body)

# artifact head is 14px system font on an off-white ground; the site's own
# tokens override everything that matters, but pin the ground explicitly.
frag = f"<title>{title}</title>\n<style>\n{css}\nhtml, body {{ background: #ffffff; }}\n</style>\n{body}"
out.write_text(frag)
print(f"wrote {out} ({out.stat().st_size/1024:.0f} KB)")
