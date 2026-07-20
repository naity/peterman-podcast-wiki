---
type: entity
entity_kind: person
updated: 2026-07-19
sources: [turing-award-winner-on-working-with.md]
---

# Leslie Lamport

Turing Award winner; inventor of Paxos, logical clocks, the Bakery algorithm, the Byzantine Generals framing, and LaTeX. Spent his whole career in industry (SRI, DEC) rather than academia ([episode](../sources/turing-award-winner-on-working-with.md)).

## Career arc

The Bakery algorithm was born of spite: his first submitted mutual-exclusion algorithm came back from the CACM editor with a bug, teaching him that concurrent programs need correctness proofs — the resulting algorithm requires no lower-level atomicity at all. His one collaboration with Dijkstra (simplifying concurrent garbage collection) earned unexpected co-authorship; Dijkstra later credited Lamport's remarkable ability at abstraction, which Lamport himself — not raw intelligence — credits for his Turing Award. His most-cited paper, "Time, Clocks," transposed special relativity to [distributed systems](../concepts/distributed-systems.md); its second, more important idea — replicated state machines — was ignored for years. Paxos began as an attempted impossibility proof of DEC SRC's storage code that inverted mid-proof into the algorithm itself; the paper sat 8 years unpublished because referees called it "not terribly important" — only Butler Lampson grasped it. He built LaTeX in 6-9 months of "spare time" as macros for his own book ([episode](../sources/turing-award-winner-on-working-with.md)).

## Key views & advice

- On understanding: "For me, understanding means you can write a proof of it. But what understanding means for most people is a warm fuzzy feeling." He told the Raft authors "send it back to me when you have a proof" — and the version user studies found "more understandable" than Paxos contained a later-discovered bug ([episode](../sources/turing-award-winner-on-working-with.md)).
- Reason about concurrent systems via invariants, not behaviors: behaviors explode exponentially while invariance proofs grow roughly quadratically — invariants are "the method that works, that you can be sure will work" ([episode](../sources/turing-award-winner-on-working-with.md)).
- On [writing and thinking](../concepts/teaching-and-communication.md): "If you're thinking without writing, you only think you're thinking." Writing instruction manuals before programs and hierarchically structured proofs exposes the "obvious" steps where errors hide; mathematicians' angry reaction to his proof style he attributes to fear of being made honest ([episode](../sources/turing-award-winner-on-working-with.md)).
- The Byzantine Generals story was deliberate marketing, invented after watching Dijkstra's Dining Philosophers become famous for its cute story (he almost used "Albanian generals"); it mattered because fly-by-wire engineers wrongly assumed 3 computers tolerate one arbitrary fault — a Boeing engineer's reaction was "Oh, shit, we need four computers." He also wrote the first digital signature algorithm on a napkin for Whit Diffie before Diffie-Hellman was published ([episode](../sources/turing-award-winner-on-working-with.md)).
- No advice for his younger self, on principle: "I shouldn't waste time trying to answer questions that I don't have to answer. I don't think about what I should have done" ([episode](../sources/turing-award-winner-on-working-with.md)).

## Related

- [Episode: Turing Award Winner On Thinking Clearly, Paxos vs Raft, Working with Dijkstra](../sources/turing-award-winner-on-working-with.md) — his interview
- [Barbara Liskov](barbara-liskov.md) — invented the same consensus protocol independently (Viewstamped Replication); fellow Dijkstra colleague
- [Marc Brooker](marc-brooker.md) — cites Lamport on writing and formal thinking; industrializes Paxos-style consensus
- [Brendan Burns](brendan-burns.md) — Kubernetes delegates leader election to Raft-based etcd
- [working with legends](../concepts/working-with-legends.md), [security and cryptography](../concepts/security-and-cryptography.md)
