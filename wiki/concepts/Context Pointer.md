---
title: Context Pointer
type: concept
status: growing
category: concepts
aliases:
  - 上下文指针
  - context pointer
tags: [agents, context, skills, workflow]
sources:
  - https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-for-agents/SKILL.md
  - conversation:2026-10-24
  - /Users/zenk/Context/20261024T210045--理解-Context-Pointer上下文指针__is.md
created: 2026-10-26T23:41:30+08:00
updated: 2026-10-26T23:41:30+08:00
summary: Context pointer 是当前上下文里指向外部材料并说明读取条件的路由提示；其措辞决定材料是否容易在正确任务分支被发现。
provenance:
  extracted: 0.85
  inferred: 0.15
  ambiguous: 0.00
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-10-26
---

# Context Pointer

Context pointer 是留在 Agent 当前上下文里的一段引用：它指出尚未加载的材料，并说明遇到什么任务时应去读取。

## 从地址到读取条件

普通链接主要回答“材料在哪里”；context pointer 还回答“什么时候需要这份材料”。[[wiki/concepts/Agent Skill|Skill]] 的模型可发现 description、`AGENTS.md` 中带条件的文档引用，都可以承担这种作用。

例如：

```text
修改数据库结构时，读取 docs/db-migrations.md 中的迁移规则。
```

“修改数据库结构时”是触发分支，“docs/db-migrations.md”是目标，“迁移规则”说明材料是什么。这里的分支指不同的适用任务情况，不必对应代码中的 if 语句。

`更多信息见这里` 只给出模糊入口。目标文件即使内容准确，Agent 也可能因为没有识别到适用条件而不去读取。

## 怎样进入执行路径

Agent 读到任务和 pointer 后，可以判断是否应通过读取工具加载目标材料。加载后，外部内容才进入后续执行的上下文。Pointer 是自然语言路由提示，不能替代宿主的加载机制，也不能保证每次必然触发。^[inferred]

在 [[wiki/sources/Writing for Agents Source Guide|Writing for Agents]] 的写作模型中，context pointer 支持 progressive disclosure：常驻一条短提示，把分支性参考资料放在主文件之外。正文避免长期占用窗口，但 pointer 本身仍支付常驻的 context load；实际读取后，正文也会占用当前窗口。

完全没有 pointer 的材料，可能需要由人记住何时调用，这会增加人的 cognitive load。这里的 cognitive load 特指“记住有哪些文档以及何时使用”的负担，不能直接等同于认知负荷理论的完整分类。

## 与相邻概念的关系

| 概念 | 负责什么 |
|---|---|
| Context pointer | 何时读取哪份外部材料 |
| [[wiki/concepts/Leading Words|Leading word]] | 用短词唤起一组行为含义，也可增强 pointer 的辨识度 |
| [[wiki/concepts/Context Anchoring|Context anchoring]] | 把决策与理由保存为可重载的外部工件 |
| [[wiki/topics/Context Management|Context management]] | 统筹什么信息进入、保留和离开当前窗口 |

## 写作与校验

1. 列出材料处理的真正不同的任务分支。
2. 每个分支保留一个清楚的触发条件，合并只是重述同一分支的近义词。
3. 把最有辨识度的 leading word 放在指针前部，并说明目标材料的用途。
4. 所有分支都依赖的关键内容优先留在主路径，只有部分分支需要的资料再外置。
5. 若必需材料经常没有被加载，先改 pointer 的措辞；仍不可靠时再考虑内联关键内容。

静态检查可以遮住目标正文，只看这一行是否足以回答“是什么、何时读、当前任务是否适用”。运行检查则应同时观察应该触发却漏读的情况，以及不该触发却误读的情况。^[inferred]

## Related

- [[wiki/concepts/Agent Skill]]
- [[wiki/topics/Context Management]]
- [[wiki/concepts/Leading Words]]
- [[wiki/syntheses/Agent Skill × Context Management]]
- [[wiki/sources/Writing for Agents Source Guide]]
