# CLAUDE.md

Static site. One page, no build step, no framework, no npm, no package.json. `index.html` is
self-contained — content, CSS, two inline SVG charts, one small scroll-spy script. It loads two
fonts from Google Fonts and nothing else.

Live at **https://beingmtm714.github.io/school2/**

## Deploy

Pages serves `main` at `/ (root)`. Push to `main` and it rebuilds in a minute or two.

```bash
git add -A && git commit -m "..." && git push origin main
```

Pages could not be enabled from the API or from an Actions workflow in this repo — the token
lacked permission both ways. It is switched on manually under Settings → Pages. Leave it alone.

## File map

```
index.html    the site — the whole thing
robots.txt    Disallow: / — required, do not remove
.nojekyll     stops Jekyll processing — keep
.gitignore
```

There is no PDF. An earlier revision shipped a 7-page PDF built with WeasyPrint from
`tools/report-print.html`; that report was superseded and both the PDF and its tooling were
removed on 2026-08-22. The originals are in the `claude-vault` repo under
`projects/school-report/` if they are ever needed. Don't reintroduce them without regenerating
the content — the old PDF contradicts the current page on the measure, the recommendation, and
the shortlist.

## Page structure

The left rail is a sticky table of contents at desktop width. Below 900px it is replaced by a
sticky `<details>` TOC in the top bar, which also names the current section when closed.

| Anchor | Label | What it is |
|---|---|---|
| `#q` | The question | Three schools, and the five criteria that produced them |
| `#arc` | The comparison | Both charts, plus how to read them |
| `#s2` | Section I | Why cohort figures rather than school averages |
| `#s4` | Section II | The schools, argued one at a time |
| `#s5` | Section III | The evidence tables |
| `#s6` | Section IV | What a move costs |
| `#s1` | Section V | The recommendation, the deadline, the calendar |
| `#field` | Reference | The full field, ranked |
| `#method` | Appendix A | Method |
| `#city` | Appendix B | Full city data |
| `#screens` | Appendix C | Evidence behind the screens criterion |

The order is deliberate: the comparison and the reasoning come before the ask. The enrollment
deadline lives in Section V, not the header — an earlier revision opened on it and read as an
alarm about a decision the reader had not been introduced to yet.

## The two charts

Both are inline SVG inside `#arc`, `viewBox="0 0 760 352"`, sharing one y-scale:

```
y = 28 + (100 - value) * 2.4        # 0 -> 268, 50 -> 148, 100 -> 28
```

X positions are fixed per panel:

```
Figure 1 left   (screener, K–3)     x = 58, 132, 206, 280
panel divider                       x = 306
Figure 1 right  (LEAP, grades 3–8)  x = 332, 392, 452, 512, 572, 632
Figure 2        (LEAP, grades 3–7)  x = 332, 407, 482, 557, 632
label gutter                        632 → 760, reserved for direct end labels
```

**Figure 1 is two panels on purpose, and the lines must not be joined across the divider.** The
left panel is the K–3 literacy screener and reports **all students**; the right panel is LEAP and
reports **the white cohort**. At Audubon and ISL the two nearly agree at grade 3, but at Plessy
they differ by seventeen points, 48.5 against 66. Splicing them would draw a school that does not
exist. The divider and the caption explaining it are load-bearing content, not decoration.

**Figure 2's shaded left region is a gap, not a zero.** The screener measures reading only, so no
early-grades mathematics figure exists for any school. Grade 8 is absent because students take
Algebra I, which reports separately.

### Chart data

Figure 1, left — screener, all students, K/1/2/3:

```
Audubon    71.6, 69.3, 81.0, 82.5
ISL        22.8, 39.8, 59.4, 68.3
Plessy     58.6, 69.6, 56.9, 48.5
Louisiana  69.0, 67.5, 64.4, 64.0   (dashed)
```

Figure 1, right — LEAP reading, white cohort, grades 3–8:

```
Audubon    86, 78, 69, 74, 89, 90
ISL        68, 87, 69, 84, 92, 82
Plessy     66, 59, 64, 79, 70, 65
Orleans    81, 80, 79, 86, 86, 84   (dashed)
```

Figure 2 — LEAP mathematics, white cohort, grades 3–7:

```
Audubon    84, 68, 53, 61, 72
ISL        60, 82, 65, 69, 80
Plessy     52, 33, 41, 73, 56
Orleans    73, 69, 62, 80, 75       (dashed)
```

Change any of these and four things must agree: the `<polyline>` points, the endpoint `<circle>`
positions, the `<text class="endlab">` direct labels, and the `<ul class="legend">` beneath the
figure — plus the matching table in Section III.

## Series colours

```
Audubon  #A87B0E     ISL  #0B6FA4     Plessy  #A83232     benchmark  #857B70 dashed
```

**Do not revert these to the page's oxblood and pine.** That pair measured ΔE 4.9 under
deuteranopia against a floor of 8, and two of the three fell below the chroma floor — they
rendered as gray. This set passes lightness band, chroma floor, CVD separation, normal-vision
floor and contrast, with a worst adjacent pair of ΔE 18.4. Every line also carries a direct end
label, so identity never rests on colour alone. If you change a series colour, re-validate the
whole set rather than eyeballing it.

Series colour is a separate job from the page palette below. The card score chips use pine and
oxblood tints as *status* colours, good against weak, which correctly stays distinct from series
identity.

## Design tokens

Ink `#16130F` · secondary `#494139` · muted `#857B70` · background `#F7F5F1` · card `#FFFFFF` ·
rules `#E2DCD3` and `#EFEAE3` · oxblood `#7A2E2E` · pine `#1F5C4D` · amber `#8A6D1F`.
Newsreader for display and body, Source Sans 3 for labels and tables.

## Constraints

1. No build step, framework, or dependency.
2. Don't rename `index.html`.
3. Don't edit findings, figures, or citations. Every number traces to a Louisiana Department of
   Education workbook, named in Appendix A.
4. **Keep the `noindex` meta tag and `robots.txt`.** The site is meant to be reachable by link
   but absent from search results. The repository is public, so the page content is public
   regardless — the meta tag only keeps it out of search results.
5. Keep `.nojekyll`.

## Don't

Modernize the typography. Add gradients, card shadows, or larger radii. Add analytics. Turn the
tables into a JS component. Add animation — one orchestrated moment on load is the whole budget.
