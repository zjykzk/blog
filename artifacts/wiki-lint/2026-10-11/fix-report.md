# Wiki Lint Fix Report — 2026-10-11

修复完成时间：2026-10-11T17:55:18+08:00。用户已授权修复。原审计保存在 [report.md](report.md)，当前结果见 [after-findings.json](after-findings.json)。

本轮修复了全部 36 条已确认结构发现和字段警告，修改 53 个 wiki 文件（包含审计日志）。未提交 Git。

| 检查 | 修复前 | 修复后 |
| --- | --- | --- |
| YAML 解析错误 | 11 | 0 |
| 孤立页 | 4 | 0 |
| 失效双链 | 0 | 0 |
| 首页遗漏 | 12 | 0 |
| 首页过时缓存描述 | 1 | 0 |
| 基础元数据缺失 | 1 | 0 |
| 摘要缺失/过长 | 1/1 | 0/0 |
| 生命周期字段问题 | 3 | 0 |
| 非法关系类型 | 2 | 0 |

## 实际修复

- 把 11 页带英文冒号的 summary 改成有效 YAML 折叠标量。语法维护没有批量刷新旧内容时间。
- 为原始草稿补齐元数据，sources 指向修复前的 Git 版本；保留正文与草稿身份。
- 将 lifecycle: seed 修为 draft，保留 status: seed 与原状态日期；两条 part_of 关系改用 related_to，没有提升审阅或验证状态。
- 加入 12 个首页入口，同步 Hot Cache 描述，缩短注意力概念摘要。4 个孤立页另获 Learning/CS 地图或概念页的语义入口。
- 移除 10 页重复的 synthesis 类型标签；category/type 继续表达页面类型。
- 复核并更新 8 篇综合页，补入验证独立性、目标适配、缓存稳定、记忆管理、更新范围与阅读实践。新增综合判断均标 inferred。
- 复核原来的 22 个 provenance 候选，补齐逐项标记，修正段落末尾标记的计数范围，重算 13 个页面的比例。已标出的推断和不确定性未被伪装成直接提取。
- 修正时间反演与时间平移混淆，以及从 A=A 证明物理普适性的错误；校正欧几里得引用与公理缺口表述，收窄“所有大厂必然建设某种平台”的无依据断言。

## 仍属审阅提醒的结果

- 377 页超过 90 天未更新，全部 draft；没有通过批量改时间戳消除这类提醒。
- 210 个置信度估算候选：缺少稳定 source_id 与质量分类，没有按猜测改写既有 base_confidence。
- 21 项 provenance 提醒：其中包含段落范围纠正后新显露的候选、高流量页推断比例，以及已显式标注的来源不确定性。
- 2 页仍有来源 mtime 晚于 updated 的候选；已核对的语义维护与文件触碰不等于旧结论过期。
- 6 个综合机会属于可新增内容，不是现存结构错误。

### 当前 provenance 审阅队列

| 页面 | 提醒 |
| --- | --- |
| [concepts/Data Warehouse Bus Matrix.md](</Users/zenk/study/wiki/wiki/concepts/Data Warehouse Bus Matrix.md>) | drift-candidate |
| [concepts/Iceberg Model.md](</Users/zenk/study/wiki/wiki/concepts/Iceberg Model.md>) | drift-candidate |
| [concepts/Logit Lens.md](</Users/zenk/study/wiki/wiki/concepts/Logit Lens.md>) | drift-candidate |
| [concepts/Slowly Changing Dimension.md](</Users/zenk/study/wiki/wiki/concepts/Slowly Changing Dimension.md>) | drift-candidate |
| [concepts/Verification Loop.md](</Users/zenk/study/wiki/wiki/concepts/Verification Loop.md>) | hub-inferred |
| [maps/Classification Thinking Map.md](</Users/zenk/study/wiki/wiki/maps/Classification Thinking Map.md>) | drift-candidate |
| [sources/Iceberg Model Source Guide.md](</Users/zenk/study/wiki/wiki/sources/Iceberg Model Source Guide.md>) | speculation-heavy |
| [syntheses/AI 泡沫判断的结构.md](</Users/zenk/study/wiki/wiki/syntheses/AI 泡沫判断的结构.md>) | drift-candidate |
| [syntheses/Agent Skill Patterns as Human Workflow Control Structures.md](</Users/zenk/study/wiki/wiki/syntheses/Agent Skill Patterns as Human Workflow Control Structures.md>) | drift-candidate |
| [syntheses/Buddhist Practice Nihilism and Liberation.md](</Users/zenk/study/wiki/wiki/syntheses/Buddhist Practice Nihilism and Liberation.md>) | speculation-heavy |
| [syntheses/Business Analysis to Software Design.md](</Users/zenk/study/wiki/wiki/syntheses/Business Analysis to Software Design.md>) | drift-candidate |
| [syntheses/Euclid as a Case of Formalization's Limits.md](</Users/zenk/study/wiki/wiki/syntheses/Euclid as a Case of Formalization's Limits.md>) | drift-candidate |
| [syntheses/Human Agency × Narrative.md](</Users/zenk/study/wiki/wiki/syntheses/Human Agency × Narrative.md>) | drift-candidate |
| [syntheses/Permissionless Leverage × Wealth Creation.md](</Users/zenk/study/wiki/wiki/syntheses/Permissionless Leverage × Wealth Creation.md>) | drift-candidate |
| [syntheses/React UI Organization Model.md](</Users/zenk/study/wiki/wiki/syntheses/React UI Organization Model.md>) | drift-candidate |
| [syntheses/Tool and Skill Boundary in Agent Harnesses.md](</Users/zenk/study/wiki/wiki/syntheses/Tool and Skill Boundary in Agent Harnesses.md>) | drift-candidate |
| [syntheses/Zima Blue 自我回归与无我.md](</Users/zenk/study/wiki/wiki/syntheses/Zima Blue 自我回归与无我.md>) | drift-candidate |
| [topics/AI Memory.md](</Users/zenk/study/wiki/wiki/topics/AI Memory.md>) | hub-inferred |
| [topics/AI Skills Workflow.md](</Users/zenk/study/wiki/wiki/topics/AI Skills Workflow.md>) | hub-inferred |
| [topics/Mental Models.md](</Users/zenk/study/wiki/wiki/topics/Mental Models.md>) | hub-inferred |
| [topics/Modern Software Engineering.md](</Users/zenk/study/wiki/wiki/topics/Modern Software Engineering.md>) | hub-inferred |

### 来源时效候选

| 派生页 | 来源 |
| --- | --- |
| [syntheses/AI Agent Engineering Learning Path.md](</Users/zenk/study/wiki/wiki/syntheses/AI Agent Engineering Learning Path.md>) | `wiki/concepts/Agent.md` |
| [syntheses/AI Agent Engineering Learning Path.md](</Users/zenk/study/wiki/wiki/syntheses/AI Agent Engineering Learning Path.md>) | `wiki/concepts/Agentic Control Loop.md` |
| [syntheses/AI Agent Engineering Learning Path.md](</Users/zenk/study/wiki/wiki/syntheses/AI Agent Engineering Learning Path.md>) | `wiki/sources/Code as Agent Harness Paper Source Guide.md` |
| [syntheses/Learning Methodology × Mental Models.md](</Users/zenk/study/wiki/wiki/syntheses/Learning Methodology × Mental Models.md>) | `wiki/topics/Mental Models` |

## 验证

所有 517 页完成严格 YAML 解析与链接图检查；元数据、摘要、生命周期、关系类型、库存及孤立检查为 0。源稿 Git 版本可读取，原有 base_confidence 未改，lifecycle 仅修复无效枚举。`git diff --check` 通过。

完整改动回执见 [fix-verification.json](fix-verification.json)，来源快照与审阅处理见 [fix-review.json](fix-review.json)。
.obsidian/workspace.json 的现有变动由应用产生，本轮未编辑或回退它。
QMD skipped: QMD_WIKI_COLLECTION unset。
