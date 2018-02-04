+++
author = "zenk"
slug = ""
tags = ["vim"]
draft = false
categories=["cs"]
title="vim常用操作"
description="vim常用操作"
date="2018-01-10T18:16:35+08:00"
+++

1. 在命令模式使用函数

```
:%s/ab(.*)c/\=submatch(1) . 'test'/gc
```

2. 窗口间切换

```
跳转至某个窗口：窗口number + c-w + w：
跳至当前位置的左边某个窗口：c-w <number>h
跳至当前位置的右边某个窗口：c-w <number>l
跳至当前位置的上边某个窗口：c-w <number>j
跳至当前位置的下边某个窗口：c-w <number>k
```

3. 全文缩进

```
gg=G
```

4. 把数字替换成原来的数字减一

```
:%s/(\d+)/\=submatch(1)-1/gc
```

5. 移动屏幕

```
H // 把当前行的位置移到最上面
M // 把当前行的位置移到屏幕中间
L // 把当前的位置移到屏幕底部
```

6. 全局操作`g`

```
:{range}g/patten/{range}/cmd // 后面的range是基于前面查询的结果
```

7. 移动窗口

```
CTRL-W [K/J/H/L/T] //  把窗口移到最上面、下面、左边、右边、新标签
```