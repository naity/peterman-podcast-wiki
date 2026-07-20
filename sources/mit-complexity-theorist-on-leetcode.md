---
type: source
updated: 2026-07-19
raw: ../raw/mit-complexity-theorist-on-leetcode.md
guest: "Ryan Williams"
guest_role: "MIT professor, complexity theorist, Gödel Prize winner"
date: 2026-06-29
url: https://www.developing.dev/p/mit-complexity-theorist-on-leetcode
---

# MIT Complexity Theorist: Why You Can Do Better Than 'Optimal' On Leetcode & SAT | Ryan Williams

[Ryan Williams](../entities/ryan-williams.md) is a [complexity-theory](../concepts/complexity-theory.md) professor at [MIT](../entities/mit.md) and Gödel Prize winner, best known recently for a shocking 2025 result that time-T computation can be simulated in about square-root-of-T space. The episode is structured as a fun conceit — asking a theorist the most popular LeetCode question (3SUM) — then descends into fine-grained complexity, SETH, SAT solvers, his contrarian probability assignments on famous open problems, the story behind the space-time breakthrough, and how he picks "can't-lose" research directions.

## Key takeaways

- The "optimal" n-squared 3SUM solution (sort + two-finger search) taught for [hiring-and-interviews](../concepts/hiring-and-interviews.md) LeetCode prep is not actually optimal: by grouping the sorted list into tiny blocks and preprocessing a fancy lookup structure (via the linear decision tree model), you can beat n squared — roughly n squared divided by polylog factors — and several algorithms of this family exist.
- Fine-grained complexity asks whether canonical textbook algorithms are optimal in exact exponent, using reductions that preserve "a little improvement here gives a little improvement there" — which can meaningfully relate an NP-complete problem to a P problem, something classical P vs NP theory cannot do.
- Example he calls "preserving magic": Subset Sum's 2^n brute force reduces via meet-in-the-middle (used in cryptanalysis) to a giant 2SUM instance, giving square-root-of-2^n time — the n log n "magic" of sorting/binary search transfers to an NP-complete problem.
- SETH (Strong Exponential Time Hypothesis) says CNF-SAT can't be solved in 1.999...^n for any string of nines; it's a "severe strengthening of P vs NP." Williams is on record not believing it — but says its truth value is "almost irrelevant" to him because assuming it's false forces him into unexplored algorithmic directions, and his failed refutation attempts kept yielding other results.
- Believing SETH is convenient for the field: SAT reduces to edit distance and pattern-matching problems, so SETH "proves" a swath of textbook algorithms optimal in one stroke.
- His famous contrarian odds: only 80% on P != NP (bumped from 75% after Scott Aaronson objected) because algorithmic surprises are constant while lower-bound surprises are rare — "my intuition for what should be is often just wrong"; 45% on NEXP != EXP because super-compressible SAT instances may be easy (the same structure hypothesis that may explain why SAT solvers work in practice); 80% on NEXP = coNEXP via a "little birdie" counting argument he thinks may be constructible within NEXP.
- His space-time breakthrough: since Hopcroft-Paul-Valiant (1975), the best known was simulating time T in space T/log T; he showed space ~sqrt(T) suffices (at exponential time cost), building on Cook and Mertz's tree evaluation trick — instead of writing only into erased memory, XOR onto existing memory so cleverly that contents can be recovered without storing them, then cut computation into sqrt(T) intervals of sqrt(T) steps.
- He didn't believe his own result: he assumed a bug for months, rewrote the proof repeatedly, sent it to two trusted colleagues asking them to "find the mistake" (one refused to read past the abstract), and submitted to STOC still unsure — then promoted the footnote that finally convinced a colleague into a "warmup" section.
- Research strategy: seek win-win hypotheses where either outcome yields progress — e.g., his orthogonal-vectors program would radically break SETH if true, and proves new circuit lower bounds if false. His Stanford-job-winning circuit lower bounds came from a failed SAT algorithm he pivoted ([regrets-and-advice](../concepts/regrets-and-advice.md): stare at failures and extract what works).
- Book recommendations: Avi Wigderson's book, Fortnow's The Golden Ticket, Mertens & Moore's The Nature of Computation, Sipser's Introduction to the Theory of Computation.
- Advice to younger self: "you don't need permission to work on very tough problems" — open problems level the playing field; and avoid inertia by regularly interrupting yourself to ask whether coasting in the current direction leads anywhere you want, since grad school has no external metric — you can only compare present self to past self.

## Notable quotes

- "The truth value of SETH to me is almost irrelevant because if I believe that it's false, then I get good ideas." — Ryan Williams, ~21:47
- "There are surprises, like all the time, in the power of algorithms. There are very few surprises in terms of lower bounds." — Ryan Williams, ~35:32
- "I was just exhausted from thinking about it for so long and just thought, maybe someone else will find the mistake for me." — Ryan Williams, ~59:23 (on submitting his space-time simulation breakthrough)
- "You don't need permission to think about these problems... this knowledge is open to the world and it's open to you." — Ryan Williams, ~01:09:15

## Connections

- [Turing Award Winner: P vs NP, Zero-Knowledge Proofs, Quantum Computation | Avi Wigderson](turing-award-winner-p-vs-np-zero.md) — same field; Williams recommends "Avi's book" by name and offers contrarian takes on the questions Wigderson discusses.
- [Turing Award Winner: NSA, Public Key Cryptography, Crypto Wars | Martin Hellman](turing-award-winner-nsa-public-key.md) — Hellman grounds cryptography in one-way functions and P vs NP; Williams notes meet-in-the-middle from cryptanalysis and that his simulation applies even to cryptographic pseudorandom processes.
- [Co-Creator of Haskell: Functional Programming, Thinking in Types, Useless Languages | Simon Peyton Jones](co-creator-of-haskell-functional.md) — academic researchers on decades-long research programs and joyful grinding.
- [Turing Award Winner On Thinking Clearly, Paxos vs Raft, Working with Dijkstra | Leslie Lamport](turing-award-winner-on-working-with.md) — shared theme of writing and rewriting as the tool for believing/verifying hard results.
