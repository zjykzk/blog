---
title: >-
  React Hooks useState useEffect Source Guide
category: sources
tags:
  - article
  - frontend
  - architecture
sources:
  - conversation:2026-05-12
created: 2026-05-12T16:36:46+08:00
updated: 2026-05-12T16:36:46+08:00
summary: >-
  这页保存一份中文 React Hooks 讲解，把 useState 和 useEffect 放在函数组件反复执行、状态驱动渲染和渲染后副作用的框架下理解。
provenance:
  extracted: 0.91
  inferred: 0.08
  ambiguous: 0.01
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-05-12
---
# React Hooks useState useEffect Source Guide

> Source: 当前对话中的中文 React Hooks 讲解：useState vs useEffect

## Capture Policy

这页保留 source 层内容，不翻译，不压缩成简短摘要。它保存的是一份可直接复读的中文教学材料：共同底层前提、核心心智模型、代码例子、依赖数组、清理函数、误区和判断标准。

这份材料与 [[wiki/sources/React Hooks useRef useContext useMemo Source Guide]] 构成同一组 React Hooks 入门来源层：前者解释 `useRef` / `useContext` / `useMemo`，本页解释 `useState` / `useEffect`。二者共同补充 [[wiki/concepts/React]]、[[wiki/concepts/State Management]] 和 [[wiki/syntheses/React UI Organization Model]] 中关于渲染、状态与组件协作的知识。^[inferred]

## What It Covers

这份讲解把 `useState` 和 `useEffect` 放在 React 函数组件的同一个底层事实里理解：

React 组件每次渲染，函数都会重新执行。

所以 React 需要解决两个问题：

1. 有些数据要跨渲染保留，并且变化后要刷新 UI → `useState`
2. 有些事情不应该直接放在渲染过程中做，而应该在渲染之后同步外部世界 → `useEffect`

一句话：

- `useState` 管“组件内部状态”
- `useEffect` 管“渲染后的副作用”

更短：

- `useState` 让组件记住值。
- `useEffect` 让组件对变化做事。

## Preserved Content

### useState：让组件拥有会驱动 UI 更新的状态

基本形式：

```jsx
const [count, setCount] = useState(0)
```

它做两件事：

1. `count` 是当前状态值
2. `setCount` 用来更新状态，并触发组件重新渲染

例子：

```jsx
function Counter() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div>{count}</div>
      <button onClick={() => setCount(count + 1)}>+</button>
    </>
  )
}
```

点击按钮后：

```jsx
setCount(count + 1)
```

React 会：

1. 记录新的 `count`
2. 重新执行 `Counter`
3. 用新的 `count` 重新生成 UI

所以 `useState` 的核心是：

状态变化 → 触发重新渲染 → UI 更新

### 为什么不能直接用普通变量

不要这样写：

```jsx
function Counter() {
  let count = 0

  return (
    <>
      <div>{count}</div>
      <button onClick={() => count++}>+</button>
    </>
  )
}
```

这不行。

原因是：

1. `count++` 不会通知 React 重新渲染
2. 即使组件重新渲染，函数重新执行，`count` 又会变回 `0`

所以普通变量的问题是：

它既不能触发渲染，也不能跨渲染保留。

`useState` 同时解决这两个问题：

1. 跨渲染保留值
2. 更新时触发渲染

### useState 的心智模型

`useState` 像组件身上的“状态槽”。

组件函数每次重新执行，但 React 在组件背后保存了一组状态槽。

```jsx
function Demo() {
  const [name, setName] = useState('Alice')
  const [age, setAge] = useState(18)
}
```

可以理解成 React 给这个组件保存了两个槽：

```text
slot 1: name
slot 2: age
```

每次组件重新渲染，React 按 Hook 调用顺序把状态还给你。

这也是为什么 Hook 不能写在 `if` 里面：

```jsx
if (condition) {
  const [x, setX] = useState(0)
}
```

因为这样会破坏 Hook 的调用顺序。

### useState 的更新不是立即修改当前变量

很多初学者会写：

```jsx
function Counter() {
  const [count, setCount] = useState(0)

  function handleClick() {
    setCount(count + 1)
    console.log(count)
  }

  return <button onClick={handleClick}>{count}</button>
}
```

点击时，`console.log(count)` 仍然可能打印旧值。

因为：

```jsx
setCount(count + 1)
```

不是把当前这一轮函数里的 `count` 立刻改掉，而是告诉 React：下一次渲染时，请使用新的状态。

所以更准确地说：

`setState` 安排下一次渲染的状态，不是原地修改当前变量。

### 函数式更新：依赖旧状态时更稳

如果新状态依赖旧状态，推荐写：

```jsx
setCount(c => c + 1)
```

而不是：

```jsx
setCount(count + 1)
```

尤其是连续更新时：

```jsx
setCount(count + 1)
setCount(count + 1)
setCount(count + 1)
```

这不一定会加 3，因为三个 `count` 可能都是同一个旧值。

更稳的写法：

```jsx
setCount(c => c + 1)
setCount(c => c + 1)
setCount(c => c + 1)
```

这里每次都基于 React 提供的最新状态继续算。

### useEffect：在渲染后执行副作用

基本形式：

```jsx
useEffect(() => {
  // 做一些事
}, [deps])
```

`useEffect` 的意思是：

当组件渲染完成后，如果依赖变化了，就执行这个函数。

例子：

```jsx
function UserProfile({ userId }) {
  const [user, setUser] = useState(null)

  useEffect(() => {
    fetch(`/api/users/${userId}`)
      .then(res => res.json())
      .then(data => setUser(data))
  }, [userId])

  return <div>{user?.name}</div>
}
```

这里：

1. 组件先根据当前状态渲染
2. 渲染后，`useEffect` 发现 `userId` 变化
3. 发起请求
4. 请求完成后 `setUser(data)`
5. 状态更新，再次渲染 UI

所以 `useEffect` 的核心是：

渲染完成后 → 根据依赖变化 → 同步外部系统或执行副作用

### 什么是副作用

在 React 里，组件渲染本身最好是“纯”的。

也就是说：

同样的 props 和 state，应该返回同样的 UI。

渲染阶段不应该直接做这些事：

1. 请求网络
2. 操作 DOM
3. 设置定时器
4. 订阅事件
5. 写 localStorage
6. 修改外部变量
7. 调用非 React 管理的外部 API

这些都叫副作用。

因为它们会影响 React 之外的世界。

`useEffect` 就是专门处理这些事情的地方。

### 为什么不能直接在组件函数里 fetch

不要这样写：

```jsx
function UserProfile({ userId }) {
  const [user, setUser] = useState(null)

  fetch(`/api/users/${userId}`)
    .then(res => res.json())
    .then(data => setUser(data))

  return <div>{user?.name}</div>
}
```

问题是：

1. 组件每次渲染都会重新执行函数
2. 每次执行都会发起 fetch
3. fetch 完成后 `setUser`
4. `setUser` 又触发渲染
5. 渲染又 fetch

可能形成无限循环。

正确做法：

```jsx
useEffect(() => {
  fetch(`/api/users/${userId}`)
    .then(res => res.json())
    .then(data => setUser(data))
}, [userId])
```

意思是：

只有 `userId` 变化时，才重新请求。

### useEffect 的依赖数组

`useEffect` 最难的地方通常是依赖数组。

形式一：没有依赖数组

```jsx
useEffect(() => {
  console.log('rendered')
})
```

每次渲染后都会执行。

形式二：空依赖数组

```jsx
useEffect(() => {
  console.log('mounted')
}, [])
```

只在组件首次挂载后执行一次。

常用于：

1. 初始化请求
2. 初始化订阅
3. 初始化第三方库

形式三：有依赖

```jsx
useEffect(() => {
  console.log('count changed')
}, [count])
```

首次渲染后执行一次，以后只有 `count` 变化才执行。

### useEffect 的清理函数

有些副作用需要清理。

比如定时器：

```jsx
useEffect(() => {
  const id = setInterval(() => {
    console.log('tick')
  }, 1000)

  return () => {
    clearInterval(id)
  }
}, [])
```

这里 `return` 出来的函数就是清理函数。

它会在这些时候执行：

1. 组件卸载时
2. effect 下一次重新执行前

再比如事件监听：

```jsx
useEffect(() => {
  function handleResize() {
    console.log(window.innerWidth)
  }

  window.addEventListener('resize', handleResize)

  return () => {
    window.removeEventListener('resize', handleResize)
  }
}, [])
```

核心原则：

谁创建，谁清理。

否则容易出现：

1. 定时器泄漏
2. 重复订阅
3. 事件监听越来越多
4. 旧请求覆盖新结果

### useState vs useEffect 的核心区别

可以这样记：

| Hook | 解决什么问题 | 什么时候执行 | 是否触发渲染 |
|---|---|---|---|
| `useState` | 保存组件状态 | 渲染期间读取，事件中更新 | `setState` 会触发渲染 |
| `useEffect` | 执行副作用 | 渲染提交后执行 | 本身不触发，但里面调用 `setState` 会触发 |

更直观：

- `useState` 是“数据”。
- `useEffect` 是“动作”。

`useState` 问的是：

这个组件现在处于什么状态？

`useEffect` 问的是：

当某些状态或 props 变化后，我需要对外部世界做什么？

### 两者经常配合使用

最典型的组合：

```jsx
function SearchResult({ keyword }) {
  const [results, setResults] = useState([])

  useEffect(() => {
    fetch(`/api/search?q=${keyword}`)
      .then(res => res.json())
      .then(data => setResults(data))
  }, [keyword])

  return (
    <ul>
      {results.map(item => (
        <li key={item.id}>{item.title}</li>
      ))}
    </ul>
  )
}
```

这里：

`useState` 保存搜索结果。

```jsx
const [results, setResults] = useState([])
```

`useEffect` 在 `keyword` 变化后发请求。

```jsx
useEffect(() => {
  fetch(...)
}, [keyword])
```

请求完成后：

```jsx
setResults(data)
```

更新状态，触发 UI 重新渲染。

所以完整链路是：

`keyword` 变化 → 组件渲染 → effect 执行请求 → 请求完成 → setResults → 组件重新渲染 → UI 显示新结果

### 一个常见误区：用 useEffect 同步可以直接算出来的状态

不要这样写：

```jsx
function User({ firstName, lastName }) {
  const [fullName, setFullName] = useState('')

  useEffect(() => {
    setFullName(firstName + lastName)
  }, [firstName, lastName])

  return <div>{fullName}</div>
}
```

这里 `fullName` 完全可以从 props 直接算出来：

```jsx
function User({ firstName, lastName }) {
  const fullName = firstName + lastName

  return <div>{fullName}</div>
}
```

原则：

如果一个值可以在渲染期间直接从 props/state 算出来，就不要放进 state，也不要用 effect 同步。

否则会带来：

1. 多一次渲染
2. 状态重复
3. 数据不一致风险
4. 代码复杂度增加

### 什么时候用 useState

当你需要组件记住某个值，并且这个值变化后要影响 UI。

常见场景：

1. 输入框内容
2. 弹窗是否打开
3. 当前选中的 tab
4. 请求结果
5. 加载状态
6. 错误信息
7. 用户交互产生的状态

例子：

```jsx
const [open, setOpen] = useState(false)
const [text, setText] = useState('')
const [loading, setLoading] = useState(false)
const [error, setError] = useState(null)
```

判断标准：

这个值是否会随着用户交互、请求结果或组件生命周期变化？

这个值变化后是否应该刷新 UI？

如果是，用 `useState`。

### 什么时候用 useEffect

当你需要在渲染后同步 React 外部的东西。

常见场景：

1. 网络请求
2. DOM 订阅
3. WebSocket 连接
4. 定时器
5. localStorage 同步
6. document title 更新
7. 第三方库初始化
8. 手动注册和注销事件

例子：

```jsx
useEffect(() => {
  document.title = `Count: ${count}`
}, [count])
```

```jsx
useEffect(() => {
  const socket = new WebSocket(url)

  return () => {
    socket.close()
  }
}, [url])
```

判断标准：

这件事是不是在 React 渲染之外产生影响？

如果是，它大概率属于 `useEffect`。

### 更底层的理解

React 渲染可以分成两类工作：

1. 计算 UI 应该长什么样
2. 把 React 外部世界同步到这个 UI 状态

`useState` 属于第一类的输入：

它提供“当前 UI 应该基于什么状态来计算”。

`useEffect` 属于第二类的出口：

它在 UI 渲染完成后，把变化同步给外部系统。

所以：

```text
props/state → render → UI
                 ↓
              effect → 外部世界
```

或者：

```text
useState：进入渲染的数据
useEffect：离开渲染的动作
```

### 和 useRef / useMemo / useContext 放在一起看

`useRef`：跨渲染保存可变值，但不触发渲染。

`useContext`：跨组件共享值，避免 props drilling。

`useMemo`：缓存计算结果，避免重复计算或引用不稳定。

现在加上两个：

`useState`：跨渲染保存状态，并触发 UI 更新。

`useEffect`：渲染后执行副作用，同步外部系统。

放在一起：

| Hook | 核心用途 |
|---|---|
| `useState` | 保存会驱动 UI 的状态 |
| `useEffect` | 渲染后执行副作用 |
| `useRef` | 保存不驱动 UI 的可变值 |
| `useContext` | 跨层共享值 |
| `useMemo` | 缓存计算结果 |

最关键的区分是：

- 需要 UI 更新 → `useState`
- 不需要 UI 更新，只要保存值 → `useRef`
- 需要对外部世界做事 → `useEffect`
- 需要跨组件共享 → `useContext`
- 需要缓存计算结果 → `useMemo`

### 一句话总结

`useState` 是：

我想让组件记住一个值，并且这个值变化时刷新页面。

`useEffect` 是：

我想在渲染完成后，根据某些变化去做一件影响外部世界的事。

再压缩一点：

`useState` 管状态。

`useEffect` 管副作用。

最底层：

`useState` 参与渲染。

`useEffect` 发生在渲染之后。

## Integration Decisions

这份 source guide 应保留在来源层，因为它是一份完整的中文教学材料，价值在于讲解顺序、代码例子、判断标准和常见误区共同构成的学习路径，而不只是几个抽象结论。

可提升到稳定知识层的内容包括：

- `useState` 是函数组件里的状态槽：跨渲染保留值，并在更新时触发重新渲染。
- `setState` 安排下一次渲染的状态，不是原地修改当前变量。
- 当新状态依赖旧状态时，函数式更新比直接使用当前闭包里的状态更稳。
- `useEffect` 是渲染提交后的副作用出口，用于同步 React 外部世界。
- 如果一个值可以在渲染期间直接从 props/state 算出来，就不应该再用 state 和 effect 同步。
- `useState` 是进入渲染的数据；`useEffect` 是离开渲染的动作。

这份材料强化了 [[wiki/concepts/State Management]] 对“状态在哪里、谁改变它、改变如何传播”的解释，也强化了 [[wiki/syntheses/React UI Organization Model]] 对 React 作为 UI 协调模型的理解。^[inferred]

后续如果继续补充 `useReducer`、`useCallback`、`useLayoutEffect`，可以建立一个更完整的 React Hooks 概念页；但当前不需要为了这份 tutorial 立即创建新概念页，避免把 source 层教学材料过早压缩成概念索引。^[inferred]

## Open Questions

- 是否需要建立单独的 `React Hooks` 概念页，把 `useState`、`useEffect`、`useRef`、`useContext`、`useMemo` 放入同一个“函数组件持久化结构”模型？
- `useEffect`、`useLayoutEffect` 和事件处理函数之间的边界是否需要单独整理？
- React 新文档中“you might not need an effect”的判断标准，是否应该补充进 [[wiki/concepts/State Management]] 或未来的 Hooks 概念页？

## Related

- [[wiki/concepts/React]]
- [[wiki/concepts/State Management]]
- [[wiki/topics/Frontend Development]]
- [[wiki/syntheses/React UI Organization Model]]
- [[wiki/sources/React Hooks useRef useContext useMemo Source Guide]]
- [[wiki/sources/React Framework Background and Core Concepts Source Guide]]
