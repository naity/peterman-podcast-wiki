---
type: concept
updated: 2026-07-27
sources: [co-creator-of-haskell-functional.md, boris-cherny-creator-of-claude-code.md, creator-of-c-bell-labs-negative-overhead.md, creator-of-ocaml-functional-programming.md]
---

# Functional programming

Programming with values instead of mutation — covered definitively by the creators of both major ML-family survivors, Haskell's [Simon Peyton Jones](../entities/simon-peyton-jones.md) and OCaml's [Xavier Leroy](../entities/xavier-leroy.md), and echoed from industry by [Boris Cherny](../entities/boris-cherny.md), who credits type-driven functional thinking with reshaping how he codes.

## What the guests say

### The research program: what happens if you exclude side effects?

Peyton Jones defines FP as "programming with values instead of mutation" — mathematics made executable — and his whole career as running one hypothesis: exclude side effects by default and see what you learn. His slogan: "when the limestone of imperative programming has worn away, the granite of functional programming will be revealed underneath" ([episode](../sources/co-creator-of-haskell-functional.md)). Concretely from the episode:

- FP is the mainstream's idea laboratory: garbage collection, lambdas, language-integrated query, parametric polymorphism, and static typing all grew up in functional languages before infecting imperative ones.
- Laziness was not a gimmick but a forcing function: because Haskell was lazy it *had* to stay pure, which led to monads — effects as first-class typed values (`IO Int` can be named, passed, stored), so "purity is preserved because dirtiness is declared in the type." Laziness is also modularity glue (per John Hughes): generate an infinite game tree in one module, prune it in another.
- Haskell v1 was "safe but useless" (no I/O — programs were string-to-string functions) and climbed toward useful; OCaml is the sibling that chose strictness and easy impure I/O. Rust attacks the same safety problem from the useful-but-unsafe corner ([programming-languages](programming-languages.md)).
- GHC itself is the strongest maintainability testimonial: 35-year-old Haskell he refactors "fearlessly," with a typed intermediate language (Core, a tiny System F of ~8 constructors) that catches optimizer bugs no other production compiler could.
- The FP-hardware dream (Lisp machines, SKIM, dataflow) was an "inspiring mistake" — see [computer-architecture](computer-architecture.md).

### The OCaml side: functional programming as systems programming

Leroy completes the sibling story Peyton Jones sketched — OCaml chose strictness, easy impure I/O, and a "very predictable cost model," making it "a fairly decent systems programming language": Cornell's Ensemble protocol stack matched C performance by running GC while packets were in flight, MirageOS built unikernels on it, and Ensemble alumnus Yaron Minsky made it Jane Street's trading-infrastructure language, where financial engineers can read the code ([episode](../sources/creator-of-ocaml-functional-programming.md)). Against the "brilliant language" framing of Rob Pike's Googlers quote, Leroy argues FP is not fundamentally harder given a little math background — the quote describes Google's hire-fresh-and-train model, Jane Street inverts it by using OCaml as a hiring filter, and "Python is 50% functional language... people are already halfway through functional programming when they are comfortable with Python" ([episode](../sources/creator-of-ocaml-functional-programming.md)). He also gives FP's deepest practical payoff: purely functional style shrinks the gap between program and mathematics, which is why CompCert was written functionally so it could be *proved* correct ([formal-verification](formal-verification.md)). His caveat on concurrency: he always preferred Erlang-style message passing over shared memory ("breaking into your neighbor's house and moving the furniture") but never landed a design that beat the copying-cost objection, and multicore OCaml (2022) ultimately shipped shared memory with a hard-won memory model ([episode](../sources/creator-of-ocaml-functional-programming.md)).

### The practitioner's endorsement

Cherny — creator of Claude Code, formerly Meta/Instagram IC8 — recommends exactly one technical book to everyone: *Functional Programming in Scala*. "Thinking in types" changed how he codes more than anything else, and he came to terse, expressive languages partly out of necessity after a motorcycle accident broke both arms and every keystroke counted ([episode](../sources/boris-cherny-creator-of-claude-code.md)). Notably he applied the mindset in thoroughly imperative ecosystems (TypeScript at Meta, where he wrote the book and ran SF's biggest TypeScript meetup) — supporting Peyton Jones's limestone/granite claim that FP's value arrives even where the language isn't functional.

### Where FP is heading

Two of Peyton Jones's forward bets ([episode](../sources/co-creator-of-haskell-functional.md)): LLMs "may be the best thing that's happened to statically typed languages," since the compiler prunes the model's generation space — pure, typed code is unusually machine-checkable (Leroy independently reports the confirming evidence: LLMs write OCaml about as well as popular languages despite less training data, and types measurably help — [episode](../sources/creator-of-ocaml-functional-programming.md)); and the frontier moves outward — his day job is Verse at Epic Games, a functional *logic* language "way out" beyond FP in the design space, the same kind of weird-but-worth-exploring bet FP was in 1980. Meanwhile the most-used functional language is a spreadsheet: Excel's pure formula language outnumbers everything else by three orders of magnitude, and his LAMBDA addition made it Turing complete.

No real disagreement exists among the FP guests on FP itself; the live tension is with the wider [programming-languages](programming-languages.md) debate — [Bjarne Stroustrup](../entities/bjarne-stroustrup.md) recommends learning ML/Haskell to escape monoglot thinking while building the archetypal imperative language ([episode](../sources/creator-of-c-bell-labs-negative-overhead.md)).

## Practical takeaways

- Read *Functional Programming in Scala* (Cherny's single book recommendation); the payoff is "thinking in types," not switching languages ([Cherny](../sources/boris-cherny-creator-of-claude-code.md)).
- Treat effects as values: declare dirtiness in the type rather than hiding it — usable in any language with a decent type system ([Peyton Jones](../sources/co-creator-of-haskell-functional.md)).
- Use types as the refactoring engine: change the type, follow the wave of errors ([Peyton Jones](../sources/co-creator-of-haskell-functional.md)).
- Expect FP ideas to keep arriving in your mainstream language; learning them at the source is cheaper than re-learning them piecemeal ([Peyton Jones](../sources/co-creator-of-haskell-functional.md)).
- In the LLM era, purity and static types make generated code easier to constrain and verify ([Peyton Jones](../sources/co-creator-of-haskell-functional.md), [Leroy](../sources/creator-of-ocaml-functional-programming.md)).
- Write code you must reason hard about (compilers, protocols) in a pure functional style — it is the style closest to mathematics ([Leroy](../sources/creator-of-ocaml-functional-programming.md)).
- Don't treat FP as an elite skill: anyone comfortable with Python comprehensions is halfway there ([Leroy](../sources/creator-of-ocaml-functional-programming.md)).

## Related

- [programming-languages](programming-languages.md) — the broader typing and safety debates; [formal-verification](formal-verification.md) — where purity pays off in proofs; [ai-coding-tools](ai-coding-tools.md) — LLMs plus type systems.
- Key people: [Simon Peyton Jones](../entities/simon-peyton-jones.md), [Xavier Leroy](../entities/xavier-leroy.md), [Boris Cherny](../entities/boris-cherny.md).
- Most relevant episodes: [Peyton Jones](../sources/co-creator-of-haskell-functional.md), [Leroy](../sources/creator-of-ocaml-functional-programming.md).
