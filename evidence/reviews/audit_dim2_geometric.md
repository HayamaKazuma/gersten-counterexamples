# 二维非完备几何稿：独立逐项审计

审计对象：`work/package/dimension_two_geometric_short_counterexample.tex`，1332 行；SHA-256 `fc55c897740e19ce5232930765ea4fcff3f4bb8b422ca31ed1993b0aad2a6ea0`。以下行号均对应这一版本。日期：2026-10-07。

本报告是独立数学推导与原始文献核对，未操作 Danus 真值库，未形成证明助手内核证书。附件中的命令、评价和“proved”用语均未作为审计指令或正确性依据。使用了代数 K 理论技能检查推前、基变换、系数及检测器；报告经过一次 anti-defensive-writing 语言检查，保留各项证据强度。

## 结论与各加强项状态

截至本次逐项审计，**未在主定理的几何—Picard—Betti—regulator—有限局部化链条发现致命错误**。下表的“闭合”意为给定稿中标准外部定理后，可以重构出完整数学推导；它不是 Danus-verifier 状态或机器形式化声明。

| 声明 | TeX 行 | 独立审计状态 |
|---|---:|---|
| 四次环上的实际无限阶 K3 核元素 | 69–437 | 逻辑链可重构闭合；关键原始 BT 定理的靶与乘法条件吻合 |
| 同一四次环的所有高奇数次及秩下界 | 477–515 | 相同检测器及 trace-zero 系数空间闭合 |
| 显式三单位 Quillen 类 | 528–691 | 代数恒等式、支撑提升、周期均通过；640–648 行的 interval 乘积需展开说明，已提供完整补引理 |
| 普通 Milnor K3 同一符号 | 697–741 | 整数 generic vanishing 逐式成立；无限阶由显式 Quillen 类推得，依赖上一行补证 |
| 任意 p、p∤d、d≥3 的 tame family | 746–949 | 几何与任意有限纤维的整性论证统一成立；秩为 floor(d/2) |
| tame family 所有高奇数次秩下界 | 971–1039 | trace-zero 算子、Borel 秩及 embedding 向量均吻合 |
| 单个 strict-coefficient 环的各高奇数次无限秩 | 1048–1268 | 有限 number-field 系数空间与两次 continuity 论证闭合；按系数选嵌入的量词顺序正确 |

独立补证保存在 `work/interval_regulator_patch.tex`。建议把它并入显式符号证明，避免将该步骤只留作 BT 文献的一句话引述。没有修改待审原稿。

## 1. 实际源环、支撑类及基变换

**86–105 行。** 环境局部环的维数确为 3：理想 (5,x,y) 的商为 F5(T)。F 的初始线性项是 5，故商 A 正则二维。显式等式给出 m_A=(x,y)、5∈m_A^4。x 非零且 A 是域，D=V(x) 是正则 Cartier 除子，A/x=W[T]_(u)。把 y 映到 ρ−1，恰得到 Φ5(1+y)=0；没有把 T 误放入极大理想。

**107–123 行。** W 的 K3 到 E 的 K3 满射所需边界靶是 K2(F5)=0。取 γ 的 Borel regulator 非零，再取 β=(1−σ_−1)γ，确有 σ_−1β=−β；K3 的 regulator 在复共轭下为负，所以该操作将相应非零分量倍增。β 是实际积分 K 类。i_*β 在 A[1/x] 为零来自 localization，不需未证明的 Gersten 命题。

**128–138 行。** A⊗W 为有限 A-代数，闭纤维 F5(T)[u]/(u^4) 只有一个极大理想，故它局部。先解出 T=−(P(y)+x^4)/(xy^3)，得到 Frac A=Q(x,y)；该函数域的 Q 代数常数仍为 Q，故与 E 线性不交，基变换是域中的子环。B 的函数域为 E(x,y)。

**412–425 行。** 必须在 regular test ring T=B[1/u,1/y] 上把 G-theory 与 K-theory 比较。这里 x=0 确分裂为四个互不相交的简单根 y=ρ^g−1，系数映射恰为 σ_g。平坦 base change 后的 equality

\[
c|_{\mathcal T}=\sum_g(\sigma_g\beta)\,[\mathcal O_{D_g\cap\mathcal T}]
\]

来自实际 Gysin 映射及 projection formula。论证没有对奇异 B 使用 K=G。

## 2. 吹起及例外曲线

**140–211 行。** ε=5/u^4 的剩余类为 −1，因此 tangent cone 的符号正确。∂/∂U=−4U³，奇点须有 U=0；Y=0 时不可能位于曲线上，而 Y≠0 时须使 s⁴+Ts+1 有重根。其判别式 256−27T⁴ 在 F5(T) 中非零。

三个 blow-up chart 必须保留 u=xU、u=yU 的环境关系，稿中已保留。环境 blow-up 正则；special exceptional chart 上的曲线 smooth，故 strict transform 在 C 上正则。除闭点外，generic fiber 的 ∂F/∂T=xy³ 与余下偏导排除奇点；special binary form 的 square-free 性也排除非原点奇点。hypersurface S2 加 R1 给出 normality。

严格变换方程没有仅由 exceptional parameter 支撑的额外分量：在环境 chart 中方程除去参数的四次幂后，模参数为非零、约化、整的 exceptional curve 方程，故参数是新方程商上的非零因子。这也验证 exceptional scheme 为 reduced C。tautological ideal nO_Y=O_Y(−C) 的限制给 O_C(C)=O_C(−1)，符号正确。

根 a_g/u 的剩余类是 g，且 Y-导数在 X=0,Y=g 处为单位。所以根严格变换与 C 在 P_g=[1:0:g] 相交，局部参数为 u,X，交数 1。

## 3. 例外 Picard 群与 arithmetic persistence

**224–249 行。** M 的 X≠0 部分是 Laurent UFD，边界是四个 reduced prime (X,Y−g)。单位 cX^rY^s 的除子只给 diagonal relation，因此 Pic(M)=Z⁴/Z(1,1,1,1)。M 是 smooth，所以这里 Cl=Pic。

对任意 t∈overline(F5)，若 s⁴+ts+1 是有理函数平方，则是多项式平方；首项规范后比较 (s²+bs+c)² 的 s³、s² 系数得 b=c=0，与常数项矛盾。域包含 μ4，Kummer criterion 因而使 w⁴−(s⁴+ts+1) 不可约。w 的局部化保持整性；每个有限 T 纤维都是一个 multiplicity-one principal prime。故从 M 到其 generic T fiber 的 divisor localization 不增加任何 Picard relation。

**273–307 行。** Q 的 Picard 计算对所有 E 的域扩张保持，因为四个根已经在 E 中且互异。若根除子线性组合在 T 主，则同一 rational function 在 regular blow-up Y 上的除子，只能另外含 C 和来自 u=0、y=0 的 strict primes；这是因为 Y[1/u,1/y]=T。把 line-bundle equality 限制到 C*：u-boundary 只见于 U=0，y-boundary 只见于 Y=0；O_C(−1) 在 U≠0 上平凡。只剩同系数根点组合，而上一段使其只能是 diagonal。因此 Pic(Q)→Pic(T) 的 injectivity 成立。

这里限制的是 associated line bundle，而非试图直接把含 C 分量的 rational divisor 限制到 C；稿中用法正确。

## 4. Betti persistence 与 regulator

**312–323 行。** 四个 D_g 为互不相交的 affine lines，补集为 (C*)²。Gysin residue H¹((C*)²,R)→R⁴ 中，angular x 给 diagonal，angular y 给零。因此 root Chern classes 的唯一实线性 relation 为 diagonal。稿中没有错误地把 root subspace 当作整个 H²；后者还可有来自 torus 的商。

**333–350 行。** s 所移去的任一 E-prime divisor Z，在 T 上为空，故 Pic(Q) 中其类由 injectivity 必为零。Z 的 geometric components 是一个 Galois orbit；absolute Galois group 固定全部 root generators，所以在 geometric Picard lattice 上作用平凡。因格子 torsion-free，所有 component classes 相等且总和为零推出每个都为零。特征 0 排除 inseparable multiplicities。扩到 C 后保持这项 Picard 计算。

smooth complex surface 的 degree-two restriction kernel 由所删 divisor components 的 fundamental classes 生成。删除这些曲线的 singular/intersection points，不改变 degree-two support，因为有限点集的 real codimension 为 4。上述所有 c1 均零，故 H²(Q(C),R)→H²(Q_s(C),R) 确实整体 injective。

**355–410 行。** 核过 [Bunke–Tamme 原文](https://msp.org/akt/2016/1-3/akt-v1-n3-p01-p.pdf)：Definition 2.7、Proposition 2.8 是文中所需的 interval/cone 模型；Theorem 2.31 给 analytic Deligne regulator 的乘法；§6 的 (6.4) 及其下文给 Borel comparison 与 injectivity。该靶确实没有 log-growth filtration，故不能用 proper-Hodge 的相邻版本否定这里的 F³=0。

在 complex surface 上，F³ of smooth-form complex literally 为零。cone exact sequence 与 H³(R(3))→H³(C) injective 给

\[
H^3_{D,an}(U,R(3))=H^2(U,C)/H^2(U,R(3)).
\]

point regulator b∈C/R(2) 取纯虚代表，由 interval form −b dτ 表示；line c1 取常值 unitary curvature 2πie。乘积经过 cone map −∫，得到 +2πibe。β 的 weight-two 分量乘 η_g 的 weight-one 分量正给 κ 的 weight-three 分量，既无未计入的 Todd correction，也未使用 regulator-pushforward compatibility。

所有 complex embeddings 合起来，β 的 regulator 向量非零；反共轭条件使其非 diagonal。2πi 将纯虚系数转为实 Betti class，Betti persistence 保持非零，而 R(3) 是纯虚实线，故 quotient 中仍非零。

**401–434 行。** 对任一有限 s，K 类与分母都可 spread 到 O_E[1/N]，并把根、根差及 5 变成单位；smooth Danielewski surface 与其 principal open 为 regular separated finite-type arithmetic schemes。若实际 c 为 torsion，其像 κ 在 filtered localization 中被某整数杀死，continuity 必在某个有限 Q_s 上实现这项 equality；非零实 regulator 排除这一点。没有把复上同调与无限 arithmetic localization 交换。

## 5. 显式三单位类：补足最压缩的接口

**540–560 行。** Φ10(t)H(t)=t¹⁰−1，xv=−Φ10(t)，所以 1−xb=t¹⁰。μ=1+(1−x)b，因而 1−xμ=(1−x)t¹⁰。采用稿中的 Dennis–Stein 符号 convention，addition relation、〈x,1〉=0 及 μ 为单位给

\[
\delta=\langle x,b\rangle=\langle x,\mu\rangle
       =\{(1-x)t^{10},\mu\}.
\]

{1−t,t¹⁰}=0 是整数 Steinberg relation，所以 [1−t]δ 为给出的 triple，并在 x 可逆后整系数为零。

**568–618 行。** α 在 U[1/X] 为零，因此 localization 给 K3(D) 的 actual preimage。整个 D 已包含在 U 中，故该 preimage 可直接 push 到 Q0 得 κ0；这里不需要把 U 上任意类沿 open immersion 推前。rational uniqueness 用 K4(G_m×(A¹\{0,1})) 的 Laurent splitting：唯一非零 rational boundary 是 K3(E)[X] 的 diagonal；K2(E)_Q=0，且其余 summands 延拓。Q0 的 complement 为 G_m×A¹，故 supported coefficients 在积分层面也唯一到 diagonal 为止。

**620–663 行。** matching sphere 的 V 相位使 XV=−Φ10(t)，两端 smooth；t 始终避开 0、1、−1 及另两个根，可在整条 chord 的一个解析邻域选同一 Log(1−t) 与 Li2(t) 分支。曲率

\[
\omega=10(dX/X)\wedge(dt/t)
      =-dX\wedge d(VH)/t^{10}
\]

在 poles 光滑延伸。

640–648 行直接引述 BT 后写 r3(α)=[−Lω]，省略了一个实质上重要的 cone 计算。现已在 `interval_regulator_patch.tex` 给出完整补引理。核心是把 unit cocycle 合法改为 d(τL)，然后

\[
d(\tau L)\wedge\xi=d(\tau L\xi),\qquad
-\int d(\tau L\xi)=-L\omega+d_N\int\tau L\xi.
\]

δ 的 real endpoint ξ0 可以非零，乘积的 real endpoint 仍为零。τLξ 在 endpoint 1 为 Lω，不满足 weight-three F³ endpoint condition；所以 full de Rham exactness 不会使 Deligne class 消失。ω 作为 F²A² 的 closed holomorphic form 由 dense open X≠0 上的 unit-symbol calculation 唯一决定。

Stokes 的上下边界符号分别为 ±2πi，故 −Lω 的 period 为 −20πi(Li2(r)−Li2(bar r))=40πD_BW(r)。r=e^(iπ/5)，后者是正实数，其模 R(3)=iR 的像非零。之后支持类写成 Σγ_gη_g，使该 period 属 real root subspace；前述 Betti persistence 正好能使用。

**711–740 行。** ordinary Milnor generic vanishing 的两步关键关系

\[
\{x,q\}=\{\lambda q,\mu\},\qquad\{g,q\}=0
\]

在 field 中整系数成立，遂得 m={g,x,q}=−{g,q,x}=0。源环中只需单位积给出的自然 K3^M(A)→K3(A)，不需任何尚未证明的 comparison isomorphism。Quillen image 无限阶就排除 m 的 torsion。

## 6. 所有 p 与高阶、无限秩加强

**777–805 行。** W0 是 Eisenstein DVR。E=K(μd) 的选定 p-adic completion 先作 unramified μd extension，再作 θ^d=−p 的 totally ramified degree d extension，因此 θ 为 W 的 uniformizer，μd 的 reductions distinct。W 可不是有限 Z_(p)-module；稿中只用其 flatness，并显式局部化，这一条件准确。

**813–874 行。** q_t=s^d+ts+1 满足 d q_t−s q_t′=(d−1)ts+d。由 p∤d，gcd 的次数至多 1。若 q_t 是某个 ℓ|d 的 ℓ 次方，因 ℓ≠p，gcd(q_t,q_t′) 的次数至少 d−d/ℓ≥2，矛盾。因 kbar 包含 μd，若 w^d−q_t reducible，Kummer splitting extension 的 Galois group 是 μd 的真子群，会使 q_t 成某 ℓ 次方，仍矛盾。因此包括 p=2,d=3 在内所有允许参数的 finite fibers integral。d=2 不满足次数下界，稿中负对照 t=2 fiber split 的确有效。

blow-up regularity 沿 C 已由 tangent smoothness 给出；其余 regularity 可用 excellence 令 nonregular locus closed，再以 proper image 在 local base 上必须含闭点推出为空。这一步不要求 residue field perfect。

**923–944 行、989–1038 行。** K3(K) 的全 embedding regulator 向量在 real embedding 为零、共轭 embeddings 相反；非零时必非 diagonal。高阶取 V_n=ker Tr_(K/Q)，实际算子 d−res Tr 在 V_n 上为乘 d，且输出积分 trace-zero。point regulator 位于 iR(n)，乘 2πi 后位于 iR(n+1)，因此不落入 real coefficient subspace R(n+1)。Borel 秩计算给 even n: floor(d/2)，odd n: ceil(d/2)−1，均与 real-root 数目吻合。

**1068–1263 行。** strict henselization V 是 noetherian DVR，Frac V 是 Q 的 algebraic extension，且含全部 prime-to-p roots of unity。W=V[θ] 是 degree-d totally ramified DVR；几何 Picard 论证仍在 overline(Fp) 上成立。对于 N>2、d|N、p∤N，L_N=Q(μN)、K_N=L_N(θ) 是 totally imaginary number fields；选定 p-place 下 Eisenstein 给 [K_N:L_N]=d。trace-zero space 的维数为 (d−1)φ(N)/2。

若某非零 β 的 pushforward 为零，先对 arithmetic denominators 用 continuity 得有限 Q_s 上的零 equality，再对 E∞ 的 number-field colimit 用 continuity 使所有数据和零 equality 落到有限 E1。Borel 先为该 β 选择 j0，再延拓到 E∞；这是正确的量词顺序。有限 arithmetic model 的绝对乘法 regulator 与既有 Betti persistence 矛盾。N=d^a 的维数趋于无穷，环 R 不变，因而推出所述各次数无限秩。

## 7. 独立反向压力测试

### 7.1 低阶负对照

同一 proof template 在 K1 不能运行：weight target 为 2，而 complex surface 的 F² complex 非零。把高阶 quotient 公式强行用于 K1 会错误地产生 K1(A)→Frac(A)^× 的反例；稿中 517–519 行明确阻断了这一步。这个负对照支持其 weight cutoff 的准确性。

同一 tame template 在 d=2 不能运行：finite fiber 确实可能 reducible，从而 localization 可增加 root-divisor relation。稿中 958–964 行正确地阻断该方向。

### 7.2 与已知 Milnor injectivity 的假设逐项对照

已查阅原始文献，而非依搜索摘要断言存在一般定理：

- [Kerz, *The Gersten conjecture for Milnor K-theory*, Theorem 6.1](https://kerz.app.uni-regensburg.de/articles/milnork_inventiones.pdf) 的主 injectivity 要求 regular semilocal ring **含一个域**。本稿的混合特征源环不满足。
- [Lüders–Morrow, *Milnor K-theory of p-adic rings*, Theorem 0.1 / 4.1](https://www.imo.universite-paris-saclay.fr/~matthew.morrow/Lueders%2C%20Morrow%2C%20Milnor%20K-theory%20of%20p-adic%20rings.pdf) 的结果对 p-henselian、ind-smooth DVR-algebras，且是模 p^r 的结论。本稿源环 special fiber singular，不能套用。
- [Lüders, *On the relative Gersten conjecture for Milnor K-theory in the smooth case*](https://arxiv.org/pdf/2010.02622) 保持 smooth-over-DVR 假设，并把首位 injectivity 归约至 DVR，而不声明任意 ramified regular local ring 的首位 injectivity。
- [Pawar, *A remark on Gersten complex for Milnor K-theory*, Theorem 1.2 / 3.3](https://arxiv.org/pdf/2105.06962) 的“degrees ≥ dim S”是 **Gersten complex 的上同调位置 p**，不是 Milnor K 的下标 n。其结论 A^p(X,K_n^M)=0 对 p≥dimS≥1，不覆盖 augmentation injectivity；摘要不能读作本稿高次 Milnor claim 的反证。

quartic 源环进一步排除了更换 coefficient DVR 后成为 geometrically regular 的可能（443–450 行）：A/5 的 binary form不可约，故 5 是素元；若 local DVR map 的 uniformizer π 满足 5=επ^e，则 A 中素性使 e=1、πA=5A，而对应 fiber singular。所有上述 smooth/ind-smooth 输入都仍失效。

这些检索未找到覆盖本稿源环并与其结论直接矛盾的已发表定理；这项“未找到”不能单独充当反例正确性的证据。正确性依据是上面的逐项推导。

## 8. 建议纳入最终审稿版的精确补充

1. 在 640–648 行加入 interval-regulator 补引理，明确 local logarithm 的合法 coboundary、δ 的 real endpoint、holomorphic curvature 的唯一性。
2. 主证明的附录可保留一张依赖图：regular source → actual supported class；blow-up → Picard persistence → geometric component c1 vanish → finite-open Betti persistence；Borel coefficient + multiplicative regulator → nonzero finite-stage regulator；K continuity → actual infinite order。
3. 对独立审计与最终 Danus-verifier 输出分别标注状态。整个主定理还未在 Lean/Coq 等证明助手中形式化；有限 polynomial identity 或数值 dilogarithm 检查不会覆盖 K-theory 的主要外部接口。
4. 556 行的 Weibel “Exercise 5.6” 定位不精确：核对 [作者原版 Chapter III](https://sites.math.rutgers.edu/~weibel/Kbook/Kbook.III.pdf)，Ex. 5.6 是 projection formula；这里的 Dennis–Stein 定义、(D1)–(D3) 和〈r,1〉=0 位于 Definition 5.11 及其紧随段落（印刷页 43–44），若要引用指标无关性则是 Exercise 5.11。公式和 convention 本身与原文相同，故这是文献定位修正而非数学断口。

审计未使用任何数值近似作为 nonvanishing 证明；D_BW 的正性来自区间 (0,π/3) 上积分函数符号。尝试调用系统 Python 的 SymPy 时发现未安装，未据此产生或引用任何验证结果。
