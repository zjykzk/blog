# Article Source Capture Pattern

Use this when the user pastes a full web article or essay directly into the chat and asks to capture it. The goal is to preserve the source layer without turning a single article into a premature stable concept page.

## Trigger shape

- User pastes a complete or near-complete article, blog post, essay, newsletter, or practitioner report.
- The source is not a PDF/paper, not an X thread, and not merely a short quote.
- The article introduces a named method, playbook, practitioner metric, or set of examples that overlaps existing wiki concepts.

## Recommended workflow

1. Treat the page as `category: sources` with `article` plus topical controlled tags.
2. Search `index.md` for exact title, author, organization, and central phrase to avoid duplicates.
3. Keep the body detailed enough to revisit the article without reopening the chat:
   - opening anecdote or motivating case;
   - explicit definition or thesis;
   - major examples and workflows;
   - tables or playbooks;
   - reported metrics;
   - closing recommendations.
4. In `Capture Policy`, state that this preserves source-level article content, not a stable concept.
5. In `Integration Decisions`, separate:
   - claims to keep source-level until corroborated, especially metrics and company-specific results;
   - concepts already covered by existing pages;
   - whether a future concept page may be warranted after more sources.
6. Prefer linking to existing concept/topic/synthesis pages instead of creating a new concept page just because the article uses a memorable phrase. Create a new stub only when the named idea is central, reusable, and not already represented by existing pages.
7. Update the most relevant map, not only `index.md`, `log.md`, and `hot.md`.

## Pitfalls

- Do not compress a practitioner article into only “Key Points”; preserve its argument flow and examples.
- Do not promote self-reported productivity metrics into general wiki claims without marking them as source-reported.
- Do not create duplicate concepts when the article is an example of an existing concept such as harness ratchets, feedback flywheels, verification loops, or team standards.
- Do not omit open questions. Practitioner articles often imply unresolved governance questions: ownership of rules, pruning stale context, metric validity, autonomy boundaries, or review risk.

## Minimal article source guide sections

```markdown
# <Article Title> Source Guide

> Source: <article title, author, publisher, URL if available>

## Capture Policy
<Preserves source-level article content; note concept-promotion boundary.>

## What It Covers
<Article thesis and why it belongs in the wiki.>

## Preserved Content
### Opening example / motivating case
### Definition or thesis
### Main workflow / playbook
### Examples and reported results
### Closing recommendations

## Integration Decisions
<Existing wiki pages it supports; source-level claims to avoid overgeneralizing.>

## Open Questions
<Governance, measurement, risk, pruning, scope questions.>

## Related
<2+ resolved wikilinks>
```
