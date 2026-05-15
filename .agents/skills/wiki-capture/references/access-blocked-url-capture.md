# Access-Blocked URL Capture Pattern

Use this when direct URL source capture hits Cloudflare, bot detection, timeouts, paywall-like blocking, or otherwise cannot retrieve the page body after reasonable attempts.

## Trigger shape

- User invokes wiki-capture with a URL.
- Browser or curl reaches an access-denied page, Cloudflare block, timeout, or empty body.
- Search snippets, official metadata, cached excerpts, or mirrored quotes expose enough of the source to preserve a limited source guide.

## Workflow

1. Try at least two retrieval paths before falling back: browser/rendered page plus a non-executing shell fetch such as `curl -L --fail --max-time ... -o /tmp/page.html`.
2. If blocked, gather secondary grounding without pretending full access succeeded:
   - Search exact title, URL, and distinctive phrases.
   - Prefer snippets for the same official URL over third-party summaries.
   - Use multiple snippets when possible to recover exact public wording.
3. Create a source guide only if enough grounded content exists to be useful. Otherwise tell the user the source could not be captured reliably.
4. In `Capture Policy`, explicitly state the access limitation and what the preserved content is grounded in.
5. Lower provenance confidence and mark synthesized operational guidance with `^[inferred]`.
6. Avoid claiming the note is a complete reproduction. Phrase it as a limited source guide for the public wording / visible excerpts / accessible metadata.
7. Keep the original URL in `sources:` and the `> Source:` line, even when the body was reconstructed from snippets.
8. Verification is unchanged: frontmatter, taxonomy, links, index/log/hot, and relevant map coverage still must pass.

## Pitfalls

- Do not silently use search snippets while writing as if the page was fetched normally.
- Do not mirror broad third-party explanations when the user asked to capture the primary URL; keep third-party material out or label it clearly.
- Do not over-compress access-limited captures into conclusions; preserve the exact exposed wording and separate interpretation from extracted content.
