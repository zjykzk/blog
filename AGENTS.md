# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This repository is a personal knowledge base centered on the structured `wiki/` directory.

There are three distinct content layers:
- `wiki/`: the current canonical knowledge layer, organized as maps, concepts, topics, syntheses, and source guides
- `raw/`, `mobu/`, and `logseq/`: source material, legacy notes, and migration inputs that feed the structured wiki over time
- `content/posts/`: a separate publishing layer rather than the canonical destination for stable knowledge

## Knowledge organization

`wiki/` is the main long-term knowledge layer, not a scratch directory.

Key structure:
- `wiki/maps/`: map-of-content entry points
- `wiki/concepts/`: stable concept pages
- `wiki/topics/`: long-running topic pages
- `wiki/syntheses/`: cross-source synthesis pages
- `wiki/sources/`: structured guides to raw or imported material

Important entrypoints:
- `wiki/index.md`: actual wiki homepage and navigation hub
- `wiki/NAMING.md`: naming and placement rules for the wiki
- `wiki/Welcome.md`: legacy page kept only for historical clarity, not as the homepage

## Content migration model

The repository is in a transition from a mixed notes vault to a more structured “LLM Wiki”.
- New stable knowledge should generally land in `wiki/`
- `content/posts/` is not the canonical destination for long-term knowledge
- `mobu/`, `raw/`, older notes, and Logseq artifacts are migration inputs rather than the canonical destination

## Working notes for future edits
- Prefer organizing durable knowledge under `wiki/` instead of adding new material to legacy note areas
- Do not treat `wiki/Welcome.md` as the homepage when updating navigation or entrypoints
- When classifying new material, use the structure in `wiki/NAMING.md`
