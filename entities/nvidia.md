---
type: entity
entity_kind: org
updated: 2026-07-19
sources: [distinguished-eng-on-stack-ranking.md, mozilla-firefox-cto-on-browser-war.md, turing-award-winner-tpu-vs-gpu-vs.md]
---

# NVIDIA

NVIDIA appears in three episodes as the dominant AI-hardware company whose moat, and the strategic question of how to relate to it, guests analyze from the outside.

## What the episodes reveal

- **The real moat is libraries, not just CUDA.** David Patterson argues NVIDIA's advantage is not merely the CUDA language (funded by Jensen Huang in 2006) but the hand-tailored libraries its huge engineering staff rewrites for each new architecture — which is also why MLPerf benchmarks lost popularity: startups can't match that library engineering, so NVIDIA wins the benchmark game. Google's 2016 TPU (~30x GPU inference) was the shot that forced NVIDIA and [Intel](intel.md) to react ([Patterson](../sources/turing-award-winner-tpu-vs-gpu-vs.md)).
- **Strategy in NVIDIA's shadow.** Oxide Computer deliberately avoids both doors — "compete with NVIDIA" and "partner with NVIDIA" — focusing on general-purpose compute instead of chasing the hot space ([Bryan Cantrill](../sources/distinguished-eng-on-stack-ranking.md)).
- **As a workplace.** Bobby Holley's NVIDIA internship was his example of structured onboarding — the contrast that made early Mozilla's "get on IRC and Bugzilla and figure out some things to do" anti-onboarding so striking ([Mozilla CTO](../sources/mozilla-firefox-cto-on-browser-war.md)).

## People

No guest's primary career was at NVIDIA; it appears through [David Patterson](david-patterson.md) (TPU-vs-GPU analysis), [Bryan Cantrill](bryan-cantrill.md) (Oxide strategy), and [Bobby Holley](bobby-holley.md) (internship).

## Related

- [computer-architecture](../concepts/computer-architecture.md) — GPUs, domain-specific architectures
- [ai-era-engineering](../concepts/ai-era-engineering.md) — the hardware substrate of the AI boom
- [Intel](intel.md), [Google](google.md) (TPUs)
