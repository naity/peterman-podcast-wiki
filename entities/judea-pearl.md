---
type: entity
entity_kind: person
updated: 2026-08-03
sources: [turing-award-winner-early-ai-llm.md]
---

# Judea Pearl

Turing Award winner (2011) and longtime [UCLA](ucla.md) computer science professor, responsible for two distinct revolutions in AI: Bayesian networks, which made probabilistic reasoning tractable and gave 1980s expert systems a statistical foundation, and the causal calculus (the do-operator, the ladder of causation) that he argues probability by itself can never express.

## Career arc

Educated in Mandate Palestine by German professors who had fled Hitler and who taught science historically — as the work of human actors rather than a catalogue of techniques — which he credits with making him feel like a participant in science rather than an observer ([episode](../sources/turing-award-winner-early-ai-llm.md)). Israeli military service, then electrical engineering and physics at the Technion, where by his own account he was "third or fourth. Always never match the geniuses." He then studied at Brooklyn Polytechnic while working at RCA's David Sarnoff Research Laboratory in Princeton on superconducting memory, where he discovered the permanent vortices in thin superconducting films now known as the Pearl vortex — before semiconductors killed the technology for a reason he concedes was obvious in advance ("who is going to trust memory to battery failure?").

He joined UCLA around 1969–70 as its computer science department was forming, hired to teach memory hardware, and drifted through pattern recognition and image compression into AI by way of game playing. There he proved alpha-beta pruning mathematically optimal — a result that surprised Donald Knuth — then "got sick and tired of search" and turned to reasoning under uncertainty, which produced Bayesian networks (with Azaria Paz of the Technion on the graphoid axioms) and, later, causality ([episode](../sources/turing-award-winner-early-ai-llm.md)).

## Key views & advice

- **Probability is not enough.** He believed for years that probability captured all of human reasoning and changed his mind on the evidence that experts always draw arrows from cause to effect, never the reverse. The property probability lacks is invariance under intervention; the repair was to put computer science's directional assignment operator on top of algebra ([causality](../concepts/causality.md), [episode](../sources/turing-award-winner-early-ai-llm.md)).
- **The ladder of causation.** Association, intervention, counterfactual explanation — and you cannot climb a rung on lower-rung data alone: "You cannot go from level I to level I plus 1 unless you have assumptions here."
- **On LLMs, a precise and non-obvious critique.** They do not violate his hierarchy, because they never see raw environmental data — they consume text that humans already interpreted causally, so they summarize rung-2 and rung-3 world models while operating at rung 1 ([ai-era-engineering](../concepts/ai-era-engineering.md), [episode](../sources/turing-award-winner-early-ai-llm.md)).
- **On AGI.** Achievable eventually; not by scaling language models alone — "they need to have some understanding of causality." His proposal is a hybrid he calls causal AI. He cites Geoffrey Hinton's "we are on a dead end" against the labs promising AGI in three to five years, and demands that consciousness claims come with a stated test.
- **Rebel, including against him.** "The scientific community and academic community is the most dogmatic, conservative, anti-progress that we have invented" — aimed at statistics and economics, which he says are "still thinking like 100 years ago" about causation ([academia-vs-industry](../concepts/academia-vs-industry.md)).
- **World models over stored answers.** "You don't store the questions and the answers explicitly. You derive them when you need them from a very parsimonious code" — the same instinct behind his preference for physics over chemistry and his admiration for Descartes ([regrets-and-advice](../concepts/regrets-and-advice.md)).

## Related

- [Episode: Turing Award Winner: Early AI, LLM Predictions, Causality](../sources/turing-award-winner-early-ai-llm.md) — his interview
- [UCLA](ucla.md) — his institution for over fifty years, and the host's alma mater
- [causality](../concepts/causality.md) — the concept he created and the page he anchors
- [Roberto Ierusalimschy](roberto-ierusalimschy.md) — the following week's guest; the other academic who refuses to forecast AI, by declining to name a mechanism at all
- [Xavier Leroy](xavier-leroy.md) — the other 2026 academic-legend episode arguing LLM output needs an external correctness apparatus (proofs, in Leroy's case)
- [Mike Stonebraker](mike-stonebraker.md) — the empirical version of Pearl's skepticism, via text-to-SQL benchmarks that collapse on real data
- [Avi Wigderson](avi-wigderson.md), [Ryan Williams](ryan-williams.md) — fellow theorists whose central results are also statements about what is impossible or provably optimal
