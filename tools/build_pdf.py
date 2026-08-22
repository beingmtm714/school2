#!/usr/bin/env python3
"""
Rebuild school-selection-report.pdf from tools/report-print.html.

Only needed if the PDF content changes. The website (index.html) and the PDF are
separate documents that share content — neither generates the other.

Usage:
    python3 tools/build_pdf.py

Requires: pip install weasyprint
Fonts are downloaded to tools/fonts/ on first run (gitignored).
"""

import pathlib
import subprocess
import sys
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
TOOLS = ROOT / "tools"
FONTS = TOOLS / "fonts"
SRC = TOOLS / "report-print.html"
OUT = ROOT / "school-selection-report.pdf"

FONT_URLS = {
    "SourceSerif4-Regular.ttf": "https://github.com/adobe-fonts/source-serif/raw/release/TTF/SourceSerif4-Regular.ttf",
    "SourceSerif4-Semibold.ttf": "https://github.com/adobe-fonts/source-serif/raw/release/TTF/SourceSerif4-Semibold.ttf",
    "SourceSerif4-Bold.ttf": "https://github.com/adobe-fonts/source-serif/raw/release/TTF/SourceSerif4-Bold.ttf",
    "SourceSerif4-It.ttf": "https://github.com/adobe-fonts/source-serif/raw/release/TTF/SourceSerif4-It.ttf",
    "SourceSans3-Regular.ttf": "https://github.com/adobe-fonts/source-sans/raw/release/TTF/SourceSans3-Regular.ttf",
    "SourceSans3-Semibold.ttf": "https://github.com/adobe-fonts/source-sans/raw/release/TTF/SourceSans3-Semibold.ttf",
    "SourceSans3-Bold.ttf": "https://github.com/adobe-fonts/source-sans/raw/release/TTF/SourceSans3-Bold.ttf",
    "SourceSans3-It.ttf": "https://github.com/adobe-fonts/source-sans/raw/release/TTF/SourceSans3-It.ttf",
}

EXPECTED_PAGES = 7  # cover + contents + 5 content pages


def fetch_fonts() -> None:
    FONTS.mkdir(exist_ok=True)
    for name, url in FONT_URLS.items():
        dest = FONTS / name
        if dest.exists() and dest.stat().st_size > 50_000:
            continue
        print(f"  downloading {name}")
        urllib.request.urlretrieve(url, dest)


def build() -> None:
    try:
        from weasyprint import HTML
    except ImportError:
        sys.exit("weasyprint not installed. Run: pip install weasyprint")

    print("Fetching fonts...")
    fetch_fonts()

    print("Rendering PDF...")
    # report-print.html references fonts/ relative to its own directory
    HTML(filename=str(SRC), base_url=str(TOOLS)).write_pdf(str(OUT))

    try:
        from pypdf import PdfReader

        pages = len(PdfReader(str(OUT)).pages)
        status = "OK" if pages == EXPECTED_PAGES else "PAGE COUNT CHANGED"
        print(f"{status}: {pages} pages (expected {EXPECTED_PAGES})")
        if pages != EXPECTED_PAGES:
            print(
                "  The brief specifies 5 content pages excluding cover and contents.\n"
                "  Trim or expand prose until the count returns to 7 total."
            )
    except ImportError:
        print("(install pypdf to verify page count)")

    print(f"Wrote {OUT}")


if __name__ == "__main__":
    build()
