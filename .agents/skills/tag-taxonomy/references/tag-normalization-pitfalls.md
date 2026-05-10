# Tag normalization pitfalls from 2026-05-10 wiki cleanup

Context: wiki-lint found only two remaining issues after link, provenance, stale, and confidence fixes: low-cohesion tag clusters `ai` (93 pages) and `source` (53 pages). The correct fix was taxonomy normalization, not cross-linking.

## Lessons

1. Broad umbrella tags can be graph noise.
   - `ai` grouped nearly every AI-related page, but the pages were already better described by `agents`, `llm`, `harness`, `memory`, `context`, `inference`, `ai-coding`, `tools`, etc.
   - Retire the umbrella tag and keep the specific cluster tags.

2. Type tags can duplicate frontmatter category.
   - `source` duplicated `category: sources` and created a low-cohesion cluster.
   - Remove it from page tags; use source-kind tags (`paper`, `article`, `blog`, `arxiv`, `survey`, `book`) plus topical tags instead.

3. Do not satisfy tag cohesion by adding weak links.
   - For broad clusters, dozens of links would make the metric look better while making the graph worse.
   - Split/retire the tag first; cross-link only smaller coherent topics.

4. Create `_meta/taxonomy.md` if missing.
   - Include rules, retired tags, common cluster tags, source-kind tags, and aliases.
   - Mention `visibility/` only as reserved system tags, not as canonical taxonomy entries.

5. Keep derived files in sync.
   - After editing frontmatter tags, update tag snippets in `index.md`.
   - Update `hot.md` Recent Activity.
   - Append `TAG_NORMALIZE` and final `LINT` log entries.

6. Avoid large greedy regexes on `index.md`/`hot.md`.
   - A broad multi-line section regex timed out on `index.md`/`hot.md` handling.
   - Prefer line-wise processing for index tag snippets and section slicing by exact heading lines for `hot.md`.

7. Re-run stale checks after tag edits.
   - Tag edits change file mtimes.
   - If a source guide is modified, pages that list it in `sources:` may become stale. Update source pages first, then dependent synthesis pages.

## Known-good result shape

Final verification after the cleanup should show:

- retired `ai` tags remaining: 0
- retired `source` tags remaining: 0
- fragmented tag clusters: 0
- stale content: 0
- broken links: 0
- missing frontmatter/summary: 0
- provenance and confidence/lifecycle issues: 0
