The baseline source is distributed as `review-history/round2-reviewed.tex`, and the final source as `reviewed.tex`. Paths beginning with `work/` name temporary audit artifacts.

# Final supporting-input repair: bounded source audit

Completed 8 October 2026. This records the completed independent, read-only comparison of `work/manuscript_math_review_round2.tex` against the native `github-release/main.tex` after the revision and the removal of six unsolicited author-placeholder/editorial-macro lines. No additional audit or manuscript modification was performed when this record was saved.

## Source identity

- Baseline SHA-256: `c9a62527699740774c4e3cde106c50dc42dc430170620ab8aac4a22884ab0b96`.
- Audited revised native source SHA-256: `4129b94964a2e5a46bdde8141aa7bf580d93e4fb869c177aea402ac919c824a2`.
- Expanding `outputs/gersten-counterexamples/paper/main.tex` with the repository's `flatten` function produced text byte-for-byte identical to the audited native source. The function was invoked in memory; no generated source file was written during the audit.

## Authorized scope

The comparison allowed only the six supporting-input repairs: divisor-support Thom/Gysin identification; cyclic first-Chern normalization and finite-model descent; rigid support vanishing and restriction; finite-coefficient projective-line splitting; analytic Stein-surface Deligne vanishing; and equal-characteristic rational weight-two constancy. It also allowed the required downstream propagation of the common nonzero scalar, one new equation label, the Cartan bibliography entry, and the optional Feld citation-tail shortening.

Every actual difference hunk was inspected. The changes fall within that scope. The obsolete diff file's six unsolicited metadata/editorial lines are absent from the audited current source.

## Preservation and consistency findings

| Item | Baseline | Revised | Finding |
|---|---:|---:|---|
| Formal result environments | 100 | 100 | Order preserved: 22 theorems, 23 propositions, 45 lemmas, 10 corollaries |
| Proof environments | 96 | 96 | Order preserved; no unrelated proof dropped |
| Labels | 286 | 287 | All existing labels and their order preserved; only `d3:eq:finitePonebundle` added |
| Bibliography keys | 49 | 50 | All existing keys and their order preserved; only `CartanStein1952` added |

Only the authorized statement of `d2:prop:cyclic` changed among the 100 formal result bodies. The module boundary sequence was preserved. No undefined cross-reference, duplicate label, duplicate bibliography key, author placeholder, or unsolicited editorial macro remained. The bibliography after deletion of the new Cartan entry was identical to the baseline bibliography.

The scalar audit checked the proposition, the completed quartic detector, the higher odd-degree product, and the even-degree product with Laurent residue. These use the same first power of the common nonzero scalar at each fixed coefficient ring. Raw point coordinates and the purely de Rham classes and weighted proposition remain unchanged. Both trace/contraction formulas include the scalar. The independence argument uses injectivity of multiplication by a nonzero coefficient-field element as a linear map over the base field; it imposes no rationality or Galois-invariance condition on the scalar. The separate three-dimensional formulas written as `t gamma` define gamma to be the actual character component and therefore require no additional scalar insertion.

## Outcome and limit

**No concrete blocking issue was found in this bounded source audit.** The source preserves all results and proofs within the authorized repair scope. This is preservation and consistency evidence; it is not a replacement for the final whole-paper mathematical verifier, which was being started separately when this record was saved. The counts are coverage counts, not counts of independently certified theorems.
