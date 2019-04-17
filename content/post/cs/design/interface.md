+++
author = "zenk"
slug = ""
tags = ["program","design"]
draft = true
categories=["cs"]
title="接口一些设计原则"
description="接口一些设计原则。"
date="2019-04-12T10:32:07+08:00"

+++

什么是好的接口？怎么定义？

*How to Design a Good API and Why it Matters*

易学。

易用，甚至不需要文档。

难用错。

方便阅读和维护使用接口的代码。

足够的能力满足需求。

方便扩展。

易于解释。

一些惯例？

设计过程

1. 收集需求
   1. 收集更多的解决方案
   2. 提取真正的需求，使用use-cases
   3. 构建通用的东西会更简单，更有回报
2. 从短小的spec开始，1页纸就够了
   1. 敏捷胜于完整。不需要完整的spec，提出方案讨论。
   2. 开展讨论，认真吸收大家提出的方案。
   3. 保持spec短小，方便修改。
   4. 确定没问题以后补充完整。

RESTFul

http://www.ruanyifeng.com/blog/2018/10/restful-api-best-practices.html