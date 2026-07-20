---
type: entity
entity_kind: person
updated: 2026-07-19
sources: [the-creator-of-kubernetes-on-building.md]
---

# Brendan Burns

Co-creator of Kubernetes at [Google](google.md); now Technical Fellow/CVP at [Microsoft](microsoft.md) ([episode](../sources/the-creator-of-kubernetes-on-building.md)).

## Career arc

At Google he pitched open-sourcing Kubernetes using the MapReduce/Hadoop lesson — publishing the paper but not the runnable implementation had left Google out of the driver's seat — and rejected platform exclusivity because "the majority of people are going to be not on your platform." The MVP took four to five days to write and already demoed container deployment, load balancing, health checking, and rolling upgrades. Google deliberately gave up control by donating Kubernetes to the CNCF with a literal governance constitution in 2016 so no single company could dominate; Red Hat and others joined because orchestration was undifferentiated heavy lifting they'd otherwise each build. He later moved to Microsoft as Technical Fellow. His PhD, he says, probably didn't matter for career level, but its writing, argumentation, and teaching skills directly shaped how Kubernetes was organized to be learnable ([episode](../sources/the-creator-of-kubernetes-on-building.md)).

## Key views & advice

- On [open source](../concepts/open-source.md) strategy: open-sourcing created a new playing field where Google was the thought leader rather than fighting on rivals' terms ([episode](../sources/the-creator-of-kubernetes-on-building.md)).
- "You can hide order 10% of your effort from your management": always keep a self-directed project you believe in, and expect portfolio economics — one hit out of five bets beats grinding for top ratings every cycle ([episode](../sources/the-creator-of-kubernetes-on-building.md)).
- Hardest architectural call in [systems design](../concepts/systems-design.md): making Kubernetes ~15 loosely coupled cooperating processes — excellent resiliency, painful debugging. Forcing every component through the API server meant anything could restart and recover, the key to stability; leader election was delegated to etcd's Raft, provably correct and much easier than Paxos ([episode](../sources/the-creator-of-kubernetes-on-building.md)).
- Scaling law: "every time you increase by an order of magnitude, what you thought was the main problem is going to become easy and then the problem moves somewhere else" — early Kubernetes capped near 100 nodes; [OpenAI](openai.md) pushed 7,500-node clusters while most users unexpectedly went to thousands of small clusters instead ([episode](../sources/the-creator-of-kubernetes-on-building.md)).
- "The inevitable trajectory of software is death": his original code has been rewritten many times; Kubernetes' successor may be natural-language interfaces replacing YAML, or the system simply becoming invisible as attention shifts to AI — "I think that's happening already" ([episode](../sources/the-creator-of-kubernetes-on-building.md)).
- Care that you're learning, not what you learn; keep better notes (the interpersonal history of Kubernetes is undocumented). Books: Design Patterns early career, Leadership on the Line and The Five Dysfunctions of a Team for leaders ([episode](../sources/the-creator-of-kubernetes-on-building.md)).

## Related

- [Episode: The Creator of Kubernetes On Building Kubernetes](../sources/the-creator-of-kubernetes-on-building.md) — his interview
- [Leslie Lamport](leslie-lamport.md) — Kubernetes relies on Raft-based etcd; Lamport on Paxos vs Raft
- [Marc Brooker](marc-brooker.md) — large-scale cloud infrastructure and reliability
- [distributed systems](../concepts/distributed-systems.md), [influence and leadership](../concepts/influence-and-leadership.md), [ai-era engineering](../concepts/ai-era-engineering.md)
