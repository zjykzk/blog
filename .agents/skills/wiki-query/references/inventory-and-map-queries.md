# Inventory and map-style wiki queries

Session pattern: user asked `有哪些『机制模型』`, then continued with `goon` / `很好，请继续`.

Useful retrieval pattern:

1. Treat the question as an inventory/synthesis query, not a factual lookup. The target term may not exist as a page title.
2. Read `hot.md` and `index.md` first for recent clusters and canonical page inventory.
3. Search frontmatter summaries/titles/tags for broad terms related to the requested class, not only the exact phrase. For Chinese conceptual inventories, include English and Chinese variants, e.g. `机制|模型|model|mechanism|feedback|system|loop|结构`.
4. Use section/full reads only on the top cluster representatives, not every candidate.
5. Synthesize as a map grouped by the generative question each page answers, e.g.:
   - 世界如何生成结果
   - 人如何认识世界
   - 人如何行动
   - 组织如何失真或学习
   - 软件如何从需求收缩到结构
   - AI agent 如何被 harness 成可靠行为
6. If no canonical map/concept page exists, state the gap and suggest creating one, but only after presenting the discovered cluster.

Answer shape that worked well:

- Start with `Based on the wiki:`.
- Define the queried class in the user's language.
- Group pages into 6-10 conceptual buckets, each with `[[wikilinks]]` and a compact mechanism sentence.
- Then provide a cross-cutting template or total chain that converts the inventory into a reusable thinking tool.
- For Chinese user/source material, write the synthesis in Chinese.

Example compression from the session:

`机制模型 = 变量 + 关系 + 约束 + 反馈 + 时间 + 杠杆点`

`机制模型是解释一个结果为什么会反复长出来，并指出从哪里改才能让它不再这样长出来的结构。`
