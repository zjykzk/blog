---
title: Memory-as-a-Tool Paper River Source Guide
category: sources
tags:
  - paper
  - arxiv
  - agents
  - memory
  - feedback
sources:
  - conversation:2026-06-10
  - https://arxiv.org/pdf/2601.05960
  - /Users/zenk/Documents/notes/20260610T103719--paper-river-memory-as-tool__paper_river.org
created: 2026-06-10T21:35:12+08:00
updated: 2026-06-10T21:35:12+08:00
summary: >-
  保留 Memory-as-a-Tool 论文倒读法：从 CoT、Self-Refine、Reflexion、MemGPT、MemLLM 到 Memory-R1，说明反馈如何从一次性修正变成可复用记忆原则。
provenance:
  extracted: 0.93
  inferred: 0.06
  ambiguous: 0.01
base_confidence: 0.39
lifecycle: draft
lifecycle_changed: 2026-06-10
aliases:
  - Distilling Feedback into Memory-as-a-Tool Paper River
  - Memory-as-a-Tool Paper River
  - Feedback Guideline Memory
---
# Memory-as-a-Tool Paper River Source Guide

> Source: `ljg-paper-river` reading of `https://arxiv.org/pdf/2601.05960`, plus the generated note at `/Users/zenk/Documents/notes/20260610T103719--paper-river-memory-as-tool__paper_river.org`.

## Capture Policy

这页保存当前会话生成的 Memory-as-a-Tool 论文倒读法，而不是替代目标论文的 primary paper source guide。它的价值在于保留一条问题演化线：测试时多想和自我修正有效，但反馈如果不能留下来，每次任务都会重新付费。

这条谱系是按问题相关性组织的主链。CoT、Self-Refine、Reflexion、MemGPT、MemLLM、Memory-R1 与目标论文属于确认相关的上游或邻近工作；Memori 是 2026 年相邻前沿，当前未确认直接引用或批判目标论文。^[ambiguous]

## What It Covers

目标论文 *Distilling Feedback into Memory-as-a-Tool for LLM Agents* 的核心问题是：模型被 rubric 批评之后，能不能把这次批评抽象成下次可用的行为原则，而不是只修当前答案。

这条 paper river 把目标论文放进三条汇合的研究线：

- 推理时计算：CoT 让模型在当前上下文里展开中间步骤。
- 自我修正：Self-Refine 和 Reflexion 把反馈、批评和反思引入生成循环。
- 外部记忆：MemGPT、MemLLM、Memory-R1 让记忆从上下文片段变成可管理、可读写、可学习的外部状态。

Memory-as-a-Tool 的转折是把 feedback 不再只当作当前答案的修补材料，而是蒸馏成文件系统里的 guideline。它更像给 agent 一本会更新的工作手册，而不是把所有历史都塞回 prompt。^[inferred]

## Preserved Content

### 问题之河

核心问题是：模型每次被批评之后，能不能真的记住教训，而不是下次又从零开始犯同样的错？

LLM 的许多“改进”发生在一次调用或一次任务内部。让模型先写、再批评、再重写，效果会变好；但任务结束后，批评信号也常常散掉。下一次遇到相似任务，系统还要重新花 token、时间和 money 生成反馈。参数微调能把行为固化下来，但慢、贵，并且不适合用户随时给出的私人 rubric。

于是问题一路从“怎样让模型多想一步”变成“怎样把多想一步留下来”。

### 溯源地图

```text
[2022] Wei et al. - Chain-of-Thought Prompting
  |
  | 问题: 模型直接答题太像猜答案, 中间推理没有展开
  | 解法: 让模型把中间步骤说出来, 用更多测试时计算换准确率
  v
[2023] Madaan et al. - Self-Refine
  |
  | 问题: 一次推理还不够, 初稿常有明显缺陷
  | 解法: 生成 -> 自评 -> 重写, 在同一题里循环修正
  v
[2023] Shinn et al. - Reflexion
  |
  | 问题: 反馈只改当前答案, 没有跨试次学习
  | 解法: 把失败后的反思写成文字, 下次试同类任务时再读
  v
[2023] Packer et al. - MemGPT
  |
  | 问题: 反思/历史塞进上下文会爆窗, 长期对话没有内存管理
  | 解法: 像操作系统一样管理不同层级的记忆
  v
[2024] Modarressi et al. - MemLLM
  |
  | 问题: 外部记忆常是脚手架, 模型不一定会稳定读写
  | 解法: 训练模型使用显式 read-write memory
  v
[2025] Yan et al. - Memory-R1
  |
  | 问题: 记忆管线多靠静态规则, 不知道何时增删改查
  | 解法: 用强化学习训练记忆管理和记忆使用
  v
[2026] Gallego - Memory-as-a-Tool
  |
  | 问题: 自我修正很有效但每题都要重做; 记忆系统又常存原始历史
  | 解法: 把 rubric 反馈抽象成可读、可编辑、可检索的文件原则
  v
[2026] Borro et al. - Memori (相邻前沿, 非确认引用)
  |
  | 问题: 长期记忆如果只是塞原始对话, 成本和噪声都太高
  | 解法: 把对话压成结构化 triples 和摘要, 做 API 层持久记忆
```

### 从 CoT 到 Self-Refine

Chain-of-Thought Prompting 看到的是直接回答太仓促。模型直接给最终答案时，复杂推理被压在最后一步，读者也不知道答案是算出来的还是蒙出来的。它像给模型草稿纸：先写中间步骤，再给最终答案。

Self-Refine 进一步看到：初稿常有明显缺陷，而一次生成把缺陷固定在答案里。它把一次生成变成 `draft -> feedback -> revised answer` 的小循环，不改参数，只是在测试时多跑几步。

这两步共同留下一个问题：当前答案可能更好，但反馈没有沉淀成未来任务可直接读取的资产。

### 从 Reflexion 到记忆治理

Reflexion 把“反馈 -> 重写当前答案”变成“反馈 -> 写一段反思 -> 下次带着反思行动”。这种自然语言反思像轻量记忆，不需要更新权重。

MemGPT 看到的是长期运行会撞上上下文窗口限制，于是借操作系统比喻管理不同层级的记忆。MemLLM 把显式 read-write memory 纳入模型训练目标，让模型学会和结构化外部记忆交互。Memory-R1 则把新增、更新、删除、保持不变这些操作变成可学习策略。

这条线把问题从“怎么反思”推进到“怎么治理记忆”。但如果目标只是保留 rubric feedback，用训练或 RL 管理整套记忆系统可能过重。

### Memory-as-a-Tool: 把一次性批评蒸馏成可复用原则

Memory-as-a-Tool 卡在两条线的交叉处：Self-Refine/Reflexion 说明反馈和反思有效，但常常一次性；MemGPT/MemLLM/Memory-R1 说明外部记忆重要，但许多系统保存的是历史、事实或 episode，而不是“我下次怎么做会更符合 rubric”。

它给模型一个文件系统式记忆工具。收到 rubric 反馈后，模型不只是改当前答案，而是把反馈抽象成通用 guideline，写入 `./memories/`。下次遇到新任务，模型先查看有哪些记忆文件，再按文件名读取相关原则，直接生成更像“已经被改过”的答案。

```text
Self-Refine:
  draft -> critique -> revised answer

Reflexion:
  trial -> feedback -> reflection text -> next trial

Memory-as-a-Tool:
  task -> feedback -> abstract guideline file
       -> future task -> retrieve guideline -> direct good answer
```

目标论文报告的关键效果是：Memory + Feedback 起点像 base model，但几轮反馈后接近或超过 self-critique，并且后续任务不需要完整批评-重写循环。长 horizon 混合任务实验也显示，记忆能跨任务类型积累。这些数值和实验结论应留在 source 层，等待后续复现或更多论文交叉验证。

它的新坑包括：文件名检索在几千个文件时会吃力；文件记忆可能碎片化；guideline 需要合并、遗忘、冲突解决和 provenance；如果模型把坏反馈抽象错，记忆会固化错误。

### 前沿延伸

截至 2026-06-10，当前捕获未找到直接引用或明确批判目标论文的后续论文。目标论文 arXiv 初版为 2026-01-09，PDF v2 为 2026-03-17，距离捕获时间较近。

Memori 属于相邻前沿：它把长期记忆做成 API 层数据结构，将对话压成语义 triples 和摘要以降低 token 成本与噪声。它和 Memory-as-a-Tool 的共同点是反对把原始历史全塞回 prompt；差别是 Memori 更偏事实/对话持久记忆基础设施，Memory-as-a-Tool 更偏从 feedback 中抽象可执行原则。^[inferred]

## Integration Decisions

这页应作为 Memory-as-a-Tool paper-river 的 source 层材料保留。关于目标论文的实验设置、Rubric Feedback Bench、具体表格和算法细节，可以后续单独创建 `Memory-as-a-Tool Paper Source Guide`；本页不替代 primary paper capture。

它对 [[wiki/topics/AI Memory]] 的补充是：AI memory 不只保存事实、对话和 episode，也可以保存从 feedback 中抽象出来的行为原则。这个原则层更接近 “working manual memory” 或 guideline memory，而不是普通 retrieval memory。^[inferred]

它对 [[wiki/concepts/Agent Memory Write-Manage-Read Loop]] 的补充是：Write 阶段不能只记录事件，还要把反馈抽象、去噪、命名和归档；Manage 阶段需要合并、遗忘、冲突解决；Read 阶段要根据任务读取少量可执行原则。

它和 [[wiki/syntheses/Verification Loop × Feedback Flywheel]] 的关系是：verification loop 捕获当前任务偏差，feedback flywheel 把偏差变成未来默认行为。Memory-as-a-Tool 是这条飞轮在 agent memory 层的一种轻量实现。^[inferred]

它也应接入 [[wiki/maps/Self-Evolving Agents Map]]：Reflexion 是轻量反思记忆，Memory-as-a-Tool 则把反思进一步蒸馏成文件化原则，介于运行时 memory 层和 skill/harness ratchet 层之间。

## Open Questions

- guideline 文件应该何时合并、何时分裂、何时归档？
- 文件名检索在大规模记忆库中会不会成为主要瓶颈？
- 如何验证一条 guideline 真正提升了未来任务，而不是把 judge 偏好或坏反馈固化？
- feedback guideline memory 和 skill repository、team standards、harness rules 之间的边界应该如何划分？
- 多 agent 或组织共享 guideline memory 时，权限、provenance、版本和 rollback 应该怎样设计？

## Related

- [[wiki/topics/AI Memory]]
- [[wiki/concepts/Agent Memory Write-Manage-Read Loop]]
- [[wiki/concepts/Agent Memory Mechanism Families]]
- [[wiki/concepts/Agent Memory Evaluation Stack]]
- [[wiki/syntheses/Verification Loop × Feedback Flywheel]]
- [[wiki/concepts/Feedback Flywheel]]
- [[wiki/concepts/Harness Ratchet]]
- [[wiki/maps/Self-Evolving Agents Map]]
- [[wiki/sources/Memory for Autonomous LLM Agents Source Guide]]
- [[wiki/sources/AI Memory Survey Source Guide]]
