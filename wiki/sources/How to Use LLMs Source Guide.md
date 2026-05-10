---
title: >-
  How to Use LLMs Source Guide
type: source
status: seed
category: sources
tags:
  - llm
  - workflow
  - tools
sources:
  - conversation:2026-05-09
created: 2026-05-09T21:26:53+08:00
updated: 2026-05-09T21:26:53+08:00
summary: >-
  Source guide for Karpathy's practical LLM-use walkthrough: model choice, search, deep research, documents, code, agents, voice, vision, and memory.
provenance:
  extracted: 0.93
  inferred: 0.07
  ambiguous: 0.0
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-05-09
aliases:
  - How to Use LLMs
  - Karpathy LLM Usage Walkthrough
  - Practical LLM Use
---
# How to Use LLMs Source Guide

> Source: inline paste of an interactive walkthrough titled "How to Use LLMs", based on Andrej Karpathy's 2025 follow-up to his LLM deep dive.

## What It Covers

This source explains how to use LLM products in daily work once the internal model is understood. It shifts from model mechanics to operating practice: when to trust weights, when to search, when to use deep research, how to read documents with models, how to use code execution, how to work with coding agents, when voice or vision is useful, and how persistent memory or custom instructions shape interaction.

Its central mental model is that an LLM product is a probabilistic compressed snapshot of internet text plus a bounded working-memory context window and optional surrounding tools. Effective use depends on matching the task to the right combination of weights, retrieval, tools, model tier, modality, and verification loop.

## Key Points

- ChatGPT can be treated as a "one-tab ZIP file": a compressed, stale, probabilistic recollection of internet-scale training data rather than a live database or guaranteed source of truth.
- The context window is the model's working memory; information inside it is directly usable, while information outside it does not exist for the current conversation.
- For timeless, well-documented knowledge, model weights can be enough; for recent, changing, niche, or esoteric information, search or a search-first product such as Perplexity is safer.
- Model selection should follow task shape: fast general models suit simple work, thinking models suit hard math or formal reasoning, Claude is often strong for coding and documents, and search-first systems suit source-grounded research.
- LM Arena is presented as a useful external signal for comparing model quality because model rankings shift quickly.
- Thinking models spend more inference time exploring, checking, and backtracking before producing an answer; they are useful when the task benefits from deliberation, but wasteful for simple requests.
- Deep Research combines extended reasoning with web search over many sources to produce a structured multi-source report; it fits literature reviews, competitive analysis, due diligence, and research-heavy questions.
- Document attachment turns the model into a reading assistant: summarize, ask section-level questions, build concept maps, and verify claims against the attached text.
- Mermaid diagrams are useful as a bridge from document reading to structural understanding because they force the model to express relationships, not just prose summaries.
- Code execution is appropriate when the task requires arithmetic, statistics, data cleaning, transformation, or visualization; the model can write and run Python, but outputs still need source-level verification.
- A correct-looking chart can still contain hallucinated or misread values; verification should inspect the generated code and the numeric source data, not only the visual shape.
- Agentic coding tools such as Cursor and Windsurf wrap the model in an editor-level loop: plan, edit files, run commands, observe errors, and iterate with user approval around risky actions.
- Coding agents are strongest when the user understands the model well enough to guide, constrain, and correct it; the workflow is not merely prompt-and-hope.
- Voice input reduces interaction friction for natural-language queries, but typed input remains better for product names, library names, and technical vocabulary that speech transcription may mishear.
- Native advanced voice differs from transcription-plus-text-to-speech because audio tokens flow directly through the model interface. ^[inferred]
- NotebookLM-style audio generation can turn uploaded documents into passive learning material, especially for walks or drives.
- Vision input works well for common, well-documented visual domains such as screenshots, lab panels, charts, famous maps, and consumer devices, but rare or proprietary visual objects have higher hallucination risk.
- Custom instructions act like a persistent personal system prompt, compressing preferences and background that would otherwise be repeated every session.
- Persistent memory changes the default statelessness of chat by carrying selected facts across sessions, but the user should still manage what is worth remembering.
- The practical rule is to match the tool to the uncertainty source: stale knowledge calls for search, complex synthesis calls for deep research, exact computation calls for code, large documents call for attachment, and repeated preferences call for memory or custom instructions. ^[inferred]

## Integration Decisions

This source should remain a source guide rather than become a single broad concept page. It is a practical operating manual that connects many existing pages rather than defining one new stable concept.

- The foundation section strengthens [[wiki/concepts/LLM]], [[wiki/topics/Context Management]], and [[wiki/topics/AI Memory]] by turning the weights/context distinction into a user-facing reliability rule.
- The search and deep-research sections connect to [[wiki/concepts/AI Learning Tutor Loop]] because useful AI learning workflows depend on source grounding, disagreement mapping, and diagnostic follow-up rather than summaries alone.
- The code-execution and data-analysis sections connect to [[wiki/concepts/Verification Loop]]: executable tools improve capability, but also create a need to verify code, numbers, and assumptions.
- The agentic coding section belongs with [[wiki/concepts/Agentic Engineering]], [[wiki/concepts/Coding Agent User Harness]], and [[wiki/topics/AI Harness]] because practical coding productivity comes from harnessed loops, checks, permissions, and human steering.
- The personalization section should inform future pages on user-level AI operating systems or personal harnesses, but it does not yet require a separate concept page. ^[inferred]

## Open Questions

- Which recommendations are stable usage principles and which are product-specific to the 2025 ChatGPT, Claude, Perplexity, Cursor, and NotebookLM landscape? ^[ambiguous]
- Should "when to search" become a separate concept page, or stay under context management until more sources accumulate? ^[inferred]
- How should the wiki distinguish personal LLM usage workflows from production agent harness engineering without duplicating the same context/tool/verification ideas? ^[inferred]

## Related

- [[wiki/concepts/LLM]]
- [[wiki/topics/Context Management]]
- [[wiki/topics/AI Memory]]
- [[wiki/concepts/AI Learning Tutor Loop]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/concepts/Agentic Engineering]]
- [[wiki/concepts/Coding Agent User Harness]]
- [[wiki/topics/AI Harness]]
- [[wiki/maps/AI Map]]
