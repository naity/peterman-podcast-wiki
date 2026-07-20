---
type: concept
updated: 2026-07-19
sources: [openai-codex-tech-lead-on-how-his.md, new-grad-to-principal-engineer-ic8.md, boris-cherny-creator-of-claude-code.md, meta-distinguished-eng-ic9-on-influencing.md, airbnb-staff-eng-on-how-to-not-get.md, openai-eng-and-dev-tools-founder.md, anthropic-eng-leader-and-ex-senior.md, ex-head-of-eng-at-instagram-career.md, msl-eng-director-promo-hacking-industry.md, instagram-principal-eng-ic8-on-building.md]
---

# Developer tools

Building tools for other engineers — build systems, editors, notebooks, linters — recurs as both a product category and a career engine: several guests earned their highest promotions, or founded their companies, on internal tooling. The through-line: tool success is an adoption problem more than a technical one.

## What the guests say

### Adoption is won socially, not technically

Michael Bolin built the Buck build system as a hackathon project against near-universal advice, with an internal competitor already staffed and Google's Blaze looming; his conviction came from an "existence proof" (he'd seen Blaze work) plus a first-principles insight about caching. His influence tactic: deliberately scope-couch disruptive projects ("just an Android build system"), borrow credibility from a respected supporter, and let adoption come voluntarily — the iOS team asked for Buck a year later, and Uber and Airbnb adopted it externally ([episode](../sources/openai-codex-tech-lead-on-how-his.md)). Adrien Friggeri's Bento (Meta's notebook platform, eventually used by ~60% of data practitioners) started as personal scripts that cut 300 lines of data-pipeline boilerplate to 20; his adoption strategy was to capture newcomers at bootcamp onboarding in a fast-growing company so network effects convert the stragglers, and to support the legacy systems first to build trust before migrating their users ([episode](../sources/new-grad-to-principal-engineer-ic8.md)). Boris Cherny's Undux became Facebook's most popular state-management framework after he scraped internal support posts, tallied complaints by team, and gave 20-40 per-team tech talks ([episode](../sources/boris-cherny-creator-of-claude-code.md)).

The cautionary tale is Adam Ernst's ComponentScript: a two-year cross-platform framework that was "a total and complete failure" despite checking every technical box — it targeted no specific engineer persona, he refused to compromise on data consistency while a rival skipped it and won, and he went wide instead of landing one committed anchor team ([episode](../sources/meta-distinguished-eng-ic9-on-influencing.md)). Bolin has his own version: he correctly predicted Nuclide's Atom foundation would lose to VS Code, but pushing the argument too aggressively delayed his E9 promotion — the lesson was about *how* he pushed, not what he argued ([episode](../sources/openai-codex-tech-lead-on-how-his.md)).

### Why big companies breed great tools

Bolin: "Facebook was always hitting the scaling limits of every mobile developer tool before everybody else... we got to solve problems that nobody had solved before, and not just as a science project, but because it was real business value" ([episode](../sources/openai-codex-tech-lead-on-how-his.md)). John Myles White generalizes this into a startup playbook: Statsig is essentially Meta's Deltoid, and Airflow literally is Meta's DataSwarm (its author quit and open-sourced it a week later) — internal big-tech infra is repeatably commercializable ([episode](../sources/msl-eng-director-promo-hacking-industry.md)). James Everingham's Meta dev-infra org (~1,000 engineers) produced DevMate, the internal agentic platform that inspired his startup Guild ([episode](../sources/ex-head-of-eng-at-instagram-career.md)).

Charlie Marsh founded Astral on comparative perspective rather than big-tech infra: having worked across Python, Go, and Rust, he saw JavaScript embracing native tooling (esbuild, Bun) while Python tools were still written in Python; Ruff's prototype shipped nine days after his "type checking at scale" blog post, and he credits choosing Rust — "largely because of hype" at the time — with making the systems layer accessible via Cargo's opinionated tooling ([episode](../sources/openai-eng-and-dev-tools-founder.md)).

### Measuring developer productivity

Laurent Charignon refused to rank engineers by lines of code or PR counts; at Stripe he instead instrumented the full journey of a code change (think, write, CI, review, merge), turning an unfair individual ranking into actionable org-level friction data. His companion practice: "channel your inner frustration" — Stripe's friction logs screenshot each step of a flow and interrogate every friction point; he could find 50-60 improvements in a single code-change flow ([episode](../sources/airbnb-staff-eng-on-how-to-not-get.md)). The stakes of neglect are Ryan Olson's exit condition: by the time he left Instagram he was spending 4+ hours a day waiting for builds — "the tooling just had not kept up with the velocity at which people were writing code" ([episode](../sources/instagram-principal-eng-ic8-on-building.md)).

### Dev tools as career engine

Almost every tool story above doubled as a promotion story: Bento earned Friggeri's IC7 ([episode](../sources/new-grad-to-principal-engineer-ic8.md)); Buck anchored Bolin's rise toward E9 ([episode](../sources/openai-codex-tech-lead-on-how-his.md)); Undux and side projects seeded Cherny's reputation ([episode](../sources/boris-cherny-creator-of-claude-code.md)); Fiona Fung's Claude Code role let a former Senior Director ship production software again ([episode](../sources/anthropic-eng-leader-and-ex-senior.md)); and Astral's tools got Marsh acquired by OpenAI ([episode](../sources/openai-eng-and-dev-tools-founder.md)).

## Practical takeaways

- Start tools as scoped, credibility-borrowed experiments; let teams ask for them rather than mandating adoption (Bolin [episode](../sources/openai-codex-tech-lead-on-how-his.md)).
- Pick one committed anchor team and a specific engineer persona before going wide (Ernst [episode](../sources/meta-distinguished-eng-ic9-on-influencing.md)).
- In fast-growing orgs, win newcomers at onboarding and let network effects do the rest; support legacy systems before migrating their users (Friggeri [episode](../sources/new-grad-to-principal-engineer-ic8.md)).
- Do the tedious demand research — scrape support posts, tally pain by team, then evangelize team by team (Cherny [episode](../sources/boris-cherny-creator-of-claude-code.md)).
- Measure the pipeline, not the people: instrument the code-change journey and keep friction logs (Charignon [episode](../sources/airbnb-staff-eng-on-how-to-not-get.md)).
- Being right about a tool bet isn't enough — how you argue it determines whether you (and it) survive (Bolin [episode](../sources/openai-codex-tech-lead-on-how-his.md)).

## Related

- [ai-coding-tools](ai-coding-tools.md) — the current generation of dev tools
- [influence-and-leadership](influence-and-leadership.md) — the persuasion skills tool adoption runs on
- [open-source](open-source.md) — the external analogue of these adoption games
- [startups-and-founding](startups-and-founding.md) — commercializing internal infra
- Key episodes: [Michael Bolin](../sources/openai-codex-tech-lead-on-how-his.md), [Adrien Friggeri](../sources/new-grad-to-principal-engineer-ic8.md), [Charlie Marsh](../sources/openai-eng-and-dev-tools-founder.md), [Laurent Charignon](../sources/airbnb-staff-eng-on-how-to-not-get.md)
