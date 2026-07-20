---
type: entity
entity_kind: person
updated: 2026-07-19
sources: [openai-eng-and-dev-tools-founder.md]
---

# Charlie Marsh

Founder of Astral, the [developer-tools](../concepts/developer-tools.md) company behind Ruff, uv, and Ty, acquired by [OpenAI](openai.md) ([episode](../sources/openai-eng-and-dev-tools-founder.md)).

## Career arc

Marsh worked across Python, Go, and Rust at a computational-biology startup, and that comparative perspective seeded Astral: JavaScript was embracing native tooling (esbuild, SWC, Bun) while Python tools were still written in Python ([episode](../sources/openai-eng-and-dev-tools-founder.md)). He shipped the Ruff prototype nine days after his "type checking at scale" blog post, deliberately [starting](../concepts/startups-and-founding.md) with a linter — useful immediately with a small core, unlike a 75%-done type checker — then capitalized on Hacker News attention by fixing reported issues within a day and courting figures like FastAPI's Sebastián Ramírez ([episode](../sources/openai-eng-and-dev-tools-founder.md)). Investors preemptively initiated all three raises (seed plus never-announced Series A and B); monetization came via the Pyx private registry funneled from free [open source](../concepts/open-source.md), and the company ended up acquired by OpenAI ([episode](../sources/openai-eng-and-dev-tools-founder.md)).

## Key views & advice

- He chose Rust "largely because of hype" but now calls it the best possible decision — Cargo made systems programming accessible — and would not start a net-new project in C or C++ today ([episode](../sources/openai-eng-and-dev-tools-founder.md)).
- Rust sets the performance floor, not the ceiling: uv's speed is mostly architecture (cache design; BurntSushi packing >90% of version objects into a single u64), and Ty does lazy incremental checking on rust-analyzer's Salsa framework ([episode](../sources/openai-eng-and-dev-tools-founder.md)).
- On [AI coding](../concepts/ai-coding-tools.md) and open source: "the cost of putting up a plausible PR has gone to zero, while the cost to review and vet a plausible PR has remained the same and is very high" — Astral requires contributors to understand what they submit, and he would block a Bun-style unreviewed agent rewrite of uv (Hyrum's Law: it trades known issues for unknown ones pushed onto millions of users) ([episode](../sources/openai-eng-and-dev-tools-founder.md)).
- Anti-slop tactics: heavy automated verification (benchmark and ecosystem-diff tests on every PR), encoding recurring review feedback into AGENTS.md, and reviewing your own PR as if you were the reviewer ([episode](../sources/openai-eng-and-dev-tools-founder.md)).
- "Being a great software engineer is more useful than ever" — the strongest engineers are also the best agent users; he thinks being early-career now would be very hard ([episode](../sources/openai-eng-and-dev-tools-founder.md)).
- Developer marketing is underrated: you get ~10 seconds to convey why a project matters; Ruff's benchmark graph was "priceless" ([episode](../sources/openai-eng-and-dev-tools-founder.md)).
- Most startup advice is survivorship bias — pick principles (remote, solo founder, minimal fundraising time) and stick to them ([episode](../sources/openai-eng-and-dev-tools-founder.md)).

## Related

- [Episode: OpenAI Eng & Dev Tools Founder: How Software Engineering Is Changing](../sources/openai-eng-and-dev-tools-founder.md) — his interview
- [Simon Peyton Jones](simon-peyton-jones.md) — type systems and the "compiler prunes LLM generation space" thesis Marsh builds tools for
- [James Cowling](james-cowling.md) — fellow infra founder on engineering rigor in the AI era
- [Bjarne Stroustrup](bjarne-stroustrup.md) — the skeptical counterpoint on AI-generated code
- [developer-tools](../concepts/developer-tools.md), [ai-era-engineering](../concepts/ai-era-engineering.md), [open-source](../concepts/open-source.md), [programming-languages](../concepts/programming-languages.md)
