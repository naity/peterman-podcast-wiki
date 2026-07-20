---
type: source
updated: 2026-07-19
raw: ../raw/msl-eng-director-promo-hacking-industry.md
guest: "John Myles White"
guest_role: "Ex-Director of Engineering at Meta Superintelligence Labs (PyTorch), Julia core contributor"
date: 2026-05-04
url: https://www.developing.dev/p/msl-eng-director-promo-hacking-industry
---

# PyTorch Eng Director: Promo Hacking, Industry Shifts, Regrets | John Myles White

John Myles White recently left his role as director of engineering at [Meta](../entities/meta.md) Superintelligence Labs (MSL), where he led PyTorch engineering after years in Data Infra and AI Infra, so he speaks unusually freely: about why he's bullish on Meta stock but bearish on being a Meta employee, how [promo culture](../concepts/promotions.md) wrecked teams in AI Infra, his earlier life as a [Julia](../concepts/programming-languages.md) core language contributor and statistician, and the career regret of never showing up to his skip-level's office hours.

## Key takeaways

- White is "very bullish on Meta as a stockholder, very bearish if you're an employee who's not a stockholder": the labor market flipped from chronic undersupply of engineers to perceived oversupply (except frontier-lab AI researchers), so employers across Silicon Valley make fewer retention sacrifices — comp, perks, employee voice ([big-tech-culture](../concepts/big-tech-culture.md), [layoffs](../concepts/layoffs.md)). Once layoffs became real, employees tolerated perk cuts they'd previously called unforgivable.
- Ran [promotions](../concepts/promotions.md) in AI Infra for years: in AI Infra literally everyone's first goal was promo (versus early Facebook where it "was just not ever a thing"), and Monetization recruited with detailed promo-plan documents. Result: teams shipping projects everyone agreed were bad ("I have to ship it because that's my promo bar") and systems deliberately maximally coupled to other systems to hit scope bars — promo culture decoupled promotion from the skills that actually compound.
- You can't unilaterally disarm inside a promo-driven org — "it's totally irrational not to play the game" — but you have agency in choosing teams: PyTorch selected for love of the craft, held promo bars so high its IC8s were "as good as you're going to get anywhere in this whole world," and that credibility ironically made outside orgs trust its promo cases. White accepted ~20% less compensation to be somewhere he was proud of ([calibrations-and-ratings](../concepts/calibrations-and-ratings.md), [compensation-and-equity](../concepts/compensation-and-equity.md)).
- Early-Meta [career growth](../concepts/career-growth.md) story: joined Core Data Science as IC4 right as the "emotional contagion" PNAS paper became Meta's worst PR disaster of the year (company-wide apology Q&A, meetings with the head of legal); then all senior engineers left the experimentation-tools team within six months and he went from random IC5 to de facto TL of Deltoid 3, Meta's A/B testing framework — "people understate how often these things can happen in tech."
- Claims Statsig is essentially Deltoid and Airflow literally is Meta's DataSwarm (its author quit and open-sourced it a week later) — the repeatable playbook of turning internal big-tech infra into billion-dollar [startups](../concepts/startups-and-founding.md), and his own missed chance: "I probably should have built a Deltoid startup many years earlier."
- On Julia: designed by MIT math people "to destroy MATLAB"; his pitch is that naive R translations of C loops run 1,000-10,000x slower, and dynamic languages are slow because of what they *might* do — R's braces are user-redefinable operators, its lazy promise arguments are unnecessary ~70-90% of the time, Python's inspect module lets anyone rewrite the symbol table. "What makes a language fast is invariants."
- On academics treating industry as a fallback: grad students assume they can "compete with the dumb people" easily, then interview terribly — including a CS professor who passed values between functions by reading the REPL output and retyping it ([hiring-and-interviews](../concepts/hiring-and-interviews.md)).
- Statistics is "the craziest field" — pure math that sells itself as practical; he recommends anything by Larry Wasserman ("the embodiment of hyper-intense honesty") and Peter Aronow's Foundations of Agnostic Statistics; misunderstood significance thresholds plus goal culture produce pathologies like teams shipping a metric win on July 1 they planned to delete on July 2.
- Biggest [regret](../concepts/regrets-and-advice.md): never once attending office hours held by his skip-level Javi (Javier Olivan, now Meta COO) despite weekly prompting — a fear-driven decision that hurt both parties. Directors and above are starved for ground truth; "if a leader says, please show up and talk to me, do it" ([mentorship-and-sponsorship](../concepts/mentorship-and-sponsorship.md)).
- Advice to his younger self: be more ambitious — people "over convince themselves of the greatness of other people and under convince themselves of how much they can achieve... they're not actually doing that much better than you. They just tried and you didn't try."

## Notable quotes

- "I am very bullish on Meta as a company that I am now a stockholder of, but not an employee." — John Myles White, ~0:54
- "Everyone agreed the thing we were working on was bad. No one thought it would succeed, but people were like, oh, but I have to ship it because that's my promo bar." — John Myles White, ~7:42
- "Fundamentally, any code that's slow is slow because it's doing stuff it doesn't need to do." — John Myles White, ~26:22
- "They're not actually doing that much better than you. They just tried and you didn't try." — John Myles White, ~42:04

## Connections

- [Airbnb Staff Eng on How To Not Get Stuck at Senior and Untold Rules of Calibrations](airbnb-staff-eng-on-how-to-not-get.md) — the calibration/promo machinery White ran from the other side.
- [Instagram Principal Eng (IC8) On Building IG Stories, 1 Promo Per Half, Small Teams](instagram-principal-eng-ic8-on-building.md) — contrasting fast-promo Meta story versus PyTorch's deliberately high bar.
- [Honest Big Tech Layoff Story After 25 Years](laid-off-from-big-tech-after-25-years.md) — the employee side of the labor-leverage shift White describes.
- [Co-Creator of Haskell: Functional Programming, Thinking in Types, Useless Languages | Simon Peyton Jones](co-creator-of-haskell-functional.md) — fellow language designer; Julia's speed-through-invariants thesis versus Haskell's type-driven design.
- [Google DeepMind Pre-Training Lead: How To Get a Job at a Frontier Lab | Vlad Feinberg](google-deepmind-pre-training-lead.md) — the frontier-lab AI researcher market that White notes is the one exception to employer leverage.
