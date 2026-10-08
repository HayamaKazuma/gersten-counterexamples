# Lean 有限形式化覆盖审计

审计对象：

- outputs/gersten-audit/formal/GerstenAudit.lean，86 行；
- outputs/gersten-audit/formal/README.zh-CN.md，44 行；
- 已有 lean_verification.log；
- Lean 4.34.1 自带 Init/Grind/Ring/Basic.lean 中的环类定义。

按委托未重新运行 Lean，也未扩张形式化。既有编译成功作为输入；本审计检查 kernel 所检查的命题是否正是数学稿需要的有限命题。

**结论：12 个命题的形式化范围有效，未发现循环假设、只验证整数特例、错误符号版本或奇偶下标遗漏。** README 对核心覆盖范围与未形式化的分析接口基本准确。建议收紧两处描述，避免把多项式关系的验证读成单位性或形式幂级数环同态的完整验证。

## 1. 通用交换环量词核对

源文件第 3 行打开 Lean.Grind，因此前十条的 [CommRing R] 是 Lean.Grind.CommRing，而不是仅为 Int 配置的特殊类。已经读过官方工具链中的类定义：

- Semiring 含通常的加法、乘法、零、一、分配律及自然数系数；
- Ring 增加加法逆元、减法及与整数系数的相容性；
- CommSemiring 增加乘法交换；
- CommRing 继承 Ring 与 CommSemiring。

其幂运算受到零次幂及后继幂公理约束；数值字面量与 natural/integer casts 相容。**未要求 IsCharP、CharZero、Domain、Field 或 Nontrivial。** 因而前十项是任意交换含幺环中的恒等式或条件恒等式，可用于所需的整系数商环、完备环及其局部化。这里没有把在 Int 中成立的公式误当作 arbitrary-ring theorem。

第七项明确要求 2r=1，恰好表达选取 1/2；在交换环中无需额外右逆假设。源环的剩余特征为 3，所以该假设成立。零环也满足形式命题，既不影响证明，也不减弱对实际非零源环的适用性。

## 2. 十二项逐项对应

下表中 G 为二维几何短稿 dimension_two_geometric_short_counterexample.tex，S 为三维短稿 gersten_explicit_short_proof.tex，Q 为 gersten_quadric_research_manuscript.tex。

| Lean 命题及行号 | 假设审查、数学稿对应 | 范围判断 |
|---|---|---|
| cyclotomic_five_expansion，7–9 | 无额外假设；展开 1+(1+y)+⋯+(1+y)^4；对应 G 62 行 | 系数 5,10,10,5,1 正确；formal 文件未另定义通用 cyclotomic polynomial 函数，但展开多项式正是 Φ5 |
| cyclotomic_ten_factorization，12–13 | 无额外假设；(t⁴−t³+t²−t+1)(t⁵−1)(t+1)=t¹⁰−1；对应 G 540–545 | 次数、符号正确；无取样 |
| dim2_symbol_relation，16–18 | 唯一额外假设 xv+Φ10(t)=0；结论 1−xvH(t)=t¹⁰；对应 G 540–545 | 假设是定义方程的改写，不是待证结论；原环中 t=−1−y、v=x³+Ty³ 的代入仍是书面连接 |
| dim2_H_substitution，20–21 | 无额外假设；将 t=−1−y 代入 H；对应 G 542 | 准确证明多项式表达；未证明 H 本身是单位 |
| dim2_ds_relation，24–25 | 假设 1−xb=q；结论 1−x[1+(1−x)b]=(1−x)q；对应 G 543、555 | 正确的负号版本；它只验证 DS 操作所用环等式，不验证 DS 符号关系本身 |
| dim3_ds_relation，27–28 | 假设 1+xt=q；结论 1+x[1+(1+x)t]=(1+x)q；对应 S 112–122、Q 3576–3584 | 正确的正号版本，适合〈−x,t〉；未把 x 与 −x 混淆 |
| dim3_quadratic_unit_relation，31–33 | 假设 2r=1、3+xy+z²=0；结论 ((1+z)r)(1−(1+z)r)=1+xy r²；对应 S 112 | 恰为 a(1−a)=1+xy/4；没有把该结论作为假设 |
| dim3_scaling_relation，36–38 | 假设 u²=−3、XY+Z²=1；结论 3+(uX)(uY)+(uZ)²=0；对应 Q 3592–3598 | 准确验证缩放后定义方程归零；没有形式化 formal-series substitution 的收敛或连续性 |
| quartic_repeated_root_discriminant，41–43 | 假设 q(s)=0 与 q′(s)=4s³+T=0；结论 256−27T⁴=0；对应 G 148–151 | 假设正是共同根条件；甚至对任意 commring 成立；反向、平方自由性及几何光滑性没有在 Lean 中证明 |
| quartic_scaled_identity，46–49 | 假设 u⁴e=5；验证缩放后完整四次式为 u⁴ 倍 chart 方程；对应 G 140–141、179–181 | e 的符号和所有 u 幂次正确；未取消 u⁴，也未假设可以约去零因子；README 的“除以 u⁴ 前”准确 |
| tail_exponential_bound_even，65–72 | 对每个 n:Nat，4n+11<3^(n+3)；对应 S 405–409 | 恰覆盖 j=4+2n；真实归纳，无有限截断 |
| tail_exponential_bound_odd，75–82 | 对每个 n:Nat，4n+13<3^(n+3)；对应同处 | 恰覆盖 j=5+2n；真实归纳，无遗漏奇数支 |

前十项的条件都来自具体 quotient relation、逆元条件或共同根条件。没有任何 K-group 非零性、regulator 非零性、Gersten injectivity 失败或无限阶作为 Lean 假设。

## 3. 三进尾项指数界：完整下标与桥接证明

S 397–414 行以及 Q 3656–3672 行的量为

\[
12\frac{(-3)^jS_j}{2j+3},\qquad
S_j=\sum_{k=0}^j\frac1{2k+1},\qquad
A_j=1+j-\lfloor\log_3(2j+1)\rfloor-v_3(2j+3).
\]

对每个整数 j≥4，存在唯一的以下一个表示：

- j 偶数：j=4+2n，n≥0；
- j 奇数：j=5+2n，n≥0。

偶数情形 2j+3=4n+11，奇数情形 2j+3=4n+13；两种情形都有 floor(j/2)+1=n+3。因此 Lean 的两个 theorem 正好给

\[
2j+3<3^{\lfloor j/2\rfloor+1}.
\]

这不是“只验证两个初始 j”：两个 theorem 对所有 n 作归纳。归纳步骤中的左端分别是 4(n+1)+11 和 4(n+1)+13，均严格小于原左端的三倍；右端的幂增加一次，完全对应 j 增加二。

以下书面连接有效，但没有在此 Lean 文件中形式化：

\[
\lfloor\log_3(2j+1)\rfloor
\le\lfloor\log_3(2j+3)\rfloor
\le\lfloor j/2\rfloor,
\qquad
v_3(2j+3)\le\lfloor\log_3(2j+3)\rfloor.
\]

于是

\[
A_j\ge1+j-2\lfloor j/2\rfloor
=\begin{cases}1,&j\text{ 偶数},\\2,&j\text{ 奇数}.\end{cases}
\]

README 所述统一下界 A_j≥1 正确。j=1,2,3 分别直接算出 1,2,1；j=0 是已单独取出的首项 4，不属于 tail，故没有遗漏需要控制的下标。

从 S_j 各 summand 的赋值可得
\(v_3(S_j)\ge-\lfloor\log_3(2j+1)\rfloor\)；
因 v3(12)=1，原 series 的第 j 项赋值至少 A_j。最后还需

\[
A_j\ge1+j-2\log_3(2j+3)\longrightarrow+\infty
\]

以保证尾项收敛。这项趋于无穷的结论不由“统一下界≥1”单独推出，也不在两个 Lean 指数 theorem 的结论中。README 42 行已正确地把它标为额外书面分析连接。因此可以说 Lean 核检过统一指数上界，不能说 Lean 已核检整个 p-adic series 的收敛、赋值或非零性。

## 4. README 的两项建议措辞

建议作以下小幅范围修订：

1. README 表格 dim2_H_substitution 行的“H(t) 的显式单位表达”改为“H(t) 的显式多项式表达”。H=y((1+y)^5+1) 在源局部环通常不是单位；三单位符号中的第三个单位是 1+(1−x)vH，二者应区别。
2. README 表格 dim3_scaling_relation 行的“保证缩放定义环同态”改为“验证缩放使源环定义多项式归零；形式幂级数代入的收敛另行证明”。Lean 命题给 quotient polynomial relation，formal completion 上的实际 ring map 尚需原稿的连续性/收敛论证。

此外，dim2_ds_relation 的源码注释“preserves its unit condition”宜理解为验证乘法分解：若另知 q 与 1−x 是单位，则新表达式是单位。该 theorem 没有 IsUnit 假设和结论，故不能据它单独宣称所有参与 DS 符号的单位条件已形式化。README 正文末段已明确没有形式化 DS 的 K 理论实现，这点没有形成实质误导。

## 5. 内核与总体证明边界

源码的 12 项均有实际 proof term 构造；未出现 sorry、admit、自定义 axiom 或 native_decide。现存 #print axioms 日志对前十项列出 propext、Classical.choice、Quot.sound，对后两项列出 propext、Quot.sound，均与 README 的标准逻辑公理说明相容。

这些结果足以支持“列举的十项 arbitrary-commring polynomial relations 和两项 all-index natural-number inequalities 已由 Lean 内核检查”。它们不定义 K 理论、闭浸入推前、局部化长正合列、Picard/Betti 持续性、Borel regulator、AMMN、syntomic comparison、形式 de Rham detector 或 Gersten 核。完整反例的证明状态必须继续依据独立数学审计及 Danus 记录，不能由本文件的 kernel success 升格。
