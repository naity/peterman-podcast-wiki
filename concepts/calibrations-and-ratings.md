---
type: concept
updated: 2026-07-19
sources: [meta-senior-manager-m2-on-manager.md, airbnb-staff-eng-on-how-to-not-get.md, distinguished-eng-on-stack-ranking.md, amazon-vp-on-promotions-getting-fired.md, instagram-senior-staff-eng-ic7-on.md, retired-netflix-engineering-director.md, cloudkitchens-cto-on-intelligence.md, instagram-staff-ic6-promo-despite.md, meta-senior-staff-ic7-engs-honest.md, quitting-robinhood-and-raising-35m.md, 26-year-old-meta-staff-eng-ic6-on.md, msl-eng-director-promo-hacking-industry.md, instagram-principal-eng-ic8-on-building.md, intern-to-microsoft-distinguished.md, uber-distinguished-eng-on-unfair.md, meta-senior-staff-eng-ic7-on-zuck.md, tech-lead-for-metas-most-used-programming.md]
---

# Calibrations and ratings

The performance-review machinery of big tech — calibration rooms, rating scales ("redefines expectations", "top tier"), low-performer quotas, stack ranking, and PIPs — described from both the manager's chair and the receiving end.

## What the guests say

### How the machinery works

Stefan Mai, who administered the process at both Amazon and Meta, says the two systems converge: public ratings plus a *private* VP/director process (Amazon "top tier", Meta discretionary equity) that picks linchpins by trajectory and irreplaceability. He estimates the review process costs ~$15,000 per engineer per cycle and defends it anyway: "the integrity of the performance review process is the whole ball game" — if people stop believing it rewards performance, they stop performing ([episode](../sources/meta-senior-manager-m2-on-manager.md)). Marius Schulz explains the Meta calibration vocabulary from the IC side: "laddering" articulates why doing next-*next*-level work separates "redefines expectations" from "greatly exceeds" ([episode](../sources/instagram-senior-staff-eng-ic7-on.md)); Simon Kindström earned "redefines" twice through persistence on failing experiments ([episode](../sources/26-year-old-meta-staff-eng-ic6-on.md)).

Laurent Charignon exposes the folklore layer: calibrations run on untold, locally-developed rules — e.g. changing roles less than ~2.5 months before cycle end yields an automatic "meets expectations", a rule that cost him a probable staff promotion. To dispute one, never fight in the calibration room; go one-on-one, gather evidence, and first learn the story behind the rule ([episode](../sources/airbnb-staff-eng-on-how-to-not-get.md)). His manager-side discipline was a "surprise factor" metric — any mismatch between the rating a report expected and received, including positive surprises, counted as a coaching failure ([same episode](../sources/airbnb-staff-eng-on-how-to-not-get.md)).

### The stack-ranking argument

The strongest disagreement in the corpus. Bryan Cantrill calls stack ranking "organizational cancer": firing a bottom percentage incentivizes managers to keep dead weight as sacrificial fodder (he watched it at Sun) and "teaches you that your team are adversaries"; Oxide has no ranks at all ([episode](../sources/distinguished-eng-on-stack-ranking.md)). Ethan Evans, from the Amazon VP chair, defends the quota's existence with data: when Amazon removed its unregretted-attrition goal (~4–7%/year), managers simply stopped having hard conversations, so it came back ([episode](../sources/amazon-vp-on-promotions-getting-fired.md)). Stefan Mai lands between them: low-performer quotas (roughly 7–15%, sometimes 20%) are universal at scale and the process is worth its cost — but he names the nightmare case, a director forcing a manager to retroactively downgrade someone they'd praised all half ([episode](../sources/meta-senior-manager-m2-on-manager.md)). David Ronca, having lived Netflix's *absence* of leveling and individual credit, argues the opposite corner: objective, data-driven calibration was "the most valuable thing Meta taught me" — without it, credit accrues to leaders and your best engineers leave ([episode](../sources/retired-netflix-engineering-director.md)).

### PIPs: escapable or not?

A direct factual disagreement. Ethan Evans: PIPs are self-fulfilling — everyone he coached through one was fired anyway, so spend the PIP time job hunting ([episode](../sources/amazon-vp-on-promotions-getting-fired.md)). Stefan Mai: PIPs are first a legal paper trail, but people *genuinely escape them*, because the trail loses legal credibility if nobody survives; Amazon HR was savage box-checking while Meta HR exhausted every avenue to protect its employer brand ([episode](../sources/meta-senior-manager-m2-on-manager.md)). The two men overlapped at Amazon; the disagreement is about the same system.

### What ratings actually buy you — and don't

Jayendra Jog's formative disillusionment: months of 2 AM nights earned a 5/5 rating with *no* promotion or compensation change attached, after which he deliberately coasted ([episode](../sources/quitting-robinhood-and-raising-35m.md)). Cantrill saw the inverse pathology at Sun: a "superlative" grade *forced* a promotion, so managers apologetically withheld the top grade because promos were rationed to every 18 months ([episode](../sources/distinguished-eng-on-stack-ranking.md)). Ryan Olson's dual TL/manager role averaged his ratings down ([episode](../sources/instagram-principal-eng-ic8-on-building.md)), and for senior external hires the clock is hostile: Igor found that joining Meta at E7 means being calibrated against tenured E7s within about a year, under a bottom-10% culture ([episode](../sources/meta-senior-staff-ic7-engs-honest.md)).

### Gaming, Goodhart, and alternatives

Sash Zats invokes Goodhart's law — any chosen metric degrades as people game it, and much of what matters isn't measurable — while conceding big companies need frameworks because nothing else scales; his experimental hardware team was explicitly reviewed on *de-risking directions*, showing systems can protect risk-takers ([episode](../sources/instagram-staff-ic6-promo-despite.md)). Marius Schulz treats diff counts as "directionally interesting" but gameable ([episode](../sources/instagram-senior-staff-eng-ic7-on.md)); Laurent Charignon redirected a leadership request to rank engineers by LOC/PR counts into instrumenting the code-change journey — org-level friction data instead of unfair individual ranking ([episode](../sources/airbnb-staff-eng-on-how-to-not-get.md)). John Myles White saw goal culture plus statistical illiteracy produce a team planning to ship a metric win July 1 and delete it July 2 — he used rating authority to stop it ([episode](../sources/msl-eng-director-promo-hacking-industry.md)). The most radical rebuild: CloudKitchens threw out an Uber-style scope-indexed ladder after Travis Kalanick rejected it, distilling ~1,000 real performance examples into 12 skill gradients that reward truth-seeking over politics-friendly "influencing other teams" competencies ([Brian Attwell](../sources/cloudkitchens-cto-on-intelligence.md)).

## Practical takeaways

- Eliminate surprise: align with your manager on the expected rating *before* the cycle ends; a surprised report is a failed manager ([Laurent Charignon](../sources/airbnb-staff-eng-on-how-to-not-get.md)).
- Learn your org's untold calibration rules (role-change cutoffs, promo windows) before making moves, and dispute rules one-on-one with evidence, never in the room ([Laurent Charignon](../sources/airbnb-staff-eng-on-how-to-not-get.md)).
- If you're PIP'd at Amazon-style companies, treat the clock as a job-search runway; at reputation-protective companies, a genuine escape is possible — read your HR culture ([Ethan Evans](../sources/amazon-vp-on-promotions-getting-fired.md), [Stefan Mai](../sources/meta-senior-manager-m2-on-manager.md)).
- Ratings and rewards are separate systems; a top rating with nothing attached is a signal to renegotiate or leave ([Jayendra Jog](../sources/quitting-robinhood-and-raising-35m.md)).
- Joining senior from outside, budget for the calibration clock: ramp by building, not by reading docs ([Igor](../sources/meta-senior-staff-ic7-engs-honest.md)).
- Don't measure engineers by output counts; measure the system's friction instead ([Laurent Charignon](../sources/airbnb-staff-eng-on-how-to-not-get.md), [Sash Zats](../sources/instagram-staff-ic6-promo-despite.md)).

## Related

- [promotions](promotions.md) — the decisions calibration feeds
- [layoffs](layoffs.md) — quotas and unregretted attrition as the system's sharp edge
- [management](management.md) — the manager's side of the process
- [compensation-and-equity](compensation-and-equity.md) — the private money layer above public ratings
- Key people: [Stefan Mai](../entities/stefan-mai.md), [Laurent Charignon](../entities/laurent-charignon.md), [Bryan Cantrill](../entities/bryan-cantrill.md), [Ethan Evans](../entities/ethan-evans.md), [David Ronca](../entities/david-ronca.md)
- Most relevant episodes: [Untold rules of calibrations](../sources/airbnb-staff-eng-on-how-to-not-get.md), [M2 on PIPs, Amazon vs Meta](../sources/meta-senior-manager-m2-on-manager.md), [Stack ranking as organizational cancer](../sources/distinguished-eng-on-stack-ranking.md)
