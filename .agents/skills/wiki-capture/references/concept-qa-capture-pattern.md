# Concept Q&A Capture Pattern

Use this pattern when a user invokes `wiki-capture` after a short explanatory Q&A about a concept pair, distinction, or related concept cluster.

## When it applies

- The conversation is mostly teaching/explanation rather than implementation.
- The user manually invoked wiki-capture, so err toward preserving the conceptual structure.
- The durable value is the distilled concept, not the fact that the user asked questions.

## Capture shape

Prefer `type=concept` when the result defines what something is and how it relates to adjacent concepts.

Prefer `type=topic` when the user asked an operational “how to” question and the durable artifact is a reusable procedure, workflow, or method page rather than a single concept definition. This is especially true when an existing topic/map cluster already exists for that domain; extend the cluster with a topic page instead of forcing the content into `concepts/`.

Write the page as declarative knowledge in the source/user language. For Chinese explanatory discussions, write Chinese wiki prose and confirm in Chinese.

Useful concept sections:

- `# <Concept Pair / Concept Name>`
- `## What It Is` — definition and core distinction
- `## How It Works` — mechanism, use, or analytic role
- `## Concept Cluster` — adjacent concepts and relation chains
- `## When to Use` — which analytic lens to apply when
- `## Related` — links to at least two existing pages

Useful topic/procedure sections:

- `# <Procedure / Method Name>`
- `## Core Formula` — compact operating model if one emerged
- `## Principle` — the main decision rule behind the method
- `## Operating Flow` — numbered reusable workflow
- `## Quality Checks` — how to tell the method worked
- `## Common Failure Modes` — predictable mistakes and boundaries
- `## Related` — existing map/topic/concept links

## Good transformation

Do not preserve the chat sequence. Convert:

- “What is X?”
- “What is its role?”
- “What related concepts exist?”

to:

- definition
- analytic function
- surrounding concept map
- decision rule for when to use the concept

## Tracking updates

Full capture still updates the normal vault tracking files:

- add the new concept to `index.md`
- append a `CAPTURE type=concept` row to `log.md`
- add a recent activity line and, if useful, an active-thread/key-takeaway entry to `hot.md`

## Iterative concept-chain captures

When the user invokes `wiki-capture` repeatedly during one conceptual thread, treat the captures as a growing concept chain, not isolated pages.

- If a new concept extends or generalizes an earlier captured concept from the same session, link them both ways when appropriate: add the new page to the earlier page's `Related`, and include the earlier page in the new page's `Related`.
- Preserve existing uncommitted tracking entries from previous captures. Re-read dirty shared files before patching, then append only the minimal new `index.md`, `log.md`, `hot.md`, and map entries for the current capture.
- Do not reorder, rewrite, or collapse neighboring recent entries unless the current capture explicitly updates their substance.
- In the confirmation, mention when shared tracking files already contained pre-existing dirty changes and that the current capture was kept logically separable.

If `QMD_WIKI_COLLECTION` is unset, report `QMD skipped: QMD_WIKI_COLLECTION unset`; do not treat that as a failure.
