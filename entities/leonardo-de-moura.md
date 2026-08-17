---
type: entity
entity_kind: person
updated: 2026-08-10
sources: [creator-of-lean-the-end-of-handwritten.md]
---

# Leonardo de Moura

Creator of the Lean proof assistant and, twenty years earlier, of the Z3 SMT solver — two of the most widely deployed pieces of automated-reasoning infrastructure in existence. Senior Principal Applied Scientist at [AWS](aws.md) and co-founder, with Sebastian Ullrich, of the nonprofit behind Lean.

## Career arc

He started Z3 around 2006 on joining [Microsoft](microsoft.md) Research: a fully automatic SMT solver whose background theories (arithmetic, arrays) were chosen for test-case generation and software verification, and which became the backend of a generation of program-analysis tools ([episode](../sources/creator-of-lean-the-end-of-handwritten.md)). Z3 turned out to be excellent at *finding* bugs — encode a suspicious execution path as constraints and get either "unsatisfiable" or a concrete triggering input — and, in his own assessment, "never super successful" at proving their absence: the heuristics for quantified properties were hand-coded, they failed on anything nontrivial, and users who already knew the proof had no way to tell the solver about it. "That's why Lean started."

Lean is now thirteen years old and spent its first ten as a research project. Its first constituency was mathematicians, not programmers — mathlib began in 2017, and the 2020 Liquid Tensor Experiment (formalizing an unpublished result Fields Medalist Peter Scholze was unsure of) is what brought the math community in. It became "a product" only in 2023, when he and Ullrich founded the nonprofit and could hire an engineering team, funded on the strength of that mathematical impact; AWS/Amazon are its largest donors so far, and the direction the funding pushes is the underfunded half — Lean as a general programming language for software and hardware verification ([academia-vs-industry](../concepts/academia-vs-industry.md)). At AWS itself there is a half-million-line Lean compiler for AI accelerators, where the proofs are a bonus rather than the goal.

He describes the C++ → Lean self-hosting rewrite for Lean 4 as the hardest thing he has built: ~100,000 lines, all human-written, bootstrapped with deliberately minimal features, failing file by file down a 1,000-file pipeline, and requiring proofs constructed with no interactivity at all — "almost like programming in assembly." "I literally wanted to cry when I managed to compile Lean 4." Many people expected the attempt to fail.

## Key views & advice

- **Specifications were never the bottleneck; proof maintenance was.** [Formal verification](../concepts/formal-verification.md) cost roughly 10x the program historically, and the recurring pain was repairing proofs after every code change, often without remembering why they were written. "Properties are usually vaguely in your mind," and his most portable line is that "an inefficient program can be viewed as a specification" — write the naive version, then ask for the fast one plus a proof of equivalence ([episode](../sources/creator-of-lean-the-end-of-handwritten.md)).
- **AI has already absorbed the proof-writing cost.** Models are "extremely good at proving, writing formal proofs, maintaining formal proofs"; his colleague Kim Morrison got an AI to translate zlib from C into Lean, pass zlib's test suites, and prove that decompression inverts compression — in about a week. "Six months ago, I would say this is science fiction" ([ai-era-engineering](../concepts/ai-era-engineering.md)).
- **Proofs are for optimization courage, not just safety.** People refuse to optimize code they don't fully understand; a proof removes the fear, and an agent that hands you a proof of equivalence alongside its optimization is "a game changer" compared with inspecting the diff by hand. His own workflow: "I'm not writing unit tests anymore. I'm writing properties and proving them" ([episode](../sources/creator-of-lean-the-end-of-handwritten.md)).
- **Once a proof carries the code, how the code reads stops mattering.** "If I'm not the one that's writing most of the code anyway, it doesn't really matter... It doesn't really matter how the code has been written" — which dissolves the usual objections to [functional programming](../concepts/functional-programming.md) and puts him directly against [Roberto Ierusalimschy](roberto-ierusalimschy.md)'s argument, made a week earlier, that AI makes readability *more* valuable.
- **Handwritten math changes dramatically but survives as communication.** Handwritten proofs persist the way handmade furniture does, because a proof is an artifact for convincing another human. Humans also stay structurally in the loop as the writers of specifications, without which AI-generated math is "some alien thing that's going by itself" ([episode](../sources/creator-of-lean-the-end-of-handwritten.md)).
- **AI finds proofs; it does not yet invent mathematics.** No evidence of novel concept formation — the million-line refutation of the unit distance conjecture is a proof, not a theory — but "I would not bet against AI here."
- **Design by listening to a specific community.** He chose dependent type theory over the much-easier-to-implement higher-order logic because Jeremy Avigad convinced him serious mathematicians would never adopt the latter; abstract math needs structures as first-class citizens, and higher-order logic forces "encoding tricks. It's a mess." Same-day feature turnaround for early users, and a Zulip community that answered in five minutes, are what he credits for Lean's growth ([open-source](../concepts/open-source.md), [programming-languages](../concepts/programming-languages.md)).
- **Extensibility is a distribution strategy.** Because Lean is written in Lean, outsiders build serious things without ever contacting the core team — Patrick Massot's Lean Verbose (proofs as structured English/French textbook prose with clickable next moves), the Veil protocol-verification DSL — and AI agents now write Lean metaprograms to debug their own conjectures ([developer-tools](../concepts/developer-tools.md)).
- **Advice to his younger self is social.** "I'm super introverted. And I would tell, look, you should work on your people skills because it helps a lot... when you have to interact with a community, with people." He otherwise refuses to warn himself: "eagerness is bliss. I mean, you don't know how hard things are, and when you start the adventure" ([regrets-and-advice](../concepts/regrets-and-advice.md)).

## Related

- [Episode: Creator of Lean: Handwritten Math Will Change Dramatically](../sources/creator-of-lean-the-end-of-handwritten.md) — his interview
- [Xavier Leroy](xavier-leroy.md) — the corpus's other verification anchor; same Dijkstra opening and the same "decade of formal verification" call, but Leroy thinks specifications are the unsolved problem and de Moura thinks proof maintenance was
- [Leslie Lamport](leslie-lamport.md) — "understanding means you can write a proof of it," which de Moura reports as an empirical effect of formalizing anything
- [Roberto Ierusalimschy](roberto-ierusalimschy.md) — the direct disagreement about whether AI makes code readability more or less important
- [Simon Peyton Jones](simon-peyton-jones.md) — Lean is "close to Haskell, but with the support for proofs"; dependent types are the escalation of his static-typing case
- [Judea Pearl](judea-pearl.md) — the other guest drawing a boundary around AI capability, structurally where de Moura draws it empirically
- [Edsger Dijkstra](edsger-dijkstra.md) — the testing aphorism the whole episode is built on
- [Anders Hejlsberg](anders-hejlsberg.md) — the direct objection from outside formal methods: a proof discharges correctness, not accountability, and you cannot fix or answer for code you don't understand ([his episode](../sources/creator-of-typescript-10x-faster.md))
- [Marc Brooker](marc-brooker.md) — AWS colleague whose specification-driven-development prediction this episode supplies the missing verification layer for
- [AWS](aws.md), [Amazon](amazon.md), [Microsoft](microsoft.md) — Lean's largest funder, and Z3's birthplace
- [formal-verification](../concepts/formal-verification.md), [ai-era-engineering](../concepts/ai-era-engineering.md), [programming-languages](../concepts/programming-languages.md)
