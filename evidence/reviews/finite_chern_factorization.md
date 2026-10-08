# Finite-coefficient Chern factorization in every weight n ≥ 2

Independent stress test, 2026-10-07. Scope: manuscript lines 314–340 and 1703–1755. No obstruction was found. This note records the precise factorization and the roles of the cited results. It is a mathematical audit, not a formal certificate.

Let E/Q5 be any finite extension, O its valuation ring, and let n≥2 and j=2n−1≥3. Put X=K(O), Xν=X/5^ν, and Tν=μ_{5^ν}^{⊗n} on Spec E, with the usual Tate-twist reduction transition maps. We use spectral p-completion X^∧_5=holimν Xν.

For each ν there is a composite

    π_j(X^∧_5) → K_j(O; Z/5^ν)
                  → K_j(E; Z/5^ν)
                  → H¹(E,Tν).

The first arrow is the canonical homotopy-limit projection, the second comes from O→E, and the last is Soulé's finite Chern class c_{n,1}. The hypothesis that 5 be invertible applies to E, not O. Applying the cited étale-Chern construction directly to O would be unjustified; the displayed route is exactly the route allowed by the manuscript.

## Verification against Weibel's numbered statements

The primary source is Charles Weibel, *Étale Chern classes at the prime 2*, pages 8–12:
https://sites.math.rutgers.edu/~weibel/archive/papers-dir/chernclass.pdf

- The construction (2.1) works for K-degree j≥2 with j+k=2i. Taking i=n, k=1, j=2n−1 gives every weight n≥2, with no stable-range upper bound in n.
- Proposition 2.1.1 gives naturality under ring maps, hence under every automorphism σ_g of E.
- Lemma 2.3 identifies the finite Chern class after K_j(E)→K_j(E;Z/5^ν) with the ordinary integral-source Chern class with those finite coefficients. It also gives additivity for the latter.
- Proposition 2.4 gives additivity of the finite-source Chern class because 5^ν is odd. The exception at the prime two is irrelevant in all degrees here.
- Proposition 2.8 includes compatibility of K_j(A;Z/qr)→K_j(A;Z/r) with the corresponding twist-coefficient reduction. Set q=5 and r=5^ν. This is precisely the ν+1→ν transition used above. No factor depending on ν appears in this reduction square.

A notation caution: the transition on twists is the canonical reduction of Z5(n), equivalently induced by μ_{5^{ν+1}}→μ_{5^ν}, ζ↦ζ^5, in each factor. One must not replace it by a tensor power of the opposite inclusion. The manuscript uses the reduction direction, so there is no hidden factor 5^{n−1} in the inverse system.

## The source inverse limit and linearity

Compatibility gives a canonical additive map

    π_j(X^∧_5) → limν H¹(E,Tν).

The source Milnor exact sequence has a possible lim¹ K_{j+1}(O;Z/5^ν) term. That term presents no obstruction: the map uses the canonical projections, not an asserted identification π_j(X^∧_5)=lim K_j(O;Z/5^ν), nor a lifting of arbitrary compatible families. Any element in the source lim¹ subgroup is simply killed by all of these projections and hence by the constructed map. Neither surjectivity nor injectivity of actual K_j(O) into completed homotopy is needed.

Homotopy groups of a 5-complete spectrum carry their canonical Z5-module structure. Every finite target H¹(E,Tν) is killed by 5^ν. If a∈Z5, choose an integer aν congruent to a modulo 5^ν; for z in the source, additivity gives fν(az)=aν fν(z), since (a−aν)z lies in 5^ν times the source. Hence the inverse-limit map is Z5-linear. This argument does not assume a separate continuity theorem for the Chern maps.

## The target inverse limit and its only lim¹ issue

Continuous étale/Galois cohomology has the exact sequence

    0 → lim¹ν H⁰(E,Tν) → H¹_cont(E,Z5(n))
      → limν H¹(E,Tν) → 0.

Each H⁰(E,Tν) is finite: it is a subgroup of the finite module Tν. Any inverse sequence of finite groups is Mittag–Leffler, because the images in each fixed finite level form a descending chain of subgroups and stabilize. Surjectivity of the transition maps on invariants is not required. Thus the target lim¹ term is zero and the inverse limit identifies canonically with H¹_cont(E,Z5(n)).

Rationalization gives

    π_j(K(O)^∧_5[1/5]) → H¹(E,Q5(n)).

Here π_j commutes with inverting 5. Also H¹(E,Z5(n))[1/5]≅H¹(E,Q5(n)): continuous cocycles on the compact group G_E have bounded image in a finite-dimensional Q5-vector space, and can be multiplied by a single power of 5 to lie in the stable lattice Z5(n); the same scaling treats coboundaries. This verifies the comparison in degree one directly. The resulting map is Q5-linear and Galois-equivariant.

By Lemma 2.3 and naturality, the composite from every actual element of K_j(O) is its usual rational étale Chern class. It therefore has exactly the factorization required in the manuscript.

## Compatibility with the arithmetic polylogarithm coefficients

Besser–de Jeu, Theorem 1.10(2), applies in all n≥2 to a localization of a number ring at a nonzero prime and sends a special-unit symbol to a common nonzero rational multiple ±(n−1)! of the modified polylogarithm. There is no unproved Beilinson–Soulé assumption for those number fields:
https://www.numdam.org/article/ASENS_2003_4_36_6_867_0.pdf

For the manuscript's ζ_jρ, both the root and its complement are units at the selected prime, because the residue of ζ_j is not 1. The factor ζ_jρ is torsion, so the rational symbol is a cycle. The local completion of Q(μ_{5^m−1},ρ) is E_m: the order of 5 modulo 5^m−1 is m, and adjoining ρ supplies the totally ramified degree-four factor. The automorphisms fixing μ_{5^m−1} and sending ρ↦ρ^g preserve the selected prime and induce the stated local σ_g.

A finite family of rational K-classes can be multiplied by one common nonzero integer to yield actual classes. Further antisymmetrization by 1−σ_{−1} is integral and kills the residue because σ_{−1} acts trivially there. The common integer and the fixed factorial multiply all relevant regulator values by the same nonzero rational scalar. For n≥6, this scalar may be divisible by 5; that does not destroy a Q5-linear independence statement. It may postpone detection to higher coefficient levels, but does not invalidate the compatible inverse-limit construction.

Huber–Kings Example 2.2.4 and Propositions 2.2.7, 2.2.9, 2.3.4 identify the relevant point syntomic coordinate, compatibly with Chern classes, with the Bloch–Kato exponential to H¹(E,Q5(n)). The exponential is an isomorphism for every n>1; their Introduction and §1.3 state this for arbitrary finite E/Qp, including ramified E:
https://arxiv.org/pdf/math/0612611

Therefore the independent e3 projections of the syntomic regulator values remain independent after the étale comparison. The map just constructed factors these values through completed K-theory. Via the AMMN point coordinate, any Q5-linear relation among the e3(b_j) would produce the same relation among the étale Chern images, which is impossible. One does not need the AMMN scalar and the syntomic scalar to be numerically equal.

## Verdict

The all-weight finite-Chern factorization used in Propositions 2.2 and Lemma 9.1 is valid under the manuscript's stated finite local-field hypotheses. None of the following is being assumed: source Mittag–Leffler, actual-to-completed injectivity, surjectivity onto the completed vector space, a finite bound n<p, or a direct identification of AMMN and polylogarithm coordinates. The target H⁰ Mittag–Leffler argument is sufficient and applies exactly as written.
