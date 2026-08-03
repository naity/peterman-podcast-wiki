---
type: concept
updated: 2026-08-03
sources: [turing-award-winner-early-ai-llm.md, turing-award-winner-postgres-disagreeing.md, aws-distinguished-eng-learnings-from.md, creator-of-ocaml-functional-programming.md, google-deepmind-pre-training-lead.md]
---

# Causality

The distinction between seeing and doing — between correlation, intervention, and counterfactual explanation — and why [Judea Pearl](../entities/judea-pearl.md) argues it is the thing missing from statistics, from most of machine learning, and from large language models. One episode carries almost all of this content, but it bears directly on claims made across the podcast's AI thread.

## What the guests say

### The ladder of causation

Pearl's framework, given first-hand in his 2026-07-27 interview ([episode](../sources/turing-award-winner-early-ai-llm.md)), has three rungs:

1. **Association** — "if you see X, what can you tell me about Y?" This is all of classical statistics, "Statistics 101 even to 808."
2. **Intervention** — what happens if I *force* X, rather than observe it. "The intervention is forcing you to do something that you're not inclined to do naturally." Normally this requires experiments; the do-calculus is the machinery for deciding when observational data plus a causal graph suffices.
3. **Counterfactual explanation** — retrospective reasoning from an outcome that did happen: "Given that I observe that I am 80 years old and I am still alive... what if I didn't smoke?" The hardest rung, requiring the most assumptions and different algebra.

The load-bearing claim is a limitation, not a taxonomy: "You cannot go from level I to level I plus 1 unless you have assumptions here." Higher-rung questions are not answerable from lower-rung data alone, no matter how much of it you have — which is why Pearl treats "more data" and "more compute" as non-answers to causal questions.

### Why probability alone fails

Pearl spent years believing probability captured all of human reasoning. What changed his mind was noticing that when domain experts drew their networks, "always the arrows went from what we believe to be cause into the effect. It never went the other way around" ([episode](../sources/turing-award-winner-early-ai-llm.md)). The property probability lacks is **invariance**: causal relations stay stable when you intervene on the system or transplant them into a new one; correlational ones don't. Disease→fever transfers; fever→disease doesn't. His illustration of what a purely equational reasoner concludes: that "fiddling around with the barometer will change the weather tomorrow."

The mathematical repair was to borrow directionality from computer science — the assignment operator, which unlike the equals sign is not symmetric: "You put the logic of assignment on top of the algebra, on top of physics, you get causal science."

### Bayesian networks: relevance as structure

The earlier half of the same lineage. Expert systems needed to combine uncertainty and logic could not; textbook probability could but was exponential. Pearl's move was to ask why humans manage anyway, and answer: because most facts are irrelevant to most queries — "the color of the eye of my uncle is irrelevant when I'm trying to find a diagnosis of a disease." Conditional independence encoded as a graph lets you read relevance off the structure without ever materializing the joint distribution, and with Azaria Paz he showed the axioms of conditional independence in probability are the same axioms as graph separation ([episode](../sources/turing-award-winner-early-ai-llm.md)).

### Where LLMs sit — and the disagreement this creates

Pearl's answer is subtler than the usual "LLMs only do correlation." He says they do not violate the hierarchy at all, because they are not looking at the world: "They're looking at interpreted data, data interpreted already by physicians and interpreters" ([episode](../sources/turing-award-winner-early-ai-llm.md)). A model trained on human writing inherits world models that humans already built at rungs 2 and 3, so it can *appear* to answer interventional and counterfactual questions while doing associational work over other people's causal reasoning — "it's taking the introspection that already was done and summarizing it."

Two consequences the wiki's other AI claims should be read against:

- **It predicts exactly Stonebraker's benchmark result.** Mike Stonebraker reported LLM text-to-SQL scoring ~85% on academic benchmarks and 0% on his real-world warehouse benchmark ([episode](../sources/turing-award-winner-postgres-disagreeing.md)). Pearl's account says why that should be expected rather than surprising: where humans have already published interpretation, the model is strong; where the data is idiosyncratic and nobody wrote the interpretation down, there is nothing to summarize.
- **It puts a ceiling on "the models will get there."** Vlad Feinberg's frontier-lab framing treats capability as a scaling and engineering problem and locates the durable human role in accountability rather than in reasoning ([episode](../sources/google-deepmind-pre-training-lead.md)). Pearl (2026-07-27) disagrees at the level of mechanism: scaling rung-1 competence does not produce rung-2 competence, so "I don't think so, but not without the element. They need to have some understanding of causality." His proposal, *causal AI*, is a hybrid — LLMs for finite-sample-to-distribution inference, causal machinery for intervention and counterfactuals.

The structural echo elsewhere in the podcast is Xavier Leroy's argument one week earlier that LLM output needs an external correctness apparatus, in his case machine-checkable proofs ([episode](../sources/creator-of-ocaml-functional-programming.md)). Leroy and Pearl want different apparatus for different failure modes — Leroy fears code that is wrong, Pearl fears conclusions that are unjustified — but both reject the position that better models alone close the gap.

### The practitioner's version

Nobody else on the podcast uses the vocabulary, but the problem recurs. Marc Brooker's account of learning from 3,000 incidents is fundamentally about not stopping at correlation — the discipline of establishing what actually caused an outage rather than what was merely present during it ([episode](../sources/aws-distinguished-eng-learnings-from.md), [incident-management](incident-management.md)). Pearl's rung-2/rung-3 distinction is the formal statement of why post-incident "what would have happened if we hadn't deployed?" is a genuinely harder question than "what was correlated with the outage?"

## Practical takeaways

- Before asking a model or a dataset a question, ask which rung it lives on. If it contains the words "if we had" or "if we force," observational data alone will not answer it ([Pearl](../sources/turing-award-winner-early-ai-llm.md)).
- Expect LLMs to be strongest exactly where humans have already published their interpretation, and weakest on proprietary, idiosyncratic data — and benchmark accordingly ([Pearl](../sources/turing-award-winner-early-ai-llm.md); [Stonebraker](../sources/turing-award-winner-postgres-disagreeing.md)).
- Treat direction as information. A model that fits equally well with the arrows reversed has not learned anything you can act on ([Pearl](../sources/turing-award-winner-early-ai-llm.md)).
- "How it summarizes is a mystery that no one has yet been able to decode" — from the man who formalized probabilistic reasoning, a caution against confident mechanistic stories about model behavior ([Pearl](../sources/turing-award-winner-early-ai-llm.md)).

## Related

- [ai-era-engineering](ai-era-engineering.md) — the profession-level version of the same argument
- [ai-coding-tools](ai-coding-tools.md) — where the LLM capability claims Pearl contests get made concretely
- [incident-management](incident-management.md) — root-cause analysis as applied causal inference
- [formal-verification](formal-verification.md) — the other external-correctness-apparatus proposal, from Leroy
- [Judea Pearl](../entities/judea-pearl.md) — the concept's originator; [Episode](../sources/turing-award-winner-early-ai-llm.md)
