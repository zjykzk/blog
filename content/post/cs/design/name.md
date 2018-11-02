+++
author = "zenk"
slug = ""
tags = ["program","design"]
draft = true
categories=["cs"]
title="命名习惯"
description="一些命名习惯。"
date="2018-09-26T10:22:39+08:00"

+++

变量

i > index

函数

每个单词首字母大写，（当然如果包内访问第一个单词首字母小写）

db：Insert/Remove/Update/Find

结构体

每个单词首字母大写，（当然如果包内访问第一个单词首字母小写）

接口

如果接口只有一个方法，以"er"结尾

配置命名

变量： conf

类型： XXXConfig

创建对象统一用New，不用Create。



https://blog.golang.org/package-names
https://rakyll.org/style-packages/
https://github.com/bketelsen/talks/blob/master/slides/gcru18-best.md


代码组织：

## 包的组织

同一个包中使用多个文件，每个文件负责不同的逻辑

把类型定义在它被使用的附近

按照功能组织代码，还不是类型

不导出main这个包中的任何东西，因为它是起点

## 包名

小写，短小精悍，通过包名知道包的作用，避免common/utils这样的包名

导入干净的包路径，导入路径中不能有src/pkg

不能有复数的包名字

重命名的时候也应该遵守通用的规则

使用虚拟URL，就是给一个包定义一个导入的路径，如果不按这个路径来就会出错，这个可以避免多副本的问题