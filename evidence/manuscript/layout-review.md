The page images named below were temporary inspection artifacts. They can be regenerated from the identified release PDF and are not distributed.

# Final repaired PDF: visual layout review

Review completed 8 October 2026 (Asia/Shanghai). **No blocking visual layout issue found.** This review concerns rendering and pagination only; it does not report a mathematical-verifier outcome.

## Exact artifact

- Live artifact: `paper/gersten-counterexamples.pdf`.
- Stable inspected snapshot: `work/final-repaired-layout-source.pdf`.
- SHA-256: `4d0f9f55ffff30979efd40231744bc92c79f1e3172182935aef9d1769c48deb7`.
- Size: 1,184,639 bytes; 121 A4 pages (595.276 × 841.89 pt).
- PDF creation/modification metadata: 8 October 2026, 07:47:23 CST.
- A final byte comparison at 08:09:59 +08:00 confirmed that the live artifact still matched the inspected snapshot. Evidence is saved in `work/final_repaired_layout/hash_recheck.json`.
- Earlier comparison artifact retained: `work/final-context-layout-source.pdf` (118 pages). The new proof material increases the article to 121 pages. This audit does not claim byte-identical page geometry against that earlier edition.

## Rendering and actual inspection

All **121 pages** were rendered at 65 dpi as JPEGs under `work/final_repaired_layout/pages/`. All **16 contact sheets** (`contact-01.jpg` through `contact-16.jpg`) were personally viewed, covering every page in order. The contact-sheet manifest is `work/final_repaired_layout/contact_manifest.json`.

A further **42 full-page PNGs at 120 dpi** were rendered under `work/final_repaired_layout/full/`. Every one of these full pages was personally viewed at original image detail:

**1–3, 17–28, 33–35, 39–41, 54–57, 69–74, 111–121.**

The detailed selection covers the title, abstract, both contents pages, the introduction/result table, all six repair locations, their neighboring page transitions, downstream uses of the changed cyclic comparison, both appendices, and every bibliography page. The full-page render list is also saved in `work/final_repaired_layout/full/rendered_pages.json`.

## Repair locations and findings

| Location | Full pages inspected | Visual finding |
|---|---|---|
| First pages and contents | 1–3 | Title, abstract, contents, result table, and beginning of Section 2 fit their margins. Appendix and bibliography page numbers reflect the new pagination. |
| Divisor support, Thom class, and global Chern identification | 17–19, 39–41 | New argument and its later use render without clipped text, colliding superscripts, or crowded equation numbers. Section/proof transitions remain readable. |
| Cyclic comparison, ordinary differential image, common scalar, and model descent | 20–24, 33–35 | Proposition 7.1 and its extended proof are legible. Displays (7.2) and (7.3), the point-coordinate discussion, and the idempotent iteration fit. Proof continuation across pp. 21–23 is continuous. |
| Rigid restriction and graph-divisor support argument | 24–28 | The support-vanishing paragraph on p. 25 and graph argument on p. 27 fit cleanly. Displays and citations remain inside the text area. |
| Finite-coefficient projective-line splitting and later uses | 54–57, 69–74 | New display (16.3) on p. 56 fits with its arrow label. The stalk argument and limit paragraph are readable; later split-injection and normalization formulas do not collide with surrounding text. |
| Higher-degree uses of the cyclic scalar | 111–115 | Odd- and even-degree product displays, contraction formulas, and the rank-three argument fit. Theorem 31.2 continues from p. 113 to p. 114 at a normal paragraph boundary. |
| Stein-surface analytic Deligne calculation | 115–117 | Appendix A.1, its two-line exact sequence, and the matrix displays fit. No truncated line or equation is visible. |
| Rational weight-two calculation and Feld context | 116–118 | The new localization proof continues naturally across pp. 116–117. The Feld paragraph spans pp. 117–118, and its shortened final sentence keeps the citation inline. |
| Final appendix, authoring note, and references | 118–121 | Matrix displays, the transition to the authoring note, and all 50 bibliography items fit. Link text wraps without clipping; the final page ends with normal white space. |

## Retained pagination details

- On p. 115, the Appendix A heading is followed by one complete introductory sentence; subsection A.1 begins on p. 116. This is slightly shallow section opening placement, but it is not a bare orphan heading and creates no ambiguity or collision. No change is required for release.
- The one-line statement of Proposition 12.22 is at the bottom of p. 41, with its proof continuing on the next page. The statement itself is complete. Long theorem/proof blocks also continue across pp. 111–112 and 113–114; these are ordinary mathematical page breaks.
- Short mathematical connectors, display tails, and normal hyphenation were retained. This final gate did not reopen the earlier comprehensive short-line editing pass.

## Log corroboration and scope

The current TeX log was checked independently: **0 overfull warnings, 0 occurrences of undefined references/citations, and 2 underfull warnings** (one hbox, badness 2173, at lines 245–249; one output vbox, badness 10000). The inspected images show no material spacing problem associated with those warnings.

Across the full contact-sheet inspection and the 42 detailed pages, no visible clipping, overlapping text, collided equations, missing page content, bare orphan section heading, or anomalous blank page was found. The contact-sheet check gives full-document coverage at reduced scale; the 42 listed pages received detailed inspection. No manuscript, source ledger, or PDF was edited during this review. Earlier layout reports and snapshots remain intact.
