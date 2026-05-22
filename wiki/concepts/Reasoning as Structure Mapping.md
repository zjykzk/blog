---
title: Reasoning as Structure Mapping
type: concept
status: draft
category: concepts
tags:
  - thinking
  - reasoning
  - cognition
sources:
  - conversation:2026-05-18
  - /Users/zenk/Documents/notes/20260408T203540--概念解剖-推理__concept.org
  - conversation:2026-05-19
created: 2026-05-18T22:25:02+08:00
updated: 2026-05-19T22:35:35+08:00
summary: 推理可以理解为结构之间的关系保持映射：用一个已知结构照亮未知结构，并检查这种照亮是否保住了约束。
provenance:
  extracted: 0.94
  inferred: 0.06
  ambiguous: 0.00
base_confidence: 0.73
lifecycle: draft
lifecycle_changed: 2026-05-18
aliases:
  - 结构映射式推理
  - 推理作为结构映射
  - structural mapping reasoning
---
# Reasoning as Structure Mapping

推理作为结构映射，是把一组关系搬到另一组关系里，并检查哪些关系能保住、哪些关系会断裂。

## What It Is

结构映射式推理不把推理看成从一个点跳到另一个点，而把推理看成两个结构之间的对齐。

它关注的不是对象是否表面相似，而是关系是否可以迁移。一个隐喻、模型或类比，只有在它能产生可检验的新判断时，才不只是修辞，而是推理工具。^[inferred]

例如“公司像机器”不是说公司真的有齿轮，而是把机器结构映射到公司结构：

```text
零件   -> 部门 / 岗位
传动   -> 流程 / 协作
故障   -> 瓶颈 / 内耗
维护   -> 管理 / 优化
输出   -> 产品 / 结果
```

这个映射一旦成立，就会生成后续判断：如果机器卡住，要找摩擦点；如果输出不稳定，要检查输入、流程和部件；如果局部过载，系统会提前磨损。

## How It Works

结构映射通常包含四个环节：

1. 源结构：已经熟悉的结构，例如机器、地图、生态、市场、战争、游戏、剧场、网络。
2. 目标结构：想理解的对象，例如公司、知识、人生、AI、城市、学习、推理本身。
3. 对应关系：找出哪些元素、角色和关系能对上。
4. 约束检验：检查映射推出的新判断是否仍然合理。

核心动作不是词对词，而是关系对关系。`地图 : 地形 = 模型 : 现实` 这种表达有效，是因为它保持了“简化表示指向复杂对象”的关系。

传统隐喻常把推理看成链条：

```text
A -> B -> C -> D
```

链条隐喻强调步骤、顺序和证明，但容易让人误以为推理总是线性的。

结构映射隐喻把推理看成结构补全：

```text
source structure              target structure

a ---- b                      x ---- y
|      |          maps to     |      |
c ---- d                      z ---- ?
```

如果 `a:b:c:d` 的关系能映射到 `x:y:z:?`，就可以推断缺失的 `?`。这时推理不是“走到下一步”，而是“补全一个结构”。

## When to Use

结构映射适合处理以下问题：

- 用熟悉领域理解陌生领域。
- 检查一个比喻是否只是好听，还是能生成判断。
- 从已有案例、模型或理论迁移到新情境。
- 发现一个框架照亮了什么，也遮蔽了什么。

它尤其适合理解类比推理、数学建模、法律适用、科学建模和 LLM reasoning。类比推理从熟悉结构迁移到陌生结构；数学推理保持形式关系；法律推理把案件结构映射到规则结构；科学建模把现象结构映射到理论结构；LLM reasoning 则可以被看作在上下文、模式和潜在表示之间寻找可延续结构。^[inferred]

## Failure Modes

坏推理常常不是没有映射，而是映射错了。

常见错误包括：

- 只映射表面相似，不映射深层关系。
- 只保留有利关系，丢掉限制条件。
- 把局部结构强行扩展成整体结构。
- 忘记源结构和目标结构有不同边界。

“人生像游戏”有用，因为它能保留规则、反馈、技能和升级这些关系；它也危险，因为现实没有完全公平的规则，失败成本也不只是“重开一局”。每个隐喻都是一盏灯，也是一片阴影。

## Relation to Analysis and Judgment

[[wiki/concepts/Analysis]] 先把整体打开，识别部分、关系和约束；结构映射式推理则把这些关系迁移到另一个结构，并检查迁移后的约束是否仍然成立。

[[wiki/topics/Critical Thinking]] 负责审查映射是否可靠：前提是否成立、词义是否含混、假设是否隐藏、证据是否足够、替代解释是否被遗漏。

[[wiki/syntheses/Thinking and Judgment Workflow]] 提醒，推理质量不只取决于映射是否漂亮，也取决于一开始的问题框架是否正确。错误的问题框架会让后续映射在错误对象上打转。

## Compact Form

```text
Reasoning = source structure + target structure + relation mapping + constraint check
```

更短地说：结构映射式推理，就是用一个已知结构照亮一个未知结构，并不断检查这束光有没有照歪。

## Related

- [[wiki/concepts/Analysis]]
- [[wiki/topics/Critical Thinking]]
- [[wiki/syntheses/Thinking and Judgment Workflow]]
- [[wiki/sources/推理概念解剖 Source Guide]]
- [[wiki/sources/推理证明与未知问答 Source Guide]]
- [[wiki/sources/LLM Reasoning Is Latent, Not the Chain of Thought Source Guide]]
- [[wiki/sources/Theory Is All You Need Source Guide]]
