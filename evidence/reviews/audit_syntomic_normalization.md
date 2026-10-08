# 点上 syntomic 坐标与 Bloch–Kato exponential 的交叉审计

范围：`gersten_quadric_research_manuscript.tex` 的 2926–2962 行，及其在 1666–1675 行和高阶 cyclotomic 类中的使用。1758–1801 行的复 regulator／全嵌入有理类比较是另一个接口；本记录不把二者混同。状态：独立数学审计及可插入补证；不是 Danus verifier 或 Lean 的完整证明证书。

结论：可以闭合点上坐标比较，且不会留下随根、嵌入、剩余次数变化的 Frobenius 因子。原稿 2955–2957 行用 `(1−φ/p^n)u` 描述 modified 坐标，在一般分歧域上不够准确，应改为 q-Frobenius 并给出下面的 norm-polynomial 计算。这个修订不改变声称的共同非零有理常数 κ_n。

## 1. 已读原始来源及准确用途

- Besser, *Syntomic regulators and p-adic integration I: Rigid syntomic regulators*, 作者版内部页 24–28，Definition 8.1、Proposition 8.6、Remark 8.7(3)：半线性 syntomic 到线性 modified syntomic 的比较，使用 Frobenius 的有限几何级数；规范点坐标来自 quasi-fiber product 的连接映射。作者版内部页 31–32，Proposition 9.9、Corollary 9.10、Proposition 9.11：与 étale Chern 类兼容，规范坐标上的比较是 Bloch–Kato exponential。
  原文下载自 [Besser 作者页面](http://www.math.bgu.ac.il/~bessera/reg/reg.html) 的 `reg.ps.gz`，本地可读文件为 `work/besser_original.pdf`（从原始 PostScript 转换）和 `work/besser_original.txt`。不要使用 `work/dim3_sources/besser.pdf`；那是误存的 HTML 文件。
- [Besser–de Jeu 2003](https://www.numdam.org/article/ASENS_2003_4_36_6_867_0.pdf)，§4，尤其 pp. 889–892、Definition 4.6：modified Frobenius 是基域线性的 q-Frobenius，规范坐标对 raw cone 坐标施加 `(1−φ_q^*/q^n)^{-1}`。Theorem 1.12 与 Remark 1.7 给出 cyclotomic 符号的值及仅依赖权重／次数的符号约定。
- [Huber–Kings](https://arxiv.org/pdf/math/0612611)，Example 2.2.4、Propositions 2.2.7、2.2.9、2.3.4：点上双项复形、与 Besser 的理论比较、Chern 类兼容和 exponential 交换图。§1.3 的 exponential 在 n>1 时为同构。

这些引用在点 `Spec O_E` 上的假设均满足：有限扩张 E/Q_p 的剩余域有限，点相对于 O_E 平滑且 proper，n≥2、i=1 满足 Besser 8.6(3) 的条件。没有用到“E 不分歧”或“p 为奇数”。

## 2. 将半线性与线性 Frobenius 分开

设 E/Q_p 有限，E_0 为最大不分歧子域，剩余域为 F_q、q=p^f，ι:E_0→E 为包含，σ 为 E_0 的算术 Frobenius。于是 σ^f=1。令

\[
 A=1-p^{-n}\sigma,\qquad
 N=\sum_{j=0}^{f-1}p^{-nj}\sigma^j,\qquad
 P=1-q^{-n}.
\]

有限几何级数恒等式给出

\[
 NA=AN=P\operatorname{id}_{E_0}.
\]

因为 n>0，所以 P≠0，A 可逆，且 `A^{-1}=P^{-1}N`。这里 A、N 是 Q_p 线性算子，不应擅自视为 E 线性算子，也不应把 σ 直接延拓到任意分歧 E。

点上的相对 de Rham 复形是 E[0]，其 F^n=0（n>0）。在 Huber–Kings Example 2.2.4 的 cone 约定下，普通 syntomic 用双项复形

\[
 C_E=[E_0\longrightarrow E\oplus E_0],\qquad
 c\longmapsto(\iota c,Ac)
\]

表示，两个次数分别为 0、1。一个类 `[a,b]` 的规范 E 坐标为

\[
 \eta([a,b])=a-\iota A^{-1}b.
\]

这不是形式上的“自然性”推断：右式直接消去边界 `(ιc,Ac)`；并且每个 `[a,b]` 都唯一等于 `[a−ιA^{-1}b,0]`。因此 η 是同构，逆映射为 `u↦[u,0]`。

## 3. Besser 比较与 BDJ 的逆规范化完全相消

BDJ 在剩余域为 F_q 的点上可取 q-Frobenius，其 O_E 线性 lift 为点的恒等映射。因此

\[
 \varphi_q^*|_{H^0_{\mathrm{rig}}(\operatorname{Spec}\mathbf F_q/E)}
 =\operatorname{id}_E.
\]

modified 点复形是 `Cone(F^n E→E)[−1]=E[−1]`。它的 raw cone 坐标记为 ε。Besser 8.6(2) 的证明先用 N 将半线性 p-Frobenius cone 映到 q-Frobenius cone，再扩标量到 E。这在点上给出（固定同一 cone 符号约定）

\[
 \epsilon=P a-\iota N b
 =P\bigl(a-\iota A^{-1}b\bigr)
 =P\eta([a,b]).
\]

第一式确实消去边界，因为

\[
 P\iota c-\iota NAc=0.
\]

也可以先把 ordinary 的 `[a,b]` 映到 modified 的双项模型中，再用 `P a-b'` 化为单一 raw cone 坐标；结果相同。Besser Remark 8.7(3) 对普通和 modified 模型的描述正是这个计算在不分歧情形及其线性版本中的表述。

BDJ Definition 4.6 将 ε 变成

\[
 (1-\varphi_q^*/q^n)^{-1}\epsilon
 =P^{-1}\epsilon
 =\eta([a,b]).
\]

所以经过 BDJ 已经采用的规范化，点坐标就是 Bloch–Kato exponential 所用的 de Rham 坐标。没有额外的 `1−σ/p^n`、`1−q^{-n}` 或其逆因子。若改变全局 cone 符号约定，只会同时改变一个固定符号，仍可并入 κ_n。

如将 q-Frobenius 换成 q^r-Frobenius，raw 坐标乘上 `1+q^{-n}+⋯+q^{-(r−1)n}`，新的逆规范化除以 `1−q^{-rn}`；最终 η 不变。由此也直接检查了选择更高 Frobenius 次数和有限剩余域扩张时的相容性。

## 4. 对高阶、分歧、p=2 与秩结论的影响

BDJ 的 regulator 是 Chern 类形式，Theorem 1.12 已经使用 Definition 4.6 的规范化；在 root of unity 上 `L_mod,n(ρ)=Li_n(ρ)`。因此将实际 cyclotomic 类送入 étale Chern 类后得到

\[
 c_{n,1}(b_n(\rho))
 =\exp_{E,n}\bigl(\kappa_n\operatorname{Li}_n(\rho)\bigr),
 \qquad \kappa_n\in\mathbf Q^\times,
\]

其中固定 BDJ 符号时可取其定理中的固定 `±(n−1)!`；如另外使用 Chern character 约定，则只改变依赖 n 的有理因子。Remark 1.7 的符号依赖 n、r，这里 r=1 固定，故不能随 ρ 或嵌入任意选择。

本计算允许任意分歧和 p=2。普通 p-Frobenius 只在 E_0 上使用，modified q-Frobenius 才在 E 上使用，所以没有隐含的分歧域 Frobenius lift 假设。n≥2 时 exponential 为 Q_p 线性同构，乘以 κ_n 保留所有非零性和 Q_p 线性独立性；即使 p 整除 `(n−1)!`，在 Q_p 中仍可逆。

对秩论证，仅同一 E 上一个共同可逆 Q_p 线性算子已足以保留整组独立性；但原稿还使用明确的 Li_n 坐标和嵌入／character 计算，所以最好使用上面的严格坐标等式。这里得到的结论比“共同可逆算子”更强：根本没有剩余 Frobenius 算子。

1758–1801 行的 `β_BDJ=s β_BT` 是实际有理 K 类的比较，需要全复嵌入及 Borel injectivity 等独立输入。点坐标计算不证明那个 s 有理；该接口已由 `work/audit_explicit_coefficient_transfer.md` 单独核查。本报告只说明，一旦这个实际类等式成立，转到 p-adic regulator 时不会再引入根相关因子。

## 5. 建议的局部修订

以 `work/syntomic_normalization_patch.tex` 替换 2953–2962 行或作为紧随其后的解释。至少将原稿 `φ/p^n` 改为 `φ_q^*/q^n` 并声明 q 为剩余域基数；否则原句不能按字面用于分歧 E。此次交叉审计未发现该接口导致核心反例或高阶秩结论失败。

