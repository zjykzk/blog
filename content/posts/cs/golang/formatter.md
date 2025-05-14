+++
author = "zenk"
slug = ""
tags = ["golang"]
draft = false
categories=["cs"]
title="gofmt原理分析一"
description="缩进、二元表达式"
date="2025-05-10T21:10:21+08:00"
+++

# 缩进

核心数据结构：

```go
const (
    indent   = whiteSpace('>')
    unindent = whiteSpace('<')
)

type printer struct {
    indent       int          // current indentation
    wsbuf        []whiteSpace // delayed white space
}
```

1. [`printer.wsbuf`](https://github.com/golang/go/blob/master/src/go/printer/printer.go#L68)记录[`indent`](https://github.com/golang/go/blob/master/src/go/printer/printer.go#L35)和[`unindent`](https://github.com/golang/go/blob/master/src/go/printer/printer.go#L36)两个常量；

2. [`printer.indent`](https://github.com/golang/go/blob/master/src/go/printer/printer.go#L61)字段保存当前缩进个数, 当在调用函数[`writeWhitespace`](https://github.com/golang/go/blob/master/src/go/printer/printer.go#L817)时会遍历`wsbuf`遇到`indent`值加1，遇到`unindent`时减一；

3. 当调用写入数据函数的时候，如果当前列是第一列就写入缩进；

# 二元表达式

## 缩进

生成：运算符和左边的表达式不在同一行，会在格式化右边表达式之前多一个索引；

消除：右边的表达式格式化完成以后，会减少一个缩进；

## 空格

运算符前后是否需要空格，比如：`a +b`中`+`左边有空格，右边没有空格。它的计算依赖一个**优先级分隔符**概念，它的值是一个优先级。

1. 优先级分隔符大于当前运算符优先级：
   
   * 运算符左边有空格；
   
   * 如果运算符和右表达式没有空行，运算符右边也有空格，否则没有空格；

2. 优先级分隔符小于等于当前运算符优先级：运算符左右都没有空格。

### 表达式深度

1. 初始深度是1；

2. 左操作数的深度以下两种情况会增加1：
   
   * 不是二元表达式
   
   * 是二元表达式，并且运算符的优先级和当前运算符一致；

3. 右操作数的深度增加1；

4. 操作数是圆括号的话，比如：`(a+b)`减一，但是不会小于1；

#### 模式

根据表达式深度的大小定义两种模式：

1. 普通模式：表达式深度等于1；

2. 紧凑模式：表达式深度大于1；

### 优先级分隔符

#### 运算符优先级

| 运算符                      | 优先级 |
| ------------------------ | --- |
| `*  /  %  <<  >>  &  &^` | 5   |
| `+  -  \|  ^`            | 4   |
| `==  !=  <  <=  >  >=`   | 3   |
| `&&`                     | 2   |
| `\|\|`                   | 1   |

#### 规则

1. 优先级小于等于3时，运算符左右边都有空格；

2. 运算符右边是一元运算符，按照下面的方式返回：
   
   | 二元运算符 | 右边的一元运算符 | 优先级分隔符 |
   | ----- | -------- | ------ |
   | /     | *        | 6      |
   | &     | &        | 6      |
   | &     | ^        | 6      |
   | +     | +        | 5      |
   | -     | -        | 5      |

3. 如果同时有4和5优先级的运算符，那么紧凑模式下返回4，普通模式下返回5；

4. 如果没有4或者5优先级的运算符，那么紧凑模式下返回4，普通模式下返回6；
