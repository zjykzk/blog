# wiki-query fallback notes — 2026-05-11

Observed during a wiki query from `/Users/zenk/study/wiki`:

- `~/.obsidian-wiki/config` may be absent even though the repo itself contains the canonical vault under `wiki/`.
- `llm-wiki/SKILL.md` may be absent; the query should not fail. Use the fallback primitive order now embedded in `SKILL.md`.
- `search_files` can return unrelated `index.md` files from themes or publishing layers. Prefer the project-context canonical `wiki/index.md` when AGENTS/CLAUDE context says `wiki/` is the stable knowledge layer.
- For conceptual questions like “ICAP 是否适用于所有知识”, a good cheap path is: `hot.md` → `wiki/index.md` → frontmatter grep → targeted section reads of the source guide, learning methodology, knowledge types, and cognitive load pages.

This is not a new standalone skill; it is a robustness note for the class-level `wiki-query` workflow.