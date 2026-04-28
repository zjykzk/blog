---
title: Requirement to Architecture Mapping
type: topic
status: growing
source_count: 3
updated: 2026-04-20
aliases:
  - req_map_to_arch
  - 用户故事到架构映射
tags:
  - architecture
  - requirements
  - mapping
---

# Requirement to Architecture Mapping

这个主题页沉淀的是：如何把用户故事、PRD、free-form requirement 先归一化，再稳定映射到分层架构。

## Normalized input

在做架构映射前，先把输入统一为：

- feature
- use_case
- entry
- input / output
- business_rules
- domain_objects
- data_access
- external_calls
- errors
- shared_utils
- assumptions

如果输入不完整，保守推断，并明确标出 assumptions。

## Layer mapping heuristics

- 协议入口、handler、DTO、协议错误码 → `api/`
- 业务判断、校验、状态流转、领域对象、业务错误 → `service/`
- service 需要的外部能力接口定义 → `service/` 中的 repo / capability interface
- MySQL / Redis / RPC / HTTP / MQ / SDK 的技术实现 → `infra/`
- 无业务语义的纯技术 helper → `pkg/`

## Fast judgment questions

拿到一句需求后，依次问：

1. 它是在描述怎么接请求吗？→ `api/`
2. 它是在描述业务如何判断或流转吗？→ `service/`
3. 它是在描述系统需要什么外部能力吗？→ `service/` 定义接口
4. 它是在描述能力如何落地实现吗？→ `infra/`
5. 它只是纯技术工具吗？→ `pkg/`

## Common mistakes

- 把库存校验规则放到 `infra/`
- 把 RPC client 放到 `pkg/`
- 在 `infra/` 定义 repo interface
- 让 handler 直接依赖 MySQL repo

## Navigation

- [[wiki/maps/AI Map]]
- [[wiki/topics/Karpathy Guidelines]]
- `content/posts/cs/arch/arch.md`

## Source notes

- `pages/项目___AI___req_map_to_arch.md`
- `journals/2026_04_01.md`
- `pages/项目___AI.md`
