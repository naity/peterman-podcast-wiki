# Wiki Schema

## Domain
Knowledge base for The Peterman Post podcast (Ryan Peterman, developing.dev) — 54 episodes (Jan 2025 – Jul 2026) of interviews with senior/distinguished engineers, Turing Award winners, CTOs, and founders about software careers, engineering leadership, and computer science. Yuan wants a browsable, interlinked knowledge base with a knowledge graph, episode summaries, and cross-episode connections, plus a web app built on top of it (app/index.html, data/graph.json).

## Structure
- `raw/` — full verbatim episode transcripts, one markdown file per episode, named by Substack slug (e.g. `turing-award-winner-tpu-vs-gpu-vs.md`). READ ONLY.
- `sources/` — one summary page per episode (same slug). Frontmatter includes `guest`, `date`, `url` in addition to standard fields.
- `entities/` — people (guests, frequently-discussed figures) and organizations (companies, labs). Frontmatter `entity_kind: person | org`.
- `concepts/` — recurring themes: promotions, career growth, AI-era engineering, distributed systems, hiring, management, etc.
- `notes/` — filed analyses and syntheses.
- `data/` — machine-readable layer: `episodes.json` (manifest), `extracts/<slug>.json` (per-episode structured extraction), `graph.json` (knowledge graph consumed by the web app).
- `app/` — single-file HTML web app (knowledge graph viz + episode explorer).

## Conventions
- Episode source pages carry extra frontmatter: `guest`, `guest_role`, `date` (publish date), `url` (developing.dev link).
- Every source page cites its raw transcript; every claim on entity/concept pages cites episode source pages.
- Per-episode extracts (data/extracts/) follow the JSON shape documented in data/episodes.json's sibling README comment: {slug, title, guest, guest_role, companies[], concepts[], key_takeaways[], notable_quotes[], related_slugs[]}.
- Concept slugs are kebab-case and singular-theme (e.g. `promotions`, `ai-era-engineering`).

## Workflow preferences
- Batch-ingested at init (all 54 episodes) via parallel agents; user reviews via the web app and the log.
- A weekly scheduled task ("Peterman Post weekly episode ingest", Mondays 7:06am PT) checks the archive API and fully ingests any new episode: git pull → transcript → source page → extract → entity/concept integration → `python3 data/build_graph_index.py` → `python3 data/rebuild_app.py` → git commit+push → SendUserFile + update_artifact (id: peterman-podcast-knowledge-graph). No-new-episode runs just append a `check` line to log.md and push.
- The GitHub repo (https://github.com/naity/peterman-podcast-wiki) is the durable source of truth. Every push triggers .github/workflows/deploy.yml: rebuild graph + app, fail on broken links, deploy app/ to GitHub Pages at https://naity.github.io/peterman-podcast-wiki/.
- Rebuild pipeline after ANY wiki change: build_graph_index.py (also lints links; fix until 0 broken), then rebuild_app.py.

## Synthesis
The web app (app/index.html) is the primary consumption surface; data/graph.json is regenerated from data/extracts/ whenever the wiki changes.
