---
fact_id: d8c925bb8cff43ee
problem_id: gersten-package-audit
author: xhigh2
predecessors: [868cb19bf6a0a52c, 50b9a29bc7dc842b]
glossary_introduces:
  Delta: The diagonal divisor on that product.
  Gamma_q: The graph divisor of a map q into the elliptic curve.
  K': A finite constant field extension of K.
  P: The normalized Poincare line bundle on mathcalE×mathcalE.
  Q: Its nonconstant special-fiber map U→E_0^circ.
  Qbar: The finite extension of Q to Ubar.
  Qtilde: The assumed W-morphism Spec D→mathcalE^circ.
  Tr: The normalized top-degree cohomological trace.
  Ubar: The smooth proper compactification of U.
  W': Its ring of integers.
  alpha: The unit root in Z_5 of X^2−2X+5.
  d: A positive integer such that U and Q descend to F_(5^d).
  gamma: The pulled-back proper unit-root cohomology class Q^*eta.
  m: The positive degree of Qbar, including inseparable degree.
  mathcalE: The smooth projective elliptic W-curve v^2=z^3+z.
  mathcalE_circ: The complement of O and (0,0) in mathcalE.
  mathcalL_Q: The line bundle of the difference of the graphs of Qtilde and -Qtilde, pulled to B.
external_refs: [{"key": "DLZ2011", "authors": ["Christopher Davis", "Andreas Langer", "Thomas Zink"], "title": "Overconvergent de Rham-Witt cohomology", "year": 2011, "cited_for": "Introduction p.198, existence of an integral Frobenius lift on the weak completion of a smooth affine W(k)-lift; published PDF downloaded and read. DOI 10.24033/asens.2143; Matlas retrieval attempted."}, {"key": "Berthelot1997Duality", "authors": ["Pierre Berthelot"], "title": "Dualite de Poincare et formule de Kunneth en cohomologie rigide", "year": 1997, "cited_for": "Sections 1–3: trace, Poincare duality and Kunneth, compatibility with proper crystalline cohomology. Author manuscript downloaded from https://wstein.org/people/berthelo/publis/Poincare_Kunneth.pdf and read."}]
---

## statement
Nonconstant elliptic graph divisors survive generic Cohen completion. Let k be an algebraic closure of F_5, W=W(k), K=W[1/5], and let mathcalE/W be the smooth elliptic curve v^2=z^3+z with origin O. Put mathcalE^circ=mathcalE\{O,(0,0)}, E_0=mathcalE⊗_W k, and A=Gamma(mathcalE^circ,O). Let D be a smooth affine W-algebra of relative dimension one with connected nonempty special fiber U=Spec(D/5D), and suppose a W-morphism Qtilde:Spec D→mathcalE^circ has nonconstant special fiber Q:U→E_0^circ. Let C be the 5-adic completion of D localized at the generic point of its special fiber, F=C[1/5], Ahat the 5-adic completion of A, and B=(Ahat⊗_W C)^wedge_5. Let mathcalL_Q be the pullback to Spec B of the line bundle O(Gamma_Qtilde−Gamma_(-Qtilde)) on mathcalE^circ×_W Spec D. Then c_1^dR(mathcalL_Q) is nonzero in Omega^2_(B/W)[1/5]/d Omega^1_(B/W)[1/5]. The forms are continuous and the quotient uses the ordinary image, not its closure. Nonvanishing persists after any finite extension of the constant field K, using the corresponding finite extension of W and continuous relative forms over that extension.

## proof
We first compute the finite-type Chern class and then apply the two accepted analytic facts.

1. Proper generators and a mixed Chern class. The elliptic curve E_0 is ordinary, as established in fact 50b9a29bc7dc842b. Its proper rational crystalline H^1 has a one-dimensional slope-zero space and a one-dimensional slope-one space. Its model is already defined over F_5. Choose a slope-zero generator eta over Q_5 and a slope-one generator omega over Q_5, and normalize them so that their proper cup pairing has trace one, with the order (eta,omega). Proper smooth crystalline/de Rham comparison for mathcalE identifies these with algebraic de Rham classes on mathcalE_K. Their restrictions to the affine curve mathcalE^circ_K can be represented by algebraic one-forms, still denoted eta and omega, since affine de Rham hypercohomology is computed by global forms. These forms also give dagger representatives and continuous representatives. Fact 50b9a29bc7dc842b applies to them.

Let P be the Poincare line bundle on mathcalE×mathcalE, normalized at the origin. Explicitly, with the principal polarization convention it is O(Delta−mathcalE×O−O×mathcalE), where Delta is the diagonal; choosing the opposite polarization changes all subsequent signs together and has no effect on nonvanishing. Its Chern class has only the mixed H^1⊗H^1 term. Indeed its restrictions to each origin slice are trivial, which kills the two pure degree-two terms in the proper Kunneth decomposition. The diagonal correspondence acts as the identity on H^1. With the stated dual basis its mixed tensor is
 omega⊗eta−eta⊗omega.
One can check this without a choice of coordinates: multiplying by the pullback of eta on the first factor and taking the trace on that factor returns eta on the second; doing the same with omega returns omega. The cup pairing is perfect, so these two evaluations determine the mixed tensor.

For an arbitrary map q to mathcalE, the graph line O(Gamma_q) is the pullback of O(Delta) by id×q. Hence the difference for q=Qtilde and q=−Qtilde is the difference of their pulled-back Poincare bundles: the first-factor O(O) cancels, and the second-factor contributions cancel since [-1]^*O(O)≅O(O). The inversion map acts by -1 on proper H^1. Consequently the Chern class of the graph difference on the affine product has representative
 2(omega∧Qtilde^*eta−eta∧Qtilde^*omega).
This equality first holds in algebraic de Rham cohomology of the finite-type affine product over K, by pullback of the proper diagonal identity. Thus the difference from any other de Rham Chern representative is the differential of an algebraic one-form on that affine product. It remains exact on passage to the dagger complex, to the generic localization, and to the completed continuous complex. No Kunneth formula for the completed algebra B is asserted.

The standard cohomological properties used in this step are the proper smooth comparison, perfect cup pairing, and Kunneth for proper curves. In rigid cohomology they are supplied by Pierre Berthelot, Dualite de Poincare et formule de Kunneth en cohomologie rigide (1997), §§1–3: its trace agrees with crystalline trace in the proper smooth case, and its duality and Kunneth morphisms are isomorphisms. In characteristic zero the same statements for mathcalE_K follow from proper algebraic de Rham cohomology. The diagonal calculation above makes the particular Chern class used here explicit.

2. The pulled-back unit-root class is nonzero in rigid H^1. Compactify U to its smooth proper connected curve Ubar. Properness of E_0 extends the nonconstant rational map Q uniquely to Qbar:Ubar→E_0. A nonconstant morphism of proper integral curves is finite surjective of a positive integer degree m, including its inseparable degree.

Here is the exact injectivity argument in rational crystalline, equivalently proper rigid, cohomology. Cup products in degree one are perfect, and pullback in top degree by Qbar multiplies the normalized trace by m. The top-degree assertion follows from the divisor class of a point: its pullback divisor has total degree m, with lengths counted, and the trace of a degree-one point class is one. Thus for any two degree-one classes a,b on E_0,
 Tr_Ubar(Qbar^*a∪Qbar^*b)=m Tr_E0(a∪b).
If Qbar^*a=0, then the left side vanishes for every b; the integer m is invertible in K, and perfectness forces a=0. This proves injectivity without a separability hypothesis. The trace and cycle compatibilities are those of Berthelot's §§1–2 cited in step 1.

Restriction from Ubar to U is injective in rigid H^1: in the Gysin sequence for the finite set Ubar\U the preceding term is its degree-minus-one cohomology, hence zero. Therefore gamma=Q^*eta is nonzero in H^1_rig(U/K). Functoriality of the comparison with dagger de Rham complexes identifies its representative with Qtilde^*eta.

3. Scalar Frobenius hypothesis and generic survival. All the finitely many coefficients of the special-fiber curve U and its map Q are algebraic over F_5. They belong to some finite field F_(5^d). The proper model of E_0 is over F_5. Frobenius on its slope-zero line has a unit eigenvalue alpha in Z_5. To see the coefficient-field assertion directly, the four F_5-points are O and the three points with v=0 at z=0,2,3; at z=1,4 the cubic takes a nonsquare value. Thus the Frobenius polynomial is X^2−2X+5, whose reduction has the two simple roots 0 and 2. Hensel lifting gives its two roots in Z_5, one of them a unit, denoted alpha. The slope-zero generator eta can therefore be chosen over Q_5 with Frobenius eigenvalue alpha.

The weak completion Ddagger admits an integral lift of absolute Frobenius, semilinear for Witt Frobenius on W. This is precisely the smooth-affine lifting statement recorded in Christopher Davis, Andreas Langer and Thomas Zink, Overconvergent de Rham-Witt cohomology, Ann. Sci. ENS 44 (2011), p.198: a smooth affine lift over W(k) has a noncanonical Frobenius lift on its weak completion. We use this statement only for D, which is smooth over W with perfect residue field k. Iterate the lift d times to obtain phi inducing the 5^d-th power map. Its action in rigid cohomology is the canonical Frobenius action and is independent of the chosen lift. Since Q descends to F_(5^d), functoriality gives phi^*[gamma]=alpha^d[gamma]. In the affine dagger de Rham complex this equality means, literally, that
 phi^*(Qtilde^*eta)−alpha^d Qtilde^*eta=dh
for a function h in Ddagger[1/5]. The multiplier alpha^d is in W. All hypotheses of accepted fact 868cb19bf6a0a52c therefore hold, and the image of gamma in Omega^1_(C/W)[1/5]/dF is nonzero.

4. Contraction and conclusion. Apply accepted fact 50b9a29bc7dc842b to the forms omega and eta and this ring C. It supplies the bounded functional with ell(omega)=1 and ell(eta)=0 and the degree-minus-one operator L on the completed product. The class computed in step 1 maps under L to 2[gamma]. This is nonzero by step 3. Because L sends exact two-forms to exact one-forms, c_1^dR(mathcalL_Q) could not have been exact. This proves the asserted nonvanishing using the ordinary image throughout.

Let K'/K be a finite extension with ring of integers W'. A finite module over a complete discrete valuation ring is complete, and W' is finite free over W. Consequently scalar extension to W' commutes with the adic limits defining B and its finite-projective continuous form modules. Relative continuous forms over W' identify with the old forms tensored with W'. After inverting 5, the resulting complexes are the original K-complex tensored with K'. Tensoring vector spaces with a field extension is exact and faithfully flat, so it commutes with kernels and ordinary images and preserves the nonzero cohomology class. This is the stated constant-extension conclusion.

## intuition
The graph difference has one mixed summand with a slope-one elliptic factor and a unit-root base factor. The bounded contraction isolates the latter, and scalar Frobenius prevents that base class from acquiring a primitive at the completed generic point.
