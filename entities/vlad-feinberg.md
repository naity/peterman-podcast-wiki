---
type: entity
entity_kind: person
updated: 2026-07-19
sources: [google-deepmind-pre-training-lead.md]
---

# Vlad Feinberg

Pre-training area lead at Google DeepMind for Gemini Flash and Flash-Lite ([Google](google.md)) ([episode](../sources/google-deepmind-pre-training-lead.md)).

## Career arc

Feinberg's rise came from taking unglamorous but important work: after his manager Rohan Anil pushed him off maximizing first-author papers, he did hyperparameter tuning and "golfing the XLA compiler" for SFT on the first Bard release using old TPUs — work that earned a Jeff Dean spot bonus and snowballed into leading pre-training ([episode](../sources/google-deepmind-pre-training-lead.md)). His signature war story: Flash 2.0's MoE-at-Flash-latency problem looked infeasible until his report Geng Yan's pipeline-prefill idea (parallelize layers instead of experts so experts stay machine-resident) hid the communication cost — followed by 40 days of dual-shift training babysitting by a ~five-person rotation, ending with Flash 2.0 Thinking topping LMSYS just as DeepSeek-V3 launched ([episode](../sources/google-deepmind-pre-training-lead.md)).

## Key views & advice

- Frontier labs have "voracious demand" for kernel development and low-level engineering; much frontier work is classical [distributed-systems](../concepts/distributed-systems.md) engineering at extreme scale — DeepMind's distillation infra went through 3-4 design-doc-driven generational rewrites without which Flash 3.0 would not exist ([episode](../sources/google-deepmind-pre-training-lead.md)).
- Engineering is a roughly deterministic DAG of milestones; research is a stochastic MDP, and "research taste" is learned intuition for estimating success probability and cost of unproven approaches ([episode](../sources/google-deepmind-pre-training-lead.md)).
- Pre-training is scaling laws as recipes (FLOPs budget to training routine plus loss prediction) because each run is one-shot at unprecedented scale; Kaplan and Chinchilla papers are table stakes for candidates ([episode](../sources/google-deepmind-pre-training-lead.md)).
- [Getting hired](../concepts/hiring-and-interviews.md): the best signal is public evidence you built something useful (vLLM, SGLang, TensorRT/Dynamo contributions); study kernel DSLs (ThunderKittens, CuTe), RL literature, and the distributed-systems/optimization overlap. His standing offer: do The Scaling Book exercises handwritten on video plus his transformer exercise and he will interview you for his New York team ([episode](../sources/google-deepmind-pre-training-lead.md)).
- Against "permanent underclass" AI doom: accountability keeps humans essential — "you can't hand off blame to AI... they can't represent you in court because they can't be disbarred"; planning around stochastic AI components is the differentiating skill ([episode](../sources/google-deepmind-pre-training-lead.md)).
- [Advice](../concepts/regrets-and-advice.md): chase problems people face today with humility, embrace the menial parts of important projects, and "be the kind of coworker that people would want to see succeed" — amicability beats cynical workplace game theory ([episode](../sources/google-deepmind-pre-training-lead.md)).

## Related

- [Episode: Google DeepMind Pre-Training Lead: How To Get a Job at a Frontier Lab](../sources/google-deepmind-pre-training-lead.md) — his interview
- [Charlie Marsh](charlie-marsh.md) — complementary take on which engineering skills stay valuable in the AI era
- [David Patterson](david-patterson.md) — the TPU hardware side of the accelerator co-design Feinberg works atop
- [John Myles White](john-myles-white.md) — notes frontier-lab AI researchers are the exception to the labor-leverage shift
- [ai-era-engineering](../concepts/ai-era-engineering.md), [hiring-and-interviews](../concepts/hiring-and-interviews.md), [career-growth](../concepts/career-growth.md), [working-with-legends](../concepts/working-with-legends.md)
