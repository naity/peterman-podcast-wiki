---
type: entity
entity_kind: person
updated: 2026-07-19
sources: [creator-of-c-bell-labs-negative-overhead.md]
---

# Bjarne Stroustrup

Creator of C++, former [Bell Labs](bell-labs.md) researcher ([episode](../sources/creator-of-c-bell-labs-negative-overhead.md)).

## Career arc

His Cambridge PhD ordeal — rewriting a Simula simulator in BCPL (~50x faster, cost "half his hair") — convinced him never to use inadequate tools again ([episode](../sources/creator-of-c-bell-labs-negative-overhead.md)). At Bell Labs, whose culture was "hire the best people and don't tell them what to do" (his job description: "do something interesting in a year's time," no formal interview — he chatted with Dennis Ritchie and got an offer by phone a week later), a failed attempt to build a distributed Unix exposed the gap C++ filled: no language combined C's low-level hardware access with Simula's high-level class structure ([episode](../sources/creator-of-c-bell-labs-negative-overhead.md)). Ritchie helped design const and endorsed C++ as C's successor — the C vs C++ wars were "ridiculous" ([working-with-legends](../concepts/working-with-legends.md)) ([episode](../sources/creator-of-c-bell-labs-negative-overhead.md)). Standardization was forced on him in 1989 by [IBM](ibm.md) and HP, who couldn't depend on a corporate-owned language; the 527-member committee runs on judged consensus (~80-90%) to prevent dialects, and C++ grew its developer base 10-12x after Java — with Sun's marketing campaign versus C++'s $5,000 budget — promised to kill it ([episode](../sources/creator-of-c-bell-labs-negative-overhead.md)).

## Key views & advice

- "What do I need to build a language" is the wrong question — first identify a problem no existing language solves; C++ used C as its portable assembler: "we can have Dennis Ritchie's mistakes, which we know... so we'll take Dennis's" ([episode](../sources/creator-of-c-bell-labs-negative-overhead.md)).
- C++ was never object-oriented — it is type/class-oriented and deliberately multi-paradigm; static typing was chosen because ~99% of computers are memory-constrained embedded systems ([episode](../sources/creator-of-c-bell-labs-negative-overhead.md)).
- Richer type information can beat C: "negative overhead abstraction." Modern first optimization step: delete the clever 1990s hand-optimized code, guided by Knuth's 2-3% rule ([episode](../sources/creator-of-c-bell-labs-negative-overhead.md)).
- On memory safety: over 90% of exploited C++ safety bugs come from C-style raw-pointer code (Herb Sutter's data); C++26 standardizes a hardened library and his profiles work aims to make safety enforceable by default — "when the bugs are common in industry, you should do something else" ([episode](../sources/creator-of-c-bell-labs-negative-overhead.md)).
- The Vasa story he told the standards committee: adding a second gun deck to a half-built ship sank it — improve foundations before adding features, never skip testing, and sometimes the professional thing is to tell the bosses no ([episode](../sources/creator-of-c-bell-labs-negative-overhead.md)).
- On [AI writing code](../concepts/ai-era-engineering.md): fine for boilerplate and docs, but in safety/performance-critical domains it brings bugs, bloat, and an unsolvable validation burden; eliminating junior programmers raises "where do you get the senior programmers from?", and (echoing Dijkstra) natural language is too ambiguous to be a programming language. "The idea that the next version will solve the problem is always a dangerous assumption" ([episode](../sources/creator-of-c-bell-labs-negative-overhead.md)).

## Related

- [Episode: Creator of C++: Bell Labs, Negative Overhead Abstraction, Mistakes](../sources/creator-of-c-bell-labs-negative-overhead.md) — his interview
- [Simon Peyton Jones](simon-peyton-jones.md) — fellow language creator; Stroustrup recommends learning ML/Haskell
- [David Patterson](david-patterson.md) — the hardware side of the compiler/register story C++ grew up in
- [Charlie Marsh](charlie-marsh.md) — the optimistic counterpoint on AI-era developer tooling
- [programming-languages](../concepts/programming-languages.md), [working-with-legends](../concepts/working-with-legends.md), [teaching-and-communication](../concepts/teaching-and-communication.md)
