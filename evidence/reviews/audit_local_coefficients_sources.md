# Actual local K3 coefficients: primary-source closure

Date: 2026-10-07. This is an independent mathematical/source audit of the long manuscript's Lemmas 12.3, 12.19, and 13.10. It is not a proof-assistant certificate or an independent Danus acceptance record. Source locations and exact consequences are separated from deductions below.

## Result

The requested primary references match the hypotheses needed in the manuscript, including p=2. The former source-access gaps for Levine's constants theorem and Hesselholt–Madsen / Rognes–Weibel are now closed. The source statements do not imply surjectivity of actual K3 onto a rational completed group; the manuscript instead needs density of actual classes and finite-dimensional spanning, and the stated argument supplies these.

The only useful precision amendment is to spell out how the field finite-coefficient statements imply finiteness for the valuation ring, and how the completed statement of Rognes–Weibel implies finite-coefficient finiteness. A more direct p=2 citation is their Theorem 1.15(a). A second, independent proof of the conclusion of Lemma 13.10 avoids both local all-degree computations and is supplied in `work/local_point_spanning_alternative.tex`.

## A. Levine: original statements and hypotheses

Primary source: Marc Levine, *The indecomposable K3 of fields*, Ann. Sci. ÉNS (4)22 (1989), 255–344. Stable PDF: https://www.numdam.org/item/10.24033/asens.1585.pdf . Downloaded as `work/dim3_sources/levine_full.pdf` and extracted to `.txt`. Published pp.335–336 were also visually inspected; renderings are `levine_p335.png` and `levine_p336.png`. The earlier incomplete download `levine.pdf` is superseded by this complete copy.

- Theorem 4.12, published p.335 (PDF p.82), identifies the finite-coefficient **indecomposable** K3 with H1(E,mu_{ell^n}^{tensor2}). Its scope is a field E and ell distinct from char(E). The proof reduces to adjoining roots of unity; containing those roots is not a hypothesis in the conclusion. The ordinary field here has characteristic zero, so ell=p, including ell=2, is allowed.
- Theorem 4.13, published p.336 (PDF p.83), second assertion, states that the inclusion of the field of constants E0 into E induces K3(E0)^ind/ell^n ≅ K3(E)^ind/ell^n. It does not require E to be finitely generated in that assertion: its first words quantify over a field, and its proof uses the preceding general-field result. We use this finite-quotient assertion; no interchange of a continuous-cohomology limit with a field colimit is needed.
- To avoid any ambiguity about the definition of the finite-coefficient indecomposable quotient, Weibel's *Étale Chern classes at the prime 2*, §5, published p.24, explicitly writes the exact sequence K3^M(E)→K3(E;Z/q)→H1(E,mu_q^{tensor2})→0 for every q invertible in E, crediting Levine and Merkurjev–Suslin. That is exactly the form needed in 12.3. Author's PDF: https://sites.math.rutgers.edu/~weibel/archive/papers-dir/chernclass.pdf .

This source does **not** identify the ordinary quotient K3(E)^ind/ell^n with finite-coefficient K3(E;Z/ell^n)^ind before accounting for K2 torsion. The manuscript correctly supplies that accounting separately.

## B. K2 torsion and Milnor K3 divisibility

Weibel, *The K-book*, Chapter III, Theorem 6.2.4 (Moore's theorem), explicitly gives K2(E)=U⊕mu(E), where U is uniquely divisible and mu(E) is finite cyclic, for a local field. Its proof distinguishes Moore's divisibility and Merkurjev's characteristic-zero torsion-freeness. Example 6.2.5 includes Q2. The inspected source is `work/sources/weibel_III.txt`, lines 2531–2542, obtained by the main audit from the author's chapter, https://sites.math.rutgers.edu/~weibel/Kbook/Kbook.III.pdf .

Chapter III, Exercise 7.4, lines 3725–3732, explicitly states that Milnor K_n(E) is divisible for n≥3 for a complete discretely valued field with finite residue field. The supplied hint proves the needed n=3 case from the norm-residue pairing and Moore's theorem; the text even records a stronger unique-divisibility theorem, which is unnecessary here.

For completeness, the mod-ell argument in that hint is as follows. If mu_ell is absent, K2(E)/ell=0. If it is present, K2(E)/ell is one-dimensional and the Hilbert pairing on E^*/E^{*ell} is nondegenerate. Given a triple, either its last two entries already pair to zero, or choose a nonzero b' orthogonal to the last entry and choose a' pairing with b' to reproduce the first two entries' K2 class. The triple is then zero mod ell. The orthogonal hyperplane contains a nonzero vector because the local Kummer space has dimension at least two. Iterating divisibility by p gives divisibility by every p^nu.

In particular, K2(E)[p^nu] has uniformly bounded exponent. Its coefficient-transition maps are multiplication by p, so the resulting inverse system is pro-zero and its inverse limit, the p-adic Tate module, is zero. This remains true at p=2.

## C. Complete proof chain for Lemma 12.3

Let G=K3(E), E/Qp finite.

1. Milnor K3(E) is p-divisible, so its map to K3(E;Z/p^nu), which factors through G/p^nu G, is zero. The Levine–Weibel exact sequence therefore identifies K3(E;Z/p^nu) naturally with H1(E,mu_{p^nu}^{tensor2}). The finite-coefficient Chern map is additive in K-degree three, also at p=2 (Weibel Proposition 2.4), and compatible with coefficient reduction (Proposition 2.8).
2. The coefficient exact sequence is 0→G/p^nu→K3(E;Z/p^nu)→K2(E)[p^nu]→0. The right transition is multiplication by p. By B its limit is zero, and hence the limit of the middle groups equals lim G/p^nu. In fact no further lim1 term is needed for this equality; left-exactness of inverse limit and vanishing of the right limit suffice for the surjectivity onto the middle limit.
3. H0(E,mu_{p^nu}^{tensor2}) is finite, so its inverse system satisfies Mittag–Leffler. The continuous cohomology coefficient sequence identifies lim H1(E,mu_{p^nu}^{tensor2}) with H1(E,Zp(2)). This is a finitely generated Zp-module by local Galois cohomology.
4. G is dense in its p-adic quotient completion: a basic open condition is a class in some G/p^nu, which by definition lifts to G. Consequently the rational Chern images span H1(E,Qp(2)). Indeed every Qp-linear subspace of that finite-dimensional target is closed.
5. Quillen localization gives K3(O_E)→K3(E)→K2(k_E); the last group is zero by Quillen's finite-field computation. Thus actual integral classes lift. This is localization for a DVR, not an appeal to the new Gersten claim.
6. The Bloch–Kato exponential in twist two is a natural isomorphism E→H1(E,Qp(2)), as checked separately in Huber–Kings. For a quadratic extension E/F, apply 1−sigma to actual lifts; their values span E^−, of dimension [F:Qp]. No division by two is made in integral K-theory.

Thus the actual-class spanning statement, including its Galois-equivariant form, follows for every p.

## D. Complete proof chain for Lemma 12.19

Let W0 be the arithmetic DVR in the manuscript, H=Frac(W0^h), and K=Frac(W0-hat).

1. H is henselian, dense in K, algebraic over the number field Frac(W0), and has the same completion. A henselian rank-one valued field is separably algebraically closed in its completion: approximate a separable root closely enough to apply Hensel, and separate its finitely many conjugates to force equality with the root supplied by Hensel. Since the characteristic is zero, all algebraic roots are separable.
2. Therefore H is exactly the subfield of K algebraic over Q. This is the field of constants of K in Levine 4.13. That theorem gives K3(H)^ind/p^nu ≅ K3(K)^ind/p^nu.
3. Milnor K3(K) is p-divisible, so its image in K3(K) is contained in p^nu K3(K); consequently K3(K)^ind/p^nu=K3(K)/p^nu. The quotient map from actual K3(H) onto its indecomposable quotient is surjective, giving K3(H)→K3(K)/p^nu surjective.
4. W0^h is a noetherian DVR with finite residue field. Its localization sequence has zero K2 of that residue field, so every element of K3(H) lifts to actual K3(W0^h).
5. The image is therefore dense in the same inverse-limit lattice as in C. Its rational Chern values span H1(K,Qp(2)).

No rigidity theorem with residual prime inverted is being incorrectly applied at ell=p. The argument uses a characteristic-zero field theorem with p invertible in that field.

## E. Hesselholt–Madsen: what Theorem A supplies

Primary source: Hesselholt–Madsen, *On the K-theory of local fields*, author PDF https://math.mit.edu/~larsh/papers/010/annals.pdf ; saved as `work/dim3_sources/hm.pdf` and `.txt`. The accessed author's version has 96 pages; Theorem A is on its PDF p.2. Avoid transplanting its PDF pagination into the published 113-page article.

The introduction fixes a complete mixed-characteristic discrete valuation field with **perfect residue field of odd characteristic**. Theorem A treats every positive K-degree and every p-power coefficient. It states odd K_{2s−1} as H1 with twist s, and even K_{2s} as H0 with twist s plus H2 with twist s+1. The introduction expressly says that roots of unity need not lie in the field for this conclusion. Thus finite E/Qp, arbitrary ramification, and p>2 are covered.

For finite E/Qp the Galois cohomology groups on the right are finite. This gives the finite-coefficient finiteness used in 13.10, including K4 needed for the Milnor lim1 term. To pass from E to O_E, use the coefficient localization sequence and K_j(k_E;Z/p^nu)=0 for j>0. Hence K_j(O_E;Z/p^nu)→K_j(E;Z/p^nu) is an isomorphism for j≥2. This one-line deduction should be stated explicitly beside the citation.

Only finiteness is needed here. No identification of the Hesselholt–Madsen isomorphism with the AMMN point-coordinate normalization is asserted or required.

## F. Rognes–Weibel: p=2 and the finite-coefficient inference

Primary source: Rognes–Weibel, *Two-primary algebraic K-theory of rings of integers in number fields*, JAMS13 (2000), 1–54, author PDF https://sites.math.rutgers.edu/~weibel/archive/papers-dir/RognesWeibel.pdf ; saved as `work/dim3_sources/rw.pdf` and `.txt`.

Theorem 3.7, published/PDF p.19, explicitly covers **any finite extension E/Q2**, with its ring of integers. It computes the completed groups in every nonnegative degree; in degrees ≥2 they are finite cyclic in even degree and a finite cyclic group plus Z2^[E:Q2] in odd degree. No unramified, root-of-unity, or low-weight restriction is imposed.

The citation is valid for finite-coefficient finiteness, but that fact is a consequence rather than the theorem's literal statement. There are two precise deductions:

- A connective spectrum and its derived p-completion have the same mod-p^nu cofiber. The coefficient exact sequence applied to the completed groups makes each finite-coefficient group an extension of two finite groups, since the adjacent completed homotopy groups in Theorem 3.7 are finitely generated Z2-modules.
- More directly, Theorem 1.15(a), pp.10–11, explicitly computes the mod-2 K-groups of any p-local characteristic-zero field: odd degrees give E*/E*² and positive even degrees give an extension of H0 by H2. For the finite E/Q2 used here these groups are finite. The cofiber coefficient sequence for 2^nu, 2^{nu+1}, and 2 gives finiteness for all nu by induction. Coefficient localization then transfers it to O_E in degrees ≥2. This route avoids any potential ambiguity in the word “completed”.

Thus the finite K4(O_E;Z/2^nu) groups satisfy Mittag–Leffler and have vanishing lim1. The degree-three point completion is finitely generated as claimed in 13.10.

## G. Full density chain for Lemma 13.10

For G=K3(O_E), use 0→G/p^nu→K3(O_E;Z/p^nu)→K2(O_E)[p^nu]→0. The actual injection K2(O_E)→K2(E) follows from localization and K2(k_E)=0. Thus B makes the right-hand system pro-zero. E and F make the finite-coefficient groups finite, including K4; hence the homotopy-limit exact sequence gives

π3 K(O_E)^hat_p = lim K3(O_E;Z/p^nu) = lim G/p^nu.

Finite generation at p=2 follows from RW3.7. At odd p it also follows by the local H1 description (or the all-prime Levine route C). Actual G is dense in this lattice. The AMMN point comparison identifies its rationalization with E, so the actual point-character values span E. The anti-invariant conclusion follows by 1−sigma as in C.

This proves the exact density statement used in the manuscript; actual-to-completed surjectivity is neither asserted nor needed.

## H. Independent spanning proof and absence of a dependency cycle

The conclusion of 13.10 has the following shorter alternative, even if one chooses not to use E/F:

- C establishes Lemma 12.3 from Levine, Milnor divisibility, Moore–Merkurjev, localization, and Bloch–Kato.
- Lemma 13.20 constructs a Qp-linear factor of actual Chern classes through V=π3 K(O_E;Qp), using only finite-coefficient Chern additivity/compatibility, the canonical πholim→limπ map, and the H0 coefficient lim1 calculation. Its proof calls neither 13.10 nor any point-coefficient cup theorem.
- AMMN at a point gives dim_Qp V=[E:Qp], without any assertion about the actual image.
- Bloch–Kato gives dim_Qp H1(E,Qp(2))=[E:Qp]. By 12.3 the image of actual classes under the composite spans H1. Therefore the factor V→H1 is a surjection between equal finite dimensions, hence an isomorphism, and actual classes span V.

This graph is acyclic. The proof does not identify the AMMN regulator with the old syntomic regulator, even up to a scalar. It uses only a natural factor and dimension. The TeX version is `work/local_point_spanning_alternative.tex`.

## Cross-audit status

The main coordinator reports that the original three-adic short theorem, including its AMMN module-compatible character and logarithmic unit formula, has been accepted in Danus record `59cdde297e2a4505` with no assumptions and empty reported error/gap lists. This source-audit report records that coordinator-provided status; it does not itself create or certify the record, and it does not promote unrelated long-manuscript extensions to verified status. The essentially smooth extension 13.26 is undergoing a separate gate.
