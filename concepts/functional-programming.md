---
type: concept
updated: 2026-07-19
sources: [co-creator-of-haskell-functional.md, boris-cherny-creator-of-claude-code.md, creator-of-c-bell-labs-negative-overhead.md]
---

# Functional programming

Programming with values instead of mutation — covered definitively by Haskell co-creator [Simon Peyton Jones](../entities/simon-peyton-jones.md) and echoed from industry by [Boris Cherny](../entities/boris-cherny.md), who credits type-driven functional thinking with reshaping how he codes.

## What the guests say

### The research program: what happens if you exclude side effects?

Peyton Jones defines FP as "programming with values instead of mutation" — mathematics made executable — and his whole career as running one hypothesis: exclude side effects by default and see what you learn. His slogan: "when the limestone of imperative programming has worn away, the granite of functional programming will be revealed underneath" ([episode](../sources/co-creator-of-haskell-functional.md)). Concretely from the episode:

- FP is the mainstream's idea laboratory: garbage collection, lambdas, language-integrated query, parametric polymorphism, and static typing all grew up in functional languages before infecting imperative ones.
- Laziness was not a gimmick but a forcing function: because Haskell was lazy it *had* to stay pure, which led to monads — effects as first-class typed values (`IO Int` can be named, passed, stored), so "purity is preserved because dirtiness is declared in the type." Laziness is also modularity glue (per John Hughes): generate an infinite game tree in one module, prune it in another.
- Haskell v1 was "safe but useless" (no I/O — programs were string-to-string functions) and climbed toward useful; OCaml is the sibling that chose strictness and easy impure I/O. Rust attacks the same safety problem from the useful-but-unsafe corner ([programming-languages](programming-languages.md)).
- GHC itself is the strongest maintainability testimonial: 35-year-old Haskell he refactors "fearlessly," with a typed intermediate language (Core, a tiny System F of ~8 constructors) that catches optimizer bugs no other production compiler could.
- The FP-hardware dream (Lisp machines, SKIM, dataflow) was an "inspiring mistake" — see [computer-architecture](computer-architecture.md).

### The practitioner's endorsement

Cherny — creator of Claude Code, formerly Meta/Instagram IC8 — recommends exactly one technical book to everyone: *Functional Programming in Scala*. "Thinking in types" changed how he codes more than anything else, and he came to terse, expressive languages partly out of necessity after a motorcycle accident broke both arms and every keystroke counted ([episode](../sources/boris-cherny-creator-of-claude-code.md)). Notably he applied the mindset in thoroughly imperative ecosystems (TypeScript at Meta, where he wrote the book and ran SF's biggest TypeScript meetup) — supporting Peyton Jones's limestone/granite claim that FP's value arrives even where the language isn't functional.

### Where FP is heading

Two of Peyton Jones's forward bets ([episode](../sources/co-creator-of-haskell-functional.md)): LLMs "may be the best thing that's happened to statically typed languages," since the compiler prunes the model's generation space — pure, typed code is unusually machine-checkable; and the frontier moves outward — his day job is Verse at Epic Games, a functional *logic* language "way out" beyond FP in the design space, the same kind of weird-but-worth-exploring bet FP was in 1980. Meanwhile the most-used functional language is a spreadsheet: Excel's pure formula language outnumbers everything else by three orders of magnitude, and his LAMBDA addition made it Turing complete.

No real disagreement exists between the two guests on FP itself; the live tension is with the wider [programming-languages](programming-languages.md) debate — [Bjarne Stroustrup](../entities/bjarne-stroustrup.md) recommends learning ML/Haskell to escape monoglot thinking while building the archetypal imperative language ([episode](../sources/creator-of-c-bell-labs-negative-overhead.md)).

## Practical takeaways

- Read *Functional Programming in Scala* (Cherny's single book recommendation); the payoff is "thinking in types," not switching languages ([Cherny](../sources/boris-cherny-creator-of-claude-code.md)).
- Treat effects as values: declare dirtiness in the type rather than hiding it — usable in any language with a decent type system ([Peyton Jones](../sources/co-creator-of-haskell-functional.md)).
- Use types as the refactoring engine: change the type, follow the wave of errors ([Peyton Jones](../sources/co-creator-of-haskell-functional.md)).
- Expect FP ideas to keep arriving in your mainstream language; learning them at the source is cheaper than re-learning them piecemeal ([Peyton Jones](../sources/co-creator-of-haskell-functional.md)).
- In the LLM era, purity and static types make generated code easier to constrain and verify ([Peyton Jones](../sources/co-creator-of-haskell-functional.md)).

## Related

- [programming-languages](programming-languages.md) — the broader typing and safety debates; [ai-coding-tools](ai-coding-tools.md) — LLMs plus type systems.
- Key people: [Simon Peyton Jones](../entities/simon-peyton-jones.md), [Boris Cherny](../entities/boris-cherny.md).
- Most relevant episode: [Peyton Jones](../sources/co-creator-of-haskell-functional.md).
