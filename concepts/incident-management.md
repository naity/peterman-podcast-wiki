---
type: concept
updated: 2026-07-19
sources: [aws-distinguished-eng-learnings-from.md, airbnb-staff-eng-on-how-to-not-get.md, google-deepmind-pre-training-lead.md, intern-to-microsoft-distinguished.md, mozilla-firefox-cto-on-browser-war.md, staff-engineer-meta-by-age-25-evan.md, stripe-cto-on-what-grew-his-career.md, dropboxs-former-most-senior-eng-building.md, retired-netflix-engineering-director.md]
---

# Incident management

On-call, postmortems, and outages — dominated by [Marc Brooker](../entities/marc-brooker.md)'s learnings from 3,000+ AWS incident reviews, with contrasting views from other guests on heroics, preparation, and what incidents do to careers.

## What the guests say

### Postmortems as an institution

Brooker calls [AWS](../entities/aws.md)'s weekly COE meeting — engineers and senior leaders reviewing incidents together — "a core, almost causal factor behind AWS's success," because it forces leadership bandwidth onto how systems actually operate. A great postmortem digs through multiple levels of "why" (code bug → testing gap → organizational cause), produces fixes at each level, and patterns across postmortems get leveled up into whole-class fixes — Aurora DSQL was designed against recurring relational-database outage patterns. He estimates he has read 3,000–4,000 of them ([episode](../sources/aws-distinguished-eng-learnings-from.md)). [David Singleton](../entities/david-singleton.md) lists blameless incident review among the systems that enforce culture at [Stripe](../entities/stripe.md) — alongside hiring and performance evaluation ([episode](../sources/stripe-cto-on-what-grew-his-career.md)).

### Heroics: the field's live disagreement

Brooker names two failure modes of postmortem culture, and the harder one is normalization of operational heroics: superhuman on-calls hacking around root causes feels like strong ownership from the inside but is "a fantastically expensive investment" in a break-fix cycle ([episode](../sources/aws-distinguished-eng-learnings-from.md)). Yet Brooker himself stayed on call for 15 years because "the majority of my in-practice knowledge about how to build distributed systems has come from being on call" — his resolution is that on-call should surface *unexpected* behavior for deep experts while rote ticket-closing gets automated. [James Cowling](../entities/james-cowling.md) pushes back on the modeling instinct from another angle: when he jumped on every page to demonstrate ownership, his team concluded that was "James's job" — don't lead by example; explicitly teach and reframe on-call as empowering ownership instead ([episode](../sources/dropboxs-former-most-senior-eng-building.md)). [David Ronca](../entities/david-ronca.md) goes furthest against heroics: he ordered a burned-out engineer to take a vacation regardless of outages — "if things break, they break" — and the team stabilized the system precisely because they stepped back ([episode](../sources/retired-netflix-engineering-director.md)).

### Preparation beats response

- [Bobby Holley](../entities/bobby-holley.md)'s Mozilla story is the strongest case for structural preparation: when a threat actor exfiltrated ~45 security bugs from Bugzilla, all but ~2 were already fixed because his "Slaughterhouse" project had eliminated the exploit class in advance — "sometimes you don't have the luxury of time" ([episode](../sources/mozilla-firefox-cto-on-browser-war.md)).
- [Laurent Charignon](../entities/laurent-charignon.md) reports [Airbnb](../entities/airbnb.md) hiring actual firefighters and crisis-management professionals to run incident management — a practice he carried to every later job. Notably, incidents were the *only* time this question-led influence practitioner would outright tell people what to do — command-and-control has its one legitimate hour ([episode](../sources/airbnb-staff-eng-on-how-to-not-get.md)).
- [David Fowler](../entities/david-fowler.md) argues debugging under fire is the real high-leverage skill — "diagnosing race conditions at 1am with 100 engineers on a call" — and would interview candidates by handing them a crash dump ([episode](../sources/intern-to-microsoft-distinguished.md)).

### Incidents at the frontier, and as career events

[Vlad Feinberg](../entities/vlad-feinberg.md) describes AI-lab operations as incident management by another name: after the pipeline-prefill breakthrough that made Gemini 2.0's MoE possible came 40 days of round-the-clock training babysitting by a ~5-person rotation across two continents — and "pure research" teams act as SREs for training runs ([episode](../sources/google-deepmind-pre-training-lead.md)). [Evan King](../entities/evan-king.md)'s Senior-to-Staff promotion came from leading the creation of Meta's real-time integrity team after the Christchurch incident — a reminder that incident response, with its unusual visibility and stakes, is where scope gets created ([episode](../sources/staff-engineer-meta-by-age-25-evan.md)).

## Practical takeaways

- Run a standing, leadership-attended postmortem review; its output should be whole-class fixes (services, libraries, design changes), not just action items ([Brooker](../sources/aws-distinguished-eng-learnings-from.md)).
- Push every postmortem through multiple "whys" — code, testing, process — and fix at each level ([Brooker](../sources/aws-distinguished-eng-learnings-from.md)).
- Watch for normalized heroics: if your best on-calls are superhuman, you're funding a break-fix cycle instead of fixing root causes ([Brooker](../sources/aws-distinguished-eng-learnings-from.md), [Ronca](../sources/retired-netflix-engineering-director.md)).
- Don't model on-call ownership silently — teach it explicitly, or the team will decide it's your job ([Cowling](../sources/dropboxs-former-most-senior-eng-building.md)).
- Eliminate failure classes before the incident; assume your bug tracker or system will eventually be compromised or overloaded ([Holley](../sources/mozilla-firefox-cto-on-browser-war.md)).
- Treat incident command as a profession — consider dedicated crisis-management hires and a clear switch to directive leadership during incidents ([Charignon](../sources/airbnb-staff-eng-on-how-to-not-get.md)).
- Train and hire for debugging under pressure (crash dumps, race conditions), not just feature work ([Fowler](../sources/intern-to-microsoft-distinguished.md)).

## Related

- [distributed-systems](distributed-systems.md) — the systems on fire; [systems-design](systems-design.md) — postmortems as design input; [security-and-cryptography](security-and-cryptography.md) — breach response; [career-growth](career-growth.md) — incidents as scope-creating moments.
- Key people: [Marc Brooker](../entities/marc-brooker.md), [Bobby Holley](../entities/bobby-holley.md), [Laurent Charignon](../entities/laurent-charignon.md), [David Fowler](../entities/david-fowler.md).
- Most relevant episodes: [Brooker](../sources/aws-distinguished-eng-learnings-from.md), [Holley](../sources/mozilla-firefox-cto-on-browser-war.md), [Charignon](../sources/airbnb-staff-eng-on-how-to-not-get.md).
