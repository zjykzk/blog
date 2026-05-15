---
title: >-
  LLM Wiki Source Guide
category: sources
type: source
status: draft
tags: [article, llm, agents, memory, llm-wiki]
sources:
  - https://gist.githubusercontent.com/karpathy/442a6bf555914893e9891c11519de94f/raw/ac46de1ad27f92b28ac95459c782c07f6b8c964a/llm-wiki.md
  - conversation:2026-05-15
created: 2026-05-15T21:19:51+08:00
updated: 2026-05-15T21:19:51+08:00
summary: >-
  Source guide for Karpathy's LLM Wiki idea file: a persistent, LLM-maintained Markdown wiki that compiles raw sources into cumulative, cross-linked knowledge.
provenance:
  extracted: 0.91
  inferred: 0.08
  ambiguous: 0.01
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-05-15
aliases:
  - LLM Wiki
  - Karpathy LLM Wiki
  - Personal knowledge bases using LLMs
---

# LLM Wiki Source Guide

> Source: Andrej Karpathy, "LLM Wiki", raw gist, https://gist.githubusercontent.com/karpathy/442a6bf555914893e9891c11519de94f/raw/ac46de1ad27f92b28ac95459c782c07f6b8c964a/llm-wiki.md

## Capture Policy

This page preserves the source-level content of Karpathy's idea file. It keeps the article's argument flow, architecture, operations, indexing model, optional tools, practical tips, and rationale as source material rather than promoting every claim into stable wiki doctrine.

The source is intentionally abstract: it proposes a pattern for building a personal or team knowledge base with an LLM agent, but leaves the concrete directory structure, schema, tools, and workflow to be instantiated by each user and agent.

## What It Covers

The source describes LLM Wiki as a pattern for using LLMs to build and maintain a persistent personal knowledge base. Its central distinction is between ordinary RAG and a compounding wiki layer: RAG retrieves chunks from raw sources at query time, while LLM Wiki uses the LLM to incrementally compile raw sources into a structured, cross-linked Markdown wiki that keeps synthesis, contradictions, and references current.

It belongs in the wiki because it directly grounds this repository's own knowledge architecture: raw sources feed a canonical `wiki/` layer; `index.md`, `log.md`, and `hot.md` help navigation and temporal context; capture and query outputs can become durable pages; linting and cross-linking preserve graph health. It connects especially to [[wiki/topics/AI Memory]], [[wiki/topics/AI Skills Workflow]], [[wiki/topics/Context Management]], [[wiki/concepts/Agent Skill]], [[wiki/concepts/Feedback Flywheel]], and [[wiki/concepts/Harness Ratchet]].

## Preserved Content

### 1. High-level intent

The file is framed as an idea file to be copied into an LLM agent such as OpenAI Codex, Claude Code, OpenCode/Pi, or similar. It is not a finished implementation manual. Its purpose is to communicate the pattern so that a user and their agent can instantiate the details collaboratively.

The pattern targets a common failure of document-based LLM workflows: the LLM can answer questions from uploaded files, but each subtle question requires rediscovering and reassembling the relevant fragments. There is no persistent accumulation. The same synthesis has to be rebuilt every time.

### 2. Core idea: persistent compiled knowledge instead of query-time rediscovery

The source contrasts two modes:

| Mode | What happens | Failure mode |
|---|---|---|
| RAG / file upload / NotebookLM-style retrieval | Raw documents are indexed or uploaded; the LLM retrieves relevant chunks at query time and generates an answer. | The system repeatedly rediscovers knowledge from scratch; cross-document synthesis is not durably preserved. |
| LLM Wiki | The LLM incrementally builds and maintains a structured Markdown wiki between the user and the raw sources. | The maintenance burden moves to the LLM; schema discipline and verification become important. ^[inferred] |

The key claim is that the wiki is a persistent, compounding artifact. Cross-references are already present. Contradictions are already flagged. Summaries and synthesis pages already reflect the growing source collection. Every source and good question can make the wiki richer instead of disappearing into chat history.

The human rarely writes the wiki directly. The human curates sources, explores, asks questions, reads results, and judges what matters. The LLM handles summarizing, cross-referencing, filing, updating summaries, and bookkeeping.

Karpathy's working image is: Obsidian is the IDE, the LLM is the programmer, and the wiki is the codebase. The agent edits the wiki while the user watches and browses the results in Obsidian, following links and graph structure.

### 3. Use cases

The source lists several domains where the pattern applies:

- **Personal knowledge**: goals, health, psychology, self-improvement, journal entries, articles, podcasts, and a structured picture of oneself over time.
- **Research**: deep topic exploration over weeks or months, using papers, reports, articles, and evolving thesis pages.
- **Reading a book**: each chapter can be filed as the book is read; pages for characters, themes, plot threads, places, and events can accumulate into a personal companion wiki. The source compares this to community fan wikis such as Tolkien Gateway, except maintained by an LLM for one reader.
- **Business and team work**: internal wikis fed by Slack threads, meeting transcripts, project documents, and customer calls, possibly with human review of the LLM's updates.
- **Competitive analysis, due diligence, trip planning, course notes, hobby deep-dives**: any domain where knowledge is accumulated over time and should become organized rather than scattered.

These examples show that LLM Wiki is not only a research workflow. It is a general pattern for turning repeated source accumulation into maintained structure.

### 4. Architecture: three layers

The source describes three layers.

#### Raw sources

Raw sources are the curated collection of source documents: articles, papers, images, data files, transcripts, and other materials. They are immutable. The LLM reads them but does not modify them. They remain the source of truth.

This layer matters because the wiki is generated and revisable; claims should remain traceable back to source material. ^[inferred]

#### The wiki

The wiki is a directory of LLM-generated Markdown files. It can contain summaries, entity pages, concept pages, comparisons, overviews, and syntheses. The LLM owns this layer: it creates pages, updates them when new sources arrive, maintains cross-references, and keeps pages consistent.

The human reads the wiki, corrects direction, and uses it as the active knowledge interface, but the repetitive maintenance is delegated to the LLM.

#### The schema

The schema is a document such as `CLAUDE.md` or `AGENTS.md` that tells the LLM how the wiki is structured, what conventions apply, and what workflows to follow for ingesting sources, answering questions, and maintaining the wiki.

This layer makes the difference between a generic chatbot and a disciplined wiki maintainer. The schema is expected to co-evolve with the user and the LLM as the domain, conventions, and workflow become clearer.

### 5. Operations: ingest, query, lint

#### Ingest

Ingest starts when the user adds a new source to the raw collection and asks the LLM to process it. A typical flow:

1. The LLM reads the source.
2. The LLM discusses or identifies key takeaways with the user.
3. The LLM writes a summary or source page in the wiki.
4. The LLM updates the index.
5. The LLM updates relevant entity, concept, topic, and synthesis pages.
6. The LLM appends an entry to the log.

A single source can touch 10–15 wiki pages. The source recommends ingesting one source at a time with user involvement when quality matters, though batch ingestion is possible if the workflow supports it.

The durable workflow should be documented in the schema so future sessions do not rely on ad hoc memory.

#### Query

Query means asking questions against the wiki rather than directly against raw documents. The LLM searches for relevant pages, reads them, and synthesizes an answer with citations. Answers can become many formats: Markdown pages, comparison tables, slide decks, charts, or canvases.

The important insight is that good answers can be filed back into the wiki. A comparison, analysis, or newly discovered connection should not disappear into chat history if it has future value. This turns exploration itself into wiki growth.

#### Lint

Lint is periodic wiki health checking. The LLM should look for:

- contradictions between pages;
- stale claims superseded by newer sources;
- orphan pages with no inbound links;
- important concepts mentioned but lacking their own page;
- missing cross-references;
- data gaps that could be filled with web search.

Linting keeps the wiki healthy as it grows. It also helps the LLM suggest new questions and new sources.

### 6. Indexing and logging

The source highlights two special files.

#### index.md

`index.md` is content-oriented. It is a catalog of everything in the wiki, with links, one-line summaries, and optional metadata. It is organized by category such as entities, concepts, sources, and syntheses.

When answering a query, the LLM reads the index first to find relevant pages, then drills into those pages. The source says this works surprisingly well at moderate scale, roughly around 100 sources and hundreds of pages, and can avoid embedding-based RAG infrastructure at that scale.

#### log.md

`log.md` is chronological. It is append-only and records ingests, queries, lint passes, and other operations. If each entry uses a consistent prefix, it becomes parseable with Unix tools such as `grep` and `tail`.

The log gives the wiki an evolution timeline and helps the LLM understand what was done recently.

### 7. Optional CLI tools

The source suggests adding small tools when the wiki grows. Search is the most obvious need. At small scale, `index.md` may be enough. At larger scale, a local Markdown search engine such as `qmd` can provide hybrid BM25/vector search and LLM reranking on-device, through either CLI or MCP.

The source also leaves room for simpler custom search scripts. Tooling is modular: the wiki pattern does not require a specific search backend.

### 8. Tips and tricks

The article lists practical Obsidian and Markdown tips:

- **Obsidian Web Clipper** can convert web articles to Markdown quickly.
- **Local image downloads** make clipped sources more durable. In Obsidian, setting a fixed attachment folder and using the download-attachments hotkey can preserve images locally instead of depending on remote URLs.
- **Image handling remains clunky for LLMs**: an LLM may need to read Markdown text first, then inspect selected referenced images separately.
- **Obsidian graph view** helps reveal the shape of the wiki: hubs, orphans, and clusters.
- **Marp** can turn Markdown into slide decks, useful when wiki material needs presentation form.
- **Dataview** can query frontmatter to generate dynamic tables and lists.
- **Git** gives the Markdown wiki version history, branching, and collaboration without additional infrastructure.

### 9. Why the pattern works

The source argues that the tedious part of maintaining a knowledge base is not reading or thinking, but bookkeeping:

- updating cross-references;
- keeping summaries current;
- noting when new data contradicts old claims;
- maintaining consistency across many pages.

Humans often abandon wikis because the maintenance burden grows faster than perceived value. LLMs are well-suited to this bookkeeping because they can touch many files in one pass and do not get bored by repetitive maintenance.

The human's job remains source curation, analysis direction, question quality, and interpretation of meaning. The LLM's job is the maintenance substrate around those human judgments.

### 10. Relation to Memex

The source relates the idea to Vannevar Bush's Memex from 1945: a private, curated knowledge store with associative trails between documents. The source claims Bush's vision was closer to this pattern than to the public web as it evolved, because it emphasized private curation and meaningful connections.

The missing piece in Memex was who performs the maintenance. The source's answer is that the LLM handles the maintenance.

### 11. Implementation remains intentionally open

The final note emphasizes that the document is abstract. It describes an idea, not a specific implementation. Directory structure, page formats, schema conventions, tooling, and output formats should vary by domain, preference, and LLM.

The right use is to share the document with an LLM agent and work together to instantiate the pattern. This makes the document itself a seed schema artifact rather than a turnkey product manual. ^[inferred]

## Integration Decisions

This source should remain a source guide. It is foundational for the local wiki architecture, but it is not itself enough to define every stable concept in the current vault.

- The article directly supports [[wiki/topics/AI Memory]] by separating persistent memory structures from per-query retrieval.
- It supports [[wiki/topics/Context Management]] because the wiki acts as a compiled context layer that can be selectively loaded rather than flooding the context window with raw material.
- It supports [[wiki/topics/AI Skills Workflow]] and [[wiki/concepts/Agent Skill]] because the schema and workflows behave like reusable operational knowledge for an LLM agent.
- It supports [[wiki/concepts/Feedback Flywheel]] and [[wiki/concepts/Harness Ratchet]] because valuable queries, lint findings, and source ingests should update durable control surfaces instead of remaining one-off conversations.
- It overlaps with [[wiki/sources/从知识堆积到结构化记忆 Source Guide]], which interprets LLM Wiki alongside Obsidian-Wiki, GBrain, and Skillify. This page preserves the primary Karpathy source itself; the Chinese source guide preserves a secondary comparative interpretation.
- It also explains why [[wiki/index]], [[wiki/log]], and [[wiki/hot]] are not incidental files: they are navigation, chronology, and recency-control surfaces for the wiki maintainer.

Source-level claims to keep bounded:

- The moderate-scale claim that `index.md` works well for around 100 sources and hundreds of pages is source-reported and should not become a universal capacity estimate without more evidence.
- The claim that LLM maintenance cost is "near zero" should be treated as directionally about bookkeeping effort, not as a guarantee of correctness, safety, or no review burden. ^[inferred]
- The Memex comparison is a conceptual analogy, not an implementation dependency.

## Open Questions

- What is the scale boundary where `index.md` stops being enough and hybrid search or graph tooling becomes necessary?
- How much human review is needed for source guides versus concept updates in high-stakes domains?
- Which parts of schema evolution should be manual, and which can be safely suggested or edited by an agent?
- How should a wiki distinguish raw-source truth, LLM-generated synthesis, and user-approved doctrine when the same page evolves many times?

## Related

- [[wiki/topics/AI Memory]]
- [[wiki/topics/Context Management]]
- [[wiki/topics/AI Skills Workflow]]
- [[wiki/concepts/Agent Skill]]
- [[wiki/concepts/Feedback Flywheel]]
- [[wiki/concepts/Harness Ratchet]]
- [[wiki/sources/从知识堆积到结构化记忆 Source Guide]]
- [[wiki/maps/AI Map]]
- [[wiki/index]]
- [[wiki/log]]
- [[wiki/hot]]
