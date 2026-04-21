---
title: Cynefin Framework source note
type: source
status: archived
updated: 2026-04-21
aliases:
  - Cynefin Framework
---

# Cynefin Framework source note

沉淀后的概念页：[[wiki/concepts/Cynefin Framework]]

## 原始摘录

# Cynefin Framework
- Obvious（simple）-"The Domain of Best Practice"
    - 特点
        - 每个人都很清楚原因和结果的关系。
        - 存在唯一正确的答案。
        - 需要基于实时的方法。
        - 问题容易理解，解决方法也很明显。
        - 可以应用简单的解决问题方法。
        - 需要很少的专家或者不需要专家就能解决。
    - 解决方法（sense-category-response）重点是归类到已知有最佳实践的问题。
        - 和大家同步问题。
        - 感知事实情况并收集数据。
        - 把问题归类到已知的问题分类。
        - 使用众所周知的方案或者已知的最佳实践解决问题。
    - 例子
        - 告警手册
- Complicated-"The Domain of Experts"
    - 特点
        - 有多潜在个答案。
        - 清楚知道哪些不知道。
        - 你明白需要回答什么问题。
        - 不知道怎么获得答案。
        - 问题倾向与可以预测，而不是不可以预测。
        - 原因和结果的关系不能立马知道，需要时间。
    - 解决方法（Sense – Analyze – Respond）重点是分析问题，变成obvious
        - 评估现场感知问题。
        - 调查多种选项。
        - 根据需要分析更多数据，更多其他的类似场景。
        - 使用专家知识。
        - 使用指标来控制。（监控、日志）
        - 通过上面的各种方法把问题简单，然后基于最佳实践指定执行计划（计划、执行、核实、调整）
    - 例子
        - 设计一个分布式系统。
- Complex Contexts – "The Domain of Emergence"
    - 特点
        - 不知道哪里不知道。
        - 需要实验去发现突破口。
        - 相比起来不可预测性大于可以预测性。
        - 只有通过探索问题才会明朗。
        - 需要创新的想法。
        - 无法使用常规的方法。
        - 需要更多的更高维度的思考与沟通。
    - 解决方法（Probe – Sense – Respond）重点是理解问题，需要创新想法，变成complicated
        - 通过探索理解问题。
        - 开发理论和实验收集更多的数据。
        - 通过实验发现问题模式，获取更多知识，努力把问题变成complicated或者obvious。
    - 例子
        - 排查线上故障。
- Chaotic Contexts – "The Domain of Rapid Response"
    - 特点
        - 最高的优先级是止损。
        - 最好的方案是响应时间最短的。
        - 先止损然后把问题变成其他领域的问题。
        - 没有人确定的知道具体解决方案。
        - 寻找知道可行的方案而不是正确的方案。
        - 没时间思考，需要执行很多决定让系统恢复到有序状态。
    - 解决方法（Act – Sense – Respond）
        - 需要有人马上决策和行动。
        - 寻找让系统回到有序的状态下的所有行动并执行让系统回到有序状态。
        - 避免让系统更加无序的行为。
        - 然后评估问题，把问题转移到其他领域的问题。
    - 例子
        - 线上问题回滚版本。
- Disorder
    - 特点
        - 问题和条件都无法归类到上面的四个领域。
        - 依赖个人喜好解决问题。
        - 没有时间纠正去纠正问题。
        - 执行一个糟糕的过程。
    - 解决方法
        - 收集更多的信息。
        - 定义好已知和未知。
        - 把问题分解成多个子任务，并把这些任务归类到上述的四个领域。
        - 专注与活动而不是人。
    - 例子
        - 线上出问题一刻，你是disorder，分析以后会认为问题是chaotic的。
- 参考链接
    -  [https://txm.com/making-sense-problems-cynefin-framework/]("https://txm.com/making-sense-problems-cynefin-framework/")
    -  [https://thecynefin.co/cynefin-st-davids-2022-1-of-2/]("https://thecynefin.co/cynefin-st-davids-2022-1-of-2/")
    -  [https://thecynefin.co/cynefin-st-davids-2022-2-of-2/]("https://thecynefin.co/cynefin-st-davids-2022-2-of-2/")
    -  [https://cynefin.io/wiki/Cynefin]("https://cynefin.io/wiki/Cynefin")