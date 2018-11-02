+++
author = "zenk"
slug = ""
tags = ["memory"]
draft = true
categories=["cs"]
title="cache相关概念"
description="cache的相关问题"
date="2018-10-29T17:30:38+08:00"

+++

## 缘起

由于程序的时间空间局部性原理以及CPU访问内存的开销，增加一层cache加速数据的访问。

## 相关概念

cache中有三个核心概念：路（Way），组（Set），标记（Tag）。路和组用来组织cache，标记用来标识是否命中。这样的组织方式是性能和功耗折中的结果。这里组用的是虚拟地址，标记用的是物理地址。

通过查看`/sys/devices/system/cpu/cpu0/cache/index0`查看cache大小。CPU `Intel(R) Core(TM) i7-4790 CPU @ 3.60GHz`一些特性：支持39bit的物理地址，48位虚拟地址，一级cache大小是32K，8路，64组，行大小64。因此，物理页大小4K=2^12，标记需要2^39/2^12=27bit，组需要6bit，字节需要6位。



## 一致性协议