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

## 类型同一性（Type identity）

**两个类型，要么一样要么不一样。**

`type typename struct{}`和`type typename existed-type`这样定义出来的类型是一个全新的类型，与其他现有的类型都不一样。如果两个类型要一样，那么他们的`underlying type`的结构必须是一致，也就是说他们结构定义以及对应的组成部分必须是一致的：

1. 数组：长度和元素的类型要一样。
2. slice：元素类型要一样。
3. 结构体：字段的顺序、名字、类型和tags必须一致。不同包的`Non-exported`字段的名字一定是不一样的。
4. 指针：指向的类型要一样。
5. 函数：参数和返回值的个数和类型要一样。另外，要么都是变参，要么都不是。参数和返回值的参数名字不要求一样。
6. 接口：方法集合有一样的名字和函数类型，顺序没关系。不同包的`Non-exported`方法名字一定是不一样的。
7. map：key类型和元素类型要一样。
8. channel：元素类型和读写类型要一样。

## 方法集合（Method sets）

一个类型会有一个相关联的方法集合。

1. 接口：方法集合就是它定义的方法。
2. 常规类型`T`：接收者类型为`T`的方法集合。
3. 指针类型`*T`：接收者类型为`*T`或者`T`的方法集合。
4. 结构体`S`含类型为`T`嵌入字段（embedded field）：`S`和`*S`的方法集合都包含`T`的方法集合，`*S`的方法集合还包含`*T`的方法集合。
5. 结构体`S`含类型为`*T`嵌入字段（embedded field）：`S`和`*S`的方法集合都包含`T`的方法集合以及`*T`的方法集合。
6. 其他类型没有方法集合。