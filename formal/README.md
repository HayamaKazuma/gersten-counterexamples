# Local formal checks

`GerstenAudit.lean` contains twelve theorems checked by Lean 4.34.1. It imports
only `Std`. The first ten prove polynomial identities over an arbitrary
commutative ring, with quotient relations and invertibility assumptions stated
explicitly. The last two prove inequalities in natural numbers used to control
indices in the written tail argument.

The development contains no proof admission or custom axiom and does not use
`native_decide`. `#print axioms` records dependence on Lean's standard
`propext`, `Classical.choice`, and `Quot.sound` where applicable.

## Run

Install [Lean 4.34.1](https://github.com/leanprover/lean4/releases/tag/v4.34.1)
directly, or use an existing `elan` installation:

```sh
elan toolchain install leanprover/lean4:v4.34.1
make formal
```

Run `make formal` from the repository root. The script invokes Lean in this
directory, so `lean-toolchain` takes effect. A direct compiler path also works:

```sh
make formal LEAN=/path/to/lean
```

New output is saved to `build/formal/lean.log` and `build/formal/result.json`.
The checked-in `lean_verification.log` and `verification_manifest.json` describe
the original audit run. The source hash is checked by `make check`.
No Lake package file is needed for a single file importing only `Std`.

## Mathematical boundary

The polynomial identities certify the displayed algebraic relations, including
the Dennis--Stein argument substitutions and the equations for the scaled maps.
They do not certify the Dennis--Stein identities in algebraic K-theory, the
existence or continuity of ring homomorphisms, the invertibility of every symbol
entry, or the subsequent regulator calculation. The two inequalities support
the written valuation estimate; they do not formalize valuations or convergence
of the infinite series. The full counterexamples are established by the textual
proofs in the paper and supporting evidence, with the stated external inputs.
