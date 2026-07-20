---
type: source
updated: 2026-07-19
raw: ../raw/tech-lead-for-metas-most-used-programming.md
guest: "Dwayne Reeves"
guest_role: "Meta Senior Staff Engineer (IC7), tech lead for the Hack programming language"
date: 2025-07-25
url: https://www.developing.dev/p/tech-lead-for-metas-most-used-programming
---

# Tech Lead for Meta's Most-Used Programming Language (Promotion Story)

Dwayne Reeves joined pre-IPO Facebook straight out of [MIT](../entities/mit.md) and, over ~14 years at [Meta](../entities/meta.md), became the Senior Staff (IC7) tech lead for Hack, the company's most-used [programming language](../concepts/programming-languages.md). The episode traces his IC5, IC6 and IC7 [promotion](../concepts/promotions.md) stories — each one a surprise that came from strategy and alignment rather than code output — plus his round trip through [management](../concepts/management.md) as a TLM, why static typing wins at scale, his "uncanny valley of type systems" idea, and why he never left Meta.

## Key takeaways

- Dwayne interviewed at Facebook only as practice for [Google](../entities/google.md); he was won over by real engineering problems (memcache scaling, the custom PHP runtime) and by care signals: an unsolicited offer increase (vs. [Amazon](../entities/amazon.md)'s "we don't negotiate with new grads") and CTO Bret Taylor taking MIT's new-grad cohort to lunch.
- On school prestige: MIT's value was opportunity access, not the education — equally capable colleagues without degrees only landed at Facebook by chance ([hiring and interviews](../concepts/hiring-and-interviews.md)).
- His breakout project was typing an untyped core PHP API with Hack: scoped as 1–2 weeks, it took a quarter, and ~20% of migrated call sites revealed real bugs (mostly null-handling) — the result that made Meta take Hack seriously as more than a cool tool.
- Static typing is superior at industry scale because a large codebase is an information-communication problem: types communicate intent, enable tooling (autocomplete, search), and formally rule out whole classes of errors; only solo hobbyists move faster dynamically.
- His "uncanny valley of type systems": as a dynamic codebase approaches full static typing, the remaining places where types lie become more off-putting, so things get worse just before 100% — an argument for removing PHP behaviors incompatible with a sound type checker. The metaphor became the Hack team's rallying vision.
- IC5 promotion story: the half where he wrote the least code of his career (driving Hack coverage from ~20–30% to ~60–70% by influencing others) was his highest-rated ever ("redefined") — teaching him the job is identifying and solving problems, not code output ([career-growth](../concepts/career-growth.md), [calibrations-and-ratings](../concepts/calibrations-and-ratings.md)).
- IC6 promotion story: his manager's rocket-ship analogy — "I only cared about you getting us out of orbit" — forced him to hand his year-long collections redesign to another engineer once aligned; the handoff itself demonstrated next-level scope and got him promoted. Both promos surprised him because his mental model of the next level was wrong.
- He became a TLM reluctantly (his rule: doing the uncomfortable thing has always paid off), grew to ~13 reports including managers, but found he coached ICs on technical problems while org design got "vibe management"; he returned to IC because replacing a manager for 6–7 people was easier than replacing a tech lead for 35–40.
- IC7 came while still a manager, attributed to his technical vision (crossing the uncanny valley): by then essentially the whole codebase was strict Hack, up from 5–10% of files in 2015 — impact spanning thousands of engineers.
- On [working with legends](../concepts/working-with-legends.md) like type-theory researcher Andrew Kennedy: don't fear pedigree — you always have value to add — and accomplished seniors owe juniors the same approachability and humility ([imposter syndrome](../concepts/imposter-syndrome.md)).
- Why he stayed ~14 years: "I don't want to make permanent decisions based off of temporary circumstances" — every time he had an outside offer, the actual problem (a two-month discomfort, a project issue) was solvable in place, and he felt valued.
- Advice to his younger self: when told to write code, ask how they knew it was the right code — aim to be in the rooms deciding what to build, because your value is more than what you type ([regrets and advice](../concepts/regrets-and-advice.md)).

## Notable quotes

- "Writing code is just not what my job as a software engineer is. My job is to identify and solve problems." — Dwayne Reeves (~18:30)
- "You're a rocket ship... I only cared about you getting us out of orbit. Now that we've done that, you should pass this off to someone else." — Dwayne recounting his manager (~21:00)
- "I don't want to make permanent decisions based off of temporary circumstances." — Dwayne Reeves (~42:20)
- "You should stop and think: how do they know that's the right code to write? You should aim to be the person who's making those decisions." — Dwayne Reeves (~44:40)

## Connections

- [New Grad to Principal Engineer (IC8) at Meta (Career Story)](new-grad-to-principal-engineer-ic8.md) — parallel long-tenure new-grad-to-senior-IC climb at Meta.
- [Meta Senior Staff Eng (IC7) On Zuck Stories, Rapid Career Growth, Code Machine Archetype](meta-senior-staff-eng-ic7-on-zuck.md) — another Meta IC7 journey, including the "code machine" archetype Dwayne learned to outgrow.
- [Instagram Staff (IC6) Promo Despite 10 Team Switches in 9 Years (Career Story)](instagram-staff-ic6-promo-despite.md) — contrasting Meta career strategy: Dwayne's decade of depth on one language vs. Sash's 10 team switches.
- [Co-Creator of Haskell: Functional Programming, Thinking in Types, Useless Languages | Simon Peyton Jones](co-creator-of-haskell-functional.md) — type systems and language design from the research side.
- [GoogleX Chief Scientist On Imposter Syndrome, Career Growth, Project Taste | Carey Nachenberg](googlex-chief-scientist-on-imposter.md) — imposter syndrome and project selection themes echoed in Dwayne's reflections.
