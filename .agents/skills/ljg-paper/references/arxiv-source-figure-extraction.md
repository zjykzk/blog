# arXiv source and figure extraction workflow

Use this when reading an arXiv paper and the PDF text or embedded figures need more reliable extraction than the PDF alone.

## Pattern

1. Download the PDF for the reading source.
2. Also fetch the arXiv source package:
   - `https://arxiv.org/e-print/<paper-id>`
   - Extract it into a temp directory.
3. Read the main `.tex` file for:
   - exact abstract, authors, captions, section structure
   - figure filenames and captions
   - experiment claims and numeric values that may be hard to extract from the PDF
4. Convert important PDF figures to PNG before visual inspection:
   - `magick -density 200 figure.pdf -quality 90 figure.png`
5. Use image/vision inspection for plots when the paper only gives trends in captions:
   - axes and methods
   - approximate values at key points
   - baseline vs proposed method comparisons
6. Save only the one overview/architecture figure that carries the paper's core story into `~/Documents/notes/images/` using the skill's Denote image naming rule. Do not save every plot unless the note needs it.

## Why this matters

The PDF text layer often mangles equations, captions, and figure labels. The arXiv source gives exact captions and figure file names, while converted plots let the agent read numeric evidence without inventing values.

## Pitfall

Do not encode transient local setup failures as skill rules. If a binary is missing, use an available alternative in the environment, but record the durable workflow: source package + TeX captions + figure conversion + vision-assisted plot reading.