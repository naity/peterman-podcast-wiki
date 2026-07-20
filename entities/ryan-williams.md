---
type: entity
entity_kind: person
updated: 2026-07-19
sources: [mit-complexity-theorist-on-leetcode.md]
---

# Ryan Williams

[MIT](mit.md) professor and complexity theorist, Gödel Prize winner, known for circuit lower bounds and the 2025 breakthrough showing time-T computation can be simulated in roughly sqrt(T) space ([episode](../sources/mit-complexity-theorist-on-leetcode.md)).

## Career arc

Williams built his career on [complexity theory](../concepts/complexity-theory.md)'s hardest open problems, landing his [Stanford](stanford.md) faculty job on circuit lower bounds that came from pivoting a failed SAT algorithm ([episode](../sources/mit-complexity-theorist-on-leetcode.md)). At MIT he helped define fine-grained complexity — asking whether canonical algorithms are optimal in exact exponent, via reductions that can even relate NP-complete problems to problems in P ([episode](../sources/mit-complexity-theorist-on-leetcode.md)). His space-simulation breakthrough improved the 1975 Hopcroft-Paul-Valiant T/log T bound to ~sqrt(T) space, building on Cook-Mertz tree evaluation; he spent months assuming the result was buggy, rewrote it repeatedly, asked colleagues to find the mistake, and submitted to STOC still unsure ([episode](../sources/mit-complexity-theorist-on-leetcode.md)).

## Key views & advice

- Even "optimal" textbook solutions can fall: the n^2 3SUM algorithm can be beaten by polylog factors via block preprocessing in the linear decision tree model — relevant to anyone who treats [Leetcode](../concepts/hiring-and-interviews.md) answers as final ([episode](../sources/mit-complexity-theorist-on-leetcode.md)).
- On SETH: he's on record disbelieving it, but "the truth value of SETH to me is almost irrelevant because if I believe that it's false, then I get good ideas" — operating as if hypotheses are false forces novel algorithms ([episode](../sources/mit-complexity-theorist-on-leetcode.md)).
- Contrarian probabilities: 80% P != NP (raised from 75% after Scott Aaronson objected) because "there are surprises, like all the time, in the power of algorithms. There are very few surprises in terms of lower bounds"; 45% NEXP != EXP; 80% NEXP = coNEXP ([episode](../sources/mit-complexity-theorist-on-leetcode.md)).
- Research strategy: find win-win hypotheses where either truth value yields progress — his orthogonal vectors program breaks SETH if true and proves circuit lower bounds if false ([episode](../sources/mit-complexity-theorist-on-leetcode.md)).
- "You don't need permission to think about these problems" — hard open problems level the playing field; and schedule "interrupts" to reflect on direction, since research has no external metric beyond comparing your present self to your past self ([episode](../sources/mit-complexity-theorist-on-leetcode.md)).
- Book picks: Wigderson's book, Fortnow's The Golden Ticket, Mertens & Moore's The Nature of Computation, Sipser ([episode](../sources/mit-complexity-theorist-on-leetcode.md)).

## Related

- [Episode: MIT Complexity Theorist: Why You Can Do Better Than 'Optimal' On Leetcode & SAT](../sources/mit-complexity-theorist-on-leetcode.md) — his interview
- [Avi Wigderson](avi-wigderson.md) — same field; Wigderson explains Williams' sqrt(T) result in his own episode
- [Martin Hellman](martin-hellman.md) — cryptography rests on the hardness assumptions Williams studies
- [complexity-theory](../concepts/complexity-theory.md), [regrets-and-advice](../concepts/regrets-and-advice.md), [teaching-and-communication](../concepts/teaching-and-communication.md)
