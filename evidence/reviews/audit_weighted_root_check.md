# 二维完备稿 Proposition 7.1 的独立加权根检查

对象：work/package/gersten_dimension_two_research_manuscript.tex，第 1273–1335 行，Proposition 7.1 / prop:dimtwoWeightedNonzero。范围限于既有算术 coefficient、形式替换、tame trace、bounded elliptic contraction 和 scalar-Frobenius persistence 之间的这一个接口。本次不重复整篇完备稿，也不改变 Danus 状态。

结论：未发现确切失败。角色确实是 e_3，四根总系数确实是 4εℓ(ω)，有限常数扩张不会引入新的 primitive 来消灭已检测到的向量。论证没有暗用整个 root Picard lattice 张量 Q_5 后单射。

## 1. 输入逐项对应

| 此命题需要的输入 | 稿件出处 | 本接口实际使用的部分 |
|---|---:|---|
| 实际 coefficient 的 b∈E，σ_−1(b)=−b，e_3(b)≠0 | 273–340 | 只在 regulator 目标施加 Q_5-idempotent；不在 actual rational K_3 内制造 idempotent 分量。 |
| root label 保持为 g | 849–898 | 形式替换固定 V′，把 J_g 的 Picard 类送到 (X,Y−[g])，不交换 g 与 g^−1。 |
| 非常值 Q 与准确 root equivariance | 486–524 | h(P_g)=[g^−1]Q；至少一个固定 h 给出非挠、非常值 Q。 |
| trace 与 line norm 相容 | 803–835 | Tr(c_1 L)=c_1 Nm(L)，且是有界严格链映射。 |
| 固定 bounded functional ℓ 与 total de Rham contraction | 637–727 | ℓ(ω)≠0、ℓ(η)=0，且 exact 二形式送到 actual exact 一形式。 |
| Poincaré mixed-class computation | 745–773 | 对 Γ_R−Γ_−R，输出 ±2ℓ(ω)R^*η，共同符号不依赖 R。 |
| Q^*η 在 ordinary generic-Cohen quotient 非零 | 775–800、544–610 | scalar-Frobenius lemma 应用于非零 proper unit-root pullback；不用 Hausdorff 商替代 ordinary 商。 |

对 bounded functional 存在及 scalar-Frobenius lemma 的外部 crystalline 输入，本轮采用主审计已核的命题；这里逐项验证其假设如何吻合当前向量，不声称重新证明那些外部比较定理。

## 2. CM、Galois 与 e_3 的方向

取 i∈Z_5，i²=−1，i≡2 mod 5。在 E_0:v²=z³+z 上

\[
[i](z,v)=(-z,iv),\qquad [i]^*(dz/v)=i\,dz/v.
\]

因此 holomorphic line 的角色是 i。proper H^1 的交错配对在度一 automorphism [i] 下不变，另一条线的角色必须是 i^−1=−i。

此处需要确定后一条线是 unit-root line，而不能只凭“另一条线”命名。直接计数 E_0(F_5) 有四点：三个仿射点 (0,0)、(2,0)、(3,0)，加原点 O。因此 Frobenius 特征多项式为 X²−2X+5。CM Frobenius 是 1+2[i]：其微分 1+2i 在特征 5 为零；1−2[i] 的微分为单位，因而是另一条、可分的 degree-five endomorphism。两个特征值为

\[
1+2i\in5\mathbf Z_5,\qquad 1-2i\in\mathbf Z_5^\times.
\]

故 proper unit-root generator η 满足 [i]^*η=−iη，准确角色为 χ_0=ω^3；dual slope-one generator ω 的角色为 i。这与稿件 1279–1284 和 789–792 一致。

另一方面，原几何旋转 (X,Y,Z)↦(iX,iY,Z) 给 w=Z/Y↦−iw，经两个 elliptic quotient 的显式公式都变成目标上的 [−i]。因此 h(P_i)=[−i]Q。于是

\[
(h(P_i))^*\eta=Q^*[-i]^*\eta=iQ^*\eta,
\]

不是 −iQ^*η。一般而言其权重是 χ_0(g)^−1。这正是 e_3 的权重 ω(g)^−3，而不是 e_1 的权重。

以上涉及两个不同的作用：σ_g 是 arithmetic coefficient E=Q_5(ρ) 的 Galois 作用；[g] 是常值 elliptic curve 的 CM automorphism。将二者配对的是 root label g 与等式 h(P_g)=[g^−1]Q；证明没有把两个作用当成同一个作用。形式替换也不必与所有 σ_g 等变，只需分别保持每个 root Picard 类并固定 W′，这正是 863–898 行的结论。

## 3. 从四个 root 到精确系数 4ε

令 c_g=σ_g(b)。由 σ_−1(b)=−b 得 c_−g=−c_g。根理想 J_g 对应 O(−P_g)，所以

\[
\gamma_g=-c_1(J_g)=c_1\mathcal O(P_g).
\]

选择对置对的代表 {1,i}，有

\[
\Xi=c_1(\gamma_1-\gamma_{-1})
      +c_i(\gamma_i-\gamma_{-i}).
\]

此式中的 c_1 是标量 σ_1(b)=b，不是 Chern 操作符。为避免记号混淆，也可直接写 b(γ_1−γ_−1)+σ_2(b)(γ_2−γ_3)。

对每个 root section，norm divisor 的 pushforward 系数为 1：该 section 到其 image graph 的 residue function-field degree 为 1。h 是 degree 2 不会在这里再次乘 2。ramification 的 multiplicity 在 h^*Nm 的等式中出现，不能再加到 pushforward 的每个 rational section 上。

因此 tame trace 把 γ_g−γ_−g 送到

\[
c_1\mathcal O(\Gamma_{[g^{-1}]Q}-\Gamma_{-[g^{-1}]Q}).
\]

Poincaré mixed term 是同一个 ε∈{±1} 下的

\[
2\varepsilon\left(\omega\otimes
       ([g^{-1}]Q)^*\eta-\eta\otimes([g^{-1}]Q)^*\omega\right).
\]

固定 ℓ 杀死 η，故每个对置差输出

\[
2\varepsilon\ell(\omega)\chi_0(g)^{-1}Q^*\eta.
\]

由于 χ_0(−1)=−1，χ_0(−g)^−1c_−g=χ_0(g)^−1c_g；把两个代表的和写回全部四个 g，准确得到

\[
(L\circ\operatorname{Tr})(\Xi)
 =\varepsilon\ell(\omega)
   \sum_{g\in\mathbf F_5^\times}\chi_0(g)^{-1}\sigma_g(b)\,Q^*\eta
 =4\varepsilon\ell(\omega)e_3(b)\,Q^*\eta.
\]

一个可直接排除反号的四项检查是 ω(1)=1、ω(2)=i、ω(3)=−i、ω(4)=−1：

\[
4e_3(b)=b+i\sigma_2(b)-i\sigma_3(b)-\sigma_4(b)
       =2\bigl(b+i\sigma_2(b)\bigr).
\]

若错用 e_1，则会得到 2(b−iσ_2(b))，与 P_i↦[−i]Q 的 pullback 不符。实际系数 4ε 既没有缺失对置差的 2，也没有重复加入 trace degree 2。η 与 ω 被选为 dual generators，故 Poincaré coefficient 的归一化自由只留下共同符号；ℓ 的额外缩放已经包含于 ℓ(ω)。

## 4. 有界泛函与有限常数扩张

记 K=W(k)[1/5]、K′=K(ρ)，W′=W(k)[ρ]。K′/K 有限，W′/W 有限自由；5-adic 与 π-adic 拓扑等价。把 ℓ 乘一个非零常数使之 integral 后，其每个有限精度的映射

\[
\Omega^1_{\widehat A/W}/5^\nu\longrightarrow W/5^\nu
\]

可先张量 W′/5^ν，再取逆极限。由于 W′ 是有限自由模，这与原 completed tensor construction 相容，给出有界 K′-线性泛函 ℓ′。因此 σ_g(b)∈K′ 可以从 trace 与 contraction 中作为常数提出。

这里 de Rham complex 的基环也从 W 改成 W′，所以不产生 dρ 项；相应 continuous differential complexes 是原复形的有限常数基变换。每个 g 的 σ_g 可扩张为固定 K 的 K′-automorphism，且 ℓ 来自 K，故其基变换与这些常数 automorphisms 相容。不过加权计算只需 K′-线性，甚至不依赖额外等变性断言。

对于任意 K-线性复形 V^•，有限 field extension 给出

\[
H^j(V^\bullet\otimes_K K')
 \simeq H^j(V^\bullet)\otimes_K K'.
\]

这是 exact flat scalar extension，不涉及闭包。也可选 K-basis of K′：若扩张后的向量有 primitive，逐个基系数就给出扩张前的 primitive。有限维常数基变换与这里的 completion 可交换，因此适用于稿件的 ordinary continuous de Rham 商。它不是一般的“无限 completed tensor product 与 cohomology 可交换”断言。

所以 Q^*η 的已知非零类在扩张后仍非零；ℓ(ω) 和 e_3(b) 都是 K′ 中非零元素，乘积不能把它消灭。

## 5. ordinary quotient 与 root-lattice 依赖检查

ℓ 在 elliptic 因子上因 boundedness 必须杀掉 exact forms 的闭包，这确实同时杀掉 proper unit-root η；证明因此特意让 ℓ 检测 dual slope-one ω。剩下的 Q^*η 位于参数因子，它不是再送入 Hausdorff 商，而是保留在

\[
\Omega^1_{C/W}[1/5]/d(C[1/5]).
\]

其非零性需要 scalar-Frobenius lemma。Q 非常值，故 proper pullback η 非零；有限字段下降后 multiplier 是 (1−2i)^d∈Z_5^×，满足该引理的 integral scalar 假设。稿件所用向量与引理假设完全匹配。若擅自把最后这个商换成除去闭包的商，论证就会失败；当前稿件没有这样做。

反证只需一条链：假设 Xi 为 actual exact 二形式；形式替换、bounded tame trace、bounded contraction 都把它送到 actual exact 一形式；但后者的 ordinary cohomology 类已经计算为非零的 4εℓ(ω)e_3(b)Q^*η，矛盾。

这条链只依赖一个精确角色分量。root Picard lattice 的整系数独立性在更早的几何步骤用来保证某个 h 的 Q 非挠；在此处没有将整系数独立性升级成 Q_5 系数线性独立性。尤其无需证明四个 γ_g 在 completed de Rham target 中只有 diagonal relation，也无需证明其 entire anti-part 的 Q_5-rank 为 2。

审计状态：本有界接口通过独立交叉检查；无需修改命题或系数。可将四项恒等式 4e_3(b)=2(b+iσ_2(b)) 添加为读者自检，但不是缺失假设的修补。
