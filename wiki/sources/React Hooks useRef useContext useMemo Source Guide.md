---
title: >-
  React Hooks useRef useContext useMemo Source Guide
category: sources
tags:
  - article
  - frontend
  - architecture
sources:
  - conversation:2026-05-12
created: 2026-05-12T15:50:12+08:00
updated: 2026-05-12T15:50:12+08:00
summary: >-
  这页保存一份中文 React Hooks 讲解，把 useRef、useContext、useMemo 放在函数组件反复执行的共同框架下理解。
provenance:
  extracted: 0.92
  inferred: 0.07
  ambiguous: 0.01
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-05-12
---
# React Hooks useRef useContext useMemo Source Guide

> Source: 当前对话中的中文 React Hooks 讲解：useRef、useContext、useMemo 的共同框架

## Capture Policy

这页保留 source 层内容，不翻译，不压缩成简短摘要。它保存的是一份可直接复读的中文讲解材料：核心心智模型、判断标准、代码例子、注意事项和三者对照。

这份材料不直接替代 [[wiki/concepts/React]]、[[wiki/concepts/State Management]] 或 [[wiki/syntheses/React UI Organization Model]]；它更适合作为 React Hooks 入门理解的来源层，后续可以从中提炼更稳定的 Hooks 概念页或 React 状态传播模型。^[inferred]

## What It Covers

这份讲解把 `useRef`、`useContext`、`useMemo` 放在一个共同框架里理解：

React 组件每次渲染，函数都会重新执行。

所以核心问题是：

1. 有些值我想“跨渲染保留”，但不想触发重新渲染 → `useRef`
2. 有些值我想“跨组件共享”，避免层层传 props → `useContext`
3. 有些计算我不想每次渲染都重新算 → `useMemo`

一句话：

- `useRef` 管“可变容器”
- `useContext` 管“跨层共享”
- `useMemo` 管“缓存计算结果”

这个共同框架补充了 [[wiki/topics/Frontend Development]] 中关于状态、渲染和组件协作的长期问题：前端复杂性不只是“页面怎么写”，而是数据如何跨渲染、跨组件、跨计算过程保持可理解。^[inferred]

## Preserved Content

### 共同底层前提：函数组件会反复执行

React 函数组件不是传统意义上的实例对象。组件每次渲染时，组件函数都会重新执行。

因此：

```jsx
function Component() {
  const x = {}
}
```

每次渲染，`x` 都是一个新对象。

```jsx
function Component() {
  const result = expensive()
}
```

每次渲染，`expensive` 都会重新执行。

```jsx
function Component() {
  let value = 0
}
```

每次渲染，`value` 都重新从 `0` 开始。

于是 React 提供三种机制：

- `useRef`：让某个值逃过函数重新执行的重置
- `useMemo`：让某个计算逃过不必要的重复执行
- `useContext`：让某个值逃过 props 层层传递

它们本质上都在处理 React 函数组件的一个核心事实：

组件函数不是实例对象，它会反复执行。Hook 是 React 给函数组件补上的“持久化结构”。

### useRef：保存一个不会触发渲染的可变值

最常见形式：

```jsx
const ref = useRef(initialValue)
```

它返回一个对象：

```js
{
  current: initialValue
}
```

可以读写：

```js
ref.current = xxx
```

重点是：修改 `ref.current` 不会导致组件重新渲染。

这和 `useState` 最大区别：

```jsx
const [count, setCount] = useState(0)
```

`setCount(1)` 会触发重新渲染。

但：

```jsx
const countRef = useRef(0)
countRef.current = 1
```

不会触发重新渲染。

所以 `useRef` 适合保存：

1. DOM 节点引用
2. 定时器 ID
3. 上一次的值
4. 某些不参与 UI 渲染的状态
5. 避免闭包拿到旧值

#### 例子 1：操作 DOM

```jsx
function InputFocus() {
  const inputRef = useRef(null)

  function focusInput() {
    inputRef.current.focus()
  }

  return (
    <>
      <input ref={inputRef} />
      <button onClick={focusInput}>Focus</button>
    </>
  )
}
```

这里 `inputRef.current` 指向真实 DOM 节点。

#### 例子 2：保存定时器 ID

```jsx
function Timer() {
  const timerRef = useRef(null)

  function start() {
    timerRef.current = setInterval(() => {
      console.log('tick')
    }, 1000)
  }

  function stop() {
    clearInterval(timerRef.current)
  }

  return (
    <>
      <button onClick={start}>Start</button>
      <button onClick={stop}>Stop</button>
    </>
  )
}
```

`timerRef.current` 改变，不需要让页面重渲染。

#### useRef 的心智模型

`useRef` 像组件实例上的一个小盒子。

组件重新渲染时，函数会重新执行，但这个盒子还在。

```jsx
function Demo() {
  const ref = useRef(0)

  ref.current++

  console.log(ref.current)
}
```

每次渲染，`ref.current` 会保留之前的值，而不是重新变成 `0`。

#### useRef 的注意点

不要用 `useRef` 存储需要显示到页面上的数据。

```jsx
function Counter() {
  const countRef = useRef(0)

  return (
    <>
      <div>{countRef.current}</div>
      <button onClick={() => countRef.current++}>+</button>
    </>
  )
}
```

点按钮后，`countRef.current` 确实变了，但页面不会更新。

如果 UI 依赖它，就应该用 `useState`。

判断标准：

- 需要驱动 UI 更新 → `useState`
- 只是跨渲染保存一个可变值 → `useRef`

### useContext：跨组件共享数据

React 默认是单向数据流：

父组件 → 子组件 → 孙组件

如果孙组件需要父组件的数据，传统方式是 props 一层层传：

```jsx
<App user={user}>
  <Page user={user}>
    <Header user={user}>
      <Avatar user={user} />
```

这叫 props drilling，props 逐层下钻。

`useContext` 解决的是：不想中间组件都帮忙转发数据。

基本用法：

```jsx
const ThemeContext = createContext(defaultValue)

function App() {
  return (
    <ThemeContext.Provider value="dark">
      <Page />
    </ThemeContext.Provider>
  )
}

function Page() {
  return <Header />
}

function Header() {
  const theme = useContext(ThemeContext)
  return <div>{theme}</div>
}
```

`Header` 没有从 `Page` 接收 props，但能拿到 `ThemeContext.Provider` 提供的 `value`。

#### useContext 的心智模型

Context 像一个“作用域变量”。

Provider 提供值。
`useContext` 消费离自己最近的 Provider 的值。

例如：

```jsx
<ThemeContext.Provider value="dark">
  <A />
  <ThemeContext.Provider value="light">
    <B />
  </ThemeContext.Provider>
</ThemeContext.Provider>
```

`A` 拿到 `dark`。
`B` 拿到 `light`。

#### useContext 的常见使用场景

1. 主题 `theme`
2. 当前登录用户 `user`
3. 国际化语言 `locale`
4. 权限信息 `auth`
5. 全局配置 `config`
6. 轻量级全局状态

例子：

```jsx
const UserContext = createContext(null)

function App() {
  const user = { name: 'Alice' }

  return (
    <UserContext.Provider value={user}>
      <Profile />
    </UserContext.Provider>
  )
}

function Profile() {
  const user = useContext(UserContext)

  return <div>{user.name}</div>
}
```

#### useContext 的注意点

Context 不是万能状态管理。

因为 Provider 的 `value` 变了，所有消费这个 Context 的组件都会重新渲染。

例如：

```jsx
<UserContext.Provider value={{ name: 'Alice' }}>
  <Profile />
</UserContext.Provider>
```

这里每次 `App` 渲染，都会创建一个新的对象：

```js
{ name: 'Alice' }
```

即使内容一样，引用也不一样。

所以可能导致额外渲染。

常见优化是配合 `useMemo`：

```jsx
const user = useMemo(() => ({ name: 'Alice' }), [])

<UserContext.Provider value={user}>
  <Profile />
</UserContext.Provider>
```

判断标准：

- 如果只是父子传值 → props 就够了
- 如果很多层都要用，且中间组件只是转发 → `useContext`
- 如果是复杂、高频、细粒度状态 → 考虑 Zustand / Redux / Jotai 等状态库

### useMemo：缓存一个计算结果

基本形式：

```jsx
const memoizedValue = useMemo(() => {
  return expensiveCalculation(a, b)
}, [a, b])
```

意思是：

只有当 `a` 或 `b` 变化时，才重新执行 `expensiveCalculation`。
否则复用上一次的结果。

例子：

```jsx
function ProductList({ products, keyword }) {
  const filteredProducts = useMemo(() => {
    return products.filter(p => p.name.includes(keyword))
  }, [products, keyword])

  return (
    <ul>
      {filteredProducts.map(p => (
        <li key={p.id}>{p.name}</li>
      ))}
    </ul>
  )
}
```

如果组件因为其他 state 变化而重新渲染，但 `products` 和 `keyword` 没变，那么过滤逻辑不会重新执行。

#### useMemo 的心智模型

`useMemo` 是“渲染期间的计算缓存”。

它缓存的是值，不是函数。

对比：

```jsx
const value = compute()
```

每次渲染都算。

```jsx
const value = useMemo(() => compute(), [deps])
```

`deps` 不变，就不重新算。

#### useMemo 的常见场景

1. 昂贵计算
2. 大数组 `filter` / `map` / `sort`
3. 避免创建新的对象引用
4. 配合 `React.memo` 减少子组件渲染
5. 稳定 Context Provider 的 `value`

#### 例子：稳定对象引用

```jsx
function App() {
  const [theme, setTheme] = useState('dark')

  const config = useMemo(() => {
    return {
      theme,
      version: '1.0'
    }
  }, [theme])

  return <ConfigContext.Provider value={config}>...</ConfigContext.Provider>
}
```

如果不用 `useMemo`：

```jsx
const config = {
  theme,
  version: '1.0'
}
```

每次 `App` 渲染都会创建新对象，导致 Context 消费者可能跟着重新渲染。

#### useMemo 的注意点

不要滥用 `useMemo`。

因为 `useMemo` 本身也有成本：

1. React 要保存上一次结果
2. 要比较依赖数组
3. 代码复杂度增加

所以简单计算没必要：

```jsx
const fullName = firstName + lastName
```

不需要：

```jsx
const fullName = useMemo(() => firstName + lastName, [firstName, lastName])
```

判断标准：

- 计算很便宜 → 不用 `useMemo`
- 计算很贵，且依赖不常变 → `useMemo`
- 需要稳定对象/数组引用 → `useMemo`
- 只是为了“看起来性能更好” → 不要用

### 三者对比

可以这样记：

`useRef`：

- 保存一个“可变盒子”
- 变了不渲染
- 主要解决“跨渲染保存值”的问题

`useContext`：

- 读取一个“上层作用域共享值”
- Provider 变了，消费者更新
- 主要解决“跨组件传值”的问题

`useMemo`：

- 保存一个“计算结果缓存”
- 依赖不变就复用
- 主要解决“重复计算/引用不稳定”的问题

| Hook | 解决什么问题 | 改变后是否触发渲染 |
|---|---|---|
| `useRef` | 保存可变值 / DOM 引用 | 不会 |
| `useContext` | 跨组件共享数据 | Provider value 变化会 |
| `useMemo` | 缓存计算结果 | 不主动触发，只影响渲染期间计算 |

### 一个组合例子

```jsx
const ThemeContext = createContext(null)

function App() {
  const inputRef = useRef(null)
  const [theme, setTheme] = useState('dark')

  const contextValue = useMemo(() => {
    return {
      theme,
      toggleTheme: () => {
        setTheme(t => (t === 'dark' ? 'light' : 'dark'))
      }
    }
  }, [theme])

  function focusInput() {
    inputRef.current.focus()
  }

  return (
    <ThemeContext.Provider value={contextValue}>
      <input ref={inputRef} />
      <button onClick={focusInput}>Focus input</button>
      <Toolbar />
    </ThemeContext.Provider>
  )
}

function Toolbar() {
  const { theme, toggleTheme } = useContext(ThemeContext)

  return (
    <div>
      <div>Current theme: {theme}</div>
      <button onClick={toggleTheme}>Toggle theme</button>
    </div>
  )
}
```

这里：

- `useRef` 保存 input DOM 节点。
- `useContext` 让 `Toolbar` 拿到 `theme`。
- `useMemo` 缓存 `contextValue`，避免每次渲染都创建新对象。

### 一句话总结

`useRef` 是“我想记住一个东西，但它变化不该刷新页面”。

`useContext` 是“我想让很多组件共享一个东西，但不想一层层传 props”。

`useMemo` 是“我想复用一个计算结果，只在依赖变化时重新计算”。

## Integration Decisions

这份 source guide 应保留在来源层，因为它是一份完整的中文教学材料，价值在于例子、判断标准和底层框架共同构成的解释顺序，而不只是几个抽象结论。

可提升到稳定知识层的内容包括：

- React 函数组件每次渲染都会重新执行，因此 Hooks 是函数组件的“持久化结构”。^[inferred]
- `useRef` 处理“跨渲染保留但不驱动 UI 更新”的可变容器问题。
- `useContext` 处理“跨组件共享但不逐层转发 props”的作用域共享问题。
- `useMemo` 处理“依赖不变时复用渲染期间计算结果”的缓存问题。
- Context 的 Provider `value` 引用变化会造成消费者更新，因此 `useMemo` 常用于稳定对象引用。

这些判断可以连接到 [[wiki/concepts/State Management]]，因为它们都在回答状态、引用、计算和 UI 更新之间的传播边界。它们也连接到 [[wiki/syntheses/React UI Organization Model]]，因为 React 的组件化、声明式渲染和状态驱动更新需要具体 Hooks 机制来落地。^[inferred]

## Open Questions

- 是否需要建立单独的 `React Hooks` 概念页，把 `useState`、`useEffect`、`useRef`、`useContext`、`useMemo` 放入同一个状态与生命周期模型？
- `useMemo` 与 `useCallback` 的边界是否应该单独整理，尤其是“缓存值”与“缓存函数引用”的区别？
- React Context 与 Zustand / Redux / Jotai 等状态库之间的适用边界，是否需要在 [[wiki/concepts/State Management]] 下继续展开？

## Related

- [[wiki/concepts/React]]
- [[wiki/concepts/State Management]]
- [[wiki/topics/Frontend Development]]
- [[wiki/syntheses/React UI Organization Model]]
- [[wiki/sources/React Framework Background and Core Concepts Source Guide]]
