---
type: source
updated: 2026-07-19
raw: ../raw/aws-distinguished-eng-learnings-from.md
guest: "Marc Brooker"
guest_role: "Distinguished Engineer at AWS (databases/serverless), new grad to DE at Amazon"
date: 2026-04-13
url: https://www.developing.dev/p/aws-distinguished-eng-learnings-from
---

# AWS Distinguished Eng: Learnings From 3000 Incidents And How Engineering Is Changing | Marc Brooker

[Marc Brooker](../entities/marc-brooker.md) joined [AWS](../entities/aws.md) as a new grad and rose to Distinguished Engineer, working across EC2, EBS, Lambda, Aurora, and Aurora DSQL. The episode distills what he's learned from reading 3,000–4,000 postmortems, why he stayed on call for 15 years, the technical case against caches ([metastable failures](../concepts/incident-management.md)), how [AI is changing software engineering](../concepts/ai-era-engineering.md) for junior and senior engineers, and why writing is the highest-leverage skill for technical people.

## Key takeaways

- Finding problems that matter requires going "super broad": combine what customers say is still hard, bottom-up hardware/technical trends (faster networks, storage, GPUs), and macro industry shifts — moments of change carry the opportunity. Aurora Serverless and Aurora DSQL both came from colliding a customer signal (serverless devs stuck with serverful relational databases) with a technical trend (object storage as the durability layer) ([systems-design](../concepts/systems-design.md)).
- He stayed on call for 15 years because "the majority of my in-practice knowledge about how to build distributed systems has come from being on call" — on-call should surface unexpected system behavior for deep experts, while rote ticket-closing should be automated ([incident-management](../concepts/incident-management.md), [distributed-systems](../concepts/distributed-systems.md)).
- [AWS](../entities/aws.md)'s weekly Wednesday COE (postmortem) meeting — engineers and senior leaders across the company reviewing incidents together — is in his view "a core, almost causal factor behind AWS's success" because it forces leadership bandwidth and top engineering time onto deeply understanding how systems actually operate.
- He estimates he's read 3,000–4,000 postmortems/COEs. A great postmortem digs through multiple levels of "why" (code bug → testing gap → process/organizational cause), produces concrete fixes at each level, and patterns across postmortems should be leveled up into services, libraries, or whole-class fixes — DSQL was explicitly designed against common relational-database outage patterns (e.g. a client starting a transaction, stalling, and holding locks; DSQL avoids this with MVCC plus optimistic commit-time checks, so readers never block writers and vice versa; MVCC storage overhead is typically under ~10%).
- Two failure modes of bad postmortem culture: insufficient focus on outcomes, and — harder to fix — normalization of operational heroics, where superhuman on-calls hacking around root causes feels like strong ownership from the inside but is "a fantastically expensive investment" in a break-fix cycle.
- Caches are dangerous in distributed systems because they create modality: a full-cache mode that's fast and an empty/cold-cache mode where the un-scaled backend collapses — a metastable failure that is stable in the down state. Rare per-system (you may go years without one) but an underlying cause "in probably a majority" of the industry's biggest outages. Prefer complete materialized views, local in-memory copies of slow-moving data, or a scalable backend over bolting on caches.
- On AI: software has been supply-constrained for its entire ~60-year history and the opportunity is nearly unbounded; the mainstream will adopt agentic/AI-powered/specification-driven development, while hand-craft coding persists as joy (like hand joinery) and legacy "old way" niches remain economically real but shrinking ([ai-era-engineering](../concepts/ai-era-engineering.md), [ai-coding-tools](../concepts/ai-coding-tools.md)).
- Advice for junior engineers: customer/business/context understanding is moving from senior-engineer work to the earliest career stages; the pure "type in the IDE for 8 hours" career is disappearing, but deep technical/scientific expertise is more leveraged than ever because asking the right questions matters more. Employers' and juniors' incentives are aligned — leaders must redesign the early-career ladder ([career-growth](../concepts/career-growth.md)).
- Advice for senior engineers: "if you aren't doing it hands-on, your opinion about it is very likely to be completely wrong" — influence-role leaders must get back to building with modern agentic tools; admitting this takes humility that's hard for people with fancy titles. S3 and EC2 endured because leadership at all levels was grounded in the details.
- Writing scales expertise across space and time better than any other medium and forces mental clarity ([teaching-and-communication](../concepts/teaching-and-communication.md)); he sometimes writes docs he never shares just to sharpen his thinking. Documenting which design decisions were carefully reasoned versus arbitrary is almost as important as the decisions themselves.
- From his "Four Hobbies and Apparent Expertise" 2x2 (doing vs discussing): 100% on either axis is a failure mode; his personal sweet spot is ~75/25 practitioner-to-communicator, and long-term it's better to be underrated than overrated ([influence-and-leadership](../concepts/influence-and-leadership.md), [visibility](../concepts/influence-and-leadership.md)).
- He admires Allan Vermeulen (early S3 architect, one-time Amazon CTO) for operating at every level — arguing Paxos edge cases while also setting cloud strategy — and for not wanting to be a celebrity. Book recommendations: Kleppmann's Designing Data-Intensive Applications, Hennessy & Patterson's computer architecture book, a quantitative systems design book, plus papers (now more accessible with Claude summarizing them) and old sources like Erlang's telephone-traffic work that informed Lambda's traffic management.
- Advice to his younger self: be bolder about changing teams — he changed organizations 4 times and "maybe five or six would have been optimal"; keep asking what you're learning, who you're learning from, and follow curiosity ([regrets-and-advice](../concepts/regrets-and-advice.md)).

## Notable quotes

- "The majority of my in practice knowledge about how to build distributed systems has come from being on call and analyzing and deeply understanding these post mortems and COEs." — Marc Brooker (5:59)
- "The best estimate I could come up to... was between 3000 and 4000 [postmortems read], and so know even a little bit of lesson from each one, and it tends to, you know, tends to stick." — Marc Brooker (11:33)
- "We are in this minute that if you aren't doing it hands on, your opinion about it is very likely to be completely wrong. And that takes a level of humility to admit." — Marc Brooker (47:31)
- "Writing lets you scale out the impact of your expertise in space and time in a way that's really hard to do in other media." — Marc Brooker (51:21)

## Connections

- [Turing Award Winner: Postgres, Disagreeing with Google, Future Problems | Mike Stonebraker](turing-award-winner-postgres-disagreeing.md) — direct counterpoint: Brooker builds the AWS database portfolio Stonebraker says is "12 too many," and took the big-tech distinguished engineer path Stonebraker rejected.
- [Turing Award Winner On Thinking Clearly, Paxos vs Raft, Working with Dijkstra | Leslie Lamport](turing-award-winner-on-working-with.md) — Brooker explicitly cites Lamport's episode and extends the writing-for-clarity argument (Lamport pushes it further into formal math); he also debated Paxos edge cases at AWS.
- [Turing Award Winner: TPUs vs GPUs vs CPUs, Computer Architecture, RISC vs CISC | David Patterson](turing-award-winner-tpu-vs-gpu-vs.md) — Brooker recommends Hennessy & Patterson's architecture book; hardware trends drive his problem-finding.
- [Dropbox's Former Most Senior Eng: Building Great Systems and Advice for the AI Era | James Cowling](dropboxs-former-most-senior-eng-building.md) — same pairing of large-scale systems craft with advice for the AI era.
- [Distinguished Eng On Stack Ranking, Competing with Bezos, Regrets | Bryan Cantrill](distinguished-eng-on-stack-ranking.md) — fellow distinguished-engineer-level systems veteran reflecting on cloud infrastructure careers and Amazon.
- [OpenAI Eng & Dev Tools Founder: How Software Engineering Is Changing | Charlie Marsh](openai-eng-and-dev-tools-founder.md) — shared theme of how AI tooling is reshaping the practice of software engineering.
