---
type: concept
updated: 2026-07-19
sources: [boris-cherny-creator-of-claude-code.md, co-creator-of-haskell-functional.md, creator-of-c-bell-labs-negative-overhead.md, harvard-professor-cs50-what-matters.md, mozilla-firefox-cto-on-browser-war.md, msl-eng-director-promo-hacking-industry.md, openai-eng-and-dev-tools-founder.md, tech-lead-for-metas-most-used-programming.md, turing-award-winner-data-abstraction.md]
---

# Programming languages

The podcast has interviewed an unusual density of language creators — CLU ([Barbara Liskov](../entities/barbara-liskov.md)), C++ ([Bjarne Stroustrup](../entities/bjarne-stroustrup.md)), Haskell ([Simon Peyton Jones](../entities/simon-peyton-jones.md)), Hack's tech lead ([Dwayne Reeves](../entities/dwayne-reeves.md)), a Julia core contributor ([John Myles White](../entities/john-myles-white.md)) — plus practitioners who bet careers on language choices (Rust at Mozilla and Astral, TypeScript at Meta).

## What the guests say

### Languages are born from problems, not from wanting a language

Stroustrup is explicit: "what do I need to build a language" is the wrong question — find a problem no existing language solves. C++ came from his failed attempt to build a distributed Unix when nothing offered both C's hardware access and Simula's classes ([episode](../sources/creator-of-c-bell-labs-negative-overhead.md)). The pattern repeats across episodes: CLU embodied Liskov's data-abstraction answer to the 1970s software crisis ([episode](../sources/turing-award-winner-data-abstraction.md)); Rust was Mozilla's answer to two structural C++ problems, memory-safety exploits and single-threaded engines on multi-core hardware ([Bobby Holley's episode](../sources/mozilla-firefox-cto-on-browser-war.md)); Hack existed to type a giant PHP codebase ([episode](../sources/tech-lead-for-metas-most-used-programming.md)); Julia was designed "to destroy MATLAB" ([episode](../sources/msl-eng-director-promo-hacking-industry.md)).

### Static typing: the podcast's rarest thing — near-consensus

Almost every guest lands on the same side, for different reasons:

- Reeves (Hack): a large codebase is an information-communication problem; types communicate intent, power tooling, and rule out whole error classes — "only solo hobbyists move faster dynamically." Typing one untyped core PHP API surfaced real bugs in ~20% of migrated call sites. His "uncanny valley of type systems": as a codebase approaches full typing, the remaining places where types lie get more off-putting, so things feel worse just before 100% ([episode](../sources/tech-lead-for-metas-most-used-programming.md)).
- Peyton Jones (Haskell): the biggest benefit is maintainability — he refactors 35-year-old GHC "fearlessly" by changing a type and following the wave of errors; weak type systems are strictly worse than strong ones, with dynamic escape hatches for the remainder ([episode](../sources/co-creator-of-haskell-functional.md)).
- Liskov: Python's flaw is modules without encapsulation ([episode](../sources/turing-award-winner-data-abstraction.md)).
- White (Julia): "what makes a language fast is invariants" — dynamic languages are slow because of what they *might* do (R's redefinable braces, Python's rewritable symbol table) ([episode](../sources/msl-eng-director-promo-hacking-industry.md)).
- Stroustrup: static typing was chosen for C++ because embedded systems can't drop into a debugger ([episode](../sources/creator-of-c-bell-labs-negative-overhead.md)); [Boris Cherny](../entities/boris-cherny.md) wrote the TypeScript book and says "thinking in types" changed how he codes more than anything else ([episode](../sources/boris-cherny-creator-of-claude-code.md)); [Charlie Marsh](../entities/charlie-marsh.md) is building the Ty type checker for Python ([episode](../sources/openai-eng-and-dev-tools-founder.md)).

The one deliberate dissent is pedagogical, not technical: [David Malan](../entities/david-malan.md) still starts CS50 with C — not for types but because it's closest to hardware, forcing students to build hash tables and linked lists before week 6 collapses it all into one line of Python ([episode](../sources/harvard-professor-cs50-what-matters.md)).

### Memory safety: the sharpest disagreement in the series

Peyton Jones says C's unchecked mutation means the Internet's infrastructure is "a boat built out of paperclips" — writing it in Haskell/ML would remove ~99% of exploits by construction ([episode](../sources/co-creator-of-haskell-functional.md)). Stroustrup's response to the memory-safety campaign: "I'm so tired of that" — over 90% of exploited C++ safety bugs come from C-style code with raw pointers, hardened libraries already exist, C++26 standardizes a hardened option, and his profiles work aims at enforceable-by-default guarantees against committee members "devoted to their old code" ([episode](../sources/creator-of-c-bell-labs-negative-overhead.md)). The practitioners have voted with their feet: Holley co-evolved Rust with Servo and shipped its parallel CSS engine as Firefox Quantum ([episode](../sources/mozilla-firefox-cto-on-browser-war.md)), and Marsh — who chose Rust "largely because of hype" and now calls it the best possible choice — "absolutely would not start a new project in C/C++ today" ([episode](../sources/openai-eng-and-dev-tools-founder.md)). Peyton Jones frames Rust as moving C's "useful but unsafe" quadrant toward safety, while Haskell climbed toward usefulness from the opposite corner ([episode](../sources/co-creator-of-haskell-functional.md)).

### Adoption is a strategy problem

Contrasting playbooks, explicitly at odds:

- Stroustrup rode compatibility and standardization: C++ reused C as its portable assembler ("we can have Dennis Ritchie's mistakes, which we know, and my mistakes, which we don't know yet — so we'll take Dennis's"), was pushed into ISO standardization by IBM/HP who couldn't depend on a corporate-owned language, and grew 10–12x on a $5,000 marketing budget while Sun spent millions on Java ([episode](../sources/creator-of-c-bell-labs-negative-overhead.md)).
- Peyton Jones ran the opposite experiment: Haskell's "avoid success at all costs" deliberately refused to compromise its core principle to chase users ([episode](../sources/co-creator-of-haskell-functional.md)).
- Liskov deliberately kept CLU a research artifact rather than productizing it — its ideas won through Ada and Java instead ([episode](../sources/turing-award-winner-data-abstraction.md)).
- Marsh argues developer marketing is underrated — you have ~10 seconds to convey why a project matters; Ruff's viral benchmark graph was "priceless" ([episode](../sources/openai-eng-and-dev-tools-founder.md)). Reeves adds the inside-a-company version: the migration became real when the "uncanny valley" metaphor became the Hack team's rallying vision ([episode](../sources/tech-lead-for-metas-most-used-programming.md)).

### Performance philosophy

Stroustrup's "negative overhead abstraction": more type information feeds the optimizer, so C++ can beat C, and 1990s-clever hand optimizations are often pessimizations on modern hardware — his first optimization step is deleting the clever code ([episode](../sources/creator-of-c-bell-labs-negative-overhead.md)). White: "any code that's slow is slow because it's doing stuff it doesn't need to do" ([episode](../sources/msl-eng-director-promo-hacking-industry.md)). Marsh cautions the language is only the floor: uv's speed comes as much from architecture (cache design, packing >90% of version objects into a single u64) as from Rust ([episode](../sources/openai-eng-and-dev-tools-founder.md)).

### Languages in the LLM era

Peyton Jones thinks LLMs "may be the best thing that's happened to statically typed languages" — the compiler prunes the model's generation space in a tight loop ([episode](../sources/co-creator-of-haskell-functional.md)). Stroustrup is the skeptic for safety-critical code: LLM output brings bugs, bloat, and an unsolvable validation burden, and he channels Dijkstra — natural language is too ambiguous to be a programming language ([episode](../sources/creator-of-c-bell-labs-negative-overhead.md)). Malan splits the difference in the classroom: no Copilot on problem sets (it would autocomplete the whole assignment from a filename), unlimited use of a deliberately less-helpful tutor ([episode](../sources/harvard-professor-cs50-what-matters.md)).

## Practical takeaways

- Pick languages the way creators design them: start from the problem, not the language ([Stroustrup](../sources/creator-of-c-bell-labs-negative-overhead.md)).
- At industry scale, choose static types; treat a large codebase as a communication problem ([Reeves](../sources/tech-lead-for-metas-most-used-programming.md), [Peyton Jones](../sources/co-creator-of-haskell-functional.md)).
- Expect a typed-migration to feel worst just before completion — plan for the uncanny valley ([Reeves](../sources/tech-lead-for-metas-most-used-programming.md)).
- For new systems code, the practitioners' default is Rust; the C++ camp's counterargument is hardened profiles plus existing code bases ([Marsh](../sources/openai-eng-and-dev-tools-founder.md), [Stroustrup](../sources/creator-of-c-bell-labs-negative-overhead.md)).
- Learn a language from another paradigm to escape monoglot thinking — even Stroustrup recommends ML/Haskell ([Stroustrup](../sources/creator-of-c-bell-labs-negative-overhead.md)).
- Speed comes from invariants and architecture; delete clever code before adding it ([White](../sources/msl-eng-director-promo-hacking-industry.md), [Marsh](../sources/openai-eng-and-dev-tools-founder.md)).
- Learn one level below the abstraction you work at — the CS50 argument for C ([Malan](../sources/harvard-professor-cs50-what-matters.md)).

## Related

- [functional-programming](functional-programming.md) — the paradigm laboratory; [systems-design](systems-design.md) — abstraction and modularity; [developer-tools](developer-tools.md) — linters, type checkers, package managers; [ai-coding-tools](ai-coding-tools.md) and [ai-era-engineering](ai-era-engineering.md) — LLMs meet type systems.
- Key people: [Bjarne Stroustrup](../entities/bjarne-stroustrup.md), [Simon Peyton Jones](../entities/simon-peyton-jones.md), [Barbara Liskov](../entities/barbara-liskov.md), [Dwayne Reeves](../entities/dwayne-reeves.md), [Charlie Marsh](../entities/charlie-marsh.md), [John Myles White](../entities/john-myles-white.md).
- Most relevant episodes: [Stroustrup](../sources/creator-of-c-bell-labs-negative-overhead.md), [Peyton Jones](../sources/co-creator-of-haskell-functional.md), [Reeves](../sources/tech-lead-for-metas-most-used-programming.md), [Liskov](../sources/turing-award-winner-data-abstraction.md).
