---
title: Qiaomu Best Prompt Source Guide
type: source
status: seed
source_count: 1
updated: 2026-04-23
aliases:
  - 论文证实：用最常见最自然的Prompt，才能解锁大模型真正实力 source guide
  - qiaomu best prompt
  - 向阳乔木 best prompt
  - 文本频率法则 source guide
tags:
  - article
  - blog
  - ai
  - llm
  - prompting
  - source
---

# Qiaomu Best Prompt Source Guide

## Current role

这篇文章当前更适合作为一个 source-facing note 进入当前仓库，而不是直接升格成稳定母页。

原因不是它不重要，而是它本身是对一篇论文的二手解读。对当前仓库来说，它更像一个 prompt / LLM 方向的高价值输入来源：可以提炼出稳定判断，但不应该把文章里的全部实验叙述直接当成已经定型的知识。

## Source metadata

- Title: *论文证实：用最常见最自然的Prompt，才能解锁大模型真正实力*
- URL: https://blog.qiaomu.ai/bestprompt
- Site: 乔木博客
- Author: 向阳乔木
- Published: 2026-04-20
- Ingested: 2026-04-23
- Source type: blog article summarizing a research paper

## Why ingest this

- 它把一个很容易被误解成“prompt 只是写作技巧”的问题，重新表述为训练分布与表达频率问题。
- 它强化了一个更稳定的判断：语义保持近似不变时，prompt 的统计常见度/自然度会影响模型表现。
- 它给 prompt 优化提供了一个很实用的方向：先把表达改得更自然，再去堆叠额外技巧。
- 它也给当前 wiki 里的 `[[wiki/topics/Prompt Frequency]]` 提供了更明确的来源承接点。

## Distilled claims

- 文章主张：在语义不变时，更常见、更自然的表达通常更能帮助大模型发挥能力。
- 它把这条规律表述为“文本频率法则（Textual Frequency Law, TFL）”。
- 它强调高频表达与“简单表达”不是同一个维度，关键不是字少，而是模型在训练中更常见地见过类似表述。
- 文章称相关实验覆盖数学推理、常识推理、机器翻译和工具调用等任务，高频版本整体更优。
- 它还声称高频输入不只改善最终答案，也改善推理过程质量。
- 除 prompt 改写外，文章还提到文本频率蒸馏（TFD）和课程文本频率训练（CTFT）等训练/微调方向。
- 对普通实践者来说，这篇文章给出的直接操作建议是：减少生硬、书面、罕见表达，优先用自然、常见、真实人会说的话描述任务。

## Candidate wiki destinations

### [[wiki/topics/Prompt Frequency]]

应直接吸收。

可吸收的判断：
- prompt 的表达频率/自然度会影响模型表现。
- 改 prompt 时，优先尝试自然改写，而不是先增加复杂控制项。
- “高频”比“简单”更接近真正的解释变量。

### [[wiki/maps/AI Map]]

应作为 source note 接入。

可吸收的作用：
- 作为 prompting / LLM 方向的来源入口。
- 与 reasoning、workflow、context management 等主题形成互补来源层。

## What should stay source-only

以下内容目前更适合保留在 source layer，而不应直接升格成稳定结论：

- 文中引用实验的具体数值与模型名单
- TFPD、TFD、CTFT 的实验细节
- “这条规律已经被论文完全证实”这类过强表述
- 对上游原论文尚未核实的具体细节

当前更值得沉淀的，是它提出的问题切分：prompt 优化不只是信息补充，也是在调整输入表达与训练分布之间的贴合度。

## Open questions

- 上游原论文的准确标题、作者列表与链接是什么？
- 文章中的“频率”具体是如何度量的：语料统计、语言模型概率，还是别的指标？
- 这条规律在中文任务、强格式任务、精确约束任务里是否同样稳定？
- 后续如果继续 ingest prompting 方向资料，是否要把 `Prompt Frequency` 继续提升为更高层的 synthesis？

## Related

- [[wiki/topics/Prompt Frequency]]
- [[wiki/maps/AI Map]]