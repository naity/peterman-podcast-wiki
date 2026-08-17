---
type: entity
entity_kind: person
updated: 2026-08-17
sources: [creator-of-typescript-10x-faster.md]
---

# Anders Hejlsberg

Creator of TypeScript and C#, and before them Turbo Pascal and Delphi at Borland — four widely-adopted languages across four decades. He is a Technical Fellow at [Microsoft](microsoft.md) and, unusually for that altitude, still an individual contributor working on the TypeScript compiler itself.

## Career arc

The episode is a design conversation rather than a biography, and it moves between the two ends of his career ([episode](../sources/creator-of-typescript-10x-faster.md)). At Borland he built Turbo Pascal alone — compiler, editor and runtime library all written in Z80 assembly, on 8-bit machines with 64k of memory, where the team counted individual bytes to fit into ROM ("I'm 20 bytes over budget here") and would convert a long jump into a short jump to an adjacent jump to reclaim one. He learned delegation only when machines grew past what one person could hold. At [Microsoft](microsoft.md) he created C#, where he worked mostly on design while others wrote the code — a prestigious arrangement he came to find unfulfilling, drifting into what he calls being an "architecture astronaut." TypeScript put him back into a compiler, where he has stayed. The occasion for the interview is the port of the TypeScript compiler from JavaScript to Go, which he worked on directly, including its shared-memory concurrency — the hardest technical problem he names from recent years.

Not discussed in the episode: the TypeScript team's size or structure, how the Go port was kept in sync with the JavaScript codebase, TypeScript 7 release plans, or his position on the Microsoft ladder (that detail comes from [David Fowler](david-fowler.md)'s episode, which names him as sitting above level 70).

## Key views & advice

- **Self-host inside the ecosystem you want to join.** The TypeScript compiler was written in JavaScript — after early C prototypes built on an Internet Explorer parser — because that made the team daily users of their own product and let the compiler run in a browser, which native code could not do before WebAssembly. "If you can self-host in the ecosystem that you want to be a part of, that is dramatically better than targeting from outside" ([programming-languages](../concepts/programming-languages.md)).
- **The thing that forced the rewrite was cores, not speed.** JavaScript's 2–3x penalty against native was tolerable; its single-threaded model, where web workers cannot share data structures, was not. "Moore's Law has stopped giving us faster CPUs, it's giving us more CPUs" ([computer-architecture](../concepts/computer-architecture.md)).
- **Port, don't rewrite — which chose the language.** Preserving semantics and backward compatibility meant keeping a codebase that assumes garbage collection and first-class functions. Rust was tried and rejected: no GC, and a borrow checker that cannot express a compiler's pervasive circular structures (parent pointers, recursive types, symbol references). "We tried, and it just wasn't feasible."
- **For big migrations, have AI write the deterministic tool rather than do the migration.** Turning a model loose on a million lines leaves you verifying all of it against hallucination; a generated tool shrinks the validation surface to the tool ([ai-coding-tools](../concepts/ai-coding-tools.md)).
- **AI entrenches incumbent languages.** Models are best at what they saw most, teaching a niche language costs prompt tokens, and the non-AI bar for a new language — compiler, tooling, language services, debugger, profiler, frameworks, multiple targets — was already rising. He also argues LLMs will not bypass source languages for machine code: text is the most compressed form and closest to the meaning, while machine code is mostly noise irrelevant to the logic.
- **Fast tooling matters more under AI, not less.** "If type checking takes two minutes every time the LLM writes something, that's horrible" — and semantic operations agents need (renaming a property without grep's false positives) require a compiler: "the only thing that can do semantic search is a compiler," reached through LSP or a CLI ([developer-tools](../concepts/developer-tools.md)).
- **The AI-writes-90% claim is about volume, not quality.** AI already writes 100% of some application categories and the statistic is partly self-fulfilling — but "high quality code that no one has ever written before, it's not clear AI will write 90% of that." His own compiler is his example of what models write badly ([ai-era-engineering](../concepts/ai-era-engineering.md)).
- **IDEs and understanding survive because accountability does.** On IDEs going away, "good luck to you": someone has to take responsibility when an AI-built system does harm, and you cannot fix a bug or answer a breach in code you don't understand.
- **The junior-engineer question nobody answers.** "If it does, then how do we ever get senior software engineers?" He expects the pyramid to narrow at the base and the job to become more reviewing and less typing — the craft changes rather than ends.
- **Stay in the code if that is what you like.** He remains an IC by choice, having found the design-only role hollow, and argues the general rule is fit rather than trajectory — plus a practical case that architects who keep a corner of the implementation can propose refactorings that are real ([regrets-and-advice](../concepts/regrets-and-advice.md)).
- **Advice to his younger self:** learn teamwork earlier, and don't let people tell you a thing can't be done — the people who said Turbo Pascal was impossible were describing their own understanding.
- **Book:** Niklaus Wirth's *Algorithms + Data Structures = Programs*, from which he learned hash tables; replacing Turbo Pascal's linked-list symbol tables doubled the compiler's speed.

## Related

- [Episode: Creator of TypeScript: 10x Faster Typescript, Why AI Won't Replace SWEs](../sources/creator-of-typescript-10x-faster.md) — his interview
- [Bjarne Stroustrup](bjarne-stroustrup.md) — his closest analogue: mainstream-language creator, still hands-on, skeptical of AI on quality grounds, and the other guest to ask where senior engineers will come from
- [Roberto Ierusalimschy](roberto-ierusalimschy.md) — agrees AI entrenches incumbents and that verification is the human's remaining job, but is his counterparty on dynamic typing and on whether small teams beat institutional governance
- [Leonardo de Moura](leonardo-de-moura.md) — the direct opposition: de Moura says a machine-checked proof makes it not matter how code was written; Hejlsberg says accountability makes understanding non-optional
- [Simon Peyton Jones](simon-peyton-jones.md) — "copilots need pilots," and the static-types-help-LLMs bet TypeScript instantiates at industrial scale
- [Xavier Leroy](xavier-leroy.md) — "every new line of code is a liability" is the economic form of Hejlsberg's checking-cost objection
- [David Fowler](david-fowler.md) — the Microsoft-ladder episode that places Hejlsberg above level 70
- [Microsoft](microsoft.md) — C#, TypeScript, and the Turbo Pascal/Delphi lineage he brought with him
- [programming-languages](../concepts/programming-languages.md), [ai-era-engineering](../concepts/ai-era-engineering.md), [ai-coding-tools](../concepts/ai-coding-tools.md), [developer-tools](../concepts/developer-tools.md)
