# Entity / concept page instructions (phase 2 subagents)

Wiki root: /home/claude/peterman-wiki. Inputs you may read: data/episodes.json, data/extracts/*.json (structured per-episode data), sources/*.md (episode summary pages). Do NOT read raw/ transcripts unless a specific fact needs checking — sources + extracts are sufficient.

General rules:
- Filenames: lowercase-kebab-case under entities/ or concepts/.
- Relative links: to an episode page `[Title](../sources/<slug>.md)`, to an entity `[Name](../entities/<slug>.md)` (or `<slug>.md` if linking from within the same directory), to a concept `[name](../concepts/<slug>.md)`.
- Every claim cites at least one episode source page inline.
- Write for a reader who hasn't heard the episodes: dense, specific, no filler. Short is fine.
- Do not edit index.md or log.md (the coordinator handles those).

## Guest entity page (entities/<guest_slug>.md)

```
---
type: entity
entity_kind: person
updated: 2026-07-19
sources: [<episode-slug>.md, ...]
---

# <Guest name>

<1–2 sentences: who they are, current/peak role.>

## Career arc
<Compact narrative of their path as told in the episode(s), with companies linked to org entity pages where those exist (major orgs only — see list below).>

## Key views & advice
<Their most distinctive positions and advice, cited to the episode: e.g. "Argues promo-oriented behavior backfires ([episode](../sources/<slug>.md))." Link concepts on first mention.>

## Related
- [Episode: <title>](../sources/<slug>.md) — their interview
- <links to related people/orgs/concepts with a phrase each>
```

For anonymous guests, title the page with their descriptor (e.g. "Meta IC7 (demotion story)") and use the guest_slug from the extract.

## Org entity page (entities/<org_slug>.md)

Only these orgs get pages: meta, instagram, google, microsoft, amazon, aws, openai, anthropic, apple, ibm, intel, nvidia, stripe, uber, mozilla, snapchat, mit, stanford, uc-berkeley, harvard, netflix, dropbox, shopify, airbnb, bell-labs. Link other orgs as plain text.

```
---
type: entity
entity_kind: org
updated: 2026-07-19
sources: [<episode-slug>.md, ...]
---

# <Org name>

<1–2 sentences on the org and why it recurs in this podcast.>

## What the episodes reveal
<Synthesis of what guests said about working there — culture, promo system, eng practices, stories — each point cited. Where guests disagree, present both views attributed and dated.>

## People
<Guests who worked there, linked, with role.>

## Related
<Concepts strongly associated with this org in the episodes.>
```

## Concept page (concepts/<concept_slug>.md)

```
---
type: concept
updated: 2026-07-19
sources: [<episode-slug>.md, ...]
---

# <Concept name (human-readable title)>

<1–2 sentences defining the theme as it appears in the podcast.>

## What the guests say
<The heart of the page: synthesis ACROSS episodes. Organize by sub-question or position, not by episode. Attribute every view: "Ilya Grigorik argues X ([episode](../sources/distinguished-engineer-at-shopify.md)), while Ethan Evans counters Y ([episode](../sources/amazon-vp-on-promotions-getting-fired.md))." Explicitly flag disagreements and tensions between guests — these are the most valuable content.>

## Practical takeaways
<3–7 actionable distillations with citations.>

## Related
<Links to adjacent concepts, key people for this theme, and the most relevant episodes.>
```

To find which episodes touch a concept: `grep -l "<concept-slug>" data/extracts/*.json` and read those extracts/source pages.

## Final report
Return one line per page written: path — 1-line description. Nothing else.
