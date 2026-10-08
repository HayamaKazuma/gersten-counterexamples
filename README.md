# Rational Gersten kernels in ramified regular local rings

[GitHub repository](https://github.com/HayamaKazuma/gersten-counterexamples) · [Hosted checks](https://github.com/HayamaKazuma/gersten-counterexamples/actions) · [Publishing instructions](PUBLISHING.md)

[Read the paper](paper/gersten-counterexamples.pdf) · [中文说明](README.zh-CN.md) · [Verification evidence](evidence/README.md)

This repository contains a 121-page research article, its TeX sources, supporting audit records, and a small Lean development. The article constructs infinite-order elements in rational Gersten kernels for ramified regular local rings, beginning with the two-dimensional ring

$$
A_2=\left(\mathbf Z_{(5)}[T,x,y]/(\Phi_5(1+y)+x^4+Txy^3)\right)_{(5,x,y)}
$$

and its completion, and the three-dimensional ring

$$
A_3=\left(\mathbf Z_{(3)}[x,y,z]/(3+xy+z^2)\right)_{(x,y,z)}
$$

and its completion. In the latter case the class is the explicit product

$$
c=2\left\{\frac{1+z}{2},\,1+x,\,1+\frac{(1+x)y}{4}\right\}.
$$

The article gives explicit unit products in both dimensions and develops the supported-class, regulator, and completion arguments. Its extensions include:

- Tame and Eisenstein families at every residue prime, with arbitrarily large kernel rank in fixed local dimension.
- Higher odd-degree classes and products of specified units in every degree at least three.
- At every prime, fixed three-dimensional rings, including complete rings, with infinite rational generic-kernel rank in every degree at least three.
- A fixed complete two-dimensional ring in residue characteristic five with the same infinite-rank property in every degree at least three.
- Explicit Milnor kernel classes in dimensions two and three, and Beilinson-motivic and higher-Chow consequences of the three-dimensional construction.

The introduction gives the coefficient rings, residue fields, and references for each family. The original research manuscripts are preserved separately. [Manuscript production and coverage](evidence/manuscript-production.md) records how the six article modules were assembled and checked.

## Contents

| Path | Contents |
| --- | --- |
| [`paper/`](paper/) | The 121-page article, six source modules, and buildable TeX sources |
| [`formal/`](formal/) | Twelve Lean lemmas, pinned toolchain, and the original checking log |
| [`evidence/danus/`](evidence/danus/) | Twelve accepted mathematical facts, full proofs, verdicts, and dependency index |
| [`evidence/reviews/`](evidence/reviews/) | Source-assisted reviews and coverage inventories |
| [`evidence/supplements/`](evidence/supplements/) | TeX supplements prepared during the audit |
| [`archive/original/`](archive/original/) | Five original TeX manuscripts, preserved byte for byte |
| [`scripts/`](scripts/) | Portable consistency checks and packaging tools |

## Build and check

The paper requires a TeX distribution with `pdflatex`, `latexmk`, Latin Modern fonts, and the usual AMS and extended LaTeX packages. The scripts require Python 3.9 or later. The formal check requires [Lean 4.34.1](https://github.com/leanprover/lean4/releases/tag/v4.34.1), with no Mathlib or other external Lean packages.

```sh
make check          # TeX references, proof hashes, dependencies and archive hashes
make pdf            # paper/gersten-counterexamples.pdf
make formal         # compile the twelve local Lean proofs
make standalone     # build/gersten-counterexamples.tex, with local inputs expanded
make dist           # check, build, and package into dist/gersten-counterexamples.zip
```

To select a separately installed Lean binary, use `make formal LEAN=/path/to/lean`. With `elan`, the file `formal/lean-toolchain` selects the required version. See [formal/README.md](formal/README.md) for the exact scope and setup. `make clean` removes generated intermediates and keeps the manuscript PDF.

The GitHub Actions workflow is configured to run the same checks, build the PDF, and upload it as an artifact. It uses a read-only repository token and requires no secrets. The Lean release archive is checked against its SHA-256 digest, and both Actions are pinned to verified commit IDs. [Tool provenance](evidence/tool-provenance.md) records the release sources. TeX is installed from Ubuntu packages; the workflow reproduces the build process, rather than promising byte-identical PDFs across TeX distributions. The local packaging snapshot predates hosted checks. See [GitHub Actions](https://github.com/HayamaKazuma/gersten-counterexamples/actions) for subsequent hosted results; they are separate from the recorded local verification.

## Verification scope

The audit accepted twelve facts through Danus independent language-model review, including the complete central theorems for the two-dimensional and three-dimensional rings and their completions. The fact graph is complete and acyclic. The mathematical proof texts are preserved with their original hashes; each verdict is linked from the [fact index](evidence/danus/fact_index.json).

The Lean development checks ten polynomial identities and two inequalities in natural numbers. Its recorded run contains no `sorry`, `admit`, custom axiom, or `native_decide`. These local proofs do not formalize the complete algebraic K-theory, regulator, or comparison arguments.

The consolidated article contains 100 theorem, lemma, proposition, or corollary environments and 96 proof environments. These are source-coverage counts, not 100 independent certifications. The original twelve accepted facts and the twelve local Lean lemmas retain their separate scopes. The final whole-manuscript Danus review completed without an unresolved mathematical blocker. All 50 bibliography ledger entries received verified verdicts within their recorded source and applicability scopes. The [production record](evidence/manuscript-production.md) identifies the reviewed release, completed checks, and historical-source and transcription limits.

The source, evidence, and automated checks are intended to make mathematical review reproducible. A passing build checks the files and local formal lemmas; it does not rerun the historical model review.

## Citation and rights

The article carries the **OpenAI** byline at the user's request, attributing its preparation to ChatGPT/Codex. This is not an official OpenAI publication or institutional endorsement. [CITATION.cff](CITATION.cff) supplies the citation metadata. The original source manuscripts retain their archived attribution.

The [publication record](evidence/publication/README.md) records this metadata-only change and binds the current PDF and sources to the preserved mathematical review. All ten other TeX modules, including the six mathematical sections and bibliography, are byte-for-byte unchanged.

A distribution license has not yet been selected. See [COPYRIGHT.md](COPYRIGHT.md). The external build tools retain their own licenses and are not included in this repository.
