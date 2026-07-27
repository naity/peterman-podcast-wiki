---
type: entity
entity_kind: person
updated: 2026-07-27
sources: [creator-of-ocaml-functional-programming.md]
---

# Xavier Leroy

Creator of the OCaml programming language and lead of CompCert, the formally verified C compiler; French researcher hired at Inria in the 1990s, now a professor (Collège de France), still maintaining OCaml and CompCert at almost 60.

## Career arc

Hired at Inria on a research position in the '90s having built the predecessor of OCaml, at a moment when colleagues told him "there's no future in programming language research — industry has decided it will be C forever"; Java's arrival a few years later vindicated PL research ([episode](../sources/creator-of-ocaml-functional-programming.md)). OCaml, designed for theorem provers and DSLs, found systems users via Cornell's Ensemble network stack (whose PhD student Yaron Minsky took it to Jane Street) and MirageOS unikernels. He then spent many years proving CompCert correct in the Coq/Rocq proof assistant — a C compiler whose emitted assembly is proved faithful to the source, deliberately written in a purely functional style so it could be reasoned about, with termination itself among the proved properties. He was initially reluctant about the multicore rewrite of OCaml's runtime (shipped 2022, built largely by OCaml Labs at Cambridge), having always preferred Erlang-style message passing over shared memory ([episode](../sources/creator-of-ocaml-functional-programming.md)).

## Key views & advice

- Manual memory management is not automatically faster than GC: defensive copying and ownership-forced unsharing can make Rust/C code lose to a garbage collector, and stack-allocation tricks (Jane Street's OxCaml) win less than expected ([programming-languages](../concepts/programming-languages.md), [episode](../sources/creator-of-ocaml-functional-programming.md)).
- [Functional programming](../concepts/functional-programming.md) is not fundamentally harder — "Python is 50% functional language"; the Rob Pike "Googlers" quote describes Google's hiring model, and Jane Street inverts it by using OCaml as a [hiring filter](../concepts/hiring-and-interviews.md) ([episode](../sources/creator-of-ocaml-functional-programming.md)).
- JavaScript's total dynamism (runtime-redefinable method invocation, call-stack introspection) is "a security nightmare... completely unnecessary" ([episode](../sources/creator-of-ocaml-functional-programming.md)).
- [Formal verification](../concepts/formal-verification.md) champion: purely functional style shrinks the gap between program and mathematics; mechanized proofs (vs. thousand-page paper proofs) are what make verified software evolvable; predicts "maybe this will be the decade of formal verification" ([episode](../sources/creator-of-ocaml-functional-programming.md)).
- AI-code skeptic on economic grounds: "every new line of code is a liability" — generation cost falls to zero but checking cost doesn't, and expecting humans to review the volume "is just wrong." Receives mostly-noise AI-generated bug reports on OCaml/CompCert and may ban AI contributions ([open-source](../concepts/open-source.md)). His proposed fix: LLMs should emit machine-checkable Lean/Coq proofs, which relocates the hard problem to trustworthy specifications ([ai-coding-tools](../concepts/ai-coding-tools.md), [episode](../sources/creator-of-ocaml-functional-programming.md)).
- Advice ([regrets-and-advice](../concepts/regrets-and-advice.md)): he specialized in PL too early — get broad CS foundations (computability, complexity) even when they look irrelevant. Books: *Programming Pearls*, *How to Design Programs* ([episode](../sources/creator-of-ocaml-functional-programming.md)).

## Related

- [Episode: Creator of OCaml: Functional Programming, Formal Verification, Programming Languages](../sources/creator-of-ocaml-functional-programming.md) — his interview
- [Simon Peyton Jones](simon-peyton-jones.md) — creator of Haskell, OCaml's lazy/pure sibling; convergent view that type systems help LLM codegen
- [Bjarne Stroustrup](bjarne-stroustrup.md) — fellow language creator and fellow LLM-code skeptic; C++ is CompCert's source-language world
- [Leslie Lamport](leslie-lamport.md) — the podcast's other proofs-first thinker ("understanding means you can write a proof")
- [Edsger Dijkstra](edsger-dijkstra.md) — Leroy builds his verification argument on Dijkstra's testing aphorism
- [formal-verification](../concepts/formal-verification.md), [programming-languages](../concepts/programming-languages.md), [functional-programming](../concepts/functional-programming.md)
