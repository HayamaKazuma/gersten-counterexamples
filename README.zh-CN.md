# 分歧正则局部环中的有理 Gersten 核

[阅读全文](paper/gersten-counterexamples.pdf) · [English](README.md) · [核验证据](evidence/README.md)

[GitHub 仓库](https://github.com/HayamaKazuma/gersten-counterexamples) · [线上检查](https://github.com/HayamaKazuma/gersten-counterexamples/actions) · [发布说明](PUBLISHING.md)

本仓库包含121页研究论文、可编译的 TeX 源文件、数学审计记录和局部 Lean 证明。核心结果在二维、三维分歧正则局部环及其完备化上构造实际无限阶的 Quillen $K_3$ 元素，其分式域像积分地为零，从而得到有理 Gersten 映射的非零核。

二维例子为

$$
A_2=\left(\mathbf Z_{(5)}[T,x,y]/(\Phi_5(1+y)+x^4+Txy^3)\right)_{(5,x,y)}.
$$

三维例子为

$$
A_3=\left(\mathbf Z_{(3)}[x,y,z]/(3+xy+z^2)\right)_{(x,y,z)},
\qquad
c=2\left\{\frac{1+z}{2},1+x,1+\frac{(1+x)y}{4}\right\}.
$$

论文在两个维数都给出显式单位乘积，并展开支撑类、regulator 检测和完备化的证明。进一步结果包括：

- 每个剩余素数处的温和及 Eisenstein 族，在固定局部维数中得到任意大的核秩。
- 高奇数阶的类，以及每个三阶以上次数中的指定单位乘积。
- 每个素数处存在固定三维环及固定完备三维环，在每个三阶以上次数中都有无限秩有理泛点核。
- 剩余特征五中存在一个固定完备二维环，在每个三阶以上次数中都有同样的无限秩性质。
- 二维、三维显式 Milnor 核类，以及三维构造的 Beilinson-motivic 和高阶 Chow 推论。

引言的结果表给出各族的系数环、剩余域和对应定理。五份原始 TeX 文稿另存于 `archive/original/`，原始字节与 SHA-256 均予保留。[论文制作与覆盖记录](evidence/manuscript-production.md)说明六个正文模块的汇编和检查过程。

## 目录

| 路径 | 内容 |
| --- | --- |
| `paper/` | 121页论文、六个正文模块、TeX 源文件与成品 PDF |
| `formal/` | 12 个 Lean 引理、固定版本与原始检查日志 |
| `evidence/danus/` | 12 项接受事实的完整证明、verdict 与依赖索引 |
| `evidence/reviews/` | 分支审计、文献核查及覆盖清单 |
| `evidence/supplements/` | 审计中形成的 TeX 补证 |
| `archive/original/` | 五份原始 TeX 文稿 |
| `scripts/` | 一致性检查与打包脚本 |

## 编译与复核

需要 Python 3.9 以上版本，以及包含 `pdflatex`、`latexmk`、Latin Modern 字体、AMS 与常用扩展宏包的 TeX 发行版。形式化部分固定使用 [Lean 4.34.1](https://github.com/leanprover/lean4/releases/tag/v4.34.1)，无需 Mathlib。

```sh
make check          # 引用、证明哈希、依赖图和归档来源
make pdf            # 生成 paper/gersten-counterexamples.pdf
make formal         # 重新检查 12 个局部 Lean 证明
make standalone     # 展开本地输入，生成 build/gersten-counterexamples.tex
make dist           # 完整检查、编译并生成发布 ZIP
```

指定已有 Lean 可执行文件：`make formal LEAN=/path/to/lean`。使用 `elan` 时，`formal/lean-toolchain` 会选择所需版本。`make clean` 清理中间文件并保留论文 PDF。

GitHub Actions 已配置为自动运行同一组检查、编译 PDF 并上传构建产物，无需配置密钥。两项 Actions 均固定到核对过的真实提交，Lean 下载包使用官方 SHA-256 校验；版本来源见[工具记录](evidence/tool-provenance.md)。TeX 使用 Ubuntu 软件包，因此复现目标是编译过程与内容，不保证不同 TeX 发行版产生逐字节相同的 PDF。本地打包快照形成时尚未运行线上检查；后续结果见 [GitHub Actions](https://github.com/HayamaKazuma/gersten-counterexamples/actions)，并与归档中的本地核验记录分别标识。

## 核验范围

原审计共有 12 项事实通过 Danus 独立语言模型审查，涵盖二维、三维原环及其完备化的核心完整定理。公开证明保留原始字节与哈希，依赖图无缺失、无循环。[事实索引](evidence/danus/fact_index.json)逐项链接证明和 verdict。

Lean 核验了 10 个多项式恒等式和 2 个自然数不等式，无 `sorry`、`admit`、自定义公理或 `native_decide`。完整 K 理论、regulator 与比较定理的证明尚未端到端形式化。

汇编论文包含100个定理、引理、命题或推论环境，以及96个证明环境。这是源码覆盖数量，不表示100项独立认证。原12项 Danus 接受事实与12个局部 Lean 引理各保留原有范围。最终全稿 Danus 审查已完成，未留下尚未解决的数学阻断项。50条参考文献台账记录均在各自载明的来源与适用范围内获得 verified 判定。[制作记录](evidence/manuscript-production.md)标明受审发布版本、已完成的检查，以及历史原文获取和转录证据的具体限制。

自动检查通过表示文件一致性和局部形式化证明通过；脚本不重新运行历史 Danus 模型审查。

## 引用与许可证

论文按用户要求署名 **OpenAI**，用于标识 ChatGPT/Codex 对文稿的整理与制作；该署名不代表 OpenAI 官方发表或机构背书。[CITATION.cff](CITATION.cff) 提供引用元数据，原始文稿保留归档中的原有署名。

[发布记录](evidence/publication/README.md)保存本次元数据变更，并用哈希将当前 PDF 和源码与原数学审查记录关联。其余十个 TeX 模块（包括六个数学正文模块和参考文献）逐字节保持不变。

仓库尚未选定分发许可证，说明见 [COPYRIGHT.md](COPYRIGHT.md)。外部构建工具遵循各自许可证，本仓库不附带这些工具的二进制文件。
