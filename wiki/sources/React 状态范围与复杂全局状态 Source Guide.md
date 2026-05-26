---
title: >-
  React 状态范围与复杂全局状态 Source Guide
category: sources
tags:
  - article
  - frontend
  - architecture
sources:
  - conversation:2026-05-27
created: 2026-05-27T00:37:25+0800
updated: 2026-05-27T00:37:25+0800
summary: >-
  这页保存一段中文 React 状态管理追问：从 useState/useRef/useContext/useMemo，到复杂全局状态、高频细粒度更新和“全局”范围的判断。
provenance:
  extracted: 0.82
  inferred: 0.16
  ambiguous: 0.02
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-05-27
---
# React 状态范围与复杂全局状态 Source Guide

> Source: 当前对话中的中文 React 状态管理追问：除了 `useMemo` / `useState` 还有什么、复杂全局状态是什么、高频细粒度更新是什么、“全局”到底是什么范围。

## Capture Policy

这页保留 source 层的教学追问，不直接替代 [[wiki/concepts/State Management]]、[[wiki/sources/React Hooks useRef useContext useMemo Source Guide]] 或 [[wiki/sources/React Hooks useState useEffect Source Guide]]。它保存的是一组围绕 React 状态范围、传播范围和更新粒度的解释顺序，后续可以从中提炼“前端状态范围 taxonomy”或“React 状态传播模型”。^[inferred]

## What It Covers

这段教学把 React 状态管理从“有哪些 Hook”推进到“状态的边界在哪里”。核心问题不是只选 `useState`、`useRef`、`useContext`、`useMemo` 或外部状态库，而是判断：

1. 状态是否需要驱动 UI 更新。
2. 状态是否只属于一个组件。
3. 状态是否跨组件共享。
4. 状态是否高频变化。
5. 状态变化是否只应该影响很小一部分 UI。
6. 状态是否需要跨页面、刷新或服务端保存。

这补充了 [[wiki/concepts/State Management]] 中“状态住在哪里、谁能改、变化如何传播”的定义，也补充了 [[wiki/syntheses/React UI Organization Model]] 中 React 作为声明式渲染、组件边界和状态流协同模型的理解。

## Preserved Content

### 原始问题链

这段教学由三个连续追问组成：

1. “状态管理除了 `useMem` & `useState`，还有别的吗？”这里的 `useMem` 被解释为 `useMemo`。
2. “展开下复杂全局状态 / 高频细粒度更新。”
3. “‘全局’是什么范围？”

这三个问题逐步把主题从 Hook 清单推进到状态范围模型。

### 除了 useState 和 useMemo 还有什么

React 函数组件每次渲染都会重新执行，所以不同 Hook 解决的是不同类型的“保存、传播、计算、同步”问题：

| 需求 | 工具 | 核心判断 |
|---|---|---|
| UI 要跟着变化 | `useState` | 状态变化要触发重新渲染 |
| 跨渲染保存，但不刷新 UI | `useRef` | 值要保留，但不参与 UI 输出 |
| 跨组件共享，避免层层传 props | `useContext` | 共享值被子树消费 |
| 缓存昂贵计算或稳定对象引用 | `useMemo` | 依赖不变时复用计算结果 |
| 渲染后同步外部系统 | `useEffect` | 网络、DOM、订阅、localStorage 等副作用不应放在渲染阶段 |
| 复杂全局状态 / 高频细粒度更新 | Zustand / Redux / Jotai 等状态库 | 需要更明确的订阅、更新和治理边界 |

`useEffect` 严格说不是状态管理工具，而是“渲染后同步外部世界”的机制；它常通过 `setState` 把请求结果、订阅结果或外部 API 结果带回 React UI。

### 复杂全局状态

“复杂全局状态”不是“很多组件都要用”这么简单。`theme`、`locale`、`currentUser` 这类低频共享值，很多时候用 `useContext` 就足够。

复杂全局状态通常有这些特征：

- 多个远距离组件都要读写同一份状态。
- 状态之间有派生关系，例如筛选条件、列表、选中项、分页、权限和缓存结果互相影响。
- 更新路径多，不止一个按钮或组件能修改它。
- 有异步过程，例如 loading、error、retry、optimistic update 和回滚。
- 需要调试“是谁在什么时候把状态改了”。
- 局部更新不应该让整棵组件树跟着重渲染。

它对应的不是单个 Hook 问题，而是状态治理问题：状态放在哪里，谁能改，怎么改，变化如何传播，哪些观察者应该被通知。

### 高频细粒度更新

“高频”是状态变化很频繁，“细粒度”是每次变化只应该影响很小一部分 UI。

典型场景包括：

- 输入框每个字符变化。
- 拖拽位置、鼠标移动、滚动位置。
- 实时协作光标。
- 股票价格、监控面板、聊天消息流。
- 大表格里某一行、某一格更新。
- 游戏、画布、时间轴编辑器里的局部状态。

这类问题的关键不是“能不能共享”，而是“一次小变化会不会让太多组件重渲染”。

### 为什么 useContext 不适合复杂高频状态

`useContext` 的边界在于：Provider 的 `value` 变化时，消费这个 Context 的组件会重新渲染。

如果把一个大对象塞进 Context：

```jsx
<AppStateContext.Provider value={{ user, theme, filters, selectedId, items }}>
```

那么 `selectedId` 的变化可能牵动所有消费这个 Context 的组件，即使某个组件只关心 `theme`。这会让状态共享范围和重渲染传播范围绑在一起。

因此 Context 更适合：

- 低频共享。
- 粗粒度共享。
- 相对稳定的环境值。
- 读多写少的配置类状态。

Context 不适合：

- 复杂状态。
- 高频变化。
- 细粒度订阅。
- 多处写入的大型状态对象。

### Zustand / Redux / Jotai 的分工

这段教学没有把 Zustand、Redux、Jotai 展开成完整框架比较，但给出了状态库介入的判断：当状态变成复杂、高频、细粒度状态时，应考虑外部状态层。^[inferred]

#### Redux

Redux 更适合强治理的全局状态。它的核心优势不是“全局”，而是状态变化可追踪、规则明确。它适合业务状态复杂、多处修改同一状态、需要 action/reducer/devtools 追踪变化、团队需要统一状态更新规范的场景。代价是样板代码和心智负担较重，小项目容易过度设计。^[inferred]

#### Zustand

Zustand 更适合轻量 store 加 selector。组件可以只订阅自己关心的 slice，例如：

```js
const count = useStore(s => s.count)
```

这种模型比把整个大对象放进 Context 更容易控制无关渲染。它适合需要全局 store、希望局部订阅、又不想引入 Redux 重治理的中小型复杂状态。^[inferred]

#### Jotai

Jotai 更适合原子化状态。它把状态拆成多个 atom，而不是一个中央大对象；适合状态之间有很多局部组合、希望状态像依赖图一样组合、某些状态只影响少数组件的场景。^[inferred]

### “全局”是什么范围

“全局”不是指整个互联网，也不必然指整个应用所有页面。它是相对于某个边界的全局：某份状态的读写范围超过了单个组件局部边界，需要被多个组件、页面、流程或模块共享。

| 范围 | 例子 | 通常怎么管 |
|---|---|---|
| 组件局部 | 输入框展开/收起、modal open | `useState` |
| 父子局部 | 父组件给子组件传选中项 | props |
| 子树范围 | 一个页面区域里的表单上下文、局部筛选条件 | Context / 局部 store |
| 页面范围 | 一个列表页的筛选、分页、选中项、弹窗状态 | 页面级 store / URL / state |
| 应用范围 | 当前用户、权限、主题、语言、全局通知 | Context / 全局 store |
| 跨页面 / 可恢复范围 | 搜索参数、tab、筛选条件、页面位置 | URL / router state / storage |
| 服务端共享范围 | 用户资料、订单列表、权限、远端缓存 | server state / query cache |

所以同一份状态可能对某个局部是“全局”，但对整个 App 不是全局：

```text
UserProfileCard 内部的 hover 状态
→ 组件局部，不是全局

整个 Settings 页面里的 form draft
→ 对 Settings 页面是全局，但对整个 App 不是全局

currentUser / auth / theme
→ 对整个 App 基本是全局

商品列表查询结果
→ 对前端组件是共享状态，但真实来源在服务端，不应简单当成本地全局状态
```

### 判断顺序

选择状态工具时，可以按这个顺序判断：

| 情况 | 优先方案 |
|---|---|
| 单个组件内部状态 | `useState` |
| 跨渲染保存但不刷新 UI | `useRef` |
| 父传子、层级不深 | props |
| theme / user / locale / auth 这类低频共享 | `useContext` |
| Context value 需要稳定引用 | `useMemo` |
| 多组件共享，且更新频繁 | Zustand / Jotai / Redux |
| 状态变化需要强审计、可回放、团队规范 | Redux |
| 想轻量全局 store + 局部订阅 | Zustand |
| 想拆成很多细粒度状态节点 | Jotai |
| 刷新后还应该保留 | URL / storage / server state |

### 压缩结论

`useState` 管局部 UI 状态，`useRef` 管不触发渲染的跨渲染盒子，`useContext` 管低频共享值，`useMemo` 管渲染期间的计算缓存或引用稳定。状态一旦变成多源修改、异步演化、频繁更新、只想局部重渲染，就进入复杂状态管理问题，应考虑 Zustand、Redux、Jotai 或服务端状态缓存等外部状态层。^[inferred]

“全局”不是绝对范围，而是边界判断：状态的生命周期、读写者和影响范围超过了某个局部边界，它就在那个边界上成为全局状态。

## Integration Decisions

这页应保留为 source guide，因为它保存的是一段连续追问形成的教学路径，而不是单一稳定概念定义。它可以后续提升出两个更稳定页面：

- “前端状态范围 taxonomy”：区分组件局部、子树、页面、应用、URL/storage、服务端状态。
- “React 状态传播模型”：区分共享范围、更新频率、订阅粒度和重渲染传播。

Zustand、Redux、Jotai 的说明目前主要是教学性补充，应保持 source-level，直到 wiki 引入专门材料或实践经验后再提升成独立比较页。^[inferred]

## Open Questions

- 是否需要新增稳定概念页 `Frontend State Scope`，专门保存局部状态、页面状态、应用状态、URL 状态和服务端状态的 taxonomy？
- 是否需要为 Zustand、Redux、Jotai 建立单独 source guides 或概念页？
- React 状态管理是否应连接到 [[wiki/syntheses/信息流与状态流转设计原则]]，把前端状态也纳入更一般的软件状态流转框架？

## Related

- [[wiki/concepts/State Management]]
- [[wiki/concepts/React]]
- [[wiki/syntheses/React UI Organization Model]]
- [[wiki/topics/Frontend Development]]
- [[wiki/topics/Frontend Development Workflow]]
- [[wiki/sources/React Hooks useRef useContext useMemo Source Guide]]
- [[wiki/sources/React Hooks useState useEffect Source Guide]]
- [[wiki/sources/Frontend Development Workflow Roundtable Source Guide]]
