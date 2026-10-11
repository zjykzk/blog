---
title: Rule Adjudication Agent Evaluation
type: topic
status: draft
category: topics
tags: [agents, testing, metrics, judgment, feedback]
aliases:
  - 规则裁决 Agent 评测
  - 合规判断 Agent 评测
  - 规则符合性 Agent 评测
relationships:
  - target: "[[wiki/concepts/Agent Evaluation Metric Vector]]"
    type: extends
  - target: "[[wiki/concepts/Confusion Matrix]]"
    type: uses
  - target: "[[wiki/concepts/Judgment Externalization]]"
    type: uses
  - target: "[[wiki/concepts/Evaluation]]"
    type: related_to
sources:
  - conversation:2026-10-10
created: 2026-10-10T19:36:48+0800
updated: 2026-10-10T19:36:48+0800
summary: >-
  规则裁决 Agent 评测把合规判断拆成适用性、事实、构成要件、例外和证据充分性，并用多类结论、裁决图、边界样本和错误方向评估可靠性。
provenance:
  extracted: 0.82
  inferred: 0.17
  ambiguous: 0.01
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-10-10
tier: supporting
---

# Rule Adjudication Agent Evaluation

规则裁决 Agent 的任务不是把数据做成“合规/违规”二分类，而是完成一次可审计的规则裁决：确定规则是否适用，从数据中提取相关事实，逐项判断构成要件，检查例外与版本，再在证据边界内给出结论。

## Core Formula

对禁止性规则，违规判断可以压缩为：

~~~
Violation =
  Applicable(rule, context)
  AND RulePredicate(relevant facts)
  AND NOT ValidException
  AND SufficientEvidence
~~~

义务性、许可性或豁免性规则需要改写 RulePredicate，但裁决链不变：适用性、事实、要件、例外和证据充分性缺一不可。

最终输出至少保留五类：

- VIOLATION：有充分证据证明违规；
- COMPLIANT：有充分证据证明满足规则；
- NOT_APPLICABLE：规则不适用于当前主体、地域、时间或场景；
- INSUFFICIENT_EVIDENCE：关键事实缺失，不能完成裁决；
- CONFLICT_OR_REVIEW：规则冲突、语义歧义或风险过高，需要人工处理。

COMPLIANT 不等于 NOT PROVEN VIOLATION。缺少必要字段时，正确输出通常是证据不足，而不是默认合规。

## Principle

评测首先检查裁决链是否正确，再检查最终标签。只对标签判分会奖励“猜中答案但理由错误”的系统，也无法判断错误来自规则检索、事实提取、要件判断、例外处理还是证据不足时的过度裁决。

这是一种 [[wiki/concepts/Judgment Externalization|判定外化]]：标准答案不只保存结论，还保存规则版本、相关事实、证据位置、构成要件和例外，使另一个执行者能够沿同一依据重放判断。

## Two Evaluation Tracks

### Given-Rule Track

评测直接提供规则正文、版本和适用背景，只测试事实提取、规则解释、要件判断、例外处理、证据引用和最终裁决。这条赛道更接近纯粹的规则应用能力。

### Rule-Retrieval Track

评测只提供规则库，让 Agent 自己找到适用规则。这条赛道额外测试规则召回、地域与主体范围、生效时间、上下位规则和冲突处理。

两条赛道必须分开报告。否则同一个错误既可能表示“没有找到规则”，也可能表示“规则找对但应用错误”。

## Gold Adjudication Record

每道题的标准答案应是一张裁决图，而不是一个标签：

~~~yaml
applicable: true
rule_id: rule-17
rule_version: "2026-01-01"
relevant_facts:
  - fact: "交易金额为 120 万元"
    evidence: "transactions[3].amount"
elements:
  - element: "交易金额超过 100 万元"
    status: satisfied
  - element: "未履行申报义务"
    status: satisfied
exceptions:
  - exception: "集团内部豁免"
    status: not_satisfied
verdict: violation
review_required: false
~~~

裁决图让评测能够给出阶段分数，并定位第一个上游错误。它也使 [[wiki/concepts/Verification Loop]] 能把具体失败回流成规则修正、数据补全或新测试，而不是只留下一个不可解释的总分。^[inferred]

## Test Matrix

高价值样本应覆盖以下层次：

| 样本类型 | 主要测试 |
|---|---|
| 明确符合、明确违规 | 基础裁决能力 |
| 阈值两侧的最小差异样本 | 比较符、单位和边界 |
| 缺少关键字段 | 正确拒判 |
| 存在例外、豁免 | 是否机械套用主规则 |
| 规则不适用 | 主体、地域、时间和场景 |
| 多条规则冲突 | 优先级与人工升级 |
| 旧版与新版规则 | 生效时间和版本 |
| 无关噪声与字段重排 | 相关事实识别与不变性 |
| 数据内部矛盾 | 冲突检测 |
| 对抗性命名或措辞 | 是否被表面文字诱导 |

成对样本比孤立样本更有诊断力。最小差异测试只改变一个决定性事实，结论应随之翻转；不变性测试只改变无关字段顺序、实体名称或表达方式，结论不应改变。

## Metrics

评测结果应报告一个指标向量，而不是只报告总准确率：

- 最终结论 [[wiki/concepts/Confusion Matrix|混淆矩阵]]；
- 违规召回率和错误放行率；
- 合规误伤率；
- 规则适用性准确率；
- 构成要件判断准确率；
- 证据引用 precision / recall；
- 例外条款召回率；
- 正确拒判率；
- 置信度校准；
- 多次运行的一致性。

风险发现、自动拒绝和执法处罚使用不同的错误代价。前者通常更怕漏报，后两者通常更怕误伤；因此应按业务代价选择 operating point，而不是声明一个脱离场景的“最佳准确率”。^[inferred]

## Quality Checks

- 标签必须互斥且定义清楚；
- 标准答案由领域专家编写，并经过独立复核与争议裁决；
- 规则正文、版本、生效时间和适用范围必须冻结；
- 开放式理由不能只由一个 LLM judge 决定；
- 高风险样本必须检查证据位置与完整轨迹；
- 同一 Agent 应在多个 seed 或多次运行中评估一致性；
- 报告必须分离端到端错误和各阶段错误。

## Common Failure Modes

- 强迫所有案例进入“符合/违规”两类；
- 把未证明违规当作符合；
- 标准答案只有标签，没有裁决依据；
- 忽略规则版本、地域、主体或生效时间；
- 只看总体准确率，隐藏漏报和误伤方向；
- 用表述相似度代替事实、状态和要件检查；
- 让生成模型同时定义标准、执行任务并宣布自己通过；
- 在证据不足或规则冲突时仍要求 Agent 给出确定结论。

## Related

- [[wiki/concepts/Agent Evaluation Metric Vector]] — 通用 Agent 轨迹指标向量。
- [[wiki/concepts/Confusion Matrix]] — 展开最终标签的错误方向。
- [[wiki/concepts/Judgment Externalization]] — 把规则、证据、执行与治理变成可复核资产。
- [[wiki/concepts/Evaluation]] — 评价对象、尺度、语境和评价者位置的一般结构。
- [[wiki/sources/AI Evals FAQ Source Guide]] — 从真实失败建立 rubric 和回归评测。
- [[wiki/sources/Agent Benchmark Landscape Research Report Source Guide]] — 通用 Agent benchmark 地图、方法学陷阱与三层评测组合。

