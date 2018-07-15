+++
author = "zenk"
slug = ""
tags = ["编程","设计"]
draft = true
categories=["cs"]
title="常用面向对象设计原则"
description="常用的面向对象设计原则，SOILD"
date="2018-07-04T22:28:20+08:00"
+++

## 设计

目的TODO

坏味道

## 单一职责原则

又名SRP(Single Responsibility Principle)。针对一个函数、类、组件、架构的修改有且只有一个理由，而理由的来自于使用者。这样的好处是把拥有相同修改理由的函数、类、组件组织在一起，不同的分开，达到修改的时候不会影响其他代码，增强了可维护性。

这是一个定义简单，实操不容易正确的原则。原因在于：

1. **职责**无法度量
2. 因为团队、项目背景等待原因，在具体实现的细节中很难做到SRP

因此，在设计的时候接口一定做到SRP，实现尽量SRP。

**注：**

组件层面的SRP，叫做Component common closure，架构层面的SRP叫做axis of change responsibility for creation of architecture boundary。

## 开闭原则

TODO

## 里氏替换原则

TODO

## 结论

原则用到的工具抽象TODO，抽象变化

各个原则之间的关系，理由，总结TODO