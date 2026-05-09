---
title: >-
  How LLMs Actually Work Source Guide
type: source
status: seed
category: sources
tags:
  - source
  - ai
  - llm
  - transformer
  - security
sources:
  - conversation:2026-05-09
created: 2026-05-09T21:19:58+08:00
updated: 2026-05-09T21:19:58+08:00
summary: >-
  Source guide for an interactive walkthrough of the LLM pipeline, from web data and tokenization through pretraining, post-training, RAG, and security.
provenance:
  extracted: 0.93
  inferred: 0.07
  ambiguous: 0.0
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-05-09
aliases:
  - How LLMs Actually Work
  - Karpathy LLM Walkthrough
  - From Text to Assistant
---

# How LLMs Actually Work Source Guide

> Source: inline paste of an interactive walkthrough titled "How LLMs Actually Work", based on Andrej Karpathy's technical deep dive.

## What It Covers

This source explains the full lifecycle of a large language model: collecting and filtering internet-scale text, tokenizing it, pretraining a transformer through next-token prediction, sampling tokens at inference time, converting the base model into an assistant through SFT and RLHF, and then operating the assistant with retrieval and security constraints.

Its central contribution is a layered mental model: an LLM assistant is not a single magic object, but a pipeline connecting data curation, representation, learned tensor computation, conversation imitation, preference optimization, external retrieval, tool use, and adversarial surfaces.

## Key Points

- Frontier-scale LLM training starts with enormous web-scale corpora, but filtering quality and diversity matter more than raw volume alone.
- Common Crawl-style raw web data is progressively filtered through URL blocklists, text extraction, language filtering, deduplication, and PII removal before becoming a curated pretraining corpus.
- [[wiki/concepts/Tokenization]] turns text into numeric token IDs; Byte Pair Encoding balances vocabulary size against sequence length by merging frequent adjacent byte or character patterns.
- A transformer begins as random parameters and learns by repeatedly predicting the next token, comparing that prediction with the true next token, and nudging weights by gradient descent.
- Scaling laws frame model quality as a smooth function of parameter count and training tokens, which explains the GPU arms race around larger models and larger datasets.
- Embeddings map token IDs into learned vectors; later attention layers contextualize those vectors so the same token can carry different meanings in different sequences.
- [[wiki/concepts/Autoregressive Decoding]] generates text one token at a time: the model returns a probability distribution over the vocabulary, a token is sampled, and that token becomes part of the next input.
- Temperature changes how broadly sampling explores the distribution: low temperature collapses toward the top token, while high temperature increases randomness.
- The base model is an internet document simulator, not an assistant: it continues token sequences according to learned statistical structure rather than following user intent as a stable role.
- In-context learning lets base models infer tasks such as translation or classification from examples in the context window without weight updates.
- The model's weights are a lossy compression of training data, not a database; memorized facts, plausible completions, and hallucinations all come from the same continuation mechanism.
- Supervised fine-tuning turns a base model toward assistant behavior by continuing training on idealized conversation examples.
- RLHF trains a reward model from human preference rankings, then optimizes the assistant to produce responses that receive higher preference scores.
- The assistant can be read as a statistical simulation of expert labeler behavior under labeling instructions, not as a self with stable independent knowledge.
- The context window functions as precise working memory, while parameters function as vague long-term memory; important current facts should be placed in context rather than assumed from weights.
- Tool use works by letting the model emit tool-call tokens or structured actions, pausing generation, executing external software, and injecting the result back into context.
- Retrieval-Augmented Generation embeds documents, retrieves semantically close chunks at query time, and injects them into context so generation is grounded in current external facts rather than only in memorized training data.
- Prompt injection appears because models process external content and user instructions through the same text-conditioned mechanism; they cannot reliably separate trusted instruction from malicious instruction by default.
- Jailbreaks, data poisoning, adversarial multimodal inputs, and prompt injection make LLM security a cat-and-mouse field where patching one attack pattern may not remove the underlying attack generator.
- The OS metaphor maps files or the internet to disk, the context window to RAM, GPU inference to CPU-like compute, and tools/retrieval to system calls around the model. ^[inferred]

## Integration Decisions

This source should be treated as a broad source-level walkthrough rather than a single stable concept page. Several parts already map onto existing wiki pages:

- The pretraining, tokenization, and sampling path strengthens [[wiki/concepts/LLM]], [[wiki/concepts/Tokenization]], [[wiki/concepts/Next-Token Pipeline]], and [[wiki/topics/LLM Inference Systems]].
- The base-model and assistant distinction clarifies why post-training is a role-shaping layer, not the same thing as pretraining knowledge.
- The RAG section connects [[wiki/topics/AI Memory]] and [[wiki/topics/Context Management]]: persistent external knowledge must be retrieved into the active context before it can steer inference.
- The security section belongs with the agent and harness cluster because prompt injection is a control-boundary problem around tools, retrieval, browsing, and multimodal input. ^[inferred]

## Open Questions

- Which exact figures in the walkthrough are illustrative rather than tied to a specific named frontier model? The source says representative figures shift by release, so the scale should be preserved more strongly than the exact numbers.
- Should the wiki promote RAG into its own concept page, or keep it as part of context management and AI memory until more sources accumulate? ^[inferred]
- How should the base-model-to-assistant distinction be represented without overstating SFT/RLHF as the only post-training path? ^[inferred]

## Related

- [[wiki/concepts/LLM]]
- [[wiki/concepts/Tokenization]]
- [[wiki/concepts/Next-Token Pipeline]]
- [[wiki/concepts/Autoregressive Decoding]]
- [[wiki/topics/LLM Inference Systems]]
- [[wiki/topics/AI Memory]]
- [[wiki/topics/Context Management]]
- [[wiki/maps/AI Map]]
