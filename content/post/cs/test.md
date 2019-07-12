+++
author = "zenk"
slug = ""
tags = ["test"]
draft = true
categories=["cs"]
title="测试相关"
description="测试相关一些注意点。"
date="2019-06-05T18:01:33+08:00"

+++

### 单元测试

#### 为什么需要

确保软件没有我难题，提升上线的自信。

#### 一些注意点

1. 小步重构，目标是行为（behavior）不变，修改实现。
2. 单元测试，是正确重构的保障。
3. **尽量测试行为（behavior），不是测试实现**，这个很重要，不然实现改了测试也要跟着改，但是也无法完全避免针对实现的代码进行测试。
4. 新的需求来了，才需要写测试。
5. 测试单元的粒度是模块，不是类。
6. 需要测试的是模块的稳定API。
7. 测试覆盖的是用户用例（用户故事）。
8. 不要使用[ATDD](https://www.ca.com/en/blog-agile-requirements-designer/guide-to-test-driven-development-tdd-vs-bdd-vs-atdd.html)，使用TDD，并和产品代码使用同样的编程语言。
9. 使用“Given When Then”模式，给定上下文，设置输入，判定输出。
10. 测试之间应该互相独立，测试之后要删除fake数据。
11. mock地方应该是模块的边界，比如说mock数据库。
12. 让测试跑的更快。

#### TDD小结