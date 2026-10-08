# Byline edition

The user requested the **OpenAI** byline and publication on GitHub on 8 October 2026. The byline attributes preparation of this consolidated article to ChatGPT/Codex. It is not an official OpenAI publication or institutional endorsement. The original manuscripts retain their archived contents and attribution.

This edition adds the byline and its explanatory note in `paper/main.tex`, the PDF author field in `paper/preamble.tex`, and an attribution paragraph in `paper/verification-scope.tex`. The exact changes are in [metadata.patch](metadata.patch). The other ten TeX modules, including all six mathematical sections and the bibliography, retain their reviewed bytes.

[metadata-manifest.json](metadata-manifest.json) binds the current PDF and standalone source to the historical reviewed source. The previous PDF is preserved as [`../manuscript/reviewed.pdf`](../manuscript/reviewed.pdf); the path in the historical manifest records its original location. The historical source, ledgers, verdicts, manifests, and build records are unchanged. This production update does not rerun or extend the Danus verdict to new mathematics.

`make check` verifies every recorded hash, reverses exactly the three permitted metadata changes to recover the reviewed module hashes, regenerates the patch, and compares a fresh standalone expansion with [publication.tex](publication.tex). This makes the scope of this edition independently checkable with Python. The PDF hash identifies the distributed PDF, not a promise of identical output from another TeX installation. After rebuilding a PDF, preserve the previous record and record a new artifact hash before publishing a new edition.

Citation metadata is validated against the [official CFF 1.2.0 schema](https://raw.githubusercontent.com/citation-file-format/citation-file-format/1.2.0/schema.json). No affiliation, institutional approval, DOI, or distribution license has been added.

The fixed Lean 4.34.1 compiler was rerun locally before packaging; all twelve unchanged local lemmas passed. The new [result](lean-rerun-result.json) and [output](lean-rerun-output.txt) accompany the preserved historical checking records.

The local build and layout checks are recorded in [production-checks.json](production-checks.json) and [layout-review.md](layout-review.md). This packaging snapshot precedes hosted checks. The root [publishing record](../../PUBLISHING.md) identifies the public repository and links subsequent GitHub Actions results.
