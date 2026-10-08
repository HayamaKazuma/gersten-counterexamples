# 完备 node 的 dagger cup 注入：原文接口审计

审计对象：长稿 `gersten_quadric_research_manuscript.tex`，Lemma 12.1（1349–1428 行）、perfect-residue 扩展 Lemma 12.21（2598–2673 行），及高阶系数的 2973–2985 行。状态：独立数学审计，未写入 Danus 真值库，不是形式化证明证书。

结论：这一比较接口可以闭合。固定半径上的 scheme/rigid 比较、系数逆极限与 dagger 半径余极限的次序、权重三的临界项、topological heart 到普通上同调的过渡均有适用的原文依据。没有发现有限域、无分歧或 p≠2 的遗漏假设。建议补出一个实际 noetherian integral model，并单独列出 P¹ 的代数—解析 torsion 比较，使读者无需补认这两步。

## 1. 实际读过的来源

1. [Achinger, *Wild ramification and K(π,1) spaces*](https://arxiv.org/pdf/1701.03197)，§6.1–6.2，特别 Theorem 6.2.1，印刷页 19–20。它记录 Fujiwara Corollary 6.6.3 的 Gabber–Fujiwara 定理。假设是 **noetherian henselian pair (A,I)**，并比较 `Spec A \ V(I)` 与 `Spf(Â)^rig`；系数是任意 torsion abelian sheaf，包含 p-primary。§6.4 同时说明 rigid 与关联 adic 的 étale topoi 对应。
2. [Colmez–Nizioł, arXiv:1905.04721v2](https://arxiv.org/pdf/1905.04721v2)，原文的 Theorem 1.3 / 7.9、§3.1.1、§3.2.1–3.2.3、§5.1–5.2、Propositions 5.5、5.6、5.9、§7.2.4。下文缩写 CN。
3. [Berkovich, *Étale cohomology for non-Archimedean analytic spaces*](https://www.numdam.org/article/PMIHES_1993__78__5_0.pdf)，Theorem 6.1.1（印刷页 110）：代数曲线的 torsion compact-support cohomology 与解析化相同；在 proper 曲线 P¹ 上就是通常 cohomology。此定理的陈述没有 prime-to-residue-characteristic 限制。

下载记录：`work/cn1905.pdf/.txt`、`work/achinger1701.pdf/.txt`、`work/berkovich_etale1993.pdf/.txt`。本审计核对这些原文的定理和相关定义，未重证其深层比较定理。

## 2. 一个固定半径容纳全部 formal series，并有明确的 integral model

记 `W=O_E`，`0≠d∈m_W`。原稿任取 `1<ρ<|d|^{-1}` 是可行的；为消除“rational radius 的模型是什么”的隐含步骤，可固定

\[
 \rho=|d|^{-1/2}\in\sqrt{|E^\times|}.
\]

考虑 π-adically complete noetherian W-algebra

\[
 A_\rho=
 W\langle a,b,c,u,v,z\rangle/
 (a^2-du,\ b^2-dv,\ c^2-dz,\ ab+c(c+d)).
\]

若要求 flat formal model，可再除以其 W-torsion；这个操作不改变 generic fiber。把 `X=a/d,Y=b/d,Z=c/d` 代入，其 generic affinoid 由

\[
 XY+Z(Z+1)=0,\qquad
 |dX|,|dY|,|dZ|\le1,\qquad
 |dX^2|,|dY^2|,|dZ^2|\le1
\]

定义，后面三个条件已经给出 `|X|,|Y|,|Z|≤ρ`，故它正是原稿的 `U_ρ`。这也说明不必把 E 扩大来实现 ρ。

更强的是，这个模型直接接受积分 formal ring 的映射：在 `A_ρ` 中 `a²,b²,c²∈dA_ρ`，所以 `(a,b,c)` 的幂次趋于零。任意 `W[[x,y,w]]` 中的 formal series 都可在同一 π-adic ring 内代入 `(a,b,c)`；总次数至少 `6N` 的每个 monomial 都有某一指数至少 `2N`，故在 `d^N A_ρ` 中。关系恰好给出

\[
 W[[x,y,w]]/(xy+w(w+d))\longrightarrow A_\rho.
\]

反转 d 后得到原稿 1382 行所需的 ring map。等价的 Banach 估计为第 n 次齐次项的范数至多 `(|d|ρ)^n`。因此无需为每个 formal series 单独选择半径，也无需把此 formal ring 偷换成 Tate algebra。

## 3. Gabber–Fujiwara 的确在正确位置使用

将 Achinger 6.2.1 用于 `(A_ρ,(π))`：A_ρ 完备 noetherian，故此 pair henselian；`Spec A_ρ[1/π]=Spec O(U_ρ)`。这个 theorem 给所有有限系数的自然 quasi-isomorphism

\[
 R\Gamma_{\mathrm{et}}(\operatorname{Spec}O(U_\rho),\mu_{p^\nu}^{\otimes r})
 \simeq R\Gamma_{\mathrm{et}}(U_\rho,\mu_{p^\nu}^{\otimes r}).
\]

接在 `Spec O(U_ρ)→T_d` 的 scheme pullback 后即可。**该定理不直接应用于 m-adic formal local ring 的整个位形**；原稿先到固定 affinoid 模型的做法是正确的，也避免 generic fiber 类型混淆。

pullback 由同一个 topos morphism 给出，故兼容 coefficient transition、cup product 和 Kummer Chern class。目标 characteristic 0，μ_{p^ν} 是 étale sheaf；原文也并未要求 p 在积分模型中可逆。

## 4. 两个极限的次序恰好是 CN 定义

令 `U_{ρ_h}` 为 `ρ_h↓1`、`ρ_h≤ρ` 的共尾呈现。它们是 U_ρ 内的 rational neighborhoods，给标准 dagger algebra 的 presentation；CN Definition 3.2 与 Example 3.3 就描述这种情形。

比较映射的次序是

\[
\begin{aligned}
 &\bigl(R\varprojlim_\nu R\Gamma_{\mathrm{et}}(T_d,\mathbf Z/p^\nu(r))\bigr)[1/p]\
 &\quad\longrightarrow
 \bigl(R\varprojlim_\nu R\Gamma_{\mathrm{et}}(U_\rho,\mathbf Z/p^\nu(r))\bigr)[1/p]\
 &\quad\simeq R\Gamma_{\mathrm{proet}}(U_\rho,\mathbf Q_p(r))\
 &\quad\longrightarrow
 \operatorname*{hocolim}_h R\Gamma_{\mathrm{proet}}(U_{\rho_h},\mathbf Q_p(r))
 =R\Gamma_{\mathrm{proet}}(U^\dagger,\mathbf Q_p(r)).
\end{aligned}
\]

CN §3.2.3，公式 (3.11)，明确先在每个 qc affinoid 上取 `holim_ν`，再取 presentation 的 `hocolim_h`。同节给 qc rigid affinoid 的 continuous étale/pro-étale strict quasi-isomorphism。

原稿没有使用一般不合法的 `holim hocolim ≅ hocolim holim`，也没有假设 dagger étale→dagger pro-étale 的反向比较。它只从一个固定呈现对象映到 homotopy colimit。全程使用 derived inverse limit，故不需要证明 T_d 或 U_ρ 的 `lim¹=0`。

## 5. Ruling 的几何计算与临界项

积分 unit quadric `XY+Z(Z+1)=0` 是 smooth：special fiber 若 X=Y=0，则 Z=0 或−1，故导数 `2Z+1` 是 unit，p=2 也如此。理想 `(X,Z)` 在包含它的点上由 X 生成，因为 `Z+1` 可逆；其他点上是单位理想。因此其两全局生成元给 weak formal ruling。

unit dagger 上 ruling 的两张 closed-disc 逆像是

\[
 (X,t)\mapsto(X,-t(1+Xt),Xt),\qquad
 (s,Y)\mapsto(-s(1+sY),Y,-1-sY).
\]

两张都是 dagger bidisc，交是 dagger unit annulus × disc，过渡为 `s=t^{-1}`, `Y=−t−Xt²`。逐项积分时除以整数只产生次指数增长，因此任意略小的 overconvergence radius 仍可用。交上的唯一正次数 cohomology 由 `dlog t` 给出。有限 Čech 复形遂给

\[
 H^2_{dR}(U^\dagger)=E\,[d\log t],\quad H^3_{dR}(U^\dagger)=0,
 \quad f^*:H^2_{dR}(\mathbf P^1_E)\simeq H^2_{dR}(U^\dagger).
\]

这是同一 ruling 的 pullback，不能仅用两边维数等于一代替最后一条。

CN 的式 (5.4) 及紧随其后的 strict quasi-isomorphism 对 **semistable weak formal model** 给

\[
 R\Gamma_{HK}(\mathfrak X_0)\otimes_{F_0}E\simeq R\Gamma_{dR}(\mathfrak X_E).
\]

这里 unit quadric model 是 smooth，从而 semistable；P¹ model 也适用。CN Proposition 5.5 将模型 HK 与 dagger HK 比较，5.6 给有限维性／classical 性。这些映射对 ruling 自然。因为 E/F_0 是忠实的域扩张，可推出

\[
 f^*:H^2_{HK}(\mathbf P^1_E)\simeq H^2_{HK}(U^\dagger),\qquad
 H^3_{HK}(U^\dagger)=0.
\]

前者是 slope-one line `F_0 h`，`φ(ah)=pσ(a)h`、`N=0`。若 `φ(ah)=p²ah` 且 a≠0，取 valuation 给 `1+v(a)=2+v(a)`，矛盾。

因此 CN Theorem 1.3(2) / Proposition 5.9(2) 在 r=3 时夹住的两项

\[
 H^2_{HK}(U^\dagger)^{\varphi=p^2},\qquad
 H^3_{HK}(U^\dagger)^{N=0,\varphi=p^3}
\]

均为零。其第一长正合列实际给出 **同构**

\[
 H^2_{dR}(U^\dagger)\simeq
 \widetilde H^3_{\mathrm{proet}}(U^\dagger,\mathbf Q_p(3)),
\]

因为 surface 上 F³=0。同一事实在 P¹ 成立。不能只写 Theorem 1.3 的一般 injectivity 后就不加说明地忘掉拓扑；原稿用 HK vanishing 强化为同构，正好关闭了这个风险。

## 6. 普通上同调、P¹ 与 Chern cup

CN §3.1.1 明写 classical-part functor C 满足 `C(tilde H^i)=H^i`。任何 functor 都保同构；所以对上面的同构应用 C，得到普通 cohomology 的同构。这里无需假设 C 保持一般单射。CN §5.1 还给出源 de Rham cohomology 的 classical 性。

P¹ 的 proper dagger/rigid pro-étale 比较由 CN §7.2.4 给出。另需将原稿的 **scheme** P¹ 连到 analytic P¹：Berkovich Theorem 6.1.1 对所有 torsion sheaves 已足够，因为 P¹ proper；逐 ν 比较，再 derived inverse limit/invert p，即得所需 continuous comparison。该映射兼容 pullback 和 Kummer Chern classes。

有限 E/Q_p 时 projective-bundle formula 和 `cd_p(E)=2` 给

\[
 H^3_{\mathrm{cont,et}}(\mathbf P^1_E,\mathbf Q_p(3))
 =H^1(E,\mathbf Q_p(2))\,c_1(O(1)).
\]

所有映射均由同一 `(x,w)` quotient line bundle、同一 ruling 拉回。故经过 T_d 的 cup map 再到 dagger 的复合，正是上述 P¹ pullback 同构在此直和项的限制。复合单射，所需 cup map 单射。

## 7. Perfect residue 与更高权重

CN 开篇允许任意 mixed-characteristic complete DVR with perfect residue field，而非仅有限 residue。上述 A_ρ 仍 noetherian；两图 de Rham 计算相同；CN 5.5–5.6 的有限维 HK 与 strict comparison 不需 k 有限。只有 5.6(4) 的 Weil-weight 陈述额外需要 k 有限，这里没有调用它。排除 `φ=p²` 用 valuation，不需要 σ 有有限阶。

因此 Lemma 12.21 的 perfect-residue 扩展也适用。最后一步仅需 projective-bundle **split injection**，不必宣称整个 H³(P¹) 只有一个直和项。

对 n≥3，目标 twist r=n+1，degree i=3 满足 `i≤r−1`，可直接用 CN Theorem 1.3(1) / 7.9(1) 的 stable-range 同构；n=2 是上面已单独消去 HK 项的 borderline 情形。不存在把 stable range 错用到 n=2 的问题。

## 8. AMMN 是否可以替代

长稿 Proposition 13.11 `directtccoefficientcup`（4183 行起）用 AMMN 与 continuous cyclic de Rham class 检测 `β(1−[J])`，可以为这些实际 K 类的非零性／线性独立性提供不经过 dagger étale cup 的另一条证明。

但 AMMN 本身不直接给本 Lemma 12.1 所声称的 **任意 étale H¹ 系数的 H³ cup 注入**。不能从 K 类非零直接倒推其 étale Chern 像非零。要把直接 AMMN 路线作为同一个 étale 结论的替代，仍须加入合适的 Chern/TC/étale 比较及相应 injectivity；本报告没有偷补这个推论。鉴于上述 dagger 接口已经闭合，无须增加这条额外依赖。

## 建议在原稿保留的两处补充

- 1384 行附近给出一个 A_ρ 的模型，或至少明确“取 ρ=|d|^{-1/2}，以 a²=du 等方程构造 complete noetherian integral model”，使 Gabber–Fujiwara 的 henselian-pair 条件可直接检查。
- 1427 行附近将“proper étale/pro-étale”与“scheme P¹/analytic P¹”两种比较分开引用；后一种补 Berkovich 6.1.1 或其 proper comparison 后继版本。

这两项是使论证自足且引用可追溯的补充；本次原文核查没有留下该 cup 注入的未解决数学接口。
