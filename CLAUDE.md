# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This repository is a personal Hugo-based knowledge site.

There are three distinct content layers:
- `content/posts/`: published blog posts that Hugo renders into the site
- `wiki/`: the current canonical knowledge layer, organized as maps, concepts, topics, syntheses, and source guides
- `raw/`, `mobu/`, and `logseq/`: source material, legacy notes, and migration inputs that feed the structured wiki over time

The active Hugo theme is `devise` (`config.toml`), while `themes/zen` and `themes/simple` are present as older or alternative themes.

## Common commands

### Run the site locally
- `hugo server`

### Build the site
- `hugo`

### Deploy helper
- `./deploy-blog.sh`
  - builds the site with `hugo`
  - then commits and pushes the generated `public/` site repo
  - this script performs git operations in `public/`, so inspect before using

### Theme-related Node dependencies
The active `devise` theme has a `package.json` for frontend dependencies:
- `cd themes/devise && npm install`

The legacy `zen` theme has its own Node/Gulp toolchain:
- `cd themes/zen && npm install`
- `cd themes/zen && npm test`

There is no repo-wide lint or test harness beyond the theme-specific tooling above.

## Architecture

### Hugo site configuration
- Root site configuration lives in `config.toml`
- The site uses `theme = "devise"`
- Homepage behavior and recent-post selection are driven by `params.recent_posts` and `params.mainSections`
- Goldmark passthrough is enabled for math-style delimiters in Markdown

### Rendering flow
- `themes/devise/layouts/_default/baseof.html` defines the shared page shell with `head`, `header`, and `footer` partials
- `themes/devise/layouts/index.html` renders either homepage content or the default category-driven listing
- `themes/devise/layouts/partials/category-posts.html` builds the homepage listing: recent posts first, then posts grouped by category taxonomies
- `themes/devise/layouts/post/single.html` renders individual posts

### Styling model
- `themes/devise/layouts/partials/head.html` compiles Sass through Hugo Pipes
- `themes/devise/assets/sass/override.scss` is the main style override entrypoint; it imports Bootstrap and Font Awesome and applies site-specific typography/layout styling
- Theme colors and some typography are parameterized from `config.toml` via `.Param "style.*"`

### Knowledge organization
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

### Content migration model
The repository is in a transition from a mixed notes vault to a more structured “LLM Wiki”.
- New stable knowledge should generally land in `wiki/`
- `content/posts/` remains the public publishing layer
- `mobu/`, `raw/`, older notes, and Logseq artifacts are migration inputs rather than the canonical destination

## Working notes for future edits
- When changing site behavior, check both `config.toml` and the active `themes/devise/layouts/` templates
- When changing visual styling, start with `themes/devise/assets/sass/override.scss`
- Do not assume files under `wiki/` are published directly; published output is still driven by Hugo content under `content/posts/`
- Be careful around `deploy-blog.sh`: it assumes `public/` is a separate git checkout with a tracked `master` branch
