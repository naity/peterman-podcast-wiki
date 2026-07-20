---
type: source
updated: 2026-07-19
raw: ../raw/openai-eng-and-dev-tools-founder.md
guest: "Charlie Marsh"
guest_role: "Founder of Astral (Ruff, uv, Ty), acquired by OpenAI"
date: 2026-06-22
url: https://www.developing.dev/p/openai-eng-and-dev-tools-founder
---

# OpenAI Eng & Dev Tools Founder: How Software Engineering Is Changing | Charlie Marsh

Charlie Marsh is the founder of Astral, the Python devtool startup behind Ruff, uv, and the Ty type checker, which was acquired by [OpenAI](../entities/openai.md). The episode traces how a second engineer at a computational-biology startup turned a "Python tooling could be much faster" hypothesis into tools used by millions, and digs into how agents (Codex especially) are reshaping how his team writes, reviews, and optimizes software — plus candid lessons from founding and fundraising as a lifelong IC engineer.

## Key takeaways

- The origin insight behind [developer-tools](../concepts/developer-tools.md) startup Astral was comparative: Charlie had worked across Python, Go, and Rust ecosystems and saw the JavaScript world embracing native tooling (esbuild, SWC, Bun, Deno) while Python tools were still written in Python. Ruff started as a hypothesis test — the prototype followed his "type checking at scale" blog post by just nine days.
- He deliberately started with a linter rather than a type checker or package manager because a linter is useful immediately with a small core plus rules, letting him ship iteratively and build momentum — a 75%-done type checker is useless. A startup lesson in picking the right first form factor ([startups-and-founding](../concepts/startups-and-founding.md)).
- On [open-source](../concepts/open-source.md) traction: after hitting Hacker News he capitalized by acknowledging, fixing, and releasing within one day of issue reports, and courting high-profile ecosystem figures like Sebastián Ramírez (FastAPI). He argues developer marketing is underrated — you have ~10 seconds to convey why a project matters, and the viral Ruff benchmark graph was "priceless" for attention.
- He chose Rust "largely because of hype" but now considers it the best possible choice, crediting Cargo's opinionated tooling with making systems programming accessible; he would not start a new project in C/C++ today ([programming-languages](../concepts/programming-languages.md)).
- Rust is the performance floor, not the ceiling: uv's speed comes as much from architecture (a cache design making repeat installs near-instant; BurntSushi's representation of >90% of version objects in a single u64) as from the language. Ty is built for lazy, incremental checking on the Salsa query framework used by rust-analyzer.
- On the Bun Zig-to-Rust agent rewrite: he's glad someone is pushing the envelope but wouldn't do it for uv — Hyrum's Law means an automated rewrite trades known issues for unknown ones pushed onto users, and no human meaningfully reviewed that code. He'd block a similar rewrite at Astral today ([ai-era-engineering](../concepts/ai-era-engineering.md)).
- Astral's open-source AI policy: agent-written contributions are fine only if the contributor understands what they're submitting, because the cost of a plausible PR has gone to zero while the cost of reviewing it stays high — on Ty a two-minute agent PR can take maintainers an hour to vet, and compounding mentorship of contributors is disappearing.
- Combating gray-area AI slop ([ai-coding-tools](../concepts/ai-coding-tools.md)): heavy automated verification (Valgrind/CodSpeed memory and time benchmarks on every PR, ecosystem-wide diagnostic diff tests), assuming everyone runs Codex Review before pushing, encoding recurring review feedback into AGENTS.md and shared skills, and personally reviewing your own PR in the GitHub UI as if you were the reviewer.
- A teammate told him "I used to review your PRs minimally because I trusted your work; now I have to review closely because the agent writes them" — a moment that made him confront how easy it is to accept work below your former standard. He remains "slightly concerned" how much garbage he'd churn out using these tools without engineering experience, and thinks being an early-career engineer right now would be very hard ([career-growth](../concepts/career-growth.md)).
- Founding lessons: investors preemptively initiated all three raises (seed, unannounced Series A and B); an investor telling him "you can give the money back in six months if you hate it" lowered the pressure to start; monetization was a hosted private registry (Pyx) funneled from free open-source tools; and his meta-advice is that startup advice is survivorship bias — pick principles (he stayed remote, solo-founder, minimal fundraising time) and stick to them ([regrets-and-advice](../concepts/regrets-and-advice.md)).

## Notable quotes

- "The cost of putting up a plausible PR has gone to zero, while the cost to review and vet a plausible PR has remained the same and is very high." — Charlie Marsh, ~32:19
- "It used to be the case that whenever you put up a PR, I could review it pretty minimally because I had a lot of confidence in your work. And now... I actually have to review it really closely because you're not writing anymore." — Charlie Marsh (quoting a teammate), ~48:14
- "Being a great software engineer is more useful than ever... the people on our team who have the strongest engineering skills are the most effective, even at using agents." — Charlie Marsh, ~59:24
- "I largely chose Rust for that project because of hype... In hindsight, I think it was an amazing decision, and I absolutely would not do it differently." — Charlie Marsh, ~14:57

## Connections

- [OpenAI Codex Tech Lead On How His Career Grew And How He Uses Codex | Michael Bolin](openai-codex-tech-lead-on-how-his.md) — Charlie now works at OpenAI and describes Codex-centric workflows; Bolin builds Codex itself.
- [Boris Cherny (Creator of Claude Code) On How His Career Grew](boris-cherny-creator-of-claude-code.md) — fellow AI coding-tool builder; contrasting Anthropic-side view of agentic engineering.
- [Dropbox's Former Most Senior Eng: Building Great Systems and Advice for the AI Era | James Cowling](dropboxs-former-most-senior-eng-building.md) — shared theme of maintaining engineering rigor and systems thinking as AI changes the job.
- [AWS Distinguished Eng: Learnings From 3000 Incidents And How Engineering Is Changing | Marc Brooker](aws-distinguished-eng-learnings-from.md) — another senior engineer's take on how engineering practice is changing with AI.
- [Robinhood SWE Turned $1B+ Founder on Non-Linear Careers, Being Jaded About Promos, Startup Learnings](quitting-robinhood-and-raising-35m.md) — engineer-turned-founder path, fundraising and startup learnings.
