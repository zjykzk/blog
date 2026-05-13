---
title: Agentic AI Architecture Taxonomy
type: concept
status: seed
summary: Agentic AI Architecture Taxonomy decomposes agent systems into core components, cognitive architecture, learning, multi-agent systems, environments, and evaluation.
category: concepts
sources:
  - https://arxiv.org/abs/2601.12560v1
created: 2026-05-13T10:37:07+08:00
updated: 2026-05-13T10:37:07+08:00
base_confidence: 0.57
lifecycle: draft
lifecycle_changed: "2026-05-13"
provenance:
  extracted: 0.86
  inferred: 0.12
  ambiguous: 0.02
aliases:
  - agentic AI taxonomy
  - LLM agent architecture taxonomy
tags:
  - agents
  - architecture
  - taxonomy
---
# Agentic AI Architecture Taxonomy

Agentic AI Architecture Taxonomy 是论文提出的六维分类框架，用来把 LLM agent 从“功能清单”还原成系统架构：

1. **Core Components**：perception、memory、action/tool、profiling。
2. **Cognitive Architecture**：planning、reflection，以及从 ReAct 到 tree search / recursive decomposition 的推理结构。
3. **Learning**：in-context learning、fine-tuning、RLHF/RLAIF 等让 agent 获取或调整能力的路径。
4. **Multi Agent Systems**：chain、star、mesh、hierarchical 等协作拓扑。
5. **Environments and Domains**：web、OS、software engineering、robotics、games、healthcare、science、finance 等任务环境。
6. **Evaluation and Safety**：cost、latency、accuracy、security、stability 以及 prompt injection、infinite loops、hallucination in action 等风险。

这个 taxonomy 的关键不是列更多术语，而是把 agent architecture 的不同问题拆到不同层：感知世界、保存状态、生成计划、执行动作、多人协作、部署到环境、接受评估和安全约束。

## Relation to Existing Wiki Vocabulary

这套 taxonomy 与当前 wiki 的 [[wiki/syntheses/Agent System Design Space]] 很契合：它把 design space 中已有的 context、tool、memory、verification、permission、recovery、orchestration 等线索放进一个论文级架构框架。

但它也暴露一个边界：论文的 taxonomy 偏 survey / architecture inventory，当前 wiki 更强调 harness 作为运行秩序层如何把这些组件治理起来。^[inferred]

## Related

- [[wiki/concepts/Agentic Control Loop]]
- [[wiki/topics/AI Harness]]
- [[wiki/topics/AI Memory]]
- [[wiki/concepts/Agent Action Space]]
- [[wiki/syntheses/Agent System Design Space]]
- [[wiki/sources/Agentic Artificial Intelligence Paper Source Guide]]
