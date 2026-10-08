# 二维完备化路线独立审计

对象：`work/package/gersten_dimension_two_research_manuscript.tex`，2394 行。审计日期：2026-10-07。此文件记录独立数学审阅，不是形式化证明证书，也没有写入或替代 Danus fact graph / verifier 的判定。

## 结论与边界

通读了完整二维稿及核心原始文献。没有找到足以否定其主 Gysin 构造的确定数学错误。主路线刻意区分 ordinary image 与 closure、actual K 与 spectral p-completion、relative injection 与 localization injection，这三个最容易出错的接口在稿件中均被分别处理，没有发现把它们混用。

确认一处引用错配：2291–2295 行将 Bökstedt–Ottosen 的 Definition 2.1 / Remark 2.2 / Proposition 2.3 引为 mixed HKR map 的出处。这些条目实际讨论 cyclic complexes、shuffle products 和 HC− 模正合列，未陈述所需 HKR map。本审计已写出可直接插入的补证 `work/hkr_repair.tex`。在本文 D=2,3、p=5 的范围，规范化 mixed HKR 是积分 quasi-isomorphism；一般 D 的有界挠误差论证也可以成立，因 Ω 的无 p 挠性排除了 cone 的额外顶层 kernel。

显式三单位补充的 1482–1509 行需明确 curvature 与完整 Deligne regulator 的接口。原引用支持乘法和单位规范化，但没有直接陈述该 Dennis–Stein matching-sphere period 公式。本审计重建了局部 Deligne-product 补证 `work/explicit_regulator_repair.md`：在 chord 的单连通邻域选择 Log(1−t)，使用 a(f) cup y=a(f R_hol(y))，再由稠密开集上的 Dennis–Stein 恒等式确定曲率。因此非零性的机制可闭合；精确的共同符号 −10/−1/2 仍应由同一套 cone 与球面方向约定固定。共同符号不影响无限阶结论。该补充不影响独立的主 Gysin 类与高阶构造。

这里“通过独立审阅”仅表示本次逐步检查未发现失效推理，并且指定引用的适用条件已核对；没有把引用的深层定理重新证明，也没有将整个论证送入 Lean/Coq。需与主线程 Danus 结果合并后再决定哪些命题可以称 Danus-verified。

## 逐命题覆盖

| 编号 / 标签 | 行号 | 状态与核查内容 |
|---|---:|---|
| Thm 1.1 `dimensiontwoMain` | 93–111, 1335–1348 | 由 2.2、7.1、6.2 的依赖链给出；本次未检出主链致命缺口。actual c 及完成像无限阶由向 Q5 向量空间的非零像推出，不需要 actual K→completion 注入。 |
| Lem 2.1 `dimtwoDilogCharacters` | 200–271 | 展开、character reindexing、Gauss valuation 逐式检查一致。r=1,3 的模5首项分别为2,1。连接 affinoid 上的 depleted polylog continuation 是指明的解析输入。 |
| Prop 2.2 `dimtwoActualCoefficient` | 273–341 | special unit −ρ,1+ρ；BDJ number-field theorem 无 Beilinson–Soulé 假设；K2(F5)=0 允许提升；反对称化使 reduction 积分为0。Huber–Kings 的 ramified point syntomic/étale 比较适用。利用有限 Chern maps 只推断 AMMN coordinate 的 character 非零，无须将其认作同一具体 polylog 坐标。 |
| Lem 3.1 `quarticrootlattice` | 367–410 | D[1/X] 的 Laurent UFD 给四生成元、唯一对角关系；所有 T=t 纤维积分的四次 Kummer 判据成立，因为基含 μ4且 q(s) 非平方。垂直局部化仅去掉 principal divisors。 |
| Lem 3.2 `quarticconstantquotients` | 412–484 | z=w²/x、v±=w(x±r)/x 的方程、双覆盖 involutions、四个边界点的像及次数均一致。有限 étale radicals 均是单位且2,4可逆。E/F5 点数4，Frobenius trace2；Hasse系数2给 ordinary。 |
| Lem 3.3 `quarticnonconstantroot` | 486–527 | Klein四群 norm identity 给 isogeny；anti-root非挠迫使至少一个常椭圆商像非挠；k=Fbar5 的常点都是挠点，故Q非恒定。root rotation 的 [a^{-1}] 符号与 w=Z/Y 一致。 |
| Lem 4.1 `scalarFrobeniusCohen` | 544–615 | 核心 pole-order 论证成立：q m 与 ≤m 无法抵消。递归去π系数必须使用所有闭点、D0正规和 completed intersection，该稿已具备。常数域的完整补强见下节。Caro–D’Addezio 3.2.1 确实给 degree-one rigid→convergent 注入。 |
| Lem 5.1 `ellipticContinuousFunctional` | 637–665 | Caro–D’Addezio 7.2.1/7.3.1/7.3.6 对 ordinary proper slope lines 的用法一致。K=Frac W(Fbar5) 是完全离散赋值域，因此球完备；分离 Banach quotient 可用非阿基米德 Hahn–Banach。 |
| Lem 5.2 `ellipticCompletedTensor` | 677–728 | 先积分缩放后逐模5^ν张量，允许连续延拓。局部 T 坐标算出 L₂d=−dL₁，符号符合[-1] shift；未交换 cohomology 与完成。 |
| Prop 5.3 `ellipticCohenDetector` | 730–801 | Poincaré mixed class 的两项、相反图像差的系数2，以及杀掉 slope0 的 contraction 一致。Q* 在 proper H1 上由 trace∘pullback=deg 注入，包括纯不可分情形；unit-root scalar Frobenius multiplier为(1−2i)^d。 |
| Lem 5.4 `tameQuarticTrace` | 803–838 | tame ramification 局部s=t²、2可逆给全微分的invariant descent，含base dT。norm与Chern由pullback后验证，再用Tr h*=2。 |
| Lem 5.5 `quarticFormalReplacement` | 849–899 | 两个光滑仿射lift在完备底上同构的逐层lift论证成立；Y-monic给无π挠；Pic(B)→Pic(B/π) 注入可由 Hom提升+Nakayama证明；只识别Pic类而不要求实际ideal逐项相等。 |
| Cor 5.6 `quarticRootChernDetected` | 901–921 | 由Q非恒定、norm、scalar survival、formal replacement推出非零。只需要非零map，不声称将整数lattice张量Q5后仍注入。 |
| Lem 6.1 `dimensiontwoAMMNinput` | 997–1061 | essentially smooth model 的相对dimension为2而非1，因dT保留；AMMN square 与 HC ordinary quotient 定位一致。完整mixed HKR补证另存。模块接口见下节。 |
| Prop 6.2 `dimensiontwoactualassembly` | 1086–1253 | actual relative point lift来自K4(F5)=0和residue reduction0。Geisser–Levine给特殊纤维 q>2 的有限系数消失；Milnor sequence需q,q+1两度，稿件使用正确。两条注入所需度分别4及3，均具备。只在有限平坦扩系数后计算Gysin，之后拉回line bundles，不误用scaled map平坦性。完成与generic vanishing均成立。 |
| Prop 7.1 `dimtwoWeightedNonzero` | 1286–1333 | weighted trace 收缩给4 ε ℓ(ω)e3(b)Q*η；无需假设整条root lattice在Q5上线性独立。CM unitroot character ω³ 与 i≡2mod5 一致。 |
| Prop 8.1 `dimtwoExplicitTriple` | 1374–1561 | 积分DS vanishing检查通过；universal supported coefficients 模diagonal唯一的localization计算正确。period→exact rational coefficient接口已由独立交叉审计闭合，见 `audit_explicit_coefficient_transfer.md` 与 `interval_regulator_patch.tex`；共同符号不影响非零性。主Gysin路线不依赖本命题。 |
| Cor 8.2 `twodimexplicitMilnor` | 1573–1617 | field Steinberg/skew-symmetry推导积分为0正确；非零无限阶由natural Milnor→Quillen product映射反推。后半依赖8.1的明确regulator接口。 |
| Lem 9.1 `dimtwoVisibleHigherCoefficientRank` | 1627–1755 | depleted Lin公式与character作用一致；rational map h3n nonconstant，degree≤5，有限像大小≥5^{m−1}，从而F5-span≥m−1；归一化Q5关系取reduction证明lift独立。σ只反转ρ且固定ζ，因此n奇时也不会错误地用复杂共轭奇偶性消灭系数。点Chern比较n≥2适用。 |
| Thm 9.2 `dimtwoCompleteAllOddInfiniteRank` | 1765–1869 | higher HC的t^{2−n}Ω²/dΩ¹度数正确；scalar relative base令cyclic shuffle修正为0。Q5独立的e3(bj)乘同一E∞非零向量仍独立；actual rational关系会给Q5关系。两条完成注入在所有2n−1≥3均成立。 |
| Lem 10.1 `dimtwoFullCohenLaurentResidue` | 1884–1971 | 模π^a在(BT/π^a)((S))中逐层反转primitive denominator成立；不必要求首个字面系数是unit。inverse limit容许随a增长的负幂界。residue sign (−1)^{r−1}给Res d=−dRes，r=3给θ∧dlogS映到θ。 |
| Thm 10.2 `dimtwoCompleteAllDegreesInfiniteRank` | 1973–2176 | 相对dimension3令finite coefficient vanishing从q>3开始；even degree2n≥4的两条注入需2n+1,2n都满足。odd degree3无需错误地调用特殊纤维K3消失，而由even产品独立推出odd因子独立。line/unit higher terms与cyclic shuffle最终HH degree≥5，在D=3下消失。 |
| Lem A.1 `essentiallysmoothAMMN` | 2191–2305 | cotangent absolute-to-relative在固定range的有界p挠证明可用；split triangle来自P projective及M amplitude[−1,0]。circle orbits按connectivity截断处理，没有直接交换任意colimit/completion。mixed HKR引用错配已给完整修补；D+1层数可在Ω无挠后证明。 |

## Cohen常数域接口的补强

544–615 行的C不是含一个任意新常数的微分域，而是光滑W曲线的generic-special-point完成。可选分离参数t，使适当开集对W[t] étale；完成后Taylor substitution t↦t+z由formal étaleness唯一提升，得到积分Hasse导数D_j:C→C。它们与通常导数满足j!D_j=∂^j。

若f∈C且df=0，则char0及无p挠给所有D_j(f)=0。其reduction属于k(U)的共同Hasse常数域。在函数域的一元p-basis描述下，D_1 u=0蕴含u=v^p；D_{pj}(v^p)=D_j(v)^p继续迫使v同样为常数。因此u属于所有k(U)^{p^r}。对任意离散赋值，其极点/零点阶数被所有p^r整除，故均为0，u是光滑proper模型上的常函数，属于代数闭域k。减去此常数的Witt lift再除p并迭代，得f∈W。对F=C[1/p]缩放给constants exactly K。这同时解释了“不完美residue函数域”不构成反例。

Frobenius recursion中a只需积分，不需unit；φ(p)=p保证每次除p后仍保持同一方程。右端在widehat D中，而widehat D∩pC=p widehat D由mod p的D0→k(U)注入给出。故primitive一旦满足该scalar equation就不能引入新的closed-point poles。

## AMMN模块接口

AMMN Proposition 2.8 / Corollary 2.10的中间项确实是H⊗D，H=THH(B)。H是cyclotomic commutative algebra，这些项自然为H-modules；横箭头id_H⊗f、canonical TC→TC−、fixed-to-Tate箭头都兼容H作用。TC的lax monoidal结构把它们送到TC(H)-module diagrams，逆转equivalences仍保留module结构。之后THH→HH以及absolute→W-relative HH是对应的equivariant algebra/module映射。

norm fiber给ΣHC的HC−作用；限制沿multiplicative cyclotomic trace给K(B)作用。这个论证比“natural hence multiplicative”强，稿件确实写出了所需构造。余下链层产品由Bökstedt–Ottosen §2的shuffle/cyclic-shuffle公式支持。scalar coefficient在relative base中时修正项含一个base normalized bar slot，故零；D=3的line×unit修正至少form degree5。

## 实际核对的主要原始文献

- Besser–de Jeu, The syntomic regulator for the K-theory of fields, Theorems 1.10 / 1.12: https://www.numdam.org/article/ASENS_2003_4_36_6_867_0.pdf
- Huber–Kings, A p-adic analogue of the Borel regulator and the Bloch–Kato exponential map, Example 2.2.4, Propositions 2.2.7 / 2.2.9 / 2.3.4: https://arxiv.org/pdf/math/0612611
- Weibel, Étale Chern classes at the prime 2, Proposition 2.1.1 / 2.4: https://sites.math.rutgers.edu/~weibel/archive/papers-dir/chernclass.pdf （odd coefficients的additivity明确包括在内，文章题名不造成p=5适用性障碍。）
- Caro–D’Addezio, Injectivity failure in crystalline comparisons, Theorems 3.2.1 / 7.2.1 / 7.3.1 / 7.3.6: https://carod.users.lmno.cnrs.fr/Injectivity.pdf
- Antieau–Mathew–Morrow–Nikolaus, On the Beilinson fiber square, Theorem A, Propositions 2.8 / 4.10, Corollaries 2.10 / 3.8, Theorem 2.12: https://arxiv.org/pdf/2003.12541
- Geisser–Levine, The K-theory of fields in characteristic p, mod-p K_n(X)=0 for n>dim X: https://www2.rikkyo.ac.jp/web/geisser/p-part.pdf
- Bökstedt–Ottosen, A Hochschild–Kostant–Rosenberg theorem for cyclic homology, §2: https://arxiv.org/pdf/1601.07412
- Bunke–Tamme, Multiplicative differential algebraic K-theory and applications, Proposition 2.8, Theorem 2.31, Lemma 4.5, Theorem 4.9: https://msp.org/akt/2016/1-3/akt-v1-n3-p01-p.pdf

## 最小剩余核验接口

1. 将本审计的mixed HKR补证明文纳入原稿，纠正引用范围。此项是明确的可修复文本/论证缺口。
2. 显式符号只需与检测类相差同一个非零有理倍数，故共同符号不是反例非零性或逻辑闭合的障碍。全embedding period→Borel→BDJ接口已由独立交叉审计闭合，完整记录为 `work/audit_explicit_coefficient_transfer.md`，可插入补证为 `work/interval_regulator_patch.tex`；它不再是开放接口。
3. 主链使用的Caro–D’Addezio、AMMN和syntomic comparison是外部深层定理输入。它们的适用条件已检查，但本次审计未重做其证明；它们应作为明确dependencies，而非隐含为形式化结果。
4. 此报告本身不可充当Danus verified状态。每个待认证事实及依赖应由主线程的fact graph/verifier提供独立记录。


## 后续有限压力测试：所有weight的finite Chern因子化

已逐源复核 Weibel Proposition 2.1.1、Lemma 2.3、Propositions 2.4 / 2.8，以及 Huber–Kings 的 n>1 比较。完整精确适用证明见 `work/finite_chern_factorization.md`。未发现错误：有限 Chern maps 在field E上使用（不是在不能invert5的O上）；odd coefficients保证全degree additivity；Prop2.8的middle→right coefficient reduction保证tower兼容；source只需canonical projections，允许非零lim¹；target的H⁰有限群tower是ML，足够将lim H¹识别为continuous H¹。高weight的factorial有5因子不影响Q5独立性。此项不再作为开放接口。

## 后续交叉核验：point syntomic normalization

普通半线性点坐标与 BDJ modified normalized coordinate 的关系另存 `work/audit_syntomic_normalization.md`。令 A=1−σ/p^n、N=Σ(σ/p^n)^j、P=1−q^(−n)，则 NA=P；ordinary η=a−A^(-1)b，而 modified raw ε=Pa−Nb=Pη，BDJ Definition 4.6 除以 P 后严格得到 η。因此没有剩余 Frobenius 算子，n≥2 的所有权重及分歧域均可使用同一个非零有理常数乘 Li_n 的坐标。本计算从 Besser Proposition 8.6 的原始证明获得，未凭自然性消去算子。
