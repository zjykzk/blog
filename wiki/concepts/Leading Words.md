---
title: Leading Words
type: concept
status: growing
category: concepts
aliases:
  - 行为锚点
  - leading word
  - leading words
tags: [agents, context, skills, workflow]
sources:
  - https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-for-agents/SKILL.md
  - conversation:2026-10-24
  - /Users/zenk/Context/20261024T210428--理解-Leading-Words行为锚点__is.md
created: 2026-10-26T23:41:30+08:00
updated: 2026-10-26T23:41:30+08:00
summary: Leading word 用一个已有语义的短词或短语唤起一组行为要求，在正文中锚定执行，在 context pointer 中帮助发现对应材料。
provenance:
  extracted: 0.80
  inferred: 0.20
  ambiguous: 0.00
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-10-26
---

# Leading Words

在 [[wiki/sources/Writing for Agents Source Guide|Writing for Agents]] 的语境里，leading word 是用来唤起一组既有行为含义的短词或短语，可理解为“行为锚点”。

## 用短词唤起整套做法

关键在词所携带的概念关联，而非它是不是句子的第一个词。作者优先选模型训练中已有的概念，例如 `lesson`、`fog of war`、`tracer bullets`。自造标签也可以使用，但要额外解释其含义。

原文强调重复的是简短标签，不是反复复制整段定义。一个标签由相关规则与实例不断充实，再在后续指令中唤起那套行为。这里的词或短语不保证恰好对应 tokenizer 的一个 token。^[inferred]

## red 的例子

在测试语境中，`red` 可以把模糊的“可信测试循环”转成可观察的状态：测试在缺陷存在时失败。对话把这个例子进一步具体化为：^[inferred]

```text
这里的 red：回归测试在修复前，确实因待修复缺陷而失败。
后续指令：先让测试 red，再进行修复。
```

这缩短了后续指令，又保留了对应的行为目标。若测试因缺少依赖而失败，它并没有验证待修复缺陷；因此只保留 `red` 而丢掉失败原因的边界，会形成错误的完成标准。^[inferred]

Leading word 本身不执行动作，也不证明动作正确。它提供语义锚定，具体执行和证据仍依赖工具与 [[wiki/concepts/Verification Loop|验证回路]]。^[inferred]

## 执行锚定与调用锚定

在正文里，leading word 帮助 Agent 反复回到同一类做法；在 [[wiki/concepts/Context Pointer|context pointer]] 里，它帮助当前任务与对应材料建立联系。提示、文档和代码库共用同一个有辨识度的词，可以增强这种联系。

因此二者可以配合：leading word 唤起“怎样做”，pointer 说明“何时去读哪份材料”。同一个词也可以用于 pointer 触发，不能把它们理解成互斥的类型。^[inferred]

## 使用与失效条件

先明确希望模型执行的动作，再选已有对应含义的词，在首次使用时说明必要边界。后续重复标签，同时把权威定义保留在一个位置。

短或响亮不等于有效。若“严谨”“深入”没有改变模型默认行为，原文把这种指令称为 no-op。有效性具有模型和任务依赖，需要通过运行文档判断。

若压缩后发生歧义，应补回关键约束或更换词；若总要重新解释整段内容，标签就没有取得预期收益。单靠更强的词也不能补齐模型能力或验证机制的缺口。^[inferred]

## Related

- [[wiki/concepts/Context Pointer]]
- [[wiki/concepts/Agent Skill]]
- [[wiki/topics/Context Management]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/sources/Writing for Agents Source Guide]]
