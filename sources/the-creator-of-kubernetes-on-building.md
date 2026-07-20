---
type: source
updated: 2026-07-19
raw: ../raw/the-creator-of-kubernetes-on-building.md
guest: "Brendan Burns"
guest_role: "Co-creator of Kubernetes, Technical Fellow/CVP at Microsoft"
date: 2026-03-23
url: https://www.developing.dev/p/the-creator-of-kubernetes-on-building
---

# The Creator of Kubernetes On Building Kubernetes

Brendan Burns co-created Kubernetes at [Google](../entities/google.md) and is now a Technical Fellow/CVP at [Microsoft](../entities/microsoft.md) working on Azure infrastructure. The episode is a builder's history of Kubernetes: how he pitched an open-source container orchestrator to Google leadership in an AWS-dominated world, hacked together the MVP in under a week, made the architectural bets (etcd, API server, loose coupling, declarative config) that made the system stable, and then deliberately gave the project away — writing a literal governance constitution so no single company could own it ([open-source](../concepts/open-source.md)).

## Key takeaways

- The internal pitch at [Google](../entities/google.md) leaned on the MapReduce/Hadoop lesson: Google published the paper but Hadoop became the implementation everyone ran — "if it's not something that people can run, we're not going to be in the driver's seat." Open-sourcing was framed as "creating a brand new playing field where you are the thought leader," and keeping it platform-exclusive was rejected because "the majority of people are going to be not on your platform" ([startups-and-founding](../concepts/startups-and-founding.md) via competitive strategy, [big-tech-culture](../concepts/big-tech-culture.md)).
- The Kubernetes MVP took roughly four to five days to write, and the demo already showed container deployment across machines, load balancing across replicas, health checking, and V1-to-V2 upgrades.
- On making time for unsanctioned work: "I believe you can hide order 10% of your effort from your management... you should always have something that nobody told you to do, but that you think is important." Expect a portfolio payoff — bet five times and one hit beats grinding for exceeds every cycle ([career-growth](../concepts/career-growth.md)).
- The hardest architectural aspect was the early decision to make Kubernetes a loosely coupled system of ~15 cooperating processes: great resiliency, painful debugging ("you can see that the outcome wasn't achieved... now I have to sift through a bunch of different logs") ([distributed-systems](../concepts/distributed-systems.md), [systems-design](../concepts/systems-design.md)).
- Leader election was delegated "pretty exclusively" to etcd (a Raft-based key-value store — provably correct consensus that's "way easier to implement" than Paxos), and Burns pushed hard for the rule that every component accesses state only through the API server, which meant "everybody gets to restart all the time and they just come up and they work" — the key to stability.
- Community buy-in from Red Hat and others worked because orchestration was "undifferentiated heavy lifting" they'd otherwise build alone, plus a real "seat at the design table." To prevent Google dominance, Kubernetes was donated to the CNCF and in 2016 six or seven people literally wrote a governance constitution and steering committee in "a couple, three fairly intense meetings" ([open-source](../concepts/open-source.md), [influence-and-leadership](../concepts/influence-and-leadership.md)).
- Early Kubernetes "couldn't really handle more than about 100 nodes"; scaling to AI-training sizes (OpenAI ran 7,500-node clusters) meant reducing API noise and fighting etcd as the main bottleneck — "everything else is basically horizontally scalable... it's the storage layer that is the bottleneck." Meanwhile most real users went the other way: hundreds or thousands of small clusters ([ai-era-engineering](../concepts/ai-era-engineering.md)).
- On the PhD question: career-wise "it probably doesn't matter one way or the other" (an undergrad classmate reached the same level via startups), but the writing, arguing and teaching skills mattered — explaining computing to novices "really helped me organize the initial parts of the Kubernetes project" ([teaching-and-communication](../concepts/teaching-and-communication.md), [regrets-and-advice](../concepts/regrets-and-advice.md)).
- "The inevitable trajectory of software is death": don't cling to dying systems; his original source code has been rewritten many times. Kubernetes' successor may be natural-language interfaces ("way easier to say I would like a reliable web service than YAML, YAML, YAML") or simple invisibility — "people focus so much on the AI that they forget about the Kubernetes part. And I think that's happening already."
- Book recommendations: Design Patterns (Gang of Four) for early career; Leadership on the Line and The Five Dysfunctions of a Team for leaders. Advice to younger self: "Keep better notes" — the interpersonal/partner history of Kubernetes is largely undocumented.

## Notable quotes

- "You can't win if you make it only on your platform... the majority of people are going to be not on your platform." — Brendan Burns (~00:05)
- "I believe you can hide order 10% of your effort from your management." — Brendan Burns (~00:12)
- "Every time you increase by an order of magnitude, what you thought was the main problem is going to become easy and then the problem moves somewhere else." — Brendan Burns (~00:53)
- "It could be that people focus so much on the AI that they forget about the Kubernetes part. And I think that's happening already." — Brendan Burns (~01:03)

## Connections

- [AWS Distinguished Eng: Learnings From 3000 Incidents And How Engineering Is Changing | Marc Brooker](aws-distinguished-eng-learnings-from.md) — large-scale distributed infrastructure, reliability and how AI changes systems engineering.
- [Turing Award Winner On Thinking Clearly, Paxos vs Raft, Working with Dijkstra | Leslie Lamport](turing-award-winner-on-working-with.md) — Kubernetes leans on Raft-based etcd; Lamport invented Paxos and discusses Paxos vs Raft directly.
- [Dropbox's Former Most Senior Eng: Building Great Systems and Advice for the AI Era | James Cowling](dropboxs-former-most-senior-eng-building.md) — building great systems, distributed-systems design taste, AI-era advice.
- [Turing Award Winner: Postgres, Disagreeing with Google, Future Problems | Mike Stonebraker](turing-award-winner-postgres-disagreeing.md) — another canonical open-source infrastructure project and its ecosystem strategy.
- [Intern to Microsoft Distinguished Engineer in 11 Promotions (Career Story)](intern-to-microsoft-distinguished.md) — reaching the most senior IC levels at Microsoft, where Burns is a Technical Fellow.

## Notes

Guest is not named in the manifest title; page identifies him as Brendan Burns.
