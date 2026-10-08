---
fact_id: 7aedefba09125cf6
problem_id: gersten-package-audit
author: xhigh2
predecessors: []
glossary_introduces:
  E: The local field Q_5(rho).
  F: The depleted dilogarithm Li_2(z)−5^(-2)Li_2(z^5) within this proof.
  G: The group (Z/5Z)^×.
  L_mod,n: The modified Coleman polylogarithm in Besser–de Jeu's syntomic formula.
  Li_2: Coleman's dilogarithm normalized by its series at zero.
  S_j: The integral rational function (z d/dz)^j(1/(1-z)).
  W_E: The complete DVR Z_5[rho].
  W_ar: The arithmetic DVR Z_(5)[rho].
  b: The point coordinate r_E(beta|_(W_E)).
  beta: The actual antisymmetrization (1−sigma_(-1))beta_0.
  beta_0: An actual lift of an integer multiple of beta_rat.
  beta_rat: The rational special-unit K_3 class associated with [−rho]_2.
  c_(2,1): The etale Chern class from K_3 to H^1 with twist two.
  e_r: The rational 5-adic character projector (1/4)sum_g omega(g)^(-r)sigma_g, for r=1,3.
  mathcalK: Spectral 5-completion of K-theory followed by inversion of 5.
  mu_(5^n): The Galois module of 5^n-th roots of unity.
  omega: The Teichmuller character G→Z_5^× in this arithmetic coefficient fact.
  pi: The uniformizer rho−1.
  r_E: The natural AMMN point coordinate on actual K_3(W_E) after rationalized spectral completion.
  rho: A primitive fifth root of unity.
  sigma_g: The automorphism rho↦rho^g.
  tau_r: The Gauss sum sum_g omega(g)^(-r)rho^g.
external_refs: [{"key": "BdJ2003", "authors": ["Amnon Besser", "Rob de Jeu"], "title": "The syntomic regulator for the K-theory of fields", "arxiv": "math/0110334", "year": 2003, "cited_for": "Theorems 1.6 and 1.10, Remark 1.7: special-unit symbol and regulator formula; source downloaded and definitions/proof read."}, {"key": "BdJ2008", "authors": ["Amnon Besser", "Rob de Jeu"], "title": "Li^(p)-service? An algorithm for computing p-adic polylogarithms", "year": 2008, "cited_for": "Theorem 2.7(3): depleted polylogarithm is analytic away from the specified small disc; DOI 10.1090/S0025-5718-07-02027-3; source downloaded and read."}, {"key": "HuberKings2006", "authors": ["Annette Huber", "Guido Kings"], "title": "A p-adic analogue of the Borel regulator and the Bloch-Kato exponential map", "arxiv": "math/0612611", "year": 2006, "cited_for": "Example 2.2.4, Propositions 2.2.7,2.2.9,2.3.4 and §1.3: ramified-field syntomic-to-etale comparison and exponential isomorphism."}, {"key": "WeibelChern", "authors": ["Charles Weibel"], "title": "Etale Chern classes at the prime 2", "cited_for": "Proposition 2.1.1, Lemma 2.3, Propositions 2.4,2.8; source https://sites.math.rutgers.edu/~weibel/archive/papers-dir/chernclass.pdf downloaded and read."}, {"key": "AMMN2021", "authors": ["Benjamin Antieau", "Akhil Mathew", "Matthew Morrow", "Thomas Nikolaus"], "title": "On the Beilinson fiber square", "arxiv": "2003.12541", "year": 2021, "cited_for": "Theorem A, Proposition 4.10 and Corollary 3.8, point case."}, {"key": "Quillen1972", "authors": ["Daniel Quillen"], "title": "On the cohomology and K-theory of the general linear groups over a finite field", "year": 1972, "cited_for": "Finite-field K-groups, giving zero positive rationalized 5-completed residue groups."}]
---

## statement
An actual cyclotomic K_3 coefficient with both odd point-character components nonzero. Fix a primitive fifth root of unity rho, set W_ar=Z_(5)[rho], W_E=Z_5[rho], E=Q_5(rho), and pi=rho−1. For g in G=(Z/5Z)^× let sigma_g(rho)=rho^g, and let omega:G→Z_5^× be the Teichmuller character. Let mathcalK(T)=K(T)^wedge_5[1/5]. Define r_E:K_3(W_E)→E by passage to pi_3 mathcalK(W_E), the canonical inverse of pi_3 mathcalK(W_E,(pi))→pi_3 mathcalK(W_E), and the AMMN relative point equivalence with HC_2^cts(W_E/W_E;Q_5)=E. For r=1,3 write e_r=(1/4)sum_(g in G)omega(g)^(-r)sigma_g, acting only on Q_5-vector-space targets. There is an actual beta in K_3(W_ar) of the form beta=(1−sigma_(-1))beta_0 such that its reduction in K_3(F_5) is zero, sigma_(-1)beta=−beta integrally, and b=r_E(beta|_(W_E)) satisfies e_1b≠0 and e_3b≠0. No Q_5-linear projector is applied to an actual rational K-group.

## proof
1. An explicit local nonvanishing calculation. Put tau_r=sum_(g=1)^4 omega(g)^(-r)rho^g. Its pi-adic valuation is r for r=1,3. Indeed expand rho^g=(1+pi)^g. The coefficient of pi^j is sum_g omega(g)^(-r) binom(g,j). For j<r its reduction modulo 5 is zero: binom(g,j) is a polynomial of degree j in g, and the power sums on F_5^× vanish for exponents not divisible by 4. For j=r the leading coefficient gives 4/r! modulo 5, nonzero. The terms j<r therefore have valuation at least 4+j>r, while terms j>r have valuation at least j>r, since pi^4 is a unit multiple of 5. The unique term of lowest valuation is the j=r term.

Let Li_2 be the Coleman dilogarithm normalized by sum_(m>=1)z^m/m^2 on the open unit disc. Define S_j(z)=(z d/dz)^j(1/(1-z)), a rational function in Z[z,(1-z)^(-1)], and
 F(z)=Li_2(z)−5^(-2)Li_2(z^5).
On the open unit disc, partitioning indices prime to 5 as a+5m, with 1<=a<=4 and m>=0, and expanding their inverse squares gives
 F(z)=sum_(j>=0)(-1)^j(j+1)5^j S_j(z^5) sum_(a=1)^4 z^a/a^(j+2).
The right side converges uniformly on the affinoid |z|<=1, |1-z^5|=1, because the S_j have integral coefficients and unit denominators there and the norm of the j-th term is at most 5^(-j). This affinoid is connected: its reduction is the integral curve Spec F_5[z,(1-z)^(-1)], and its defining integral affinoid algebra has no nontrivial idempotent. Theorem 2.7(3) of Besser–de Jeu, Li^(p)-service? An algorithm for computing p-adic polylogarithms (Math. Comp. 77 (2008)), states that Li_n(z)−p^(-n)Li_n(z^p) is represented by a convergent series in 1/(1-z) outside the closed disc |z−1|<=p^(-1/(p−1)). This contains our affinoid for p=5. Thus both sides are rigid analytic there; equality on the open disc extends by the identity principle. This argument uses the exact primary theorem, not numerical evaluation of a Coleman function.

At z=−rho, one has z^5=−1, and |1-z^5|=1. The term Li_2(−1) is fixed by every sigma_g, hence is killed by e_1 and e_3. Permuting g gives
 e_r(rho^a)=(omega(a)^r/4)tau_r.
Consequently
 4 e_r Li_2(−rho)/tau_r
 =sum_(j>=0)(-1)^j(j+1)5^j S_j(−1) sum_(a=1)^4 (-1)^a omega(a)^r/a^(j+2).
Each S_j(−1) is 5-integral. The terms j>=1 vanish modulo 5; the j=0 term is
 (1/2)sum_(a=1)^4(-1)^a a^(r−2).
For r=1 this equals (1/2)(−1+3−2+4)=2 in F_5; for r=3 it equals (1/2)(−1+2−3+4)=1. Thus e_r Li_2(−rho) is nonzero for both r. Division by tau_r is legitimate by its valuation calculation, and no precision is lost because the displayed projection identity is exact.

2. The actual arithmetic symbol. We spell out the external regulator statement and its hypotheses. In Besser–de Jeu, The syntomic regulator for the K-theory of fields, arXiv:math/0110334, Theorem 1.10(1)–(2), if F_0 is a number field and O_0 its integer ring localized at a nonzero prime, there is a natural rational K-theory map from their special-unit symbol complex; in degree one and weight n, the syntomic regulator under an embedding into a p-adic field is [x]_n↦±(n−1)!L_mod,n(x). A special unit means x and 1−x both belong to O_0^×. The sign is the single convention in Remark 1.7. In weight two no conjectural vanishing assumption is needed, also by their Theorem 1.6.

Take F_0=Q(rho), O_0=W_ar, n=2, x=−rho. Both x and 1−x=1+rho are units because 1+rho reduces to 2 modulo pi. The symbol [−rho]_2 is a degree-one cocycle in the rational special-unit complex: its differential is (1+rho) tensor (−rho), or its exterior version, and the second factor is a root of unity, hence zero after rationalization. Its image gives a rational class beta_rat in K_3(W_ar)⊗Q. Its local syntomic regulator is ±L_mod,2(−rho)=±Li_2(−rho), because every modification term contains log(−rho)=0. Choose a positive integer N clearing its denominator and an actual beta_0 in K_3(W_ar) representing N beta_rat. Set beta=(1−sigma_(-1))beta_0. This is an exact operation on actual groups. Its reduction is zero because sigma_(-1) acts as the identity on W_ar/pi=F_5, and its antisymmetry is integral. The syntomic regulator is equivariant, so its two odd character components are twice the corresponding components for beta_0. They are nonzero by step 1.

3. Passage through finite-coefficient Chern classes. Huber–Kings, A p-adic analogue of the Borel regulator and the Bloch–Kato exponential map, arXiv:math/0612611, §2 (which explicitly imposes no ramification restriction), supplies the following comparison. For the ring of integers of a finite p-adic field E and n>1, its syntomic degree-one coordinate is E (Example 2.2.4); it agrees with Besser's definition (Proposition 2.2.7), and the Chern-compatible map to H^1(E,Q_p(n)) is the Bloch–Kato exponential (Propositions 2.2.9 and 2.3.4). The exponential is an isomorphism for n>1, as recalled in §1.3. These maps are natural under field automorphisms. Apply them with our possibly ramified E=Q_5(rho), n=2. It follows that the ordinary etale Chern image c_(2,1)(beta) in H^1(E,Q_5(2)) has both odd projections nonzero.

There is a natural G-equivariant Q_5-linear map
 pi_3 mathcalK(W_E)→H^1(E,Q_5(2))
through which the Chern class of an actual element factors. Here is an explicit construction avoiding any surjectivity of actual K-theory onto its completion. First map to pi_3 K(E)^wedge_5; its canonical maps to all finite-coefficient spectra give a map to lim_n K_3(E;Z/5^n). At every level apply Soule's Chern class into H^1(E,mu_(5^n)^(tensor2)). Charles Weibel, Etale Chern classes at the prime 2, Proposition 2.1.1, Lemma 2.3, Proposition 2.4 and Proposition 2.8 state respectively naturality, compatibility of the integral Chern class with reduction, additivity for odd coefficients, and compatibility with coefficient transitions. Thus these maps form a compatible additive system and recover the actual Chern class. Each finite target is killed by 5^n, which makes the induced map Z_5-linear. Moreover the H^0(E,mu_(5^n)^(tensor2)) groups are finite, so their inverse system is Mittag–Leffler. The continuous-cohomology inverse-limit exact sequence therefore identifies lim_n H^1 with H^1(E,Z_5(2)). Invert 5 to obtain the displayed map. No vanishing of a derived inverse limit on the K-theory side is needed.

4. The point coordinate and its character projections. Quillen's finite-field calculation gives K_(2j)(F_5)=0 and K_(2j−1)(F_5)=Z/(5^j−1) for j>=1. Hence all positive homotopy groups of K(F_5)^wedge_5 vanish; this follows also levelwise from the finite-coefficient exact sequences since multiplication by 5 is invertible on these positive groups. In particular pi_3 and pi_4 of mathcalK(F_5) vanish. The relative fiber sequence consequently makes pi_3 mathcalK(W_E,(pi))→pi_3 mathcalK(W_E) an isomorphism.

The point case of the AMMN relative fiber square (On the Beilinson fiber square, arXiv:2003.12541, Theorem A and Proposition 4.10) identifies pi_3 mathcalK(W_E,(pi)) with HC_2^cts(W_E/W_E;Q_5)=E. Its hypotheses hold: W_E is a complete mixed-characteristic DVR with perfect finite residue field, its formal spectrum is smooth over itself, and changing the ideal (5) to (pi) only changes the special fiber by a nilpotent thickening, covered by their Corollary 3.8. The construction is natural for automorphisms of the coefficient point, so this isomorphism is G-equivariant. Compose its inverse with the Chern map in step 3. This is a G-equivariant Q_5-linear map from E to H^1(E,Q_5(2)) carrying b=r_E(beta) to c_(2,1)(beta). If e_r b were zero, its Chern image in that character would be zero, contradicting step 3. Thus e_1b and e_3b are both nonzero. Equivariance also gives sigma_(-1)b=−b.

This proof needs no equality of a chosen syntomic scalar normalization with the AMMN coordinate. It uses only an equivariant comparison out of the completed group, while the coefficient beta itself remains an actual class.

## intuition
An exact dilogarithm depletion identity detects both odd local character components of one rational cyclotomic symbol. Clearing denominators and antisymmetrizing preserves an actual arithmetic class, and finite Chern classes transfer the nonvanishing to its AMMN coordinate.
