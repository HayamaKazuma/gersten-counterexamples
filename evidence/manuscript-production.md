# Manuscript production and verification

*Rational Gersten kernels in ramified regular local rings* is a consolidated research article of **121 pages**. It covers the two- and three-dimensional constructions, all-prime families, rank calculations, higher-degree classes, fixed-ring infinite rank, and explicit Milnor, Beilinson-motivic, and higher-Chow consequences. The introduction states the coefficient and residue-field conditions for each family.

## Coverage and preservation

The article has six mathematical source modules: introduction; explicit three-adic core; quartic core; three-dimensional families; two-dimensional families; and comparisons with related formulations. Together they contain **100 theorem, lemma, proposition, or corollary environments and 96 proof environments**. These are source-coverage counts.

Preservation comparisons checked the mathematical bodies against the reviewed source modules, accounting for namespaced macros and labels, citation aliases, heading changes, and enumerated production edits. They retained every result and proof through the completed assembly and prose passes. The original five TeX manuscripts remain byte-for-byte copies under `archive/original/`, with recorded SHA-256 hashes. The reference record supplies precise source locators and Petrequin’s proper-cycle argument for total degree, including inseparability.

## Distinct verification scopes

- **Original Danus audit:** twelve accepted facts, with their exact statements, full proofs, dependencies, and verdicts under `evidence/danus/`. This is independent language-model review of those facts.
- **Article coverage:** the 100 result environments and 96 proof environments inventory the assembled text; they are not 100 independent certifications.
- **Lean development:** twelve local lemmas—ten polynomial identities and two natural-number inequalities—were recompiled successfully with Lean 4.34.1. The source hash matches the original audit; the checked development contains no `sorry`, `admit`, custom axiom, or `native_decide`. The full K-theory, regulator, and comparison proofs are outside this local formalization.
- **Final whole-manuscript review:** Native Danus `paper_verify_math` returned `passed` / `correct` for the complete final source, with 0 must-fix findings and 0 ignorable findings. The exact source, native ledger, reference ledger, structured verdict, and artifact hashes are archived in [the manuscript review records](manuscript/README.md). The first whole-paper review passed. A second review, after a two-sentence literature addition, identified six missing advanced inputs or normalization justifications. These findings were retained in the review history and addressed by explicit arguments and checked citations before the final complete-document review.

## References

All **50 canonical bibliography ledger entries** have native `verified` verdicts. The records distinguish bibliographic identity, exact theorem locators, and the hypotheses needed at each application. The latest verdicts supersede earlier retrieval or applicability gaps.

The original Dennis–Stein (1975), Merkurjev (1983), and Quillen finite-field (1972) articles were not retrieved in full. Their historical metadata was confirmed, and every invoked input was checked in the cited author-hosted Weibel chapters: III.5.11, III.6.2.4, and IV.1.13, respectively.

For Besser's 2000 regulator article, the host supplied a transcription after inspecting original-source images. The browser verifier corroborated the cited specialization through directly inspected Huber–Kings and Besser–de Jeu texts and checked the normalization identity algebraically. It did not independently decode the original PostScript or authenticate the host's checksums. The final verdict preserves this evidence distinction.

## Production checks

Completed local checks include PDF compilation with `latexmk` and `pdflatex`; TeX input, label, and citation consistency; accepted-proof and archive hashes; a complete acyclic fact graph; and the Lean compilation above. The standalone-source expander passed nested-input, ordering, comment-handling, and cycle-rejection checks. Script syntax, JSON records, documentation links, Makefile targets, and distribution-file selection were checked. Public article sources were screened for internal instructions, private paths, and editorial notes.

Before the final citation revision, all 117 pages of the revised layout rendered successfully. A completed review inspected 25 selected pages at full size, both sides of 38 neighbouring page transitions, and all 393 automated layout flags in context; it found no new defect requiring repair. An earlier review also covered all ten contact sheets of the preceding snapshot. These checks concern their recorded PDF snapshots.

**Final layout review:** The final repaired article was rendered and inspected after compilation. See [the exact final layout record](manuscript/layout-review.md) for the inspected pages, any retained spacing warnings, and the artifact hash. Earlier layout inspections are historical checks of the source versions recorded in the review history.

The GitHub workflow is configured for source checks, PDF compilation, and the local Lean check, with read-only repository permissions, pinned Actions, a checked Lean archive digest, and no secrets or deployment. Its configuration was inspected locally; **no hosted GitHub Actions run has been performed**.

## Release identity

- Flattened manuscript source SHA-256: `4129b94964a2e5a46bdde8141aa7bf580d93e4fb869c177aea402ac919c824a2`
- PDF SHA-256: `4d0f9f55ffff30979efd40231744bc92c79f1e3172182935aef9d1769c48deb7`

Authorship and a distribution license remain unassigned pending the rights holders' choices. The citation template and copyright-status file record those decisions without inventing metadata or granting a license.

## Byline-edition addendum — 8 October 2026

The release identity and unassigned-authorship sentence above describe the reviewed pre-byline edition. The user subsequently requested an OpenAI byline and publication on GitHub. The current edition adds that byline, the PDF author field, and the attribution explanation. All ten other TeX modules remain byte-for-byte unchanged. The [publication record](publication/README.md) preserves the exact delta, the old PDF, and a new source/PDF hash manifest. No new mathematical claim was introduced, and no additional Danus review is claimed.

The byline attributes preparation to ChatGPT/Codex and does not represent an official OpenAI publication or institutional endorsement. The active `CITATION.cff` now contains this attribution. A distribution license remains unselected. The [publishing record](../PUBLISHING.md) reports the actual external-publication status; the historical statement about hosted Actions above remains accurate at the time of this addendum.
