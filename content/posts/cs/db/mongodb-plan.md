+++
author = "zenk"
slug = ""
tags = []
draft = true
categories=[]
title="mongodb plan"
description="mongodb学习计划"
date="2020-03-07T13:31:54+08:00"

+++

# case

golang里面调用find查询,mongodb返回结果.中间都发生了什么?

1. 请求协议是怎么样的?
   1. golang客户端代码
   2. 怎么选择一个server的
2. 数据格式怎么封装?
3. mongodb收到数据以后处理逻辑是怎么样的,他的网络模型是怎么样的?
4. qsl是怎么处理的?
5. 数据怎么从磁盘读出来的,在磁盘里面又是什么格式?
6. 主从复制原理?
7. 不通的writeConcern它的实现原理是什么?
8. 不同的readContern实现原理是什么?
9. 分片原理?
10. 索引原理?
11. 内存管理?