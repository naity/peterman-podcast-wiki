# Log

## [2026-07-19] init | Wiki created
Domain: The Peterman Post podcast knowledge base (54 episodes, Jan 2025 – Jul 2026).
Structure per SCHEMA.md. Batch ingest of all 54 episodes begins.

## [2026-07-19] ingest | Batch ingest: all 54 podcast episodes
Fetched full transcripts to raw/ (47 complete; 6 early episodes are summary-only pages with no published transcript: n=1-5,7; 7 long episodes tail-truncated past ~1.5h by the fetch pipeline — flagged in frontmatter). Created 54 source pages, 62 guest+discussed-person pages, 26 org pages, 31 concept pages. Generated data/graph.json (54 episodes, 53 guests, 20 orgs, 31 concepts, 800+ edges) and index.md.

## [2026-07-19] lint | Post-ingest link check
62 broken links found and fixed: 9 missing entity pages created (netflix, airbnb, bell-labs, harvard, ucla, dropbox, shopify, edsger-dijkstra, mark-zuckerberg), one-off org/person links de-linked, truth-seeking concept folded into startups-and-founding.

## [2026-07-27] ingest | Episode 55: Creator of OCaml | Xavier Leroy
Fetched full transcript (1 chunk, complete, 01:23:28 runtime) to raw/, wrote source page, extract, episodes.json entry (n=55). New pages: entities/xavier-leroy.md, concepts/formal-verification.md (synthesizes Leroy + Lamport + Wigderson + SPJ + Stroustrup). Revised programming-languages (GC-vs-manual-memory caveat to Rust enthusiasm; industry-vs-academia inversion; type inference), functional-programming (OCaml systems-FP story), ai-coding-tools + ai-era-engineering + open-source (Leroy's "every new line of code is a liability" and AI-slop bug reports, dated 2026-07-20), hiring-and-interviews (OCaml as Jane Street hiring filter), regrets-and-advice (specialized too early). Cross-linked SPJ, Stroustrup, Lamport, Dijkstra entities and 5 episode Connections. Graph rebuilt: 55 episodes, 32 concepts, 830 links, 0 broken.
