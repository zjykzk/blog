---
title: Web Chunk Source Guide
category: sources
tags:
  - frontend
  - architecture
  - software-engineering
sources:
  - conversation:2026-05-26
  - conversation:2026-05-27
created: 2026-05-26T23:02:15+08:00
updated: 2026-05-27T00:41:19+08:00
summary: >-
  这页保存一份中文前端构建讲解：bundler 把源码模块图转换成浏览器可加载的 chunks/assets，loadable 只是提供代码分割信号。
provenance:
  extracted: 0.93
  inferred: 0.07
  ambiguous: 0.00
base_confidence: 0.46
lifecycle: draft
lifecycle_changed: 2026-05-26
type: source
status: draft
aliases:
  - Web Chunk
  - 前端 Chunk
  - Bundler Chunk
---

# Web Chunk Source Guide

> Source: conversation:2026-05-26; conversation:2026-05-27

## Capture Policy

这页保留一份关于前端 `chunk`、`bundler`、`loadable`、动态导入和构建产物关系的中文教学材料。它作为 source 层材料保存解释顺序、示例和术语区分，不直接提升为前端工程的稳定母页。

## What It Covers

这份材料解释：`chunk` 不是 `loadable` 自己生成的东西，而是构建工具根据模块依赖图切出来的一组模块集合。`bundler` 的核心作用，是把源码里的 module graph 转换成浏览器可加载的 chunks / assets；`loadable` 的主要作用，是把代码写成构建工具能识别的分割点。

```tsx
const UserPage = loadable(() => import('./UserPage'))
```

这里真正关键的是动态导入：

```tsx
import('./UserPage')
```

Webpack、Vite、Rollup 等构建工具看到动态导入后，会知道 `./UserPage` 不必放进主包里，可以单独拆出去。

## Preserved Content

### bundler 是什么

`bundler` 就是前端打包工具。它做的事不是简单把文件拼起来，而是把一堆源码模块分析成浏览器能高效加载的产物。

最核心一句：

```txt
bundler 把源码里的 module graph 转换成浏览器可加载的 chunks / assets。
```

比如源码里写：

```tsx
import React from 'react'
import Header from './Header'

const UserPage = lazy(() => import('./UserPage'))
```

bundler 会做几件事：

1. 从入口文件开始，比如 `main.tsx`
2. 递归分析所有 `import / export`
3. 建出一张模块依赖图，也就是 module graph
4. 区分静态 import 和动态 import
5. 根据入口、动态 import、共享依赖、配置策略切出 chunk
6. 把 chunk 输出成 `.js`、`.css`、图片、map 等 asset
7. 生成运行时代码，让浏览器能按需加载异步 chunk

可以这样看：

```txt
源码文件
  ↓
Module
  ↓
Module Graph
  ↓
Chunk
  ↓
Asset
  ↓
浏览器请求和执行
```

常见 bundler：

| 工具 | 角色 |
| --- | --- |
| Webpack | 老牌全能 bundler，生态强，配置复杂 |
| Rollup | 更偏 library 打包，tree-shaking 强 |
| Vite | 开发期用原生 ESM + esbuild，生产构建底层用 Rollup |
| Rspack | Rust 写的 Webpack 兼容型 bundler，强调速度 |
| Parcel | 零配置 bundler |

它和 `loadable` 的关系是：

```txt
loadable / React.lazy
  ↓
包装 dynamic import
  ↓
bundler 看到 import()
  ↓
切出 async chunk
  ↓
浏览器运行时按需加载
```

所以更准确地说：

- `loadable` 不生成 chunk
- `import()` 提供分割信号
- `bundler` 生成 chunk
- 浏览器加载的是 bundler 输出的 asset

### chunk 是怎么来的

构建流程大致是：

```txt
源码
 ↓
入口文件 entry，比如 src/main.tsx
 ↓
构建工具分析 import / export
 ↓
生成模块依赖图 module graph
 ↓
遇到动态 import，形成分割点 split point
 ↓
把一组模块分到某个 chunk
 ↓
最终输出成 .js / .css / map 等文件
```

例如：

```tsx
// App.tsx
import Header from './Header'

const UserPage = loadable(() => import('./UserPage'))
```

依赖关系可能是：

```txt
App.tsx
 ├─ Header.tsx       静态 import
 └─ UserPage.tsx     动态 import
      ├─ UserTable.tsx
      └─ userApi.ts
```

构建工具可能生成：

```txt
main.[hash].js              // App + Header + runtime
UserPage.[hash].js          // UserPage + UserTable + userApi
```

其中 `UserPage.[hash].js` 对应的内部概念就是一个 chunk。

### 谁生成 chunk

chunk 主要由 bundler 或 build tool 生成。

| 项目工具 | 底层负责 chunk 的工具 |
| --- | --- |
| Webpack | Webpack |
| Vite | Rollup，开发期是 esbuild + Vite dev server |
| Rollup | Rollup |
| Rspack | Rspack |
| Parcel | Parcel |

`loadable` 本身不负责打包。它只提供 React 组件层的懒加载封装：

```tsx
loadable(() => import('./UserPage'))
```

关系是：

```txt
loadable 写法
 ↓
动态 import
 ↓
bundler 识别 split point
 ↓
生成 chunk
 ↓
运行时按需加载 chunk
```

也可以更准确地说：

```txt
loadable 包装动态 import
动态 import 提供分包信号
bundler 生成 chunk
runtime 加载 chunk
React 渲染组件
```

### 同一抽象层级的概念

如果按“打包产物”这个层级看，`chunk` 常和 `module`、`asset`、`bundle` 一起讨论。

```txt
Module -> Chunk -> Asset / Bundle
```

不同工具的叫法略有差异，但可以按下面的方式理解。

### Module

module 是源码层的基本单位。一个文件通常就是一个 module。

```txt
src/App.tsx
src/UserPage.tsx
src/api/user.ts
```

它们都是 module。

特点：

- 来自源码
- 由 `import` / `export` 连接
- 是构建工具分析依赖图的节点

例如：

```tsx
import { getUser } from './api/user'
```

这里的 `./api/user` 就是一个 module。

### Chunk

chunk 是构建工具内部划分出来的模块组。

```txt
Chunk: main
 ├─ App.tsx
 ├─ Header.tsx
 └─ router.tsx

Chunk: UserPage
 ├─ UserPage.tsx
 ├─ UserTable.tsx
 └─ userApi.ts
```

特点：

- 由 bundler 生成
- 通常由入口、动态 import、手动分包配置决定
- 不一定直接等于最终文件，但通常会输出成文件

### Asset

asset 是构建后真正落到 `dist` 里的文件。

```txt
dist/assets/main.abc123.js
dist/assets/UserPage.def456.js
dist/assets/main.abc123.css
dist/assets/logo.789.png
```

特点：

- 是文件系统里的实际产物
- 浏览器最终请求的是 asset
- 一个 chunk 可能生成一个或多个 asset

例如一个异步页面 chunk 可能生成：

```txt
UserPage.abc123.js
UserPage.abc123.css
```

### Bundle

bundle 是比较泛的“打包结果”说法，不是所有工具里都严格定义的内部概念。

它可以指某个包：

```txt
main.js
vendor.js
UserPage.js
```

也可以泛指整个构建产物：

```txt
dist/ 目录里的所有 JS/CSS
```

所以：

- `chunk` 更偏构建工具内部概念
- `asset` 更偏最终文件概念
- `bundle` 更偏口语或文档层面的“包”

### 它们的关系

```txt
源码文件 / npm 包
     ↓
Module
     ↓
依赖图 Module Graph
     ↓
Chunk
     ↓
Asset
     ↓
浏览器加载执行
```

更具体地说：

```txt
src/App.tsx          ┐
src/Header.tsx       ├─ main chunk ─────── main.abc123.js
src/router.tsx       ┘

src/UserPage.tsx     ┐
src/UserTable.tsx    ├─ UserPage chunk ─── UserPage.def456.js
src/userApi.ts       ┘
```

### 常见 chunk 类型

#### Entry chunk

入口 chunk。

```tsx
// main.tsx
ReactDOM.createRoot(...).render(<App />)
```

它会形成主 chunk：

```txt
main.[hash].js
```

这是页面启动必须加载的。

#### Async chunk

异步 chunk，通常由动态 import 产生。

```tsx
const UserPage = loadable(() => import('./UserPage'))
```

生成：

```txt
UserPage.[hash].js
```

只有访问到这个页面时才加载。

#### Vendor chunk

第三方依赖 chunk。

```txt
vendor.[hash].js
```

里面可能有：

```txt
react
react-dom
lodash
antd
```

这样拆的好处是第三方库变化少，可以更好地利用浏览器缓存。

#### Common chunk

公共 chunk。

如果多个异步页面都依赖同一个模块：

```txt
PageA ─┐
       ├─ shared/dateFormatter.ts
PageB ─┘
```

构建工具可能把它抽成公共 chunk：

```txt
common.[hash].js
```

这样可以避免 PageA 和 PageB 各自重复打包一份。

#### Runtime chunk

runtime chunk 是构建工具的运行时代码。Webpack 中常见：

```txt
runtime.[hash].js
```

它负责：

- 维护 chunk 映射
- 加载异步 chunk
- 处理模块缓存
- 拼接资源 URL

浏览器运行时加载异步 chunk，靠的就是这部分代码。

### 完整例子

源码：

```tsx
// App.tsx
import Header from './Header'

const ReportPage = loadable(() => import('./ReportPage'))
const AuditPage = loadable(() => import('./AuditPage'))

export default function App() {
  return (
    <>
      <Header />
      <Routes>
        <Route path="/report" element={<ReportPage />} />
        <Route path="/audit" element={<AuditPage />} />
      </Routes>
    </>
  )
}
```

可能生成：

```txt
dist/assets/
  main.111.js
  ReportPage.222.js
  AuditPage.333.js
  vendor.444.js
  runtime.555.js
```

对应关系：

```txt
main.111.js
  App
  Header
  router 配置

ReportPage.222.js
  ReportPage
  ReportTable
  report API 相关代码

AuditPage.333.js
  AuditPage
  AuditForm
  audit API 相关代码

vendor.444.js
  react
  react-dom
  react-router
  antd

runtime.555.js
  chunk 加载逻辑
  module cache
  chunk id 映射
```

用户第一次打开页面：

```txt
加载 main + vendor + runtime
```

访问 `/report` 时：

```txt
额外加载 ReportPage.222.js
```

访问 `/audit` 时：

```txt
额外加载 AuditPage.333.js
```

### 总结

chunk 是 bundler 根据模块依赖图和代码分割点生成的模块分组。module 是源码模块，asset 是最终文件，bundle 是打包结果的泛称。`loadable` 通过 dynamic import 间接促成 async chunk 的生成。

## Integration Decisions

这页应保持在 source 层，因为它解释的是一次具体教学中的术语关系和构建流程。后续如果要提升为稳定概念，可以考虑建立 `Chunk` 或 `Code Splitting` 概念页，但目前更适合作为 [[wiki/topics/Frontend Development|Frontend Development]] 与 [[wiki/concepts/React|React]] 周边的构建知识材料。

这里的关键边界是：`loadable` 属于 React 组件层的懒加载封装；动态 `import()` 是语言/模块系统层面的分割信号；`bundler` 是把源码模块图转成 chunk、asset 和 runtime 映射的构建层。这个边界可以帮助避免把运行时懒加载组件误解成“组件库自己打包”。^[inferred]

## Related

- [[wiki/topics/Frontend Development]]
- [[wiki/topics/Frontend Development Workflow]]
- [[wiki/concepts/React]]
- [[wiki/concepts/Component-Based Architecture]]
- [[wiki/concepts/State Management]]
- [[wiki/sources/React Component Lifecycle Source Guide]]
- [[wiki/sources/React Hooks useState useEffect Source Guide]]
