# Wiki Lint Script Pitfalls

Session-derived notes for future wiki-lint runs.

## Timestamp and stale checks

- Normalize ISO timestamps before comparison. `2026-05-10T14:31:47+0800` and `2026-05-10T14:31:47+08:00` are equivalent.
- If a pass updates source pages and synthesis pages together, write source pages first and bump synthesis pages afterward. Otherwise synthesis pages can immediately look stale because their sources have newer mtimes.
- When a previous same-session lint pass used faulty logic, append a new `LINT` entry with a note like `supersedes prior same-session LINT...` rather than deleting log history.

## Provenance counting

- Count each claim unit once. Use priority: ambiguous > inferred > extracted.
- Compute `extracted = max(0, 1 - inferred - ambiguous)`; negative extracted means the parser double-counted markers.
- Paragraph/list-item units are more robust than naive sentence splitting for mixed English/Chinese markdown, bullets, tables, and code fences.

## Visibility / PII scanning

- Avoid broad keyword matches for `token`, `secret`, etc. They create false positives on conceptual pages like `Life of a Token`.
- Prefer anchored key-value patterns (`^\s*(password|api_key|secret|ssn|email|phone)\s*[:=]\s*\S+`) and then manually inspect before tagging.

## Fragmented tags

- Low cohesion for broad tags such as `ai` or `source` is usually a taxonomy signal, not a request to add dozens of weak links.
- For large clusters, recommend splitting tags or excluding meta/system tags from cohesion checks.
- For smaller topical clusters, use cross-linker and add only semantic links.
