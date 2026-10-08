# Build-tool provenance

The following upstream releases were checked on 2026-10-07. The workflow pins
the Actions by their actual Git commit identifiers, resolved from the official
release tags through the GitHub API.

| Tool | Version | Immutable identifier |
| --- | --- | --- |
| [actions/checkout](https://github.com/actions/checkout/releases/tag/v7.0.1) | v7.0.1 | `3d3c42e5aac5ba805825da76410c181273ba90b1` |
| [actions/upload-artifact](https://github.com/actions/upload-artifact/releases/tag/v7.0.1) | v7.0.1 | `043fb46d1a93c77aae656e7c1c64a875d1fc6a0a` |
| [Lean](https://github.com/leanprover/lean4/releases/tag/v4.34.1) | v4.34.1, Linux x86-64 | archive SHA-256 `47bf4bbd78f70c2e9670598ab7124d92b6efb7330ff33e5fbb4030f6fd72e4e4` |

The original local Lean check used the macOS ARM64 asset from the same release;
its SHA-256 is recorded in `formal/verification_manifest.json`. CI downloads
the Linux asset directly from that release and verifies its digest before use.

The workflow uses `ubuntu-24.04` and its distribution packages for Python and
TeX. Those package versions can receive distribution updates. The repository
therefore pins the formal prover and Actions while recording a reproducible
TeX build procedure, without asserting byte-for-byte reproducibility across
distribution updates.
