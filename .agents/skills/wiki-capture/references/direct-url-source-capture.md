# Direct URL Source Capture Pattern

Use this when the user invokes wiki-capture with a plain web URL rather than pasting the full article text.

## Trigger shape

- User provides a direct URL and asks to capture it, or invokes `/wiki-capture` with only the URL as the instruction.
- The URL resolves to a readable Markdown/text/HTML article, gist, documentation page, idea file, or practitioner note.
- An existing source guide may already cover a secondary interpretation of the same object.

## Recommended workflow

1. Fetch the URL with an actual tool (`curl -L --fail` or the relevant web extraction/browser tool); do not infer the source from memory or from existing secondary notes.
2. Search `index.md` and existing `wiki/sources/` for exact title, URL, author, and central phrase before deciding whether to create, expand, or companion-link a page.
3. If the URL is the primary/source artifact and an existing guide covers commentary or comparison, create a companion primary-source guide instead of overwriting the secondary page. In `Integration Decisions`, explicitly distinguish primary-source claims from commentary-grounded interpretation.
4. Preserve source-level structure: purpose, thesis, architecture/model, operations/workflow, examples/use cases, optional tools, tips, limitations, and rationale. Do not reduce the fetched article to only key points.
5. Include the URL in `sources:` frontmatter and in the `> Source:` line. Also include `conversation:<date>` when the capture request itself provides provenance.
6. Choose a source-kind tag such as `article`, then topical tags from taxonomy. If a tag is already used in the vault but missing from `_meta/taxonomy.md`, treat it as taxonomy drift and add it deliberately before verification.
7. If the URL is access-blocked after reasonable attempts (for example Cloudflare, bot detection, timeout, or empty body), switch to `references/access-blocked-url-capture.md`: gather official search snippets/metadata, disclose the limitation in `Capture Policy`, lower confidence, and mark operational interpretation with `^[inferred]`. Do not write as though the page was fully fetched.
8. Update `index.md`, `log.md`, `hot.md`, and the most relevant map. If the source is about the wiki system itself or agent memory/workflow, `AI Map` is usually relevant.
9. Verify frontmatter, taxonomy tags, all wikilinks, tracking-file references, log timestamp, and map coverage before confirming.

## Pitfalls

- Do not treat an existing secondary/comparative source guide as a duplicate of the primary URL. Preserve both layers and cross-link them.
- Do not cite only `conversation:<date>` for a fetched URL; keep the actual URL in frontmatter.
- Do not add a widely-used vault tag as an ad hoc page tag without updating taxonomy if taxonomy exists.
- Do not leave the new source technically indexed but practically invisible; add a domain map link when the source clearly belongs to an existing map.
