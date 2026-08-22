# CLAUDE.md

## Your task

Publish this folder to GitHub Pages and give me back the live URL.

Finished static site. No build step, no framework, no npm, no package.json. `index.html` is
self-contained — content, CSS, inline SVG chart, one small scroll-spy script. It loads two
fonts from Google Fonts and nothing else.

**If these files arrived as a zip, unzip into the working directory first and confirm the
file map below before doing anything else.** The archive may not carry `.nojekyll`,
`.gitignore`, or `robots.txt` depending on how it was extracted — recreate any that are
missing using the contents given at the bottom of this file.

## Deploy

```bash
git init -b main
git add .
git commit -m "School selection research memorandum"
gh repo create school-report --public --source=. --remote=origin --push
gh api -X POST repos/:owner/school-report/pages -f 'source[branch]=main' -f 'source[path]=/'
```

If that last call errors: **Settings → Pages → Deploy from a branch → `main` → `/ (root)`.**

Wait for it to go live, then report the URL:

```bash
URL=$(gh api repos/:owner/school-report/pages --jq .html_url)
until curl -sfo /dev/null "$URL"; do sleep 10; done
echo "LIVE: $URL"
```

Print the URL on its own line so I can copy it.

## Verify before reporting back

- [ ] Page loads; the two literacy curves animate in on the hero figure
- [ ] All three Download links serve `school-selection-report.pdf`, which opens to 7 pages
- [ ] All ten rail links jump correctly (I, II, III, IV, V, VI, A, B, C, Sources)
- [ ] Left rail highlights the active section on scroll at desktop width
- [ ] At 390px the rail collapses to a top bar and the chart shows a text legend
- [ ] `curl <URL>/robots.txt` returns `Disallow: /`
- [ ] Page source contains `<meta name="robots" content="noindex, nofollow, noarchive">`

## File map

```
index.html                    the site — 6 sections plus 3 appendices
school-selection-report.pdf   download target, 7 pages
robots.txt                    Disallow: / — required, do not remove
.nojekyll                     stops Jekyll processing — keep
.gitignore
tools/report-print.html       WeasyPrint source for the PDF
tools/build_pdf.py            regenerates the PDF; fetches fonts on first run
```

## Constraints

1. No build step, framework, or dependency.
2. Don't rename `index.html` or `school-selection-report.pdf` — the PDF filename is hardcoded
   in three `<a href>` attributes.
3. Don't edit findings, figures, or citations. Every number traces to a Louisiana Department
   of Education workbook.
4. **Keep the `noindex` meta tag and `robots.txt`.** The site is meant to be reachable by link
   but absent from search results. If either is missing after extraction, recreate it.
5. Keep `.nojekyll`.
6. **The PDF is Sections I–VI only. The appendices are web-only.** Don't add them to the PDF
   without instruction — it is tuned to exactly five content pages and extra content overflows.

## Editing the hero chart

Inline SVG in `index.html` inside `<figure class="figure">`. Coordinates are computed:

```
x = 48 + gradeIndex * 184        # K=48, G1=232, G2=416, G3=600
y = 24 + (100 - value) * 2.56    # viewBox 720 x 300
```

Values: Plessy `58.6, 69.6, 56.9, 48.5` (`#7A2E2E`), ISL `22.8, 39.8, 59.4, 68.3`
(`#1F5C4D`), Louisiana benchmark `69.0, 67.5, 64.4, 64.0` (dashed gray).

Change the data and five things must agree: polyline points, endpoint `<circle>` positions,
`<text class="flab">` labels, the `<ul class="legend">` below the SVG, and Table 3 in Section V.

## Rebuilding the PDF

Only if PDF content changes.

```bash
pip install weasyprint pypdf
python3 tools/build_pdf.py
```

Prints the page count. **Seven total is correct** — cover, contents, five content pages. If it
changes, trim prose; don't shrink type, it's already at 8.6pt.

## Design tokens

Ink `#16130F` · secondary `#494139` · muted `#857B70` · background `#F7F5F1` · rules `#E2DCD3`
· oxblood `#7A2E2E` · pine `#1F5C4D` · amber `#8A6D1F`. Newsreader for display and body,
Source Sans 3 for labels and tables.

## Don't

Modernize the typography. Add gradients, card shadows, or larger radii. Add analytics. Turn the
tables into a JS component. Add animation — one orchestrated moment on load is the whole budget.

## Recreate if missing after unzip

`robots.txt`:

```
User-agent: *
Disallow: /
```

`.nojekyll` — empty file.

`.gitignore`:

```
fonts/
__pycache__/
.DS_Store
*.pyc
```

And in the `<head>` of `index.html`, immediately before `<title>`:

```html
<meta name="robots" content="noindex, nofollow, noarchive">
```
