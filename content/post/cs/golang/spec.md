+++
author = "zenk"
slug = ""
tags = ["golang"]
draft = true
categories=["cs"]
title="golang spec记录"
description="关于golang的spec的理解。"
date="2019-04-12T10:41:42+08:00"

+++

## 可赋值性（Assignability）

**可赋值性**定义了一个变量能否赋值给另一个变量的规则。

```
var (
    x T
    y V
)
x = y
```

上述代码中如果`x=y`要成立，类型`T`和`V`需要满足以下几个条件：

1. 相同的类型，比如他们都是类型`int`。

2. 相同的underlying type，同时`T`和`V`中至少有一个不是通过这样的形式`define typeName otherType`定义的。

   ```
   // case 1 failed，因为V就是string，内置类型也算是define定义出来出来的，只是预定义而已
   type T string
   type V = string
   
   // case 2 OK
   type T struct{}
   type V = T
   
   // case 3 failed，因为都使用了define定义新的类型
   type T struct{}
   type V T
   
   // case 4 failed，因为都使用了define定义新的类型
   type T string
   type V string
   ```

3. `T`是接口，`V`实现了该接口的方法。

4. `V`是可读写的`channel`类型，`T`也是channel类型不限制读写，他们的元素类型必须相同，同时`T`和`V`中至少有一个不是通过这样的形式`define typeName otherType`定义的。

5. `y`是预定义的`nil`值，那么`T`类型必须是指针类型、函数类型、slice、map、channel或者接口类型。

6. `y`是无类型的（`untyped`）的常量，这个常量值在`T`类型能表示范围内。