---
type: entity
entity_kind: person
updated: 2026-07-19
sources: [aws-distinguished-eng-learnings-from.md]
---

# Marc Brooker

Distinguished Engineer at [AWS](aws.md) working on databases and serverless (Aurora Serverless, DSQL); rose from new grad to DE inside [Amazon](amazon.md) ([episode](../sources/aws-distinguished-eng-learnings-from.md)).

## Career arc

Spent his career at AWS, staying on call for 15 years because most of his practical [distributed-systems](../concepts/distributed-systems.md) knowledge came from on-call and postmortems. He changed organizations 4 times and says 5-6 would have been optimal — his top advice to his younger self is to be bolder about changing teams and keep asking what you're learning and from whom ([episode](../sources/aws-distinguished-eng-learnings-from.md)).

## Key views & advice

- Finding problems that matter means going super broad: intersect customer pain, bottom-up hardware trends, and macro industry shifts — Aurora Serverless and DSQL both came from colliding a customer signal with a technical trend (object storage as durability layer) ([episode](../sources/aws-distinguished-eng-learnings-from.md)).
- On [incident management](../concepts/incident-management.md): AWS's weekly company-wide COE/postmortem review is "a core, almost causal factor behind AWS's success." Great postmortems dig through multiple levels of why; cross-postmortem patterns should become whole-class fixes — DSQL was designed against common relational outage patterns. The two failure modes of postmortem culture are insufficient focus on outcomes and normalization of operational heroics ([episode](../sources/aws-distinguished-eng-learnings-from.md)).
- Caches are dangerous: warm/cold modality lets an un-scaled backend collapse into a metastable failure that is stable while down — rare per-system yet an underlying cause of a majority of the industry's biggest outages. Prefer materialized views, local copies of slow-moving data, or scalable backends ([episode](../sources/aws-distinguished-eng-learnings-from.md)).
- On [AI-era engineering](../concepts/ai-era-engineering.md): software has been supply-constrained for ~60 years; the mainstream will move to agentic/specification-driven development while hand-coding persists as craft. For juniors, business and customer context moves to the earliest career stages, but deep expertise is more leveraged than ever because asking the right questions matters more ([episode](../sources/aws-distinguished-eng-learnings-from.md)).
- For senior engineers: "if you aren't doing it hands on, your opinion about it is very likely to be completely wrong" — influence-role leaders must get back to hands-on building with agentic tools, which takes humility ([episode](../sources/aws-distinguished-eng-learnings-from.md)).
- On [writing](../concepts/teaching-and-communication.md): writing scales expertise across space and time; he writes docs he never shares just to sharpen thinking, and documenting which design decisions were reasoned vs arbitrary is almost as important as the decisions. His doing-vs-discussing sweet spot is ~75/25 practitioner-to-communicator, and long-term it's better to be underrated than overrated ([episode](../sources/aws-distinguished-eng-learnings-from.md)).

## Related

- [Episode: AWS Distinguished Eng: Learnings From 3000 Incidents](../sources/aws-distinguished-eng-learnings-from.md) — his interview
- [Mike Stonebraker](mike-stonebraker.md) — critiques the AWS database portfolio Brooker works on; opposite academia-vs-industry path
- [Leslie Lamport](leslie-lamport.md) — Brooker cites his writing/formal-thinking views and has debated Paxos edge cases
- [Barbara Liskov](barbara-liskov.md) — pioneered the replication techniques Brooker's systems industrialize
- [Brendan Burns](brendan-burns.md) — large-scale cloud infrastructure and AI-era engineering
- [databases](../concepts/databases.md), [career growth](../concepts/career-growth.md)
