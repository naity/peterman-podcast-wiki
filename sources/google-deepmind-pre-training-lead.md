---
type: source
updated: 2026-07-19
raw: ../raw/google-deepmind-pre-training-lead.md
guest: "Vlad Feinberg"
guest_role: "Google DeepMind pre-training area lead (Gemini Flash/Flash-Lite)"
date: 2026-06-15
url: https://www.developing.dev/p/google-deepmind-pre-training-lead
---

# Google DeepMind Pre-Training Lead: How To Get a Job at a Frontier Lab | Vlad Feinberg

Vlad Feinberg leads pre-training at [Google DeepMind](../entities/google.md), where his team delivers the Gemini Flash and Flash-Lite models that power AI Overviews and AI Mode in Search. Building on his viral post "How to Land a Job at a Frontier Lab," he lays out concretely which skills labs are desperate for, how research work differs from software engineering, and how to signal your fitness to labs like DeepMind, [Anthropic](../entities/anthropic.md), or [OpenAI](../entities/openai.md) — plus war stories from shipping Flash 2.0 and a spot bonus from Jeff Dean.

## Key takeaways

- Frontier labs have "voracious demand" for kernel development and low-level engineering across the stack ([hiring-and-interviews](../concepts/hiring-and-interviews.md)); much of frontier work is classical backend/[distributed-systems](../concepts/distributed-systems.md) engineering at extreme scale — DeepMind's distillation infrastructure went through 3–4 generational rewrites that each started with "a good old-fashioned design doc," and Flash 3.0 wouldn't exist without them.
- The research/applied divide is blurrier than people think: even product verticals like Gemini-for-Search do hard research (factuality, grounding, source quality), while "pure research" teams also act as SREs for training runs. Everyone must be fluid across the spectrum ([ai-era-engineering](../concepts/ai-era-engineering.md)).
- The core difference between engineering and research: an engineering project is a roughly deterministic DAG of milestones you can execute monotonically, while research is a stochastic (even hidden) MDP — per Jacob Steinhardt's "research as an MDP" framing — where "research taste" is the learned intuition for estimating success probabilities and time costs of unproven approaches.
- Table-stakes context for LLM pre-training: the Kaplan and Chinchilla scaling-law papers. The name of the game is recipes — functions from FLOPs budget to training routine — paired with prediction rules for final loss, because every pre-training run is effectively one-shot at a scale never attempted before.
- High-leverage domains to study: programming-language abstractions for kernels (ThunderKittens, CuTe DSL), reinforcement learning literature (PPO/RLHF is now unquestionably in production), and the distributed-systems/optimization overlap (asynchrony, gradient staleness, pipelining effects on convergence).
- Best marketing signal to labs: public evidence you've made something useful — optimizing open-source LLM serving stacks (vLLM, SGLang, TensorRT/Dynamo contributions) counts heavily; for internal transfers, becoming the person who integrates LLMs effectively in your product org naturally makes you the research team's partner (that's how Nate Lintz moved from Search to owning Flash inference co-design).
- His concrete hiring invitation: complete The Scaling Book exercises handwritten on video plus his transformer exercise, and he'll interview you for his New York team — someone responded within a week ([career-growth](../concepts/career-growth.md)).
- On AI doomerism: he rejects the "permanent underclass" FUD — accountability keeps humans in the loop ("you can't hand off blame to AI... LLMs can't be disbarred"), and the research skill of planning around stochastic components will matter in every job.
- The Jeff Dean spot bonus came from unglamorous work — hyperparameter tuning and "golfing the XLA compiler" for SFT on the first Bard release, on old TPUs — after his manager Rohan Anil pushed him off pure paper-maximizing research; that small engagement snowballed into his current role ([working-with-legends](../concepts/working-with-legends.md)).
- Flash 2.0 war story: an MoE at Flash latency was thought infeasible because sharding experts across N chips explodes communication; his report Geng Yan's pipeline-prefill idea (parallelize layers, not experts, keeping experts resident per machine) hid the communication and made Gemini 2.0's MoE possible — followed by 40 days of round-the-clock training babysitting by a ~5-person rotation across Mountain View and Paris ([incident-management](../concepts/incident-management.md)).

## Notable quotes

- "Until I know the sum total of humanity's bleeding edge in this topic, I'm definitely not going to be able to further that bleeding edge." — Vlad Feinberg, ~13:34
- "There's an element of making decisions around how we allocate these resources that will always be something that needs to be attributable to a human... you can't hand off blame to AI. [LLMs] could review your contract for you... but they can't represent you in court because they can't be disbarred." — Vlad Feinberg, ~28:15
- "We all have agency over our future and we can start investing in skills that matter for tomorrow, today... Worrying about it is not going to help you." — Vlad Feinberg, ~29:30
- "Be the kind of coworker that people would want to see succeed." — Vlad Feinberg, ~59:54

## Connections

- [Stanford PhD, AI Researcher and Ex-Citadel Quant Shares His Experience](stanford-phd-ai-researcher-and-quant.md) — another view of the AI research career path and what research work is actually like.
- [OpenAI Codex Tech Lead On How His Career Grew And How He Uses Codex | Michael Bolin](openai-codex-tech-lead-on-how-his.md) — engineering inside a frontier lab; the applied side of the research/engineering spectrum Vlad describes.
- [OpenAI Eng & Dev Tools Founder: How Software Engineering Is Changing | Charlie Marsh](openai-eng-and-dev-tools-founder.md) — complementary take on which engineering skills stay valuable in the AI era.
- [Turing Award Winner: TPUs vs GPUs vs CPUs, Computer Architecture, RISC vs CISC | David Patterson](turing-award-winner-tpu-vs-gpu-vs.md) — hardware/accelerator side of the same efficiency problems (MFU, quantization, inference co-design run on TPUs).
- [Turing Award Winner: Data Abstraction, Dijkstra, Distributed Systems | Barbara Liskov](turing-award-winner-data-abstraction.md) — the distributed-systems fundamentals Vlad says underpin frontier training and serving infrastructure.
