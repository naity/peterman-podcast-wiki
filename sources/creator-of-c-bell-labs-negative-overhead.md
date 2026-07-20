---
type: source
updated: 2026-07-19
raw: ../raw/creator-of-c-bell-labs-negative-overhead.md
guest: "Bjarne Stroustrup"
guest_role: "Creator of C++, former Bell Labs researcher"
date: 2026-05-18
url: https://www.developing.dev/p/creator-of-c-bell-labs-negative-overhead
---

# Creator of C++: Bell Labs, Negative Overhead Abstraction, Mistakes | Bjarne Stroustrup

[Bjarne Stroustrup](../entities/bjarne-stroustrup.md) created C++ at [Bell Labs](../entities/bell-labs.md), where he had weekly lunches with Dennis Ritchie for years. The episode covers the origin of C++ (born of his painful Cambridge PhD experience rewriting a Simula simulator in BCPL), what made Bell Labs the best applied engineering lab in the world, [programming language](../concepts/programming-languages.md) design philosophy — type systems, memory safety, "negative overhead abstraction" — plus standards-committee war stories (shuttle diplomacy between IBM and Intel, the Vasa battleship cautionary tale) and his skeptical take on [AI-written code](../concepts/ai-era-engineering.md) for safety-critical systems.

## Key takeaways

- C++ began as a failed attempt to build a distributed Unix: no language offered both low-level hardware access (C) and high-level structure (Simula's classes), so he merged them — after a Cambridge PhD ordeal where rewriting his Simula simulator in one-datatype BCPL made it ~50x faster but cost him "half his hair," convincing him never to work with inadequate tools again.
- Bell Labs hiring and research culture: no formal interview process (he flew over on his own tab, chatted with Dennis Ritchie, got a call a week later), and the research mandate was "do something interesting in a year's time" reported on a single sheet of paper — he argues this anarchic model out-produced carefully managed research programs (Unix, fiber optics, CCDs, cellular systems all emerged this way).
- Dennis Ritchie helped design C++'s const and endorsed C++ as C's successor in writing — Stroustrup calls the C vs C++ language wars "ridiculous"; Ritchie's "fat pointers" (pointer + size) were rejected by the C committee decades before the same idea shipped in C++ as span. Modern C function declaration syntax and call semantics actually came from Stroustrup's early C++ work.
- Advice on building languages: "what do I need to build a language" is the wrong question — identify a problem no existing language solves first; C++ reused C as its portable assembler/interface to 25 linkers and dozens of optimizers ("we can have Dennis Ritchie's mistakes, which we know, and my mistakes, which we don't know yet — so we'll take Dennis's").
- C++ was never an object-oriented language: it's type/class-oriented, deliberately supporting non-OO styles (no "object-oriented complex numbers" — math notation and Fortran-level performance mattered), and static typing was chosen because embedded systems (99% of all computers) can't drop into a debugger and must fit small memories.
- On [memory safety](../concepts/security-and-cryptography.md): "I'm so tired of that" — per Herb Sutter's data, over 90% of exploited C++ safety bugs come from C-style code with raw pointers; hardened libraries exist everywhere, C++26 standardizes a hardened option, and his profiles work aims to make guarantees enforceable by default (proposed for C++29) against committee members "devoted to their old code."
- Standardization was forced on him: IBM/HP representatives spent an hour twisting his arm in his office in 1989 because their organizations couldn't depend on a corporate-owned language; without it, he believes C++ would have "faded into an academic cube language." C++ marketing budget: $5,000 over three years, versus Sun's massive Java campaign — yet C++ developers grew 10-12x since Java promised to kill it. The 527-member committee runs on judged consensus (~80-90% supermajorities), not simple majorities, to avoid dialects.
- The Vasa story he told the committee: the king's demand for a second gun deck on a half-built battleship (plus skipped stability tests) sank it in Stockholm harbor in 1624 — lessons: improve the foundation before stacking features, never compromise testing, and sometimes the professional thing is telling the bosses no.
- Performance philosophy: C++ can beat C ("negative overhead abstraction") because more type information feeds the optimizer; 1990s-clever hand optimizations are often pessimizations on modern hardware — his standard first optimization step is deleting the clever code, and Knuth's 2-3% rule tells you where optimizing is worth it.
- On AI writing code: fine for boilerplate and docs, but in safety/performance-critical domains (his 10-20% of the world's code) LLM output brings more bugs, bloat, and an unsolvable validation burden — regulators require validating changes, prompts perturb whole codebases, senior validators are retiring, and eliminating junior programmers begs the question "where do you get the senior programmers from?" He also channels Dijkstra: natural language is too ambiguous to be a programming language.

## Notable quotes

- "We can have Dennis Ritchie's mistakes, which we know, and we can have my mistakes, which we don't know yet, so we'll take Dennis's." — Bjarne (31:21), on choosing C compatibility
- "This is why I talk about zero overhead abstraction... that's understating the ability of the C++ compiler. We can do negative overhead abstraction." — Bjarne (1:23:12)
- "There are people who say you should only standardize what is common in industry, but when the bugs are common in industry, you should do something else." — Bjarne (48:53)
- "They built more features on top without improving the foundation... And furthermore, you've all noticed when your high bosses say something should be done, and the high bosses don't always know what's right. Sometimes the professional thing is to say, no, we are not doing this." — Bjarne (1:16:56), on the Vasa
- "I'm always told by AI proponents that either the problem has already been solved or it'll be solved in the next release... The idea that the next version will solve the problem is always a dangerous assumption." — Bjarne (1:34:10)

## Connections

- [Co-Creator of Haskell: Functional Programming, Thinking in Types, Useless Languages | Simon Peyton Jones](co-creator-of-haskell-functional.md) — fellow language creator; Stroustrup explicitly recommends learning ML/Haskell to escape monoglot thinking, and both discuss type systems deeply.
- [Turing Award Winner: Data Abstraction, Dijkstra, Distributed Systems | Barbara Liskov](turing-award-winner-data-abstraction.md) — abstraction and language design from the CLU lineage; both worked on the foundations of modern type systems and both invoke Dijkstra.
- [Turing Award Winner: TPUs vs GPUs vs CPUs, Computer Architecture, RISC vs CISC | David Patterson](turing-award-winner-tpu-vs-gpu-vs.md) — hardware-software boundary: Stroustrup's cache/memory-model concerns (IBM vs Intel shuttle diplomacy) meet Patterson's architecture perspective.
- [Turing Award Winner On Thinking Clearly, Paxos vs Raft, Working with Dijkstra | Leslie Lamport](turing-award-winner-on-working-with.md) — another legend-of-CS episode; Stroustrup cites Dijkstra's verdict on natural-language programming.
- [OpenAI Eng & Dev Tools Founder: How Software Engineering Is Changing | Charlie Marsh](openai-eng-and-dev-tools-founder.md) — contrasting, more optimistic view of AI-era tooling versus Stroustrup's skepticism about LLM code in critical systems.
