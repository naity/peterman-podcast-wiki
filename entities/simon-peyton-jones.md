---
type: entity
entity_kind: person
updated: 2026-07-19
sources: [co-creator-of-haskell-functional.md]
---

# Simon Peyton Jones

Co-creator of Haskell and long-time lead of its GHC compiler, formerly of [Microsoft](microsoft.md) Research; now designing the Verse language at Epic Games ([episode](../sources/co-creator-of-haskell-functional.md)).

## Career arc

Peyton Jones describes his research life as one long experiment in [functional programming](../concepts/functional-programming.md): what happens if you exclude side effects by default? ([episode](../sources/co-creator-of-haskell-functional.md)). Haskell version 1 was "very safe but useless" (no I/O — a program was a string-to-string function) and climbed toward usefulness without abandoning purity; laziness forced it to stay pure and led to monads ([episode](../sources/co-creator-of-haskell-functional.md)). He led GHC for 35 years — parse/rename/typecheck, desugar to Core (a tiny, fully type-checkable System F with ~8 constructors, barely changed in 35 years), then core-to-core optimization ([episode](../sources/co-creator-of-haskell-functional.md)). His day job at Epic Games is Verse, a functional logic language he frames as the same weird-but-worth-it bet FP was in 1980, now with a games company's resources; he also spent 20 years pushing LAMBDA into Excel, which he calls the world's most widely used [programming language](../concepts/programming-languages.md) by three orders of magnitude ([episode](../sources/co-creator-of-haskell-functional.md)).

## Key views & advice

- FP has been the mainstream's idea laboratory: garbage collection, lambdas, LINQ-style query, parametric polymorphism, and static typing all grew up in functional languages first ([episode](../sources/co-creator-of-haskell-functional.md)).
- C's unchecked mutation made the Internet "a boat built out of paperclips": infrastructure in Haskell/ML would remove ~99% of exploits by construction; Rust keeps C's usefulness while moving far toward safety ([episode](../sources/co-creator-of-haskell-functional.md)).
- Special hardware for FP (Lisp machines, dataflow machines, SKIM) was an "inspiring mistake" — interpreters in hardware, doing at runtime what compilers do better, that could never outrun Intel's x86 investment ([episode](../sources/co-creator-of-haskell-functional.md)).
- Static types' biggest payoff is maintainability: he refactors 35-year-old GHC fearlessly by changing a type and following the wave of compile errors; dynamic typing should be an explicit escape hatch, not the default ([episode](../sources/co-creator-of-haskell-functional.md)).
- "Avoid success at all costs" parses two ways, both intended: don't win by compromising the no-side-effects core, and don't get so successful you can't change anything ([episode](../sources/co-creator-of-haskell-functional.md)).
- On [AI](../concepts/ai-era-engineering.md): LLMs "may be the best thing that's happened to statically typed languages for a long time" — the compiler prunes the generation space — but copilots need pilots, he won't merge unreviewed AI code into GHC, and every child should know "it's all just bits" ([episode](../sources/co-creator-of-haskell-functional.md)).
- [Advice](../concepts/regrets-and-advice.md): all successful people are making it up as they go along, so it's fine if you are too; "if you want to be lucky, you need to put yourself in positions where lucky things could happen. And that means taking some kind of risk" ([episode](../sources/co-creator-of-haskell-functional.md)).

## Related

- [Episode: Co-Creator of Haskell: Functional Programming, Thinking in Types, Useless Languages](../sources/co-creator-of-haskell-functional.md) — his interview
- [Bjarne Stroustrup](bjarne-stroustrup.md) — fellow language creator; C++ is the "useful but dangerous" counterpoint on his safety-vs-usefulness graph
- [Charlie Marsh](charlie-marsh.md) — builds the type checkers and tooling that operationalize these ideas for Python
- [David Patterson](david-patterson.md) — the hardware-architecture view of why specialized machines win or lose
- [functional-programming](../concepts/functional-programming.md), [programming-languages](../concepts/programming-languages.md), [teaching-and-communication](../concepts/teaching-and-communication.md)
