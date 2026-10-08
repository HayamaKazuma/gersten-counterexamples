# GitHub 发布与更新

公开仓库地址为 [HayamaKazuma/gersten-counterexamples](https://github.com/HayamaKazuma/gersten-counterexamples)。仓库已创建，本地发布包记录上传前的制作快照；实际文件和提交以仓库页面为准，线上核验结果见 [GitHub Actions](https://github.com/HayamaKazuma/gersten-counterexamples/actions)。

论文按用户要求署名 OpenAI，首页、制作说明和引用文件说明 ChatGPT/Codex 制作归属及其含义。PDF 位于 `paper/gersten-counterexamples.pdf`，机器可读引用位于 `CITATION.cff`。

## 构建与后续更新

使用有权访问该仓库的 GitHub 账号获取源码：

```sh
git clone https://github.com/HayamaKazuma/gersten-counterexamples.git
cd gersten-counterexamples
make check
make pdf
make formal
make standalone
make dist
```

`make check` 包括原审计文件一致性和本次署名变更的来源核对。发布包包含逐文件 SHA-256 清单。本次打包前，固定版本 Lean 4.34.1 已重新检查全部 12 个局部引理并通过；新记录位于 `evidence/publication/lean-rerun-result.json` 和 `lean-rerun-output.txt`，原始检查记录保持不变。

后续修改应先同步远程提交，完成相应检查，再提交并推送：

```sh
git pull --ff-only
git add .
git commit -m "Update manuscript release records"
git push origin main
```

检查 GitHub Actions 的实际运行结果后，再记录线上核验状态。本地核验成功与托管平台运行成功分别记录。

原 Danus verdict 对应 `evidence/manuscript/reviewed.tex`。署名版的三个元数据模块改动记录在 `evidence/publication/metadata.patch`，其余十个 TeX 模块保持原哈希。修改数学内容后需重新审查对应论证并更新版本记录。PDF 哈希标识本次分发的具体文件；重新编译后如字节发生变化，应保留旧记录并记录新的构建产物，再制作下一版发布包。

仓库尚未选择分发许可证；状态见 `COPYRIGHT.md`。
