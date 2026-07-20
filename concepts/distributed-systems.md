---
type: concept
updated: 2026-07-19
sources: [aws-distinguished-eng-learnings-from.md, dropboxs-former-most-senior-eng-building.md, google-deepmind-pre-training-lead.md, the-creator-of-kubernetes-on-building.md, turing-award-winner-data-abstraction.md, turing-award-winner-on-working-with.md, turing-award-winner-postgres-disagreeing.md, uber-distinguished-eng-on-unfair.md]
---

# Distributed systems

How the podcast's guests — spanning the people who invented consensus protocols to the people who operate hundreds of thousands of machines — think about building computer systems that span many machines and keep working when parts fail.

## What the guests say

### The consensus lineage: one idea, three names

[Barbara Liskov](../entities/barbara-liskov.md) and [Leslie Lamport](../entities/leslie-lamport.md), interviewed separately, tell two halves of the same story: her Viewstamped Replication and his Paxos are "essentially the same idea" invented independently — views are just incrementing numbers, no clocks — and the leader-failure step is the key advance both share over transaction-commit protocols ([episode](../sources/turing-award-winner-data-abstraction.md)). Paxos won the mindshare anyway; per Lamport (quoted approvingly by Liskov): "I went around giving all the talks and she implemented it." A former student of hers even recognized the Google File System's replication as Viewstamped Replication while [Google](../entities/google.md) "seemed to think it was Paxos." Lamport's own origin story is that Paxos began as an attempted impossibility proof of DEC's distributed storage design — "this isn't a proof, this is an algorithm" ([episode](../sources/turing-award-winner-on-working-with.md)). [James Cowling](../entities/james-cowling.md) carried the lineage into industry: his MIT PhD in Liskov's group produced Viewstamped Replication Revisited (used by companies like TigerBeetle) and Granola, cited by Google's Spanner paper ([episode](../sources/dropboxs-former-most-senior-eng-building.md)).

**Disagreement — what does "understandable" mean?** [Brendan Burns](../entities/brendan-burns.md) delegated Kubernetes' consensus "pretty exclusively" to etcd because Raft is "provably correct consensus that's way easier to implement" than Paxos ([episode](../sources/the-creator-of-kubernetes-on-building.md)). Lamport rejects the entire premise of Raft's understandability pitch: he told the Raft authors "send it back to me when you have a proof," and notes the version students found "more understandable" contained a later-discovered bug — "for me, understanding means you can write a proof of it. What understanding means for most people is a warm fuzzy feeling" ([episode](../sources/turing-award-winner-on-working-with.md)). The practitioners in the series mostly side with Burns by their actions, but nobody rebuts Lamport's point that the warm feeling and correctness are different things.

**Disagreement — how do you actually learn this field?** Lamport's answer is mathematics: understand programs via invariants (proofs grow ~quadratically with process count, behavioral reasoning blows up exponentially), and "if you're thinking without writing, you only think you're thinking" ([episode](../sources/turing-award-winner-on-working-with.md)). [Marc Brooker](../entities/marc-brooker.md)'s answer is operations: "the majority of my in-practice knowledge about how to build distributed systems has come from being on call" and from reading 3,000–4,000 postmortems ([episode](../sources/aws-distinguished-eng-learnings-from.md)). Cowling's is the PhD — the formative experience of facing a problem nobody can answer ([episode](../sources/dropboxs-former-most-senior-eng-building.md)). These are less contradictory than complementary, but each guest is emphatic that his or her channel is the load-bearing one.

### Consistency and coordination

[Mike Stonebraker](../entities/mike-stonebraker.md) recounts publicly rejecting eventual consistency because it breaks integrity constraints (stock can't go below −1) and says Google "completely abandoned" it with Spanner's conventional transactions — one of two public fights with Google he claims to have won ([episode](../sources/turing-award-winner-postgres-disagreeing.md)). Liskov's Argus had already imported atomic transactions from [databases](databases.md) into distributed computing in the 1980s so computations complete entirely or not at all ([episode](../sources/turing-award-winner-data-abstraction.md)). Cowling's performance version of the same instinct: what matters at scale is not raw hardware speed but eliminating points of coordination ([episode](../sources/dropboxs-former-most-senior-eng-building.md)).

### Designing for failure, not for the demo

- Brooker's most technical warning: caches create modality — a fast full-cache mode and a cold-cache mode where the un-scaled backend collapses — a metastable failure that is stable in the down state, an underlying cause "in probably a majority" of the industry's biggest outages. Prefer materialized views, local copies of slow-moving data, or a backend that scales ([episode](../sources/aws-distinguished-eng-learnings-from.md)).
- Burns says the hardest Kubernetes decision was making it ~15 loosely coupled processes: great resiliency, painful debugging. His stability rule — every component reads state only through the API server, so "everybody gets to restart all the time and they just come up and they work." Also: "every time you increase by an order of magnitude... the problem moves somewhere else" (etcd, the storage layer, became the bottleneck at AI-training scale) ([episode](../sources/the-creator-of-kubernetes-on-building.md)).
- Cowling: "It's not about getting a system to work. It's what do you do when it doesn't work." Magic Pocket hit ~24 nines of modeled durability with erasure coding spread across racks, power feeds, drive manufacturers and regions, and Go-runtime OOMs that looked like disk failures could 7x load into congestion collapse — the reason storage nodes were rewritten in Rust ([episode](../sources/dropboxs-former-most-senior-eng-building.md)).

### Build vs. buy, and who should do this at all

Cowling led the largest data migration in history off [AWS](../entities/aws.md) S3 — justified by strategic control, pre-IPO cost, and a workload understanding S3 couldn't match — yet tells almost everyone else not to build their own infrastructure: "most people should focus on their applications" ([episode](../sources/dropboxs-former-most-senior-eng-building.md)). [Joakim Recht](../entities/joakim-recht.md)'s Odin shows the payoff when a platform team does centralize it: ~120,000 physical servers and ~500,000 databases at Uber operated by ~20 people, replacing per-technology toolchains across ~52 database technologies ([episode](../sources/uber-distinguished-eng-on-unfair.md)). And [Vlad Feinberg](../entities/vlad-feinberg.md) confirms the field's continuity into the AI era: much of frontier-lab work is "classical backend/distributed-systems engineering at extreme scale" — DeepMind's distillation infrastructure went through 3–4 generational rewrites, each starting with "a good old-fashioned design doc" ([episode](../sources/google-deepmind-pre-training-lead.md)).

## Practical takeaways

- Learn the consensus canon once, properly — Paxos, Raft, and Viewstamped Replication are one idea; knowing that saves you from treating them as three ([Liskov](../sources/turing-award-winner-data-abstraction.md), [Cowling](../sources/dropboxs-former-most-senior-eng-building.md)).
- Don't build your own consensus; delegate to a proven store (etcd) and route all state access through one API layer so everything is restartable ([Burns](../sources/the-creator-of-kubernetes-on-building.md)).
- Treat caches as a last resort: they add a failure mode that is stable in the down state ([Brooker](../sources/aws-distinguished-eng-learnings-from.md)).
- Design for the failure case first; at scale, eliminate coordination points rather than chasing raw speed ([Cowling](../sources/dropboxs-former-most-senior-eng-building.md)).
- Get on call, and read postmortems like literature — it's where distributed-systems judgment actually comes from ([Brooker](../sources/aws-distinguished-eng-learnings-from.md)).
- Write proofs, or at least invariants, for the synchronization kernel of your system — keep the algorithm separate from the code ([Lamport](../sources/turing-award-winner-on-working-with.md)).
- Distributed-systems skills transfer directly to AI infrastructure — frontier labs are hiring for exactly this ([Feinberg](../sources/google-deepmind-pre-training-lead.md)).

## Related

- [systems-design](systems-design.md) — the broader design-judgment theme; [databases](databases.md) — transactions and consistency; [incident-management](incident-management.md) — the operational side Brooker champions.
- Key people: [Leslie Lamport](../entities/leslie-lamport.md), [Barbara Liskov](../entities/barbara-liskov.md), [James Cowling](../entities/james-cowling.md), [Marc Brooker](../entities/marc-brooker.md), [Brendan Burns](../entities/brendan-burns.md).
- Most relevant episodes: [Lamport](../sources/turing-award-winner-on-working-with.md), [Liskov](../sources/turing-award-winner-data-abstraction.md), [Brooker](../sources/aws-distinguished-eng-learnings-from.md), [Cowling](../sources/dropboxs-former-most-senior-eng-building.md), [Burns](../sources/the-creator-of-kubernetes-on-building.md).
