# Long Course / Lecture Source Capture

Use when the user invokes wiki-capture with a long pasted course chapter, lecture note, workshop handout, or tutorial-style artifact.

## Capture stance

- Default to `source`, not `concept`, unless the user explicitly asks for distillation.
- Preserve the source language in title, summary, index entry, hot entry, map entry, and body. For Chinese lectures, prefer a readable Chinese source-guide filename.
- Treat the pasted material as a reusable reading artifact, not as a chat transcript and not as a brief summary.

## What to preserve

Keep the source's teaching sequence and operational artifacts:

- opening story / motivating failure case
- audience framing and decision tables
- pyramids, layered models, or other named structures
- templates and checklists
- example code blocks / diagrams / pseudo-code
- workshop agendas and scripts
- action recommendations
- module/course context when it clarifies where the material fits

Normalize broken copied formatting when needed, but do not compress away the examples that make the source reusable.

## Integration pattern

- Link to at least two existing concept/topic/map pages discovered from `index.md`.
- Add the source to the most relevant map, not only `index.md`; for software architecture course material this is often `CS Map` and/or `Software Design Map`.
- If the guide names future promotable concepts, either create stubs or mention them in plain text without wikilinks.
- In `Integration Decisions`, separate source-level claims from future synthesis candidates.

## Verification emphasis

After writing, verify:

- frontmatter and taxonomy tags
- no broken wikilinks, especially for Chinese filenames and path-qualified links
- `index.md`, `log.md`, `hot.md` entries
- relevant map coverage
