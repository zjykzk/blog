# Chinese source capture with promoted concept

Session pattern: user pasted a long Chinese source article and explicitly said “不用翻译”. The correct capture shape was:

- Classify the pasted article as `source`, not synthesis, because the durable artifact is an external/source-facing reading guide.
- Preserve Chinese in the note body, summaries, hot/index/map updates, and final confirmation.
- Use a faithful Chinese display title, but sanitize unsafe filename punctuation if needed. Example:
  - display title: `内核：你的三个自我 Source Guide`
  - filename: `内核 你的三个自我 Source Guide.md`
  - aliases include the original source title with punctuation: `内核：你的三个「自我」`.
- If the source introduces a central named framework, create a minimal concept page rather than leaving an aspirational broken link. Example: source guide plus `wiki/concepts/三个自我模型.md`.
- Add both the source guide and promoted concept to `index.md`, `log.md`, `hot.md`, and a relevant map such as `Learning Map.md`.
- Verify frontmatter, taxonomy tags, wikilinks, and incoming links after both files and tracking pages are written.

Good controlled tags for this pattern, when available: `article`, `cognition`, `learning`, `thinking`, and a specific technical analogy tag such as `llm` when the source substantially uses AI/LLM comparison.