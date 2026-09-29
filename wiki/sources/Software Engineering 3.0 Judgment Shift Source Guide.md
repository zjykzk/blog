---
title: Software Engineering 3.0 Judgment Shift Source Guide
type: source
status: draft
category: sources
tags: [article, software-engineering, ai-coding, judgment, organization]
aliases:
  - 软件工程 3.0 判定转向
  - 软件工程 3.0 六个判断
  - 软件工程3.0判定外化
relationships:
  - target: "[[wiki/concepts/Judgment Externalization]]"
    type: related_to
  - target: "[[wiki/concepts/Verification Gap]]"
    type: related_to
  - target: "[[wiki/topics/Modern Software Engineering]]"
    type: related_to
sources:
  - conversation:2026-09-29
  - Excalidraw/ai effective.md
created: 2026-09-29T18:14:09+0800
updated: 2026-09-29T18:14:09+0800
summary: >-
  保存软件工程 3.0 文章的六条判断及配套 Excalidraw：AI 使生成变便宜后，工程重心从动作上移到判定，组织竞争力转向可执行、可审计、可反馈的判定资产。
provenance:
  extracted: 0.82
  inferred: 0.16
  ambiguous: 0.02
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-09-29
tier: supporting
---

# Software Engineering 3.0 Judgment Shift Source Guide

> Source: 用户提供的《软件工程 3.0》中文长文及其结构图 [[Excalidraw/ai effective|AI effective]]。

## Capture Policy

这页保存文章的 source-level 论证、六个判断和后续讨论对图中概念的校正。文章中的行业类比、组织规模效应和长期人才影响保持为 source-reported claims；从对话中补出的 validation / verification 边界、判定系统分层和适用条件标为推论。

稳定机制另行沉淀为 [[wiki/concepts/Judgment Externalization]]。它不把整篇文章升格为已证实理论，而是保留“从生成到判定”的可复用结构。

## Source Diagram

![[Excalidraw/ai effective]]

图中主干为：AI coding 具有高速、大量、概率性和不可追责等特征；人的判定精力无法按同一速度扩张，因此判定成为稀缺能力；解法是把判定外化为规则、正负样本、评测集、历史事故、执行器和治理结构，再由程序与大模型批量执行。

## Core Question

文章追问：软件已经能够测量交付速度、缺陷密度和构建时长，为什么仍然难以稳定测量最昂贵的偏差——一段需求是否被正确理解，并转化为正确的软件行为？

传统组织把大量答案留在工程师的经验、上下文记忆和责任心中。大模型扩大生成吞吐后，个人无法继续按产出数量逐件理解和担保结果，正确性因而需要进入一套机器可执行、可审计和可反馈的系统结构。

## Six Judgments

### 1. 自动化单位从工序上移到链路

文章以铁路联锁区分两种自动化：工序自动化减少某一步的人力，链路自动化则通过约束关系阻止错误组合出现。软件工程 3.0 不只自动格式化、检查、编码或生成测试，而是让需求、设计、实现、测试、部署和运行反馈互相约束。

链路闭合的验收标准是：一次失败能否回溯到上游那个被证伪的假设，并把修正沉淀进下一轮执行。

### 2. 判定权从手感移交给可审计规则

文章借复式记账和审计说明，信任可以从“这个人可信”转成“别人能够重算这笔账”。软件中的对应变化是把代码质量和业务正确性的判断，改写为可以执行、审阅和版本化的判定。

手感并未消失，而是从写实现迁移到制定规则、选择证据和处理例外。门禁是否拥有真正的阻断权，决定规则是建议还是约束。

### 3. 分水岭是知识可编码程度

模型放大组织已经表达清楚的部分。规则、数据结构、失败条件和评测集越明确，模型越容易获得可靠反馈；知识仍散落在个人经验中时，高速生成会放大含混。

高可编码业务更容易获得直接自动化收益。低可编码业务也可能从 AI 获益，但首要收益是暴露组织没有说清的判断，而不是立即替代执行。^[inferred]

### 4. 简单任务先自动化会造成逆向选择

输入输出清楚、容易验收的工作最先被机器接管。文章认为这会减少知识沉淀，增加机器生成债务，并切断新人从简单任务进入领域的学习路径。长期风险不是新人立刻失业，而是中层骨干和领域判断出现断层。

因此自动化既可以被当作当期收入，也可以被当作长期资本。前者只追求更多产出，后者把每次失败变成可继承的规则、样本和系统能力。

### 5. 规模经济临界点改变

文章把企业的判定资产比作农业中的“自留种”：模型可以买到，组织对“什么算对”的评测集、正负样本和历史失败却难以直接购买。

大组织只有在大量相似判断能够共享规则、评测集和基础设施时，才能摊薄固定建设成本。小团队在业务可以接受通用能力时能直接采购并避开历史包袱。中型组织可能同时面临特殊业务需求和不足以摊薄自建成本的复用规模。这条判断的机制比影响幅度更可信。^[ambiguous]

### 6. 代码退回中间产物

当意图、约束和验收标准成为稳定资产，代码可以被理解为规格的一次实例化。工程技能因而从掌握实现语言，部分迁移到把要求写成无歧义约束。

这条判断存在硬边界：只有已经被说清的约束才能机械化。代码仍然保存大量没有进入规格的兼容处理、性能知识和历史修复，因此“代码可随时重建”只在规格、验证、环境和依赖都足够完整时成立。^[inferred]

## Concept Structure

```text
执行者变化
人：慢、能接触上下文、可以承担责任
模型：快、概率性、缺乏稳定自知、不能承担组织责任
            |
            v
生成速度超过人工理解与复核速度
            |
            v
判定成为稀缺能力
            |
            v
判定外化
标准 + 证据 + 执行 + 治理
            |
            v
程序硬检查 + 大模型语义判定
            |
     自动通过 / 失败
            |
     少量例外回到人
            |
            v
人的裁决沉淀为新规则和新样本
```

## Reasoning Flow

文章先用制药、造桥、临床、铁路和会计建立“手感转成公共判定程序”的工程化模型，再指出软件长期无法稳定测量意图到实现的翻译是否正确。

大模型不是普通工具升级，因为它开始承担分析、设计和实现等认知执行。它的高速与概率性使个人担保无法随产出同比扩张，工程瓶颈因而从生成转向判定。

判定要获得机器速度，就必须从个人经验中外化出来，形成标准、证据、执行器与治理结构。机器负责大多数重复判定，人从逐件审核退到目标定义、规则设计、抽样校准和异常裁决。^[inferred]

这套变化进一步重排组织优势、人才培养和软件资产形态：可复用的判定密度成为组织能力，简单工作消失迫使组织重建学徒路径，代码则在部分场景中退为规格的一次生成结果。

## Latent Assumptions and Boundaries

- **工程化不只是量化。** 许多判断不能压成单一数字，但仍能外化为程序、案例、rubric 和异议处理流程。^[inferred]
- **规则可审计不等于规则正确。** [[wiki/concepts/Executable Specification]] 区分 validation 与 verification：实现符合规格，不证明规格对准真实需要。
- **外化不等于人工全审。** 外化的直接目的就是让程序和模型批量执行判断；若每件产出都回到人，验证鸿沟没有被解决。^[inferred]
- **模型可以执行判定。** 只要规则、证据、配置和结果能在调用之外保存，概率性的 LLM judge 也属于外化判定的一部分。^[inferred]
- **反馈不自动形成学习。** 失败只有转化成新规则、样本、门禁或工作流修改，才会成为组织资本。^[inferred]
- **规模经济依赖可复用性。** 大企业人数和调用量本身不能摊薄知识异质、组织孤岛和重复建设。^[inferred]
- **形式化有认知边界。** 尚未被专家想清、价值冲突未被解决或高度依赖开放现实的判断，不能仅靠更强模型变成确定规则。

## Change Mechanisms

文章隐含两条相反的积累回路。正向回路把专家判断写成规则，让机器扩大执行规模；真实失败再补充证据，推动规则变强。负向回路则让组织只追求生成数量，新人失去实践入口，人工审核逐渐形式化，认知债务和无人敢改的代码持续累积。^[inferred]

```text
判定资本回路
专家判断外化 -> 机器批量执行 -> 真实反馈 -> 新规则/样本 -> 可委托范围扩大

认知耗损回路
简单任务自动化 -> 学习入口消失 -> 旁观式批准 -> 认知债务 -> 更难验证
```

## Article Series

- [软件工程3.0宣言（2026年版）](https://mp.weixin.qq.com/s?__biz=MjM5ODczMDc1Mw==&mid=2651863238&idx=1&sn=ef6dd436ae1af4e50d13e56f7a37cd23&scene=21#wechat_redirect)
- [「软件工程3.0」十大开发原则](https://mp.weixin.qq.com/s?__biz=MjM5ODczMDc1Mw==&mid=2651863261&idx=1&sn=be67673c0465abf43c9c605b33b47aa5&scene=21#wechat_redirect)
- [软件工程3.0的理论基础（3）——复杂性科学](https://mp.weixin.qq.com/s?__biz=MjM5ODczMDc1Mw==&mid=2651863340&idx=1&sn=2e2c176719e6889f1e9683ac137a5852&scene=21#wechat_redirect)
- [透过图谱：解码软件工程3.0核心密码](https://mp.weixin.qq.com/s?__biz=MjM5ODczMDc1Mw==&mid=2651862995&idx=1&sn=962b2d0432d37006cdd2c0584c8e81a3&scene=21#wechat_redirect)
- [软件工程3.0方法论核心架构：IDAKE](https://mp.weixin.qq.com/s?__biz=MjM5ODczMDc1Mw==&mid=2651863392&idx=1&sn=7ff8b1ec1db77302df12671d5f81bbbe&scene=21#wechat_redirect)
- [软件工程3.0三年之路：从概念到规模化落地的探索与实践](https://mp.weixin.qq.com/s?__biz=MjM5ODczMDc1Mw==&mid=2651863434&idx=1&sn=285b6f605e5d80e18e7401efbbee30bd&scene=21#wechat_redirect)
- [2025 年终回顾：软件工程 3.0 全面落地，AI 重塑研发新范式](https://mp.weixin.qq.com/s?__biz=MjM5ODczMDc1Mw==&mid=2651862927&idx=1&sn=aee9932abdf4242fd420cd3a50c422b7&scene=21#wechat_redirect)
- [「软件工程3.0方法论」已成为企业的必选项](https://mp.weixin.qq.com/s?__biz=MjM5ODczMDc1Mw==&mid=2651863672&idx=1&sn=4cb71cdbfc8c6b40603fa660204a97dc&scene=21#wechat_redirect)
- [未来趋势：从“让模型像人一样工作”到“让模型像基础设施一样可靠”](https://mp.weixin.qq.com/s?__biz=MjM5ODczMDc1Mw==&mid=2651864340&idx=1&sn=a4342ced9264636c3888aeab96a64c43&scene=21#wechat_redirect)
- [为什么智能体时代，「软件工程」从“奢侈品”变成生存基础？](https://mp.weixin.qq.com/s?__biz=MjM5ODczMDc1Mw==&mid=2651864352&idx=1&sn=791b914aa50a4d8498dc081ce4656a49&scene=21#wechat_redirect)

## Related

- [[wiki/concepts/Judgment Externalization]]
- [[wiki/concepts/Verification Gap]]
- [[wiki/concepts/Executable Specification]]
- [[wiki/concepts/Formalization]]
- [[wiki/concepts/Attention as the Scarce Resource]]
- [[wiki/topics/Modern Software Engineering]]
- [[wiki/sources/软件工程真正降临 Source Guide]]
- [[wiki/sources/AI 什么都能写与软件价值重心转移 Source Guide]]
