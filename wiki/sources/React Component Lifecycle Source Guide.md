---
title: >-
  React Component Lifecycle Source Guide
category: sources
tags:
  - article
  - frontend
  - architecture
sources:
  - conversation:2026-05-12
created: 2026-05-12T20:56:53+08:00
updated: 2026-05-12T20:56:53+08:00
summary: >-
  这页保存一份中文 React 组件生命周期讲解，把 mount、render/update、unmount 放在 UI 树存在关系与 Hooks 持久化结构下理解。
provenance:
  extracted: 0.86
  inferred: 0.13
  ambiguous: 0.01
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-05-12
---
# React Component Lifecycle Source Guide

> Source: 当前对话中的中文 React 组件生命周期讲解：组件何时 mount、何时 unmount，以及一个生命周期内为什么可以多次 render。

## Capture Policy

这页保留 source 层内容，不压缩成简短摘要。它保存的是一份可直接复读的中文讲解材料：生命周期尺度、render/update 与 mount/unmount 的区别、条件渲染、列表 key、effect 清理函数，以及与 `useState`、`useRef`、`useMemo` 的关系。

这份材料不直接替代 [[wiki/concepts/React]]、[[wiki/concepts/State Management]] 或 [[wiki/syntheses/React UI Organization Model]]；它更适合作为 React 生命周期入门理解的来源层，后续可以从中提炼更稳定的组件生命周期概念页或 React reconciliation / key 机制页。^[inferred]

## What It Covers

这份讲解围绕一个核心问题展开：React 组件的“生命周期”不是一次函数调用，也不是一次渲染，而是组件从进入 UI 树到离开 UI 树的整段存在期。

核心区分是：

1. `mount`：组件从“不在 UI 树里”变成“在 UI 树里”。
2. `render/update`：组件已经在 UI 树里，只是 props、state 或 context 变化，需要重新计算 UI。
3. `unmount`：组件从“在 UI 树里”变成“不在 UI 树里”。

因此，一个组件在同一个生命周期内可以 render 多次。生命周期是存在期，render 是这段存在期里的重复计算。

## Preserved Content

### 组件生命周期不是一次渲染

React 组件的生命周期不是：

```text
创建一次 → 渲染一次 → 销毁
```

更准确的结构是：

```text
挂载 mount → 多次渲染 render/update → 卸载 unmount
```

一个组件实例的一生可以理解成：

1. 挂载：组件第一次出现在页面上。
2. 渲染：React 执行组件函数，得到 JSX / UI 描述。
3. 提交：React 把结果更新到真实 DOM。
4. 副作用：`useEffect` 在渲染提交后执行。
5. 更新：props / state / context 变化后，再次渲染。
6. 卸载：组件从页面移除，相关状态槽、ref、effect 清理逻辑结束。

所以：

```text
一个生命周期 = 从 mount 到 unmount 的整段时间
一次 render = 生命周期中的一次“重新计算 UI”
```

两者不是同一个尺度。

### 一个生命周期内可以多次 render

函数组件可以用这个例子理解：

```jsx
function Counter() {
  const [count, setCount] = useState(0)

  console.log('render')

  return (
    <button onClick={() => setCount(count + 1)}>
      {count}
    </button>
  )
}
```

第一次显示组件：

```text
mount
render count = 0
commit DOM
```

点击按钮一次：

```text
setCount(1)
render count = 1
commit DOM
```

再点击一次：

```text
setCount(2)
render count = 2
commit DOM
```

这些 render 仍然发生在同一个组件生命周期里。组件没有被卸载，只是在同一个生命周期中经历了多次 UI 重新计算。

这与 [[wiki/sources/React Hooks useState useEffect Source Guide]] 中的核心前提一致：React 组件每次渲染，函数都会重新执行。`useState` 保存跨渲染状态，并通过 `setState` 触发下一次渲染。

### 函数组件重新执行不等于重新 mount

函数组件不是传统意义上一直运行的对象实例方法。它更像：React 保存组件背后的状态槽；每次需要更新 UI 时，重新调用组件函数；再把这次函数返回的 UI 描述与上一次结果比较、提交。

普通局部变量会被重置：

```jsx
function Demo() {
  let x = 0
}
```

每次 render，`x` 都重新从 `0` 开始。

但 React 管理的结构可以跨 render 保留：

```jsx
const [count, setCount] = useState(0)
const ref = useRef(null)
const value = useMemo(() => compute(), [deps])
```

这些东西不是靠函数局部变量自然保留，而是靠 React 在这个组件实例背后保存。

### 什么时候 mount

当 React 决定“这个组件现在应该出现在 UI 树里”，并且它之前不存在时，组件就会 mount。

常见场景包括：

#### 应用第一次渲染

```jsx
root.render(<App />)
```

`App` 第一次进入 React 树，`App` mount。

如果 `App` 里面有：

```jsx
function App() {
  return <Counter />
}
```

那么 `Counter` 也会第一次 mount。

#### 条件渲染从 false 变成 true

```jsx
function App() {
  const [show, setShow] = useState(false)

  return (
    <>
      <button onClick={() => setShow(true)}>show</button>
      {show && <Panel />}
    </>
  )
}
```

一开始 `show = false`，`Panel` 不在 UI 树里。点击后 `show = true`，React 第一次看到这里需要一个 `Panel`，于是 `Panel mount`。

#### 列表里新增一个 key

```jsx
{items.map(item => (
  <TodoItem key={item.id} item={item} />
))}
```

如果新增一个 `id = 3` 的 item，React 发现列表里多了一个以前没有的 key，于是对应的 `TodoItem` mount。

#### key 变化导致新组件

```jsx
<Profile key={userId} userId={userId} />
```

如果 `userId` 从 `1` 变成 `2`，React 会认为旧的 `key=1` 的 `Profile` 不再是同一个组件，新的 `key=2` 的 `Profile` 是另一个组件。

这通常表现为：

```text
旧 Profile unmount
新 Profile mount
```

这也是有时故意使用 `key` 来重置组件状态的原因。^[inferred]

### 什么时候 unmount

当 React 决定“这个组件不应该继续留在 UI 树里”时，组件就会 unmount。

常见场景包括：

#### 条件渲染从 true 变成 false

```jsx
{show && <Panel />}
```

如果原来 `show = true`，`Panel` 已经 mount。后来 `show = false`，React 发现这里不再需要 `Panel`，于是 `Panel unmount`。

#### 父组件卸载，子组件一起卸载

```jsx
{showPage && <Page />}
```

如果 `Page` 被移除，那么 `Page` 里面的子组件也会一起 unmount。

```jsx
function Page() {
  return (
    <>
      <Header />
      <Content />
    </>
  )
}
```

`Page` unmount 时，`Header`、`Content` 也会 unmount。

#### 列表里删除一个 key

```jsx
{items.map(item => (
  <TodoItem key={item.id} item={item} />
))}
```

如果某个 `item.id` 从列表里消失，对应的 `TodoItem` unmount。

#### key 改变

```jsx
<Profile key={userId} userId={userId} />
```

`userId` 变化时，旧组件可能 unmount，新组件 mount。这里不是普通更新，而是身份被 key 切换。

### update/render 不是 mount，也不是 unmount

重新渲染不等于重新 mount。

```jsx
function Counter() {
  const [count, setCount] = useState(0)

  return <button onClick={() => setCount(count + 1)}>{count}</button>
}
```

点击按钮时：

```text
setCount
重新执行 Counter
更新 UI
```

这只是 update/render，不是重新 mount。

组件仍然是同一个组件实例，它的 `useState` 状态槽、`useRef` 盒子、`useMemo` 缓存结构仍然留在 React 管理的组件身份下面。

可以压成一张表：

| 状态 | 含义 |
|---|---|
| mount | 组件从“不在树里”变成“在树里” |
| update/render | 组件已经在树里，只是 props/state/context 变了，要重新计算 UI |
| unmount | 组件从“在树里”变成“不在树里” |

### useEffect 如何观察 mount 与 unmount

`useEffect` 与生命周期的关系可以这样理解：effect 不是 render 本身，而是在 render commit 之后执行的副作用。

空依赖数组的 effect：

```jsx
useEffect(() => {
  console.log('mounted')
}, [])
```

会在组件首次挂载后执行一次。这个模式经常用来观察 mount。

如果返回清理函数，就能观察 unmount：

```jsx
useEffect(() => {
  console.log('mount')

  return () => {
    console.log('unmount')
  }
}, [])
```

这段的含义是：

```text
组件 mount 后：执行 effect
组件 unmount 时：执行 cleanup
```

但 cleanup 不只在 unmount 时执行。[[wiki/sources/React Hooks useState useEffect Source Guide]] 中已经指出，清理函数会在两个时候执行：

1. 组件卸载时。
2. effect 下一次重新执行前。

例如：

```jsx
useEffect(() => {
  const socket = new WebSocket(url)

  return () => {
    socket.close()
  }
}, [url])
```

这里：

- 组件第一次 mount 后，创建 socket。
- 如果 `url` 变了，不一定是组件 unmount；但旧 effect 会先 cleanup，关闭旧 socket，然后重新执行 effect，创建新 socket。
- 如果组件真的 unmount，也会 cleanup。

### 和常用 Hooks 放在一起看

`useState`：跨渲染保存状态，并触发 UI 更新。

`useRef`：跨渲染保存可变值，但不触发渲染。

`useMemo`：缓存计算结果；依赖不变时复用，依赖变化时重新计算。

`useEffect`：渲染提交后执行副作用；依赖决定执行次数；cleanup 负责清理副作用。

这些 Hook 都依附于同一个组件身份。只要组件没有 unmount，它们背后的状态槽、ref 盒子和 memo 缓存就可以跨多次 render 保留。组件 unmount 后，这些结构随组件身份一起结束。

### 最简模型

```text
第一次出现在 UI 树里
  => mount

还在 UI 树里，只是数据变了
  => render/update

从 UI 树里消失
  => unmount
```

如果要判断当前发生的是 update 还是 remount，关键看组件在 React 树中的身份是否仍然被认为是同一个：位置、组件类型和 key 共同影响这个判断。^[inferred]

## Integration Decisions

这份 source guide 应保留在来源层，因为它是一份中文教学材料，价值在于用连续问题把 React 生命周期、函数组件反复执行、状态槽、effect cleanup 和 key 身份串成同一个解释顺序。

可提升到稳定知识层的内容包括：

- React 组件生命周期是组件身份从 mount 到 unmount 的存在期，而不是一次 render。
- 一个组件生命周期内可以发生多次 render/update。
- mount/unmount 的核心判据是组件是否进入或离开 UI 树。
- update/render 的核心判据是同一组件身份仍在树中，只是 props/state/context 变化。
- `key` 会影响组件身份判断，key 改变常用于强制重置组件状态。^[inferred]
- `useEffect` 的 cleanup 既会在 unmount 时执行，也会在 effect 下一次重新执行前执行。

这些判断可以连接到 [[wiki/concepts/State Management]]，因为生命周期决定状态槽、ref、memo 缓存何时保留、何时被销毁。它们也连接到 [[wiki/syntheses/React UI Organization Model]]，因为 React 的声明式渲染和组件边界最终依赖组件身份、更新传播和副作用清理来维持可理解性。^[inferred]

## Open Questions

- 是否需要建立单独的 `React Component Lifecycle` 概念页，把 mount、update、unmount、effect cleanup 和 key 身份机制提升成稳定模型？
- React reconciliation 中“同位置同类型同 key 复用组件身份”的规则，是否需要单独整理成 source guide 或概念页？
- `useLayoutEffect`、Strict Mode 下开发环境的重复执行、Concurrent Rendering 对生命周期心智模型的影响，是否需要后续补充？

## Related

- [[wiki/concepts/React]]
- [[wiki/concepts/State Management]]
- [[wiki/topics/Frontend Development]]
- [[wiki/syntheses/React UI Organization Model]]
- [[wiki/sources/React Hooks useState useEffect Source Guide]]
- [[wiki/sources/React Hooks useRef useContext useMemo Source Guide]]
