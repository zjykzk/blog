---
title: Loop Engineering
category: concepts
tags:
  - agents
  - harness
  - feedback
  - workflow
aliases:
  - loopcraft
  - 循环工程
relationships:
  - target: "[[wiki/topics/AI Harness]]"
    type: uses
  - target: "[[wiki/concepts/Verification Loop]]"
    type: uses
  - target: "[[wiki/concepts/Event-Driven Agent Loop]]"
    type: uses
  - target: "[[wiki/concepts/Continual Learning for AI Agents]]"
    type: related_to
sources:
  - https://www.langchain.com/blog/the-art-of-loop-engineering
  - https://cdn.openai.com/pdf/8a9f00cf-d379-4e20-b06f-dd7ba5196a11/OAI_WhitePaper_Codex-maxxing26.pdf
summary: Loop Engineering stacks execution, verification, event-triggering, trace-driven improvement, memory, review, and artifact loops around an agent so value compounds beyond one model call.
provenance:
  extracted: 0.78
  inferred: 0.22
  ambiguous: 0.0
base_confidence: 0.62
lifecycle: draft
lifecycle_changed: 2026-07-04
tier: supporting
created: 2026-07-04T23:00:06+0800
updated: 2026-07-07T21:07:28+08:00
---

# Loop Engineering

Loop Engineering 是把 agent 从“模型调用工具的一次性执行”推进成多层反馈系统的工程方法。LangChain 文章把它也称为 loopcraft：通过叠加基础执行、质量验证、事件触发和长期优化循环，让 agent 能自动完成工作、被外部标准校验、嵌入业务环境，并从运行轨迹中持续改进。

## Four Stacked Loops

1. **Agent loop**：模型拿到上下文后调用工具，直到任务完成。文档 agent 示例中，它会克隆仓库、读写文档、提交 PR。
2. **[[wiki/concepts/Verification Loop]]**：在 agent 输出后加入 grader，用 rubric、测试、CI 或 LLM-as-judge 检查结果；失败时把反馈送回 agent 重试。
3. **[[wiki/concepts/Event-Driven Agent Loop]]**：用 webhook、cron、schedule 或 Slack channel 等事件触发 agent，让它成为业务生态里持续运行的组件，而不是人工手动调用的一次性工具。
4. **Hill climbing loop**：用 trace analysis agent 审查历史运行轨迹，发现共性问题后反向修改 prompt、tool、grader、memory、skill，甚至在 open-weight 场景中把 traces/evals 变成 RL fine-tuning 信号。

[[wiki/sources/Codex Maxxing for Long Running Work Source Guide]] 给这组循环补了一个产品化样例：长期线程承载上下文，memory vault 记录滚动状态，thread automation 周期性唤醒同一工作流，strong goal 提供完成判据，side panel 让 artifact 成为下一轮上下文。这里的 loop 不只是 agent 内部执行循环，而是“工作有地方住、能被人审查、能在变化后回来继续”的 operating loop。^[inferred]

这四层不是并列功能清单，而是由内向外扩张的控制系统：内层负责把事做完，外层负责让做完的事更可靠、更自动、更会学习。^[inferred]

## Why It Matters

文章的关键判断是：agent 的生产力潜力不只在模型本身，而在围绕模型建出的循环。单个 agent loop 能自动化执行，但仍可能一次性出错；验证循环把错误变成可反馈信号；事件驱动循环把 agent 接入真实系统；hill climbing loop 则把历史运行数据转成未来系统改进。

这与 [[wiki/topics/AI Harness]] 的核心判断一致：生产级 agent 的行为经常由 harness 的上下文、工具、权限、触发器、检查、trace 和恢复机制共同决定，而不只是由模型权重决定。^[inferred]

## Human Judgment Positions

Loop Engineering 不等于把人排除出系统。文章把人放在几个判断杠杆位：

- agent loop 中，高风险 tool call 需要人工审批；
- verification loop 中，主观或敏感工作流可以由人充当 grader；
- application loop 中，最终输出进入用户或业务系统前可以由人批准；
- hill climbing loop 中，自动提出的 harness 改进需要经过人工 review 后再发布。

这说明“human in the loop”的重点不是让人卡在每一步操作上，而是让人守住价值判断、风险边界和系统演化方向。^[inferred]

## Open Questions

- 哪些 agent 工作只需要前两层循环，哪些必须进入事件驱动和 hill climbing？^[inferred]
- 当 hill climbing loop 自动修改 prompt、tools 或 grader 时，什么证据门槛足以允许变更进入生产 harness？^[inferred]
- 事件驱动 agent 长期运行后，如何避免自动化把错误快速规模化？^[inferred]

## Related

- [[wiki/sources/The Art of Loop Engineering Source Guide]]
- [[wiki/sources/Codex Maxxing for Long Running Work Source Guide]]
- [[wiki/topics/AI Harness]]
- [[wiki/concepts/Agentic Engineering]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/concepts/Event-Driven Agent Loop]]
- [[wiki/concepts/Harness Ratchet]]
- [[wiki/concepts/Feedback Flywheel]]
- [[wiki/concepts/Continual Learning for AI Agents]]
- [[wiki/concepts/Meta-Harness]]
- [[wiki/concepts/Agent Loop Human Judgment Positions]]
