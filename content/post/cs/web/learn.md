+++
author = "zenk"
slug = ""
tags = ["web"]
draft = true
categories=["cs"]
title="前端学习的资料"
description="前端学习的资料"
date="2019-06-05T15:33:58+08:00"

+++

## webpack

webpack是一个前端的构建JavaScript模块脚本的工具。简单来说，通过配置文件（默认`webpack.config.js`）指定输入和输出以及文件处理规则，webpack按照规则打包结果并按照输出格式输出。

常见的操作：

1. 多个入口文件。
2. 通过babel-loader把es6或者jsx代码转换成es5版本。
3. 转换图片。
4. CSS模块化。
5. 最小化js代码（UglifyJs）。
6. 通过环境变量进行条件编译。
7. 代码优化：拆分，抽取公共代码，异步加载。

## 参考

1. [webpack-howto](https://github.com/petehunt/webpack-howto)

2. [webpack-demos](https://github.com/ruanyf/webpack-demos)