---
type: concept
updated: 2026-07-27
sources: [creator-of-ocaml-functional-programming.md, turing-award-winner-on-working-with.md, turing-award-winner-p-vs-np-zero.md, creator-of-c-bell-labs-negative-overhead.md, co-creator-of-haskell-functional.md]
---

# Formal verification

Proving programs correct with mathematics instead of (only) testing — anchored by [Xavier Leroy](../entities/xavier-leroy.md), who spent years proving the CompCert C compiler correct, and [Leslie Lamport](../entities/leslie-lamport.md), for whom proof simply *is* understanding. Both build on [Dijkstra](../entities/edsger-dijkstra.md)'s aphorism, quoted verbatim by Leroy: "testing can only show the presence of bugs, but not their complete absence" ([episode](../sources/creator-of-ocaml-functional-programming.md)).

## What the guests say

### What it is and what it has actually achieved

Leroy gives the podcast's most concrete tour ([episode](../sources/creator-of-ocaml-functional-programming.md)): specifications range from "never crashes on well-formed inputs / all array accesses in bounds" (simple, yet beyond what type systems or testing ensure — crashing code is attackable code) up to termination, non-leakage of confidential data, and precise floating-point error bounds. Proof assistants (Lean, Coq/Rocq, Isabelle) grew out of computer-assisted mathematics, not programming: automatic theorem proving proved too hard, so they became formal languages where the machine does small steps, the human guides big ones, and the finished proof is machine-recheckable — no forgotten cases, no circular hypotheses. Landmark results: CompCert (the emitted assembly is proved faithful to the C source — a proof that would run "several thousand pages" on paper) and Australia's seL4 microkernel, 8,000 lines of "extremely technical" C, every line proved. Mechanization is also what makes verified software *evolvable*: adapt the proofs and be sure you introduced no regression. On the halting-problem objection: undecidability only forbids a universal analyzer — "you only need to be able to do it for the programs you really care about," and CompCert's own termination is among its proved properties.

### Proof as a way of thinking, not just a tool

Lamport arrives at the same place from distributed systems ([episode](../sources/turing-award-winner-on-working-with.md)): "For me, understanding means you can write a proof of it. What understanding means for most people is a warm fuzzy feeling" — the Raft version students found "more understandable" contained a later-discovered bug, and his Bakery algorithm exists because his first "obviously correct" submission came back with a bug. His method: invariants, not behaviors (behavioral reasoning explodes exponentially; invariance proofs grow ~quadratically). Leroy's structural version of the same insight: purely functional style shrinks the gap between program and mathematics, which is why CompCert was written functionally and why formal-methods people dislike assignment ([functional-programming](functional-programming.md)) ([episode](../sources/creator-of-ocaml-functional-programming.md)). [Avi Wigderson](../entities/avi-wigderson.md) supplies the theory outer frame: NP is exactly the class of statements whose proofs can be efficiently *checked*, and zero-knowledge shows anything provable can be proved while revealing nothing ([episode](../sources/turing-award-winner-p-vs-np-zero.md)).

### The soft frontier: types as verification-lite

Static type systems are the mass-market end of the same spectrum: [Simon Peyton Jones](../entities/simon-peyton-jones.md) calls GHC's typed Core the reason optimizer bugs get caught at compile time rather than as distant segfaults ([episode](../sources/co-creator-of-haskell-functional.md)), and Leroy notes array-bounds correctness is precisely where types stop and real verification begins ([episode](../sources/creator-of-ocaml-functional-programming.md)).

### Verification meets AI — the live debate

Leroy sees generative AI as both the crisis and the opportunity ([episode](../sources/creator-of-ocaml-functional-programming.md)): LLMs already produce plausible Lean proofs that machines can recheck (with caveats — models sometimes quietly weaken the statement or botch auto-formalization), and the same could work for programs: AI ships code *plus* a machine-checkable proof against a spec. But this relocates the hard problem to specification: programmers are bad at writing consistent specs, and an unsatisfiable precondition makes any function body "verified" vacuously — a false sense of confidence. His 2026 outlook: "maybe this will be the decade of formal verification of software. We've been waiting for that for 50 years." [Bjarne Stroustrup](../entities/bjarne-stroustrup.md) frames the same validation burden from the regulator's side — safety-critical industries must validate every change, which unreviewed LLM output makes unsolvable ([episode](../sources/creator-of-c-bell-labs-negative-overhead.md)). The tension with the AI-tools optimists ([ai-coding-tools](ai-coding-tools.md)) is real: where Bolin and Novati celebrate 80–90% model-written code, Leroy answers that checking, not writing, is the binding cost.

## Practical takeaways

- Treat crashing code as a security hole, not a quality nit — "never crashes" is a meaningful, checkable spec ([Leroy](../sources/creator-of-ocaml-functional-programming.md)).
- Reason with invariants, not execution traces; behaviors explode combinatorially ([Lamport](../sources/turing-award-winner-on-working-with.md)).
- Write code you must reason about in as pure/functional a style as possible — it shrinks the program-to-math gap ([Leroy](../sources/creator-of-ocaml-functional-programming.md)).
- Undecidability is not an excuse: you only need proofs for the programs you care about ([Leroy](../sources/creator-of-ocaml-functional-programming.md)).
- If you accept AI-generated code, push for machine-checkable evidence (proofs, exhaustive property checks) rather than human review of bulk output — and scrutinize the *specification*, including whether preconditions are satisfiable; test your specs like you test code ([Leroy](../sources/creator-of-ocaml-functional-programming.md)).

## Related

- [functional-programming](functional-programming.md) — the programming style closest to mathematics; [programming-languages](programming-languages.md) — type systems as lightweight verification; [complexity-theory](complexity-theory.md) — proofs, checkability, and undecidability; [distributed-systems](distributed-systems.md) — where Lamport's proofs earn their keep; [ai-coding-tools](ai-coding-tools.md) — the slop this discipline may answer.
- Key people: [Xavier Leroy](../entities/xavier-leroy.md), [Leslie Lamport](../entities/leslie-lamport.md), [Edsger Dijkstra](../entities/edsger-dijkstra.md), [Avi Wigderson](../entities/avi-wigderson.md).
- Most relevant episodes: [Leroy](../sources/creator-of-ocaml-functional-programming.md), [Lamport](../sources/turing-award-winner-on-working-with.md), [Wigderson](../sources/turing-award-winner-p-vs-np-zero.md).
