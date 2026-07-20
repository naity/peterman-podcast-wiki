# Episode fetch + ingest instructions (for subagents)

You are processing episodes of The Peterman Post podcast (developing.dev, host Ryan Peterman) into a wiki at /home/claude/peterman-wiki. For EACH episode slug you were assigned, do steps 1–4 completely before moving to the next episode.

The full episode manifest is at /home/claude/peterman-wiki/data/episodes.json (read it once at the start — you need it for metadata and for suggesting related episodes).

## Step 1 — Fetch the full transcript in verbatim chunks

Episode URL: `https://www.developing.dev/p/<slug>`

NEVER use curl/wget/python to fetch anything. Use ONLY the WebFetch tool.

First call — prompt:
"Reproduce VERBATIM: (1) the episode title, guest name and publish date; (2) the host's intro paragraphs; (3) the full Timestamps list; (4) the transcript from its very beginning, word for word with speaker labels, section headings and timestamp markers, until you run out of output space. Do NOT summarize or paraphrase. End your output with the line 'LAST POINT REACHED: <last timestamp you output>'."

Immediately after each WebFetch returns, Write the chunk to /home/claude/peterman-wiki/raw/.parts/<slug>/part-01.md (then part-02.md, etc.). Do this BEFORE the next fetch.

Continuation calls (the URL is cached for 15 min, so repeated fetches are cheap) — prompt:
"This page contains a podcast transcript. Reproduce VERBATIM the transcript starting exactly at timestamp <X> (speaker labels, headings, timestamp markers included), continuing word for word until you run out of output space. Do not repeat anything before <X>. Do not summarize. End with 'LAST POINT REACHED: <last timestamp>' or, if you reached the transcript's end, 'TRANSCRIPT COMPLETE'."

Repeat until TRANSCRIPT COMPLETE (or the last timestamp matches the final section and the text clearly ends, e.g. sign-off/outro). Typical episodes are 40–75 minutes and need 3–7 chunks. If two consecutive continuation calls make no progress, note it and move on — record the gap in your final report.

## Step 2 — Assemble raw transcript

Concatenate the parts into /home/claude/peterman-wiki/raw/<slug>.md using Bash `cat`, then use Edit to remove any duplicated overlap at the seams (a few repeated lines are common; trim them so the transcript reads continuously). Prepend YAML frontmatter:

```
---
type: raw-transcript
slug: <slug>
title: "<full title>"
guest: "<guest name, or 'unnamed' if anonymous>"
date: <publish date YYYY-MM-DD>
url: https://www.developing.dev/p/<slug>
fetched: 2026-07-19
complete: true|false   # false if any gap remains
---
```

Keep the host intro, timestamps list, and full transcript. Delete the .parts/<slug>/ directory afterward.

## Step 3 — Write the episode source page

Write /home/claude/peterman-wiki/sources/<slug>.md:

```
---
type: source
updated: 2026-07-19
raw: ../raw/<slug>.md
guest: "<guest name>"
guest_role: "<short role, e.g. 'Turing Award winner, UC Berkeley professor'>"
date: <publish date>
url: https://www.developing.dev/p/<slug>
---

# <Episode title>

<One paragraph: who the guest is, what the episode covers, why it's interesting.>

## Key takeaways
<5–10 information-dense bullets of the episode's most valuable points — specific advice, stories, claims, numbers. Link companies/people as [Name](../entities/<kebab-slug>.md) and themes as [theme](../concepts/<concept-slug>.md) on first mention.>

## Notable quotes
<2–4 short verbatim quotes with speaker attribution and rough timestamp.>

## Connections
<Which other episodes in the manifest this connects to and why (by title, linked as [Title](<other-slug>.md)) — shared guest, same company, same theme, contrasting opinion.>
```

Concept slugs — use these where they fit (add new kebab-case ones only when genuinely needed): promotions, career-growth, calibrations-and-ratings, management, hiring-and-interviews, layoffs, ai-era-engineering, ai-coding-tools, distributed-systems, computer-architecture, programming-languages, databases, security-and-cryptography, complexity-theory, functional-programming, developer-tools, startups-and-founding, big-tech-culture, influence-and-leadership, imposter-syndrome, regrets-and-advice, incident-management, open-source, teaching-and-communication, mentorship-and-sponsorship, corporate-politics, compensation-and-equity, non-linear-careers, working-with-legends, systems-design.

Entity slugs: kebab-case person or org name (e.g. `david-patterson`, `meta`, `amazon`, `openai`).

## Step 4 — Write the structured extract

Write /home/claude/peterman-wiki/data/extracts/<slug>.json:

```json
{
  "slug": "...",
  "n": <episode number from manifest>,
  "title": "...",
  "date": "YYYY-MM-DD",
  "url": "https://www.developing.dev/p/<slug>",
  "guest": "<name or 'unnamed'>",
  "guest_role": "...",
  "guest_slug": "<kebab-case, e.g. 'david-patterson'; for anonymous guests use the episode's descriptor e.g. 'meta-ic7-demotion-guest'>",
  "companies": ["meta", "openai", ...],
  "concepts": ["promotions", "career-growth", ...],
  "sections": [{"t": "00:42", "title": "RISC vs CISC"}, ...],
  "key_takeaways": ["...", ...],
  "notable_quotes": [{"speaker": "...", "quote": "...", "t": "12:34"}],
  "related": [{"slug": "<other-episode-slug>", "reason": "short reason"}],
  "transcript_complete": true
}
```

- companies: orgs substantively discussed (worked at, deep stories), not passing mentions. Use canonical slugs: meta, instagram (use meta AND instagram if IG-specific), google, google-deepmind, amazon, aws, microsoft, apple, openai, anthropic, netflix, stripe, dropbox, uber, airbnb, shopify, mozilla, robinhood, cloudkitchens, snapchat, citadel, intel, ibm, bell-labs, mit, stanford, uc-berkeley, harvard, ucla, nvidia.
- related: 2–5 episodes from the manifest, best matches only.
- key_takeaways: 5–10, each one self-contained sentence(s).

## Final report

Return (as your final message) one line per episode: slug — guest — transcript complete? — # chunks — any problems. Nothing else.
