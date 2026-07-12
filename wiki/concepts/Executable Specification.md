---
title: >-
  Executable Specification
category: concepts
tags: [software-engineering, specs, testing, ai-coding, verification]
sources:
  - conversation:2026-07-10
  - https://arxiv.org/pdf/2606.21894
  - https://arxiv.org/abs/2408.02232
  - https://github.com/scikit-learn/scikit-learn/issues/15534
  - https://github.com/scikit-learn/scikit-learn/pull/15535
created: 2026-07-10T20:16:00+0800
updated: 2026-07-12T00:30:14+0800
summary: >-
  Executable specification turns intent into machine-checkable commitments, separating validation of the spec from verification of the implementation.
provenance:
  extracted: 0.98
  inferred: 0.02
  ambiguous: 0.00
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-07-10
tier: supporting
aliases:
  - 可执行规格
  - executable specs
  - machine-checkable specification
  - V&V
relationships:
  - target: "[[wiki/topics/Spec-Driven Development]]"
    type: uses
  - target: "[[wiki/concepts/Verification Loop]]"
    type: implements
  - target: "[[wiki/concepts/Evidence Question Decomposition]]"
    type: uses
---

# Executable Specification

可执行规格是把“希望系统怎样”压成机器能检查的承诺：给定什么输入、处在什么条件、执行什么动作、必须看到什么结果。

## What It Is

可执行规格不是漂亮的需求文档，而是能被测试、验证器、脚本、类型系统、契约检查或运行时监控拿去判定“过 / 不过”的规格。

普通需求说：“导出账单时不要包含作废订单。”

可执行规格说：“给定一组包含正常订单、作废订单和跨部门订单的数据，当普通用户导出部门 A 的账单时，返回结果中的每一条订单都必须属于用户可见部门，且状态不是作废。”

前者表达愿望；后者提供靶子。AI coding 语境下，这个靶子尤其重要，因为生成器会很快把模糊意图补全成代码；如果意图没有被压成可检查承诺，生成速度会放大误解。

## How It Works

可执行规格通常从一条链路里长出来：

```text
模糊意图
-> 质量维度
-> 原子问题
-> 证据锚点
-> 可执行判断
-> 失败修法
```

第一步是把需求里的判断拆出来。比如“按部门导出账单”至少包含权限、范围、数据状态、异常、审计和性能几类判断。

第二步是把判断写成能回答的问题：无权限用户能否导出；父部门是否包含子部门；普通导出是否排除作废订单；成功导出是否写审计日志。

第三步是把问题挂到证据锚点：PRD、法规、旧系统行为、接口约定、用户确认或领域规则。没有锚点的“规格”只是猜测。

第四步才是可执行化：测试用例、属性测试、接口契约、前置/后置条件、不变量、模型检查或运行时断言。强度可以不同，但核心标准一样：它必须能让系统行为被检查。

## Verification and Validation

Verification 和 validation 是两道不同的门。

```text
真实世界 / 用户目的
        |
        | validate
        v
规格 / 需求 / 验收标准
        |
        | verify
        v
实现 / 代码 / 系统行为
```

Verification 问：实现是不是按规格做对了。

Validation 问：规格是不是把真实需求说对了。

所以测试通过通常只说明实现被 verified against tests。它不自动说明这些测试就是用户真正需要的东西。测试本身可能写错、漏掉边界、误解业务，或者只覆盖了“没有报错”而没有覆盖“语义正确”。

可执行规格直接服务 verification，因为它让实现有可检查标准；同时它也反过来帮助 validation，因为一旦把需求写成可执行判断，隐藏歧义会暴露出来：什么叫作废、谁有权限、例外场景是什么、失败时应返回空文件还是错误。

## Example: scikit-learn Object-Dtype Labels

scikit-learn issue #15534 报告了一个聚类指标输入校验回归：

```python
from sklearn.metrics.cluster import mutual_info_score
import numpy as np

x = np.random.choice(['a', 'b'], size=20).astype(object)
mutual_info_score(x, x)
```

这个调用抛出 `ValueError: could not convert string to float: 'b'`，但普通字符串数组可以工作；用户指出旧版本本来能工作。

这条 bug report 里的可执行规格不是“不要报错”这么粗，而是：聚类指标中的标签是类别，不是浮点特征；object dtype 的非数字字符串标签应当被当作合法标签处理。

一个可执行测试可以写成：

```python
def test_object_dtype_string_labels_match_string_labels():
    labels_object = np.array(["a", "b", "a", "b"], dtype=object)
    labels_string = np.array(["a", "b", "a", "b"])

    assert mutual_info_score(labels_object, labels_object) == \
           mutual_info_score(labels_string, labels_string)
```

SpecRover 论文把这个例子用作 code intent extraction 的动机：它从 issue、代码和测试上下文中推断 `check_array` 的局部 intended behavior，即该函数在当前问题语境下不应把包含非数字字符串的 object dtype 数组强行转成 float。

真实 scikit-learn PR #15535 采用了更局部的修法：在 clustering metrics 的 `check_clusterings` 调用 `check_array` 时传入 `dtype=None`，让标签校验保留类别语义，而不是把标签误当数值特征。这个差异说明，可执行规格还会帮助工程师判断责任层级：修在调用点，还是修在通用工具函数。

## Specification Inference and Drift

[[wiki/sources/Skills for the Future Software Profession Paper Source Guide]] 把可执行规格放进 agentic software engineering 的主流程：当 agent 能从文档、issue、代码和测试中推断规格时，人类的稀缺能力不再只是“把规格写出来”，而是判断推断结果是否忠实于用户意图、是否足够完整，以及 assurance level 是否匹配风险。

这会产生两类独立校验：一类检查实现是否满足规格，另一类检查推断规格是否仍与实现和真实意图一致。代码、测试和规格会各自演化，因此开发环境需要持续暴露三者之间的 drift 与冲突，而不是把任一方默认当作唯一真相。

## When to Use

可执行规格适合所有“生成容易、验收困难”的地方：AI coding、需求评审、接口设计、权限、账务、数据导出、合规、安全、长期维护和多团队协作。

它不要求一步到形式化验证。常见强度从轻到重包括：

1. 验收清单与示例输入输出。
2. 单元测试、集成测试、属性测试。
3. 接口契约、状态机、不变量。
4. 形式规格、模型检查、定理证明。

选择原则是：用能暴露关键歧义、足以支撑当前风险的最小规格强度。

## Common Failure Modes

- 只验证“没有报错”，没有验证语义是否正确。
- 把测试当成真实需求本身，忘记测试也需要 validation。
- 把规格写在错误层级，导致局部需求污染通用函数或通用规则压坏特殊场景。
- 规格粒度过大，AI agent 只能生成一坨代码，无法从失败中定位错因。
- 规格粒度过细，把产品取舍、审美、架构一致性等整体判断误压成机械清单。^[inferred]

## Related

- [[wiki/topics/Spec-Driven Development]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/concepts/Evidence Question Decomposition]]
- [[wiki/topics/Testing Strategy]]
- [[wiki/concepts/Verification Gap]]
- [[wiki/concepts/Cognitive Debt]]
- [[wiki/sources/Skills for the Future Software Profession Paper Source Guide]]
- [[wiki/syntheses/Agentic Engineering × Verification Loop]]
