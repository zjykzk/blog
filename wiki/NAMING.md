# Wiki naming and placement rules

这份规则用于稳定当前 `wiki/` 层的目录语义，减少后续继续迁移时的摇摆。

## Core principle

`wiki/` 是当前仓库的 canonical stable knowledge layer。

这意味着：
- `wiki/index.md` 是实际首页
- `wiki/Welcome.md` 是历史遗留页
- 新增稳定知识优先写入 `wiki/*`
- 旧 `pages/`、`mobu/`、`journals/` 内容优先保留为 source note，再逐步提升为 wiki 页面

## Page types

### `maps/`
用于导航，不承载过多原始内容。

适用条件：
- 主要目标是把一个领域里的 page 串起来
- 读者进入后先决定往哪里走
- 更像入口而不是正文

命名规则：
- 统一使用 `X Map`
- 例如：`AI Map`、`CS Map`、`Management Map`

推荐 section 结构：
- `## Concepts`（按需）
- `## Topics`（按需）
- `## Syntheses`（按需）
- `## Source notes` 或 `## Source layer`
- `## Next extraction targets` / `## Notes`（按需）

说明：
- map 页优先服务导航
- 不把大段主题正文塞进 map

### `concepts/`
用于表达一个稳定概念。

适用条件：
- 这个页面回答“X 是什么”
- 重点是定义、边界、核心机制
- 不依赖某一篇来源文章才能成立

命名规则：
- 直接使用概念名
- 避免在标题里加 `Concept`
- 例如：`Agent`、`LLM`、`Cynefin Framework`

推荐 section 结构：
- `## What it is`
- `## Why it matters`
- `## Upstream concepts`（可选）
- `## Downstream topics`（可选）
- `## Cross-links`
- `## Source notes`

说明：
- 概念页优先回答定义与边界
- 若存在明显派生主题，再补 downstream links
- 不必强行包含每一节，但顺序尽量一致

### `topics/`
用于表达一个长期主题。

适用条件：
- 这个页面回答“关于 X，有哪些长期可维护的判断”
- 往往能聚合多个来源或多个子问题
- 比 concept 更宽，比 map 更实

命名规则：
- 直接使用主题名
- 不加 `Topic`
- 例如：`Circuit Breaker`、`Technical Management`、`Testing Strategy`

推荐 section 结构：
- `## Core idea` 或 `## Why it matters`
- 主题正文（可自由分小节）
- `## Upstream concepts` / `## Upstream topics`（按需）
- `## Peer topics`（按需）
- `## Downstream synthesis`（按需）
- `## Navigation`
- `## Source notes`

说明：
- topic 页允许正文结构更自由
- 但 link 区域尽量收束到统一尾部结构
- 如果没有 synthesis 或 peer topics，可以省略对应节

### `sources/`
用于说明来源层，不直接承担稳定知识母页角色。

适用条件：
- 页面主要说明某批原始材料怎么用
- 页面价值在于回溯与解释来源，而不是给出终局表达

命名规则：
- 用 `X Source Guide` 或 `X Notes`
- 当前允许保留已有名称，如：`Published Posts`、`Mobu Notes`
- 新增时优先用更明确的 guide 命名

推荐 section 结构：
- `## Current role` 或 `## Current examples`
- `## Extraction rule` / `## Promotion rule`
- `## Related` 或 `## Promoted wiki topics`

说明：
- source guide 页解释“原始材料如何进入 wiki”
- 不承担最终知识表达

### `syntheses/`
用于跨来源综合。

适用条件：
- 已经跨越多篇 notes / posts / books
- 目标不是定义概念，而是形成框架化理解
- 通常会带比较、演化、统一视角

命名规则：
- 使用明确结果名
- 例如：`How I Use User Stories and Architecture Mapping`
- 不使用泛化标题如 `Thoughts`

推荐 section 结构：
- synthesis 正文（通常按步骤、视角或框架展开）
- `## Why this synthesis matters`
- `## Upstream concepts`（按需）
- `## Upstream topics`（按需）
- `## Navigation`

说明：
- synthesis 页的重点是把多个上游页面压缩成更高层框架
- 不必再重复 source notes，除非确实需要直接回溯原材料

## Placement heuristics

拿到一篇内容时，按这个顺序判断：

1. 它主要是在导航别的页面吗？→ `maps/`
2. 它主要是在定义一个概念吗？→ `concepts/`
3. 它主要是在聚合某个主题下的稳定判断吗？→ `topics/`
4. 它主要是在解释来源材料如何使用吗？→ `sources/`
5. 它是否已经跨多个来源形成统一框架？→ `syntheses/`

## Legacy handling rule

对旧 `pages/`、`mobu/`、`journals/` 内容：

- 原文保留时，优先把它变成 source note
- 新的稳定表达写进 `wiki/`
- 不急着移动旧文件，先保证 link 和语义稳定
