---
type: source
updated: 2026-07-19
raw: ../raw/turing-award-winner-on-working-with.md
guest: "Leslie Lamport"
guest_role: "Turing Award winner, inventor of Paxos, LaTeX, and logical clocks"
date: 2026-02-23
url: https://www.developing.dev/p/turing-award-winner-on-working-with
---

# Turing Award Winner On Thinking Clearly, Paxos vs Raft, Working with Dijkstra | Leslie Lamport

Leslie Lamport won the Turing Award for foundational work in [distributed systems](../concepts/distributed-systems.md) — logical clocks, the Bakery algorithm, Byzantine fault tolerance, and Paxos — and also created LaTeX. Ryan walks through his major papers chronologically for the stories behind them: getting a bug pointed out in his first submitted algorithm, drinking beer with [Dijkstra](../entities/edsger-dijkstra.md), writing the first digital signature scheme on a napkin for Whit Diffie, and why he thinks Raft's "understandability" is a warm fuzzy feeling rather than understanding. Notably, all of this work was done in industry (SRI, DEC SRC, later Microsoft), not academia.

## Key takeaways

- The Bakery algorithm exists because Lamport submitted a "simple" two-process mutual exclusion algorithm to CACM in 1972 and the editor mailed back the bug. Two lessons: concurrent programs are hard enough that they need correctness proofs, and spite is a fine motivator ("I'm going to solve that damn problem"). The algorithm's proof revealed a stunning property: it needs no lower-level atomicity — a reader overlapping a writer can get any value and the algorithm still works.
- His one piece of joint work with Dijkstra — simplifying the first concurrent garbage-collection algorithm by folding the free list into the regular data structure — earned him co-authorship for an idea he thought obvious. He later realized it wasn't obvious to others, and that his real gift is abstraction, not raw intelligence: "Dijkstra was smart enough to realize that" ([working-with-legends](../concepts/working-with-legends.md)).
- The "Time, Clocks" paper (his most cited) came from noticing a distributed-database design would execute operations in an order different from the order they actually happened. The happens-before definition is special relativity transposed: replace the speed of light with messages actually sent. But the paper's second idea — that any distributed system can be built as a replicated state machine — was "completely ignored" for years; readers twice insisted the paper said nothing about state machines.
- His method argument: understand programs via invariants, not behaviors. Behavioral proofs over sequences blow up exponentially; invariance proofs grow roughly quadratically with process count. "The method that works, that you can be sure will work, is the use of invariants."
- He wrote the first digital signature algorithm on a napkin in a coffee house after Whit Diffie described the open problem — impractical (~128 bits of signature per bit signed, mitigated by signing hashes), but it put signatures in his toolkit before Diffie-Hellman was published ([security-and-cryptography](../concepts/security-and-cryptography.md)). It's why his Byzantine solution needed 3n+1 processes without signatures but fewer with them.
- The "Byzantine Generals" name was deliberate marketing: he learned from Dijkstra's Dining Philosophers that a cute story makes a result famous. He first considered "Albanian generals" (his boss objected — there are Albanians in the world); Byzantines were safely extinct. The result mattered because fly-by-wire aircraft were coming (oil-crisis-era planes made aerodynamically unstable for efficiency), and engineers wrongly assumed three computers tolerate one arbitrary fault — you need four. A Boeing engineer's reaction on reading it: "Oh, shit, we need four computers."
- Paxos began as an attempted impossibility proof: he didn't believe DEC SRC's distributed storage code could be correct, tried to prove it impossible, and "at some point I stopped and said — this isn't a proof, this is an algorithm that does it." He distinguishes code from algorithms: the synchronization kernel of a system should exist as an abstract algorithm first, because code conflates concurrency-irrelevant issues.
- The Paxos paper sat unpublished for eight years partly because referees found it "okay, not terribly important" and reviewers didn't get the ancient-parliament framing; Butler Lampson was the one person who grasped its significance and proselytized state-machine replication, so Lamport felt no urgency to publish.
- On Raft: he told the authors "send it back to me when you have a proof" (or an algorithm). His sharpest critique of the "Raft is more understandable" studies: the version students found more understandable contained a later-discovered bug. "For me, understanding means you can write a proof of it. What understanding means for most people is a warm fuzzy feeling" ([teaching-and-communication](../concepts/teaching-and-communication.md)).
- LaTeX was a side project of 6–9 months (billed, statute-of-limitations permitting, to an unrelated project) built as macros for his own book, generalized so others could use them — carrying over Scribe's abstraction that ideas, not typesetting, are what the author should touch.
- "If you're thinking without writing, you only think you're thinking": writing (instruction manual before program, hierarchically structured proofs) exposes the steps you believed were obvious but never checked — that's where errors live. Mathematicians reacted to his hierarchical proof style with near-physical anger, which he attributes to fear of having to be honest about gaps.
- He never developed the hoped-for "grand theory of concurrency" (the Turing machine of concurrency) and once felt a failure for it; his mature view is that state machines described in mathematics are that foundation, that language-based approaches (Petri nets etc.) miss the point, and that "you can't beat math" — infinity and abstraction simplify rather than complicate ([regrets-and-advice](../concepts/regrets-and-advice.md)).
- Advice to his younger self, characteristically: none. "I shouldn't waste time trying to answer questions that I don't have to answer. I don't think about what I should have done."

## Notable quotes

- "For me, understanding means you can write a proof of it. But what understanding means for most people is a warm fuzzy feeling." — Leslie, ~00:50:36, on Raft vs Paxos
- "The gift that I have is not in some sense raw intelligence. It's abstraction. And it's only recently, last 10 or so years, that I realized how much better I am at that than other people." — Leslie, ~01:08:48
- "If you think you know something but don't write it down, you only think you know it... it really makes you honest." — Leslie, ~00:59:58
- "I shouldn't waste time trying to answer questions that I don't have to answer. I don't think about what I should have done." — Leslie, ~01:09:24

## Connections

- [Turing Award Winner: NSA, Public Key Cryptography, Crypto Wars | Martin Hellman](turing-award-winner-nsa-public-key.md) — Lamport wrote the first digital signature scheme for Whit Diffie, Hellman's co-author, before Diffie-Hellman was published.
- [Turing Award Winner: Data Abstraction, Dijkstra, Distributed Systems | Barbara Liskov](turing-award-winner-data-abstraction.md) — fellow Turing laureate covering Dijkstra and distributed systems, and abstraction as the core skill.
- [AWS Distinguished Eng: Learnings From 3000 Incidents And How Engineering Is Changing | Marc Brooker](aws-distinguished-eng-learnings-from.md) — Paxos-style consensus and state-machine replication as practiced at industrial scale.
- [Turing Award Winner: P vs NP, Zero-Knowledge Proofs, Quantum Computation | Avi Wigderson](turing-award-winner-p-vs-np-zero.md) — theory-side Turing laureate; contrasting view of what computation's foundational abstractions are.
- [Dropbox's Former Most Senior Eng: Building Great Systems and Advice for the AI Era | James Cowling](dropboxs-former-most-senior-eng-building.md) — building correct large-scale systems; the practitioner's descendant of Lamport's methods.
