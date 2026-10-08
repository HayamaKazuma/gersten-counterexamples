# Explicit triple: a local Deligne-product bridge for lines 1482–1509

Status: mathematical audit/reconstruction, not a formal or Danus certificate. The global exact sign still has to be matched to the chosen Chern-character and cycle orientation conventions. Nonvanishing only needs a common nonzero sign.

The manuscript should explain why its holomorphic two-form represents the regulator period; citing multiplicativity alone conceals this interface. The following supplies the missing local argument.

Let a matching sphere lie over a chord joining two distinct roots of Φ10. Choose a simply connected complex neighbourhood V of this chord which avoids 0 and 1. Then t and 1−t are units on the inverse image N of V, and 1−t admits a single-valued holomorphic logarithm f=Log(1−t) there. Thus the weight-one Deligne regulator of the unit is represented by the topologically trivial Deligne class a(±f), with the sign fixed by the cone convention.

Use the Deligne-product identity

    a(f) cup y = a(f R_hol(y)),

where y is a degree-two Deligne class of weight two and R_hol(y) is its holomorphic curvature. This identity follows immediately from the product on the truncated holomorphic Deligne complex R(p)→O→Ω¹→⋯→Ω^{p−1}; equivalently it is the usual product identity for differential characters. It shows that flat ambiguities in a differential refinement of y do not change this product. No global logarithm of X is required.

For δ=⟨X,VH(t)⟩, the curvature of its regulator is determined on the dense open X≠0 by the identity δ={X,t¹⁰} and the unit normalization:

    R_hol(reg δ)=10 dX/X ∧ dt/t.

It extends holomorphically across X=0 because 1−XVH=t¹⁰ and

    10 dX/X ∧ dt/t = −dX ∧ d(VH)/(1−XVH).

Both sides define the same global holomorphic two-form on N, by equality on the dense open. Consequently the period of reg([1−t]δ) on the sphere is represented, with the convention-dependent common sign, by

    10 Log(1−t) dX/X ∧ dt/t.

The form extends across both poles, so there are no omitted endpoint singularities. Parametrize the interior by t along the chord and X=sqrt(|Φ10(t)|)exp(iθ). The d(log sqrt(|Φ10|)) term is proportional to the chord parameter differential and disappears on wedging with dt. Integration over θ then reduces the period to a signed 20πi times the difference Li₂(t_j)−Li₂(t_i). At a root of unity the imaginary part of Li₂ is D_BW, since log|t_i|=log|t_j|=0. Taking the real part therefore gives a signed 20π times the Bloch–Wigner difference.

The line-bundle periods and Borel injectivity now determine the supported coefficients modulo their common diagonal, exactly as in the manuscript. This closes the conceptual curvature-versus-regulator interface for the nonvanishing assertion. To retain the numerical identity κ=−10Σβ_BT(t_g)η_g, the manuscript should explicitly declare the Deligne cone sign and sphere orientation used for both the regulator period and the Chern periods; otherwise write a common sign ε in that identity and in κ=ε(1/2)Σσ_g(β)η_g. The resulting infinite-order and Milnor conclusions are unchanged.
