# Review of the consolidated article

This record concerns the complete article as written, including its higher-degree and infinite-rank extensions. It is separate from the twelve accepted facts in the original audit and the twelve local Lean lemmas.

- `reviewed.tex` is the exact standalone TeX source submitted to the native Danus whole-paper mathematics verifier.
- `VERIFY_LEDGER.md` is the native mathematical verdict ledger. `math-review.json` preserves its structured outcome and findings, with internal runtime paths omitted.
- `REFERENCE_LEDGER.md` records the 50 canonical references, their confirmed metadata, precise source links, and the scope and limitations of each verification.
- `review-manifest.json` binds these records to the reviewed source, the modular TeX files, and the pre-byline release PDF by SHA-256. That PDF is now preserved as `reviewed.pdf`; the PDF path inside the historical manifest records its original location.

The review is an independent language-model assessment, not a proof-assistant certificate or journal peer review. Its verdict applies to the archived source identified by the manifest. Successful compilation and repository consistency checks do not independently establish the article's mathematical claims or extend this verdict to future edits.

The [repair record](repair-record.md) explains the six supporting-input findings raised in the second whole-paper review and their treatment in the revised article. The historical accepted-fact proofs retain their original reviewed bytes; the final manuscript supplies the recorded clarifications and normalization repair. The earlier positive and negative whole-paper verdicts are both preserved under `review-history/`.

Three older works were retained as historical attributions after their mathematical inputs were checked in the author-hosted Weibel chapters: Dennis–Stein (1975), Merkurjev (1983), and Quillen's finite-field paper (1972). Their original full texts were not inspected. Besser's regulator source was read from the author's original PostScript after local PDF conversion; the verifier received a transcription of the relevant formulas and independently checked the readable Huber–Kings and Besser–de Jeu comparisons. These distinctions are retained in the reference ledger.

The release build instructions are in the repository README. `make check` verifies source consistency and the original audit's evidence hashes. `make formal` runs the pinned Lean kernel checks. Neither command reruns the historical Danus reviews.

The current byline edition is documented in [the publication record](../publication/README.md). The reviewed source, manifests, verdicts, and historical build records are preserved byte for byte.
