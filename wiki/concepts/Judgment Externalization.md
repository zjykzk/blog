---
title: Judgment Externalization
type: concept
status: draft
category: concepts
tags: [software-engineering, ai-coding, judgment, testing, feedback]
aliases:
  - 判定外化
  - 判断外化
  - 外置判定
relationships:
  - target: "[[wiki/concepts/Formalization]]"
    type: uses
  - target: "[[wiki/concepts/Executable Specification]]"
    type: uses
  - target: "[[wiki/concepts/Verification Loop]]"
    type: implements
  - target: "[[wiki/concepts/Verification Gap]]"
    type: related_to
sources:
  - conversation:2026-09-29
  - Excalidraw/ai effective.md
created: 2026-09-29T18:14:09+0800
updated: 2026-09-29T18:14:09+0800
summary: >-
  判定外化把只存在于个人或模型内部的判断依据，变成可保存、版本化、机器执行、复核和修正的组织资产，使机器批量判定而人只处理规则、校准与例外。
provenance:
  extracted: 0.58
  inferred: 0.40
  ambiguous: 0.02
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-09-29
tier: supporting
---

# Judgment Externalization

判定外化是把原本只存在于某个执行者内部的判断依据，变成执行者之外可保存、版本化、机器执行、复核和修正的对象。外化的是判定依据与治理结构，不是排除大模型这个执行者。

## What It Is

当工程师凭经验说“这段实现没问题”时，规则、证据、边界和例外可能仍混在他的个人理解中。换一个人接手，需要重新形成同样的经验；人离开后，组织也难以重算当时的判断。

把验收规则、正反例、评测集、事故样本、证据来源和升级条件保存下来，再让程序或大模型据此判定，判断便不再只寄存在执行者身上。模型仍可担任判定者，但它不再同时垄断标准、证据、结果和修改权。

判定外化不等于普通文档化。普通文档让人能够阅读，外化判定则要求这些材料能稳定进入执行流程，让系统产生通过、失败、重试或升级人工等后果。它也不要求所有规则都变成确定性代码；自然语言 rubric 可以由大模型执行，只是证据强度低于类型、测试和形式约束。^[inferred]

## Two Gates of Correctness

判定至少覆盖两段不同关系：

```text
真实需要
    | validation：规格是否对准现实
    v
需求 / 规格 / 验收标准
    | verification：实现是否满足规格
    v
代码 / 系统行为
```

[[wiki/concepts/Executable Specification]] 主要把第二道门变成机器可检查承诺。它也能帮助第一道门，因为规则一旦被写成具体输入、行为和结果，需求中的歧义就更容易暴露。但测试全部通过只能说明实现满足了测试所表达的规格，不能单独证明规格代表真实需要。

Validation 也不只能由人手工完成。机器可以重放真实场景、比较生产指标、检查法规数据并发现规格与现实的偏差；人负责选择哪些信号代表目标，以及在信号冲突时接受什么代价。^[inferred]

## What Gets Externalized

判定系统至少需要四类资产：

| 层 | 外化对象 | 作用 |
|---|---|---|
| 标准 | 规则、约束、rubric、阈值 | 说明什么算对 |
| 证据 | 正反例、评测集、历史事故、生产数据 | 给判断提供现实锚点 |
| 执行 | 测试、程序检查、LLM judge、仿真、监控 | 批量运行判定 |
| 治理 | 版本、轨迹、权限、异常升级、抽样审计、规则修正 | 让判定可追责并持续校准 |

“历史经验”只有被转换成事故案例、边界条件、反例、新规则或评测样本之后，才成为可复用的外化资产。只把经验写成一段无法进入判定过程的叙述，仍不足以改变系统行为。^[inferred]

## How It Scales Judgment

判定外化的直接目标不是让人更方便地逐件审核，而是让机器可以重复执行人的判断。人的成本从每个结果都判断一次，转成前置设计规则、定期抽样校准和处理少量例外。

```text
人定义目标、规则与风险边界
              |
              v
     规则 + 样本 + 评测 + 证据
              |
              v
    程序硬检查 + 大模型语义判定
              |
       +------+------+
       |             |
       v             v
自动通过 / 退回    冲突 / 新场景 / 高风险
                         |
                         v
                    人工异常裁决
                         |
                         v
                  新规则与新样本
                         |
                         +---- 回到判定系统
```

如果每个 AI 输出都需要人从头理解并批准，判定还没有被充分外化，系统只是把代码生产瓶颈搬成了人工验收瓶颈。成熟系统应让明确通过和明确失败自动流转，只把低置信度、证据冲突、规则空白和高风险例外送回人。^[inferred]

这条闭环与 [[wiki/concepts/Verification Loop]] 的差别在于：verification loop 描述执行结果如何触发检查和修正；判定外化强调使这套检查得以脱离个人、跨执行者复用的资产与治理条件。

## Organizational Effects

判定体系具有固定建设成本，规模经济来自相似判断的重复使用，而不只是组织人数多。大组织只有在能跨团队共享规则、评测集和基础设施时，才能把建设成本摊到大量判定上；部门孤岛和规则高度异质会抵消这种优势。^[inferred]

小团队在业务能够接受通用模型和通用判定标准时，可以直接采购能力并避开历史包袱。中型组织更容易处在夹层：业务特殊到不能完全购买通用能力，复用规模又不足以摊薄自建体系。这个方向的机制比影响幅度更可信，不能把它写成所有企业必然遵循的规模规律。^[ambiguous]

个人角色也随之迁移：从逐件生产和审核，变成设计规则、校准判定系统和处理例外。简单任务被自动化会压缩新人形成判断力的练习场，因此组织需要主动建立模拟任务、事故复盘和逐级责任，而不能让新人直接承担“审核一个比自己懂得多的机器”。^[inferred]

## Failure Modes

- **同一黑箱包办一切**：模型临时定义标准、执行任务并宣布自己通过，没有独立规则和证据。
- **人工全量审核**：所有结果都回到人，机器生成吞吐无法转化为交付吞吐。
- **代理指标漂移**：机器稳定优化可测指标，却逐渐偏离用户和业务真正需要。
- **判定者相关失误**：生成模型和 judge 共享相同盲点，自洽不能替代独立证据。
- **规则僵化**：旧经验获得门禁权后不再接受现实反馈，外化从知识资产变成路径锁定。
- **无轨迹判定**：只有“通过/失败”，没有规则版本、输入证据和执行配置，结果无法重放。

## Recognition Test

判断一项 AI 判定是否真正外化，可以问：拿掉当前模型或当前专家以后，规则和证据是否仍然存在；换一个执行者，能否沿同一依据重新判断；发生分歧时，能否定位应该修改实现、规格、证据还是判定器。

外化的成熟标志不是“机器说了算”，而是机器能以接近生成的速度执行大多数判定，同时组织仍能知道它依据什么、在哪些条件下必须把决定权交还给人。

## Related

- [[wiki/concepts/Formalization]] — 把隐含区别与判断条件改写成可重复执行的结构。
- [[wiki/concepts/Executable Specification]] — 把意图压成机器可检查承诺。
- [[wiki/concepts/Verification Gap]] — 解释为什么判定吞吐成为 AI coding 的产能约束。
- [[wiki/concepts/Verifier Hierarchy]] — 比较程序执行、模型裁判、人类判断与形式约束的证据强度。
- [[wiki/concepts/Agent Loop Human Judgment Positions]] — 定位人应保留的价值、边界、否决和异常裁决位置。
- [[wiki/concepts/Harness Ratchet]] — 把重复失败沉淀为下一轮可执行约束。
- [[wiki/sources/Software Engineering 3.0 Judgment Shift Source Guide]] — 本概念的文章与图示来源。
