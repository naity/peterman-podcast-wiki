---
type: entity
entity_kind: person
updated: 2026-08-03
sources: [creator-of-lua-scripting-programming.md]
---

# Roberto Ierusalimschy

Creator and lead designer of Lua, the small embeddable scripting language that ended up inside World of Warcraft, Roblox, Redis, nginx and a large amount of unglamorous industrial software; professor of computer science at PUC-Rio.

## Career arc

The interview is a design-philosophy conversation rather than a biography, and Lua's institutional origins are not discussed in it ([episode](../sources/creator-of-lua-scripting-programming.md)). What he does describe is the constraint that shaped the language from the first line: Lua was written as an embeddable C library, with the standalone `lua` binary as nothing more than a client of that library. Everything distinctive follows from it — independent Lua states with no shared global state so a host process can run many at once, and `load()` rather than `eval()` so compilation and execution stay separable.

## Key views & advice

- **Embedding vs extending.** Most scripting languages handle one direction well — either the host calls into the language or the language calls out to native code. Lua was designed for both, which is why cross-language work is where he is most precise: registered C function pointers in one direction, bytecode arrays handed back to the interpreter in the other, nesting arbitrarily ([episode](../sources/creator-of-lua-scripting-programming.md), [systems-design](../concepts/systems-design.md)).
- **Minimalism as a security property, not just taste.** A Lua state can only reach the C functions the host explicitly registered, so the host defines the entire attack surface — a sandbox by construction. His example is a financial firm that embedded Lua inside Python so users could script against a whitelist without touching program state.
- **Committees cannot hold a design together.** "A camel is a horse designed by a committee," and the mechanism is an incentive asymmetry: people fight far harder to add a feature than anyone fights to keep one out. His default is refusal — "when in doubt, the rule is always don't put it... we can always add that later" ([programming-languages](../concepts/programming-languages.md)). This puts him in direct conflict with [Bjarne Stroustrup](bjarne-stroustrup.md), who credits ISO standardization with saving C++.
- **The unpopular defaults, defended.** Lua shipped without booleans (C's 0/non-zero convention) until tables needed to distinguish an absent key from a false value; "true is almost useless." And on 1-based indexing: "only in programming language there is this idea of zero" — 0-indexing won because C won, and in C it is an artifact of pointer arithmetic rather than a conceptual necessity.
- **AI makes simple languages more valuable, not less.** He declines to forecast — "it's completely feasible that we won't have programming languages" — but argues that if the human's remaining job is reading and verifying, readability becomes the scarce property. Meanwhile "implementation is the part that AI can really help you. It's not a really important cost"; the durable costs are learning burden and cognitive load, which is what language design actually controls ([ai-era-engineering](../concepts/ai-era-engineering.md)).
- **Choose by interest, because the forecast is worthless.** "Nobody has any idea what the world, your profession, will be like in four years from now" — so employability is not a usable criterion. "I program because I like that" ([regrets-and-advice](../concepts/regrets-and-advice.md)).
- **Three languages, and a case for old ones.** Haskell ("in C you really spend one week to make it efficient, and then you spend one year to make it correct. In Haskell, you spend one week to make it correct"), a historical assembly such as the Intel 8080 because modern assembly is too complex to learn from, and Scheme for its "economy of ideas" — plus SNOBOL for pattern matching, because modern languages "tend to be too uniform" ([functional-programming](../concepts/functional-programming.md), [computer-architecture](../concepts/computer-architecture.md)).
- **No shortcut for time.** "To know a lot of stuff, you really have to study a lot of stuff. And it takes time" — with a jab at the "Learn Lua in 30 minutes" genre.

## Related

- [Episode: Creator of Lua: Scripting, Programming Languages, Predictions](../sources/creator-of-lua-scripting-programming.md) — his interview
- [Xavier Leroy](xavier-leroy.md) — the adjacent language-designer episode; convergent on small teams and predictable cost models, and on LLM code needing a property models don't supply
- [Bjarne Stroustrup](bjarne-stroustrup.md) — the corpus's sharpest counterparty on committee governance of a language
- [Simon Peyton Jones](simon-peyton-jones.md) — creator of the language Ierusalimschy names first for becoming a better engineer
- [Judea Pearl](judea-pearl.md) — the preceding week's guest; the other academic refusing to forecast AI capability
- [programming-languages](../concepts/programming-languages.md), [developer-tools](../concepts/developer-tools.md), [ai-era-engineering](../concepts/ai-era-engineering.md), [academia-vs-industry](../concepts/academia-vs-industry.md)
