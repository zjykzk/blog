# 风险规则生成的第一性原理资料

- `explanation.md`：带学术参考的说明，也是 HTML 图解的内容源。
- `sources.jsonl`：五项文献的作者、版本、公开链接与核验时间。
- `evidence.jsonl`：引文、原文位置、支持的论点与适用边界。

`sources/` 保存本地下载与文本提取缓存，不进入版本控制。
来源清单中的 `local_text` 和 `sha256` 描述核验时的本机文本快照。
阅读说明与追溯文献可使用公开链接、引文和定位信息，无需该缓存。

规范知识页位于 [[wiki/syntheses/LLM Risk Rule Discovery]]。
