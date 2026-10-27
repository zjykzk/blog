---
title: Writing for Agents Source Guide
type: source
status: growing
category: sources
aliases:
  - Agent 文档写作方法
  - writing-for-agents
tags: [agents, context, skills, workflow, harness]
sources:
  - https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-for-agents/SKILL.md
  - https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-for-agents/SKILL-MECHANICS.md
  - conversation:2026-10-22
  - conversation:2026-10-24
created: 2026-10-26T23:41:30+08:00
updated: 2026-10-26T23:41:30+08:00
summary: Writing for Agents 把 Agent 文档设计为上下文路由与执行控制：管理两种负担、信息层级、完成条件、行为锚点与持续修剪。
provenance:
  extracted: 0.80
  inferred: 0.20
  ambiguous: 0.00
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-10-26
---

# Writing for Agents Source Guide

> 来源：[writing-for-agents/SKILL.md](https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-for-agents/SKILL.md) 与 [SKILL-MECHANICS.md](https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-for-agents/SKILL-MECHANICS.md)。原文在 2026-10-22 的分析中经 GitHub 页面提取与 raw Markdown 对照；2026-10-24 的对话进一步澄清两个概念。本文保存该次阅读版本，不声称 upstream main 之后未变化。

## 核心问题与目标 G

这套写作方法适用于 Agent 消费的 Skill、`AGENTS.md`、`CLAUDE.md` 及其引用文档。目标是使 Agent 更稳定地经过正确过程，允许不同任务产生不同输出。

SFAM 分析把总目标概括为：在不过度消耗 Agent 上下文和人类记忆的前提下，降低执行过程的方差。路由可靠、信息位置正确、结束条件清楚和内容持续相关，是四个相互支持的条件。^[inferred]

```text
路由：何时加载哪份材料
  → 分层：当前步骤与按需参考如何安排
  → 执行控制：做什么、何时算完成
  → 维护：删除重复、过时和不改变行为的内容
```

这是按功能归并的四阶段结构；原文自身是一组可按需使用的参考规则，不是固定的四步工作流。^[inferred]

## 两种负担

| 负担 | 支付者与内容 | 主要取舍 |
|---|---|---|
| Context load | Agent 每轮面对常驻材料时支付的 token 与注意力成本 | description、AGENTS.md 指针也有长期成本 |
| Cognitive load | 人记住哪些文档存在、何时使用它们的成本 | 人类判断有价值时值得支付，并非一律最小化 |

按指针加载的资料避免正文常驻，但保留指针本身的成本；加载后正文仍占用当前窗口。没有自动发现入口的资料，则更依赖人类记忆。减少 context load 不等于减少全部负担。

## 关键结构 S 与功能 F

| 结构 | 输入 → 输出 | 功能 |
|---|---|---|
| S1 [[wiki/concepts/Context Pointer|Context pointer]] | 材料和适用分支 → 读取条件与目标 | 控制外部知识何时进入执行路径 |
| S2 信息阶梯与渐进披露 | steps、reference、各分支需求 → 文件内步骤、文件内参考、外部参考 | 保护主路径，避免步骤被参考资料淹没 |
| S3 Co-location | 一个概念的定义、规则和例外 → 同一处的内容组 | 避免读到定义却漏掉相邻约束 |
| S4 Completion criterion | 动作和覆盖范围 → 可判断的完成边界 | 抵抗提前结束，并驱动必要的调查工作 |
| S5 Split boundary | 分支或真实抢跑问题 → 有收益的拆分边界 | 让每条路径携带所需材料，必要时把后续步骤移出视野 |
| S6 [[wiki/concepts/Leading Words|Leading words]] | 反复出现的行为描述 → 有既有语义的短标签 | 压缩解释并锚定执行与发现 |
| S7 Pruning | 每一行的来源、相关性和行为作用 → 保留、外置或删除 | 控制重复、过时缓存和 no-op 的积累 |

纯参考文档可以保留同一层级的一组规则；并非所有文档都要改成步骤。信息阶梯决定内容放多远，co-location 决定放下之后哪些内容应在一起。

## 运作逻辑 A：先修局部边界，再扩大结构

所有分支都需要的内容优先内联，只有部分分支需要的参考再放到 pointer 后面。下放过少会膨胀主文件，下放过多则可能藏起必需材料。

每个步骤的完成条件有两个维度：clarity 表示能否判断完成与否，demand 表示要求覆盖多少。“产生修改清单”与“每个被修改的模型均有交代”驱动的调查深度不同。原文认为最强的标准同时可检查且穷尽。

后续步骤可见时，Agent 可能急着转向后续工作。原文的修正次序是先把当前完成标准写清；只有边界不可避免地模糊，而且观察到抢跑，才拆分序列。隐藏后续步骤需要真实上下文边界；同一上下文里调用另一个流程，并不会移除后续内容。

这种拆分可能引入交接损失和协调成本，因此只能在收益足够时采用；写成多个文件本身不能保证当前步骤更深入。^[inferred]

## 语言压缩与修剪

Leading word 重复简短标签，single source of truth 则让权威定义只保留一处；二者并不冲突。重复整段含义会提高维护成本，并把某个规则的注意力权重抬得超过其真实重要性。

原文建议把可正向描述的要求写成目标行为，例如“写一行注释”。作者认为禁止式措辞可能激活被禁止行为；这是经验性写作主张，本文未独立验证其模型适用范围。必须保留的硬禁令仍应配上正向目标。

环境也是事实来源。脚本、配置、目录结构和 `--help` 容易查询的事实，复制进文档就是缓存。文档更值得保存查不出来的约定、选择理由、隐性陷阱，以及确实昂贵的查询结果。

逐句检查 relevance 与 no-op。过时内容会沉积为 sediment；模型默认就会执行的指令若没有行为增量，应删除整句。是不是 no-op 是模型相关的问题，要用运行结果裁决。

## Skill 专属分支

关联文档 `SKILL-MECHANICS.md` 将调用方式视为两种负担的取舍：

- **Model-invoked**：description 供模型发现，可保留用户手动调用；支付常驻 context load，换取自主发现与组合入口。
- **User-invoked**：`disable-model-invocation: true` 将调用责任交给用户；描述改成人可读摘要，触发词清单不再服务模型发现。
- **Router skill**：当手动 Skill 多到难以记忆时，用一个入口说明各 Skill 的用途与调用场景；按原文设定，它提示用户选择，而不自动触发其他 user-invoked Skill。

这些是该文采用的 Skill 机制模型。description 是否从上下文隐藏、其他 Skill 能否调用目标，都应以实际宿主实现为准；不能当成所有 Agent 系统的统一协议。^[inferred]

## 可复用审阅清单

1. 明确希望稳定的执行过程和完成结果。
2. 决定由 Agent 还是人负责发现文档。
3. 列出真正不同的触发分支，检查 pointer 是否覆盖且没有重复重述。
4. 区分步骤与参考；共用关键内容留近，分支资料外置，同一概念聚合。
5. 把完成条件写得可检查，并明确覆盖范围。
6. 观察实际抢跑后再判断是否需要真实上下文边界。
7. 用已有语义的 leading word 压缩重复解释，保留必要的约束。
8. 清除重复、环境缓存、过时层和无行为增量的句子。
9. 用实际任务检查漏触发、误触发、覆盖率和提前结束，再修正文档。^[inferred]

## 强点、边界与证据缺口

它把文档写作转换成注意力与执行路径设计，统一了 Skill description 和仓库文档引用的路由作用。它同时承认 context load 与人的 cognitive load，避免把 token 最小化当作唯一目标。^[inferred]

它不能补齐模型能力、工具权限或真实验证，也没有给出完整的对照评测集和方差指标。Leading words、否定措辞和序列拆分的效果，需要在目标模型与工作流中测试；静态审阅只能检查设计意图。^[inferred]

## Related

- [[wiki/concepts/Context Pointer]]
- [[wiki/concepts/Leading Words]]
- [[wiki/concepts/Agent Skill]]
- [[wiki/topics/Context Management]]
- [[wiki/syntheses/Agent Skill × Context Management]]
- [[wiki/syntheses/AGENTS.md as Repository Operation Contract]]
- [[wiki/concepts/Verification Loop]]
