---
type: entity
entity_kind: person
updated: 2026-07-19
sources: [openai-codex-tech-lead-on-how-his.md]
---

# Michael Bolin

Tech lead of [OpenAI](openai.md)'s Codex CLI; previously Distinguished Engineer (E9) at [Meta](meta.md), where he built the Buck build system, the Eden virtual filesystem, and Meta's IDE tooling ([episode](../sources/openai-codex-tech-lead-on-how-his.md)).

## Career arc

Left [Google](google.md) after four years because his passion projects (Google Tasks, Closure tools) weren't what Google valued — the seed of his career algorithm. At Facebook he built the Buck build system as a hackathon project against near-universal advice, with conviction from an "existence proof" (he'd seen Google's Blaze work); the iOS team asked for it a year later and Uber and Airbnb adopted it externally. After his E8 promo he failed a "hero quest" fixing facebook.com web speed, learning he succeeds on write-lots-of-code-from-scratch projects, not alignment-heavy ones. His E9 promo was delayed after he pushed too aggressively when [Microsoft](microsoft.md) acquired GitHub — he correctly predicted Nuclide's Atom foundation would lose to VS Code, but the lesson was about how he pushed, not what he argued. He built Eden (lazy file materialization for Meta's monorepo) and Myles (fuzzy file search over a million-plus files in 10-20ms). He joined OpenAI because building [dev tools](../concepts/developer-tools.md) on Llama 2 couldn't compete with GPT-4; Codex CLI launched rushed in April 2025, and the August 2025 confluence of GPT-5, a new TUI, and the VS Code extension drove it past 1M users ([episode](../sources/openai-codex-tech-lead-on-how-his.md)).

## Key views & advice

- Three-step career algorithm: figure out what you genuinely love, figure out what is invaluable to your employer, and lean hard into the intersection ([episode](../sources/openai-codex-tech-lead-on-how-his.md)).
- [Influence](../concepts/influence-and-leadership.md) tactic for disruptive projects without credibility: deliberately scope-couch them ("just an Android build system"), borrow credibility from a respected supporter, and let adoption come voluntarily ([episode](../sources/openai-codex-tech-lead-on-how-his.md)).
- On research-led vs engineering-led cultures: "if the model weren't very good, it wouldn't really matter what we did on the harness" ([episode](../sources/openai-codex-tech-lead-on-how-his.md)).
- On [AI coding tools](../concepts/ai-coding-tools.md): 80-90% of his code is now model-written, but he still hand-writes the security-critical sandboxing code in the Rust harness; the CLI is open source primarily so people can inspect an agent that runs on their machine. He believes most agent compute ultimately moves to the cloud ([episode](../sources/openai-codex-tech-lead-on-how-his.md)).
- Deep technical skills still matter because your questions bound the agent's output quality: read an OS textbook cover to cover, do CTFs as a "computer decathlon" — "it's kind of amazing and sad... how far many of us can get in software engineering without really having a clue how computers work" ([episode](../sources/openai-codex-tech-lead-on-how-his.md)).
- [Promotions](../concepts/promotions.md) lesson: recognize your triggers, don't act in the moment, go through managers; senior managers deserve more recognition for pairing senior ICs with the right projects. To his younger self: don't cling to your first programming language ([episode](../sources/openai-codex-tech-lead-on-how-his.md)).

## Related

- [Episode: OpenAI Codex Tech Lead On How His Career Grew](../sources/openai-codex-tech-lead-on-how-his.md) — his interview
- [Boris Cherny](../sources/boris-cherny-creator-of-claude-code.md) — creator of the competing coding agent, similar arc
- [Marc Brooker](marc-brooker.md) — parallel views on AI-era value of deep expertise
- [career growth](../concepts/career-growth.md), [open source](../concepts/open-source.md), [big tech culture](../concepts/big-tech-culture.md)
