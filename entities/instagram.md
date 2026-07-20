---
type: entity
entity_kind: org
updated: 2026-07-19
sources: [airbnb-staff-eng-on-how-to-not-get.md, boris-cherny-creator-of-claude-code.md, ex-head-of-eng-at-instagram-career.md, instagram-principal-eng-ic8-on-building.md, instagram-principal-engineer-ic8.md, instagram-senior-staff-eng-ic7-on.md, instagram-staff-ic6-promo-despite.md, new-grad-to-principal-engineer-ic8.md]
---

# Instagram

Instagram is [Meta](meta.md)'s photo/video subsidiary and, in this podcast, the canonical case study in small-team product engineering: eight episodes feature engineers or leaders who built Stories, Threads, IGTV, and Instagram's web and backend platforms.

## What the episodes reveal

- **Small teams as the defining ethos.** Instagram Stories was built in ~2–3 months after Ryan Olson *cut* the team down to a core of two iOS engineers with no dedicated server engineer — "if you want to go fast, go small" — beating [Snapchat](snapchat.md) at everyday sharing with the unfair advantage of the existing friend graph ([Instagram Stories episode](../sources/instagram-principal-eng-ic8-on-building.md)). James Everingham confirms from the head-of-eng side: the deliberately shrunk, talent-dense, founder-led team with no cross-org dependencies is what shipped Stories from zero in three months ([Ex-Head of Eng](../sources/ex-head-of-eng-at-instagram-career.md)). The pattern repeated with Threads: first prototype to public launch in ~5–6 months on Instagram's battle-tested primitives with a tiny team, becoming Meta's poster child for shipping big products with small teams ([Sash Zats](../sources/instagram-staff-ic6-promo-despite.md)); Marius Schulz was the *only* engineer on Threads Web for its first 6–8 weeks ([Marius Schulz](../sources/instagram-senior-staff-eng-ic7-on.md)).
- **Culture and talent density.** Early Instagram (~10 iOS engineers) was full of low-hanging fruit and had "the ax," a physical weekly award for outsized impact ([Ryan Olson](../sources/instagram-principal-eng-ic8-on-building.md)). Everingham says Instagram's unusually smart engineers "IQ'd past" the normal ~100-engineer communication breakdown until ~150–200, everyone was a power user of the product, and Mike Krieger's leadership mantra — "do the simple thing first" — was literally a conference-room name; Krieger personally coded the Stories neon brush and reviewed diffs at 2 AM ([Ex-Head of Eng](../sources/ex-head-of-eng-at-instagram-career.md), [Instagram Stories](../sources/instagram-principal-eng-ic8-on-building.md)).
- **Growth pains.** Olson answers the Thanos-snap hypothetical with yes — Instagram would likely run better with half the people, each marginal person adding invisible coordination and codebase cost (he waited 4+ hours a day on builds before leaving) ([Instagram Stories](../sources/instagram-principal-eng-ic8-on-building.md)). The Facebook/Instagram relationship had politics invisible even to IC8s: strategy calls like turning off Facebook-to-Instagram traffic only made sense to Olson years later, reading the antitrust lawsuit's internal memos on cannibalization fears ([same](../sources/instagram-principal-eng-ic8-on-building.md)).
- **Promo mechanics.** Instagram runs Meta's ladder, and its guests supply the most concrete promo stories on the show: Olson's deliberate "ask for a double promo knowing HR will refuse" gambit converting into back-to-back IC5/IC6 promos ([Instagram Stories](../sources/instagram-principal-eng-ic8-on-building.md)); Schulz's three "Redefines Expectations" promos and the IC4/IC5/IC6 "ways to solve the same problem" framework ([Marius Schulz](../sources/instagram-senior-staff-eng-ic7-on.md)); Jake Bolam's IC8 from a backend rewrite affecting hundreds of teams, plus his "go where you're valued" lesson after a rough Meta start ([Jake Bolam](../sources/instagram-principal-engineer-ic8.md)); and Zats reaching IC6 despite 10 team switches in 9 years, optimizing for fun and zero-to-one ambiguity ([Sash Zats](../sources/instagram-staff-ic6-promo-despite.md)).
- **Platform history.** Adrien Friggeri built Instagram's first A/B testing system as an embedded IC4 during the AWS-to-Facebook infra migration, having been told "don't bug us" — and calls never officially joining that ~30-person team his biggest career mistake, since peers from it reached IC7–IC10 far faster ([New Grad to IC8](../sources/new-grad-to-principal-engineer-ic8.md)). Boris Cherny joined Instagram's Tokyo landing team and seeded the Python-to-Hack migration (later delegated to Jake Bolam) ([Boris Cherny](../sources/boris-cherny-creator-of-claude-code.md)). Laurent Charignon did staff-level developer-productivity work there between [Stripe](stripe.md) and Airbnb stints ([Airbnb Staff Eng](../sources/airbnb-staff-eng-on-how-to-not-get.md)).
- **Product failures owned honestly.** IGTV failed despite anticipating vertical video — creators were "horrified" by AI landscape-to-vertical reformatting and Instagram's hubris that it could single-handedly change creator behavior didn't pan out, though it informed Reels ([Ryan Olson](../sources/instagram-principal-eng-ic8-on-building.md)). The blockchain/NFT team taught Zats that products fail on business incentives more often than technology ([Sash Zats](../sources/instagram-staff-ic6-promo-despite.md)).

## People

- [Ryan Olson](ryan-olson.md) — Principal (IC8), iOS lead for Stories/IGTV/IG Labs; co-founder of Retro
- [Jake Bolam](jake-bolam.md) — Principal (IC8), Instagram backend rewrite
- [Marius Schulz](marius-schulz.md) — Senior Staff (IC7), Threads Web
- [Sash Zats](sash-zats.md) — Staff (IC6), Threads pre-launch and AI prototyping
- [James Everingham](james-everingham.md) — Head of Engineering under CTO Mike Krieger
- [Boris Cherny](boris-cherny.md) — Principal (IC8), Tokyo landing team
- [Adrien Friggeri](adrien-friggeri.md) — brought A/B testing to early Instagram
- [Laurent Charignon](laurent-charignon.md) — staff engineer, developer productivity

## Related

- [big-tech-culture](../concepts/big-tech-culture.md) — the small-team counterculture inside big tech
- [promotions](../concepts/promotions.md), [calibrations-and-ratings](../concepts/calibrations-and-ratings.md)
- [influence-and-leadership](../concepts/influence-and-leadership.md) — Krieger's lead-from-the-front model
- [Meta](meta.md), [Snapchat](snapchat.md)
