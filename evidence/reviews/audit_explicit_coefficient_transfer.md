# 显式单位类的复周期—数域系数—p-adic 系数接口

对象：work/package/gersten_dimension_two_research_manuscript.tex，重点 1412–1557 行。此项独立审计补足显式 supplement 的系数比较；完备 detector 和 AMMN assembly 的其余输入由另一审计处理。本报告不表示这些输入已被本报告重新证明，也不宣称 Danus-verifier 或证明助手认证。

**结论：该系数转移接口可以闭合。** 需要把 1486–1490 行的 compressed regulator computation 替换或补充为 work/interval_regulator_patch.tex 的引理；随后 all-embedding period → rational K3 equality 的步骤有效，common scalar 的有理性可以严格证明，且确实足以转移两个 p-adic odd character 的非零性。该处没有发现需要丢弃显式类或改变系数的数学错误。

## A. 支撑系数只差 diagonal：先于任何 regulator 计算

令 \(V=K_3(E_0)_{\mathbf Q}\)，其中 \(E_0=\mathbf Q(\rho)\)。对

\[
Q^0=\operatorname{Spec}E_0[X,V,t]/(XV+\Phi_{10}(t)),\quad
D=V(X)=\coprod_{g=1}^4\mathbf A^1_{E_0},
\]

localization 与 homotopy invariance 将支撑类写成 \(\sum_g\gamma_g\eta_g\)。由于 \(Q^0[1/X]\simeq\mathbf G_m\times\mathbf A^1\)，Laurent fundamental theorem 给

\[
K_4(Q^0[1/X])\simeq K_4(E_0)\oplus K_3(E_0)[X].
\]

第一项延拓至 \(Q^0\)，边界为零；第二项的边界为共同符号下的 diagonal tuple，因为 \(X\) 在每个根分量上的阶数为 1。故

\[
\ker(K_3(D)\to K_3(Q^0))=\Delta K_3(E_0)
\]

在积分层面成立。因此要确定所需 \(\kappa\)，**恰须且只须确定各个 \(\gamma_i-\gamma_j\)**。不需要从 regulator 恢复任意 \(K_3(Q^0)\) 类。

对 \(U=Q^0[1/(t(1-t))]\) 的版本，额外 Laurent summands 的 rational boundary 为零：延拓项显然为零，另两项系数在 \(K_2(E_0)_{\mathbf Q}=0\)。这给 1457–1463 行的 rational uniqueness，确保任意实际 supported lift 都产生同一 \(\kappa_{\mathbf Q}\)。

## B. 完整 interval 计算处理 real endpoint

固定 embedding \(\sigma:E_0\hookrightarrow\mathbf C\) 及两个根 \(a_i=\sigma t_i,a_j=\sigma t_j\)。原始十次根集合为 \(e^{\pm i\pi/5},e^{\pm3i\pi/5}\)。其中不存在 antipodal pair，故任意两根之间的 chord 不穿过 0；其内部位于单位圆内部，不含其他根或 1。在该 chord 的一个解析邻域 \(\Omega\) 可以统一选取 \(L=\operatorname{Log}(1-t)\) 与 \(F=\operatorname{Li}_2(t)\)，并令 \(N=t^{-1}(\Omega)\subset U(\mathbf C)\)。

在 unshifted interval complex 中，unit regulator 的 canonical representative 是

\[
i\,d\arg(g)+d(\tau\log|g|),\qquad g=1-t.
\]

若 \(L=a+i\phi\)，它与 \(d(\tau L)\) 的差为 \(d(i(1-\tau)\phi)\)。后者是**合法 interval coboundary**：primitive 的 endpoint 0 在 \(\mathbf R(1)=i\mathbf R\)，endpoint 1 为 0，满足 \(F^1A^0=0\)。

令 \(\xi\) 为 \(\delta=\langle X,VH(t)\rangle\) 的 weight-two regulator 的任意 closed interval representative，允许其 endpoint \(\xi_0\ne0\)。其 endpoint \(\omega=\xi_1\) 是 closed holomorphic two-form；由于 \(F^2A^1=0\)，它不随代表改变。dense open \(X\ne0\) 上的 unit-symbol formula 给

\[
\omega=10\frac{dX}{X}\wedge\frac{dt}{t}
=-\frac{dX\wedge d(VH(t))}{t^{10}}.
\]

右式光滑延伸至两个 poles，因此确定全邻域上的 \(\omega\)。乘积由

\[
d(\tau L)\wedge\xi=d(\tau L\xi)
\]

表示。endpoint 0 为零；endpoint 1 为 \(dL\wedge\omega=0\)，因为 complex dimension 为 2。cone map \(-\int_0^1\) 与 Stokes 给

\[
r_3(\alpha)|_N=[-L\omega]
\quad\text{in}\quad H^2(N,\mathbf C)/H^2(N,\mathbf R(3)).
\]

这里没有丢弃 \(\delta\) 的 real endpoint；它被第一个因子的 endpoint 0 为零消去。也没有仅凭曲率判断 Deligne 类：\(\tau L\xi\) 的 endpoint 1 为 \(L\omega\)，一般不满足 \(F^3A^2=0\)，因此它不是 weight-three interval complex 中的 primitive。这正是非零类留下的位置。

## C. 所有 embedding 的周期确定全部差系数，符号吻合

matching sphere 用从 \(i\) 到 \(j\) 的 chord 参数 \(s\) 与角参数 \(\vartheta\)，取 orientation \(ds\wedge d\vartheta\)。因为 \(dF=-Ldt/t\)，

\[
L\omega=10d(FdX/X),\qquad
\int_{\Sigma_{ij}}r_3(\alpha)
=-20\pi i(F(a_j)-F(a_i))\pmod{i\mathbf R}.
\]

两个 poles 的正负号由边界 orientation 给出。除子 \(D_i\) 的 local normal coordinate 是 \(X\)；在 initial pole，\(s-s_i\) 为正的 \(|X|^2\) 倍数，故交数 \(+1\)。在 terminal pole，\(s_j-s\) 为正的 \(|X|^2\) 倍数，故交数 \(-1\)。因此 \(\operatorname{ch}_1(\eta_i),\operatorname{ch}_1(\eta_j)\) 的 periods 分别为 \(+2\pi i,-2\pi i\)，其余根的 period 为零。稿中 1499–1500 行的符号正确。

因 \(|a_i|=|a_j|=1\)，\(\operatorname{Im}F(a)=D_{\rm BW}(a)\)。故 regulator period 的 real part 为

\[
20\pi(D_{\rm BW}(a_j)-D_{\rm BW}(a_i)).
\]

另一方面，若 \(b_\sigma(\gamma)\in i\mathbf R\) 是 coefficient regulator，则 \(\sum\gamma_g\eta_g\) 的该 period 为 \(2\pi i(b_\sigma(\gamma_i)-b_\sigma(\gamma_j))\)，它本身是 real。两者相等推出

\[
b_\sigma(\gamma_i-\gamma_j)
=10i(D_{\rm BW}(a_i)-D_{\rm BW}(a_j))
=-10b_\sigma(\beta_{\rm BT}(t_i)-\beta_{\rm BT}(t_j)).
\]

这对每个 \(\sigma\) 成立。Borel 的 all-embedding injectivity 因而给出 \(V\) 中的 equality，而非只给一个 complex real-vector equality。固定 \(j\)，令

\[
h=\gamma_j+10\beta_{\rm BT}(t_j).
\]

则对每个 \(i\)，\(\gamma_i+10\beta_{\rm BT}(t_i)=h\)。因此余项恰为 diagonal；利用 \(\sum_i\eta_i=0\) 得

\[
\kappa=-10\sum_i\beta_{\rm BT}(t_i)\eta_i
\quad\text{in }K_3(Q^0)_{\mathbf Q}.
\]

**秩检查。** \(V\) 的 rational rank 为 2，其 complex-conjugation action 全为 \(-1\)。supported coefficient quotient \(V^4/\Delta V\) 的 rational dimension 为 6。两个独立 complex embeddings（其余由 conjugation 决定）各提供三个独立 root-difference periods，总计六个 real coordinates。Borel regulator 在 \(V\otimes\mathbf R\) 上是 rank-two isomorphism 到 coefficient target；root Chern period pairing 是 rank-three isomorphism。因此这组 periods 对该六维 supported subspace 的检测完整，没有遗失 anti-part 或额外 diagonal 外 ambiguity。这里绝不能只用一个 embedding 就宣布 coefficient equality。

## D. common scalar 的定义、独立性与有理性

核过以下原始来源：

- [de Jeu (1995), Proposition 4.1、Remark 5.2](https://www.numdam.org/article/CM_1995__96_2_197_0.pdf)：weight-two symbol 的 complex regulator 用同一个 universal normalization 给出 Bloch–Wigner 值。
- [Besser–de Jeu (2003), (1.1)、Theorem 1.10(1)–(2)、Remark 1.7](https://www.numdam.org/article/ASENS_2003_4_36_6_867_0.pdf)：Theorem 1.10 的底边明确是 (1.1) 的 de Jeu field map；符号选择只依赖 \(n,r\)，可一次固定，与 field、root 无关。其 local regulator 在 \(n=2\) 为 \(\pm L_{\rm mod,2}\)。
- [Bunke–Tamme (2016), Theorem 4.9、(4.8)](https://msp.org/akt/2016/1-3/akt-v1-n3-p01-p.pdf)：给 \(\beta_{\rm BT}(a)\) 的 normalization \(-iD_{\rm BW}(a)\)。

de Jeu p.235 的扫描页已目视核验；Proposition 4.1 的 prefactor 是 universal \(\pm(n-1)/(2\pi)^{n-1}\)，而 \(P_2=D_{\rm BW}\)。从该 normalized Tate coordinate 转回共同的 \(H^1_D(\mathbf C,\mathbf R(2))\) 坐标只涉及同一个 degree-two normalization。因此存在一个 fixed nonzero real scalar \(s_{\mathbf R}\)，使在任意 number field、任意 root、任意 embedding 上，BDJ symbol 的 regulator 等于 \(s_{\mathbf R}\) 倍 BT regulator。此处没有给每个 field 单独选 scalar。

把 \(a=\zeta_6=e^{i\pi/3}\) 置于 \(L=\mathbf Q(\sqrt{-3})\)。定义

\[
\beta_{\rm BT}(a)=\tfrac16\operatorname{bl}(6[a])
\]

即可把正文对 order ten 的记法延伸到 calibration root。\(a,1-a\) 都是 global units，\(6[a]\) 的 wedge boundary 为零，且 \(D_{\rm BW}(a)>0\)。故 BT 与 BDJ classes 都是 \(K_3(L)_{\mathbf Q}\) 的非零元素。该群是一维 rational vector space，故存在唯一

\[
s\in\mathbf Q^\times\quad\text{使}\quad
\beta_{\rm BDJ}(a)=s\beta_{\rm BT}(a).
\]

取 complex regulator 后 \(s=s_{\mathbf R}\)。这便证明此前 universal real scalar 本身是 rational。再对任意 number field 使用全部 embeddings 和 Borel injectivity，得到

\[
\beta_{\rm BDJ}(a)=s\beta_{\rm BT}(a).
\]

稿中只需 \(s\in\mathbf Q^\times\)，不需算出 \(s=+1\) 或 \(-1\)。原稿没有完全固定 de Jeu 的 orientation sign，因此不宜凭当前 convention 声称一个具体正负值；上述唯一 rational calibration 已给出可审查且足够的定义。直接把任意 real proportionality 移到 p-adic target 是不合法的，这一 rank-one calibration 正是修补该问题的必要步骤；稿中已经有它。

## E. actual antisymmetrization 与两个 p-adic characters

取 \(\Gamma=\operatorname{bl}(10[-\rho])\in K_3(\mathcal O_{E_0})\)。因为 \(1+\rho\) 的 norm 为 1，它是 global unit；\(10[-\rho]\) 的 exterior boundary 积分为零。因此 \(\Gamma\) 是 BT 定理供应的实际类。

从 all-embedding regulator formula 与 Borel injectivity 可得 rational naturality \(\sigma_g\beta_{\rm BT}(-\rho)=\beta_{\rm BT}(-\rho^g)\)；即使 integral \(\operatorname{bl}\) 的选择没有预先保证 Galois naturality，这个 rational statement 仍成立。又因 \(D(z^{-1})=-D(z)\)，

\[
\sigma_{-1}\beta_{\rm BT}(-\rho)=-\beta_{\rm BT}(-\rho),\qquad
\beta_{\mathbf Q}:=(\Gamma-\sigma_{-1}\Gamma)_{\mathbf Q}
=20\beta_{\rm BT}(-\rho)=\frac{20}{s}\beta_{\rm BDJ}(-\rho).
\]

finite residue localization 使 \(K_3(W_{\rm ar})_{\mathbf Q}\to K_3(E_0)_{\mathbf Q}\) 为同构，故这项 equality 在完成前的 coefficient DVR 上也成立，然后可施加 p-adic completion 与 syntomic regulator。因此

\[
\operatorname{reg}_{\rm syn}(\beta)
=\frac{20\epsilon}{s}\operatorname{Li}_2(-\rho),\qquad\epsilon\in\{1,-1\}
\]

在统一 BDJ convention 下成立。对 \(r=1,3\) 施加 \(e_r\) 后，乘数 \(20\epsilon/s\in\mathbf Q_5^\times\) 非零。正文 200–271 行的独立 dilogarithm character lemma 分别给 \(4e_1Li_2/\tau_1\equiv2\pmod5\)、\(4e_3Li_2/\tau_3\equiv1\pmod5\)，故两个 local character components 都非零。

复 Borel rank 本身不能推出最后这一 p-adic nonvanishing；这里实际使用的是 **数域中的 rational K-class equality + BDJ local regulator formula + 两个 p-adic congruences**。再将 local Chern nonvanishing 传到 AMMN scalar 的部分仍沿正文 Proposition “An actual arithmetic coefficient” 的既定比较，不要求 AMMN scalar 与 syntomic coordinate 的数值直接相同。

最后，\(\sigma_g\beta=20\beta_{\rm BT}(t_g)\) 给

\[
\kappa=-\tfrac12\sum_g\sigma_g(\beta)\eta_g.
\]

这项 equality 是 \(K_3(Q^0)_{\mathbf Q}\) 内的 equality，故任意 test ring pullback 都保持。1537 行的 \(-1/2\) factor 已核对，未漏 antisymmetrization 的 2 或 BT 定义的 10。它只识别 split-surface/test-algebra 上的类，不声称源环内部的 Gysin class equality。

## F. 对非完备核心结论的真正反向压力测试：是否可在 colimit 中突然为零？

审计选择一个能够实际推翻原推理的机制：存在 fixed class \(\kappa\in K_3(Q)\)，每个有限 \(Q_s\) 上的某种检测非零，但其像在 \(K_3(\mathcal T)\) 中却为零。若所用检测依赖每次重新选择不同的 K 类，或有限 opens 不是 cofinal，这个机制可能发生；本稿没有这两种缺陷。

四次主例中 \(B=A\otimes W\) 已经局部，

\[
\mathcal O(\mathcal T)=S^{-1}\mathcal O(Q),\qquad S=R_0\setminus\mathfrak m.
\]

有限个分母的乘积仍在 \(S\)，所以 \(Q_s\) 形成所需 filtered/cofinal system。它们的 regulator 检测的都是同一个 \(\kappa\) 的 restriction，未随 \(s\) 更换类。filtered colimit 的定义给出：若 \(\kappa\) 的像为零，则存在有限 \(s\) 使 \(\kappa|_{Q_s}=0\)；若某个固定整数 \(N\ne0\) 杀死其像，则存在有限 \(s\) 使 \(N\kappa|_{Q_s}=0\)。

每个有限 \(s\) 上已有真实 homomorphism 到 real vector space，且 \(\operatorname{reg}(\kappa|_{Q_s})\ne0\)，故后一 equality 也不可能。**这只用 K-theory 的 filtered continuity，完全不需要解析上同调或 regulator commute with the infinite colimit。** 因此“在每个 finite open 检测到非零却在 colimit 变零”不是此稿的残留漏洞。

进一步把“全 H²”换成仅 root subspace，也足够完成此排除；本稿的更强 H² injection 不是额外必需假设。若将同一论证搬到真正的完备 ring，有限局部化 cofinality 不再自动成立，所以该测试也解释了为什么非完备 proof 不能单独证明完备结论。完备稿必须独立通过其 scalar-Cohen / completed detector。
