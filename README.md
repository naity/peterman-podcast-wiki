# The Peterman Post — Podcast Knowledge Base

An interlinked knowledge base built from the episodes of [The Peterman Post](https://www.developing.dev/podcast), Ryan Peterman's podcast of interviews with Turing Award winners, distinguished engineers, CTOs, and founders about software careers and computer science.

**Explore the knowledge graph:** https://naity.github.io/peterman-podcast-wiki/

## What's here

- `raw/` — verbatim episode transcripts (one markdown file per episode)
- `sources/` — one summary page per episode: key takeaways, notable quotes, connections
- `entities/` — pages for every guest, plus recurring organizations and figures
- `concepts/` — cross-episode syntheses of recurring themes (promotions, AI-era engineering, distributed systems, …), including where guests disagree
- `notes/` — filed analyses and query answers
- `data/` — episode manifest, per-episode structured extracts, knowledge-graph JSON, and build scripts
- `app/` — the interactive knowledge-graph explorer (a single self-contained HTML file, deployed via GitHub Pages)
- `index.md` / `log.md` / `SCHEMA.md` — the wiki's catalog, change log, and conventions

The folder is plain interlinked markdown — it also works as an Obsidian vault out of the box.

## How it updates

A weekly automation checks for newly published episodes each Monday, ingests the transcript, integrates it across the wiki, and pushes a commit. The push triggers the GitHub Actions workflow, which rebuilds the graph and app, fails if any wiki links are broken, and redeploys the site.

To rebuild locally after editing:

```bash
python3 data/build_graph_index.py   # regenerates data/graph.json + index.md, lints links
python3 data/rebuild_app.py         # regenerates app/index.html
```

## Attribution

All podcast content — episodes, transcripts, and quotes — belongs to **Ryan Peterman / developing.dev**. This is an unofficial fan-made knowledge base for personal study; if you find it useful, subscribe to [developing.dev](https://www.developing.dev/). Available at the copyright holder's request to take down.
