---
type: source
updated: 2026-07-19
raw: ../raw/turing-award-winner-p-vs-np-zero.md
guest: "Avi Wigderson"
guest_role: "Turing Award winner and Abel Prize winner, complexity theorist at the Institute for Advanced Study"
date: 2026-06-01
url: https://www.developing.dev/p/turing-award-winner-p-vs-np-zero
---

# Turing Award Winner: P vs NP, Zero-Knowledge Proofs, Quantum Computation | Avi Wigderson

[Avi Wigderson](../entities/avi-wigderson.md) is the only person in history to have won both a Turing Award (computer science) and an Abel Prize (mathematics). In this deep technical episode he gives an accessible tour of [complexity theory](../concepts/complexity-theory.md): why P vs NP is really a question about the limits of human knowledge, how hardness and randomness turn out to be two sides of the same coin, why zero-knowledge proofs are universal rather than ridiculous, and how quantum computation is reshaping the field — including a proof system that can verify the uncomputable.

## Key takeaways

- Wigderson frames P vs NP as "whether we can know everything we want to know": NP captures all problems whose solutions we could recognize if handed to us (math proofs, scientific theories, engineering designs, solved crimes), and P captures what we can actually solve efficiently — so P = NP would mean anything checkable is findable, including a cure for cancer.
- The community's intuition that P ≠ NP rests on soft evidence: everyday experience that finding is harder than checking, and 50–70 years of thousands of practically motivated attempts at NP-hard optimization problems all failing to produce an efficient general algorithm. He admits these arguments "are not that convincing" and a new idea could upend them tomorrow.
- Real-world instances are usually not worst-case: protein folding is NP-hard in general yet bodies fold proteins constantly, the Simplex method is exponential in the worst case but effectively linear in practice, and verification/testing SAT instances have structure that clever heuristics exploit — which is why [SAT solvers](../concepts/developer-tools.md) are the workhorse for so many translated problems.
- The PCP theorem (early 90s) plus Håstad's strengthening shows even approximation is hard: for 3-variable Boolean constraints, random assignment satisfies 7/8 of them, and beating 7/8 by any epsilon is already NP-hard.
- All NP-complete problems are inter-reducible because "computation is local": any computation's evolution can be encoded as a conjunction of local constraints, which is why satisfiability (Cook, Levin) was the first complete problem and why reductions to it are usually simple.
- Ryan Williams' 2025 breakthrough showed any time-T computation can be simulated in roughly sqrt(T) space, smashing the T/log T bound of Valiant–Paul–Pippenger that stood for ~50 years; Barrington's earlier theorem (majority counting in constant space via non-commutative permutations on 5 elements) is a taste of how counterintuitive space savings can be.
- Randomness is a computational resource whose quality "is in the eye of the beholder": the Blum–Micali coin-toss thought experiment shows the same physical event has full entropy for an unaided observer and zero entropy for one with sensors and a supercomputer — pseudorandomness only has to fool the specific computational power observing it.
- The hardness-vs-randomness paradigm (including the Nisan–Wigderson generator) shows that if any sufficiently hard problem exists, then P = BPP — every efficient probabilistic algorithm can be derandomized — and conversely derandomization implies hard functions; randomness extractors can also purify weak physical sources (weather, sunspots) into near-perfect random blocks.
- Zero-knowledge proofs (Goldwasser–Micali–Rackoff; then Goldreich–Micali–Wigderson) are universal: assuming one-way functions exist, anything provable at all can be proved interactively while revealing nothing beyond its truth — via bit commitments and randomly permuted 3-colorings, then NP-completeness reductions that translate witnesses, not just instances. This underpins modern [cryptography](../concepts/security-and-cryptography.md) protocol compliance without revealing secrets.
- On quantum: Shor's 1994 factoring/discrete-log algorithms "set the world on fire" and drove both billions in hardware investment and the post-quantum cryptography program (lattice/learning-with-errors problems still resist quantum attack); the MIP* = RE result (~2020) shows entangled quantum provers can convince efficient verifiers of even uncomputable statements like the halting problem, and its techniques resolved long-standing conjectures in math and physics.

## Notable quotes

- "The question of P versus NP is whether we can solve all the problems we want to solve, whether we can know everything we want to know. This is basically about the limits of our knowledge." — Avi (02:13)
- "The quality of randomness is in the eye of the beholder or in the computational power of the beholder." — Avi (55:08)
- "We showed that it's not only not ridiculous, it's universal. Namely, anything that has a mathematical proof also has a zero-knowledge interactive proof." — Avi (01:27:17)
- "Once you get weird enough, you get weird enough consequences." — Avi (01:50:51), on how the strange MIP* = RE proof system resolved famous open problems in math and physics

## Connections

- [MIT Complexity Theorist: Why You Can Do Better Than 'Optimal' On Leetcode & SAT | Ryan Williams](mit-complexity-theorist-on-leetcode.md) — Wigderson spends several minutes explaining Ryan Williams' own 2025 time-vs-space breakthrough; same field of complexity theory.
- [Turing Award Winner: NSA, Public Key Cryptography, Crypto Wars | Martin Hellman](turing-award-winner-nsa-public-key.md) — public-key cryptography, one-way/trapdoor functions and the security assumptions Wigderson discusses trace directly to Hellman's work; both discuss the NSA and post-quantum concerns.
- [Turing Award Winner On Thinking Clearly, Paxos vs Raft, Working with Dijkstra | Leslie Lamport](turing-award-winner-on-working-with.md) — fellow Turing Award winner on the theory side of computer science and proofs.
- [Turing Award Winner: Data Abstraction, Dijkstra, Distributed Systems | Barbara Liskov](turing-award-winner-data-abstraction.md) — another Turing laureate episode in the series exploring foundational CS.
- [Turing Award Winner: TPUs vs GPUs vs CPUs, Computer Architecture, RISC vs CISC | David Patterson](turing-award-winner-tpu-vs-gpu-vs.md) — the podcast's Turing-laureate series; hardware counterpart to Wigderson's theory of what computation can do.
