---
type: concept
updated: 2026-07-19
sources: [turing-award-winner-p-vs-np-zero.md, mit-complexity-theorist-on-leetcode.md, turing-award-winner-nsa-public-key.md]
---

# Complexity theory

The limits of computation — P vs NP, hardness, randomness, and proofs — via Turing/Abel laureate [Avi Wigderson](../entities/avi-wigderson.md), Gödel Prize winner [Ryan Williams](../entities/ryan-williams.md), and [Martin Hellman](../entities/martin-hellman.md), whose cryptography rests on the field's assumptions.

## What the guests say

### What P vs NP is really asking — and how sure should we be?

Wigderson frames P vs NP as "whether we can know everything we want to know": NP captures everything whose solution we could recognize if handed to us (proofs, theories, designs, solved crimes); P = NP would mean anything checkable is findable. He is candid that the evidence for P ≠ NP is soft — everyday intuition plus decades of failed attempts — and that these arguments "are not that convincing" ([episode](../sources/turing-award-winner-p-vs-np-zero.md)).

**Disagreement — the odds.** Williams goes further than the field's near-certainty and puts only 80% on P ≠ NP (bumped from 75% after Scott Aaronson objected), reasoning that "there are surprises, like all the time, in the power of algorithms. There are very few surprises in terms of lower bounds." He also holds contrarian 45% odds on NEXP ≠ EXP and 80% on NEXP = coNEXP ([episode](../sources/mit-complexity-theorist-on-leetcode.md)). Wigderson's stated position is more conventional, though his own caveat about weak evidence partially concedes Williams's point. Williams applies the same skepticism to SETH — he is on record not believing it, while noting the field finds believing it convenient because SETH "proves" a swath of textbook algorithms optimal in one stroke; to him a hypothesis's truth value is "almost irrelevant" if assuming it false generates good research directions.

### "Optimal" algorithms usually aren't

Williams's signature move, staged around the most popular LeetCode question: the "optimal" n² 3SUM solution can be beaten (roughly n²/polylog) via block decomposition and decision-tree preprocessing. Fine-grained complexity asks whether canonical algorithms are optimal in exact exponent, with reductions that transfer "a little improvement here to a little improvement there" — even relating NP-complete problems to problems in P, as when Subset Sum's 2ⁿ brute force reduces via meet-in-the-middle to a giant 2SUM, importing sorting's n log n "magic" into an NP-complete problem ([episode](../sources/mit-complexity-theorist-on-leetcode.md)). Wigderson's complementary theme: worst-case hardness says little about practice — protein folding is NP-hard yet bodies do it constantly, Simplex is exponential in the worst case but effectively linear in practice, and structured SAT instances are why SAT solvers work ([episode](../sources/turing-award-winner-p-vs-np-zero.md)). Though he also notes the PCP-theorem limit: for 3-variable constraints, beating the trivial 7/8 approximation by any epsilon is already NP-hard.

### The 2025 space-time breakthrough, from both sides

The series captures a rare double view of the same result. Williams tells the inside story of showing time-T computation simulable in ~√T space (versus the T/log T bound standing since 1975): building on Cook–Mertz tree evaluation (XOR onto existing memory so contents can be recovered without storing them), assuming for months his proof had a bug, sending it to colleagues asking them to "find the mistake," and submitting to STOC still unsure ([episode](../sources/mit-complexity-theorist-on-leetcode.md)). Wigderson independently narrates the result's significance, calling it a smashing of a ~50-year-old bound and citing Barrington's theorem as precedent for how counterintuitive space savings can be ([episode](../sources/turing-award-winner-p-vs-np-zero.md)).

### Hardness as a resource: randomness and cryptography

Wigderson's hardness-vs-randomness paradigm: if any sufficiently hard problem exists, P = BPP — every efficient probabilistic algorithm can be derandomized — and pseudorandomness only has to fool the computational power observing it ("the quality of randomness is in the eye of the beholder"). Zero-knowledge proofs are universal: assuming one-way functions, anything provable has a proof that reveals nothing beyond its truth ([episode](../sources/turing-award-winner-p-vs-np-zero.md)). Hellman grounds the same dependence historically: public-key cryptography works only because commutative one-way functions (modular exponentiation) appear hard — complexity theory is the load-bearing wall under [security-and-cryptography](security-and-cryptography.md) ([episode](../sources/turing-award-winner-nsa-public-key.md)). Williams notes the cross-pollination runs both directions: meet-in-the-middle came from cryptanalysis ([episode](../sources/mit-complexity-theorist-on-leetcode.md)). On quantum, Wigderson marks Shor's 1994 algorithm as the moment that "set the world on fire" — driving both hardware billions and post-quantum lattice cryptography — and MIP* = RE as proof that entangled provers can verify even uncomputable statements ([episode](../sources/turing-award-winner-p-vs-np-zero.md)).

### How theorists actually work

Williams's research strategy: seek win-win hypotheses where either outcome yields progress (his orthogonal-vectors program breaks SETH if true, proves circuit lower bounds if false), stare at failures and extract what works, and remember "you don't need permission to work on very tough problems" ([episode](../sources/mit-complexity-theorist-on-leetcode.md)). Hellman's version: all his colleagues told him he was crazy to take on a multibillion-dollar NSA, and "the best ideas often seem crazy ahead of time" ([episode](../sources/turing-award-winner-nsa-public-key.md)).

## Practical takeaways

- Don't treat textbook "optimal" as final — even LeetCode chestnuts have been beaten; exponent-level improvements are an open frontier ([Williams](../sources/mit-complexity-theorist-on-leetcode.md)).
- Worst-case hardness rarely blocks practice: reach for SAT solvers and heuristics on structured real-world instances ([Wigderson](../sources/turing-award-winner-p-vs-np-zero.md)).
- Frame research bets as win-win hypotheses so any outcome is progress ([Williams](../sources/mit-complexity-theorist-on-leetcode.md)).
- Hold calibrated, not tribal, beliefs about open problems — algorithms deliver surprises constantly, lower bounds almost never ([Williams](../sources/mit-complexity-theorist-on-leetcode.md)).
- Remember what's downstream: modern cryptography and derandomization both rent their foundations from unproven hardness assumptions ([Hellman](../sources/turing-award-winner-nsa-public-key.md), [Wigderson](../sources/turing-award-winner-p-vs-np-zero.md)).

## Related

- [security-and-cryptography](security-and-cryptography.md) — cryptography as applied hardness; [hiring-and-interviews](hiring-and-interviews.md) — the LeetCode frame Williams subverts; [teaching-and-communication](teaching-and-communication.md) — Wigderson's accessible framings.
- Key people: [Avi Wigderson](../entities/avi-wigderson.md), [Ryan Williams](../entities/ryan-williams.md), [Martin Hellman](../entities/martin-hellman.md).
- Most relevant episodes: [Wigderson](../sources/turing-award-winner-p-vs-np-zero.md), [Williams](../sources/mit-complexity-theorist-on-leetcode.md).
