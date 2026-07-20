---
type: concept
updated: 2026-07-19
sources: [boris-cherny-creator-of-claude-code.md, anthropic-eng-leader-and-ex-senior.md, openai-codex-tech-lead-on-how-his.md, openai-eng-and-dev-tools-founder.md, aws-distinguished-eng-learnings-from.md, meta-senior-staff-eng-ic7-on-zuck.md, meta-hiring-lead-on-behind-the-scenes.md, ex-head-of-eng-at-instagram-career.md, creator-of-c-bell-labs-negative-overhead.md, co-creator-of-haskell-functional.md]
---

# AI coding tools

Claude Code, Codex, Cursor and their kin — told largely from inside: the podcast has interviewed the creator of Claude Code (Boris Cherny), an engineering leader on the same team (Fiona Fung), the Codex CLI tech lead (Michael Bolin), and a founder whose dev-tools company was acquired by OpenAI (Charlie Marsh).

## What the guests say

### How the winning tools were built

Boris Cherny credits Claude Code's success to Ben Mann's push: "don't build for the model of today, build for the model six months from now" — the product stayed mediocre until Sonnet/Opus 4 landed, after which ~80-90% of Claude Code was written with Claude Code and Anthropic's per-engineer productivity grew ~70% while headcount tripled ([episode](../sources/boris-cherny-creator-of-claude-code.md)). Michael Bolin makes the mirror-image point from OpenAI's research-led culture: "if the model weren't very good, it wouldn't really matter what we did on the harness" — he left Meta because dev tools built on Llama 2 couldn't compete with GPT-4, and wanted to co-develop product with the researchers making the best model ([episode](../sources/openai-codex-tech-lead-on-how-his.md)). Fiona Fung describes Claude Code's iteration loop (idea, build, internal launch, feedback, public launch) as faster than anything she saw in 11.5 years at Microsoft, and calls using Claude Code to build Claude Code "the first time I've been able to ship production software in a really long time" ([episode](../sources/anthropic-eng-leader-and-ex-senior.md)).

On form factor the builders diverge: Bolin says Codex Web was "ahead of its time" because local agents had stronger product-market fit, yet he believes most agent compute ultimately moves to the cloud ([episode](../sources/openai-codex-tech-lead-on-how-his.md)). On competition, Cherny doesn't use rival tools and tells his team not to get sidetracked — more competitors signals success ([episode](../sources/boris-cherny-creator-of-claude-code.md)). James Everingham dismisses a whole product category: tools like Cursor are "autocomplete" filling gaps the next model closes — "building for the future past" ([episode](../sources/ex-head-of-eng-at-instagram-career.md)).

### Optimists vs skeptics

The heavy users report step-change productivity: Bolin's code is 80-90% model-written ([episode](../sources/openai-codex-tech-lead-on-how-his.md)); Michael Novati reports ~5x output in Formation's ~500k-line codebase, framing LLMs as the Vim-to-VSCode leap repeated ([episode](../sources/meta-senior-staff-eng-ic7-on-zuck.md)); Marc Brooker expects agentic development to become the mainstream of a perpetually supply-constrained industry ([episode](../sources/aws-distinguished-eng-learnings-from.md)).

The skeptics — none of them Luddites — draw domain boundaries. Bjarne Stroustrup: fine for boilerplate, but in safety/performance-critical code LLMs bring bugs, bloat, and a validation burden regulators won't accept ([episode](../sources/creator-of-c-bell-labs-negative-overhead.md)). Simon Peyton Jones sees LLMs as a boon *specifically for* statically typed languages (the compiler prunes the generation space) yet refuses to merge unreviewed AI code into GHC: "copilots need pilots" ([episode](../sources/co-creator-of-haskell-functional.md)). Notably, the tool builders themselves hedge the same way: Cherny restricts vibe coding to prototypes and throwaway code, defaults to plan-mode pairing, and still hand-writes the core query loop ([episode](../sources/boris-cherny-creator-of-claude-code.md)); Bolin hand-writes the security-critical sandboxing code in Codex's Rust harness ([episode](../sources/openai-codex-tech-lead-on-how-his.md)). More skeptical positions (Stonebraker's 0% real-world text-to-SQL result, Cowling on simplicity) are covered in [ai-era-engineering](ai-era-engineering.md).

### The slop problem

Charlie Marsh gives the most concrete account of AI's downside for code quality. A teammate told him they used to review his PRs minimally on trust but now must review closely because an agent writes them — "a wake-up call about accepting work below your former standard." Astral's defenses: heavy automated verification (time/memory benchmarks and ecosystem-wide diagnostic diffs on every PR), assuming everyone runs agent review before pushing, encoding recurring review feedback into AGENTS.md and shared skills, and reviewing your own PR in the GitHub UI as if you were the reviewer ([episode](../sources/openai-eng-and-dev-tools-founder.md)). His sharpest disagreement is with Bun's largely human-unreviewed agent-driven Zig-to-Rust rewrite: glad someone is pushing the envelope, but he would block it at Astral — by Hyrum's Law an automated rewrite trades known issues for unknown ones pushed onto millions of users ([episode](../sources/openai-eng-and-dev-tools-founder.md)). Cherny's parallel rule: hold model-written code to exactly the same bar as human code ([episode](../sources/boris-cherny-creator-of-claude-code.md)).

### Second-order effects

Agentic tools are reshaping [hiring](../concepts/hiring-and-interviews.md): Austen McDonald says end-to-end ownership is now the key behavioral signal for mid-level candidates precisely because agents write the code, and calibrated senior interviewers expose AI-generated interview stories with follow-ups ([episode](../sources/meta-hiring-lead-on-behind-the-scenes.md)). Adoption is spilling past engineering — Claude Code is used by data scientists and half of Anthropic's sales team ([episode](../sources/boris-cherny-creator-of-claude-code.md)) — and Everingham's DevMate at Meta (agents driving tools, not just writing code) went viral among 40,000+ engineers ([episode](../sources/ex-head-of-eng-at-instagram-career.md)); it was DevMate that convinced Fiona Fung AI was "already here" and precipitated her move to Anthropic ([episode](../sources/anthropic-eng-leader-and-ex-senior.md)).

## Practical takeaways

- Build (and evaluate) AI products against the model six months out, not today's model (Cherny [episode](../sources/boris-cherny-creator-of-claude-code.md)).
- Same bar for agent code as human code; vibe coding for prototypes only; keep hand-writing the critical core (Cherny [episode](../sources/boris-cherny-creator-of-claude-code.md); Bolin [episode](../sources/openai-codex-tech-lead-on-how-his.md)).
- Fight slop structurally: automated benchmarks and diff tests on every PR, agent-readable review conventions (AGENTS.md), and self-review in the reviewer's UI (Marsh [episode](../sources/openai-eng-and-dev-tools-founder.md)).
- Don't ship an automated rewrite of software millions depend on without human review — Hyrum's Law (Marsh [episode](../sources/openai-eng-and-dev-tools-founder.md)).
- Ignore competitors; focus on users' problems (Cherny [episode](../sources/boris-cherny-creator-of-claude-code.md)).
- In interviews, expect your end-to-end ownership — not raw coding — to carry the signal (McDonald [episode](../sources/meta-hiring-lead-on-behind-the-scenes.md)).

## Related

- [ai-era-engineering](ai-era-engineering.md) — the profession-wide debate these tools triggered
- [developer-tools](developer-tools.md) — the adoption playbooks that predate AI
- [open-source](open-source.md) — Marsh's AI contribution policy and Codex CLI's open-sourcing
- Key people: [Boris Cherny](../entities/boris-cherny.md), [Michael Bolin](../entities/michael-bolin.md), [Charlie Marsh](../entities/charlie-marsh.md), [Fiona Fung](../entities/fiona-fung.md)
- Key episodes: [Boris Cherny](../sources/boris-cherny-creator-of-claude-code.md), [Codex CLI tech lead](../sources/openai-codex-tech-lead-on-how-his.md), [Charlie Marsh](../sources/openai-eng-and-dev-tools-founder.md)
