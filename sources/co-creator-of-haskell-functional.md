---
type: source
updated: 2026-07-19
raw: ../raw/co-creator-of-haskell-functional.md
guest: "Simon Peyton Jones"
guest_role: "Co-creator of Haskell, GHC lead; now designing Verse at Epic Games"
date: 2026-06-08
url: https://www.developing.dev/p/co-creator-of-haskell-functional
---

# Co-Creator of Haskell: Functional Programming, Thinking in Types, Useless Languages | Simon Peyton Jones

Simon Peyton Jones co-created Haskell and has spent his research life exploring one hypothesis: that programming with values instead of mutation makes programs easier to write, maintain, and reason about. The conversation ranges from lambda calculus and the failed dream of functional-programming hardware, through monads, laziness, and type systems, to how GHC works internally, why Haskell "avoids success at all costs," and why he thinks LLMs may be the best thing to happen to statically typed languages — closing with his current work on Verse at Epic Games and why Excel is his second-favorite language.

## Key takeaways

- [Functional programming](../concepts/functional-programming.md) is "programming with values instead of mutation" — mathematics made executable. Church's lambda calculus and Turing's machine are provably equivalent in power, and Simon's career has been running with the question: what happens if you exclude side effects by default? His slogan: "when the limestone of imperative programming has worn away, the granite of functional programming will be revealed underneath."
- FP has been the mainstream's idea laboratory: garbage collection, lambdas, language-integrated query, parametric polymorphism, and static typing all grew up in functional languages before infecting imperative ones ([programming-languages](../concepts/programming-languages.md)).
- Building hardware for functional languages (Lisp machines, MIT's Monsoon dataflow machine, the SKIM machine for SK combinators) was an "inspiring mistake": those machines were interpreters in hardware, doing at runtime what a compiler does better at compile time — and you can't outrun Intel's man-years on x86. Even as Intel's CEO you'd add almost nothing to the ISA for FP.
- On safety ([security-and-cryptography](../concepts/security-and-cryptography.md)): C's unchecked mutation means the Internet's infrastructure is "a boat built out of paperclips" — writing it in Haskell/ML would remove ~99% of exploits (buffer overruns, pointer bugs) by construction, though no language prevents high-level flaws like deadlock or bad logic. Rust has moved C's quadrant "useful but unsafe" toward safe while staying useful; Haskell started safe-but-useless (v1 had no I/O — programs were just string-to-string functions) and has climbed toward useful.
- Haskell vs OCaml: siblings, not rivals. OCaml's strictness gave it a defined evaluation order and thus easy impure I/O; Haskell's laziness forced it to stay pure, which led to monads. Laziness (per John Hughes's "Why Functional Programming Matters") is modularity glue — generate an infinite chess game tree in one module, prune and explore it in a completely separate one.
- Monads make effects first-class typed values: `IO Int` computations can be named, passed, stored, and sequenced with do-notation, so purity is preserved because dirtiness is declared in the type; effect systems (e.g. Tom Ellis's Bluefin library) refine this from all-or-nothing to per-effect tracking.
- The biggest benefit of static types is maintainability and design: GHC is 35-year-old Haskell that he refactors "fearlessly" by changing a type and following the wave of type errors. Weak type systems are strictly worse than strong ones; the goal is to expand what the type system accepts (parametric polymorphism onward) and provide dynamic-typing escape hatches for the rest.
- GHC's architecture: parse → rename → typecheck → desugar into Core, a tiny System F lambda calculus (~8 constructors vs the AST's ~50 node types) that has barely changed in 35 years; then core-to-core optimization passes, then C-- portable assembly, then native/LLVM backends. Core is statically type-checkable — he claims no other production compiler has a fully type-checkable intermediate language, and it catches optimizer bugs that would otherwise surface as distant segfaults.
- "Avoid success at all costs" is a deliberate pun: don't chase success by compromising the core principle (no unrestricted side effects), and avoid so much success that you can't change anything — though today he spends weeks on backward compatibility GHC never used to promise ([open-source](../concepts/open-source.md)).
- On the [AI era](../concepts/ai-era-engineering.md): LLMs "may be the best thing that's happened to statically typed languages" because the compiler prunes the LLM's generation space in a tight iteration loop. But copilots need pilots — he won't merge AI-generated code into GHC unreviewed, everyone should still learn programming, and every child should know "it's all just bits": ChatGPT is a trillion floats and floating-point arithmetic ([teaching-and-communication](../concepts/teaching-and-communication.md)).
- His day job at Epic Games is Verse, a functional logic language "way out" beyond even functional languages in the design space — the same kind of weird-but-worth-exploring bet FP was in 1980, now with a games company's muscle behind it. And Excel is the world's most widely used programming language by three orders of magnitude; after 20 years he got LAMBDA added, making its pure formula language Turing complete.

## Notable quotes

- "When the limestone of imperative programming has worn away, the granite of functional programming will be revealed underneath." — Simon Peyton Jones, ~06:00
- "It's like we've built a boat out of paperclips and we're surprised that it's leaky... we wrote our computational infrastructure for the world in an insecure language." — Simon Peyton Jones, ~21:47
- "I think it may be the best thing that's happened to statically typed languages for a long time... with a static type system, you cut down the space of programs that the LLM can generate." — Simon Peyton Jones, ~01:11:12
- "All of these people who you see very successful wandering around... are all just making it up as they go along... if you want to be lucky, you need to put yourself in positions where lucky things could happen. And that means taking some kind of risk." — Simon Peyton Jones, ~01:25:04

## Connections

- [Creator of C++: Bell Labs, Negative Overhead Abstraction, Mistakes | Bjarne Stroustrup](creator-of-c-bell-labs-negative-overhead.md) — the imperative counterpoint: another language creator, whose C++ sits at the "useful but dangerous" end of Simon's graph.
- [Turing Award Winner: TPUs vs GPUs vs CPUs, Computer Architecture, RISC vs CISC | David Patterson](turing-award-winner-tpu-vs-gpu-vs.md) — hardware-design perspective on why specialized architectures win or lose, echoing the FP-hardware/Lisp-machine lesson.
- [Turing Award Winner On Thinking Clearly, Paxos vs Raft, Working with Dijkstra | Leslie Lamport](turing-award-winner-on-working-with.md) — shared theme of mathematical thinking and formal reasoning about programs.
- [Turing Award Winner: Data Abstraction, Dijkstra, Distributed Systems | Barbara Liskov](turing-award-winner-data-abstraction.md) — type systems, abstraction, and language design from another PL pioneer (CLU's data abstraction prefigures the polymorphism discussion).
- [OpenAI Eng & Dev Tools Founder: How Software Engineering Is Changing | Charlie Marsh](openai-eng-and-dev-tools-founder.md) — contrasting practitioner's view of type checkers, compilers, and AI-generated code (Ty type checker; review burden of LLM code).
