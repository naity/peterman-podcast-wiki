---
type: entity
entity_kind: org
updated: 2026-07-19
sources: [airbnb-staff-eng-on-how-to-not-get.md, stripe-cto-on-what-grew-his-career.md]
---

# Stripe

Stripe, the payments company, appears in two episodes — from the top (David Singleton, CTO for 7 years) and from the senior-IC trenches (Laurent Charignon, "uber TL" of its developer-productivity org). Both describe an unusually deliberate, craft-obsessed operating culture.

## What the episodes reveal

- **Designed culture.** Stripe's operating principles (users first, meticulous in your craft) are concrete, distilled from the behaviors of its most effective employees, and periodically revised; culture is enforced by exemplifying it and by systems — hiring, performance evaluation, blameless incident review — because "if you don't invest in culture, you almost by definition will not have a culture." The famously helpful API error messages ("not found, but an object with that ID exists in the other mode") won customer CTOs' loyalty ([David Singleton](../sources/stripe-cto-on-what-grew-his-career.md)).
- **Operating systems for the org.** Singleton thinks of the org "as an operating system": he built nested weekly ops reviews modeled directly on [Amazon](amazon.md)'s (Charlie Bell personally walked him through Amazon's version), a program-management group, and the "engineer-acation" — roughly quarterly, leaders take ~3 days to join a team, ship a small real project, and write a friction log ([David Singleton](../sources/stripe-cto-on-what-grew-his-career.md)). Charignon institutionalized the same instinct bottom-up: friction logs — screenshot every step of a flow and interrogate each moment of friction; he could find 50–60 improvements in a single code-change flow ([Laurent Charignon](../sources/airbnb-staff-eng-on-how-to-not-get.md)).
- **Leading without authority at scale.** As uber TL over 35 (later 140) dev-productivity engineers, Charignon built credibility by embedding in each team for weeks, refused to justify decisions with "it worked at Facebook," and led almost entirely by asking questions — claiming he never outright rejected a design in his tenure. When leadership wanted to measure engineers by lines of code, he redirected: instrument the journey of a code change (think → write → CI → review → merge) to surface org-level friction instead of ranking individuals ([Laurent Charignon](../sources/airbnb-staff-eng-on-how-to-not-get.md)).
- **How senior hiring happens.** Singleton joined after asking the Collisons for *advice* on a startup idea — "anytime you want money, ask for advice, and anytime you want advice, ask for money"; Patrick Collison turned the advice conversation into recruiting, and the CTO title came later, mattering mainly for external signaling ([David Singleton](../sources/stripe-cto-on-what-grew-his-career.md)).

## People

- [David Singleton](david-singleton.md) — CTO for 7 years; ex-[Google](google.md) VP of Engineering
- [Laurent Charignon](laurent-charignon.md) — Staff engineer, uber TL of developer productivity

## Related

- [big-tech-culture](../concepts/big-tech-culture.md) — deliberately designed operating principles
- [developer-tools](../concepts/developer-tools.md) — friction logs, dev-productivity org
- [influence-and-leadership](../concepts/influence-and-leadership.md), [management](../concepts/management.md)
- [Amazon](amazon.md) — the ops-review template
