# Log

## [2026-07-19] init | Wiki created
Domain: The Peterman Post podcast knowledge base (54 episodes, Jan 2025 – Jul 2026).
Structure per SCHEMA.md. Batch ingest of all 54 episodes begins.

## [2026-07-19] ingest | Batch ingest: all 54 podcast episodes
Fetched full transcripts to raw/ (47 complete; 6 early episodes are summary-only pages with no published transcript: n=1-5,7; 7 long episodes tail-truncated past ~1.5h by the fetch pipeline — flagged in frontmatter). Created 54 source pages, 62 guest+discussed-person pages, 26 org pages, 31 concept pages. Generated data/graph.json (54 episodes, 53 guests, 20 orgs, 31 concepts, 800+ edges) and index.md.

## [2026-07-19] lint | Post-ingest link check
62 broken links found and fixed: 9 missing entity pages created (netflix, airbnb, bell-labs, harvard, ucla, dropbox, shopify, edsger-dijkstra, mark-zuckerberg), one-off org/person links de-linked, truth-seeking concept folded into startups-and-founding.
