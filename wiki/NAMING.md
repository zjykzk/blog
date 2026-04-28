# Wiki Naming and Placement Rules

这份文档规定 `wiki/` 下笔记的命名和放置规则。

## 目录角色

| 目录 | 放什么 | 命名示例 |
|------|--------|----------|
| `wiki/maps/` | 地图页，整个领域的索引入口 | `CS Map.md`、`Reading Map.md` |
| `wiki/concepts/` | 稳定的概念页，一个概念一页 | `Cognition Three Channels.md`、`Agent.md` |
| `wiki/topics/` | 长期主题页，围绕一个方法论/实践/讨论 | `Learning Methodology.md`、`Spec-Driven Development.md` |
| `wiki/syntheses/` | 跨源综合页，把多个 source 的内容拧成一篇 | `Learning Methodology Across Sources.md` |
| `wiki/sources/` | 指向原始材料（书、论文、对话、网文）的结构化导览 | `Software Methodology by Pan Jianyu.md` |

## 命名规则

1. **文件名用英文（或中英混写），空格分词**，例如 `Learning Methodology.md`，避免下划线、连字符。
2. **标题大小写**：概念和主题用 Title Case（首字母大写）；map 文件用 `X Map.md` 格式。
3. **一页一主题**：一个概念/主题/综合只建一页，不拆多个文件。
4. **别名**：frontmatter 用 `aliases` 列出中文、缩写、旧名，方便双链。

## 每页的 frontmatter 模板

```yaml
---
title: <页面标题>
type: concept | topic | synthesis | map | source
status: draft | stable | archived
updated: YYYY-MM-DD
aliases:
  - <别名1>
  - <别名2>
---
```

- `type` 必填，对应放置目录。
- `status`：新建时用 `draft`；内容稳定后改为 `stable`；被替换时改为 `archived`。

## 跨页链接

- 页内用 Obsidian 双链 `[[wiki/concepts/XXX]]`（带路径，避免同名冲突）。
- 每页末尾建议列出 `## Related`，枚举相关 wiki 页。
- 指向 `pages/` 下的 source note 用 `[[XXX]]`（Obsidian 会按 alias 解析）。

## 从 source 到 wiki 的迁移流程

1. 新知识先进 `pages/` 做 source note（原始摘录 + 指向未来的 wiki 页）。
2. 内容稳定后，在 `wiki/concepts/` 或 `wiki/topics/` 建正式页，把结论（不是对话过程）写进去。
3. 有多个 source 讲同一件事时，在 `wiki/syntheses/` 做跨源综合页。
4. 领域成形后，在 `wiki/maps/` 建地图页，把上面三层串起来。
