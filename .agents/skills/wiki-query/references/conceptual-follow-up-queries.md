# Conceptual follow-up queries

Use this when the user asks a short conceptual follow-up after a wiki-query answer, especially in the same topic cluster (for example: after asking about React `useMemo`/`useRef`, they ask about component lifecycle).

## Pattern

- Treat the follow-up as a normal wiki query, but seed candidate ranking from pages already consulted in the same conversation.
- Reuse the current vault path and recently read `hot.md`/`index.md` when they are still in context; do not spend extra reads re-discovering the same vault unless the session context is unclear.
- Do a focused section read or small offset read in the already-identified source pages before broad grep.
- Still append the Step 6 query log entry for each user question.

## Answering style

- Preserve the source language. If the source pages and user question are Chinese, answer in Chinese.
- For teaching-style conceptual answers, prefer a compact lifecycle/sequence model plus one small code example.
- Make scale distinctions explicit when the confusion is about scope, e.g. “组件生命周期 = mount 到 unmount；render = 生命周期内的一次 UI 计算”。
- Keep citations to the wiki pages actually consulted and state gaps when the wiki lacks a stable concept page.

## Pitfall

Do not flatten follow-up conceptual questions into generic framework knowledge. Use the wiki source pages as grounding, then synthesize the model in plain language.