# Publication byline PDF: independent layout review

Completed 2026-10-08T00:31:14.606357+00:00. No blocking visual layout issue found. This is a production review, not a mathematical-verification result.

## Exact artifacts

- Current PDF: `paper/gersten-counterexamples.pdf`.
- Current SHA-256: `f1ad73741d0a2cd1580cb338a8478294124653f34228277fa1dd278a45d981f6`.
- Current size: 1,183,637 bytes; 121 A4 pages (595.276 by 841.89 pt).
- Comparison PDF: `evidence/manuscript/reviewed.pdf`.
- Historical SHA-256: `4d0f9f55ffff30979efd40231744bc92c79f1e3172182935aef9d1769c48deb7`.
- PDF metadata identifies the author as OpenAI. The first-page note and authoring paragraph explain the user-requested attribution and the absence of institutional endorsement.
- A hash recheck on completing this review matched the inspected current PDF.

## Commands and actual inspection

Ran `python3 audit_short_lines.py PDF (Guo writing production checker)` separately on both PDFs. Rendered every page of the current PDF with `pdftoppm -r 65 -jpeg -jpegopt quality=85`; all 121 pages rendered successfully. Personally viewed all 16 contact sheets, covering pages 1–121 in order. The contact sheets are local production intermediates; this record preserves their inspection scope.

Rendered and personally viewed 14 full pages at 120 dpi and original image detail: **1–6 and 114–121**. These cover the title/byline/footnote, both contents pages, early text reflow and every changed flag, the neighbouring unchanged page 6, the closing proof and appendices, the new authoring paragraph, and every bibliography page. This review does not claim full-size inspection of the other 107 pages.

The title, author line, abstract, contents, and attribution footnote fit without collision or clipping. The contents continue naturally on page 2, and the early prose and theorem transitions on pages 2–6 remain readable. The new authoring paragraph fits on page 119; references 1–50 remain legible across pages 119–121. All-page contact-sheet inspection found no missing or blank page, clipped display, overlapping text, or new bare orphan heading.

## Comparison and retained flags

The current scan reports **414 flags**, compared with **413** in the preserved PDF. Of these, **401 rows are identical including page, line, and coordinates**. Twelve historical flags moved within pages 2–5. The sole newly reported content is page 5, visual line 6, “Setup 2.3. Put”; it is a normal heading and display lead-in, not a new defect. The 13 differing current rows were all inspected at full-page scale and are recorded below. Existing unchanged flags are retained under the earlier production review; this metadata pass does not claim that all 414 warnings were eliminated.

| Page | Visual line | Flag | Decision |
|---|---|---|---|
| 2 | 36 | short-paragraph-tail, 2 words: unit product | Moved historical flag. Formula lead-in is readable and stays with its display; retain. |
| 2 | 43 | short-paragraph-tail, 2 words: Krull dimension. | Moved historical flag. Normal short paragraph tail; no clipping, collision, or isolated page fragment; retain. |
| 3 | 38 | short-paragraph-tail, 2 words: algebraic K-group. | Moved historical flag. Normal short paragraph tail; no clipping, collision, or isolated page fragment; retain. |
| 3 | 52 | short-paragraph-tail, 4 words: end of the article. | Moved historical flag. Normal short paragraph tail; no clipping, collision, or isolated page fragment; retain. |
| 4 | 12 | mathematical-paragraph-tail, 2 words: Theorem 2.1. Let | Moved historical flag. A theorem heading introducing the displayed rings; retain. |
| 4 | 17 | underfilled-bare-connector-before-display, 13 words: has infinite order and maps to zero in K3(R[1/x]) integrally. Consequently, | Moved historical flag. A complete assertion naturally leads to the noninjectivity display; retain. |
| 4 | 29 | short-paragraph-tail, 2 words: absolute K-theory. | Moved historical flag. Normal short paragraph tail; no clipping, collision, or isolated page fragment; retain. |
| 4 | 37 | short-paragraph-tail, 4 words: and topological cyclic homology. | Moved historical flag. Normal short paragraph tail; no clipping, collision, or isolated page fragment; retain. |
| 4 | 42 | short-paragraph-tail, 2 words: homotopy groups. | Moved historical flag. Normal short paragraph tail; no clipping, collision, or isolated page fragment; retain. |
| 5 | 6 | mathematical-paragraph-tail, 2 words: Setup 2.3. Put | New detector flag. The setup heading naturally introduces the following displayed definitions on the same page; retain. |
| 5 | 39 | short-paragraph-tail, 3 words: assertions of Theorem 2.1. | Moved historical flag. Normal short paragraph tail; no clipping, collision, or isolated page fragment; retain. |
| 5 | 42 | short-paragraph-tail, 5 words: defining cR are units, and | Moved historical flag. Formula lead-in is readable and stays with its display; retain. |
| 5 | 50 | short-paragraph-tail, 4 words: nonzero image in F3. | Moved historical flag. Normal short paragraph tail; no clipping, collision, or isolated page fragment; retain. |

An independent positioned-text comparison used `pdftohtml -xml -stdout`, comparing text plus top/left/width/height coordinates after excluding the running-header area (XML top coordinate at most 100). Body content or positions changed only on pages **1–5 and 119–121**. Pages **6–118** have identical compared body fragments and coordinates. Running headers on even pages now read OpenAI. The comparison record and XML snapshots are retained as local production intermediates; this is a geometry check, not a proof-content certificate.

The retained Appendix A placement on page 115 matches the historical layout: its heading is followed by one complete introductory sentence, with subsection A.1 on page 116. This shallow opening is readable and was not altered.

## Log and scope

The current TeX log has **0 overfull warnings, 0 undefined-reference/citation warnings, and 2 underfull warnings**: one output vbox of badness 10000 and one hbox of badness 2173 at source lines 245–249. These match the historical warning types. The inspected bibliography and ending show no material spacing defect requiring repair.

No repository file, mathematical text, or PDF was edited during this review. Generated inspection images and XML snapshots remain local production intermediates.
