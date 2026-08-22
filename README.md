# School Selection Research Memorandum

Static site. One page — an opening question, a comparison carrying two charts, five sections, a
ranked reference table, and three appendices. No build step.

Live at **https://beingmtm714.github.io/school2/**

## Deploy

GitHub Pages serves `main` at `/ (root)`. Push and it rebuilds in a minute or two.

```bash
git add -A && git commit -m "..." && git push origin main
```

## Files

| File | Purpose |
|---|---|
| `index.html` | The site — content, styles, two SVG charts, sticky TOC, scroll-spy |
| `robots.txt` | Keeps the page out of search results |
| `.nojekyll` | Prevents Jekyll processing |

Everything is in `index.html`. There are no assets, no dependencies, and no PDF.

## What the page argues

River is entering kindergarten. Every school in New Orleans was put through a five-criterion
pedagogy screen before any test score was looked at; three cleared it — Audubon Charter, the
International School of Louisiana, and Homer Plessy, where he is enrolled now. Willow clears it
too but has the hardest admission in the city.

The measure is LEAP mastery for the cohort River belongs to, across grades 3–8, rather than the
school-level averages that public sources report. Those two numbers differ enough at Plessy that
the distance between schools changes size by a factor of six depending on which you read.

## Two things a future editor should not undo

**Figure 1's panels are separate on purpose.** The K–3 side is the literacy screener reporting
all students; the grades 3–8 side is LEAP reporting the white cohort. They are different tests
measuring different groups, and joining the lines would invent a school that doesn't exist.

**The series colours are validated, not chosen by taste.** The page's own oxblood and pine
measured ΔE 4.9 under deuteranopia, well under the floor of 8, and read as gray. The current set
passes every check with a worst pair of ΔE 18.4.

`CLAUDE.md` has the full detail — chart geometry, the underlying figures, and the constraints.

## Notes

The page carries a `noindex` meta tag and `robots.txt` disallows all crawlers, so it won't appear
in search results. This repository is public, so the content is public regardless — the meta tag
governs search visibility, not access. Treat the link like a shared document.

An earlier revision of this site shipped a 7-page PDF and the WeasyPrint tooling that built it.
Both were removed on 2026-08-22 when the report was rewritten; the originals live in the
`claude-vault` repo under `projects/school-report/`. The old PDF contradicts the current page on
the measure, the recommendation, and the shortlist, so don't restore it without regenerating it.
