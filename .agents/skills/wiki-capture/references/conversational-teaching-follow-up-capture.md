# Conversational Teaching Follow-up Capture

Use this pattern when a prior wiki-query or teaching exchange turns into a coherent tutorial through several follow-up questions, especially around a technical concept that already has adjacent source guides.

## Trigger

- The user asks a sequence of clarifying questions after a wiki-query answer.
- The exchange builds a reusable explanation rather than a one-off answer.
- Existing source guides cover neighboring material, but the new exchange adds a missing conceptual layer.

Example shape: existing React Hooks source guides cover `useState`, `useEffect`, `useRef`, and `useMemo`; follow-up questions develop the missing layer of component lifecycle: mount, repeated render/update, unmount, `key` identity, and effect cleanup.

## Capture choice

Default to `source` when the value is the teaching sequence itself: examples, mental models, contrasts, and common misconceptions. Do not force it into a concept page unless the user explicitly asks for a distilled concept.

When the user explicitly asks to preserve the original record (for example “记得保留原始记录”), make the source guide the first-class artifact and include a dedicated preserved-record section that keeps the original question ladder and key answer phrasing in source language. Then add a separate structured section for reusable knowledge; do not let the structured section replace the preserved record.

If the user later agrees that the teaching exchange should become a reusable framework or asks to “做合成”, create a companion `syntheses/` page rather than overwriting the source guide. Link both ways: the source guide should point to the synthesis as the promoted model, and the synthesis should cite the source guide as provenance.

Use a title like `<Topic> Source Guide` that matches the surrounding source-guide family, even if the body is in Chinese and the title uses an English technical term.

## Body structure

Preserve the question ladder as declarative tutorial sections, not as chat transcript:

1. The central distinction.
2. Minimal model / diagram.
3. Code examples that expose the distinction.
4. Common cases and counterexamples.
5. Relationship to existing pages.
6. Open questions for future promotion.

When the user explicitly asks to preserve the original record (for example “记得保留原始记录”), add a compact `原始问题链` or `原始记录保留` subsection before the polished tutorial. Keep the user questions in order and retain the answer spine in the original language, but avoid raw transcript noise such as tool calls, confirmations, and repeated logistics.

For React lifecycle-style material, a good preserved structure is:

- lifecycle is mount-to-unmount existence, not one render
- render/update can happen many times inside one lifecycle
- mount happens when a component first enters the UI tree
- unmount happens when it leaves the UI tree
- props/state/context changes normally trigger update, not remount
- `key` changes can reset component identity
- effect cleanup runs on unmount and before the next effect execution

## Tracking

Update `index.md`, `hot.md`, `log.md`, and the relevant domain map. If the page belongs to an existing source-guide cluster, place it near neighboring pages in `index.md` and the map so the cluster is visible.

When a preceding wiki-query already appended `QUERY` entries to `log.md`, leave them in place and add the `CAPTURE` entry after them; the capture is a later action in the same knowledge flow.
