---
title: Retrieval vs Reasoning
type: concept
status: draft
category: concepts
tags:
  - reasoning
  - retrieval
  - agents
  - llm
aliases:
  - 检索与推理
  - 检索 vs 推理
  - Retrieval and Reasoning
sources:
  - https://chatgpt.com/share/6a8bbde7-a668-83ee-a76f-60ff58322ccb
created: 2026-08-24T11:50:39+0800
updated: 2026-08-24T11:50:39+0800
summary: 检索是从已有信息空间找到已存在的答案（找节点），推理是依据已有信息与规则产生原本没有直接给出的新结论（建边）。
provenance:
  extracted: 0.92
  inferred: 0.08
  ambiguous: 0.0
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-08-24
tier: supporting
relationships:
  - target: "[[wiki/concepts/LLM Reasoning as In-Context Computation]]"
    type: related_to
  - target: "[[wiki/concepts/Reasoning as Structure Mapping]]"
    type: related_to
  - target: "[[wiki/concepts/Codebase Retrieval Index]]"
    type: related_to
---

# Retrieval vs Reasoning

检索和推理是两种完全不同的认知操作：**检索从已有的信息空间中找到答案；推理根据已有信息，通过规则或关系推出新的结论。**

## What It Is

- **检索（Retrieval）**：找到一条已经存在的信息。问"爱因斯坦什么时候获得诺贝尔物理学奖"，从知识库找到"1921 年"，就是检索。
- **推理（Reasoning）**：从多条已有信息产生一条**原本没有直接给出**的结论。已知"所有人都会死亡"和"苏格拉底是人"，得出"苏格拉底会死亡"，就是推理。

一句压缩：

```text
检索 = 找已有东西        推理 = 产生新的东西
检索 = 找"节点"          推理 = 建"边"
```

## How It Works

从信息流看，二者是先后两级：

```text
外部信息空间
    │ 检索（查找 / 匹配 / 召回）
    ▼
已存在的信息
    │ 推理（分析 / 演绎 / 归纳）
    ▼
新的结论 / 判断
```

检索先把相关"节点"（事实材料）取回来，推理再在节点之间建立"边"（因果、关系、解释结构）。回答"为什么秦国能统一六国"，检索找到 商鞅变法、军功爵制、关中地理、远交近攻 等节点，推理才把 `商鞅变法 → 提高动员能力 → 军事优势 → 兼并扩大 → 六国无法结盟 → 统一` 这些箭头连起来。这正是 [[wiki/concepts/Reasoning as Structure Mapping|结构映射式推理]]所说的"关系对关系"。

## Contrast Table

| | 检索 | 推理 |
|---|---|---|
| 核心问题 | "哪里有这个信息？" | "这些信息意味着什么？" |
| 操作 | 查找、匹配、召回 | 分析、演绎、归纳 |
| 输入 | 信息需求 | 前提 / 事实 |
| 输出 | 已存在的信息 | 新的结论 |
| 是否产生新知识 | 通常不产生 | 可以产生 |
| 典型技术 | 搜索、倒排索引、向量检索、数据库查询 | 逻辑推理、数学推导、因果分析、规划 |

## Why It Matters

- **推理的结果不保证正确**。「小明今天没打卡 / 昨天说不舒服 / 今天是工作日」→「小明可能生病了」仍是推理，只是属于**不确定推理**。所以推理 ≠ 事实，而是从事实推导出来的结论。
- **一个系统检索能力强，不代表推理能力强**。检索解决"我知道什么"，推理解决"这些东西之间是什么关系、由此能推出什么"。二者是相互独立的能力维度。^[inferred]
- **RAG 的思想**正来自这个区分：不要让模型只依赖自身记忆，先把相关事实**检索**出来，再基于这些事实**推理**——检索提供事实材料，推理建立事实之间的关系。

在 [[wiki/syntheses/Agent as Problem-Solving System|Agent 问题求解闭环]]里，检索是在**扩大系统所知道的世界**（降低对当前状态的不确定性），推理是在**已有世界模型上计算**，二者与规划、行动一起构成"检索→推理→行动→新信息→再推理"的循环。

## Related

- [[wiki/concepts/LLM Reasoning as In-Context Computation]]
- [[wiki/concepts/Planning as Goal-Directed Reasoning]]
- [[wiki/concepts/Reasoning as Structure Mapping]]
- [[wiki/concepts/Codebase Retrieval Index]]
- [[wiki/syntheses/Agent as Problem-Solving System]]
- [[wiki/sources/检索推理规划与Agent问题求解 Source Guide]]
