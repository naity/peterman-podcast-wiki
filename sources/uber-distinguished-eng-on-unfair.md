---
type: source
updated: 2026-07-19
raw: ../raw/uber-distinguished-eng-on-unfair.md
guest: "Joakim Recht"
guest_role: "Former Distinguished Engineer at Uber, now AI startup engineer"
date: 2025-11-11
url: https://www.developing.dev/p/uber-distinguished-eng-on-unfair
---

# Uber Distinguished Eng On Unfair Promos, Influence, Engineering Regrets (Career Story)

Joakim Recht grew from Senior to Distinguished Engineer at [Uber](../entities/uber.md) from its Denmark office, riding a single project — Odin, a containerized platform for stateful workloads — from a team-local Docker-for-MySQL experiment to running ~120,000 physical servers and ~500,000 databases operated by about 20 people. The episode covers how [promotions](../concepts/promotions.md) tracked that natural scope expansion, why promo committees are inevitably unfair, his contrarian insistence that engineers at every level must write code daily, growing [influence](../concepts/influence-and-leadership.md) without authority, [mentorship](../concepts/mentorship-and-sponsorship.md) strategy, Uber's 2017 scandals seen from Denmark, and why he ultimately left when management culture turned top-down.

## Key takeaways

- His Distinguished-level project (Odin) started as a local team's idea to run MySQL shards in Docker (when Kubernetes was barely in alpha) with declarative, intent-based management; it grew organically to manage all of Uber's stateful workloads — ~120,000 physical servers and ~500,000 databases run by a ~20-person team — replacing per-technology team toolchains across a company that had ~52 database technologies in use.
- Adoption strategy for platform migration: don't force it — build it, prove it works on your own team first, then expand outward through friendly departments to skeptics ("I prefer to build something and ensure that it works and then people can say, okay, that maybe isn't that bad"); ultimately top-down mandate ("you will not be allowed to have your own service any longer") was still needed for the last holdouts, because full alignment is impossible from the bottom up alone.
- His model of [promotions](../concepts/promotions.md): level tracks the number of people affected by your work, so a project with natural scope expansion (team → org → platform → company) drags promotions along "automatically" — for you and the whole team. Senior → Principal → Distinguished each followed a stage of Odin's expansion; he admits he was lucky to have one long-running project rather than being reshuffled.
- On unfair promos, from long promo-committee experience: his first committee reviewed hundreds of engineers in a single day with no preparation or materials, purely on how well each manager pitched — "if you have a bad manager, you have a bad case." Even in structured processes, dependencies ghosting you or projects canceled by management create unavoidable unfairness, and isolated teams ("you lived on an island") get denied without ever having been told what good looks like.
- His famous internal advice ("how to beat the promo committee") reduces to: software engineers must write code — at every level, ideally every day. Craftsmanship (good commits, reviewable diffs) is learned by watching others, not in college; "running code beats perfect code any day"; and rather than hunting for a promotion-worthy scope, "just relax about that part and focus on providing value — the other thing will come."
- Contrarian [delegation](../concepts/management.md) take: don't stop coding to become a whiteboard architect — you lose touch with the system, your designs become idealistic, and new engineers wonder "who's that guy with the whiteboard to say what we should be doing?" Instead, delegate the *hard, interesting* work down to people who can barely manage it (so they grow fast) and keep the boring "shoveling shit" work yourself — you have nothing left to prove, and it earns enormous trust.
- Why engineers distrust [management](../concepts/corporate-politics.md): authority without demonstrated understanding gets polite nods and silent non-compliance ("people will say, yeah, that's a pretty good idea, and then completely gaslight you"). His best influence outcome is overhearing someone champion, with conviction and as their own, an idea they once rejected from him — change without force.
- [Mentorship](../concepts/mentorship-and-sponsorship.md) strategy: pick mentees *outside* your own org — close-range mentoring teaches you nothing new, while distant mentees teach you about other parts of the company and let you "plant seeds" that change whole teams; keep it informal (no programs, plans, or schedules) and don't disqualify mentees for asking the wrong things — that's why they need mentoring.
- Politics at senior levels was the scary discovery that "nobody's in control — there's an illusion of control"; he kept sanity by saying no a lot, refusing dead-end projects, and exploiting the Denmark timezone: uninterrupted engineering days, with only a couple of evening hours exposed to San Francisco meetings and hallway VP grabs.
- He left Uber when new management brought top-down decisions engineers couldn't stand behind — e.g., a cloud migration justified on cost that "no engineer believed" and that only penciled out after a forced 50% platform cost cut that would have been cheaper on-prem; a colleague's suggestion to "stick around, do your own thing and take the money" felt impossible, so he concluded Uber no longer needed him at that level. Many departed colleagues went to Databricks; he went to an AI enterprise automation startup instead to build product, not re-build the same infrastructure.
- Biggest Uber engineering-culture mistakes: inability to effect global change (a tracing mandate was re-emailed for ~3 years and never got done) and a software networking stack built in Node ("turned out they did not know what they were talking about") that took years to untangle; the "let builders build" freedom that was right early on became "an insane strategy that's going to kill you" ten years in, and Uber never managed the transition from freedom to structure well.
- Advice to his younger self, having felt [imposter syndrome](../concepts/imposter-syndrome.md) joining Uber from "small tech": just try stuff — the big-tech people "were not that much better than me after all... it's not rocket science, it is just computers"; let curiosity lead, and periodically re-check whether what you're doing is still the best thing you could be doing.

## Notable quotes

- "The more people who are affected by what you do well, the higher you get in the level... a number of promotions will happen automatically. And not just for you, but the entire team." — Joakim, ~00:16:39
- "A software engineer needs to write code. If you're not writing code, you're not a software engineer... That applies to any level." — Joakim, ~00:29:30
- "Running code beats perfect code any day." — Joakim, ~00:31:58
- "Then you realize at some point nobody's in control. There's an illusion of control, but there's just people randomly getting ideas and pushing them out." — Joakim, ~00:49:02
- "I've tried enough to change how things are done with no effect. That just means, in my view, that Uber does not have the need for me at that level. Simple as that." — Joakim, ~01:10:01

## Connections

- [CloudKitchens CTO on Intelligence, Regrets, Steve Jobs and Travis Kalanick Stories](cloudkitchens-cto-on-intelligence.md) — fellow Uber alum (Brian Attwell was Senior Staff there); both critique scope-driven promo incentives, from opposite angles.
- [Shopify Distinguished Eng (L10) on Principal+ Engineering, Career Story, Regrets](distinguished-engineer-at-shopify.md) — another Distinguished-level career story about staff+ scope and influence.
- [Meta Distinguished Eng (IC9) On Influencing Engs, Failures, and Learnings](meta-distinguished-eng-ic9-on-influencing.md) — directly overlapping theme of influencing engineers without authority at the highest IC levels.
- [Airbnb Staff Eng on How To Not Get Stuck at Senior and Untold Rules of Calibrations](airbnb-staff-eng-on-how-to-not-get.md) — complementary insider view of calibration/promo committee mechanics and their unfairness.
- [Amazon VP Reveals Everything He's Seen In Corporate Politics](amazon-vp-reveals-everything-hes.md) — echoes Joakim's "illusion of control" view of politics at senior levels.
