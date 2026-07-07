---
title: Codex-maxxing for Long-running Work Source Guide
category: sources
tags: [agents, harness, workflow, memory, ai-coding]
sources:
  - https://cdn.openai.com/pdf/8a9f00cf-d379-4e20-b06f-dd7ba5196a11/OAI_WhitePaper_Codex-maxxing26.pdf
created: 2026-07-07T21:07:28+08:00
updated: 2026-07-07T21:07:28+08:00
summary: OpenAI 白皮书把 Codex 从一次性 prompt 工具转成可持续推进、可审查、可恢复、可唤醒的工作循环。
provenance:
  extracted: 0.78
  inferred: 0.20
  ambiguous: 0.02
base_confidence: 0.62
lifecycle: draft
lifecycle_changed: 2026-07-07
---

# Codex-maxxing for Long-running Work Source Guide

> Source: OpenAI, “Codex-maxxing for long-running work: How Codex helps work continue beyond a single prompt”, PDF white paper, 2026.

## What It Covers

这份白皮书把 Codex 描述为一个让工作“开始、继续、变成真实产出”的地方，而不只是一个回答单次 prompt 的编码助手。它围绕 Jason Liu 的日常工作流展开，说明长期线程、语音输入、运行中 steering、memory vault、browser/computer/connectors/skills、remote control、thread automations、strong goals 和 side panel 如何合成一个持续工作循环。

白皮书的核心不是单个功能，而是工作形态变化：一次性对话被改造成一个有状态、有工具、有审查边界、有周期性唤醒、有产物回路的 agent operating loop。^[inferred]

## Core Claim

Codex-maxxing 的主命题是：长时间工作需要一个可持续推进、可审查、可恢复、可自动唤醒的责任循环，而不是更长的一次性 prompt。^[inferred]

白皮书原文的中心句是：Codex is becoming a place where work can start, keep going, and become real output. 这句话把 Codex 从“生成回答的界面”重新定位为“工作有地方住”的运行环境。

## Key Points

- Durable threads 给重要 workstream 一个长期住处。长期线程积累 context、preferences、old decisions 和 open loops，适合 social feedback monitoring、open source、OpenAI CLI、Agents SDK 和 chief-of-staff 这类会反复回来的工作。
- 长期线程保留历史会带来成本权衡：它可能比 fresh short thread 更贵，但对重要工作流来说，continuity 值得支付。
- Voice input 的价值不只是输入更快，而是把半记得、半确定、未经整理的真实思考放进 Codex。白皮书用“有个叫 Ben 的人在 Slack 提过，但我不记得具体内容，你去找找”说明语音能捕捉打字时常被删掉的 messy context。
- Steering 让用户在 Codex 已经工作时继续纠偏、补充上下文、批准下一步或排队后续动作。例子包括缩小界面、修正文案、调整 spacing、完成后开 PR、等待 preview deployment、先展示 preview link。
- Memory acts as a notebook to provide context for actions. 白皮书明确区分：repositories hold code，the vault holds rolling context around the work。
- Memory 不应只藏在 conversation history 中。可用的长期记忆应该能 open、edit、diff、review、reuse；当 vault 放在 GitHub 里，diff 会成为 memory review surface。
- Memory instruction 的粒度包括：提到人时更新 people notes，项目推进时更新 project page，loop close 时标记 closed，做决定时写下 decision 和 why it matters。
- Computer and browser use 把 Codex 接到真实工作表面：local web previews、GUI-only desktop work、signed-in Chrome sessions、Slack/Gmail/Calendar/GitHub connectors，以及可复用 skills。
- 白皮书要求区分不同 surface：本地 app 迭代用 browser surface；依赖登录态或多个认证 tab 用 Chrome；只能通过桌面 app 完成时用 computer use，并设置清楚权限和 review。
- Skills 把成功过的重复 workflow 封装成 instructions、references 和 scripts，使 Codex 不必每次重新学习。
- Remote control 让人离开桌面后仍能在手机上检查、批准、重定向或要求另一个 pass。它不是跳过 review 的理由，而是降低人类关键审查的摩擦。
- Thread automations 是 attach 到当前 thread 的 heartbeat-style recurring wake-up calls。它们与普通 “Do this now” prompt 的差别在于：它们按 cadence 回到同一 conversation，保留上下文，而不是每次从零开始。
- Thread automation 可以检查 PR、Slack thread、inbox、deployment、document、customer support thread 或 long-running command，并可按条件停止或调整 cadence。
- 白皮书给出的 automation guardrail 很清楚：例如每 30 分钟检查 Slack/Gmail，研究上下文并起草回复，但未经批准不要发送。
- Loop 的力量来自 context、tools、memory、recurrence 和 review 的组合，而不是某一个孤立功能。
- Chief-of-staff loop 中，Codex 准备 open messages、relevant context、draft replies 和 questions that need judgment；用户决定 approval、tone、timing 和 final decision。
- Monitor-for-feedback loop 中，Codex 监控 Slack 动画反馈，更新 Remotion project，重新 render，并准备 review link；用户保留 creative judgment、final approval 和 publishing decision。
- Refund loop 中，Codex 检查客服是否加入，准备下一条回复、证据和下一步建议；用户保留 consent、approval 和 any irreversible action。
- Strong goal 不只是让 Codex 执行计划，而是给它 expected behavior、review criteria、constraints 或 clear definition of done。Rich-to-Rust 示例中，成功标准是 public API compatible，并通过 original unit tests。
- Side panel 不只是 preview surface，而是 artifact 进入 loop 的地方。Markdown、spreadsheets、CSVs、PDFs、slides、index.html、Storybook、Remotion Studio、Slidev、Streamlit 和 Jupyter 都可以成为可 inspect、comment、edit、review 的对象。
- Side panel 的关键句是：comments become instructions, the artifact becomes context. 产物不再只是结果，而是下一轮工作的输入。

## Derived Structure

这份白皮书可以压成一条工作系统链：^[inferred]

```text
messy context
  -> durable thread
  -> memory vault
  -> tools and surfaces
  -> steering and review
  -> thread automation
  -> strong goal
  -> artifact as context
  -> next loop
```

其中每个节点解决一个长期 agent 工作的结构问题：^[inferred]

- Thread 解决工作在哪里持续。
- Memory 解决上下文如何显式沉淀和被审查。
- Tools/surfaces 解决 Codex 能触达什么真实世界。
- Steering 解决人如何在执行中纠偏。
- Remote control 解决人如何低摩擦介入长任务。
- Automation 解决线程如何定期醒来。
- Goal 解决什么叫完成。
- Side panel 解决产物如何成为下一轮上下文。

## Responsibility Boundary

白皮书最稳定的工程含义是：Codex-maxxing 不是把人赶出循环，而是把人从重复操作位挪到判断杠杆位。^[inferred]

Codex 可以准备消息、上下文、草稿、render、证据、review link 和建议；人保留发送、发布、创意判断、同意、批准、不可逆动作和最终决策。这与 [[wiki/concepts/Agent Loop Human Judgment Positions]] 的判断一致：人不必卡在每个工具调用上，但必须守住价值定义、风险边界、硬门禁、人工入口和循环修正。^[inferred]

## Implications for Agent Harnesses

这份白皮书把 [[wiki/topics/AI Harness]] 的几个抽象面落成产品动作：^[inferred]

- durable thread 和 memory vault 是 state/context layer；
- browser、computer、Chrome、connectors 和 skills 是 action surface；
- steering、remote control 和 approval 是 human decision boundary；
- thread automation 是 event-driven loop；
- strong goals 和 original unit tests 是 verification surface；
- side panel 是 artifact-context bridge。

因此它和 [[wiki/concepts/Loop Engineering]] 的关系很直接：Codex-maxxing 是 loop engineering 的产品化样例。它把 agent execution、human steering、memory update、event wake-up、artifact review 和 verification criteria 接成一个可持续的工作闭环。^[inferred]

## Open Questions

- 长期 durable thread 如何避免 context pollution、过期 decision 和 memory drift？白皮书只指出 memory 要可 review，没有展开清理策略。
- Memory vault 写错、写重或写得太 vague 时，应该由什么 workflow 校验和回滚？
- Thread automation 误触发、漏触发或在错误上下文里唤醒时，如何诊断？
- Approval boundary 如何配置到足够安全但不把每个 loop 都阻塞成人工队列？
- Side panel comment 变成 instruction 后，如何避免评论噪音污染任务目标？
- Strong goal 如何从模糊需求中生成，而不是要求用户一开始就能写出优秀验收标准？

## Related

- [[wiki/topics/AI Harness]]
- [[wiki/concepts/Loop Engineering]]
- [[wiki/concepts/Event-Driven Agent Loop]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/concepts/Agent Loop Human Judgment Positions]]
- [[wiki/concepts/Agent Skill]]
- [[wiki/topics/Context Management]]
- [[wiki/topics/AI Memory]]
- [[wiki/sources/Agent Engineering Source Guide]]
- [[wiki/sources/The Art of Loop Engineering Source Guide]]
