# 长稿多对数来源接口审计

审计对象：work/package/gersten_quadric_research_manuscript.tex 的引理 12.7、12.9、12.15，命题 12.16，引理 12.27，命题 12.28、12.31、13.4，并核对高阶 cyclotomic class 所需的 BDJ Theorem 1.12。本记录是独立数学审计，不是 Danus 验证状态，也不是形式化证明。本轮核查原始公式、假设和解析应用范围；原稿的有限代数估值和群表示独立性推导已有独立审计，本轮没有重复全部计算。

结论：本轮列出的多对数来源接口可以闭合，没有发现需要撤回这些分支的文献假设冲突。尤其没有被遗漏的奇素数条件或权重小于素数条件。两个必须保留的区分是：普通 Coleman Li_n 与 depleted 函数的解析区域不同；BDJ 的规范化 regulator 值是 Li_n，而不是擅自替换为 depleted Li_n。

## 1. 已实际读取的原始文献

1. A. Besser–R. de Jeu, *Li^(p)-service? An algorithm for computing p-adic polylogarithms*, Math. Comp. 77 (2008), 1105–1134。大学机构库提供出版版 PDF：https://research.vu.nl/ws/portalfiles/portal/2459860/220267.pdf 。本地 work/bdj_algorithm_2008.pdf / .txt。核对 pp.1106–1113，特别是 Definition 2.1、Remark 2.2、Theorem 2.7、Proposition 2.10、Eq. (3.3)、Proposition 4.4、Remark 5.7。PDF 首张为机构封面，印刷页 1108 对应 PDF 第 5 张。
2. A. Besser–R. de Jeu, *The syntomic regulator for the K-theory of fields*, Ann. Sci. ENS 36 (2003), 867–924：https://www.numdam.org/article/ASENS_2003_4_36_6_867_0.pdf 。本地 work/dim3_sources/bdj.pdf / .txt。核对 pp.867–872、875–876、910，特别是 Eq. (1.2)、Remark 1.7、Theorems 1.10/1.12、Remark 1.13、Remark 2.3、Eq. (2.4)，以及 Theorem 1.12 的实际证明。
3. A. Besser–R. de Jeu, *The syntomic regulator for K_4 of curves*, Pacific J. Math. 260 (2012), 305–380：https://msp.org/pjm/2012/260-2/pjm-v260-n2-p03-p.pdf 。本地 work/bdj_curves_2012.pdf / .txt。核对 p.307 Eq. (1.8)、p.308 和 p.377。后者明确记载修正二重对数的反射、反演公式；无需把复二重对数的常数项移植进 p-adic 公式。

## 2. 来源提供的准确范围

Algorithm 从任意素数 p 和 C_p 开始。Theorem 2.7 对任意固定 logarithm branch、所有整数 n≥0 成立。其结论同时区分：

- Li_n 在 0 处是零常数幂级数；在非 1、∞ 的剩余圆盘上刚性解析，并满足 dLi_n=Li_(n−1) dz/z。
- F_(p,n)(z)=Li_n(z)−p^(−n)Li_n(z^p) 在 |1−z|>p^(−1/(p−1)) 上有 1/(1−z) 的收敛幂级数。这一部分甚至独立于 logarithm branch。
- Eq. (3.3) 仅先在 |z|<1 上给出 F_(p,n)=Σ_(p∤a) z^a/a^n。把它用于 |z|=1 的单位根需要额外证明解析延拓后所用的重排级数确实收敛；原稿确实给出了这个步骤。

Proposition 2.10 的分布关系为

\[
\operatorname{Li}_n(z^m)
 =m^{n-1}\sum_{\xi^m=1}\operatorname{Li}_n(\xi z),
\]

其中 m≥1；没有 (m,p)=1 假设。在 z^m≠1 时可直接应用；n≥2 时利用 Remark 5.7 的连续赋值，也可扩至 z^m=1。当前各关键应用的 z^m 均不等于 1，因而不必调用这一额外延伸。反演为

\[
\operatorname{Li}_n(z)+(-1)^n\operatorname{Li}_n(z^{-1})
 =-\log^n(z)/n!.
\]

因此在非零单位根处，Li_n 的反演符号为 (−1)^(n+1)。固定 log p=0 后，BDJ 2003 Remark 2.3 给出 Q_p-Galois 等变性。高权重造成 n! 或 (n−1)! 可被 p 整除，只影响非零有理常数及其估值，不限制这些等式的适用性。

Curves 的 D=L_mod,2=Li_2+(1/2)log(z)log(1−z) 满足 D(1−z)=−D(z) 与 D(z^−1)=−D(z)。这些是 Coleman 函数恒等式，p=2 也适用。若 z=ρ 是单位根，logρ=0；在 1−ρ 端，修正项同样包含 logρ，故

\[
\operatorname{Li}_2(\rho)
 =-\operatorname{Li}_2(1-\rho).
\]

当 ρ 是非平凡 p-power 单位根时 |1−ρ|<1，右侧才可用普通零点幂级数。

## 3. 重排级数在单位根处的合法性

这一步不是对引文的复述，而是对原稿延拓论证的独立补足。所有正整数 n≥1 和 j≥0，

\[
F_{p,n}(z)=\sum_{j\ge0}(-1)^j
 \binom{n+j-1}{j}p^j
 \left(\sum_{a=1}^{p-1}\frac{z^a}{a^{n+j}}\right)S_j(z^p),
\qquad S_j(t)=\frac{P_j(t)}{(1-t)^{j+1}},
\]

首先在 |z|<1 成立：将分母写成 a+ph，展开 (1+ph/a)^−n；|ph/a|≤p^−1，所以分母展开一致收敛，而 |z|<1 保证对 h 的级数收敛，允许交换两重求和。P_j∈Z[t]，S_0=1/(1−t)，对应 h=0 时约定 h^0=1。

取有理数 0<b<1。设

\[
\mathcal A_b=\{|z|\le1,\ v_p(1-z^p)\le b\}.
\]

在此域，第 j 项估值至少 j−(j+1)b，趋于正无穷；binomial coefficient 是整数，所以对任意高权重 n 都有同一收敛下界。

还需证明原稿所写 annulus 真正等于这个域。令 t=v_p(1−z)≥0。若 t≥1/p，则展开 1−z^p 的每一项估值均≥1，不属于此域。若 t<1/p，则 (1−z)^p 项的估值 pt 严格低于所有其他项，故 v_p(1−z^p)=pt。因此

\[
\mathcal A_b=\{p^{-b/p}\le|1-z|\le1\}.
\]

必要时有限扩充系数域，使有理半径属于值群；这是连通闭刚性环域。又 b/p<1/(p−1)，故它严格包含于 Algorithm Theorem 2.7(3) 的解析区域。重排级数在该环域上给出刚性解析函数，与 F_(p,n) 在非空开集 |z|<1 上相等；刚性恒等原理于是给出整个环域上的等式。

b=2/3 足以覆盖原稿每一个实际使用重排级数的点：

- p 奇、r≥2、z=ρ_r 时，v_p(1−z^p)=1/(p^(r−2)(p−1))≤1/2。
- p=2、r≥3、z=ρ_r 时，上述估值为 2^(−(r−2))≤1/2。
- 奇素数 r=1 的基值计算使用 z=ξρ_1，ξ∈μ_(p−1)\{1}；此时 1−z^p=1−ξ 是单位，估值为 0。
- p=2 的 i 基值计算使用 z=ζ_3 i、ζ_3² i；此时 1−z²=1+ζ_3² 或 1+ζ_3，是单位，估值为 0。

最后两条尤其重要：并未把 ρ_1 或 i 直接代入一个尚未证明在该点收敛的重排式。

## 4. 逐条对应稿件

| 长稿结果 | TeX 行号 | 来源接口结论 |
|---|---:|---|
| Lemma 12.7，p=2 的 Li_2(i) | 1602–1640 | Curves p.307/p.377 的 D 反射成立；q=1−i 满足 |q|<1。两端修正项因 log i=0 消失；BDJ Remark 2.3 与 (1.2) 保证商 Li_2(i)/i∈Q_2。 |
| Lemma 12.9，奇素数 cyclotomic Li_2 | 1719–1756 | 同一反射把问题搬到 |1−ρ|<1；普通幂级数合法。BDJ (2.4) 的 m=2 分布系数是 1/2，故 Li_2(−ρ)=(σ_2/2−1)Li_2(ρ)，符号与原稿一致。 |
| Lemma 12.15，depleted valuations | 2129–2201 | Algorithm Theorem 2.7(3) 与 (3.3) 正确匹配；上节补足 uniform convergence、环域和恒等原理，含 p=2。 |
| Proposition 12.16，wild orbit | 2203–2292 | 分布关系允许 m=p。对 r≥2（奇 p）、r≥3（p=2），p 个共轭恰为 μ_p·ρ_r，故 Tr(R_r)=p^(1−n)R_(r−1)，average trace 为 p^−n R_(r−1)。n=2 正是稿件的系数。 |
| Lemma 12.27，所有偶权重 i 基值 | 2988–3031 | m=3 分布与偶权重反演给 D_n=−(1+3^(1−n))Li_n(i)；−ζ_3 和 −ζ_3² 互逆，所以它们的 Li_n 和为零。depleted 展开在两个 twists 上合法，无 p>n 假设。 |
| Proposition 12.28，2-adic 高阶 wild augmentation | 3033–3098 | 任意 n 的上述重排式成立；反演符号为 (−1)^(n+1)，average trace 为 2^−n R_(s−1)，两者与稿件一致。 |
| Proposition 12.31，奇素数高阶 wild vector | 3193–3343 | base 的 tame twists 全落在非奇异区域；m=p−1 分布和偶权重反演给出正确的 −(1+(p−1)^(1−n)) 因子。higher-level depleted 与 trace 系数均正确。 |
| Proposition 13.4，pairwise endpoint | 3764–3845 | 下一节核验其普通 Li_2 的圆盘解析性、p=2 的下降与端点分布公式；均可闭合。 |

这里只关闭来源及解析应用接口；估值精确主项、character leading term、normal basis 的独立性推导属于稿件自身证明，不是 Algorithm 文献直接提供的结论。

## 5. Proposition 13.4 的解析函数与 endpoint

在 test ring 中 u=a−dZ，d=a′−a，且 |d|<1。选取 1<R<|d|^−1；在 |Z|≤R 上 u 仍落在 a 的剩余圆盘内，并且是单位。对任意正整数 k，(a−dZ)^k−a^k 的系数由 binomial 整数和正次 d 组成，所以在这个半径上仍具有绝对值<1。缩小 R（仍保留 R>1）即可同时处理一次有限线性关系中的全部 k。

奇 p 时 a 是 primitive 2p^r 根、k 奇且 p∤k，故 a^k 的剩余值是 −1≠0,1。Algorithm Theorem 2.7(1) 及 Proposition 4.4 在该圆盘给出刚性解析 Li_2，合成 u^k 后在 |Z|≤R 收敛。由 dLi_2(z)=−log(1−z) dz/z，

\[
F_k=-\frac nk\operatorname{Li}_2(u^k)+C,
\qquad dF_k=n\log(1-u^k)\,du/u.
\]

p=2 时，u^k 的剩余值为 1，这一步不能直接宣称 Li_2(u^k) 刚性解析。稿件改用

\[
S_k(u)=\operatorname{Li}_2(\zeta_3u^k)
       +\operatorname{Li}_2(\zeta_3^2u^k).
\]

两项分别落在 ζ_3 和 ζ_3² 的非奇异剩余圆盘，均在某个 R>1 的 Z 圆盘上解析。两项之和受 unramified quadratic Galois 作用固定；BDJ Remark 2.3 保证其系数下降至 E。由于固定的 p-adic logarithm 是乘法群到加法群的同态，

\[
dS_k=-k\log((1-\zeta_3u^k)(1-\zeta_3^2u^k))\,du/u
     =-k\log(1+u^k+u^{2k})\,du/u.
\]

故 F_k=−(n/k)S_k+C 正是所需 primitive。m=3 分布在 endpoints 给出

\[
S_k(a)=\tfrac13\operatorname{Li}_2(a^{3k})
       -\operatorname{Li}_2(a^k)=D_k(a).
\]

a 的阶是 2^r≥4，k 奇，所以 a^(3k)≠1，应用甚至不涉及 Li_2(1) 的连续赋值。乘入 symbol 前面的 k 后，primitive 的 1/k 消去；留下共同因子 n（再乘 relative-lift 的 m），不会出现依赖 k 的隐藏归一化。

反演把每一个 D_k(a) 变为 −D_k(a)，因为所有参数仍是单位根，log 项为零。因此 endpoint 检测若先得到 Σq_k D_k(a) 与 a 无关，再用 a↦a^−1 确实得到该常值为零。

以上核查没有宣称整个 formal test ring 的相对 Chern character 比较也由 Algorithm 自动给出；那是另一接口。本轮只核实它所调用的函数、primitive、下降与 endpoint identities。

## 6. 高权重 actual cyclotomic class 的文献范围

BDJ 2003 Theorem 1.12 适用于数域 F、非零素位处局部化 O 和嵌入到完备混合特征赋值域 K；相应的剩余域假设在有限 E/Q_p 情形自动满足。它计算数域符号类经 O、O_E 到规范化 syntomic regulator 的值为 ±(n−1)!L_mod,n(ρ)。数域情形不要求尚未证明的 Beilinson–Soulé 猜想；n≥2 不受 p 限制。Remark 1.7 说明符号选择只依赖 n 和 cohomological degree，因而固定一次 convention 后对所有 roots/embeddings 使用同一个系数。

Theorem 1.12 的 p.910 证明实际处理 p-power 单位根：先扩张添加阶数 prime to p 的单位根，用分布关系把非 special-unit 符号写成 special-unit 符号的组合，再利用有限基扩张兼容性下降。不是把 Theorem 1.10 的 special-unit 假设省略掉。原稿 2948–2951 行的引用在这一点正确。

单位根处 logρ=0，故 L_mod,n(ρ)=Li_n(ρ)。Remark 1.13 特意区分 Gros 的 depleted normalization 与本论文的规范化；其联系不能被解释成在 ramified E 上任意指定 Frobenius(z)=z^p。本稿的 higher-coefficient lemma 使用普通 Li_n，再把 depleted difference 用于证明独立性，这两步没有混淆。至于从这一 syntomic 数值到 Chern-compatible Bloch–Kato exponential 的比较，本轮不重新审核，维持由其他独立审计负责。

## 7. 最小编辑建议与状态

没有必须修正的数学来源错误。可把第 3 节的环域等式及严格不等式 b/p<1/(p−1) 缩成两句插入原稿第一次出现 depleted 展开的地方，此后高权重引用同一引理；可在 13.4 的“converge beyond the closed Z-disc”后增加 1<R<|d|^−1 的说明。这两处是补全已成立的推理，不改变定理。

状态：本任务列出的 Coleman/BDJ 来源接口全部关闭；它们不单独等价于完整 Gersten 反例已形式化，也不替代 regulator 与实际 K 类之间其余比较接口的审查。
