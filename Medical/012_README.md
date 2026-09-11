# Medical

这个目录保存医学指南、专家共识、综述、原始研究等 PDF 原件。PDF 是 **canonical evidence（原始证据）**；为了让 ChatGPT / Hermes / Codex 更稳定地检索、定位和核验，推荐为需要反复调用的文献建立同名 Markdown sidecar。

核心原则：**PDF 保真，Markdown 提高可检索性；任何临床结论最终都应能回到原 PDF 对应页核验。**

## 推荐文件形态

```text
Medical/
├─ 某文献.pdf          # 原始证据，不改写
├─ 某文献.md           # 可检索 sidecar，不代替 PDF
├─ 另一文献.pdf
└─ 另一文献.md
```

sidecar 与 PDF 尽量同名，便于 Agent 从检索结果直接回到原文。

## sidecar 最小内容

不要机械生成“3 个要点式摘要”。医学 sidecar 的任务是建立检索锚点和证据地图，优先保留会改变临床解释的限定条件。

推荐包含：

- Citation：题名、作者/组织、期刊、年份、卷期页码；
- DOI / PMID / guideline identifier（能可靠确认时再填，不猜）；
- document_type：guideline / consensus / systematic-review / RCT / cohort / review / other；
- clinical_scope：疾病、场景、目标人群；
- PICO 或 PECO（适用时）；
- 主要推荐或主要结果；
- recommendation strength / certainty of evidence（原文有时才记录）；
- 关键效应量：RR / OR / HR / ARR / NNT / CI / p value 等，必须保留单位、比较组和时间窗；
- 关键阈值、剂量、时间窗、诊断标准；
- 重要亚组与例外；
- adverse events / harms；
- limitations / evidence gaps；
- important_tables_figures：表格/图编号 + 页码 + 用途；
- page_anchors：重要结论所在 PDF 页码；
- source_pdf：对应 PDF 路径；
- verification_status：是否已经回到 PDF 原页核验。

## 医学证据的特殊规则

### 1. 限定词不能被摘要吃掉

例如：`selected patients`、`after adequate resuscitation`、`conditional recommendation`、`low certainty`、`within 24 h`、`unless contraindicated` 等，往往比一句“大结论”更重要。

### 2. 数字必须带上下文

不要只写“死亡率下降 20%”。至少要能回答：相对还是绝对？哪两个组？什么时间窗？样本量？95% CI？统计学与临床意义是否一致？

### 3. 共识 ≠ 强制标准

专家共识、指南推荐和高质量原始研究属于不同证据角色。sidecar 应保留文献类型、推荐强度、证据质量与适用范围，避免把“专家建议”写成“事实定律”。

### 4. 解读文章不能冒充原始指南

如果目录里同时有“原共识/指南”和“某某解读”，解读可帮助导航，但关键推荐、证据等级和原文措辞应尽可能回到原指南或共识核验。

### 5. 扫描版 PDF 单独标记

如果 PDF 无可选文本或解析结果严重乱码，sidecar 中标记：

```yaml
text_layer: scanned
```

这类文献需要 OCR 或视觉读取，但 OCR 结果只能作为检索辅助，不能替代原页视觉核验，尤其是表格、上下标、剂量和统计量。

## 推荐 frontmatter

```yaml
---
title: ""
document_type: ""
year: 
doi: ""
pmid: ""
source_pdf: ""
text_layer: unknown      # native / scanned / mixed / unknown
verification_status: unverified  # unverified / partially-verified / verified
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

字段宁缺毋滥。无法可靠确认的信息留空，不要由 Agent 猜测补齐。

## Agent 默认读取顺序

```text
真实临床/学习问题
    ↓
先检索 sidecar，快速定位文献与页码
    ↓
读取最相关 PDF 页/表格/段落
    ↓
核对原文措辞、限定条件、证据等级和数字
    ↓
回答当前问题
    ↓
只有真正改变长期判断时，才提议进入 Second-Brain Knowledge / Learning
```

如果 sidecar 不存在，Agent 可以直接读 PDF；当该文献后来反复被调用时，再为它创建 sidecar。不要为了“完成入库”一次性给所有 PDF 生成低质量摘要。

## 与 Second-Brain 的关系

`Library/Medical` 属于 source layer，不是 Second-Brain 的医学 Knowledge 目录。

- Library 回答：**原文、证据和具体页码到底说了什么？**
- Second-Brain 回答：**结合多来源证据与真实临床使用后，我们当前怎样理解和调用这个问题？**

同一篇 PDF 中的多个段落不是多个独立证据；同一指南的多个解读也不能冒充多个独立来源。

## 当前阶段

保持小而可靠。先让真实检索暴露摩擦，再决定是否需要全文文本抽取、自动索引、向量检索或更复杂的文献数据库。

> 医学知识库最危险的失败，不是“搜不到”，而是“很快搜到了一个失去限定条件的答案”。
