---
name: wiki-capture
description: >
  Save the current conversation as a permanent, structured wiki note. Use this skill when the user
  says "save this", "/wiki-capture", "capture this", "file this conversation", "preserve this",
  "add this to my wiki", or wants to turn what was just discussed into lasting knowledge. The skill
  classifies the content, rewrites it as declarative knowledge (not a chat transcript), and places
  it in the correct vault category.
---

# Wiki Capture — Conversation to Wiki Note

You are preserving knowledge from the current conversation as a permanent wiki note. The goal is to extract the *substance* — the knowledge itself — not a summary of what was said.

## Before You Start

1. Read `~/.obsidian-wiki/config` (preferred) or `.env` (fallback) to get `OBSIDIAN_VAULT_PATH` and `OBSIDIAN_LINK_FORMAT` (default: `wikilink`). If both files are missing but the current repository has a canonical `wiki/` layer (for example `wiki/index.md` and `wiki/NAMING.md` exist), treat `./wiki` as `OBSIDIAN_VAULT_PATH` and continue instead of stopping.
2. Read `$OBSIDIAN_VAULT_PATH/index.md` to understand existing wiki content (avoid duplicates)
3. Read `$OBSIDIAN_VAULT_PATH/hot.md` if it exists — it gives context on recent activity
4. Read `$OBSIDIAN_VAULT_PATH/NAMING.md` if it exists. Prefer its local naming and placement conventions over generic slug rules when they conflict, while still keeping capture frontmatter complete.
5. Read `$OBSIDIAN_VAULT_PATH/_meta/taxonomy.md` if it exists. Use existing controlled tags from this file rather than inventing near-synonym tags; for source guides, prefer a concrete source-kind tag such as `article`, `paper`, or `book` plus topical tags. If a needed tag is genuinely new, add it deliberately and update the taxonomy rather than letting a one-off tag drift into the wiki. If a tag is already widely used in existing index/map/source pages but missing from taxonomy, treat that as taxonomy drift: add the tag to taxonomy and update its timestamp rather than inventing a synonym or leaving verification ambiguous.

When writing internal links in Step 5, apply the link format from `llm-wiki/SKILL.md` (Link Format section) using the `OBSIDIAN_LINK_FORMAT` value. If that file is unavailable, follow the local convention observed in `index.md`/`NAMING.md` (for this vault, path-qualified Obsidian wikilinks such as `[[wiki/concepts/Page Name]]`).

## Step 1: Identify What's Worth Preserving

Scan the conversation. Ask: what knowledge emerged here that would be valuable in 3 months with no memory of this chat?

Worth preserving:
- Decisions made and *why* they were made
- Analysis, frameworks, mental models developed
- Technical findings, patterns, or procedures
- Synthesized understanding of a topic
- Clear explanations of a concept that took effort to arrive at
- Key facts from an external source discussed in the conversation

Skip:
- Logistics, scheduling, pleasantries
- Exploratory back-and-forth where no conclusion was reached
- Content that's already in the wiki

If the current conversation extends an already-captured concept rather than merely repeating it, do not overwrite or duplicate the existing page. Capture the new durable layer as a synthesis that links back to the existing concept. Example: if `Engineering Thinking` already exists as a concept and the new discussion develops responsibility, appealability, feedback walls, or organizational suppression mechanisms, create a focused synthesis page rather than expanding the concept into an overlarge catch-all.

If nothing material emerged, tell the user and stop.

## Step 2: Classify the Content Type

When the user pastes a large external article, web page, transcript, interactive walkthrough, or asks to preserve the source layer of a conversation, default to `source` unless the conversation itself added substantial original synthesis. Create a source guide that preserves the external artifact or conversation-source content with enough structure and detail to be reusable later; do not collapse it into a brief summary and do not promote it directly into a broad concept page just because it covers many concepts.

Assign one of five types — this determines the target folder and tone:

| Type | Description | Target folder |
|---|---|---|
| `synthesis` | Multi-step analysis or an answer to a specific question that required reasoning | `synthesis/` |
| `concept` | A definition, framework, or mental model (what a thing *is*) | `concepts/` |
| `source` | Source-layer preservation of an external document, article, resource, transcript, or conversation artifact, with structure and integration notes but not reduced to a short summary | `sources/` |
| `decision` | A strategic, architectural, or design choice and its rationale | `synthesis/` |
| `session` | A complete discussion summary when the conversation spans multiple topics | `journal/` |

If the content clearly belongs to a specific project (detected from context or user mention), place it under `projects/<project-name>/<category>/` instead.

### Direct-source companion pattern

When the user provides a primary source URL (for example an arXiv paper or a direct PDF paper link) and an existing source guide already covers a secondary explanation, article, thread, or commentary about the same object, do not overwrite or collapse the two layers. Create a companion source guide for the primary source (for example `Foo Paper Source Guide.md`) and link it to the existing article-level guide. In the new guide, explicitly state the source-layer distinction in `Capture Policy` and `Integration Decisions`, so future readers know which page to use for paper-grounded claims versus commentary-grounded interpretation.

For direct PDF paper links, follow `references/pdf-paper-source-capture.md`: download the PDF, extract text with local tools or a temp `pypdf` virtualenv when `pdfinfo`/`pdftotext` are unavailable, preserve the paper's argument/evidence/caveats, and keep primary-paper claims separate from secondary commentary.

### Pasted article source-capture pattern

When the user pastes a complete web article, blog post, essay, newsletter, or practitioner report directly into chat, default to a detailed `source` guide unless the conversation itself adds substantial independent synthesis. Preserve the article's argument flow, opening anecdote, named method, examples, playbook, reported metrics, and closing recommendations. In `Integration Decisions`, separate source-reported claims (especially productivity metrics or company-specific outcomes) from stable wiki concepts, and prefer linking to existing concepts/topics/syntheses rather than creating a duplicate concept page for a memorable phrase. Follow `references/article-source-capture.md` for the compact pattern.

### X article fallback and existing-page expansion pattern

When the capture target is an X/Twitter article or long post, prefer the normal authenticated X tool path if available. If `xurl` is missing, unauthenticated, rate-limited, or incomplete, use the browser-rendered page: extract `article.innerText`, inspect `pbs.twimg.com/media/...` images with OCR/vision when they contain diagrams, and preserve the diagrams/tables in the source guide. See `references/x-article-capture-fallback.md` for the detailed fallback. If a source guide for the same X URL already exists, expand or correct that page rather than creating a duplicate; then update `index.md`, `log.md`, `hot.md`, and the relevant map as an update.

### Query-to-wiki promotion pattern

When the immediately preceding work was a wiki-query / exploration answer and the user says the topic "has not been generated to files yet" or asks to "生成到 wiki / 生成文件 / 沉淀成页面", treat the prior synthesized answer as capture-worthy durable knowledge even if no external source was pasted. Prefer a paired output when the content has both a central concept and an inventory/map shape:

- Create a `concepts/` page for the core mental model or framework (definition, parts, how it works, when to use, template).
- Create a `maps/` page when the answer enumerated many existing wiki pages or domain entrances; the map should organize existing pages into usable clusters rather than only repeat the chat answer.
- Update `index.md`, `log.md`, `hot.md`, and the most relevant existing map so the new pages are not orphaned.
- If a genuinely new controlled tag is needed, update `_meta/taxonomy.md` deliberately and verify it.
- Verification must include frontmatter completeness, all wikilinks resolving, and incoming links from tracking/map pages.

This pattern is especially useful for Chinese conceptual explorations such as “机制模型”: preserve the user's language in the durable prose while using vault naming conventions for filenames.

### Conversational teaching follow-up pattern

When a wiki-query or teaching exchange develops through several user follow-up questions into a coherent tutorial, capture the durable explanation even if no external source was pasted. Default to a `source` guide when the value is the teaching sequence itself: concrete examples, mental models, contrasts, and common misconceptions.

Use this especially when adjacent source guides already exist but the conversation fills a missing layer. For example, after React Hooks source guides, a follow-up exchange about component lifecycle should become a companion source guide that preserves mount, render/update, unmount, key identity, and effect cleanup as a reusable explanation rather than overwriting the existing hooks pages.

Follow `references/conversational-teaching-follow-up-capture.md` for the compact pattern. If preceding wiki-query answers already appended `QUERY` entries to `log.md`, leave them and append the `CAPTURE` entry afterward; they are part of the same knowledge flow, not noise to delete.

## Step 3: Rewrite as Declarative Knowledge

Do **not** write a summary of the conversation. Write the knowledge itself, in declarative present tense:

- Not: "The user asked about X and Claude explained that..."
- Yes: "X works by..."
- Not: "We decided to use Y because..."
- Yes: "Y is preferred over Z because [reason]. [^[inferred] if the rationale was implied, not stated explicitly]"

### Language preservation

Preserve the user's/source's primary language when writing the note body, summaries, index entries, hot-cache updates, and map descriptions. If the source material is Chinese or the user writes the capture instruction in Chinese, write the durable wiki prose in Chinese by default. English page titles may still be used when they match the vault's naming convention or avoid duplicate concepts, but the explanatory content should follow the source/user language unless the user explicitly asks otherwise.

If the user explicitly says “不用翻译”, “不要翻译”, or similar, treat that as a strong capture constraint: preserve the source language not only in the prose, but also in source-facing headings, summaries, aliases, map descriptions, and confirmation text. Use an English filename/title only when the vault convention or duplicate-avoidance clearly requires it; in that case, preserve the original Chinese source title as an alias and in the `> Source:` line.

For Chinese source captures, prefer a Chinese source-guide title and confirmation even if some related stable concepts use English names elsewhere in the vault. If the source title contains filesystem-unfriendly punctuation such as `：` or `「」`, keep the display title/alias faithful but use a safe filename that still reads naturally (for example `内核 你的三个自我 Source Guide.md`).

This matters because wiki-capture is not merely storing facts; it is creating a reusable reading artifact. A Chinese source captured into English forces an unnecessary second pass and breaks the user's expected reading flow.

When the captured conversation just produced a structured analytical artifact from another skill (for example a rank analysis, PRD, research synthesis, roundtable discussion, or diagram explanation), preserve the artifact's core conceptual shape while converting it into wiki prose. Do not preserve chat logistics, but do preserve the named framework, generated categories, diagnostic questions, representative positions, durable tensions, compact diagrams, examples, and reusable templates if they are the durable knowledge. If an external side artifact was also written (for example under `~/Documents/notes/`), do not treat that file as a source unless the user asked to ingest it; cite the conversation as the source and link the wiki note to existing wiki pages.

### Source-layer preservation rule

When the target type is `source`, the body should preserve source-level content, not reduce the source to a short "Key Points" digest. Frontmatter still needs a concise `summary` for navigation, but the note body should keep enough of the original structure, examples, diagrams, argument flow, Q&A, or generated artifact to be useful without reopening the chat or external document. Put compression, abstraction, and cross-source conclusions in `synthesis` or `concept` pages instead.

When the user pastes an inline tutorial, walkthrough, code explanation, or comparison table and asks to capture it—especially with “不用翻译”—treat the pasted explanation as a source artifact unless the user explicitly asks for a distilled concept page. Preserve the teaching sequence, code examples, mental models, warnings, comparison table, and bottom-layer explanation. See `references/inline-tutorial-source-capture.md` for the compact pattern.

When the user pastes a long course chapter, lecture note, workshop handout, or architecture-methodology lesson, use the long-course pattern: keep the source's teaching sequence, motivating story, tables, templates, diagrams/code blocks, workshop agendas, and action recommendations; normalize copied formatting without collapsing the artifact into a brief digest. See `references/long-course-source-capture.md`.

For roundtable captures, default to a `source` guide unless the user asks for a distilled synthesis. Preserve the participants' stance network, representative positions, moderator summaries, core disagreement, and ASCII frameworks as durable source material. If the user asks to ingest the roundtable or says the source content matters, keep the full discussion structure and substantive turns rather than only a stance summary. If the discussion already produced a separate synthesis page, link the roundtable source guide to that synthesis while keeping the roundtable's own source-layer content. Use a concrete `roundtable` tag when the vault taxonomy supports it; if roundtable source guides already exist but taxonomy is missing `roundtable`, treat that as taxonomy drift and add it deliberately before verification.

Apply provenance markers per `llm-wiki`:
- *Extracted* — explicitly stated in the conversation (no marker)
- *Inferred* — generalized or synthesized from the conversation → `^[inferred]`
- *Ambiguous* — disputed, uncertain, or contradictory → `^[ambiguous]`

## Step 4: Generate a Slug and Title

Derive a clear, descriptive title from the content. Use the vault's local naming convention from `NAMING.md` when available. If no local convention exists, slugify it:
- Lowercase, words separated by hyphens
- Max 50 characters
- Avoid dates in the slug (the frontmatter has `created`)

For vaults whose `NAMING.md` says concept/topic/synthesis files use Title Case with spaces, create `Title Case.md` files rather than lowercase hyphenated slugs, even if the generic capture instruction says "slug".

## Step 5: Write the Wiki Note

Create the file at the target path with required frontmatter:

```yaml
---
title: >-
  <Title>
category: <syntheses|concepts|sources|journal|skills>
tags: [<2-5 domain tags from taxonomy>]
sources:
  - conversation:<ISO-date>
created: <ISO-8601 timestamp>
updated: <ISO-8601 timestamp>
summary: >-
  <1-2 sentences, ≤200 chars, answering "what knowledge does this page hold?">
provenance:
  extracted: 0.X
  inferred: 0.X
  ambiguous: 0.X
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: <ISO date today>
---
```

Body structure by type:

**synthesis / decision:**
```markdown
# Title

## Context
<What prompted this — the problem or question being addressed>

## Finding / Decision
<The core knowledge or conclusion>

## Reasoning
<Why this is the case or why this choice was made>

## Implications
<What follows from this — what to watch for, next steps, trade-offs>

## Related
<[[wikilinks]] to connected pages>
```

**concept:**
```markdown
# Title

<Definition in one clear sentence.>

## What It Is
<Explanation of the concept>

## How It Works
<Mechanism or structure>

## When to Use
<Applicability, conditions, trade-offs>

## Related
<[[wikilinks]]>
```

**source:**
```markdown
# Title

> Source: <title or URL>

## Capture Policy
<One or two sentences stating whether this page preserves source-level content, a generated artifact, or an external text.>

## What It Covers
<What the source is about and why it belongs in the wiki>

## Preserved Content
<Structured preservation of the source's argument flow, major sections, examples, diagrams, Q&A, or generated artifact. This should be detailed enough to revisit the source without relying on a compressed summary. Use subsections that match the source's own structure when possible.>

## Integration Decisions
<How this source connects to existing wiki concepts/topics/syntheses; which claims should stay source-level versus be promoted later. Use this section especially for broad external walkthroughs that touch many existing pages.>

## Open Questions
<What it raises but doesn't answer — omit if none>

## Related
<[[wikilinks]]>
```

**session:**
```markdown
# Title

*Session captured: <date>*

## Topics Covered
<Brief list>

## Key Takeaways
<The 3-5 most important things that emerged>

## Decisions Made
<Any explicit decisions, with rationale>

## Open Questions
<What remains unresolved>

## Related
<[[wikilinks]]>
```

Every note must link to at least 2 existing wiki pages. Search `index.md` before writing. If fewer than 2 related pages exist, create minimal stubs for the most important concepts referenced.

**Promotable concept links:** If a source guide names a concept as "future", "promotable", or central enough to appear as a wikilink (for example `[[wiki/concepts/Foo]]`), do not leave it as a broken aspirational link. Either (a) avoid linking it and mention the future page in plain text, or (b) create a minimal concept stub with complete frontmatter, a one-sentence definition, 2+ links, and index/map coverage. Prefer (b) when the pasted source's core contribution is a named theory, framework, or mental model.

## Step 6: Update Tracking Files

**`index.md`** — Add the new page under its category section.

**`log.md`** — Append:
```
- [TIMESTAMP] CAPTURE type=<type> page="<path>" title="<title>"
```

**`hot.md`** — Update **Recent Activity** with what was just captured. Update **Key Takeaways** if the note introduced something worth flagging. Update `updated` timestamp.

**Relevant map pages** — If the capture clearly belongs to an existing map (for example `Learning Map`, `AI Map`, `CS Map`, or `Management Map`), add the new source/concept/synthesis there as well. This prevents captures from being technically indexed but practically invisible from the user's domain entrypoints.

## Step 7: Verify and Confirm to User

Use `references/verification-pattern.md` as a reusable starting point for the lightweight verification script; adapt paths, new note list, timestamp checks, and map checks to the current capture.

Before confirming, run a lightweight verification pass:
- Re-read the created note and check that required frontmatter fields exist: `title`, `category`, `tags`, `sources`, `created`, `updated`, `summary`, `provenance`, `base_confidence`, `lifecycle`, and `lifecycle_changed`.
- If `_meta/taxonomy.md` exists, verify the chosen tags are controlled-vocabulary tags or deliberately added taxonomy entries; fix ad hoc tags before updating index summaries.
- Resolve every wikilink in the note against the vault; fix broken links before reporting success.
- Check incoming links from at least `index.md`, `log.md`, or `hot.md` so the new note is not orphaned.
- Confirm that `index.md`, `log.md`, and `hot.md` contain the new page reference and current capture timestamp.
- If a related map page was updated, confirm it contains the new page reference.
- Run the broken-link check after all supporting stubs are created, not before; a source guide plus concept stub may need a second verification pass.

Then report the saved path and title:
```
Saved to: projects/<name>/synthesis/<slug>.md
Title: <Title>
Type: synthesis
```

## Supporting References

- `references/verification-pattern.md` — lightweight verification pattern for frontmatter, taxonomy tags, wikilinks, tracking files, and map coverage.
- `references/conversational-teaching-follow-up-capture.md` — pattern for turning multi-turn explanatory follow-ups after wiki-query into companion source guides without flattening them into short summaries.
- `references/article-source-capture.md` — pattern for preserving pasted web articles, essays, newsletters, and practitioner reports as detailed source guides while keeping metrics and single-source claims source-level.
- `references/pdf-paper-source-capture.md` — fallback workflow for direct PDF paper/report captures, including temp-venv `pypdf` extraction when `pdfinfo`/`pdftotext` are unavailable or Python is PEP-668 managed.
- `references/inline-tutorial-source-capture.md` — pattern for preserving inline tutorials, walkthroughs, code explanations, and comparison tables as source-layer artifacts, especially when the user says “不用翻译”.
- `references/long-course-source-capture.md` — pattern for preserving long pasted course chapters, lecture notes, architecture-methodology lessons, and workshop handouts without reducing them to a short digest.
- `references/chinese-source-capture-promoted-concept.md` — example pattern for Chinese source captures with “不用翻译” plus a promoted central concept stub.
- `references/arxiv-source-capture-fallback.md` — fallback workflow for preserving arXiv papers when HTML is unavailable or PDF/text extraction via shell is blocked; use the arXiv API plus e-print LaTeX source bundle.
- `references/x-article-capture-fallback.md` — fallback workflow for X/Twitter articles when `xurl` is unavailable or partial; use browser-rendered article text plus image OCR, and expand an existing source guide rather than creating a duplicate.

## Quality Checklist

- [ ] Content rewritten as declarative knowledge (not a chat transcript)
- [ ] Type classified correctly; target path is in the right folder
- [ ] Frontmatter complete with title, category, tags, sources, summary, provenance, confidence, and lifecycle fields
- [ ] At least 2 wikilinks to existing pages, with no broken links
- [ ] New note has an incoming link from a tracking or related page
- [ ] `index.md`, `log.md`, and `hot.md` updated
- [ ] Verification pass completed before reporting success
- [ ] Confirmed save path to user
