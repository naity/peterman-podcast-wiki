---
type: entity
entity_kind: person
updated: 2026-07-19
sources: [turing-award-winner-tpu-vs-gpu-vs.md]
---

# David Patterson

Turing Award winner, [UC Berkeley](uc-berkeley.md) professor, coiner of "RISC," co-author (with John Hennessy) of the standard [computer architecture](../concepts/computer-architecture.md) textbooks, and now a [Google](google.md) distinguished engineer working on TPUs ([episode](../sources/turing-award-winner-tpu-vs-gpu-vs.md)).

## Career arc

Patterson led the 1980s RISC movement at Berkeley when architecture was argued by intuition rather than measurement; his quantitative case — RISC needs ~30-40% more instructions but runs them 4-5x faster, a net 3-4x speedup — eventually won the field, with ARM shipping ~350 billion processors, ~99% of processors today being RISC, and [Intel](intel.md)'s x86 surviving only by translating instructions into RISC micro-ops in hardware ([episode](../sources/turing-award-winner-tpu-vs-gpu-vs.md)). After Dennard scaling ended (~2005) and Moore's Law slowed (2010s), he was part of the ~2015 turn to domain-specific architectures at Google, where the 2016 TPU — a clean-slate matrix-multiply design with software-managed memory and bfloat16 — hit ~30x GPU and ~80x CPU inference performance and forced [Intel](intel.md) and [NVIDIA](nvidia.md) to respond ([episode](../sources/turing-award-winner-tpu-vs-gpu-vs.md)).

## Key views & advice

- Quantitative measurement settles architecture wars; the RISC/CISC fight was ferocious precisely because the field lacked numbers ([episode](../sources/turing-award-winner-tpu-vs-gpu-vs.md)).
- Moore's Law is genuinely over (SRAM barely improves; DRAM density gains slowed from 4x/3yr to ~10yr per factor), and denial is partly emotional because careers were built on sustaining it; progress now comes from chiplet packaging, 8- and 4-bit floating point, and bigger matrix units ([episode](../sources/turing-award-winner-tpu-vs-gpu-vs.md)).
- NVIDIA's moat is its hand-tailored libraries as much as CUDA — armies of engineers re-tune them per architecture, which is also why startups struggle on MLPerf ([episode](../sources/turing-award-winner-tpu-vs-gpu-vs.md)).
- [Career](../concepts/career-growth.md) rules ([regrets-and-advice](../concepts/regrets-and-advice.md)): family first ("nobody on their deathbed says I wish I spent more time in the office"), optimize happiness over wealth, protect important non-urgent work (Covey quadrant), and finish things — "it's not how many things you start, it's how many things you finish" ([episode](../sources/turing-award-winner-tpu-vs-gpu-vs.md)).
- Courage is career-critical ([influence-and-leadership](../concepts/influence-and-leadership.md)): someone should stand up to weak arguments even from leaders, but "friends come and go, enemies accumulate." His one regret: not knowing about harassment at SIGARCH conferences he chaired, which he would have stopped ([episode](../sources/turing-award-winner-tpu-vs-gpu-vs.md)).
- Marriage repair kit, boiled down to nine words: "I was wrong. You were right. I love you." ([episode](../sources/turing-award-winner-tpu-vs-gpu-vs.md)).

## Related

- [Episode: Turing Award Winner: TPUs vs GPUs vs CPUs, Computer Architecture, RISC vs CISC](../sources/turing-award-winner-tpu-vs-gpu-vs.md) — his interview
- [Martin Hellman](martin-hellman.md) — fellow Turing laureate; shared theme of courage against institutional opposition
- [Bjarne Stroustrup](bjarne-stroustrup.md) — the compiler/low-level-language side of the same era (C register hints, abstraction cost)
- [Vlad Feinberg](vlad-feinberg.md) — the modern TPU/accelerator workloads Patterson's hardware serves
- [computer-architecture](../concepts/computer-architecture.md), [ai-era-engineering](../concepts/ai-era-engineering.md), [regrets-and-advice](../concepts/regrets-and-advice.md)
