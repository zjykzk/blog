+++
author = "zenk"
slug = ""
tags = ["design-pattern"]
draft = true
categories=["cs"]
title="设计模式拾遗"
description="设计模式比较/提要。"
date="2018-09-01T15:47:56+08:00"
+++

## TEMPLATE MTEHOD模式和STRATEGY模式

<style>table{border-collapse:collapse;}table,td,th{border:1px solid #000}td{text-align:center}</style>
两个模式都用于分离通用算法和具体实现细节。当时实现的方式不一样，TEMPLATE METHOD模式通过继承，而STRAGTEGY模式使用组合或者委托。因此，两者的比较变成了继承和委托的比较。

| 模式            | 耦合度             | 灵活性                             | 复杂度                       |
| --------------- | ------------------ | ---------------------------------- | ---------------------------- |
| TEMPLATE MTEHOD | 高，和父类高度耦合 | 低，子类无法复用                   | 低                           |
| STRATEGY        | 低，依赖于接口     | 高，具体的实现可以被不同的算法复用 | 高，多了接口，字段，间接调用 |

