---
type: concept
updated: 2026-07-19
sources: [turing-award-winner-tpu-vs-gpu-vs.md, co-creator-of-haskell-functional.md, google-deepmind-pre-training-lead.md, aws-distinguished-eng-learnings-from.md]
---

# Computer architecture

Hardware design and the hardware-software boundary — anchored by [David Patterson](../entities/david-patterson.md)'s Turing-laureate episode on RISC vs CISC and the shift to domain-specific accelerators, with corroboration and one instructive counter-example from other guests.

## What the guests say

### RISC vs CISC: how numbers ended a religious war

Patterson recounts that the 1980s debate was vociferous because architecture lacked quantitative methods — designs were argued "by intuition and philosophy." Once measured, RISC needed ~30–40% more instructions but ran them 4–5x faster, a net 3–4x potential speedup. RISC won in practice — ARM has shipped ~350 billion processors and ~99% of all processors today are RISC — while x86 survived by translating its instructions into RISC micro-ops in hardware. The crux was compilers: as register allocation improved, simple instructions plus 32 registers beat sophisticated instructions compiler writers refused to use anyway ([episode](../sources/turing-award-winner-tpu-vs-gpu-vs.md)).

### The end of free scaling and the turn to specialization

Patterson's periodization: Dennard scaling quietly ended ~2005, forcing multicore; Moore's Law slowed in the 2010s, forcing the ~2015 shift to domain-specific architectures — and machine learning arrived at exactly the right moment to be the target domain. Google's 2016 TPU (a clean-slate design around a giant matrix-multiply unit, no hardware caches, and bfloat16 — the first floating-point format with a bigger exponent than fraction) delivered ~30x GPU and ~80x CPU inference performance. He insists Moore's Law is factually over (DRAM density gains went from 4x every 3 years to ~10 years per factor) and that denial is partly emotional — careers were built on sustaining it; progress now comes from packaging (chiplets), narrower data types (8- and 4-bit floats), and bigger matrix units ([episode](../sources/turing-award-winner-tpu-vs-gpu-vs.md)).

**Counterpoint from history — specialization can also be a trap.** [Simon Peyton Jones](../entities/simon-peyton-jones.md) calls the 1980s attempts to build hardware for functional languages (Lisp machines, dataflow machines, the SKIM combinator machine) an "inspiring mistake": those machines were interpreters in hardware, doing at runtime what a compiler does better at compile time, and no niche architecture could outrun Intel's man-years on x86 ([episode](../sources/co-creator-of-haskell-functional.md)). Read against Patterson, the lesson is that domain-specific hardware wins only when (a) general-purpose scaling has actually stalled and (b) the domain is a huge, regular computation (matrix multiply) rather than a language runtime. Patterson's own account of NVIDIA's moat makes the same point from the winner's side: it is not CUDA per se but the hand-tailored libraries a huge engineering staff rewrites for each architecture generation — man-years again ([episode](../sources/turing-award-winner-tpu-vs-gpu-vs.md)).

### Why software engineers should still care

[Vlad Feinberg](../entities/vlad-feinberg.md) reports "voracious demand" at frontier labs for kernel development and low-level engineering, and points to programming-language abstractions for kernels (ThunderKittens, CuTe DSL) as a high-leverage study area — the TPU/GPU efficiency problems Patterson describes are now everyday AI-infrastructure work ([episode](../sources/google-deepmind-pre-training-lead.md)). [Marc Brooker](../entities/marc-brooker.md) recommends Hennessy & Patterson's architecture textbook as core reading for systems engineers and treats hardware trends (faster networks, storage, GPUs) as a primary input for finding problems worth solving ([episode](../sources/aws-distinguished-eng-learnings-from.md)).

## Practical takeaways

- Settle architecture arguments with measurements, not philosophy — the RISC war ended when the numbers arrived ([Patterson](../sources/turing-award-winner-tpu-vs-gpu-vs.md)).
- Expect performance gains from specialization, packaging, and narrower data types now, not from process scaling ([Patterson](../sources/turing-award-winner-tpu-vs-gpu-vs.md)).
- Before betting on specialized hardware, check whether a compiler could do the same work at compile time on commodity silicon ([Peyton Jones](../sources/co-creator-of-haskell-functional.md)).
- Moats in hardware are software: libraries and toolchains, sustained over generations ([Patterson](../sources/turing-award-winner-tpu-vs-gpu-vs.md)).
- Low-level and kernel skills are a seller's market at AI labs ([Feinberg](../sources/google-deepmind-pre-training-lead.md)).

## Related

- [ai-era-engineering](ai-era-engineering.md) — accelerators are the substrate of the AI era; [programming-languages](programming-languages.md) — the compiler side of the hardware-software boundary; [distributed-systems](distributed-systems.md) — hardware trends as design inputs.
- Key people: [David Patterson](../entities/david-patterson.md), [Simon Peyton Jones](../entities/simon-peyton-jones.md), [Vlad Feinberg](../entities/vlad-feinberg.md).
- Most relevant episode: [Patterson](../sources/turing-award-winner-tpu-vs-gpu-vs.md).
