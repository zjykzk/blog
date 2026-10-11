# Wiki Health Report — 2026-10-11

> 已于 2026-10-11T17:55:18+08:00 完成修复。本文是修复前快照，当前状态见 [fix-report.md](fix-report.md)。

审计时间：2026-10-11T17:45:32+08:00。模式：`wiki-lint --check`。扫描根目录：`/Users/zenk/study/wiki/wiki`。
配置由本地 `wiki/index.md`、`wiki/.manifest.json`、`wiki/log.md` 推定；没有本地或全局配置文件。
扫描 517 个 Markdown 文件，其中 510 个位于 maps/concepts/topics/syntheses/sources；另外 7 个是首页、治理、日志及缓存文件。共处理 7,929 条有效双链；代码中的链接示例不计入图，5 条图片嵌入和 3 条指向仓库内 Excalidraw 原始材料的链接均可解析。

最先处理 YAML 解析错误、生命周期枚举、关系类型和导航遗漏。共有 36 条确定的结构发现及缺失字段警告；同一页可能计入多个检查。时效提醒、置信度与 provenance 重算候选、标签治理和综合机会另计，避免把候选当成已证实错误。

| 检查 | 结果 | 判定 |
| --- | --- | --- |
| 孤立页面 | 4 | 确定发现 |
| 失效双链 | 0 | 通过 |
| YAML 无法解析 | 11 | 错误 |
| 缺少基础元数据 | 1 | 确定发现 |
| 摘要缺失 / 过长 | 1 / 1 | 软警告 |
| 生命周期 / 置信度字段 | 1 个无效枚举 + 2 个缺失字段 | 枚举错误；缺失字段为警告 |
| 关系类型错误 | 2 | 错误 |
| 索引遗漏 / 摘要过时 | 12 / 1 | 确定发现 |
| 超过 90 天未更新 | 388 | 全部 draft；时效提醒 |
| 来源修改晚于页面 | 12 页 / 22 条来源引用 | mtime 候选 |
| Provenance | 21 个漂移候选 + 1 个高流量页提醒 | 需要语义复核 |
| 置信度重算 | 210 | 来源分类候选；其中 34 篇综合页需换用综合规则 |
| 碎片标签群 | 0 | 另有 20 个大群/来源类型标签，以及 1 个类型标签候选 |
| 敏感信息可见性 | 0 | 技术文章标题误报已排除 |
| 未说明矛盾 | 0 | 仅在抽查范围内 |
| 综合机会 | 6 | 建议项 |

## 1. Orphaned Pages — 4 found

- [concepts/Freedom and Self-Discipline.md](</Users/zenk/study/wiki/wiki/concepts/Freedom and Self-Discipline.md>) — 零入链。
- [concepts/Hierarchical Syntactic Structure.md](</Users/zenk/study/wiki/wiki/concepts/Hierarchical Syntactic Structure.md>) — 零入链。
- [sources/人生的问题循环.md](</Users/zenk/study/wiki/wiki/sources/人生的问题循环.md>) — 零入链。
- [syntheses/数据字典的秩.md](</Users/zenk/study/wiki/wiki/syntheses/数据字典的秩.md>) — 零入链。

这些页面也都未列入首页。建议先判断其是否为稳定知识，再从相应地图或现有相关正文添加有语义的入口。`sources/人生的问题循环.md` 是无 frontmatter 的正文，应先明确原始材料/知识页身份。

## 2. Broken Wikilinks — 0 found

所有双链目标均可解析。解析支持 `wiki/` 路径前缀、带空格文件名、别名、展示文本、标题/块锚点、相对路径及实际存在的图片。未因规范化规则把真实文件名改成连字符。此检查验证页面/附件存在性，不验证每个标题或块锚点的存在性。

## 3. Frontmatter — 11 malformed, 1 missing

以下 11 页的 `summary:` 值包含未保护的 `: `，标准 YAML 解析失败。应使用引号或 `summary: >-`。这些字段实际存在，审计只在内存中临时恢复以完成其他检查，未把它们重复计为字段缺失。

- [concepts/Agent Skill Design Patterns.md](</Users/zenk/study/wiki/wiki/concepts/Agent Skill Design Patterns.md:6>) — `summary` 中含未保护的英文冒号。
- [sources/Cursor Codebase Indexing Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Cursor Codebase Indexing Source Guide.md:6>) — `summary` 中含未保护的英文冒号。
- [sources/Epiplexity Paper Notes.md](</Users/zenk/study/wiki/wiki/sources/Epiplexity Paper Notes.md:6>) — `summary` 中含未保护的英文冒号。
- [sources/Harness Engineering Is Cybernetics Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Harness Engineering Is Cybernetics Source Guide.md:15>) — `summary` 中含未保护的英文冒号。
- [sources/Harness Engineering Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Harness Engineering Source Guide.md:6>) — `summary` 中含未保护的英文冒号。
- [sources/NotebookLM Learning Workflow Source Guide.md](</Users/zenk/study/wiki/wiki/sources/NotebookLM Learning Workflow Source Guide.md:6>) — `summary` 中含未保护的英文冒号。
- [sources/Principles of Mechanical Sympathy Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Principles of Mechanical Sympathy Source Guide.md:17>) — `summary` 中含未保护的英文冒号。
- [sources/Theory Is All You Need Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Theory Is All You Need Source Guide.md:6>) — `summary` 中含未保护的英文冒号。
- [syntheses/AI Harness × Testing Strategy.md](</Users/zenk/study/wiki/wiki/syntheses/AI Harness × Testing Strategy.md:17>) — `summary` 中含未保护的英文冒号。
- [syntheses/Agent Skill × Context Management.md](</Users/zenk/study/wiki/wiki/syntheses/Agent Skill × Context Management.md:17>) — `summary` 中含未保护的英文冒号。
- [syntheses/Harness Ratchet × Feedback Flywheel.md](</Users/zenk/study/wiki/wiki/syntheses/Harness Ratchet × Feedback Flywheel.md:19>) — `summary` 中含未保护的英文冒号。

- [sources/人生的问题循环.md](</Users/zenk/study/wiki/wiki/sources/人生的问题循环.md>) — 缺少：title, category, tags, sources, created, updated。

遵循 `wiki/NAMING.md`：`NAMING.md` 和 `README.md` 为治理文档，不要求补齐知识页 frontmatter。未发现重复 YAML 键。

## 3a. Missing Summary — 2 soft warnings

- [concepts/Attention as the Scarce Resource.md](</Users/zenk/study/wiki/wiki/concepts/Attention as the Scarce Resource.md:6>) — 摘要 229 字符，超过 200 字符。
- [sources/人生的问题循环.md](</Users/zenk/study/wiki/wiki/sources/人生的问题循环.md:1>) — 缺少 `summary:`。

## 4. Source Staleness — 12 page candidates, 22 references

比较了 239 条可解析本地来源引用；另有 760 条 URL、会话或非文件来源未进行远程刷新。没有无法解析的本地来源路径。以下 mtime 更新可能来自重新写入、格式维护或文件触碰，不能单独证明来源内容发生变化。15/22 条引用的来源 frontmatter 日期也比派生页更新；其余更应谨慎。

| 派生页 | 来源 | 页 updated | 来源 mtime | 来源 updated |
| --- | --- | --- | --- | --- |
| [syntheses/AI Agent Engineering Learning Path.md](</Users/zenk/study/wiki/wiki/syntheses/AI Agent Engineering Learning Path.md>) | wiki/concepts/Agent.md | 2026-08-15T22:44:31+0800 | 2026-08-24T12:05:55.878569+08:00 | 2026-05-15 21:33:01+08:00 |
| [syntheses/AI Agent Engineering Learning Path.md](</Users/zenk/study/wiki/wiki/syntheses/AI Agent Engineering Learning Path.md>) | wiki/concepts/Agentic Control Loop.md | 2026-08-15T22:44:31+0800 | 2026-08-24T12:05:40.818561+08:00 | 2026-05-13 10:37:07+08:00 |
| [syntheses/AI Agent Engineering Learning Path.md](</Users/zenk/study/wiki/wiki/syntheses/AI Agent Engineering Learning Path.md>) | wiki/sources/Code as Agent Harness Paper Source Guide.md | 2026-08-15T22:44:31+0800 | 2026-08-21T21:28:49.191824+08:00 | 2026-08-12T23:17:18+0800 |
| [syntheses/AI Harness × Testing Strategy.md](</Users/zenk/study/wiki/wiki/syntheses/AI Harness × Testing Strategy.md>) | wiki/topics/AI Harness | 2026-07-12T00:07:31+0800 | 2026-09-10T21:26:15.410289+08:00 | 2026-09-10T21:22:11+0800 |
| [syntheses/AI Harness × Testing Strategy.md](</Users/zenk/study/wiki/wiki/syntheses/AI Harness × Testing Strategy.md>) | wiki/concepts/Agentic Engineering | 2026-07-12T00:07:31+0800 | 2026-10-06T16:41:40.956558+08:00 | 2026-10-06T16:39:47+0800 |
| [syntheses/AI Harness × Testing Strategy.md](</Users/zenk/study/wiki/wiki/syntheses/AI Harness × Testing Strategy.md>) | wiki/concepts/Verification Loop | 2026-07-12T00:07:31+0800 | 2026-09-10T21:26:15.541654+08:00 | 2026-09-10T21:22:11+0800 |
| [syntheses/AI Memory × Context Graph.md](</Users/zenk/study/wiki/wiki/syntheses/AI Memory × Context Graph.md>) | wiki/topics/AI Memory | 2026-07-12T00:07:31+0800 | 2026-07-20T04:38:15.901843+08:00 | 2026-07-20T04:29:25+0800 |
| [syntheses/Agent Knowledge Architecture.md](</Users/zenk/study/wiki/wiki/syntheses/Agent Knowledge Architecture.md>) | wiki/concepts/Knowledge Types | 2026-09-09T21:39:46+0800 | 2026-09-09T21:41:10.156118+08:00 | 2026-09-09T21:39:46+0800 |
| [syntheses/Agent Skill × Context Management.md](</Users/zenk/study/wiki/wiki/syntheses/Agent Skill × Context Management.md>) | wiki/topics/Context Management | 2026-07-12T00:07:31+0800 | 2026-07-12T23:23:19.915422+08:00 | 2026-07-12T23:19:18+0800 |
| [syntheses/Agent Skill × Context Management.md](</Users/zenk/study/wiki/wiki/syntheses/Agent Skill × Context Management.md>) | wiki/concepts/Agentic Engineering | 2026-07-12T00:07:31+0800 | 2026-10-06T16:41:40.956558+08:00 | 2026-10-06T16:39:47+0800 |
| [syntheses/Agent Skill × Context Management.md](</Users/zenk/study/wiki/wiki/syntheses/Agent Skill × Context Management.md>) | wiki/concepts/Continual Learning for AI Agents | 2026-07-12T00:07:31+0800 | 2026-07-20T04:38:34.392156+08:00 | 2026-07-20T04:29:25+0800 |
| [syntheses/Agent Skill × Harness Ratchet.md](</Users/zenk/study/wiki/wiki/syntheses/Agent Skill × Harness Ratchet.md>) | wiki/concepts/Continual Learning for AI Agents.md | 2026-07-12T00:07:31+0800 | 2026-07-20T04:38:34.392156+08:00 | 2026-07-20T04:29:25+0800 |
| [syntheses/Agentic Engineering × Verification Loop.md](</Users/zenk/study/wiki/wiki/syntheses/Agentic Engineering × Verification Loop.md>) | wiki/concepts/Agentic Engineering | 2026-07-12T00:07:31+0800 | 2026-10-06T16:41:40.956558+08:00 | 2026-10-06T16:39:47+0800 |
| [syntheses/Agentic Engineering × Verification Loop.md](</Users/zenk/study/wiki/wiki/syntheses/Agentic Engineering × Verification Loop.md>) | wiki/concepts/Verification Loop | 2026-07-12T00:07:31+0800 | 2026-09-10T21:26:15.541654+08:00 | 2026-09-10T21:22:11+0800 |
| [syntheses/Coding Agent User Harness × Verification Loop.md](</Users/zenk/study/wiki/wiki/syntheses/Coding Agent User Harness × Verification Loop.md>) | wiki/concepts/Verification Loop | 2026-07-12T00:07:31+0800 | 2026-09-10T21:26:15.541654+08:00 | 2026-09-10T21:22:11+0800 |
| [syntheses/Coding Agent User Harness × Verification Loop.md](</Users/zenk/study/wiki/wiki/syntheses/Coding Agent User Harness × Verification Loop.md>) | wiki/concepts/Agentic Engineering | 2026-07-12T00:07:31+0800 | 2026-10-06T16:41:40.956558+08:00 | 2026-10-06T16:39:47+0800 |
| [syntheses/Learning Methodology × Mental Models.md](</Users/zenk/study/wiki/wiki/syntheses/Learning Methodology × Mental Models.md>) | wiki/topics/Learning Methodology | 2026-07-12T00:07:31+0800 | 2026-10-06T13:19:28.651530+08:00 | 2026-10-06T13:18:48+0800 |
| [syntheses/Learning Methodology × Mental Models.md](</Users/zenk/study/wiki/wiki/syntheses/Learning Methodology × Mental Models.md>) | wiki/concepts/Understanding | 2026-07-12T00:07:31+0800 | 2026-10-03T16:02:14.979916+08:00 | 2026-10-03 16:01:27+08:00 |
| [syntheses/Rank Reduction as Generative Model Discovery.md](</Users/zenk/study/wiki/wiki/syntheses/Rank Reduction as Generative Model Discovery.md>) | .agents/skills/ljg-rank/SKILL.md | 2026-07-19T22:00:16+0800 | 2026-09-20T21:42:32.511014+08:00 | 不可用 |
| [syntheses/Verification Loop × Feedback Flywheel.md](</Users/zenk/study/wiki/wiki/syntheses/Verification Loop × Feedback Flywheel.md>) | wiki/concepts/Verification Loop.md | 2026-07-12T00:07:31+0800 | 2026-09-10T21:26:15.541654+08:00 | 2026-09-10T21:22:11+0800 |
| [syntheses/Verification Loop × Feedback Flywheel.md](</Users/zenk/study/wiki/wiki/syntheses/Verification Loop × Feedback Flywheel.md>) | wiki/concepts/Agentic Engineering.md | 2026-07-12T00:07:31+0800 | 2026-10-06T16:41:40.956558+08:00 | 2026-10-06T16:39:47+0800 |
| [syntheses/数据字典的秩.md](</Users/zenk/study/wiki/wiki/syntheses/数据字典的秩.md>) | .agents/skills/ljg-rank/SKILL.md | 2026-07-22T10:51:10+0800 | 2026-09-20T21:42:32.511014+08:00 | 不可用 |

## 5. Contradictions — 0 new unacknowledged conflicts in sampled neighborhoods

抽查了高流量页面、同标签相关页面和 `contradicts` 关系。此结果不能证明全库没有矛盾。

- [concepts/Agentic Engineering.md](</Users/zenk/study/wiki/wiki/concepts/Agentic Engineering.md>), [concepts/Vibe Coding.md](</Users/zenk/study/wiki/wiki/concepts/Vibe Coding.md>) — contradicts edge represents contrasting practices; neither page makes incompatible factual claims.
- [concepts/Evaluation.md](</Users/zenk/study/wiki/wiki/concepts/Evaluation.md>), [sources/AI Evals FAQ Source Guide.md](</Users/zenk/study/wiki/wiki/sources/AI Evals FAQ Source Guide.md>), [concepts/Verification Loop.md](</Users/zenk/study/wiki/wiki/concepts/Verification Loop.md>), [concepts/Judgment Externalization.md](</Users/zenk/study/wiki/wiki/concepts/Judgment Externalization.md>) — All distinguish implementation checks from whether the specification represents real goals.
- [concepts/Formalization.md](</Users/zenk/study/wiki/wiki/concepts/Formalization.md>), [syntheses/Euclid as a Case of Formalization's Limits.md](</Users/zenk/study/wiki/wiki/syntheses/Euclid as a Case of Formalization's Limits.md>) — Synthesis attributes an exact phrasing to Formalization that is not present verbatim on the current concept page; historical mathematical claims were not externally verified.

Agentic Engineering 与 Vibe Coding 明确区分验证责任，因此现有 `contradicts` 边是已说明的实践对照。Evaluation / AI Evals FAQ / Verification Loop / Judgment Externalization 都区分实现满足规格与规格满足现实目标。欧几里得综合页引用的表述与当前 Formalization 页不完全相同，列为出处复核建议；本次未外部核验其中的数学史论断。

## 6. Index Consistency — 12 missing pages, 1 outdated description

首页自称 full page inventory，因此以下遗漏按索引问题报告：

- [concepts/Arithmetic Intensity.md](</Users/zenk/study/wiki/wiki/concepts/Arithmetic Intensity.md>) — 已存在但未列入 `index.md`。
- [concepts/Freedom and Self-Discipline.md](</Users/zenk/study/wiki/wiki/concepts/Freedom and Self-Discipline.md>) — 已存在但未列入 `index.md`。
- [concepts/Hierarchical Syntactic Structure.md](</Users/zenk/study/wiki/wiki/concepts/Hierarchical Syntactic Structure.md>) — 已存在但未列入 `index.md`。
- [concepts/Logit Lens.md](</Users/zenk/study/wiki/wiki/concepts/Logit Lens.md>) — 已存在但未列入 `index.md`。
- [concepts/Positional Encoding.md](</Users/zenk/study/wiki/wiki/concepts/Positional Encoding.md>) — 已存在但未列入 `index.md`。
- [concepts/Self-Attention.md](</Users/zenk/study/wiki/wiki/concepts/Self-Attention.md>) — 已存在但未列入 `index.md`。
- [concepts/Token Embedding.md](</Users/zenk/study/wiki/wiki/concepts/Token Embedding.md>) — 已存在但未列入 `index.md`。
- [concepts/Transformer Feed-Forward Network.md](</Users/zenk/study/wiki/wiki/concepts/Transformer Feed-Forward Network.md>) — 已存在但未列入 `index.md`。
- [concepts/Unembedding and Weight Tying.md](</Users/zenk/study/wiki/wiki/concepts/Unembedding and Weight Tying.md>) — 已存在但未列入 `index.md`。
- [sources/人生的问题循环.md](</Users/zenk/study/wiki/wiki/sources/人生的问题循环.md>) — 已存在但未列入 `index.md`。
- [syntheses/数据字典的秩.md](</Users/zenk/study/wiki/wiki/syntheses/数据字典的秩.md>) — 已存在但未列入 `index.md`。
- [topics/如何阅读康德.md](</Users/zenk/study/wiki/wiki/topics/如何阅读康德.md>) — 已存在但未列入 `index.md`。

- [index.md](</Users/zenk/study/wiki/wiki/index.md:545>) — Hot Cache 仍描述 DORA Metrics；[hot.md](</Users/zenk/study/wiki/wiki/hot.md:4>) 当前摘要和正文已转到规则裁决 Agent 评测。

另有 156 项首页描述与 frontmatter 摘要文字不同，未自动认定为语义错误。改写、翻译和精简可以合理不同；完整候选见 findings.json 的 `index_summary_candidates`。

## 7. Provenance — 22 review candidates

对 449 个含 provenance 或推断标记的页面估算。一个 bullet 计一项，普通段落按句子划分；排除标题、表格、代码、纯导航和 Sources/Related 列表。标记的语义覆盖可能跨句，因此这些是审阅候选，不能直接据此调低 inferred、调高 extracted。先核对来源与逐项标记，再决定是否更新摘要比例。

| 页面 | 类型 | 计数项 | inferred 存储→重算 | ambiguous 重算 | 入链页数 |
| --- | --- | --- | --- | --- | --- |
| [concepts/Agent Loop Human Judgment Positions.md](</Users/zenk/study/wiki/wiki/concepts/Agent Loop Human Judgment Positions.md>) | drift-candidate | 40 | 0.5 → 72.5% | 0.0% | 9 |
| [concepts/Attention as the Scarce Resource.md](</Users/zenk/study/wiki/wiki/concepts/Attention as the Scarce Resource.md>) | drift-candidate | 35 | 0.45 → 8.6% | 2.9% | 8 |
| [concepts/Causal Reasoning.md](</Users/zenk/study/wiki/wiki/concepts/Causal Reasoning.md>) | drift-candidate | 45 | 0.28 → 6.7% | 0.0% | 6 |
| [concepts/Formalization.md](</Users/zenk/study/wiki/wiki/concepts/Formalization.md>) | drift-candidate | 63 | 0.22 → 3.2% | 0.0% | 10 |
| [concepts/Freedom and Self-Discipline.md](</Users/zenk/study/wiki/wiki/concepts/Freedom and Self-Discipline.md>) | drift-candidate | 37 | 0.55 → 18.9% | 0.0% | 0 |
| [concepts/Judgment Externalization.md](</Users/zenk/study/wiki/wiki/concepts/Judgment Externalization.md>) | drift-candidate | 38 | 0.4 → 15.8% | 2.6% | 11 |
| [concepts/Positional Encoding.md](</Users/zenk/study/wiki/wiki/concepts/Positional Encoding.md>) | drift-candidate | 28 | 0.33 → 10.7% | 0.0% | 5 |
| [concepts/Universality of Physical Law.md](</Users/zenk/study/wiki/wiki/concepts/Universality of Physical Law.md>) | drift-candidate | 53 | 0.4 → 7.5% | 1.9% | 6 |
| [concepts/生产资料与生产要素.md](</Users/zenk/study/wiki/wiki/concepts/生产资料与生产要素.md>) | drift-candidate | 54 | 0.24 → 3.7% | 0.0% | 1 |
| [sources/AI Evals FAQ Source Guide.md](</Users/zenk/study/wiki/wiki/sources/AI Evals FAQ Source Guide.md>) | drift-candidate | 89 | 0.32 → 5.6% | 0.0% | 9 |
| [sources/Clinical Hypnosis Classic Texts Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Clinical Hypnosis Classic Texts Source Guide.md>) | drift-candidate | 41 | 0.18 → 0.0% | 0.0% | 5 |
| [syntheses/Agent Knowledge Architecture.md](</Users/zenk/study/wiki/wiki/syntheses/Agent Knowledge Architecture.md>) | drift-candidate | 33 | 0.55 → 30.3% | 0.0% | 6 |
| [syntheses/Agent Skill × Harness Ratchet.md](</Users/zenk/study/wiki/wiki/syntheses/Agent Skill × Harness Ratchet.md>) | drift-candidate | 19 | 0.41 → 68.4% | 0.0% | 4 |
| [syntheses/Buddhist Practice Nihilism and Liberation.md](</Users/zenk/study/wiki/wiki/syntheses/Buddhist Practice Nihilism and Liberation.md>) | drift-candidate | 83 | 0.3 → 13.3% | 8.4% | 5 |
| [syntheses/Euclid as a Case of Formalization's Limits.md](</Users/zenk/study/wiki/wiki/syntheses/Euclid as a Case of Formalization's Limits.md>) | drift-candidate | 37 | 0.42 → 8.1% | 0.0% | 3 |
| [syntheses/Harness Ratchet × Feedback Flywheel.md](</Users/zenk/study/wiki/wiki/syntheses/Harness Ratchet × Feedback Flywheel.md>) | drift-candidate | 16 | 0.38 → 62.5% | 0.0% | 3 |
| [syntheses/Problem-Driven Reading Workbench.md](</Users/zenk/study/wiki/wiki/syntheses/Problem-Driven Reading Workbench.md>) | drift-candidate | 46 | 0.75 → 21.7% | 0.0% | 5 |
| [syntheses/Verification Loop × Feedback Flywheel.md](</Users/zenk/study/wiki/wiki/syntheses/Verification Loop × Feedback Flywheel.md>) | drift-candidate | 22 | 0.34 → 54.5% | 0.0% | 5 |
| [syntheses/丝绸之路中的宗教组织力量.md](</Users/zenk/study/wiki/wiki/syntheses/丝绸之路中的宗教组织力量.md>) | drift-candidate | 31 | 0.5 → 22.6% | 0.0% | 2 |
| [syntheses/数据字典的秩.md](</Users/zenk/study/wiki/wiki/syntheses/数据字典的秩.md>) | drift-candidate | 24 | 0.6 → 20.8% | 0.0% | 0 |
| [topics/Mental Models.md](</Users/zenk/study/wiki/wiki/topics/Mental Models.md>) | hub-inferred | 46 | 0.15 → 23.9% | 0.0% | 63 |
| [topics/Theory of Everything Popular Science.md](</Users/zenk/study/wiki/wiki/topics/Theory of Everything Popular Science.md>) | drift-candidate | 39 | 0.4 → 0.0% | 2.6% | 6 |

`Mental Models` 有 63 个入链页面，估算 inferred=23.9%，超过高流量页面的 20% 提醒阈值。没有页面在本次计数下超过 ambiguous=15%，也没有 inferred>40% 且 sources 为空的页面。没有标记的页面按技能约定视作 extracted，这不代表其来源已经核验。

## 8. Fragmented Tag Clusters — 0 topical clusters requiring linking

按无向页面对去重，cohesion=已连接页面对 / 全部页面对；重复引用和双向引用不会膨胀结果。

| 标签 | 页数 | cohesion | 处理 |
| --- | --- | --- | --- |
| agents | 150 | 0.0958 | large cluster: taxonomy/map review before cross-linking |
| ai-coding | 60 | 0.1175 | large cluster: taxonomy/map review before cross-linking |
| architecture | 62 | 0.0862 | large cluster: taxonomy/map review before cross-linking |
| article | 71 | 0.0241 | source-kind tag excluded by taxonomy |
| arxiv | 23 | 0.0988 | source-kind tag excluded by taxonomy |
| cognition | 80 | 0.0585 | large cluster: taxonomy/map review before cross-linking |
| context | 32 | 0.123 | large cluster: taxonomy/map review before cross-linking |
| feedback | 36 | 0.081 | large cluster: taxonomy/map review before cross-linking |
| harness | 57 | 0.1241 | large cluster: taxonomy/map review before cross-linking |
| judgment | 57 | 0.0764 | large cluster: taxonomy/map review before cross-linking |
| learning | 63 | 0.1075 | large cluster: taxonomy/map review before cross-linking |
| llm | 52 | 0.1222 | large cluster: taxonomy/map review before cross-linking |
| mechanism | 58 | 0.0653 | large cluster: taxonomy/map review before cross-linking |
| paper | 34 | 0.0695 | source-kind tag excluded by taxonomy |
| reasoning | 45 | 0.103 | large cluster: taxonomy/map review before cross-linking |
| roundtable | 6 | 0.0667 | source-kind tag excluded by taxonomy |
| software-engineering | 90 | 0.0742 | large cluster: taxonomy/map review before cross-linking |
| systems | 51 | 0.0808 | large cluster: taxonomy/map review before cross-linking |
| thinking | 98 | 0.0766 | large cluster: taxonomy/map review before cross-linking |
| workflow | 39 | 0.1377 | large cluster: taxonomy/map review before cross-linking |

`#synthesis` 有 10 页、6 对连接、cohesion=0.1333，但它描述页面类型，不能证明页面主题相关。列为标签治理候选；优先检查是否应使用 category/type 表达，避免仅为提高密度插入弱链接。

## 9. Visibility Consistency — 0 confirmed issues

检查了值形式的敏感字段、visibility/pii 的 sources 要求，以及 taxonomy 中的 visibility 系统标签。3 处候选均来自 Life of a Token 技术文章标题或历史误报记录，不是凭据。未在报告中复制潜在敏感值。正则检测不能替代完整敏感信息审查。

## 10. Misc Promotion — not applicable

当前知识库没有 `misc/`；未发现 affinity 推广候选。实体、staging、archives 目录也不存在。目录命名按本库 `syntheses/` 使用。

## 12. Confidence and Lifecycle — 3 schema issues, 388 age warnings

- [sources/人生的问题循环.md](</Users/zenk/study/wiki/wiki/sources/人生的问题循环.md:1>) — 缺少 lifecycle；迁移阶段无法确认，按警告报告。
- [sources/人生的问题循环.md](</Users/zenk/study/wiki/wiki/sources/人生的问题循环.md:1>) — 缺少 base_confidence；按警告报告。
- [topics/如何阅读康德.md](</Users/zenk/study/wiki/wiki/topics/如何阅读康德.md:18>) — lifecycle: seed 不在 draft/reviewed/verified/disputed/archived 枚举内；seed 是 status 的合法值，不能代替 lifecycle。

所有已解析 base_confidence 都在 [0,1] 内。无 supersession 断链、归档目标、链或循环问题。515 页是 draft，1 页 lifecycle 无效，另 1 页缺失；11 个无法解析的原始 YAML 页已在内存恢复，其中的 draft 已计入 515。

388 页距 updated 超过 90 天，全部为 draft，没有 verified 高优先级陈旧页。包括 3 个治理文档；知识与导航页面为 385 页。时效是计算覆盖层，不能自动设成 lifecycle: stale，也不应只改 updated 清除提醒。

<details>
<summary>全部 388 页时效清单</summary>

| 页面 | updated | 距今天数 | lifecycle |
| --- | --- | --- | --- |
| [sources/Journals.md](</Users/zenk/study/wiki/wiki/sources/Journals.md>) | 2026-04-20 | 174 | draft |
| [sources/Mobu Notes.md](</Users/zenk/study/wiki/wiki/sources/Mobu Notes.md>) | 2026-04-20 | 174 | draft |
| [sources/Published Posts.md](</Users/zenk/study/wiki/wiki/sources/Published Posts.md>) | 2026-04-20 | 174 | draft |
| [README.md](</Users/zenk/study/wiki/wiki/README.md>) | 2026-04-21 | 173 | draft |
| [Welcome.md](</Users/zenk/study/wiki/wiki/Welcome.md>) | 2026-04-21 | 173 | draft |
| [concepts/Cynefin Framework.md](</Users/zenk/study/wiki/wiki/concepts/Cynefin Framework.md>) | 2026-04-21 | 173 | draft |
| [sources/Modern Software Engineering Notes.md](</Users/zenk/study/wiki/wiki/sources/Modern Software Engineering Notes.md>) | 2026-04-21 | 173 | draft |
| [syntheses/Decision Modes for Engineering Work.md](</Users/zenk/study/wiki/wiki/syntheses/Decision Modes for Engineering Work.md>) | 2026-04-21 | 173 | draft |
| [topics/BoltDB Internals.md](</Users/zenk/study/wiki/wiki/topics/BoltDB Internals.md>) | 2026-04-21 | 173 | draft |
| [topics/Circuit Breaker.md](</Users/zenk/study/wiki/wiki/topics/Circuit Breaker.md>) | 2026-04-21 | 173 | draft |
| [topics/Go Memory Model.md](</Users/zenk/study/wiki/wiki/topics/Go Memory Model.md>) | 2026-04-21 | 173 | draft |
| [topics/High Concurrency.md](</Users/zenk/study/wiki/wiki/topics/High Concurrency.md>) | 2026-04-21 | 173 | draft |
| [topics/Resource Formula.md](</Users/zenk/study/wiki/wiki/topics/Resource Formula.md>) | 2026-04-21 | 173 | draft |
| [topics/Technical Management.md](</Users/zenk/study/wiki/wiki/topics/Technical Management.md>) | 2026-04-21 | 173 | draft |
| [topics/Testing Purpose.md](</Users/zenk/study/wiki/wiki/topics/Testing Purpose.md>) | 2026-04-21 | 173 | draft |
| [topics/User Stories.md](</Users/zenk/study/wiki/wiki/topics/User Stories.md>) | 2026-04-21 | 173 | draft |
| [sources/Before the Tool Call Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Before the Tool Call Source Guide.md>) | 2026-04-22 | 172 | draft |
| [sources/LLM Reasoning Is Latent, Not the Chain of Thought Source Guide.md](</Users/zenk/study/wiki/wiki/sources/LLM Reasoning Is Latent, Not the Chain of Thought Source Guide.md>) | 2026-04-22 | 172 | draft |
| [sources/Agent Harness Qiaomu Article Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Agent Harness Qiaomu Article Source Guide.md>) | 2026-04-23 | 171 | draft |
| [sources/Qiaomu Best Prompt Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Qiaomu Best Prompt Source Guide.md>) | 2026-04-23 | 171 | draft |
| [topics/Prompt Frequency.md](</Users/zenk/study/wiki/wiki/topics/Prompt Frequency.md>) | 2026-04-23 | 171 | draft |
| [concepts/Epiplexity.md](</Users/zenk/study/wiki/wiki/concepts/Epiplexity.md>) | 2026-04-24 | 170 | draft |
| [sources/Epiplexity Paper Notes.md](</Users/zenk/study/wiki/wiki/sources/Epiplexity Paper Notes.md>) | 2026-04-24 | 170 | draft |
| [sources/Probability Roundtable Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Probability Roundtable Source Guide.md>) | 2026-04-24 | 170 | draft |
| [syntheses/不确定性下的判断.md](</Users/zenk/study/wiki/wiki/syntheses/不确定性下的判断.md>) | 2026-04-24 | 170 | draft |
| [topics/Probability.md](</Users/zenk/study/wiki/wiki/topics/Probability.md>) | 2026-04-24 | 170 | draft |
| [sources/Managed Agents Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Managed Agents Source Guide.md>) | 2026-04-25 | 169 | draft |
| [topics/Learnable Structure in Data.md](</Users/zenk/study/wiki/wiki/topics/Learnable Structure in Data.md>) | 2026-04-25 | 169 | draft |
| [concepts/Cognition Three Channels.md](</Users/zenk/study/wiki/wiki/concepts/Cognition Three Channels.md>) | 2026-04-26 | 168 | draft |
| [concepts/Expression Three Channels.md](</Users/zenk/study/wiki/wiki/concepts/Expression Three Channels.md>) | 2026-04-26 | 168 | draft |
| [sources/AI Coding Control Limits Source Guide.md](</Users/zenk/study/wiki/wiki/sources/AI Coding Control Limits Source Guide.md>) | 2026-04-26 | 168 | draft |
| [sources/Frontend Development Workflow Roundtable Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Frontend Development Workflow Roundtable Source Guide.md>) | 2026-04-26 | 168 | draft |
| [sources/Spec-Driven Development Paper Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Spec-Driven Development Paper Source Guide.md>) | 2026-04-26 | 168 | draft |
| [syntheses/Learning Methodology Across Sources.md](</Users/zenk/study/wiki/wiki/syntheses/Learning Methodology Across Sources.md>) | 2026-04-26 | 168 | draft |
| [concepts/Software Design Three Generators.md](</Users/zenk/study/wiki/wiki/concepts/Software Design Three Generators.md>) | 2026-04-27 | 167 | draft |
| [topics/Limits of Classification.md](</Users/zenk/study/wiki/wiki/topics/Limits of Classification.md>) | 2026-04-27 | 167 | draft |
| [topics/Methods of Classification.md](</Users/zenk/study/wiki/wiki/topics/Methods of Classification.md>) | 2026-04-27 | 167 | draft |
| [topics/What Makes a Good Classification.md](</Users/zenk/study/wiki/wiki/topics/What Makes a Good Classification.md>) | 2026-04-27 | 167 | draft |
| [concepts/React.md](</Users/zenk/study/wiki/wiki/concepts/React.md>) | 2026-04-28 | 166 | draft |
| [sources/React Framework Background and Core Concepts Source Guide.md](</Users/zenk/study/wiki/wiki/sources/React Framework Background and Core Concepts Source Guide.md>) | 2026-04-28 | 166 | draft |
| [concepts/Software Analysis Three Generators.md](</Users/zenk/study/wiki/wiki/concepts/Software Analysis Three Generators.md>) | 2026-04-29 | 165 | draft |
| [sources/Software Methodology by Pan Jianyu.md](</Users/zenk/study/wiki/wiki/sources/Software Methodology by Pan Jianyu.md>) | 2026-04-29 | 165 | draft |
| [topics/Software Methodology.md](</Users/zenk/study/wiki/wiki/topics/Software Methodology.md>) | 2026-04-29 | 165 | draft |
| [topics/Software Development Thought Lineage.md](</Users/zenk/study/wiki/wiki/topics/Software Development Thought Lineage.md>) | 2026-04-30 | 164 | draft |
| [NAMING.md](</Users/zenk/study/wiki/wiki/NAMING.md>) | 2026-05-01 | 163 | draft |
| [sources/Theory Is All You Need Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Theory Is All You Need Source Guide.md>) | 2026-05-01 | 163 | draft |
| [syntheses/From User Story to Architecture.md](</Users/zenk/study/wiki/wiki/syntheses/From User Story to Architecture.md>) | 2026-05-01 | 163 | draft |
| [topics/European Antisemitism.md](</Users/zenk/study/wiki/wiki/topics/European Antisemitism.md>) | 2026-05-01 | 163 | draft |
| [topics/UML Diagrams in Software Development.md](</Users/zenk/study/wiki/wiki/topics/UML Diagrams in Software Development.md>) | 2026-05-01 | 163 | draft |
| [concepts/Domain-Driven Design.md](</Users/zenk/study/wiki/wiki/concepts/Domain-Driven Design.md>) | 2026-05-02 | 162 | draft |
| [concepts/Economic Bubble.md](</Users/zenk/study/wiki/wiki/concepts/Economic Bubble.md>) | 2026-05-02 | 162 | draft |
| [concepts/Conceptual Integrity.md](</Users/zenk/study/wiki/wiki/concepts/Conceptual Integrity.md>) | 2026-05-03 | 161 | draft |
| [topics/面向对象分析与设计.md](</Users/zenk/study/wiki/wiki/topics/面向对象分析与设计.md>) | 2026-05-03 | 161 | draft |
| [sources/GenericAgent Paper Source Guide.md](</Users/zenk/study/wiki/wiki/sources/GenericAgent Paper Source Guide.md>) | 2026-05-04 | 160 | draft |
| [concepts/AI Collaboration Scaffolding.md](</Users/zenk/study/wiki/wiki/concepts/AI Collaboration Scaffolding.md>) | 2026-05-05 17:55:00+08:00 | 159 | draft |
| [concepts/AI Learning Tutor Loop.md](</Users/zenk/study/wiki/wiki/concepts/AI Learning Tutor Loop.md>) | 2026-05-05 14:18:28+08:00 | 159 | draft |
| [concepts/AI Memory 4W Taxonomy.md](</Users/zenk/study/wiki/wiki/concepts/AI Memory 4W Taxonomy.md>) | 2026-05-05 16:25:00+08:00 | 159 | draft |
| [concepts/Accountability.md](</Users/zenk/study/wiki/wiki/concepts/Accountability.md>) | 2026-05-05 14:40:00+08:00 | 159 | draft |
| [concepts/Context Anchoring.md](</Users/zenk/study/wiki/wiki/concepts/Context Anchoring.md>) | 2026-05-05 17:35:00+08:00 | 159 | draft |
| [concepts/Design-First Collaboration.md](</Users/zenk/study/wiki/wiki/concepts/Design-First Collaboration.md>) | 2026-05-05 17:25:00+08:00 | 159 | draft |
| [concepts/Knowledge Priming.md](</Users/zenk/study/wiki/wiki/concepts/Knowledge Priming.md>) | 2026-05-05 17:15:00+08:00 | 159 | draft |
| [concepts/Lost in the Middle Effect.md](</Users/zenk/study/wiki/wiki/concepts/Lost in the Middle Effect.md>) | 2026-05-05 15:45:00+08:00 | 159 | draft |
| [concepts/Permissionless Leverage.md](</Users/zenk/study/wiki/wiki/concepts/Permissionless Leverage.md>) | 2026-05-05 14:40:00+08:00 | 159 | draft |
| [concepts/Prompt Caching.md](</Users/zenk/study/wiki/wiki/concepts/Prompt Caching.md>) | 2026-05-05 13:58:10+08:00 | 159 | draft |
| [concepts/Specific Knowledge.md](</Users/zenk/study/wiki/wiki/concepts/Specific Knowledge.md>) | 2026-05-05 14:40:00+08:00 | 159 | draft |
| [sources/AI Memory Survey Source Guide.md](</Users/zenk/study/wiki/wiki/sources/AI Memory Survey Source Guide.md>) | 2026-05-05 16:25:00+08:00 | 159 | draft |
| [sources/Agent Harness Anatomy Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Agent Harness Anatomy Source Guide.md>) | 2026-05-05 14:03:13+08:00 | 159 | draft |
| [sources/How to Get Rich Source Guide.md](</Users/zenk/study/wiki/wiki/sources/How to Get Rich Source Guide.md>) | 2026-05-05 14:40:00+08:00 | 159 | draft |
| [sources/Lost in the Middle Paper Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Lost in the Middle Paper Source Guide.md>) | 2026-05-05 15:45:00+08:00 | 159 | draft |
| [sources/NotebookLM Learning Workflow Source Guide.md](</Users/zenk/study/wiki/wiki/sources/NotebookLM Learning Workflow Source Guide.md>) | 2026-05-05 14:18:28+08:00 | 159 | draft |
| [sources/Prompt Caching Claude Code Case Study Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Prompt Caching Claude Code Case Study Source Guide.md>) | 2026-05-05 13:58:10+08:00 | 159 | draft |
| [sources/Reducing Friction in AI-Assisted Development Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Reducing Friction in AI-Assisted Development Source Guide.md>) | 2026-05-05 17:55:00+08:00 | 159 | draft |
| [topics/Frontend Development Workflow.md](</Users/zenk/study/wiki/wiki/topics/Frontend Development Workflow.md>) | 2026-05-05 17:25:00+08:00 | 159 | draft |
| [topics/Karpathy Guidelines.md](</Users/zenk/study/wiki/wiki/topics/Karpathy Guidelines.md>) | 2026-05-05 17:45:00+08:00 | 159 | draft |
| [topics/Wealth Creation.md](</Users/zenk/study/wiki/wiki/topics/Wealth Creation.md>) | 2026-05-05 14:40:00+08:00 | 159 | draft |
| [concepts/Agent Action Space.md](</Users/zenk/study/wiki/wiki/concepts/Agent Action Space.md>) | 2026-05-06 11:10:34+08:00 | 158 | draft |
| [concepts/Agent Tool.md](</Users/zenk/study/wiki/wiki/concepts/Agent Tool.md>) | 2026-05-06 11:10:34+08:00 | 158 | draft |
| [concepts/Analogy-Making.md](</Users/zenk/study/wiki/wiki/concepts/Analogy-Making.md>) | 2026-05-06 19:34:46+08:00 | 158 | draft |
| [concepts/Cognitive Engineering.md](</Users/zenk/study/wiki/wiki/concepts/Cognitive Engineering.md>) | 2026-05-06 20:17:19+08:00 | 158 | draft |
| [concepts/Concept.md](</Users/zenk/study/wiki/wiki/concepts/Concept.md>) | 2026-05-06 19:18:40+08:00 | 158 | draft |
| [concepts/Feedforward and Feedback Controls.md](</Users/zenk/study/wiki/wiki/concepts/Feedforward and Feedback Controls.md>) | 2026-05-06 22:24:21+08:00 | 158 | draft |
| [concepts/Knowledge as Network.md](</Users/zenk/study/wiki/wiki/concepts/Knowledge as Network.md>) | 2026-05-06 19:18:40+08:00 | 158 | draft |
| [concepts/LLM Inference Benchmarking.md](</Users/zenk/study/wiki/wiki/concepts/LLM Inference Benchmarking.md>) | 2026-05-06 12:17:59+08:00 | 158 | draft |
| [concepts/Paged Attention.md](</Users/zenk/study/wiki/wiki/concepts/Paged Attention.md>) | 2026-05-06 12:17:59+08:00 | 158 | draft |
| [concepts/Speculative Decoding.md](</Users/zenk/study/wiki/wiki/concepts/Speculative Decoding.md>) | 2026-05-06 12:17:59+08:00 | 158 | draft |
| [sources/Agent Harness Engineering Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Agent Harness Engineering Source Guide.md>) | 2026-05-06 22:45:47+08:00 | 158 | draft |
| [sources/Analysis Concept Anatomy Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Analysis Concept Anatomy Source Guide.md>) | 2026-05-06 19:50:40+08:00 | 158 | draft |
| [sources/Application Concept Anatomy Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Application Concept Anatomy Source Guide.md>) | 2026-05-06 20:17:19+08:00 | 158 | draft |
| [sources/Claude Code Skills Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Claude Code Skills Source Guide.md>) | 2026-05-06 10:51:47+08:00 | 158 | draft |
| [sources/Creation Concept Anatomy Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Creation Concept Anatomy Source Guide.md>) | 2026-05-06 21:23:05+08:00 | 158 | draft |
| [sources/Seeing Like an Agent Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Seeing Like an Agent Source Guide.md>) | 2026-05-06 11:10:34+08:00 | 158 | draft |
| [sources/Understanding as Concept Cloud Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Understanding as Concept Cloud Source Guide.md>) | 2026-05-06 19:34:46+08:00 | 158 | draft |
| [sources/vLLM Inference Systems Source Guide.md](</Users/zenk/study/wiki/wiki/sources/vLLM Inference Systems Source Guide.md>) | 2026-05-06 12:17:59+08:00 | 158 | draft |
| [syntheses/Acting Under Complexity.md](</Users/zenk/study/wiki/wiki/syntheses/Acting Under Complexity.md>) | 2026-05-06 20:17:19+08:00 | 158 | draft |
| [topics/Tool Routing.md](</Users/zenk/study/wiki/wiki/topics/Tool Routing.md>) | 2026-05-06 11:10:34+08:00 | 158 | draft |
| [concepts/Agent Skill Design Patterns.md](</Users/zenk/study/wiki/wiki/concepts/Agent Skill Design Patterns.md>) | 2026-05-07 12:44:36+08:00 | 157 | draft |
| [concepts/Application.md](</Users/zenk/study/wiki/wiki/concepts/Application.md>) | 2026-05-07 10:44:00+08:00 | 157 | draft |
| [concepts/Harnessability.md](</Users/zenk/study/wiki/wiki/concepts/Harnessability.md>) | 2026-05-07 22:03:56+08:00 | 157 | draft |
| [sources/ADK Skill Design Patterns Source Guide.md](</Users/zenk/study/wiki/wiki/sources/ADK Skill Design Patterns Source Guide.md>) | 2026-05-07 12:44:36+08:00 | 157 | draft |
| [sources/Amabile Componential Theory of Creativity Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Amabile Componential Theory of Creativity Source Guide.md>) | 2026-05-07 10:44:00+08:00 | 157 | draft |
| [sources/Coding with AI Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Coding with AI Source Guide.md>) | 2026-05-07 22:03:56+08:00 | 157 | draft |
| [sources/Csikszentmihalyi Systems Model of Creativity Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Csikszentmihalyi Systems Model of Creativity Source Guide.md>) | 2026-05-07 10:44:00+08:00 | 157 | draft |
| [sources/Dewey Reflective Inquiry Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Dewey Reflective Inquiry Source Guide.md>) | 2026-05-07 10:44:00+08:00 | 157 | draft |
| [sources/How People Learn Transfer Source Guide.md](</Users/zenk/study/wiki/wiki/sources/How People Learn Transfer Source Guide.md>) | 2026-05-07 10:44:00+08:00 | 157 | draft |
| [sources/Revised Bloom Taxonomy Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Revised Bloom Taxonomy Source Guide.md>) | 2026-05-07 10:44:00+08:00 | 157 | draft |
| [sources/Schon Reflective Practice Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Schon Reflective Practice Source Guide.md>) | 2026-05-07 10:44:00+08:00 | 157 | draft |
| [sources/Simon Sciences of the Artificial Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Simon Sciences of the Artificial Source Guide.md>) | 2026-05-07 10:44:00+08:00 | 157 | draft |
| [syntheses/Agent Skill Patterns as Human Workflow Control Structures.md](</Users/zenk/study/wiki/wiki/syntheses/Agent Skill Patterns as Human Workflow Control Structures.md>) | 2026-05-07 13:57:16+08:00 | 157 | draft |
| [syntheses/Application and Creation Distinction.md](</Users/zenk/study/wiki/wiki/syntheses/Application and Creation Distinction.md>) | 2026-05-07 10:44:00+08:00 | 157 | draft |
| [syntheses/harness-root-ranks.md](</Users/zenk/study/wiki/wiki/syntheses/harness-root-ranks.md>) | 2026-05-07 18:33:29+08:00 | 157 | draft |
| [concepts/Action Memory.md](</Users/zenk/study/wiki/wiki/concepts/Action Memory.md>) | 2026-05-08 22:24:16+08:00 | 156 | draft |
| [concepts/Context Graph.md](</Users/zenk/study/wiki/wiki/concepts/Context Graph.md>) | 2026-05-08 22:24:16+08:00 | 156 | draft |
| [concepts/Factual Memory.md](</Users/zenk/study/wiki/wiki/concepts/Factual Memory.md>) | 2026-05-08 20:54:16+08:00 | 156 | draft |
| [concepts/Governed Action.md](</Users/zenk/study/wiki/wiki/concepts/Governed Action.md>) | 2026-05-08 22:24:16+08:00 | 156 | draft |
| [concepts/Institutional Friction.md](</Users/zenk/study/wiki/wiki/concepts/Institutional Friction.md>) | 2026-05-08 15:58:41+08:00 | 156 | draft |
| [concepts/Interaction Memory.md](</Users/zenk/study/wiki/wiki/concepts/Interaction Memory.md>) | 2026-05-08 22:24:16+08:00 | 156 | draft |
| [concepts/Organizational Memory.md](</Users/zenk/study/wiki/wiki/concepts/Organizational Memory.md>) | 2026-05-08 20:54:16+08:00 | 156 | draft |
| [concepts/engineering-thinking.md](</Users/zenk/study/wiki/wiki/concepts/engineering-thinking.md>) | 2026-05-08 22:31:50+08:00 | 156 | draft |
| [syntheses/Reality-Refutable Engineering Systems.md](</Users/zenk/study/wiki/wiki/syntheses/Reality-Refutable Engineering Systems.md>) | 2026-05-08 23:09:47+08:00 | 156 | draft |
| [concepts/Coding Agent User Harness.md](</Users/zenk/study/wiki/wiki/concepts/Coding Agent User Harness.md>) | 2026-05-09 21:05:00+08:00 | 155 | draft |
| [concepts/Cognitive Load Theory.md](</Users/zenk/study/wiki/wiki/concepts/Cognitive Load Theory.md>) | 2026-05-09 23:01:29+08:00 | 155 | draft |
| [concepts/Iceberg Model.md](</Users/zenk/study/wiki/wiki/concepts/Iceberg Model.md>) | 2026-05-09 20:15:00+08:00 | 155 | draft |
| [concepts/Leverage Points.md](</Users/zenk/study/wiki/wiki/concepts/Leverage Points.md>) | 2026-05-09 20:15:00+08:00 | 155 | draft |
| [concepts/Meta-Harness.md](</Users/zenk/study/wiki/wiki/concepts/Meta-Harness.md>) | 2026-05-09 22:42:07+08:00 | 155 | draft |
| [sources/Cognitive Load Theory Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Cognitive Load Theory Source Guide.md>) | 2026-05-09 23:00:43+08:00 | 155 | draft |
| [sources/Harness Engineering Is Cybernetics Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Harness Engineering Is Cybernetics Source Guide.md>) | 2026-05-09 21:05:00+08:00 | 155 | draft |
| [sources/How LLMs Actually Work Source Guide.md](</Users/zenk/study/wiki/wiki/sources/How LLMs Actually Work Source Guide.md>) | 2026-05-09 21:19:58+08:00 | 155 | draft |
| [sources/How to Use LLMs Source Guide.md](</Users/zenk/study/wiki/wiki/sources/How to Use LLMs Source Guide.md>) | 2026-05-09 21:26:53+08:00 | 155 | draft |
| [sources/ICAP Learning Framework Source Guide.md](</Users/zenk/study/wiki/wiki/sources/ICAP Learning Framework Source Guide.md>) | 2026-05-09 22:55:00+08:00 | 155 | draft |
| [sources/Iceberg Model Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Iceberg Model Source Guide.md>) | 2026-05-09 20:15:00+08:00 | 155 | draft |
| [sources/Meta-Harness Paper Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Meta-Harness Paper Source Guide.md>) | 2026-05-09 22:42:07+08:00 | 155 | draft |
| [sources/Team AI Coding Harness Seminar Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Team AI Coding Harness Seminar Source Guide.md>) | 2026-05-09 20:42:04+08:00 | 155 | draft |
| [syntheses/LLM Training Stages.md](</Users/zenk/study/wiki/wiki/syntheses/LLM Training Stages.md>) | 2026-05-09 21:39:04+08:00 | 155 | draft |
| [concepts/Component-Based Architecture.md](</Users/zenk/study/wiki/wiki/concepts/Component-Based Architecture.md>) | 2026-05-10 16:08:56+08:00 | 154 | draft |
| [concepts/Declarative Programming.md](</Users/zenk/study/wiki/wiki/concepts/Declarative Programming.md>) | 2026-05-10 16:08:56+08:00 | 154 | draft |
| [concepts/Heavy-Tailed Distribution.md](</Users/zenk/study/wiki/wiki/concepts/Heavy-Tailed Distribution.md>) | 2026-05-10 16:27:44+08:00 | 154 | draft |
| [concepts/State Management.md](</Users/zenk/study/wiki/wiki/concepts/State Management.md>) | 2026-05-10 16:08:56+08:00 | 154 | draft |
| [concepts/三个自我模型.md](</Users/zenk/study/wiki/wiki/concepts/三个自我模型.md>) | 2026-05-10 22:51:54+08:00 | 154 | draft |
| [sources/Evaluation Concept Anatomy Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Evaluation Concept Anatomy Source Guide.md>) | 2026-05-10 14:24:08+08:00 | 154 | draft |
| [sources/Hard Constraints Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Hard Constraints Source Guide.md>) | 2026-05-10 21:43:57+08:00 | 154 | draft |
| [sources/Heavy-Tailed World Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Heavy-Tailed World Source Guide.md>) | 2026-05-10 23:12:22+08:00 | 154 | draft |
| [sources/Narrative as First Principle Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Narrative as First Principle Source Guide.md>) | 2026-05-10 16:21:01+08:00 | 154 | draft |
| [sources/内核 你的三个自我 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/内核 你的三个自我 Source Guide.md>) | 2026-05-10 22:51:54+08:00 | 154 | draft |
| [sources/可能：不确定性是意义的燃料 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/可能：不确定性是意义的燃料 Source Guide.md>) | 2026-05-10 22:20:21+08:00 | 154 | draft |
| [sources/能动与稳态生存逻辑 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/能动与稳态生存逻辑 Source Guide.md>) | 2026-05-10 16:32:29+08:00 | 154 | draft |
| [syntheses/React UI Organization Model.md](</Users/zenk/study/wiki/wiki/syntheses/React UI Organization Model.md>) | 2026-05-10 16:10:12+08:00 | 154 | draft |
| [topics/Frontend Development.md](</Users/zenk/study/wiki/wiki/topics/Frontend Development.md>) | 2026-05-10 16:08:56+08:00 | 154 | draft |
| [concepts/Company Brain.md](</Users/zenk/study/wiki/wiki/concepts/Company Brain.md>) | 2026-05-11 10:27:21+08:00 | 153 | draft |
| [concepts/Semantic File System.md](</Users/zenk/study/wiki/wiki/concepts/Semantic File System.md>) | 2026-05-11 10:27:21+08:00 | 153 | draft |
| [concepts/Skill Self-Evolution.md](</Users/zenk/study/wiki/wiki/concepts/Skill Self-Evolution.md>) | 2026-05-11 12:08:45+08:00 | 153 | draft |
| [sources/Company Brain Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Company Brain Source Guide.md>) | 2026-05-11 10:27:21+08:00 | 153 | draft |
| [sources/Memory Is State Not a Service Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Memory Is State Not a Service Source Guide.md>) | 2026-05-11 10:27:21+08:00 | 153 | draft |
| [sources/Skills-Coach Paper Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Skills-Coach Paper Source Guide.md>) | 2026-05-11 12:08:45+08:00 | 153 | draft |
| [sources/深度思考与高阶思维对话 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/深度思考与高阶思维对话 Source Guide.md>) | 2026-05-11 21:29:38+08:00 | 153 | draft |
| [sources/Agent Observability Needs Feedback Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Agent Observability Needs Feedback Source Guide.md>) | 2026-05-12 12:20:47+08:00 | 152 | draft |
| [sources/Agent Skills Data-Driven Analysis Paper Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Agent Skills Data-Driven Analysis Paper Source Guide.md>) | 2026-05-12 11:05:11+08:00 | 152 | draft |
| [sources/Compounding Engineering Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Compounding Engineering Source Guide.md>) | 2026-05-12 21:05:21+08:00 | 152 | draft |
| [sources/Continual Learning for AI Agents Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Continual Learning for AI Agents Source Guide.md>) | 2026-05-12 11:36:33+08:00 | 152 | draft |
| [sources/React Component Lifecycle Source Guide.md](</Users/zenk/study/wiki/wiki/sources/React Component Lifecycle Source Guide.md>) | 2026-05-12 20:56:53+08:00 | 152 | draft |
| [sources/React Hooks useRef useContext useMemo Source Guide.md](</Users/zenk/study/wiki/wiki/sources/React Hooks useRef useContext useMemo Source Guide.md>) | 2026-05-12 15:50:12+08:00 | 152 | draft |
| [sources/React Hooks useState useEffect Source Guide.md](</Users/zenk/study/wiki/wiki/sources/React Hooks useState useEffect Source Guide.md>) | 2026-05-12 16:36:46+08:00 | 152 | draft |
| [sources/SkillOS Paper Source Guide.md](</Users/zenk/study/wiki/wiki/sources/SkillOS Paper Source Guide.md>) | 2026-05-12 10:45:54+08:00 | 152 | draft |
| [sources/SkillOS Source Guide.md](</Users/zenk/study/wiki/wiki/sources/SkillOS Source Guide.md>) | 2026-05-12 10:35:38+08:00 | 152 | draft |
| [sources/The ICAP Framework Paper Source Guide.md](</Users/zenk/study/wiki/wiki/sources/The ICAP Framework Paper Source Guide.md>) | 2026-05-12 16:51:48+08:00 | 152 | draft |
| [sources/架构文档与图示之道 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/架构文档与图示之道 Source Guide.md>) | 2026-05-12 17:04:17+08:00 | 152 | draft |
| [concepts/Agent Memory Evaluation Stack.md](</Users/zenk/study/wiki/wiki/concepts/Agent Memory Evaluation Stack.md>) | 2026-05-13 09:59:22+08:00 | 151 | draft |
| [concepts/Agent Memory Mechanism Families.md](</Users/zenk/study/wiki/wiki/concepts/Agent Memory Mechanism Families.md>) | 2026-05-13 09:59:22+08:00 | 151 | draft |
| [concepts/Agent Memory Write-Manage-Read Loop.md](</Users/zenk/study/wiki/wiki/concepts/Agent Memory Write-Manage-Read Loop.md>) | 2026-05-13 09:59:22+08:00 | 151 | draft |
| [concepts/Agentic AI Architecture Taxonomy.md](</Users/zenk/study/wiki/wiki/concepts/Agentic AI Architecture Taxonomy.md>) | 2026-05-13 10:37:07+08:00 | 151 | draft |
| [concepts/Agentic Control Loop.md](</Users/zenk/study/wiki/wiki/concepts/Agentic Control Loop.md>) | 2026-05-13 10:37:07+08:00 | 151 | draft |
| [concepts/Business Modeling in Software.md](</Users/zenk/study/wiki/wiki/concepts/Business Modeling in Software.md>) | 2026-05-13 00:06:14+08:00 | 151 | draft |
| [concepts/Feedback Loops.md](</Users/zenk/study/wiki/wiki/concepts/Feedback Loops.md>) | 2026-05-13 00:06:14+08:00 | 151 | draft |
| [concepts/架构一致性.md](</Users/zenk/study/wiki/wiki/concepts/架构一致性.md>) | 2026-05-13 00:06:14+08:00 | 151 | draft |
| [concepts/架构知识模型.md](</Users/zenk/study/wiki/wiki/concepts/架构知识模型.md>) | 2026-05-13 00:06:14+08:00 | 151 | draft |
| [concepts/架构认知框架.md](</Users/zenk/study/wiki/wiki/concepts/架构认知框架.md>) | 2026-05-13 00:06:14+08:00 | 151 | draft |
| [concepts/重构层次.md](</Users/zenk/study/wiki/wiki/concepts/重构层次.md>) | 2026-05-13 00:06:14+08:00 | 151 | draft |
| [sources/Agentic Artificial Intelligence Paper Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Agentic Artificial Intelligence Paper Source Guide.md>) | 2026-05-13 10:37:07+08:00 | 151 | draft |
| [sources/Memory for Autonomous LLM Agents Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Memory for Autonomous LLM Agents Source Guide.md>) | 2026-05-13 09:59:22+08:00 | 151 | draft |
| [sources/What Happens Inside Agent Memory Paper Source Guide.md](</Users/zenk/study/wiki/wiki/sources/What Happens Inside Agent Memory Paper Source Guide.md>) | 2026-05-13 10:38:00+08:00 | 151 | draft |
| [sources/从知识堆积到结构化记忆 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/从知识堆积到结构化记忆 Source Guide.md>) | 2026-05-13 16:50:00+08:00 | 151 | draft |
| [sources/架构师启示录 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/架构师启示录 Source Guide.md>) | 2026-05-13 00:06:14+08:00 | 151 | draft |
| [topics/Requirement to Architecture Mapping.md](</Users/zenk/study/wiki/wiki/topics/Requirement to Architecture Mapping.md>) | 2026-05-13 00:06:14+08:00 | 151 | draft |
| [topics/架构落地方法.md](</Users/zenk/study/wiki/wiki/topics/架构落地方法.md>) | 2026-05-13 00:06:14+08:00 | 151 | draft |
| [sources/综合调研 在没有教科书的地方挖掘真知 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/综合调研 在没有教科书的地方挖掘真知 Source Guide.md>) | 2026-05-14 12:32:46+08:00 | 150 | draft |
| [concepts/Additive World.md](</Users/zenk/study/wiki/wiki/concepts/Additive World.md>) | 2026-05-15 21:33:01+08:00 | 149 | draft |
| [concepts/Agent.md](</Users/zenk/study/wiki/wiki/concepts/Agent.md>) | 2026-05-15 21:33:01+08:00 | 149 | draft |
| [concepts/Creation.md](</Users/zenk/study/wiki/wiki/concepts/Creation.md>) | 2026-05-15 21:33:01+08:00 | 149 | draft |
| [concepts/Hard Constraint.md](</Users/zenk/study/wiki/wiki/concepts/Hard Constraint.md>) | 2026-05-15 21:33:01+08:00 | 149 | draft |
| [concepts/Human Agency.md](</Users/zenk/study/wiki/wiki/concepts/Human Agency.md>) | 2026-05-15 21:33:01+08:00 | 149 | draft |
| [concepts/Multiplicative World.md](</Users/zenk/study/wiki/wiki/concepts/Multiplicative World.md>) | 2026-05-15 21:33:01+08:00 | 149 | draft |
| [concepts/Narrative.md](</Users/zenk/study/wiki/wiki/concepts/Narrative.md>) | 2026-05-15 21:33:01+08:00 | 149 | draft |
| [concepts/Organizational Ontology.md](</Users/zenk/study/wiki/wiki/concepts/Organizational Ontology.md>) | 2026-05-15 21:33:01+08:00 | 149 | draft |
| [concepts/System.md](</Users/zenk/study/wiki/wiki/concepts/System.md>) | 2026-05-15 21:33:01+08:00 | 149 | draft |
| [concepts/Uncertainty as Meaning Fuel.md](</Users/zenk/study/wiki/wiki/concepts/Uncertainty as Meaning Fuel.md>) | 2026-05-15 21:33:01+08:00 | 149 | draft |
| [sources/Chatham House Rule Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Chatham House Rule Source Guide.md>) | 2026-05-15 22:36:42+08:00 | 149 | draft |
| [sources/LLM Wiki Source Guide.md](</Users/zenk/study/wiki/wiki/sources/LLM Wiki Source Guide.md>) | 2026-05-15 21:19:51+08:00 | 149 | draft |
| [sources/Use Case 开发管理 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Use Case 开发管理 Source Guide.md>) | 2026-05-15 21:33:01+08:00 | 149 | draft |
| [sources/思维圆桌 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/思维圆桌 Source Guide.md>) | 2026-05-15 21:33:01+08:00 | 149 | draft |
| [sources/表征 图式 心智模型和解释框架 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/表征 图式 心智模型和解释框架 Source Guide.md>) | 2026-05-15 20:56:12+08:00 | 149 | draft |
| [sources/表达清晰圆桌 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/表达清晰圆桌 Source Guide.md>) | 2026-05-15 23:34:56+08:00 | 149 | draft |
| [sources/设计模式 设计原则与系统思维 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/设计模式 设计原则与系统思维 Source Guide.md>) | 2026-05-15 21:33:01+08:00 | 149 | draft |
| [sources/配置 钩子 代码库与技能放置决策 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/配置 钩子 代码库与技能放置决策 Source Guide.md>) | 2026-05-15 22:32:37+08:00 | 149 | draft |
| [sources/面向 LLM 的清晰表达 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/面向 LLM 的清晰表达 Source Guide.md>) | 2026-05-15 23:53:00+08:00 | 149 | draft |
| [syntheses/ICAP 与知识类型的适用边界.md](</Users/zenk/study/wiki/wiki/syntheses/ICAP 与知识类型的适用边界.md>) | 2026-05-15 21:33:01+08:00 | 149 | draft |
| [syntheses/Knowledge System Construction.md](</Users/zenk/study/wiki/wiki/syntheses/Knowledge System Construction.md>) | 2026-05-15 21:33:01+08:00 | 149 | draft |
| [syntheses/Requirements Expression Beyond Use Cases.md](</Users/zenk/study/wiki/wiki/syntheses/Requirements Expression Beyond Use Cases.md>) | 2026-05-15 21:33:01+08:00 | 149 | draft |
| [syntheses/Use Cases as AI Coding Traceability Anchors.md](</Users/zenk/study/wiki/wiki/syntheses/Use Cases as AI Coding Traceability Anchors.md>) | 2026-05-15 21:33:01+08:00 | 149 | draft |
| [syntheses/信息流与状态流转设计原则.md](</Users/zenk/study/wiki/wiki/syntheses/信息流与状态流转设计原则.md>) | 2026-05-15 21:04:58+08:00 | 149 | draft |
| [syntheses/深度思考 高阶思维与本质理解.md](</Users/zenk/study/wiki/wiki/syntheses/深度思考 高阶思维与本质理解.md>) | 2026-05-15 21:33:01+08:00 | 149 | draft |
| [syntheses/软件设计作为系统诊断.md](</Users/zenk/study/wiki/wiki/syntheses/软件设计作为系统诊断.md>) | 2026-05-15 21:34:15+08:00 | 149 | draft |
| [topics/Judgment Under Leverage.md](</Users/zenk/study/wiki/wiki/topics/Judgment Under Leverage.md>) | 2026-05-15 21:33:01+08:00 | 149 | draft |
| [concepts/Use Case.md](</Users/zenk/study/wiki/wiki/concepts/Use Case.md>) | 2026-05-16 00:00:00+08:00 | 148 | draft |
| [sources/Use Case concept graph.md](</Users/zenk/study/wiki/wiki/sources/Use Case concept graph.md>) | 2026-05-16 00:00:00+08:00 | 148 | draft |
| [sources/Use Case 协作与追踪矩阵 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Use Case 协作与追踪矩阵 Source Guide.md>) | 2026-05-16 00:23:43+08:00 | 148 | draft |
| [sources/NotebookLM 产品化 RAG 技术路径 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/NotebookLM 产品化 RAG 技术路径 Source Guide.md>) | 2026-05-17 16:06:05+08:00 | 147 | draft |
| [sources/Principles of Mechanical Sympathy Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Principles of Mechanical Sympathy Source Guide.md>) | 2026-05-17 23:35:07+08:00 | 147 | draft |
| [sources/SPDD Abstraction First Source Guide.md](</Users/zenk/study/wiki/wiki/sources/SPDD Abstraction First Source Guide.md>) | 2026-05-17 22:44:01+08:00 | 147 | draft |
| [sources/SPDD Alignment Source Guide.md](</Users/zenk/study/wiki/wiki/sources/SPDD Alignment Source Guide.md>) | 2026-05-17 22:44:01+08:00 | 147 | draft |
| [sources/SPDD Iterative Review Source Guide.md](</Users/zenk/study/wiki/wiki/sources/SPDD Iterative Review Source Guide.md>) | 2026-05-17 22:44:01+08:00 | 147 | draft |
| [sources/Structured-Prompt-Driven Development Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Structured-Prompt-Driven Development Source Guide.md>) | 2026-05-17 22:44:01+08:00 | 147 | draft |
| [sources/Agent Skills Survey Paper Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Agent Skills Survey Paper Source Guide.md>) | 2026-05-18 15:01:48+08:00 | 146 | draft |
| [concepts/Reasoning as Structure Mapping.md](</Users/zenk/study/wiki/wiki/concepts/Reasoning as Structure Mapping.md>) | 2026-05-19 22:35:35+08:00 | 145 | draft |
| [sources/Galls Law Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Galls Law Source Guide.md>) | 2026-05-19 00:00:00+08:00 | 145 | draft |
| [sources/Law of Leaky Abstractions Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Law of Leaky Abstractions Source Guide.md>) | 2026-05-19 00:00:00+08:00 | 145 | draft |
| [sources/推理概念解剖 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/推理概念解剖 Source Guide.md>) | 2026-05-19 19:27:35+08:00 | 145 | draft |
| [sources/推理证明与未知问答 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/推理证明与未知问答 Source Guide.md>) | 2026-05-19 22:35:35+08:00 | 145 | draft |
| [syntheses/AI 时代开发岗位分层与协作.md](</Users/zenk/study/wiki/wiki/syntheses/AI 时代开发岗位分层与协作.md>) | 2026-05-19 23:51:12+08:00 | 145 | draft |
| [sources/Agentic-First Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Agentic-First Source Guide.md>) | 2026-05-20 04:11:49+08:00 | 144 | draft |
| [sources/推理能力训练 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/推理能力训练 Source Guide.md>) | 2026-05-20 21:34:36+08:00 | 144 | draft |
| [sources/Doris 写入与 Routine Load Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Doris 写入与 Routine Load Source Guide.md>) | 2026-05-21 15:20:08+08:00 | 143 | draft |
| [sources/Memory in the Age of AI Agents Paper Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Memory in the Age of AI Agents Paper Source Guide.md>) | 2026-05-21 14:52:00+08:00 | 143 | draft |
| [syntheses/大语言模型时代知识图谱的角色转变.md](</Users/zenk/study/wiki/wiki/syntheses/大语言模型时代知识图谱的角色转变.md>) | 2026-05-21 00:00:00+08:00 | 143 | draft |
| [sources/CAP Theorem Source Guide.md](</Users/zenk/study/wiki/wiki/sources/CAP Theorem Source Guide.md>) | 2026-05-22 01:47:51+08:00 | 142 | draft |
| [sources/Dive into Claude Code Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Dive into Claude Code Source Guide.md>) | 2026-05-22 21:13:00+08:00 | 142 | draft |
| [sources/Hyrums Law Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Hyrums Law Source Guide.md>) | 2026-05-22 02:02:00+08:00 | 142 | draft |
| [sources/组织角色与 AI 适配 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/组织角色与 AI 适配 Source Guide.md>) | 2026-05-22 23:32:41+08:00 | 142 | draft |
| [concepts/Autonomy-Supportive Parenting.md](</Users/zenk/study/wiki/wiki/concepts/Autonomy-Supportive Parenting.md>) | 2026-05-23 02:14:22+08:00 | 141 | draft |
| [sources/人力资本 信号筛选和社交资本 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/人力资本 信号筛选和社交资本 Source Guide.md>) | 2026-05-23 02:14:22+08:00 | 141 | draft |
| [sources/刻意练习 天赋的作用究竟是什么 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/刻意练习 天赋的作用究竟是什么 Source Guide.md>) | 2026-05-23 01:34:12+08:00 | 141 | draft |
| [sources/可取以及不可取的困难 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/可取以及不可取的困难 Source Guide.md>) | 2026-05-23 02:06:00+08:00 | 141 | draft |
| [sources/拥抱和桥接 知识迁移 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/拥抱和桥接 知识迁移 Source Guide.md>) | 2026-05-23 01:11:08+08:00 | 141 | draft |
| [sources/自主支持 献祭式教育终结者 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/自主支持 献祭式教育终结者 Source Guide.md>) | 2026-05-23 02:14:22+08:00 | 141 | draft |
| [sources/默会知识 AI 永远都不可能替代的技能 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/默会知识 AI 永远都不可能替代的技能 Source Guide.md>) | 2026-05-23 01:58:00+08:00 | 141 | draft |
| [sources/概念 因果 规律 机制与知识 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/概念 因果 规律 机制与知识 Source Guide.md>) | 2026-05-24 00:02:57+08:00 | 140 | draft |
| [sources/知识结构 认知结构与概念地图问答 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/知识结构 认知结构与概念地图问答 Source Guide.md>) | 2026-05-24 16:54:50+08:00 | 140 | draft |
| [sources/知识结构概念解剖 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/知识结构概念解剖 Source Guide.md>) | 2026-05-24 16:46:35+08:00 | 140 | draft |
| [sources/知识论圆桌 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/知识论圆桌 Source Guide.md>) | 2026-05-24 16:47:28+08:00 | 140 | draft |
| [sources/知识论概念解剖 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/知识论概念解剖 Source Guide.md>) | 2026-05-24 15:56:29+08:00 | 140 | draft |
| [sources/知识论的秩 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/知识论的秩 Source Guide.md>) | 2026-05-24 15:45:49+08:00 | 140 | draft |
| [sources/Bayes-Consistent Agentic Orchestration Paper River Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Bayes-Consistent Agentic Orchestration Paper River Source Guide.md>) | 2026-05-26 14:03:46+08:00 | 138 | draft |
| [sources/光速不变与相对性原则问答 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/光速不变与相对性原则问答 Source Guide.md>) | 2026-05-26 14:07:23+08:00 | 138 | draft |
| [sources/知识图谱的秩 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/知识图谱的秩 Source Guide.md>) | 2026-05-26 16:06:31+08:00 | 138 | draft |
| [sources/Fallacies of Distributed Computing Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Fallacies of Distributed Computing Source Guide.md>) | 2026-05-27T00:49:30+0800 | 137 | draft |
| [sources/Humans and Agents in Software Engineering Loops Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Humans and Agents in Software Engineering Loops Source Guide.md>) | 2026-05-27T23:47:19+0800 | 137 | draft |
| [sources/React 状态范围与复杂全局状态 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/React 状态范围与复杂全局状态 Source Guide.md>) | 2026-05-27T00:37:25+0800 | 137 | draft |
| [sources/Second-System Effect Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Second-System Effect Source Guide.md>) | 2026-05-27T00:43:06+0800 | 137 | draft |
| [sources/web_chunk.md](</Users/zenk/study/wiki/wiki/sources/web_chunk.md>) | 2026-05-27 00:41:19+08:00 | 137 | draft |
| [syntheses/总结式读书的认知损失.md](</Users/zenk/study/wiki/wiki/syntheses/总结式读书的认知损失.md>) | 2026-05-27T23:13:01+0800 | 137 | draft |
| [sources/AI 软件工程问答 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/AI 软件工程问答 Source Guide.md>) | 2026-05-28T20:28:50+0800 | 136 | draft |
| [sources/Agent Harness Engineering Survey Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Agent Harness Engineering Survey Source Guide.md>) | 2026-05-28T19:37:07+0800 | 136 | draft |
| [sources/Maintainability Sensors for Coding Agents Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Maintainability Sensors for Coding Agents Source Guide.md>) | 2026-05-28T23:40:45+0800 | 136 | draft |
| [sources/快思考慢思考物理机制问答 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/快思考慢思考物理机制问答 Source Guide.md>) | 2026-05-28T12:35:55+0800 | 136 | draft |
| [sources/大模型时代软件工程的本质与演进 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/大模型时代软件工程的本质与演进 Source Guide.md>) | 2026-05-29T22:20:57+0800 | 135 | draft |
| [sources/Grokking Simplicity Taming FP Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Grokking Simplicity Taming FP Source Guide.md>) | 2026-05-30T18:11:07+0800 | 134 | draft |
| [sources/学会提问 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/学会提问 Source Guide.md>) | 2026-05-30T23:29:58+0800 | 134 | draft |
| [sources/软件工程中的稳定性治理的秩 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/软件工程中的稳定性治理的秩 Source Guide.md>) | 2026-05-30T17:35:01+0800 | 134 | draft |
| [sources/高难度沟通 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/高难度沟通 Source Guide.md>) | 2026-05-30T18:30:04+0800 | 134 | draft |
| [sources/GEPA Paper River Source Guide.md](</Users/zenk/study/wiki/wiki/sources/GEPA Paper River Source Guide.md>) | 2026-05-31T11:35:17+0800 | 133 | draft |
| [sources/COLLEAGUE.SKILL Paper Source Guide.md](</Users/zenk/study/wiki/wiki/sources/COLLEAGUE.SKILL Paper Source Guide.md>) | 2026-06-01T16:18:53+0800 | 132 | draft |
| [concepts/Feedback Flywheel.md](</Users/zenk/study/wiki/wiki/concepts/Feedback Flywheel.md>) | 2026-06-09 14:38:22+08:00 | 124 | draft |
| [concepts/Harness Ratchet.md](</Users/zenk/study/wiki/wiki/concepts/Harness Ratchet.md>) | 2026-06-09 14:38:22+08:00 | 124 | draft |
| [concepts/Human-LLM Co-Planning Interaction Space.md](</Users/zenk/study/wiki/wiki/concepts/Human-LLM Co-Planning Interaction Space.md>) | 2026-06-09 14:38:26+08:00 | 124 | draft |
| [concepts/Law of Unintended Consequences.md](</Users/zenk/study/wiki/wiki/concepts/Law of Unintended Consequences.md>) | 2026-06-09 10:20:40+08:00 | 124 | draft |
| [concepts/Workflow Graph Orchestration.md](</Users/zenk/study/wiki/wiki/concepts/Workflow Graph Orchestration.md>) | 2026-06-09 14:38:26+08:00 | 124 | draft |
| [sources/Human-LLM Collaborative Planning Paper Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Human-LLM Collaborative Planning Paper Source Guide.md>) | 2026-06-09 14:38:26+08:00 | 124 | draft |
| [sources/Law of Unintended Consequences Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Law of Unintended Consequences Source Guide.md>) | 2026-06-09 10:20:40+08:00 | 124 | draft |
| [topics/TRAE Agent Capability Preparation Plan.md](</Users/zenk/study/wiki/wiki/topics/TRAE Agent Capability Preparation Plan.md>) | 2026-06-09 10:56:14+08:00 | 124 | draft |
| [sources/Memory-as-a-Tool Paper River Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Memory-as-a-Tool Paper River Source Guide.md>) | 2026-06-10 21:35:12+08:00 | 123 | draft |
| [_meta/taxonomy.md](</Users/zenk/study/wiki/wiki/_meta/taxonomy.md>) | 2026-06-11T22:29:33+0800 | 122 | draft |
| [concepts/DORA Metrics.md](</Users/zenk/study/wiki/wiki/concepts/DORA Metrics.md>) | 2026-06-11 22:29:33+08:00 | 122 | draft |
| [sources/DORA Metrics History Source Guide.md](</Users/zenk/study/wiki/wiki/sources/DORA Metrics History Source Guide.md>) | 2026-06-11 22:29:33+08:00 | 122 | draft |
| [sources/DORA Metrics Source Guide.md](</Users/zenk/study/wiki/wiki/sources/DORA Metrics Source Guide.md>) | 2026-06-11 22:29:33+08:00 | 122 | draft |
| [sources/Raw Experience to Skill Consumption Paper Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Raw Experience to Skill Consumption Paper Source Guide.md>) | 2026-06-11T22:36:02+0800 | 122 | draft |
| [sources/SkillOpt Paper River Source Guide.md](</Users/zenk/study/wiki/wiki/sources/SkillOpt Paper River Source Guide.md>) | 2026-06-11T10:39:52+0800 | 122 | draft |
| [sources/SkillOpt Paper Source Guide.md](</Users/zenk/study/wiki/wiki/sources/SkillOpt Paper Source Guide.md>) | 2026-06-11T11:00:54+0800 | 122 | draft |
| [sources/发现和定义问题 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/发现和定义问题 Source Guide.md>) | 2026-06-11 10:02:42+08:00 | 122 | draft |
| [syntheses/Quality Engineering Three Generators.md](</Users/zenk/study/wiki/wiki/syntheses/Quality Engineering Three Generators.md>) | 2026-06-11 17:49:52+08:00 | 122 | draft |
| [sources/AI 工程化不是提效 是换主回路 QA Source Guide.md](</Users/zenk/study/wiki/wiki/sources/AI 工程化不是提效 是换主回路 QA Source Guide.md>) | 2026-06-13T18:20:57+0800 | 120 | draft |
| [sources/四层次原因分析法 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/四层次原因分析法 Source Guide.md>) | 2026-06-13T10:44:58+0800 | 120 | draft |
| [sources/软件工程真正降临 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/软件工程真正降临 Source Guide.md>) | 2026-06-13T18:08:13+0800 | 120 | draft |
| [concepts/可计算性模型.md](</Users/zenk/study/wiki/wiki/concepts/可计算性模型.md>) | 2026-06-17T01:02:44+0800 | 116 | draft |
| [sources/可计算性问答 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/可计算性问答 Source Guide.md>) | 2026-06-17T01:12:00+0800 | 116 | draft |
| [concepts/LLM 协作思维阶段.md](</Users/zenk/study/wiki/wiki/concepts/LLM 协作思维阶段.md>) | 2026-06-18T00:12:11+0800 | 115 | draft |
| [concepts/论理词与范畴词.md](</Users/zenk/study/wiki/wiki/concepts/论理词与范畴词.md>) | 2026-06-18T00:12:11+0800 | 115 | draft |
| [sources/贝尔曼方程与大模型意识圆桌 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/贝尔曼方程与大模型意识圆桌 Source Guide.md>) | 2026-06-18T00:10:43+0800 | 115 | draft |
| [concepts/Codebase Retrieval Index.md](</Users/zenk/study/wiki/wiki/concepts/Codebase Retrieval Index.md>) | 2026-06-19T09:30:54+0800 | 114 | draft |
| [concepts/Conformed Dimension.md](</Users/zenk/study/wiki/wiki/concepts/Conformed Dimension.md>) | 2026-06-19T10:40:26+0800 | 114 | draft |
| [concepts/Data Warehouse Bus Matrix.md](</Users/zenk/study/wiki/wiki/concepts/Data Warehouse Bus Matrix.md>) | 2026-06-19T10:40:26+0800 | 114 | draft |
| [concepts/Dimension Table.md](</Users/zenk/study/wiki/wiki/concepts/Dimension Table.md>) | 2026-06-19T10:40:26+0800 | 114 | draft |
| [concepts/Dimensional Design Grain.md](</Users/zenk/study/wiki/wiki/concepts/Dimensional Design Grain.md>) | 2026-06-19T10:40:26+0800 | 114 | draft |
| [concepts/Fact Table.md](</Users/zenk/study/wiki/wiki/concepts/Fact Table.md>) | 2026-06-19T10:40:26+0800 | 114 | draft |
| [concepts/Slowly Changing Dimension.md](</Users/zenk/study/wiki/wiki/concepts/Slowly Changing Dimension.md>) | 2026-06-19T10:40:26+0800 | 114 | draft |
| [concepts/生产资料与生产要素.md](</Users/zenk/study/wiki/wiki/concepts/生产资料与生产要素.md>) | 2026-06-19T21:44:08+0800 | 114 | draft |
| [sources/Cursor Codebase Indexing Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Cursor Codebase Indexing Source Guide.md>) | 2026-06-19T09:30:54+0800 | 114 | draft |
| [sources/Kimball Dimensional Modeling Techniques Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Kimball Dimensional Modeling Techniques Source Guide.md>) | 2026-06-19T10:40:26+0800 | 114 | draft |
| [syntheses/LLM Serving Request Structure.md](</Users/zenk/study/wiki/wiki/syntheses/LLM Serving Request Structure.md>) | 2026-06-19T08:24:07+0800 | 114 | draft |
| [topics/Dimensional Modeling.md](</Users/zenk/study/wiki/wiki/topics/Dimensional Modeling.md>) | 2026-06-19T10:40:26+0800 | 114 | draft |
| [sources/Agentic Reasoning for LLMs Paper Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Agentic Reasoning for LLMs Paper Source Guide.md>) | 2026-06-21T13:32:21+0800 | 112 | draft |
| [sources/佛家觉悟结构 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/佛家觉悟结构 Source Guide.md>) | 2026-06-21T13:45:05+0800 | 112 | draft |
| [syntheses/Agent Skill Implementation Landscape.md](</Users/zenk/study/wiki/wiki/syntheses/Agent Skill Implementation Landscape.md>) | 2026-06-21T15:34:41+0800 | 112 | draft |
| [syntheses/Zima Blue 自我回归与无我.md](</Users/zenk/study/wiki/wiki/syntheses/Zima Blue 自我回归与无我.md>) | 2026-06-21T19:49:20+0800 | 112 | draft |
| [concepts/Analysis.md](</Users/zenk/study/wiki/wiki/concepts/Analysis.md>) | 2026-06-23 14:35:24+00:00 | 110 | draft |
| [sources/五大思维三层架构 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/五大思维三层架构 Source Guide.md>) | 2026-06-23 15:02:00+00:00 | 110 | draft |
| [sources/拆解 让复杂问题变清晰 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/拆解 让复杂问题变清晰 Source Guide.md>) | 2026-06-23 14:35:24+00:00 | 110 | draft |
| [syntheses/Coding Agent Debugging Skills as Evidence Gates.md](</Users/zenk/study/wiki/wiki/syntheses/Coding Agent Debugging Skills as Evidence Gates.md>) | 2026-06-23T00:47:58+0800 | 110 | draft |
| [topics/Categorical Thinking.md](</Users/zenk/study/wiki/wiki/topics/Categorical Thinking.md>) | 2026-06-23 14:35:24+00:00 | 110 | draft |
| [topics/Critical Thinking.md](</Users/zenk/study/wiki/wiki/topics/Critical Thinking.md>) | 2026-06-23 14:35:24+00:00 | 110 | draft |
| [topics/Thinking in Systems.md](</Users/zenk/study/wiki/wiki/topics/Thinking in Systems.md>) | 2026-06-23 14:35:24+00:00 | 110 | draft |
| [sources/Designing Refining and Maintaining Agent Skills at Perplexity Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Designing Refining and Maintaining Agent Skills at Perplexity Source Guide.md>) | 2026-06-24T12:01:01+0800 | 109 | draft |
| [concepts/Evidence Question Decomposition.md](</Users/zenk/study/wiki/wiki/concepts/Evidence Question Decomposition.md>) | 2026-06-27T02:24:07+0800 | 106 | draft |
| [concepts/思维模式与思维框架.md](</Users/zenk/study/wiki/wiki/concepts/思维模式与思维框架.md>) | 2026-06-28T18:05:00+0800 | 105 | draft |
| [sources/AI 什么都能写与软件价值重心转移 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/AI 什么都能写与软件价值重心转移 Source Guide.md>) | 2026-06-28T17:06:04+0800 | 105 | draft |
| [concepts/囚徒困境.md](</Users/zenk/study/wiki/wiki/concepts/囚徒困境.md>) | 2026-07-03 14:07:01+08:00 | 100 | draft |
| [sources/Vibe 时代的软件工程.md](</Users/zenk/study/wiki/wiki/sources/Vibe 时代的软件工程.md>) | 2026-07-03 21:44:55+08:00 | 100 | draft |
| [concepts/Agent Skill.md](</Users/zenk/study/wiki/wiki/concepts/Agent Skill.md>) | 2026-07-04T13:49:20+0800 | 99 | draft |
| [concepts/Agentic Coding Unknowns.md](</Users/zenk/study/wiki/wiki/concepts/Agentic Coding Unknowns.md>) | 2026-07-04T16:59:13+0800 | 99 | draft |
| [concepts/Computational and Inferential Controls.md](</Users/zenk/study/wiki/wiki/concepts/Computational and Inferential Controls.md>) | 2026-07-04T13:49:20+0800 | 99 | draft |
| [concepts/Encoding Team Standards.md](</Users/zenk/study/wiki/wiki/concepts/Encoding Team Standards.md>) | 2026-07-04T13:49:20+0800 | 99 | draft |
| [concepts/Event-Driven Agent Loop.md](</Users/zenk/study/wiki/wiki/concepts/Event-Driven Agent Loop.md>) | 2026-07-04T23:00:06+0800 | 99 | draft |
| [sources/Agentic Coding Unknowns Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Agentic Coding Unknowns Source Guide.md>) | 2026-07-04T16:59:13+0800 | 99 | draft |
| [sources/Block Agent Skills Design Principles Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Block Agent Skills Design Principles Source Guide.md>) | 2026-07-04T13:49:20+0800 | 99 | draft |
| [sources/The Art of Loop Engineering Source Guide.md](</Users/zenk/study/wiki/wiki/sources/The Art of Loop Engineering Source Guide.md>) | 2026-07-04T23:00:06+0800 | 99 | draft |
| [topics/AI Skills Workflow.md](</Users/zenk/study/wiki/wiki/topics/AI Skills Workflow.md>) | 2026-07-04T16:59:13+0800 | 99 | draft |
| [concepts/Agent Evaluation CLASSic Framework.md](</Users/zenk/study/wiki/wiki/concepts/Agent Evaluation CLASSic Framework.md>) | 2026-07-05T12:25:46+0800 | 98 | draft |
| [concepts/Agent Transformer.md](</Users/zenk/study/wiki/wiki/concepts/Agent Transformer.md>) | 2026-07-05T12:25:46+0800 | 98 | draft |
| [concepts/姓氏名与字.md](</Users/zenk/study/wiki/wiki/concepts/姓氏名与字.md>) | 2026-07-05T16:46:13+0800 | 98 | draft |
| [concepts/幂律分布与正态分布.md](</Users/zenk/study/wiki/wiki/concepts/幂律分布与正态分布.md>) | 2026-07-05T13:22:43+0800 | 98 | draft |
| [sources/AI Agent Systems Architectures Applications and Evaluation Paper Source Guide.md](</Users/zenk/study/wiki/wiki/sources/AI Agent Systems Architectures Applications and Evaluation Paper Source Guide.md>) | 2026-07-05T12:25:46+0800 | 98 | draft |
| [sources/Agent Systems Papers Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Agent Systems Papers Source Guide.md>) | 2026-07-05T12:25:46+0800 | 98 | draft |
| [sources/Zawinskis Law Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Zawinskis Law Source Guide.md>) | 2026-07-05T17:55:03+0800 | 98 | draft |
| [syntheses/Agent System Design Space.md](</Users/zenk/study/wiki/wiki/syntheses/Agent System Design Space.md>) | 2026-07-05T12:25:46+0800 | 98 | draft |
| [concepts/Loop Engineering.md](</Users/zenk/study/wiki/wiki/concepts/Loop Engineering.md>) | 2026-07-07 21:07:28+08:00 | 96 | draft |
| [sources/Agent Engineering Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Agent Engineering Source Guide.md>) | 2026-07-07 21:07:28+08:00 | 96 | draft |
| [sources/Codex Maxxing for Long Running Work Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Codex Maxxing for Long Running Work Source Guide.md>) | 2026-07-07 21:07:28+08:00 | 96 | draft |
| [maps/Software Analysis Map.md](</Users/zenk/study/wiki/wiki/maps/Software Analysis Map.md>) | 2026-07-10 20:15:07+08:00 | 93 | draft |
| [concepts/Vibe Coding.md](</Users/zenk/study/wiki/wiki/concepts/Vibe Coding.md>) | 2026-07-11T23:53:54+0800 | 92 | draft |
| [concepts/五大思维三层架构.md](</Users/zenk/study/wiki/wiki/concepts/五大思维三层架构.md>) | 2026-07-11T23:53:54+0800 | 92 | draft |
| [concepts/方法论双循环.md](</Users/zenk/study/wiki/wiki/concepts/方法论双循环.md>) | 2026-07-11T23:53:54+0800 | 92 | draft |
| [concepts/问题解决铁三角.md](</Users/zenk/study/wiki/wiki/concepts/问题解决铁三角.md>) | 2026-07-11T23:53:54+0800 | 92 | draft |
| [maps/Software Design Map.md](</Users/zenk/study/wiki/wiki/maps/Software Design Map.md>) | 2026-07-11T23:46:22+0800 | 92 | draft |
| [sources/Harness Engineering Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Harness Engineering Source Guide.md>) | 2026-07-11T23:53:54+0800 | 92 | draft |
| [sources/问题解决的终极模型：思维、方法与问题的“铁三角”如何共同进化.md](</Users/zenk/study/wiki/wiki/sources/问题解决的终极模型：思维、方法与问题的“铁三角”如何共同进化.md>) | 2026-07-11T23:51:59+0800 | 92 | draft |
| [sources/问题解决铁三角 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/问题解决铁三角 Source Guide.md>) | 2026-07-11T23:53:54+0800 | 92 | draft |
| [syntheses/Business Analysis to Software Design.md](</Users/zenk/study/wiki/wiki/syntheses/Business Analysis to Software Design.md>) | 2026-07-11T23:51:59+0800 | 92 | draft |
| [topics/Mental Models.md](</Users/zenk/study/wiki/wiki/topics/Mental Models.md>) | 2026-07-11T23:53:54+0800 | 92 | draft |
| [topics/Problem Framing.md](</Users/zenk/study/wiki/wiki/topics/Problem Framing.md>) | 2026-07-11T23:53:54+0800 | 92 | draft |
| [topics/Spec-Driven Development.md](</Users/zenk/study/wiki/wiki/topics/Spec-Driven Development.md>) | 2026-07-11T23:53:54+0800 | 92 | draft |
| [topics/Testing Strategy.md](</Users/zenk/study/wiki/wiki/topics/Testing Strategy.md>) | 2026-07-11T23:53:54+0800 | 92 | draft |
| [concepts/AI Coding Information-Theoretic Framework.md](</Users/zenk/study/wiki/wiki/concepts/AI Coding Information-Theoretic Framework.md>) | 2026-07-12T23:19:18+0800 | 91 | draft |
| [concepts/Agent Loop Human Judgment Positions.md](</Users/zenk/study/wiki/wiki/concepts/Agent Loop Human Judgment Positions.md>) | 2026-07-12T00:07:31+0800 | 91 | draft |
| [concepts/Code Expression for Human Understanding.md](</Users/zenk/study/wiki/wiki/concepts/Code Expression for Human Understanding.md>) | 2026-07-12T00:07:31+0800 | 91 | draft |
| [concepts/Cognitive Debt.md](</Users/zenk/study/wiki/wiki/concepts/Cognitive Debt.md>) | 2026-07-12T00:30:14+0800 | 91 | draft |
| [concepts/Context Information Density.md](</Users/zenk/study/wiki/wiki/concepts/Context Information Density.md>) | 2026-07-12T23:19:18+0800 | 91 | draft |
| [concepts/Dependency-Ordered Decision Making.md](</Users/zenk/study/wiki/wiki/concepts/Dependency-Ordered Decision Making.md>) | 2026-07-12T14:12:03+0800 | 91 | draft |
| [concepts/业务隐含复杂度.md](</Users/zenk/study/wiki/wiki/concepts/业务隐含复杂度.md>) | 2026-07-12T00:07:31+0800 | 91 | draft |
| [concepts/工程复杂度共同结构.md](</Users/zenk/study/wiki/wiki/concepts/工程复杂度共同结构.md>) | 2026-07-12T00:07:31+0800 | 91 | draft |
| [sources/AI Coding 信息论框架 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/AI Coding 信息论框架 Source Guide.md>) | 2026-07-12T23:19:18+0800 | 91 | draft |
| [sources/Skills for the Future Software Profession Paper Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Skills for the Future Software Profession Paper Source Guide.md>) | 2026-07-12T00:30:14+0800 | 91 | draft |
| [syntheses/AGENTS.md as Repository Operation Contract.md](</Users/zenk/study/wiki/wiki/syntheses/AGENTS.md as Repository Operation Contract.md>) | 2026-07-12T23:18:57+0800 | 91 | draft |
| [syntheses/AI Harness × Testing Strategy.md](</Users/zenk/study/wiki/wiki/syntheses/AI Harness × Testing Strategy.md>) | 2026-07-12T00:07:31+0800 | 91 | draft |
| [syntheses/AI Memory × Context Graph.md](</Users/zenk/study/wiki/wiki/syntheses/AI Memory × Context Graph.md>) | 2026-07-12T00:07:31+0800 | 91 | draft |
| [syntheses/AI 泡沫判断的结构.md](</Users/zenk/study/wiki/wiki/syntheses/AI 泡沫判断的结构.md>) | 2026-07-12T00:07:31+0800 | 91 | draft |
| [syntheses/Agent Skill × Context Management.md](</Users/zenk/study/wiki/wiki/syntheses/Agent Skill × Context Management.md>) | 2026-07-12T00:07:31+0800 | 91 | draft |
| [syntheses/Agent Skill × Harness Ratchet.md](</Users/zenk/study/wiki/wiki/syntheses/Agent Skill × Harness Ratchet.md>) | 2026-07-12T00:07:31+0800 | 91 | draft |
| [syntheses/Agentic Engineering × Verification Loop.md](</Users/zenk/study/wiki/wiki/syntheses/Agentic Engineering × Verification Loop.md>) | 2026-07-12T00:07:31+0800 | 91 | draft |
| [syntheses/Coding Agent User Harness × Verification Loop.md](</Users/zenk/study/wiki/wiki/syntheses/Coding Agent User Harness × Verification Loop.md>) | 2026-07-12T00:07:31+0800 | 91 | draft |
| [syntheses/Harness Ratchet × Feedback Flywheel.md](</Users/zenk/study/wiki/wiki/syntheses/Harness Ratchet × Feedback Flywheel.md>) | 2026-07-12T00:07:31+0800 | 91 | draft |
| [syntheses/Human Agency × Narrative.md](</Users/zenk/study/wiki/wiki/syntheses/Human Agency × Narrative.md>) | 2026-07-12T00:07:31+0800 | 91 | draft |
| [syntheses/Learning Methodology × Mental Models.md](</Users/zenk/study/wiki/wiki/syntheses/Learning Methodology × Mental Models.md>) | 2026-07-12T00:07:31+0800 | 91 | draft |
| [syntheses/Permissionless Leverage × Wealth Creation.md](</Users/zenk/study/wiki/wiki/syntheses/Permissionless Leverage × Wealth Creation.md>) | 2026-07-12T00:07:31+0800 | 91 | draft |
| [syntheses/Thinking and Judgment Workflow.md](</Users/zenk/study/wiki/wiki/syntheses/Thinking and Judgment Workflow.md>) | 2026-07-12T00:07:31+0800 | 91 | draft |
| [syntheses/Tool and Skill Boundary in Agent Harnesses.md](</Users/zenk/study/wiki/wiki/syntheses/Tool and Skill Boundary in Agent Harnesses.md>) | 2026-07-12T00:07:31+0800 | 91 | draft |
| [syntheses/Verification Loop × Feedback Flywheel.md](</Users/zenk/study/wiki/wiki/syntheses/Verification Loop × Feedback Flywheel.md>) | 2026-07-12T00:07:31+0800 | 91 | draft |
| [syntheses/丝绸之路中的宗教组织力量.md](</Users/zenk/study/wiki/wiki/syntheses/丝绸之路中的宗教组织力量.md>) | 2026-07-12T00:07:31+0800 | 91 | draft |
| [syntheses/产品行业核心概念地图.md](</Users/zenk/study/wiki/wiki/syntheses/产品行业核心概念地图.md>) | 2026-07-12T00:07:31+0800 | 91 | draft |
| [syntheses/类和对象结构图的建模作用.md](</Users/zenk/study/wiki/wiki/syntheses/类和对象结构图的建模作用.md>) | 2026-07-12T00:07:31+0800 | 91 | draft |
| [topics/Classification Procedure.md](</Users/zenk/study/wiki/wiki/topics/Classification Procedure.md>) | 2026-07-12T00:07:31+0800 | 91 | draft |
| [topics/Context Management.md](</Users/zenk/study/wiki/wiki/topics/Context Management.md>) | 2026-07-12T23:19:18+0800 | 91 | draft |

</details>

### Confidence drift — 210 heuristic candidates

存储值与按 sources 字符串估算的值差异超过 0.05。全库没有足够的 source_id/质量元数据支撑确定重算；站点、PDF、对话和重复材料的分类会影响结果。sources=[] 的治理/占位页保留已有默认值，避免对空平均数生造置信度。
其中 176 项为普通页面，34 项为综合页面。后者应优先按 `min(input_pages.base_confidence)` 规则核验，下表中的来源数量公式只是筛查值。这里没有自动改写任何 base_confidence。

<details>
<summary>全部 210 项置信度候选</summary>

| 页面 | 存储 | 筛查重算 | 差值 | 来源数 | 综合页 |
| --- | --- | --- | --- | --- | --- |
| [concepts/AI Memory 4W Taxonomy.md](</Users/zenk/study/wiki/wiki/concepts/AI Memory 4W Taxonomy.md>) | 0.57 | 0.4417 | 0.1283 | 1 | 否 |
| [concepts/Agent Evaluation CLASSic Framework.md](</Users/zenk/study/wiki/wiki/concepts/Agent Evaluation CLASSic Framework.md>) | 0.67 | 0.8333 | 0.1633 | 2 | 否 |
| [concepts/Agent Loop Human Judgment Positions.md](</Users/zenk/study/wiki/wiki/concepts/Agent Loop Human Judgment Positions.md>) | 0.42 | 0.5583 | 0.1383 | 2 | 否 |
| [concepts/Agent Skill Design Patterns.md](</Users/zenk/study/wiki/wiki/concepts/Agent Skill Design Patterns.md>) | 0.44 | 0.6083 | 0.1683 | 2 | 否 |
| [concepts/Agent Skill.md](</Users/zenk/study/wiki/wiki/concepts/Agent Skill.md>) | 0.44 | 0.8393 | 0.3993 | 7 | 否 |
| [concepts/Agent Tool.md](</Users/zenk/study/wiki/wiki/concepts/Agent Tool.md>) | 0.44 | 0.775 | 0.335 | 3 | 否 |
| [concepts/Agentic Coding Unknowns.md](</Users/zenk/study/wiki/wiki/concepts/Agentic Coding Unknowns.md>) | 0.37 | 0.4417 | 0.0717 | 1 | 否 |
| [concepts/Agentic Engineering.md](</Users/zenk/study/wiki/wiki/concepts/Agentic Engineering.md>) | 0.37 | 0.7656 | 0.3956 | 8 | 否 |
| [concepts/Analogy-Making.md](</Users/zenk/study/wiki/wiki/concepts/Analogy-Making.md>) | 0.32 | 0.7667 | 0.4467 | 3 | 否 |
| [concepts/Analysis.md](</Users/zenk/study/wiki/wiki/concepts/Analysis.md>) | 0.37 | 0.5583 | 0.1883 | 2 | 否 |
| [concepts/Application.md](</Users/zenk/study/wiki/wiki/concepts/Application.md>) | 0.37 | 0.795 | 0.425 | 5 | 否 |
| [concepts/Arithmetic Intensity.md](</Users/zenk/study/wiki/wiki/concepts/Arithmetic Intensity.md>) | 0.37 | 0.4417 | 0.0717 | 1 | 否 |
| [concepts/Arrow of Time.md](</Users/zenk/study/wiki/wiki/concepts/Arrow of Time.md>) | 0.42 | 0.7583 | 0.3383 | 3 | 否 |
| [concepts/Attention as the Scarce Resource.md](</Users/zenk/study/wiki/wiki/concepts/Attention as the Scarce Resource.md>) | 0.4 | 0.5958 | 0.1958 | 2 | 否 |
| [concepts/Autoregressive Decoding.md](</Users/zenk/study/wiki/wiki/concepts/Autoregressive Decoding.md>) | 0.37 | 0.5958 | 0.2258 | 2 | 否 |
| [concepts/Belief and Attitude.md](</Users/zenk/study/wiki/wiki/concepts/Belief and Attitude.md>) | 0.42 | 0.7167 | 0.2967 | 3 | 否 |
| [concepts/Causal Reasoning.md](</Users/zenk/study/wiki/wiki/concepts/Causal Reasoning.md>) | 0.42 | 0.5583 | 0.1383 | 2 | 否 |
| [concepts/Class as Learned Invariance.md](</Users/zenk/study/wiki/wiki/concepts/Class as Learned Invariance.md>) | 0.44 | 0.5958 | 0.1558 | 2 | 否 |
| [concepts/Coding Agent User Harness.md](</Users/zenk/study/wiki/wiki/concepts/Coding Agent User Harness.md>) | 0.44 | 0.775 | 0.335 | 3 | 否 |
| [concepts/Cognitive Engineering.md](</Users/zenk/study/wiki/wiki/concepts/Cognitive Engineering.md>) | 0.44 | 0.5708 | 0.1308 | 2 | 否 |
| [concepts/Company Brain.md](</Users/zenk/study/wiki/wiki/concepts/Company Brain.md>) | 0.44 | 0.6083 | 0.1683 | 2 | 否 |
| [concepts/Computational and Inferential Controls.md](</Users/zenk/study/wiki/wiki/concepts/Computational and Inferential Controls.md>) | 0.44 | 0.6083 | 0.1683 | 2 | 否 |
| [concepts/Concept.md](</Users/zenk/study/wiki/wiki/concepts/Concept.md>) | 0.32 | 0.4167 | 0.0967 | 1 | 否 |
| [concepts/Conformed Dimension.md](</Users/zenk/study/wiki/wiki/concepts/Conformed Dimension.md>) | 0.62 | 0.4417 | 0.1783 | 1 | 否 |
| [concepts/Context Graph.md](</Users/zenk/study/wiki/wiki/concepts/Context Graph.md>) | 0.44 | 0.6083 | 0.1683 | 2 | 否 |
| [concepts/Continuous Batching.md](</Users/zenk/study/wiki/wiki/concepts/Continuous Batching.md>) | 0.44 | 0.7667 | 0.3267 | 3 | 否 |
| [concepts/Creation.md](</Users/zenk/study/wiki/wiki/concepts/Creation.md>) | 0.37 | 0.795 | 0.425 | 5 | 否 |
| [concepts/DORA Metrics.md](</Users/zenk/study/wiki/wiki/concepts/DORA Metrics.md>) | 0.78 | 0.6083 | 0.1717 | 2 | 否 |
| [concepts/Data Warehouse Bus Matrix.md](</Users/zenk/study/wiki/wiki/concepts/Data Warehouse Bus Matrix.md>) | 0.62 | 0.4417 | 0.1783 | 1 | 否 |
| [concepts/Dependency-Ordered Decision Making.md](</Users/zenk/study/wiki/wiki/concepts/Dependency-Ordered Decision Making.md>) | 0.42 | 0.6458 | 0.2258 | 2 | 否 |
| [concepts/Dimension Table.md](</Users/zenk/study/wiki/wiki/concepts/Dimension Table.md>) | 0.62 | 0.4417 | 0.1783 | 1 | 否 |
| [concepts/Dimensional Design Grain.md](</Users/zenk/study/wiki/wiki/concepts/Dimensional Design Grain.md>) | 0.62 | 0.4417 | 0.1783 | 1 | 否 |
| [concepts/Discovery Replay Simulator.md](</Users/zenk/study/wiki/wiki/concepts/Discovery Replay Simulator.md>) | 0.42 | 0.775 | 0.355 | 3 | 否 |
| [concepts/Encoding Team Standards.md](</Users/zenk/study/wiki/wiki/concepts/Encoding Team Standards.md>) | 0.44 | 0.6083 | 0.1683 | 2 | 否 |
| [concepts/Event-Driven Agent Loop.md](</Users/zenk/study/wiki/wiki/concepts/Event-Driven Agent Loop.md>) | 0.62 | 0.4417 | 0.1783 | 1 | 否 |
| [concepts/Executable Specification.md](</Users/zenk/study/wiki/wiki/concepts/Executable Specification.md>) | 0.67 | 0.9062 | 0.2362 | 4 | 否 |
| [concepts/Fact Table.md](</Users/zenk/study/wiki/wiki/concepts/Fact Table.md>) | 0.62 | 0.4417 | 0.1783 | 1 | 否 |
| [concepts/Feedback Loops.md](</Users/zenk/study/wiki/wiki/concepts/Feedback Loops.md>) | 0.44 | 0.7375 | 0.2975 | 4 | 否 |
| [concepts/Governed Action.md](</Users/zenk/study/wiki/wiki/concepts/Governed Action.md>) | 0.44 | 0.6083 | 0.1683 | 2 | 否 |
| [concepts/Harness Ratchet.md](</Users/zenk/study/wiki/wiki/concepts/Harness Ratchet.md>) | 0.44 | 0.85 | 0.41 | 3 | 否 |
| [concepts/Harnessability.md](</Users/zenk/study/wiki/wiki/concepts/Harnessability.md>) | 0.44 | 0.6083 | 0.1683 | 2 | 否 |
| [concepts/Iceberg Model.md](</Users/zenk/study/wiki/wiki/concepts/Iceberg Model.md>) | 0.57 | 0.4417 | 0.1283 | 1 | 否 |
| [concepts/Interaction Memory.md](</Users/zenk/study/wiki/wiki/concepts/Interaction Memory.md>) | 0.44 | 0.6083 | 0.1683 | 2 | 否 |
| [concepts/Judgment Externalization.md](</Users/zenk/study/wiki/wiki/concepts/Judgment Externalization.md>) | 0.42 | 0.5583 | 0.1383 | 2 | 否 |
| [concepts/KV Cache.md](</Users/zenk/study/wiki/wiki/concepts/KV Cache.md>) | 0.44 | 0.7688 | 0.3288 | 4 | 否 |
| [concepts/Knowledge as Network.md](</Users/zenk/study/wiki/wiki/concepts/Knowledge as Network.md>) | 0.32 | 0.4167 | 0.0967 | 1 | 否 |
| [concepts/LLM.md](</Users/zenk/study/wiki/wiki/concepts/LLM.md>) | 0.44 | 0.7667 | 0.3267 | 3 | 否 |
| [concepts/Law of Unintended Consequences.md](</Users/zenk/study/wiki/wiki/concepts/Law of Unintended Consequences.md>) | 0.32 | 0.4167 | 0.0967 | 1 | 否 |
| [concepts/Leverage Points.md](</Users/zenk/study/wiki/wiki/concepts/Leverage Points.md>) | 0.57 | 0.6708 | 0.1008 | 2 | 否 |
| [concepts/Life as Dissipative Information Structure.md](</Users/zenk/study/wiki/wiki/concepts/Life as Dissipative Information Structure.md>) | 0.42 | 0.5833 | 0.1633 | 2 | 否 |
| [concepts/Linear Layer.md](</Users/zenk/study/wiki/wiki/concepts/Linear Layer.md>) | 0.42 | 0.5958 | 0.1758 | 2 | 否 |
| [concepts/Logit Lens.md](</Users/zenk/study/wiki/wiki/concepts/Logit Lens.md>) | 0.37 | 0.4417 | 0.0717 | 1 | 否 |
| [concepts/Logits.md](</Users/zenk/study/wiki/wiki/concepts/Logits.md>) | 0.42 | 0.5958 | 0.1758 | 2 | 否 |
| [concepts/Long-Running Agent Harness.md](</Users/zenk/study/wiki/wiki/concepts/Long-Running Agent Harness.md>) | 0.6 | 0.7667 | 0.1667 | 3 | 否 |
| [concepts/Mechanism Model.md](</Users/zenk/study/wiki/wiki/concepts/Mechanism Model.md>) | 0.42 | 0.5833 | 0.1633 | 2 | 否 |
| [concepts/Nature of a Question.md](</Users/zenk/study/wiki/wiki/concepts/Nature of a Question.md>) | 0.42 | 0.7333 | 0.3133 | 3 | 否 |
| [concepts/Neural Network Inference Boundary.md](</Users/zenk/study/wiki/wiki/concepts/Neural Network Inference Boundary.md>) | 0.37 | 0.5958 | 0.2258 | 2 | 否 |
| [concepts/Next-Token Pipeline.md](</Users/zenk/study/wiki/wiki/concepts/Next-Token Pipeline.md>) | 0.37 | 0.5958 | 0.2258 | 2 | 否 |
| [concepts/Nutrients Calories and Human Energy Storage.md](</Users/zenk/study/wiki/wiki/concepts/Nutrients Calories and Human Energy Storage.md>) | 0.42 | 0.5833 | 0.1633 | 2 | 否 |
| [concepts/Organizational Memory.md](</Users/zenk/study/wiki/wiki/concepts/Organizational Memory.md>) | 0.44 | 0.6083 | 0.1683 | 2 | 否 |
| [concepts/Positional Encoding.md](</Users/zenk/study/wiki/wiki/concepts/Positional Encoding.md>) | 0.37 | 0.4417 | 0.0717 | 1 | 否 |
| [concepts/Prefill Decode Split.md](</Users/zenk/study/wiki/wiki/concepts/Prefill Decode Split.md>) | 0.44 | 0.7667 | 0.3267 | 3 | 否 |
| [concepts/Prompt Caching.md](</Users/zenk/study/wiki/wiki/concepts/Prompt Caching.md>) | 0.44 | 0.6083 | 0.1683 | 2 | 否 |
| [concepts/Reasoning as Structure Mapping.md](</Users/zenk/study/wiki/wiki/concepts/Reasoning as Structure Mapping.md>) | 0.37 | 0.7333 | 0.3633 | 3 | 否 |
| [concepts/Relation as Contextual Constraint.md](</Users/zenk/study/wiki/wiki/concepts/Relation as Contextual Constraint.md>) | 0.42 | 0.5583 | 0.1383 | 2 | 否 |
| [concepts/Search and Learning as Meta-Methods.md](</Users/zenk/study/wiki/wiki/concepts/Search and Learning as Meta-Methods.md>) | 0.44 | 0.5958 | 0.1558 | 2 | 否 |
| [concepts/Self-Attention.md](</Users/zenk/study/wiki/wiki/concepts/Self-Attention.md>) | 0.37 | 0.4417 | 0.0717 | 1 | 否 |
| [concepts/Semantic File System.md](</Users/zenk/study/wiki/wiki/concepts/Semantic File System.md>) | 0.44 | 0.6083 | 0.1683 | 2 | 否 |
| [concepts/Slowly Changing Dimension.md](</Users/zenk/study/wiki/wiki/concepts/Slowly Changing Dimension.md>) | 0.62 | 0.4417 | 0.1783 | 1 | 否 |
| [concepts/Temporal Memory Validity.md](</Users/zenk/study/wiki/wiki/concepts/Temporal Memory Validity.md>) | 0.32 | 0.4167 | 0.0967 | 1 | 否 |
| [concepts/Token Embedding.md](</Users/zenk/study/wiki/wiki/concepts/Token Embedding.md>) | 0.37 | 0.4417 | 0.0717 | 1 | 否 |
| [concepts/Tokenization.md](</Users/zenk/study/wiki/wiki/concepts/Tokenization.md>) | 0.37 | 0.5958 | 0.2258 | 2 | 否 |
| [concepts/Transformer Feed-Forward Network.md](</Users/zenk/study/wiki/wiki/concepts/Transformer Feed-Forward Network.md>) | 0.37 | 0.4417 | 0.0717 | 1 | 否 |
| [concepts/Transformer Residual Stream.md](</Users/zenk/study/wiki/wiki/concepts/Transformer Residual Stream.md>) | 0.37 | 0.5958 | 0.2258 | 2 | 否 |
| [concepts/Understanding.md](</Users/zenk/study/wiki/wiki/concepts/Understanding.md>) | 0.32 | 0.7542 | 0.4342 | 6 | 否 |
| [concepts/Unembedding and Weight Tying.md](</Users/zenk/study/wiki/wiki/concepts/Unembedding and Weight Tying.md>) | 0.37 | 0.4417 | 0.0717 | 1 | 否 |
| [concepts/Universality of Physical Law.md](</Users/zenk/study/wiki/wiki/concepts/Universality of Physical Law.md>) | 0.4 | 0.7083 | 0.3083 | 2 | 否 |
| [concepts/Verification Gap.md](</Users/zenk/study/wiki/wiki/concepts/Verification Gap.md>) | 0.37 | 0.5583 | 0.1883 | 2 | 否 |
| [concepts/Verifier Hierarchy.md](</Users/zenk/study/wiki/wiki/concepts/Verifier Hierarchy.md>) | 0.32 | 0.4167 | 0.0967 | 1 | 否 |
| [concepts/Workflow Graph Orchestration.md](</Users/zenk/study/wiki/wiki/concepts/Workflow Graph Orchestration.md>) | 0.67 | 0.8333 | 0.1633 | 2 | 否 |
| [concepts/五大思维三层架构.md](</Users/zenk/study/wiki/wiki/concepts/五大思维三层架构.md>) | 0.5 | 0.7333 | 0.2333 | 3 | 否 |
| [concepts/囚徒困境.md](</Users/zenk/study/wiki/wiki/concepts/囚徒困境.md>) | 0.42 | 0.5583 | 0.1383 | 2 | 否 |
| [concepts/方法论双循环.md](</Users/zenk/study/wiki/wiki/concepts/方法论双循环.md>) | 0.44 | 0.3667 | 0.0733 | 1 | 否 |
| [concepts/架构一致性.md](</Users/zenk/study/wiki/wiki/concepts/架构一致性.md>) | 0.37 | 0.7 | 0.33 | 8 | 否 |
| [concepts/架构知识模型.md](</Users/zenk/study/wiki/wiki/concepts/架构知识模型.md>) | 0.37 | 0.7 | 0.33 | 8 | 否 |
| [concepts/架构认知框架.md](</Users/zenk/study/wiki/wiki/concepts/架构认知框架.md>) | 0.37 | 0.7 | 0.33 | 8 | 否 |
| [concepts/重构层次.md](</Users/zenk/study/wiki/wiki/concepts/重构层次.md>) | 0.37 | 0.7 | 0.33 | 8 | 否 |
| [concepts/问题解决铁三角.md](</Users/zenk/study/wiki/wiki/concepts/问题解决铁三角.md>) | 0.44 | 0.3667 | 0.0733 | 1 | 否 |
| [maps/AI Map.md](</Users/zenk/study/wiki/wiki/maps/AI Map.md>) | 0.94 | 0.8875 | 0.0525 | 14 | 否 |
| [maps/CS Map.md](</Users/zenk/study/wiki/wiki/maps/CS Map.md>) | 0.7 | 0.775 | 0.075 | 4 | 否 |
| [maps/Classification Thinking Map.md](</Users/zenk/study/wiki/wiki/maps/Classification Thinking Map.md>) | 0.37 | 0.7167 | 0.3467 | 3 | 否 |
| [maps/Learning Map.md](</Users/zenk/study/wiki/wiki/maps/Learning Map.md>) | 0.32 | 0.725 | 0.405 | 4 | 否 |
| [maps/Management Map.md](</Users/zenk/study/wiki/wiki/maps/Management Map.md>) | 0.57 | 0.6708 | 0.1008 | 2 | 否 |
| [maps/Reading Map.md](</Users/zenk/study/wiki/wiki/maps/Reading Map.md>) | 0.57 | 0.7688 | 0.1988 | 4 | 否 |
| [maps/Self-Evolving Agents Map.md](</Users/zenk/study/wiki/wiki/maps/Self-Evolving Agents Map.md>) | 0.53 | 0.7917 | 0.2617 | 3 | 否 |
| [maps/Software Design Map.md](</Users/zenk/study/wiki/wiki/maps/Software Design Map.md>) | 0.37 | 0.5333 | 0.1633 | 2 | 否 |
| [sources/ADK Skill Design Patterns Source Guide.md](</Users/zenk/study/wiki/wiki/sources/ADK Skill Design Patterns Source Guide.md>) | 0.44 | 0.6083 | 0.1683 | 2 | 否 |
| [sources/AI Agent 三重悖论 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/AI Agent 三重悖论 Source Guide.md>) | 0.32 | 0.4167 | 0.0967 | 1 | 否 |
| [sources/AI Engineering Skills Map Source Guide.md](</Users/zenk/study/wiki/wiki/sources/AI Engineering Skills Map Source Guide.md>) | 0.42 | 0.5958 | 0.1758 | 2 | 否 |
| [sources/AI Evals FAQ Source Guide.md](</Users/zenk/study/wiki/wiki/sources/AI Evals FAQ Source Guide.md>) | 0.42 | 0.5958 | 0.1758 | 2 | 否 |
| [sources/AI Memory Survey Source Guide.md](</Users/zenk/study/wiki/wiki/sources/AI Memory Survey Source Guide.md>) | 0.57 | 0.4417 | 0.1283 | 1 | 否 |
| [sources/Agent Benchmark Landscape Research Report Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Agent Benchmark Landscape Research Report Source Guide.md>) | 0.42 | 0.5583 | 0.1383 | 2 | 否 |
| [sources/Agent Harness Engineering Survey Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Agent Harness Engineering Survey Source Guide.md>) | 0.57 | 0.4417 | 0.1283 | 1 | 否 |
| [sources/Agent Observability Needs Feedback Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Agent Observability Needs Feedback Source Guide.md>) | 0.44 | 0.5958 | 0.1558 | 2 | 否 |
| [sources/Agent Systems Papers Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Agent Systems Papers Source Guide.md>) | 0.67 | 1.0 | 0.33 | 5 | 否 |
| [sources/Agentic Coding Unknowns Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Agentic Coding Unknowns Source Guide.md>) | 0.37 | 0.4417 | 0.0717 | 1 | 否 |
| [sources/Agentic Engineering at Zalando Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Agentic Engineering at Zalando Source Guide.md>) | 0.42 | 0.5958 | 0.1758 | 2 | 否 |
| [sources/Agentic Reasoning for LLMs Paper Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Agentic Reasoning for LLMs Paper Source Guide.md>) | 0.67 | 0.8 | 0.13 | 3 | 否 |
| [sources/Amabile Componential Theory of Creativity Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Amabile Componential Theory of Creativity Source Guide.md>) | 0.57 | 0.4417 | 0.1283 | 1 | 否 |
| [sources/Anti-Patterns in Software Blogging Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Anti-Patterns in Software Blogging Source Guide.md>) | 0.42 | 0.5958 | 0.1758 | 2 | 否 |
| [sources/Bayes-Consistent Agentic Orchestration Paper River Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Bayes-Consistent Agentic Orchestration Paper River Source Guide.md>) | 0.42 | 0.7083 | 0.2883 | 2 | 否 |
| [sources/Building and Deploying AI Applications Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Building and Deploying AI Applications Source Guide.md>) | 0.42 | 0.5958 | 0.1758 | 2 | 否 |
| [sources/Chatham House Rule Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Chatham House Rule Source Guide.md>) | 0.37 | 0.5958 | 0.2258 | 2 | 否 |
| [sources/Clinical Hypnosis Classic Texts Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Clinical Hypnosis Classic Texts Source Guide.md>) | 0.85 | 0.775 | 0.075 | 6 | 否 |
| [sources/Codex Maxxing for Long Running Work Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Codex Maxxing for Long Running Work Source Guide.md>) | 0.62 | 0.4417 | 0.1783 | 1 | 否 |
| [sources/Coding with AI Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Coding with AI Source Guide.md>) | 0.37 | 0.4417 | 0.0717 | 1 | 否 |
| [sources/Company Brain Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Company Brain Source Guide.md>) | 0.44 | 0.6083 | 0.1683 | 2 | 否 |
| [sources/Continual Learning for AI Agents Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Continual Learning for AI Agents Source Guide.md>) | 0.44 | 0.5958 | 0.1558 | 2 | 否 |
| [sources/Csikszentmihalyi Systems Model of Creativity Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Csikszentmihalyi Systems Model of Creativity Source Guide.md>) | 0.57 | 0.4417 | 0.1283 | 1 | 否 |
| [sources/DORA Metrics Source Guide.md](</Users/zenk/study/wiki/wiki/sources/DORA Metrics Source Guide.md>) | 0.62 | 0.4417 | 0.1783 | 1 | 否 |
| [sources/Designing Refining and Maintaining Agent Skills at Perplexity Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Designing Refining and Maintaining Agent Skills at Perplexity Source Guide.md>) | 0.37 | 0.4417 | 0.0717 | 1 | 否 |
| [sources/Dewey Reflective Inquiry Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Dewey Reflective Inquiry Source Guide.md>) | 0.37 | 0.6083 | 0.2383 | 2 | 否 |
| [sources/Dream-RSI Paper Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Dream-RSI Paper Source Guide.md>) | 0.42 | 0.7562 | 0.3362 | 4 | 否 |
| [sources/GEPA Paper River Source Guide.md](</Users/zenk/study/wiki/wiki/sources/GEPA Paper River Source Guide.md>) | 0.37 | 0.8167 | 0.4467 | 3 | 否 |
| [sources/Grokking Simplicity Taming FP Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Grokking Simplicity Taming FP Source Guide.md>) | 0.42 | 0.3667 | 0.0533 | 1 | 否 |
| [sources/How People Learn Transfer Source Guide.md](</Users/zenk/study/wiki/wiki/sources/How People Learn Transfer Source Guide.md>) | 0.37 | 0.4417 | 0.0717 | 1 | 否 |
| [sources/Iceberg Model Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Iceberg Model Source Guide.md>) | 0.57 | 0.4417 | 0.1283 | 1 | 否 |
| [sources/Kimball Dimensional Modeling Techniques Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Kimball Dimensional Modeling Techniques Source Guide.md>) | 0.62 | 0.4417 | 0.1783 | 1 | 否 |
| [sources/LLM Wiki Source Guide.md](</Users/zenk/study/wiki/wiki/sources/LLM Wiki Source Guide.md>) | 0.37 | 0.5958 | 0.2258 | 2 | 否 |
| [sources/Law of Unintended Consequences Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Law of Unintended Consequences Source Guide.md>) | 0.32 | 0.4167 | 0.0967 | 1 | 否 |
| [sources/Life of a Token Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Life of a Token Source Guide.md>) | 0.37 | 0.5958 | 0.2258 | 2 | 否 |
| [sources/Math and AI Misalignment Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Math and AI Misalignment Source Guide.md>) | 0.42 | 0.7667 | 0.3467 | 3 | 否 |
| [sources/Memory-as-a-Tool Paper River Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Memory-as-a-Tool Paper River Source Guide.md>) | 0.39 | 0.8167 | 0.4267 | 3 | 否 |
| [sources/On the Nature of Time Source Guide.md](</Users/zenk/study/wiki/wiki/sources/On the Nature of Time Source Guide.md>) | 0.42 | 0.5958 | 0.1758 | 2 | 否 |
| [sources/Principles of Mechanical Sympathy Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Principles of Mechanical Sympathy Source Guide.md>) | 0.44 | 0.5958 | 0.1558 | 2 | 否 |
| [sources/Prompt Caching Claude Code Case Study Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Prompt Caching Claude Code Case Study Source Guide.md>) | 0.44 | 0.6083 | 0.1683 | 2 | 否 |
| [sources/Prospects for an Engineering Discipline of Software Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Prospects for an Engineering Discipline of Software Source Guide.md>) | 0.42 | 0.8083 | 0.3883 | 3 | 否 |
| [sources/Raw Experience to Skill Consumption Paper Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Raw Experience to Skill Consumption Paper Source Guide.md>) | 0.42 | 0.7083 | 0.2883 | 2 | 否 |
| [sources/Revised Bloom Taxonomy Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Revised Bloom Taxonomy Source Guide.md>) | 0.62 | 0.6958 | 0.0758 | 2 | 否 |
| [sources/SPDD Abstraction First Source Guide.md](</Users/zenk/study/wiki/wiki/sources/SPDD Abstraction First Source Guide.md>) | 0.44 | 0.5958 | 0.1558 | 2 | 否 |
| [sources/SPDD Alignment Source Guide.md](</Users/zenk/study/wiki/wiki/sources/SPDD Alignment Source Guide.md>) | 0.44 | 0.5958 | 0.1558 | 2 | 否 |
| [sources/SPDD Iterative Review Source Guide.md](</Users/zenk/study/wiki/wiki/sources/SPDD Iterative Review Source Guide.md>) | 0.44 | 0.5958 | 0.1558 | 2 | 否 |
| [sources/Schon Reflective Practice Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Schon Reflective Practice Source Guide.md>) | 0.37 | 0.6083 | 0.2383 | 2 | 否 |
| [sources/SkillOS Source Guide.md](</Users/zenk/study/wiki/wiki/sources/SkillOS Source Guide.md>) | 0.44 | 0.8417 | 0.4017 | 3 | 否 |
| [sources/SkillOpt Paper River Source Guide.md](</Users/zenk/study/wiki/wiki/sources/SkillOpt Paper River Source Guide.md>) | 0.42 | 0.7083 | 0.2883 | 2 | 否 |
| [sources/SkillOpt Paper Source Guide.md](</Users/zenk/study/wiki/wiki/sources/SkillOpt Paper Source Guide.md>) | 0.42 | 0.7083 | 0.2883 | 2 | 否 |
| [sources/Software Engineering 3.0 Judgment Shift Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Software Engineering 3.0 Judgment Shift Source Guide.md>) | 0.42 | 0.5583 | 0.1383 | 2 | 否 |
| [sources/Structured-Prompt-Driven Development Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Structured-Prompt-Driven Development Source Guide.md>) | 0.44 | 0.5958 | 0.1558 | 2 | 否 |
| [sources/The AI-Native SDLC Playbook Source Guide.md](</Users/zenk/study/wiki/wiki/sources/The AI-Native SDLC Playbook Source Guide.md>) | 0.62 | 0.4417 | 0.1783 | 1 | 否 |
| [sources/The Art of Loop Engineering Source Guide.md](</Users/zenk/study/wiki/wiki/sources/The Art of Loop Engineering Source Guide.md>) | 0.62 | 0.4417 | 0.1783 | 1 | 否 |
| [sources/The Bitter Lesson Source Guide.md](</Users/zenk/study/wiki/wiki/sources/The Bitter Lesson Source Guide.md>) | 0.5 | 0.5958 | 0.0958 | 2 | 否 |
| [sources/The Physicists Philosophy of Physics Source Guide.md](</Users/zenk/study/wiki/wiki/sources/The Physicists Philosophy of Physics Source Guide.md>) | 0.42 | 0.7875 | 0.3675 | 4 | 否 |
| [sources/Three Constraints for Building Products Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Three Constraints for Building Products Source Guide.md>) | 0.42 | 0.5958 | 0.1758 | 2 | 否 |
| [sources/Understanding as Concept Cloud Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Understanding as Concept Cloud Source Guide.md>) | 0.32 | 0.7625 | 0.4425 | 4 | 否 |
| [sources/web_chunk.md](</Users/zenk/study/wiki/wiki/sources/web_chunk.md>) | 0.37 | 0.5833 | 0.2133 | 2 | 否 |
| [sources/四层次原因分析法 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/四层次原因分析法 Source Guide.md>) | 0.42 | 0.5958 | 0.1758 | 2 | 否 |
| [sources/学会提问 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/学会提问 Source Guide.md>) | 0.42 | 0.3667 | 0.0533 | 1 | 否 |
| [sources/拆解 让复杂问题变清晰 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/拆解 让复杂问题变清晰 Source Guide.md>) | 0.42 | 0.5833 | 0.1633 | 2 | 否 |
| [sources/架构师启示录 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/架构师启示录 Source Guide.md>) | 0.37 | 0.7 | 0.33 | 8 | 否 |
| [sources/贝尔曼方程与大模型意识圆桌 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/贝尔曼方程与大模型意识圆桌 Source Guide.md>) | 0.42 | 0.5583 | 0.1383 | 2 | 否 |
| [sources/问题解决铁三角 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/问题解决铁三角 Source Guide.md>) | 0.44 | 0.3667 | 0.0733 | 1 | 否 |
| [sources/高难度沟通 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/高难度沟通 Source Guide.md>) | 0.42 | 0.3667 | 0.0533 | 1 | 否 |
| [syntheses/AGENTS.md as Repository Operation Contract.md](</Users/zenk/study/wiki/wiki/syntheses/AGENTS.md as Repository Operation Contract.md>) | 0.42 | 0.8562 | 0.4362 | 4 | 是 |
| [syntheses/AI Agent Engineering Learning Path.md](</Users/zenk/study/wiki/wiki/syntheses/AI Agent Engineering Learning Path.md>) | 0.65 | 0.71 | 0.06 | 5 | 是 |
| [syntheses/AI Agent Three Paradoxes.md](</Users/zenk/study/wiki/wiki/syntheses/AI Agent Three Paradoxes.md>) | 0.32 | 0.4167 | 0.0967 | 1 | 是 |
| [syntheses/AI Harness × Testing Strategy.md](</Users/zenk/study/wiki/wiki/syntheses/AI Harness × Testing Strategy.md>) | 0.37 | 0.7 | 0.33 | 7 | 是 |
| [syntheses/AI Memory × Context Graph.md](</Users/zenk/study/wiki/wiki/syntheses/AI Memory × Context Graph.md>) | 0.42 | 0.7 | 0.28 | 7 | 是 |
| [syntheses/Acting Under Complexity.md](</Users/zenk/study/wiki/wiki/syntheses/Acting Under Complexity.md>) | 0.37 | 0.5333 | 0.1633 | 2 | 是 |
| [syntheses/Agent Knowledge Architecture.md](</Users/zenk/study/wiki/wiki/syntheses/Agent Knowledge Architecture.md>) | 0.42 | 0.7417 | 0.3217 | 3 | 是 |
| [syntheses/Agent Skill Implementation Landscape.md](</Users/zenk/study/wiki/wiki/syntheses/Agent Skill Implementation Landscape.md>) | 0.72 | 0.5583 | 0.1617 | 2 | 是 |
| [syntheses/Agent Skill × Context Management.md](</Users/zenk/study/wiki/wiki/syntheses/Agent Skill × Context Management.md>) | 0.37 | 0.7 | 0.33 | 7 | 是 |
| [syntheses/Agent Skill × Harness Ratchet.md](</Users/zenk/study/wiki/wiki/syntheses/Agent Skill × Harness Ratchet.md>) | 0.44 | 0.7 | 0.26 | 8 | 是 |
| [syntheses/Agent System Design Space.md](</Users/zenk/study/wiki/wiki/syntheses/Agent System Design Space.md>) | 0.57 | 0.8962 | 0.3262 | 13 | 是 |
| [syntheses/Agentic Engineering × Verification Loop.md](</Users/zenk/study/wiki/wiki/syntheses/Agentic Engineering × Verification Loop.md>) | 0.42 | 0.7 | 0.28 | 6 | 是 |
| [syntheses/Application and Creation Distinction.md](</Users/zenk/study/wiki/wiki/syntheses/Application and Creation Distinction.md>) | 0.57 | 0.8 | 0.23 | 7 | 是 |
| [syntheses/Buddhist Practice Nihilism and Liberation.md](</Users/zenk/study/wiki/wiki/syntheses/Buddhist Practice Nihilism and Liberation.md>) | 0.42 | 0.3667 | 0.0533 | 1 | 是 |
| [syntheses/Business Analysis to Software Design.md](</Users/zenk/study/wiki/wiki/syntheses/Business Analysis to Software Design.md>) | 0.37 | 0.7 | 0.33 | 7 | 是 |
| [syntheses/Coding Agent Debugging Skills as Evidence Gates.md](</Users/zenk/study/wiki/wiki/syntheses/Coding Agent Debugging Skills as Evidence Gates.md>) | 0.82 | 0.5833 | 0.2367 | 2 | 是 |
| [syntheses/Coding Agent User Harness × Verification Loop.md](</Users/zenk/study/wiki/wiki/syntheses/Coding Agent User Harness × Verification Loop.md>) | 0.37 | 0.7 | 0.33 | 7 | 是 |
| [syntheses/Cognition Functional Framework.md](</Users/zenk/study/wiki/wiki/syntheses/Cognition Functional Framework.md>) | 0.42 | 0.8556 | 0.4356 | 9 | 是 |
| [syntheses/Euclid as a Case of Formalization's Limits.md](</Users/zenk/study/wiki/wiki/syntheses/Euclid as a Case of Formalization's Limits.md>) | 0.6 | 0.4167 | 0.1833 | 1 | 是 |
| [syntheses/Harness Ratchet × Feedback Flywheel.md](</Users/zenk/study/wiki/wiki/syntheses/Harness Ratchet × Feedback Flywheel.md>) | 0.44 | 0.7 | 0.26 | 7 | 是 |
| [syntheses/Human Agency × Narrative.md](</Users/zenk/study/wiki/wiki/syntheses/Human Agency × Narrative.md>) | 0.42 | 0.7 | 0.28 | 7 | 是 |
| [syntheses/Hypnosis and Unconscious Curriculum for Product Managers.md](</Users/zenk/study/wiki/wiki/syntheses/Hypnosis and Unconscious Curriculum for Product Managers.md>) | 0.86 | 0.7969 | 0.0631 | 8 | 是 |
| [syntheses/Learning Methodology × Mental Models.md](</Users/zenk/study/wiki/wiki/syntheses/Learning Methodology × Mental Models.md>) | 0.42 | 0.7333 | 0.3133 | 6 | 是 |
| [syntheses/Music Genres as Philosophies of Life.md](</Users/zenk/study/wiki/wiki/syntheses/Music Genres as Philosophies of Life.md>) | 0.42 | 0.5583 | 0.1383 | 2 | 是 |
| [syntheses/Permissionless Leverage × Wealth Creation.md](</Users/zenk/study/wiki/wiki/syntheses/Permissionless Leverage × Wealth Creation.md>) | 0.37 | 0.7 | 0.33 | 7 | 是 |
| [syntheses/Programming Language Three Operations.md](</Users/zenk/study/wiki/wiki/syntheses/Programming Language Three Operations.md>) | 0.42 | 0.5583 | 0.1383 | 2 | 是 |
| [syntheses/Quality Engineering Three Generators.md](</Users/zenk/study/wiki/wiki/syntheses/Quality Engineering Three Generators.md>) | 0.68 | 0.5958 | 0.0842 | 2 | 是 |
| [syntheses/Rank Reduction as Generative Model Discovery.md](</Users/zenk/study/wiki/wiki/syntheses/Rank Reduction as Generative Model Discovery.md>) | 0.42 | 0.5583 | 0.1383 | 2 | 是 |
| [syntheses/React UI Organization Model.md](</Users/zenk/study/wiki/wiki/syntheses/React UI Organization Model.md>) | 0.37 | 0.7 | 0.33 | 6 | 是 |
| [syntheses/Thinking and Judgment Workflow.md](</Users/zenk/study/wiki/wiki/syntheses/Thinking and Judgment Workflow.md>) | 0.7 | 0.4167 | 0.2833 | 1 | 是 |
| [syntheses/Verification Loop × Feedback Flywheel.md](</Users/zenk/study/wiki/wiki/syntheses/Verification Loop × Feedback Flywheel.md>) | 0.44 | 0.7 | 0.26 | 9 | 是 |
| [syntheses/成就感驱动与行动动力结构.md](</Users/zenk/study/wiki/wiki/syntheses/成就感驱动与行动动力结构.md>) | 0.42 | 0.7333 | 0.3133 | 3 | 是 |
| [syntheses/数据字典的秩.md](</Users/zenk/study/wiki/wiki/syntheses/数据字典的秩.md>) | 0.42 | 0.5583 | 0.1383 | 2 | 是 |
| [syntheses/软件设计作为系统诊断.md](</Users/zenk/study/wiki/wiki/syntheses/软件设计作为系统诊断.md>) | 0.37 | 0.5583 | 0.1883 | 2 | 是 |
| [topics/AI Skills Workflow.md](</Users/zenk/study/wiki/wiki/topics/AI Skills Workflow.md>) | 0.44 | 0.825 | 0.385 | 9 | 否 |
| [topics/Categorical Thinking.md](</Users/zenk/study/wiki/wiki/topics/Categorical Thinking.md>) | 0.37 | 0.5583 | 0.1883 | 2 | 否 |
| [topics/Context Management.md](</Users/zenk/study/wiki/wiki/topics/Context Management.md>) | 0.57 | 0.8341 | 0.2641 | 11 | 否 |
| [topics/Critical Thinking.md](</Users/zenk/study/wiki/wiki/topics/Critical Thinking.md>) | 0.42 | 0.7417 | 0.3217 | 3 | 否 |
| [topics/Dimensional Modeling.md](</Users/zenk/study/wiki/wiki/topics/Dimensional Modeling.md>) | 0.62 | 0.4417 | 0.1783 | 1 | 否 |
| [topics/LLM Inference Systems.md](</Users/zenk/study/wiki/wiki/topics/LLM Inference Systems.md>) | 0.44 | 0.7667 | 0.3267 | 3 | 否 |
| [topics/Learning Methodology.md](</Users/zenk/study/wiki/wiki/topics/Learning Methodology.md>) | 0.44 | 0.5958 | 0.1558 | 2 | 否 |
| [topics/Mental Models.md](</Users/zenk/study/wiki/wiki/topics/Mental Models.md>) | 0.44 | 0.7563 | 0.3163 | 8 | 否 |
| [topics/Modern Software Engineering.md](</Users/zenk/study/wiki/wiki/topics/Modern Software Engineering.md>) | 0.55 | 0.7542 | 0.2042 | 6 | 否 |
| [topics/Requirement to Architecture Mapping.md](</Users/zenk/study/wiki/wiki/topics/Requirement to Architecture Mapping.md>) | 0.37 | 0.5333 | 0.1633 | 2 | 否 |
| [topics/Spec-Driven Development.md](</Users/zenk/study/wiki/wiki/topics/Spec-Driven Development.md>) | 0.44 | 0.75 | 0.31 | 3 | 否 |
| [topics/Testing Strategy.md](</Users/zenk/study/wiki/wiki/topics/Testing Strategy.md>) | 0.44 | 0.7563 | 0.3163 | 4 | 否 |
| [topics/Thinking in Systems.md](</Users/zenk/study/wiki/wiki/topics/Thinking in Systems.md>) | 0.57 | 0.7583 | 0.1883 | 3 | 否 |
| [topics/架构落地方法.md](</Users/zenk/study/wiki/wiki/topics/架构落地方法.md>) | 0.37 | 0.7 | 0.33 | 8 | 否 |

</details>

## 13. Typed Relationships — 2 invalid types

检查了 87 个 relationships block。目标均可解析，无自引用。

- [concepts/Long-Running Agent Harness.md](</Users/zenk/study/wiki/wiki/concepts/Long-Running Agent Harness.md:15>) — relationships[0] type=`part_of`，目标 `[[wiki/topics/AI Harness]]`。
- [topics/Theory of Everything Popular Science.md](</Users/zenk/study/wiki/wiki/topics/Theory of Everything Popular Science.md:28>) — relationships[2] type=`part_of`，目标 `[[wiki/maps/Reading Map]]`。

允许类型：extends / implements / contradicts / derived_from / uses / replaces / related_to。修复时需按实际关系选型，不能把部分关系机械改成继承关系。

## 11. Synthesis Gaps — 6 candidates

从入链最多的 15 个概念中取概念对；排除 index/log/hot/maps 的共同列举，要求至少 3 个实质页面同时引用且没有现有综合页同时连接。间接覆盖仍可能存在，应先做语义核验。

| 概念对 | 实质共现 / 原始共现 | 证据页面 |
| --- | --- | --- |
| [concepts/Agent Skill.md](</Users/zenk/study/wiki/wiki/concepts/Agent Skill.md>) × [concepts/Feedback Flywheel.md](</Users/zenk/study/wiki/wiki/concepts/Feedback Flywheel.md>) | 7 / 9 | [concepts/Agentic Engineering.md](</Users/zenk/study/wiki/wiki/concepts/Agentic Engineering.md>); [sources/Agentic Coding Unknowns Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Agentic Coding Unknowns Source Guide.md>); [sources/Agentic Engineering at Zalando Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Agentic Engineering at Zalando Source Guide.md>); [sources/Coding with AI Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Coding with AI Source Guide.md>); [sources/LLM Wiki Source Guide.md](</Users/zenk/study/wiki/wiki/sources/LLM Wiki Source Guide.md>); [sources/从知识堆积到结构化记忆 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/从知识堆积到结构化记忆 Source Guide.md>); [topics/AI Skills Workflow.md](</Users/zenk/study/wiki/wiki/topics/AI Skills Workflow.md>) |
| [concepts/Mechanism Model.md](</Users/zenk/study/wiki/wiki/concepts/Mechanism Model.md>) × [concepts/Knowledge as Network.md](</Users/zenk/study/wiki/wiki/concepts/Knowledge as Network.md>) | 5 / 8 | [sources/概念 因果 规律 机制与知识 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/概念 因果 规律 机制与知识 Source Guide.md>); [sources/知识图谱的秩 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/知识图谱的秩 Source Guide.md>); [sources/知识结构概念解剖 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/知识结构概念解剖 Source Guide.md>); [sources/知识论概念解剖 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/知识论概念解剖 Source Guide.md>); [sources/知识论的秩 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/知识论的秩 Source Guide.md>) |
| [concepts/Agent Skill.md](</Users/zenk/study/wiki/wiki/concepts/Agent Skill.md>) × [concepts/Computational and Inferential Controls.md](</Users/zenk/study/wiki/wiki/concepts/Computational and Inferential Controls.md>) | 4 / 6 | [sources/Agent Engineering Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Agent Engineering Source Guide.md>); [sources/Block Agent Skills Design Principles Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Block Agent Skills Design Principles Source Guide.md>); [sources/Designing Refining and Maintaining Agent Skills at Perplexity Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Designing Refining and Maintaining Agent Skills at Perplexity Source Guide.md>); [topics/AI Skills Workflow.md](</Users/zenk/study/wiki/wiki/topics/AI Skills Workflow.md>) |
| [concepts/Mechanism Model.md](</Users/zenk/study/wiki/wiki/concepts/Mechanism Model.md>) × [concepts/Analysis.md](</Users/zenk/study/wiki/wiki/concepts/Analysis.md>) | 4 / 6 | [concepts/五大思维三层架构.md](</Users/zenk/study/wiki/wiki/concepts/五大思维三层架构.md>); [sources/发现和定义问题 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/发现和定义问题 Source Guide.md>); [sources/四层次原因分析法 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/四层次原因分析法 Source Guide.md>); [sources/拆解 让复杂问题变清晰 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/拆解 让复杂问题变清晰 Source Guide.md>) |
| [concepts/Understanding.md](</Users/zenk/study/wiki/wiki/concepts/Understanding.md>) × [concepts/Mechanism Model.md](</Users/zenk/study/wiki/wiki/concepts/Mechanism Model.md>) | 4 / 8 | [sources/概念 因果 规律 机制与知识 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/概念 因果 规律 机制与知识 Source Guide.md>); [sources/知识结构概念解剖 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/知识结构概念解剖 Source Guide.md>); [sources/知识论概念解剖 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/知识论概念解剖 Source Guide.md>); [sources/表征 图式 心智模型和解释框架 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/表征 图式 心智模型和解释框架 Source Guide.md>) |
| [concepts/Harness Ratchet.md](</Users/zenk/study/wiki/wiki/concepts/Harness Ratchet.md>) × [concepts/Context Graph.md](</Users/zenk/study/wiki/wiki/concepts/Context Graph.md>) | 3 / 6 | [sources/Agent Engineering Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Agent Engineering Source Guide.md>); [sources/从知识堆积到结构化记忆 Source Guide.md](</Users/zenk/study/wiki/wiki/sources/从知识堆积到结构化记忆 Source Guide.md>); [topics/AI Harness.md](</Users/zenk/study/wiki/wiki/topics/AI Harness.md>) |

## 建议处理顺序

1. 修复 11 页 YAML summary 语法、1 个 lifecycle 枚举和 2 个关系类型。
2. 为 12 页补齐首页入口，复核 4 个孤立页该由哪张地图或相关页面承接；补齐无元数据页、压缩过长摘要，并同步 Hot Cache 首页描述。
3. 先复核高流量 Mental Models，再处理 21 个 provenance 漂移候选；检查来源和标记后更新比例。
4. 先检查有来源内容日期证据的陈旧综合页，再决定是否需要重新综合；为置信度加入稳定 source_id 和质量分类后再重算。
5. 对六个综合机会先查间接覆盖，并通过地图/主题治理大标签群。

## 审计限制与产物

- 11 malformed YAML headers were recovered in memory only for downstream checks; malformed original files remain unchanged.
- Missing lifecycle/confidence fields remain warnings because the schema rollout phase could not be established.
- Confidence drift values are heuristic candidates: source_id and source-quality metadata are absent; empty-source defaults are exempt, synthesis scoring needs input-page confidence rather than source-count scoring.
- Provenance fractions count bullets once and prose by sentence, excluding code, headings, tables and navigation; claim-level source truth was not globally verified.
- Local source mtimes can change without content changing; external URLs and conversation identifiers were not refreshed or checked remotely.
- Contradiction detection sampled linked/tagged neighborhoods and typed contradicts edges, not all possible page pairs.
- Index descriptions differing from summary text are review candidates, not automatically inconsistent; 1 stale hot-cache description was confirmed.
- Synthesis gaps use co-occurrence among top 15 linked concepts after excluding index/log/hot/maps; existing indirect syntheses may still cover the topic.

产物位于仓库的 `artifacts/wiki-lint/2026-10-11/`，避免审计报告自身改变 canonical wiki 的入链与库存。`report.md` 为完整可读报告，`findings.json` 为全部结构化结果。默认审计仅写产物和追加 wiki/log.md 记录；知识页与首页未修复。
QMD skipped: QMD_WIKI_COLLECTION unset。
