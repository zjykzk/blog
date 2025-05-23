+++
author = "zenk"
slug = ""
tags = ["golang","tool"]
draft = false
categories=["cs"]
title="gofmt原理分析二"
description="var&const group"
date="2025-05-20T10:26:00+08:00"
+++

说明以下代码格式化：

```go
var (
    i int = 1
    j
    k = 1 // comments
)

const (
    i int = 1
    j
    k = 1
)
```

`var/const/(/)`的格式化比较简单，基本上类似如下代码：

```go
println(indents, "var (", "\f")
println(indents, ")", "\f")

// indents: 表示缩进格式
```

圆括号内部稍微复杂些。内部的一条语句叫做 var spec，其完整形式是这样的：

```go
idents Type = values // comments


// e.g.
i, j int = 1, 2 // just some comments

// idents: 变量列表
// Type: 类型
// values: 值表达式列表
// comments: 注释
```

输出格式`idents|Type|= values|comments`其中`|`表示`\v`。

但是，其中`Type/=/values/comments`都是可以省略的（其中`=/values`是一起出现的）。

有几个格式化规则：

1. 如果有`Type`，前面跟着一个`|`；

```go
i|int
```

2. 如果没有`Type`，需要看当前var spec的前后多行，往前或者往后能够找到一个包含`Type`的var spec，而且中间没有仅仅只有`idents`的var spec，那么`idents`后面需要跟着一个`|`；

```go
// example
i|int|= 1
j||= 2
k
x |= 1
y |= 2
```

3. 如果有`values`，`values`之前需要`|=` ；

```go
i int |= 1
```

4. 如果有comments，`idents`和`comments`之间必须有三个`|`；

```go
// example1
i, j|int|= 1, 2|// comments

// example2
i|= 1||// just some comments

// example3
i|||// comments
```
