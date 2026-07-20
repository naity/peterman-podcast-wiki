---
type: entity
entity_kind: org
updated: 2026-07-19
sources: [amazon-vp-reveals-everything-hes.md, aws-distinguished-eng-learnings-from.md, distinguished-eng-on-stack-ranking.md, dropboxs-former-most-senior-eng-building.md, turing-award-winner-postgres-disagreeing.md]
---

# AWS

Amazon Web Services is the cloud arm of [Amazon](amazon.md), appearing in the podcast as the definitive large-scale distributed-systems employer (Marc Brooker's episode), as a competitor (Bryan Cantrill's Joyent), and as the incumbent that Dropbox famously left.

## What the episodes reveal

- **Operational culture as a causal advantage.** Marc Brooker (EC2, EBS, Lambda, Aurora, Aurora DSQL) calls AWS's weekly Wednesday COE (postmortem) meeting — engineers and senior leaders across the company reviewing incidents together — "a core, almost causal factor behind AWS's success"; he has read 3,000–4,000 postmortems and stayed on call for 15 years because that's where his distributed-systems knowledge came from. Patterns across postmortems get leveled up into services and whole-class fixes: DSQL was explicitly designed against common relational-database outage patterns ([Marc Brooker](../sources/aws-distinguished-eng-learnings-from.md)). He also warns against the failure mode of normalized operational heroics, and argues caches are an underlying cause of "probably a majority" of the industry's biggest outages ([same](../sources/aws-distinguished-eng-learnings-from.md)).
- **Competitive strategy.** Cantrill, competing head-on at Joyent, says Amazon hid AWS's margins by not breaking out revenue and cut prices at every re:Invent 2010–2015 to convince the world cloud was a terrible business — while insiders knew the margins were great ([Bryan Cantrill](../sources/distinguished-eng-on-stack-ranking.md)). Ethan Evans's politics episode captures how AWS teams are underestimated from outside: S3 dismissed by raiders as "just a big disk drive" ([Amazon VP on politics](../sources/amazon-vp-reveals-everything-hes.md)).
- **The customer's-eye view.** James Cowling led Dropbox's Magic Pocket, the multi-exabyte system that migrated Dropbox *off* S3 — then the largest data migration in history, peaking at 764 Gbps out of AWS — justified by strategic control, pre-IPO cost savings, and a workload understanding a general-purpose service couldn't match; yet he still tells almost everyone else not to build their own infrastructure ([James Cowling](../sources/dropboxs-former-most-senior-eng-building.md)).
- **Portfolio critique.** Mike Stonebraker told Amazon its ~15 database systems are "about 12 too many" — graph databases are almost never the performant option and should be layers over relational systems ([Stonebraker](../sources/turing-award-winner-postgres-disagreeing.md)); Brooker builds that portfolio and defends finding problems by colliding customer signals with technical trends (Aurora Serverless, DSQL) ([Marc Brooker](../sources/aws-distinguished-eng-learnings-from.md)).

## People

- [Marc Brooker](marc-brooker.md) — Distinguished Engineer, databases/serverless; new grad to DE
- [Bryan Cantrill](bryan-cantrill.md) — competitor as Joyent CTO
- [James Cowling](james-cowling.md) — led the Dropbox migration off S3

## Related

- [incident-management](../concepts/incident-management.md) — the COE/postmortem culture
- [distributed-systems](../concepts/distributed-systems.md), [systems-design](../concepts/systems-design.md)
- [databases](../concepts/databases.md) — the "12 too many" debate
- [Amazon](amazon.md)
