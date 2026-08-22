# School Selection Research Memorandum

Static site. One page with six sections and three appendices, plus a 7-page PDF. No build step.

## Deploy to GitHub Pages

```bash
git init -b main
git add .
git commit -m "School selection research memorandum"
gh repo create school-report --public --source=. --remote=origin --push
```

Then **Settings → Pages → Source: Deploy from a branch → `main` → `/ (root)`**.

Live at `https://<user>.github.io/school-report/` in under two minutes.

## Files

| File | Purpose |
|---|---|
| `index.html` | The site — content, styles, SVG chart, scroll-spy |
| `school-selection-report.pdf` | Download target, linked three times from the page |
| `robots.txt` | Keeps the page out of search results |
| `.nojekyll` | Prevents Jekyll processing |
| `tools/report-print.html` | WeasyPrint source for the PDF |
| `tools/build_pdf.py` | Regenerates the PDF (`python3 tools/build_pdf.py`) |

## Notes

The page carries a `noindex` meta tag and `robots.txt` disallows all crawlers, so it won't
appear in search results. It is still reachable by anyone with the URL — treat the link like
a shared document.

The site and the PDF are separate documents; content changes go in both. The three appendices
(Methodology, Full City Data, Ranked Shortlist) are web-only and not in the PDF.

See `CLAUDE.md` for full build and editing instructions.
