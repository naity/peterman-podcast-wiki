---
type: entity
entity_kind: person
updated: 2026-07-19
sources: [turing-award-winner-p-vs-np-zero.md]
---

# Avi Wigderson

Turing Award and Abel Prize winner, complexity theorist at the Institute for Advanced Study; co-inventor of zero-knowledge proof universality and the hardness-versus-randomness paradigm ([episode](../sources/turing-award-winner-p-vs-np-zero.md)).

## Career arc

Wigderson's episode is less biography than a guided tour of [complexity theory](../concepts/complexity-theory.md)'s crown jewels, most of which he helped build: the Goldreich-Micali-Wigderson result that, assuming one-way functions, anything provable has a zero-knowledge interactive proof ("we showed that it's not only not ridiculous, it's universal"), and the Nisan-Wigderson generator showing that if some sufficiently hard problem exists then P = BPP and all efficient probabilistic algorithms can be derandomized ([episode](../sources/turing-award-winner-p-vs-np-zero.md)).

## Key views & advice

- P vs NP is "whether we can know everything we want to know": NP is what we could recognize if handed a solution, P is what we can find — P = NP would mean anything checkable is findable ([episode](../sources/turing-award-winner-p-vs-np-zero.md)).
- The community's belief that P != NP rests on soft evidence (finding feels harder than checking; decades of failed attacks on thousands of NP-hard problems) and he admits one new idea could overturn it ([episode](../sources/turing-award-winner-p-vs-np-zero.md)).
- Real-world instances are usually not worst-case: protein folding is NP-hard yet bodies do it constantly, Simplex is worst-case exponential but practically linear, and structured instances are why SAT solvers work ([episode](../sources/turing-award-winner-p-vs-np-zero.md)).
- NP-complete problems are inter-reducible because computation is local — any computation encodes as a conjunction of local constraints ([episode](../sources/turing-award-winner-p-vs-np-zero.md)).
- Randomness is a resource whose quality depends on the observer's computational power: "the quality of randomness is in the eye of the beholder or in the computational power of the beholder"; pseudorandomness only needs to fool the tests applied to it, though [cryptographic](../concepts/security-and-cryptography.md) secrets need genuinely random bits ([episode](../sources/turing-award-winner-p-vs-np-zero.md)).
- On quantum: Shor's 1994 factoring algorithm triggered both quantum hardware investment and post-quantum cryptography; MIP* = RE shows entangled provers can convince efficient verifiers of uncomputable statements — "once you get weird enough, you get weird enough consequences" ([episode](../sources/turing-award-winner-p-vs-np-zero.md)).
- He highlights [Ryan Williams](ryan-williams.md)' 2025 sqrt(T)-space simulation of time-T computation as a breakthrough past a bound believed optimal for ~50 years ([episode](../sources/turing-award-winner-p-vs-np-zero.md)).

## Related

- [Episode: Turing Award Winner: P vs NP, Zero-Knowledge Proofs, Quantum Computation](../sources/turing-award-winner-p-vs-np-zero.md) — his interview
- [Ryan Williams](ryan-williams.md) — same field; gives contrarian probabilities on Wigderson's core questions
- [Martin Hellman](martin-hellman.md) — public-key cryptography rests on the one-way functions Wigderson's results assume
- [complexity-theory](../concepts/complexity-theory.md), [security-and-cryptography](../concepts/security-and-cryptography.md), [teaching-and-communication](../concepts/teaching-and-communication.md)
