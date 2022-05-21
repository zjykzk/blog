+++
author = "zenk"
slug = ""
tags = ["program","design"]
categories=["cs"]
title="常用面向对象设计原则"
description="常用的面向对象设计原则，SOILD"
date="2018-07-04T22:28:20+08:00"
+++

## 设计

软件的复杂来源于需求的易变，意味着软件本身容易修改。好设计的目的就是提供软件的可修改能力，也就是可维护性、扩展性。SOILD原则就是在设计过程中达到这个目标的一些原则。

## 单一职责原则

又名SRP（Single Responsibility Principle）。针对一个函数、类、组件、架构的修改有且只有一个理由，而理由的来自于使用者。

这样的好处是把拥有相同修改理由的函数、类、组件组织在一起，不同的分开，达到修改的时候不会影响其他代码，增强了可维护性。

这是一个定义简单，实操不容易正确的原则。原因在于：
1. **职责**无法度量。
2. 因为团队、项目背景等待原因，在具体实现的细节中很难做到SRP。

因此，在设计的时候接口一定做到SRP，实现尽量SRP。

**注：**

组件层面的SRP，叫做Component common closure，架构层面的SRP叫做axis of change responsibility for creation of architecture boundary。

## 开闭原则

又名OCP（Open-Close Principle）。对扩展开发，对修改关闭。

通过这样的方式达到添加一个功能时，尽可能少的修改现有源代码、模块、二进制文件，尽可能的通过添加代码来实现。这样减少原来的功能被破坏的概率，达到软件的可维护性、可扩展性、可复用性。因此，它是其他面向对象设计原则的核心。

遵守OCP原则的手段是**抽象**。一个功能的抽象，更依赖于使用者，而非实现者。只有使用者才明白需要抽象什么内容。抽象的难点是找到易变的部分，一个指导原则是“快速失败，下不为例”，有以下几条参考实践：
1. TDD，先写测试代码。
2. 更短的开发周期。
3. 先开发特性，后开发基础设施代码，并经常给使用者review。
4. 先开发重要功能。
5. 经常并尽早发布，尽可能让用户和使用者使用。

抽象的对象一般是类、模块以及组件。几个比较的好的实践：
1. 在函数参数、类抽象中提供稳定的接口定义。
2. 通过元数据抽象逻辑，比如通过配置的形式表达逻辑。
3. 定义项目章程，建立团队文化，沉淀优秀的习惯，提高开发效率。
4. 在架构层面，分析功能变化的来源、时机以及原因，把功能划分为不同的组件，底层组件依赖高层组件，高层组件不会受到底层组件变化的影响，同时避免循环依赖。
5. 抽象的时候需要避免过度抽象，带来不必要的复杂度。

## 里氏替换原则

又名LSP（Liskov Substitutiion Principle）。基类能够被子类代替，并且保证程序行为不变。

OCP的实现需要使用抽象和多态，静态语言中继承是多态的一个重要实现方式。LSP就是解决继承带来的一些问题，比如侵入性、耦合性、缺乏灵活性。遵守LSP能够更加容易遵守OCP，因为子类可以替换基类，达到不修改原来代码，通过扩展的方式，添加逻辑。提高程序的健壮性，版本升级的兼容性。

继承中常说的IS-A，强调的是方法的行为，子类中的方法行为要和基类中的一致，而不是性质一致。这个行为需要从设计的使用者角度来判断模块。模块逻辑的一致性，说的就是这个行为需要一致。所以，IS-A语义是子类替换时，保证程序行为一致。

虽然这里LSP强调代码中的继承，其实LSP也适用于其他约定的服务、组件，这些内容修改、替换以后都不应该影响原来程序的行为。

几个比较好的实践：
1. 当子类中override的方法工作比较少时，可能违反LSP。
2. 采用DBC（design by contract）编程方法。约定方法的前置条件和后置条件，在LSP下，子类中的前置条件只能比基类的弱，而子类中的后置条件只能比基类的强。因为，如果子类中的前置条件强，那么替换以后原来基类的前置条件下的输入就没法满足了，同样如果子类的后置条件弱，那么方法的输出在一些情况下程序行为就会和原来的不一样。

## 依赖反转原则

又名DIP（Dependence Inversion Principle）。高层不依赖底层，依赖抽象，底层也只依赖抽象；抽象不依赖细节，细节依赖抽象。

反转（inversion）包含两层含义：
1. 控制流和源代码依赖相反，a模块执行时会调用b模块函数，但是源代码层面来说b模块会依赖a模块。
2. 接口所有者，原先a模块使用b模块定义的接口，而现在接口放在了a模块中，从而从源代码层面来说b模块依赖a模块。

为什么要依赖抽象？显然抽象比实现细节稳定。从编程语言角度上来说，接口变了实现不变，而实现变了，接口不一定变，显然接口更加稳定。因此，接口的稳定也十分重要。

DIP能够减少类、模块之间的耦合，提供系统的稳定性，提高代码的复用性、可扩展性、可读性和可维护性。它是其他OO设计技巧的基础。

建立依赖的方式：
1. 构造函数传递依赖对象。
2. setter方法传递对象。
3. 接口声明依赖对象，接口中的方法参数、返回值中引用其他接口。

几个比较好的实践：
1. 每个类尽量有接口或者抽象类。
2. 变量的表面类型尽量是接口、抽象类型或者是不易变的类。
3. 任何类不从易变的具体类派生。在维护代码的时候这个实践经常会被破坏。
4. 尽量不要override基类的方法。
5. 创建对象时考虑使用工厂模式。

## 接口分离原则

又名ISP（Interface Segregation Principles）。使用者不应该依赖它不使用的方法。所以，分离的使用者意味着分离的接口。

当你依赖的接口包含不需要的方法时，加上依赖的传递性，从源代码角度看当接口的改变，你的代码可能会跟着改变（这是因为对动态语言来说不用修改原来的代码），从架构角度看由于组件依赖，当组件修改时，会导致组件的重新编译、发布。ISP的目的还是减少类、模块间的耦合，提供类、模块的内聚性，提高代码的可扩展性、可复用性。

有两类接口：
1. class interface，在类层面履行接口，每个实现细节实现具体的接口，在golang中就是`interface`定义的接口。
2. object interface，在对象层面履行接口，每个新建的对象拥有类的方法，在golang中就是`struct`定义的方法。

SRP也强调职责分离，虽然它的效果也会有ISP的效果，但是它是从业务逻辑的角度去归类职责并进行分离。而ISP是从接口的角度去分离接口，它是在SIP的基础上进一步的细分。

几个比较好的实践：
1. 一个接口是只服务于一个模块或者业务逻辑。
2. 尽量减少公共的方法。
3. 保持接口的干净。如果有污染尽快修复。

## 结论

软件开发首要原则就是管理复杂度。显然，软件中的每个组成（函数、类、模块、组件）之间越独立（耦合性越低），整个软件的复杂度越低，软件就越容易维护。所以，软件设计原则中最重要的就是降低各个组成部分的耦合度。而，最重要的手段就是抽象。OOD的原则做的都是使用抽象这个利器来降低组成部分的耦合。他们从不同的角度来实现这个目标：业务逻辑角度（SRP），接口的角度（ISP），特定语言角度（LSP），软件扩展角度（OCP），组件依赖关系角度（DIP）。