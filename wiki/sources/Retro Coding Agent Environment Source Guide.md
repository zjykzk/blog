---
title: Retro Coding Agent Environment Source Guide
type: source
status: growing
category: sources
aliases:
  - retro skill
  - Agent 环境复盘
  - 编码会话防复发审计
tags: [agents, harness, ai-coding, feedback, workflow]
sources:
  - https://raw.githubusercontent.com/mattpocock/skills/refs/heads/main/skills/engineering/retro/SKILL.md
  - conversation:2026-10-28
created: 2026-10-28T14:40:23+08:00
updated: 2026-10-28T14:40:23+08:00
summary: Retro Skill 从编码会话证据中识别环境缺口，并把机械问题、判断问题、导航与信息访问分别路由到可靠且低上下文成本的防护层。
provenance:
  extracted: 0.68
  inferred: 0.32
  ambiguous: 0.00
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-10-28
tier: supporting
---

# Retro Coding Agent Environment Source Guide

> 来源：[Matt Pocock 的 retro/SKILL.md](https://raw.githubusercontent.com/mattpocock/skills/refs/heads/main/skills/engineering/retro/SKILL.md)，读取于 2026-10-28。本文保存该次阅读与 SFAM 拆解，不声称 upstream main 后续未变化。

## 核心定位

这份 Skill 名义上复盘 coding session，实际对象是 Agent 的工作环境：仓库导航、自动检查、编码规范、常驻指令、工具调用、无效规则和信息访问。它不评价当前 Agent 的个人表现，而是建议怎样改造环境，使未来会话更容易做对。

“Agent 环境防复发审计”可以更准确地概括它的功能：把一次会话暴露的摩擦和错误当成系统传感器，再把发现转成长期防护。^[inferred]

## 总目标 G

总目标是从真实会话证据中找出可复发的环境缺口，并将其转化为未来运行可以依赖的导航、检查、标准或信息基础设施。

这可以进一步拆成四个子目标：

1. 识别本次会话中的搜索成本、错误、漏检与信息缺口。
2. 判断哪些问题值得制度化，而不是只提醒 Agent 下次注意。
3. 为每类问题选择可靠且上下文成本较低的防护层。
4. 按严重程度向用户呈现改进候选。

## 阶段与关键结构 S/F

| 阶段 | 结构 | 输入 → 输出 | 功能 |
|---|---|---|---|
| 证据落地 | S1 写作规范预加载 | `writing-for-agents` → Agent 文档写作原则 | 防止复盘生成冗长、无效或不改变行为的规则 |
| 证据落地 | S2 Session 原始证据 | 指定会话或当前会话 → 可核验的摩擦与错误 | 避免凭印象发明通用最佳实践 |
| 缺口扫描 | S3 七类候选扫描 | 会话记录与仓库 → 环境改进候选 | 用稳定分类提高覆盖率，不只盯着代码错误 |
| 防护路由 | S4 既有检查发现 | 构建脚本、lint、test、CI → 已有防线及接线状态 | 避免重复造轮子，并发现“检查存在但未执行” |
| 防护路由 | S5 机械/判断问题分类 | 违规模式 → 可自动化或需判断 | 决定机器拦截还是 Reviewer 裁决 |
| 防护路由 | S6 上下文责任分配 | 实现与 Review 阶段的压力差 → 规则归属 | 把判断型规范放到上下文压力较低的 Review 阶段 |
| 防护路由 | S7 载体选择 | 改进内容 → check、标准、指针、文档或 Skill | 让知识进入真正能改变行为的位置 |
| 输出 | S8 严重度排序 | 全部候选 → 有序改进清单 | 让用户优先处理高影响风险 |

这里的阶段划分与结构命名来自 SFAM 整理；原文给出的是步骤、候选类别和载体说明，并未显式命名这四个阶段。^[inferred]

## 七类环境缺口

- **Navigation**：Agent 是否难以找到文件、依赖或关键事实；必要时增加导航指针。
- **Automated checks**：lint、类型检查、测试和 CI 是否能捕获已发生错误；已有命令但没有被 hook 或 CI 运行也是缺口。
- **Coding standards**：Reviewer 是否需要新的判断规则；固定语法、禁用 API、import 形态和文件位置等机械问题应优先进入确定性检查。
- **Global AGENTS.md**：常驻指令是否过大，能否转移到 Review 标准、自动检查或被引用文档。
- **Tool economy**：昂贵、低信息密度的工具调用是否可被更便宜的命令或定制工具替代。
- **No-ops**：steering 文件中的指令是否真正改变 Agent 行为。
- **Information access**：是否缺少服务器日志、只读第三方服务等关键证据入口。

这些类别同时覆盖错误率、探索成本、上下文成本和可观测性，因此方法的分析单位是“Agent 与工作环境组成的系统”，而不是裸模型。^[inferred]

## 防护层选择逻辑

这套方法最重要的不是列出问题，而是决定问题应被放到哪里：

```text
会话证据
  → 识别摩擦、错误或信息缺口
  → 检查问题是否可能复发
  → 判断问题性质
      ├─ 固定且可机器判定 → repo linter / pre-commit / CI
      ├─ 需要跨文件判断   → CODING_STANDARDS.md + Reviewer
      ├─ 关键信息难找     → AGENTS.md 导航指针 → 详细文档
      ├─ 按需执行的流程   → Skill
      └─ 证据无法取得     → 日志或只读信息接口
  → 按严重程度呈现
```

确定性检查优于文本规则，因为它能稳定执行并减少重复提醒。只有无法由 guardrail 替代的跨文件一致性、周边风格匹配等判断，才进入 `CODING_STANDARDS.md`。

## Implementation 与 Review 的职责

原文用上下文压力解释职责分配：实现 Agent 要探索、写代码并调试失败，承担最高的上下文压力；Review Agent 直接获得 diff，探索压力较低。因此，编码标准应主要由 Review Agent 施加，而不是持续挤占实现阶段的注意力。

这不是说实现阶段可以忽略正确性，而是把“产生反馈”与“把所有规则同时记在工作记忆中”分开：测试和静态检查仍可在实现时运行，真正需要综合判断的规范则延后到 Review。^[inferred]

## 指令载体的分工

- `AGENTS.md` / `CLAUDE.md`：每次会话都会进入上下文，只应保存极少量导航指针。
- `CODING_STANDARDS.md`：在 Review 阶段读取，保存无法机械化的判断标准。
- Docs：承载详细参考材料，由更短的入口文件指向。
- Skills：承载按需调用的文档或用户触发流程。
- Linter、hook、CI：承载固定、可重复判定的硬约束。

这套分工把防护可靠性和上下文成本放进同一个设计问题：越能自动执行的约束，越不应该依赖模型记忆。^[inferred]

## 强点

1. **证据优先**：从实际 Session 与仓库配置出发，不凭空列通用建议。
2. **系统改进**：把失败变成环境变更，而不是“下次小心”。
3. **自动化优先**：能确定判定的规则进入机器防线。
4. **上下文成本意识**：根据实现和 Review 的不同压力分配规范责任。
5. **把缺失视为发现**：没有任何 lint/test/CI guardrail 本身就是持续风险。

## 边界与缺口

- 它更像环境缺陷审计，而不是完整 Retrospective：没有系统保存做得好的实践、目标达成情况、估计偏差或团队协作经验。^[inferred]
- 原文要求按严重程度排序，但没有定义影响、复发概率、检测难度和实施成本等评分标准。
- 它没有明确要求区分表面症状和根因；一次昂贵工具调用可能来自导航、权限、文档或接口设计。
- 工作流在“提出候选改进”处结束，没有定义批准、实施、复测和回滚。
- 默认读取当前会话，但没有说明日志缺失或上下文压缩后的降级策略。
- “调用 Skill tool”等表述依赖特定宿主环境，迁移时需要改成平台无关的能力加载方式。

## 可复用审计清单

1. 从会话原始记录列出错误、返工、长时间搜索、重复读取、昂贵调用与缺失信息。
2. 为每项写出证据，并判断它是偶发事件还是可复发模式。
3. 追问根因属于导航、检查、规则、工具、信息访问还是职责分配。
4. 先读取仓库已有的 lint、check、test、hook 与 CI 配置。
5. 能机器判定的错误进入确定性 guardrail；判断型标准交给 Reviewer。
6. 把常驻上下文压到导航指针，将细节外置到标准、文档或 Skill。
7. 每条候选项记录影响、复发概率、修改落点、成本和验证方式。^[inferred]
8. 按严重度呈现，实施后用后续会话验证是否减少同类失败。^[inferred]

一个可补入原方法的优先级近似是：`影响 × 复发概率 × 当前不可检测程度 ÷ 实施成本`。这是方法增强建议，不是原文公式。^[inferred]

## Open Questions

- 哪些单次 Session 证据足以触发共享环境修改，哪些需要跨 Session 反复出现？
- 如何衡量一次环境改进实际减少了错误、Review 负担或 Token 成本？
- 建议自动化到什么程度后，会因维护成本或误报而得不偿失？

## Related

- [[wiki/concepts/Feedback Flywheel]]
- [[wiki/concepts/Coding Agent User Harness]]
- [[wiki/concepts/Encoding Team Standards]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/concepts/Agent Skill]]
- [[wiki/syntheses/Agent Skill × Harness Ratchet]]
- [[wiki/sources/Writing for Agents Source Guide]]
