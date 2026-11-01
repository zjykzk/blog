---
title: Tacit Knowledge
type: concept
status: draft
category: concepts
summary: 默会知识是人能在实践中识别、判断或行动，却无法在当前条件下一次性完整表达和转移的知识；它依赖情境、身体、模式与共同体。
tags: [knowledge, cognition, learning, practice, judgment]
sources:
  - wiki/sources/默会知识 AI 永远都不可能替代的技能 Source Guide.md
  - inline:software-engineering-learning-imperative-2026-11-01
relationships:
  - target: "[[wiki/concepts/Knowledge Types]]"
    type: extends
  - target: "[[wiki/topics/Learning Methodology]]"
    type: related_to
  - target: "[[wiki/concepts/Software Engineering as Knowledge Discovery]]"
    type: related_to
aliases:
  - 默会知识
  - 隐性知识
  - 不可言说知识
  - Tacit Knowing
provenance:
  extracted: 0.66
  inferred: 0.28
  ambiguous: 0.06
base_confidence: 0.55
lifecycle: draft
lifecycle_changed: 2026-11-01
tier: supporting
created: 2026-11-01T22:57:50+0800
updated: 2026-11-01T22:57:50+0800
---

# Tacit Knowledge

默会知识是人能在实践中识别、判断或行动，却无法在当前表达、记录和训练条件下一次性完整说清或转移的知识。

## What It Is

默会知识常表现为：

- 能认出一个模式，却难以列出完整判别规则；
- 能把握火候、时机和分寸，却难以给出与情境无关的固定步骤；
- 能在异常中调整行动，却无法预先穷举所有例外；
- 团队能靠共同经历协调，却难以把全部默契写进制度；
- 身体能完成精细动作，而注意力无法同时描述所有控制细节。

Michael Polanyi 的经典表达是 “We can know more than we can tell”。该句及其理论脉络由现有中文来源转述，本页尚未回读原始著作校验上下文。^[ambiguous]

## Tacit Is Not the Same as Secret or Mystical

默会不等于故意隐藏，也不等于原则上永远无法学习：

- 有些知识只是尚未找到合适的表示；
- 有些知识可通过示范、模仿、实例和反馈传递；
- 有些判断可逐步外化为规则、检查表、规格或模型；
- 有些模式虽难以语言化，却可以被统计模型从数据中训练出来。

因此，更稳的边界是：默会知识无法被**当前媒介一次性完整转录**。显性化和训练可以移动边界，但不会自动保证语境、责任和价值判断也被保留。^[inferred]

## Four Sources of Tacitness

### Complex pattern recognition

专家通常整合大量弱线索，而不是逐条执行显性规则。把所有线索拉到意识前台，可能既不现实，也会干扰动作。

### Context dependence

同一句规则在不同目标、风险、关系与历史条件下可能要求不同处理。真正的能力包含何时适用、何时例外和何时升级。

### Embodiment

火候、平衡、语气、节奏和手感依赖身体与环境的连续耦合。语言只能抽取其中部分维度。

### Collective practice

团队默契存在于互动关系中。它由共同经历、角色、信任和反馈维持，不只存放在某个成员脑内。

## How Tacit Knowledge Is Learned

默会知识通常通过参与式学习获得：

1. 进入真实或高保真情境；
2. 观察熟练者如何感知线索和处理例外；
3. 尝试行动并暴露误差；
4. 获得高分辨率、及时反馈；
5. 重复练习，直到模式与动作被内化；
6. 在不同情境中迁移，识别适用边界。

这与 [[wiki/topics/Learning Methodology]] 的应用、输出、反馈和活人互动相连。文档仍然重要，但它更像进入实践的脚手架，而不是实践知识的完整替代品。^[inferred]

## Role in Software Engineering

软件工程中的默会知识包括领域专家的例外判断、架构师对耦合风险的感觉、维护者对遗留行为的历史理解，以及团队对“什么程度算安全”的共同尺度。

[[wiki/concepts/Software Engineering as Knowledge Discovery]] 通过共同建模、具体实例、原型、测试、评审和生产反馈，让这些判断逐步变成可讨论、可反驳、可复用的工件。外化不会一次完成，也不应假装所有判断都能降为机械规则。^[inferred]

## AI Boundary

AI 可以吸收文本未显式描述的统计模式，所以“说不出来”不能证明“训练不出来”。现有来源据此区分：

- 可记录、可模拟、可重复反馈的外圈更容易进入模型或工具；
- 动态共同体、具身环境、价值冲突和责任承担混合而成的判断更难完整离线复制。

这个边界是工作假设，而不是已证明的永久能力边界。^[ambiguous]

## Open Questions

- 如何区分真正依赖现场的知识与只是文档质量不足的知识？
- 团队应把哪些反复判断固化成自动检查，哪些保留给评审和责任主体？
- AI 进入实践现场后，会削弱人的内居过程，还是通过更密集反馈加速它？

## Related

- [[wiki/sources/默会知识 AI 永远都不可能替代的技能 Source Guide]]
- [[wiki/sources/软件工程为何必须成为学习专家 Source Guide]]
- [[wiki/concepts/Knowledge Types]]
- [[wiki/topics/Learning Methodology]]
- [[wiki/concepts/Software Engineering as Knowledge Discovery]]
- [[wiki/concepts/Encoding Team Standards]]
- [[wiki/concepts/Specific Knowledge]]
