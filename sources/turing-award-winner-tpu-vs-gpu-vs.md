---
type: source
updated: 2026-07-19
raw: ../raw/turing-award-winner-tpu-vs-gpu-vs.md
guest: "David Patterson"
guest_role: "Turing Award winner, UC Berkeley professor, RISC pioneer, Google distinguished engineer"
date: 2026-07-13
url: https://www.developing.dev/p/turing-award-winner-tpu-vs-gpu-vs
---

# Turing Award Winner: TPUs vs GPUs vs CPUs, Computer Architecture, RISC vs CISC | David Patterson

[David Patterson](../entities/david-patterson.md) is a Turing Award winner, [UC Berkeley](../entities/uc-berkeley.md) professor, co-author (with John Hennessy) of the standard computer architecture textbooks, coiner of "RISC," and now works at [Google](../entities/google.md) on TPUs. The episode walks through the historic RISC vs CISC debates, why compilers made RISC viable, how the end of Dennard scaling and the slowing of Moore's Law drove the industry to domain-specific architectures like GPUs and TPUs, and closes with Patterson's reflections on careers, courage, optimism, and family from half a century in the field.

## Key takeaways

- The RISC vs CISC debate of the 1980s was so vociferous partly because [computer architecture](../concepts/computer-architecture.md) then lacked quantitative methods — designs were argued by intuition and philosophy. Once numbers arrived: RISC needed ~30-40% more instructions but ran them 4-5x faster, a net 3-4x potential speedup.
- RISC won in practice: ARM began as the Acorn RISC Machine (renamed "Advanced RISC Machine" when [Apple](../entities/apple.md) adopted it for the Newton), has shipped ~350 billion processors, and today ~99% of all processors are RISC; x86's survival trick was translating x86 instructions into RISC micro-ops in hardware (an early-2000s [Intel](../entities/intel.md) move worth the overhead because of the PC binary software base).
- Compilers were the crux of the RISC argument: register allocation had been so poor that C let programmers hint register usage, but as compiler algorithms improved, simple instructions plus more registers (32 instead of 8-16) beat sophisticated instructions that compiler writers refused to use anyway.
- Dennard scaling (lowering threshold voltage kept chips at tens of watts as transistors doubled) quietly ended ~2005, forcing the shift to multicore; then Moore's Law slowed in the 2010s, forcing the ~2015 shift to domain-specific architectures — machine learning arrived at exactly the right moment to become the target domain.
- Google's 2016 TPU announcement was the watershed for [ai-era-engineering](../concepts/ai-era-engineering.md) hardware: a clean-slate design around a giant matrix-multiply unit, no hardware caches (software-scheduled memory), and bfloat16 — the first floating-point format with a bigger exponent than fraction — delivering ~30x GPU and ~80x CPU inference performance and pushing [Intel](../entities/intel.md) and [NVIDIA](../entities/nvidia.md) to react.
- NVIDIA's real moat is not just CUDA the language (funded by Jensen Huang in 2006) but the hand-tailored libraries its huge engineering staff rewrites for each new architecture — which is also why MLPerf benchmarks are less popular: startups can't match that library engineering, so NVIDIA wins the benchmark game.
- Moore's Law is factually over — SRAM barely improves, DRAM density gains went from 4x every 3 years to ~10 years per factor — but people conflate that with "technology stopped improving"; progress now comes from packaging (chiplets, dual full-reticle dies), narrower data types (8-bit and 4-bit floating point), and bigger matrix-multiply units. Patterson thinks denial about Moore's Law is partly emotional: semiconductor careers were built on sustaining it.
- Career advice ([regrets-and-advice](../concepts/regrets-and-advice.md)): keep family first ("nobody on their deathbed says I wish I spent more time in the office"), optimize for happiness over wealth, have fun as an adult, use Covey's urgent/important quadrant to protect non-urgent important work, and remember "it's not how many things you start, it's how many things you finish" — you're remembered for 5-6 things, not hundreds of little ones.
- Courage matters in a career ([influence-and-leadership](../concepts/influence-and-leadership.md)): fortune favors the bold, and someone should stand up to weak arguments even from company leaders — but "friends come and go, enemies accumulate," so pick confrontations carefully.
- His one do-over: as ACM SIGARCH chair in the 1990s he was unaware men were harassing young women at the annual conference; he wishes someone had told him because he would have stopped it.

## Notable quotes

- "It turned out you needed maybe 30%, 40% more simple instructions to execute in a program. But you could run them 4 or 5 times faster. So the net was 3 or 4x speedup was the potential for RISC over CISC." — David Patterson, ~03:43
- "Nobody on their deathbed says, you know, I wish I spent more time in the office." — David Patterson, ~43:17
- "It's not how many things you start, it's how many things you finish." — David Patterson, ~45:49
- "We boiled it down to nine magic words... 'I was wrong, you were right. I love you.'" — David Patterson, ~55:13

## Connections

- [Turing Award Winner: P vs NP, Zero-Knowledge Proofs, Quantum Computation | Avi Wigderson](turing-award-winner-p-vs-np-zero.md) — fellow Turing Award winner on foundational computer science.
- [Turing Award Winner: NSA, Public Key Cryptography, Crypto Wars | Martin Hellman](turing-award-winner-nsa-public-key.md) — fellow Turing Award winner; both stress courage/standing up (Hellman vs the NSA, Patterson vs weak arguments) and long marriages.
- [Turing Award Winner: Postgres, Disagreeing with Google, Future Problems | Mike Stonebraker](turing-award-winner-postgres-disagreeing.md) — fellow Berkeley professor and Turing Award winner who also built systems by betting against prevailing wisdom.
- [Turing Award Winner On Thinking Clearly, Paxos vs Raft, Working with Dijkstra | Leslie Lamport](turing-award-winner-on-working-with.md) — Turing Award series; contrasting style of settling debates (proofs vs measurements).
- [Creator of C++: Bell Labs, Negative Overhead Abstraction, Mistakes | Bjarne Stroustrup](creator-of-c-bell-labs-negative-overhead.md) — the compiler/low-level-language story here (C, register hints) connects directly to C++'s zero-overhead abstraction philosophy; Ryan mentions shooting the Bjarne episode in the intro.
