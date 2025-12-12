+++
author = "zenk"
slug = ""
tags = ["golang","tool"]
draft = true
categories=["cs"]
title="gofumpt原理分析四"
description="注释"
date="2025-06-18T10:38:02+08:00"
+++

doc comment

line comment

在某个token之前

复杂点：

1. token后面紧跟一个注释，空格是VTAB

2. 触发时机：每个token格式化的时候

3. token之间的换行&注释和token之间的换行怎么处理

4. 注释也是一个token，和正常token之间用空格或者vtab，换行缩进
