---
type: source
updated: 2026-07-19
raw: ../raw/meta-distinguished-eng-ic9-on-influencing.md
guest: "Adam Ernst"
guest_role: "Distinguished Engineer (IC9) at Meta, iOS infrastructure"
date: 2026-02-09
url: https://www.developing.dev/p/meta-distinguished-eng-ic9-on-influencing
---

# Meta Distinguished Eng (IC9) On Influencing Engs, Failures, and Learnings

Adam Ernst is a Distinguished Engineer (IC9) at [Meta](../entities/meta.md) who joined Facebook weeks before the 2012 IPO — when every iOS engineer fit in one conference room — and built iOS infrastructure that shaped the whole company, including the immutable-model replacement for [Apple](../entities/apple.md)'s Core Data and ComponentKit, a React-for-iOS UI framework that predated Swift, SwiftUI, and React Native. The episode is unusually candid about failure: he spends a third of it dissecting ComponentScript, the cross-platform framework he spent two years on that "was a total and complete failure," earned him a Meets Most rating, and taught him that technical excellence alone doesn't win.

## Key takeaways

- Ernst started a software company (Cosmic Soft) in middle school, selling online testing software written in REALbasic to teachers worldwide — accepting $19.95 checks by mail from an eighth grader's mailbox and emailing back unlock codes via a proto-Stripe called Ecelerate.
- His E6 [promotion](../concepts/promotions.md) came from replacing Apple's Core Data ORM (fine for a two-engineer startup, "falls over completely" at 100-200 engineers) with MemModels, an immutable model system — against pushback from "Apple-y engineers" who insisted on vanilla Apple frameworks that demonstrably don't scale to Meta's size.
- His [influence](../concepts/influence-and-leadership.md)-without-authority playbook: (1) talk in person or on video rather than in writing; (2) open by sympathizing with the other side's position; (3) do your research — his team disassembled Core Data's closed source to show exactly why it couldn't work; (4) "do the work for them" — as a self-described coding machine he'd complete the migration himself so teams only had to say yes.
- Code review is massively undervalued: he reviewed over 1,600 diffs in a half (~14 per workday) because it's an organic, structured, viral channel for influencing how engineers across the company write code. Good diff comments explain *why*, stay flexible ("here's my concern, but do what you want if you feel strongly"), and explicitly invite missing context.
- His IC7 promo project ComponentKit brought React's concepts (components, immutability, view reconciliation) to iOS in 2014 — before Swift, SwiftUI, or React Native existed — at the nudge of manager Lee Byron (GraphQL co-inventor), to save a collapsing Facebook News Feed. Winning adoption took concrete side-by-side code examples, performance data, allies who "carried weight," senior mediators, and compromise (absorbing the rival Panels team's data-source tech so everyone got a win).
- ComponentScript, his two-year cross-platform follow-up, checked every technical box (type safety, GraphQL integration, bidirectional native embedding) and still failed completely: it targeted no specific engineer persona (iOS engineers didn't want JavaScript; JS engineers wanted real React), he refused to compromise on GraphQL data consistency while a server-driven rival simply skipped it, and he went wide across all mobile engineers instead of landing one committed anchor team.
- Performance systems did their job on the failure: a Meets Most [rating](../concepts/calibrations-and-ratings.md) and a fresh-eyed new manager forced the cancellation he'd been avoiding. He'd known in his gut for a year it wasn't working, and his coding-machine reflex — "I just need to write more code" — was exactly the wrong response.
- How to kill a project responsibly: he migrated every ComponentScript feature back to native or React Native, deleted the framework from the repo entirely, and published a detailed public postmortem — and believes he got a net-positive reputation bump: "you might get more goodwill from killing it responsibly than dragging it out."
- He never considered [management](../concepts/management.md): he loves writing code, knows he's weaker at docs and alignment-driving, and is best at communicating when anchored to concrete technical problems — an argument for honest self-assessment of archetype.
- His depth-plus-breadth superpower: when blocked by another team's system (e.g. GraphQL codegen), instead of filing a ticket he dives "eight levels deep" into their guts, then either fixes it or shows up with the diagnosis — impressing the owning team, saving their time, and organically accumulating knowledge of many systems.
- On scary IC9 expectations: "I've flipped the switch off. I just don't care." He checks in with his manager to ensure he's solving problems that matter to the org, then works on what he loves without meta-anxiety — arguing the worry itself is counterproductive.
- The senior engineers he admires span archetypes: coding machine Dustin Shahidipour, fixer Wei Han, project-starter [Michael Bolin](openai-codex-tech-lead-on-how-his.md) (kickstarted Buck and the Miles file searcher), communicators Bob Baldwin and Oliver Ricard, and his "polar opposite" Nolan O'Brien, who drives alignment and manages the delicate Meta-Apple relationship.
- [Advice](../concepts/regrets-and-advice.md) to his younger self: nothing — but his general advice is to do what you love, because enthusiasm can't be faked and productivity, curiosity, and 10-layers-deep digging are all downstream of liking the work (specifically, liking solving problems).

## Notable quotes

- **Adam:** "It was a real learning experience because I learned that just because it was technically excellent, didn't mean it was going to win." (~00:22:16)
- **Adam:** "If you show up and you're like, hey, I did the work already for you. Here are the benefits. I just need you to sign off... Much easier conversation." (~00:09:33)
- **Adam:** "You might get more goodwill from killing it responsibly than just like dragging it out and constantly waiting until it's too late." (~00:28:09)
- **Adam:** "I've flipped the switch off. I just don't care... as long as I'm working on what's important for my org and I like what I'm doing, I'm just not going to worry about it." (~00:33:56)

## Connections

- [OpenAI Codex Tech Lead On How His Career Grew And How He Uses Codex | Michael Bolin](openai-codex-tech-lead-on-how-his.md) — Bolin is explicitly named by Ernst as an admired "project starter" from their shared Meta years.
- [Meta Senior Staff Eng (IC7) On Zuck Stories, Rapid Career Growth, Code Machine Archetype](meta-senior-staff-eng-ic7-on-zuck.md) — Ernst self-identifies as the coding machine archetype this episode is about, including its failure mode.
- [OpenAI & Meta Distinguished Engineer (IC9) On Working With Zuck, Carmack & Career Growth | Philip Su](openai-and-meta-distinguished-engineer.md) — the podcast's other Meta IC9 perspective on operating at distinguished-engineer level.
- [New Grad to Principal Engineer (IC8) at Meta (Career Story)](new-grad-to-principal-engineer-ic8.md) — another long single-company climb up Meta's senior IC ladder.
- [Uber Distinguished Eng On Unfair Promos, Influence, Engineering Regrets (Career Story)](uber-distinguished-eng-on-unfair.md) — parallel distinguished-engineer take on influence and engineering regrets.
