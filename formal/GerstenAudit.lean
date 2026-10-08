import Std

open Lean.Grind
namespace GerstenAudit

/-- Expansion of Phi_5(1+y). -/
theorem cyclotomic_five_expansion [CommRing R] (y : R) :
    1 + (1+y) + (1+y)^2 + (1+y)^3 + (1+y)^4 =
    5 + 10*y + 10*y^2 + 5*y^3 + y^4 := by grind

/-- The polynomial factorization underlying the dimension-two symbol. -/
theorem cyclotomic_ten_factorization [CommRing R] (t : R) :
    (t^4-t^3+t^2-t+1)*(t^5-1)*(t+1) = t^10-1 := by grind

/-- A relation in the defining quotient, not a sampled equality. -/
theorem dim2_symbol_relation [CommRing R] (x v t : R)
    (h : x*v + (t^4-t^3+t^2-t+1) = 0) :
    1-x*(v*((t^5-1)*(t+1))) = t^10 := by grind

theorem dim2_H_substitution [CommRing R] (y : R) :
    ((-1-y)^5-1)*((-1-y)+1) = y*((1+y)^5+1) := by grind

/-- The change of Dennis--Stein second argument preserves its unit condition. -/
theorem dim2_ds_relation [CommRing R] (x b q : R) (h : 1-x*b=q) :
    1-x*(1+(1-x)*b)=(1-x)*q := by grind

theorem dim3_ds_relation [CommRing R] (x t q : R) (h : 1+x*t=q) :
    1+x*(1+(1+x)*t)=(1+x)*q := by grind

/-- The quadratic arithmetic relation, with 2 explicitly invertible. -/
theorem dim3_quadratic_unit_relation [CommRing R] (x y z r : R)
    (hinv : 2*r=1) (h : 3+x*y+z^2=0) :
    ((1+z)*r)*(1-(1+z)*r) = 1+x*(y*r^2) := by grind

/-- The scaled map from the ramified local ring to the smooth formal quadric. -/
theorem dim3_scaling_relation [CommRing R] (u X Y Z : R)
    (hu : u^2+3=0) (hQ : X*Y+Z^2=1) :
    3+(u*X)*(u*Y)+(u*Z)^2=0 := by grind

/-- A repeated root forces the displayed discriminant to vanish. -/
theorem quartic_repeated_root_discriminant [CommRing R] (s T : R)
    (h0 : s^4+T*s+1=0) (h1 : 4*s^3+T=0) :
    256-27*T^4=0 := by grind

/-- Exact normalization of the scaled quartic equation before reduction. -/
theorem quartic_scaled_identity [CommRing R] (u e X Y T : R)
    (h : u^4*e=5) :
    5+10*(u*Y)+10*(u*Y)^2+5*(u*Y)^3+(u*Y)^4+(u*X)^4+T*(u*X)*(u*Y)^3
      = u^4*(X^4+Y^4+T*X*Y^3+e*(1+2*u*Y+2*u^2*Y^2+u^3*Y^3)) := by grind

#print axioms cyclotomic_five_expansion
#print axioms cyclotomic_ten_factorization
#print axioms dim2_symbol_relation
#print axioms dim2_H_substitution
#print axioms dim2_ds_relation
#print axioms dim3_ds_relation
#print axioms dim3_quadratic_unit_relation
#print axioms dim3_scaling_relation
#print axioms quartic_repeated_root_discriminant
#print axioms quartic_scaled_identity
end GerstenAudit

namespace GerstenAudit
/-- Uniform exponential bound for the even indices j=4+2n in the 3-adic tail. -/
theorem tail_exponential_bound_even (n : Nat) : 4*n+11 < 3^(n+3) := by
  induction n with
  | zero => decide
  | succ n ih =>
    calc
      4*(n+1)+11 < 3*(4*n+11) := by omega
      _ < 3*3^(n+3) := Nat.mul_lt_mul_of_pos_left ih (by decide)
      _ = 3^((n+1)+3) := by simp [Nat.pow_succ, Nat.mul_comm, Nat.add_assoc]

/-- Uniform exponential bound for the odd indices j=5+2n in the 3-adic tail. -/
theorem tail_exponential_bound_odd (n : Nat) : 4*n+13 < 3^(n+3) := by
  induction n with
  | zero => decide
  | succ n ih =>
    calc
      4*(n+1)+13 < 3*(4*n+13) := by omega
      _ < 3*3^(n+3) := Nat.mul_lt_mul_of_pos_left ih (by decide)
      _ = 3^((n+1)+3) := by simp [Nat.pow_succ, Nat.mul_comm, Nat.add_assoc]

#print axioms tail_exponential_bound_even
#print axioms tail_exponential_bound_odd
end GerstenAudit
