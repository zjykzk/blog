---
title: Software Design Map
type: map
status: seed
category: maps
summary: 这页把软件设计中的核心概念按层次放在一张图里。关键区分是：
sources:
  - mobu/读书/架构师启示录-知识模型、落地方法与思维模式.md
  - mobu/读书/架构师启示录-知识模型、落地方法与思维模式_第8章及以后章节.md
created: 2026-05-03
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-05-05
updated: 2026-05-15T20:50:29+08:00
aliases:
  - 软件设计地图
  - 软件设计核心概念地图
  - Software Design Core Concepts
tags:
  - software-design
  - architecture
  - map
---

# Software Design Map

这页把软件设计中的核心概念按层次放在一张图里。关键区分是：

- `基础设计原则`：指导局部设计判断的原则，例如 SOLID、KISS、DRY。
- `设计方法论`：组织一整套设计活动的方法，例如 DDD、Clean Architecture、Hexagonal Architecture。
- `架构风格与模式`：系统级组织方式，例如分层架构、事件驱动、CQRS、微服务。

## Concept Map

```mermaid
mindmap
  root((软件设计核心概念地图))
    底层原理
      复杂度管理
        分解
        抽象
        封装
        模块化
        信息隐藏
      变化管理
        高内聚
        低耦合
        稳定依赖
        依赖倒置
        接口隔离
      模型管理
        领域模型
        统一语言
        概念完整性
        业务规则
        不变量
        语义边界
      运行时本质
        状态
        数据流
        控制流
        并发
        一致性
        失败模式
      约束权衡
        时间
        空间
        成本
        可靠性
        可维护性
        可演化性

    基础设计原则
      SOLID
        单一职责
        开闭原则
        里氏替换
        接口隔离
        依赖倒置
      GRASP
        信息专家
        控制器
        低耦合
        高内聚
        多态
      KISS
        简单优先
        避免过度设计
      YAGNI
        不为假设需求设计
      DRY
        消除知识重复
        避免机械抽象
      关注点分离
        UI不承载业务规则
        Controller不直接写复杂查询
        领域逻辑不依赖框架
        基础设施细节不泄漏

    设计方法论
      DDD
        ModelDrivenDesign
        以领域为中心
        统一语言
        边界上下文
        Entity
        ValueObject
        Aggregate
        DomainService
        DomainEvent
        Repository
        AntiCorruptionLayer
      CleanArchitecture
        Entities
        UseCases
        InterfaceAdapters
        FrameworksDrivers
        依赖指向内层
      HexagonalArchitecture
        Port
        Adapter
        外部系统可替换
        业务核心不依赖外设
      结构化设计
        自顶向下分解
        模块职责划分
        数据流分析
      面向对象设计
        类与对象
        对象协作
        封装状态
        多态替代条件分支
      函数式设计
        纯函数
        不可变数据
        显式副作用
        函数组合

    架构层次
      表现层
        UI
        API
        Controller
        输入校验
      应用层
        UseCase
        Command
        Query
        工作流编排
        事务边界
      领域层
        业务概念
        业务规则
        不变量
        领域服务
      基础设施层
        Database
        MessageQueue
        Cache
        FileStorage
        ThirdPartyAPI

    架构风格与模式
      分层架构
        表现层
        应用层
        领域层
        基础设施层
      模块化单体
        清晰边界
        单进程部署
        低运维复杂度
      事件驱动
        Event
        Publisher
        Subscriber
        最终一致性
      CQRS
        CommandModel
        QueryModel
        读写分离
      微服务
        服务自治
        独立部署
        分布式事务
        服务发现
      插件化架构
        扩展点
        插件生命周期
        能力隔离

    最佳实践
      需求建模
        找核心业务目标
        识别用户任务
        明确成功指标
        区分规则和流程
      边界设计
        按业务能力拆分
        明确模块职责
        明确输入输出
        明确所有权
      API设计
        资源建模
        命令查询分离
        幂等性
        版本管理
        错误语义
      数据设计
        事务边界
        一致性模型
        读写模型
        索引策略
        迁移策略
      错误处理
        显式错误
        可恢复错误
        不可恢复错误
        重试
        超时
        熔断
      测试策略
        单元测试
        集成测试
        契约测试
        端到端测试
        回归测试
      可观测性
        日志
        指标
        链路追踪
        告警
        审计
      安全
        认证
        授权
        输入净化
        密钥管理
        最小权限

    质量属性
      可维护性
        清晰命名
        小函数
        小模块
        明确边界
      可测试性
        依赖注入
        纯函数
        Mock边界
        可控副作用
      性能
        缓存
        批处理
        异步化
        查询优化
      可靠性
        超时
        重试
        降级
        限流
        容灾
      可扩展性
        水平扩展
        无状态服务
        分区
        队列削峰
      可演化性
        低耦合
        契约稳定
        渐进迁移
        兼容性

    反模式
      大泥球
        边界缺失
        到处依赖
        难以测试
      贫血领域模型
        业务规则散落
        Entity只有数据
      上帝对象
        职责过多
        修改风险高
      过度抽象
        为未来幻想设计
        间接层过多
      工具类垃圾桶
        utils
        helpers
        common
        misc
      框架绑架
        业务逻辑依赖框架
        难以替换基础设施
      早期微服务化
        分布式复杂度提前出现
        运维成本过高

    决策方法
      从业务开始
        目标
        约束
        变化方向
        风险
      从边界入手
        谁拥有数据
        谁维护规则
        谁承诺接口
      从失败倒推
        会怎样失败
        谁能恢复
        如何观测
      从成本权衡
        开发成本
        运行成本
        迁移成本
        认知成本
      从演化设计
        先简单
        留边界
        可替换
        可迁移
```

## Notes

DDD 更适合归入 `设计方法论`，不是单个设计原则。它包含一组围绕领域、语言和边界展开的设计原则与建模实践。

这张图可以和 `[[wiki/concepts/Software Design Three Generators]]` 配合阅读：这里是展开地图，后者是把软件设计压缩成 `划线、接线、流转` 三个生成器。

## 架构师启示录补充

《架构师启示录》给这张软件设计地图补了一个从架构到实现的纵深：实现层不仅要讨论设计原则，还要检查分离性、复用性、防御性和一致性。

- 分离性：业务与技术、核心与非核心、变化与不变、不同非功能性需求、读写等操作类型、生产者/消费者等角色、权限/日志/事务/监控等切面、本质属性与偶然属性。
- 复用性：技术复用从函数、库、框架发展到体系；业务复用要处理“不变”和“创新变化”的张力。
- 防御性：身份认证、契约、最小知识、仲裁、重试、限流、熔断、超时和资源处理。
- 一致性：代码要与应用架构、数据架构、技术架构保持一致，并通过统一模型、统一概念和及时反馈降低信息失真。

这些内容连接到 [[wiki/concepts/架构一致性]] 和 [[wiki/concepts/重构层次]]：设计不是到图纸为止，而要在代码、运行和维护中持续校验。

## Related

- [[wiki/concepts/Software Design Three Generators]]
- [[wiki/concepts/Conceptual Integrity]]
- [[wiki/concepts/Domain-Driven Design]]
- [[wiki/topics/Modern Software Engineering]]
- [[wiki/topics/Software Methodology]]
- [[wiki/topics/面向对象分析与设计]]
- [[wiki/topics/UML Diagrams in Software Development]]
- [[wiki/maps/CS Map]]
- [[wiki/syntheses/软件设计作为系统诊断]]
- [[wiki/sources/设计模式 设计原则与系统思维 Source Guide]]


## Source layer

- [[wiki/sources/Use Case 开发管理 Source Guide]] — 说明 Use Case 如何作为行为契约衔接 UI、API、应用服务、领域模型、持久化、测试和任务拆分。
- [[wiki/sources/架构文档与图示之道 Source Guide]] — 保存一份关于架构文档、C4/UML 图示、ADR 与 Docs as Code 的中文课程材料。
- [[wiki/sources/设计模式 设计原则与系统思维 Source Guide]] — 保留一段把设计原则、设计模式、Iceberg Model、信息流和状态流转贯通起来的中文教学对话。
