---
type: source
updated: 2026-07-19
raw: ../raw/openai-codex-tech-lead-on-how-his.md
guest: "Michael Bolin"
guest_role: "OpenAI Codex CLI tech lead, ex-Meta Distinguished Engineer (E9)"
date: 2026-03-09
url: https://www.developing.dev/p/openai-codex-tech-lead-on-how-his
---

# OpenAI Codex Tech Lead On How His Career Grew And How He Uses Codex | Michael Bolin

Michael Bolin is the tech lead for [OpenAI](../entities/openai.md)'s open-source Codex CLI and a former Distinguished Engineer (E9) at [Meta](../entities/meta.md), where he created the Buck build system, the Nuclide IDE, and worked on the Eden virtual filesystem. The episode traces his path from [Google](../entities/google.md) Calendar engineer to senior IC at Meta to OpenAI, and is unusually concrete about both the technical intuitions behind his big projects and the career mechanics (delayed promos, calibrations, picking force-multiplier projects) at the highest IC levels.

## Key takeaways

- Bolin's core career algorithm ([career-growth](../concepts/career-growth.md)): (1) figure out what you genuinely love doing, (2) figure out what is invaluable to your employer, (3) lean hard into the intersection — and if the intersection doesn't exist where you are, leave. He left Google after four years because he kept pouring effort into things he loved (Google Tasks, Closure JavaScript tools, even writing a book on Closure) that Google didn't value: "harder, not smarter."
- He built Buck, Meta's Android build system, as a hackathon project against near-universal advice not to, despite an existing internal competitor (FB Build) and Google's Blaze. His conviction came from an "existence proof" — he'd seen Blaze work at Google — and from first-principles analysis: the old system rebuilt everything from scratch, so caching unchanged steps and making modules cheap to add (vs. ~200 lines of Ant XML each) yielded multi-x speedups ([developer-tools](../concepts/developer-tools.md)).
- His repeated [influence](../concepts/influence-and-leadership.md) tactic for starting disruptive projects without credibility: deliberately scope-couch them ("I'm just making an Android build system / an iOS editor — I'm not trying to take over your project") to avoid friction, borrow credibility from a respected supporter (ex-Google Android eng John Perlow for Buck), and let adoption come to you (iOS team asked to use Buck a year later; Uber and Airbnb adopted it externally).
- After his E8 (Principal) [promo](../concepts/promotions.md), he flopped on a "hero quest" — trying to fix facebook.com web speed with JavaScript expertise. Lesson: you succeed at the subset of things you genuinely enjoy (for him, writing lots of code from scratch), not data-analysis/alignment-heavy projects; senior managers deserve more credit for pairing senior ICs with the right projects.
- His E9 (Distinguished) promo was delayed after he pushed too hard when Microsoft acquired GitHub and he (correctly) predicted Nuclide's Atom foundation would die in favor of VS Code — he got coaching, and the learning was about how he pushed, not what he argued. He now recognizes what triggers him and avoids acting in that moment ([corporate-politics](../concepts/corporate-politics.md)).
- The Eden virtual filesystem + "Myles" fuzzy file-search service (built with Hanson Wang, now also on Codex) is a rare on-the-job Leetcode-style story: parallel arrays plus a 64-bit character bitmask for fast exclusion, cache-friendly linear memory reads, searching over a million files in 10–20ms; ~30 servers globally were running it when he left.
- Why he joined OpenAI ([ai-era-engineering](../concepts/ai-era-engineering.md)): at Meta he built LLM dev tools (CodeCompose) on Llama 2 while users asked "why isn't this GPT-4?"; he wanted to build with the best model, sit next to the researchers who make it, work with people at Meta E8/E9 caliber, and reach consumer-scale users again. He compares 2024 OpenAI to joining Google in 2000.
- Codex story ([ai-coding-tools](../concepts/ai-coding-tools.md)): CLI launched rushed in April 2025 (10–20k GitHub stars in ~2 weeks), Codex Web launched a month later with ~7 engineers but was "ahead of its time" — local agents had stronger product-market fit. The August 2025 confluence (GPT-5, new TUI, open-weights model support, VS Code extension) produced the inflection to "vertical line" growth, 1M+ users, usage up 5x. Long-term he still believes most agent compute moves to the cloud (agents as automation-pipeline pieces, fired off per GitHub issue).
- His own usage: 80–90% of his code is model-written; he hand-writes the security-critical sandboxing code in the Rust harness, seeds hard groundwork then lets the model fill in, and uses Codex to split oversized PRs into reviewable commits. The Codex CLI is [open source](../concepts/open-source.md) largely for trust — an agent running on your machine should be inspectable — plus contributions and recruiting.
- Education advice ([regrets-and-advice](../concepts/regrets-and-advice.md)): deep skills still matter because the quality of your questions bounds the quality of the agent's output. He recommends reading a 1000-page operating systems book cover to cover (which rescued him on Eden, having never written C), the O'Reilly Rust books, and especially CTF security competitions — a "computer decathlon" that forces breadth (GDB, assembly, janky PHP) you'd never get writing React. Advice to younger self: don't cling to your first language (he went too deep on JavaScript for too long).

## Notable quotes

- "A lot of people told me what I was doing was a very bad idea. Almost everybody, except one person." — Michael, ~00:09:30, on starting Buck
- "Facebook was always hitting the scaling limits of every mobile developer tool before everybody else... as a DevTools person, it was kind of interesting because we got to solve problems that nobody had solved before, and not just as a science project, but because it was real business value." — Michael, ~00:18:30
- "If the model weren't very good, it wouldn't really matter what we did on the harness." — Michael, ~00:44:07, on research-led vs engineering-led cultures
- "It's kind of amazing and sad or weird how far many of us can get in software engineering without really having a clue how computers work." — Michael, ~01:01:07

## Connections

- [OpenAI Eng & Dev Tools Founder: How Software Engineering Is Changing | Charlie Marsh](openai-eng-and-dev-tools-founder.md) — another OpenAI engineer with a dev-tools background on how AI is changing engineering.
- [Boris Cherny (Creator of Claude Code) On How His Career Grew](boris-cherny-creator-of-claude-code.md) — the directly competing coding agent's creator, with a similar career-story framing.
- [OpenAI & Meta Distinguished Engineer (IC9) On Working With Zuck, Carmack & Career Growth | Philip Su](openai-and-meta-distinguished-engineer.md) — same Meta-Distinguished-to-OpenAI path.
- [Meta Distinguished Eng (IC9) On Influencing Engs, Failures, and Learnings](meta-distinguished-eng-ic9-on-influencing.md) — influence and failure lessons at the same level and company.
- [Tech Lead for Meta's Most-Used Programming Language (Promotion Story)](tech-lead-for-metas-most-used-programming.md) — Meta internal dev-tooling/language work and promotion mechanics.
