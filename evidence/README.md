# Mathematical evidence and provenance

This directory contains the public mathematical records from the audit of
`gersten_research_package.zip` dated 2026-10-07. The source archive has SHA-256
`45be52c79544b9d493ce27a1b1da973ad7f489e9b367bca635b8108dde73439a`.

The [Chinese audit report](audit-report.zh-CN.md) describes the conclusions,
repairs, and scope. Its public edition omits internal process-state references.
[provenance.json](provenance.json) records the Danus source commit, model
settings, and the original verification summary.

## Accepted facts

[`danus/fact_index.json`](danus/fact_index.json) links twelve accepted facts to
their statements, predecessors, original proof hashes, and verification
records. The proof files in `danus/facts/` are byte-identical to the accepted
proofs. The files in `danus/verdicts/` preserve the mathematical verdict,
review summary, errors, gaps, timestamp, original record identifier, and the
hash of the original project verification file. Internal assignment files,
process states, and private worker memory are excluded.

The central complete theorems are facts `3bd2401d20c8d7de` (dimension two,
including completion) and `59cdde297e2a4505` (the explicit dimension-three
example, including completion). Fact `3d341b9a1d18342e` gives the independent
geometric route for the uncompleted dimension-two ring. Fact
`32e8bb926907031c` addresses the strict simplicial-functor assignments in
Satoshi Mochizuki's arXiv:1503.07966v8, Lemma 13(III); its scope does not assert
that the paper's Theorem 5 is false.

These are language-model review records. They are distinct from Lean kernel
checks and from editorial peer review. The repository's automated check verifies
their hashes, acceptance fields, and complete acyclic dependency graph; it
does not reperform the mathematical review.

## Exploratory reviews and supplements

`reviews/` preserves the source-assisted branch reviews and their historical
coverage tables. Some entries record a then-pending dependency later closed by
an accepted fact. Read such entries together with the final audit report and
fact index. A review's `R` or `C` status is a local coverage label, not a Danus
acceptance or a formal proof certificate. The higher-degree and infinite-rank
extensions have not each received a separate full-theorem acceptance.

`supplements/` contains five TeX repair notes addressing the analytic Deligne
interval model, finite-rank HKR comparison, essentially smooth localization,
point-class spanning, and syntomic normalization. They are supporting source
fragments, not independent TeX documents.

The original archive's five TeX manuscripts remain unchanged under
[`archive/original/`](../archive/original/). Their inclusion and hashes are
recorded in [`archive/origin_manifest.json`](../archive/origin_manifest.json).
The archived PDFs duplicate these sources and are omitted. The original
manuscripts contain earlier formulations; the consolidated paper and audit
corrections should be read with them.

## Consolidated article review

The complete final article also passed a separate native whole-paper mathematical review. [The manuscript records](manuscript/README.md) preserve the exact reviewed source, the verdict, all 50 reference entries, and a SHA-256 manifest. This whole-document assessment includes the extensions as written; it does not create 100 separate accepted facts or enlarge the scope of the twelve Lean lemmas. [The production report](manuscript-production.md) records the source preservation and build checks.
