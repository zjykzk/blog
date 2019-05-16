+++
author = "zenk"
slug = ""
tags = ["program","design"]
draft = true
categories=["cs"]
title="接口一些设计原则"
description="接口一些设计原则。"
date="2019-04-12T10:32:07+08:00"

+++

什么是好的接口？怎么定义？

*How to Design a Good API and Why it Matters*

易学。

易用，甚至不需要文档。

难用错。

方便阅读和维护使用接口的代码。

足够的能力满足需求。

方便扩展。

易于解释。

考虑性能。

一些惯例？

设计过程

1. 收集需求
   1. 收集更多的解决方案
   2. 提取真正的需求，使用use-cases
   3. 构建通用的东西会更简单，更有回报
2. 从短小的spec开始，1页纸就够了
   1. 敏捷胜于完整。不需要完整的spec，提出方案讨论。
   2. 开展讨论，认真吸收大家提出的方案。
   3. 保持spec短小，方便修改。
   4. 确定没问题以后补充完整。



RESTful实现需要在3级以上

1. 只使用http作为传输协议。
2. 引入资源概念。
3. 使用http的方法作为资源的不同操作，同时使用http的状态码表示不同的结果。
4. API服务使用HATEOAS（获取资源的时候返回资源相关资源以及URI和操作方法，客户就可以知道怎么请求这些资源了）。



错误处理

[google cloud](https://cloud.google.com/apis/design/errors)

```
{
  "error": {
    "code": 401,
    "message": "Request had invalid credentials.",
    "status": "UNAUTHENTICATED",
    "details": [{
      "@type": "type.googleapis.com/google.rpc.RetryInfo",
      ...
    }]
  }
}
```

[microsoft](https://github.com/Microsoft/api-guidelines/blob/master/Guidelines.md#710-response-formats)

```
{
  "error": {
    "code": "BadArgument", // 必须的
    "message": "Previous passwords may not be reused", // 必须的
    "target": "password",
    "innererror": {
      "code": "PasswordError",
      "innererror": {
        "code": "PasswordDoesNotMeetPolicy",
        "minLength": "6",
        "maxLength": "64",
        "characterTypes": ["lowerCase","upperCase","number","symbol"],
        "minDistinctCharacterTypes": "2",
        "innererror": {
          "code": "PasswordReuseNotAllowed"
        }
      }
    }
  }
}
```

[RESTful API 最佳实践](http://www.ruanyifeng.com/blog/2018/10/restful-api-best-practices.html)

[阿里研究员谷朴：API 设计最佳实践的思考](<https://mp.weixin.qq.com/s?__biz=MzA5NDg3MjAwMQ==&mid=2457103117&idx=1&sn=ce97dcdb0349b44e9336a31749953a30&chksm=87c8c3a3b0bf4ab54eea12fb58acdb34e7cef3a12ec8bea9062e81c2f7de4841016cfb027508&scene=21#wechat_redirect>)

[微软api设计指南](https://github.com/Microsoft/api-guidelines/blob/master/Guidelines.md)

[微软api设计的最佳实践](<https://docs.microsoft.com/en-us/azure/architecture/best-practices/api-design>)

[api检查清单](https://mathieu.fenniak.net/the-api-checklist/)

[google云api设计模式](https://cloud.google.com/apis/design/design_patterns)