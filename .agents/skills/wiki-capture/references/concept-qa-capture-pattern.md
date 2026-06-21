# Concept Q&A Capture Pattern

Use this pattern when a user invokes `wiki-capture` after a short explanatory Q&A about a concept pair, distinction, or related concept cluster.

## When it applies

- The conversation is mostly teaching/explanation rather than implementation.
- The user manually invoked wiki-capture, so err toward preserving the conceptual structure.
- The durable value is the distilled concept, not the fact that the user asked questions.

## Capture shape

Prefer `type=concept` when the result defines what something is and how it relates to adjacent concepts.

Write the page as declarative knowledge in the source/user language. For Chinese explanatory discussions, write Chinese wiki prose and confirm in Chinese.

Useful sections:

- `# <Concept Pair / Concept Name>`
- `## What It Is` — definition and core distinction
- `## How It Works` — mechanism, use, or analytic role
- `## Concept Cluster` — adjacent concepts and relation chains
- `## When to Use` — which analytic lens to apply when
- `## Related` — links to at least two existing pages

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

If `QMD_WIKI_COLLECTION` is unset, report `QMD skipped: QMD_WIKI_COLLECTION unset`; do not treat that as a failure.
