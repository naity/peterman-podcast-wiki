---
type: raw-transcript
slug: turing-award-winner-early-ai-llm
title: "Turing Award Winner: Early AI, LLM Predictions, Causality | Judea Pearl"
guest: "Judea Pearl"
date: 2026-07-27
url: https://www.developing.dev/p/turing-award-winner-early-ai-llm
fetched: 2026-08-03
complete: false
capture: structured
capture_note: >
  The fetch pipeline returned a detailed section-by-section capture of the full
  episode (all 10 timestamped sections, 00:54 through the 01:26:30 sign-off)
  rather than a word-for-word transcript. Every section is covered and the
  guest's specific claims, examples and timestamped quotes below are as
  reported by the fetch; connective narration between quotes is condensed
  rather than verbatim. No section of the episode is missing. Three fetch
  passes were used (whole-episode pass, 46:28-end deep pass, 00:54-46:28 deep
  pass); no adversarial prompting was used.
---

# Turing Award Winner: Early AI, LLM Predictions, Causality | Judea Pearl

**Guest:** Judea Pearl (Turing Award winner, 2011; professor of computer science, UCLA; director of the Cognitive Systems Laboratory)
**Host:** Ryan Peterman
**Publish Date:** Jul 27, 2026
**Runtime:** ~1:26:30

## Host's Intro (condensed)

Peterman says Pearl's name kept coming up among the other professors he interviewed, so he went to UCLA to talk to him. He flags the anecdotes he found most compelling: Pearl's lifelong passion for physics, his proof that alpha-beta pruning is mathematically optimal (a result that surprised Donald Knuth), and the eureka moment behind Bayesian networks. Peterman's overall impression is of a scientist whose passion for science is undimmed.

## Timestamps

- 00:54 - How he got into AI
- 11:17 - Greatest scientist of all time
- 20:15 - What people thought of AI in the 80s
- 26:23 - Entering academia and researching AI
- 34:52 - The invention of Bayesian networks
- 46:28 - Pioneering work in causality
- 55:38 - The causal hierarchy
- 59:34 - LLMs and predictions
- 01:20:12 - A restless mind pays
- 01:24:36 - Advice for his younger self

## Section capture

### 00:54 — How he got into AI

Pearl traces his path back to his high school education in Mandate Palestine (pre-1948). His teachers were German professors who had fled Hitler — from Heidelberg, Berlin and similar universities — and they taught science historically and chronologically, from the standpoint of the human actors who discovered it, rather than as a set of recipes.

> [03:37] "That's the way to teach science, not the recipe of algorithms and techniques, but ... from the viewpoint of the human actor."

He says this gave his cohort the sense of being participants in science rather than observers, and with it a habit of assertiveness. He tells a childhood story from around age ten: the whole class insisted on a wrong figure for the number of dunams in a square kilometer, and he held out for the correct one.

> [06:50] "I screamed and said, no, it's a thousand [dunams]."

After Israeli military service (assigned to a farming/kibbutz unit), he studied electrical engineering and physics at the Technion. He was strong but not the standout.

> [09:34] "I was third or fourth. Always never match the geniuses."

What drew him to physics was its predictive power from first principles — Maxwell deriving electromagnetic waves from his chair.

> [10:13] "Sitting on your chair, you can predict things in physics. Like Maxwell, who sat on his chair and said, 'That looks like a wave equation...'"

### 11:17 — Greatest scientist of all time

Pearl names René Descartes as the greatest mathematician who ever lived, for turning geometry into algebra. He says studying coordinate geometry gave him a literal fever: he could not get over the fact that every geometric construction could be done algebraically.

> [12:08] "Here you have two different languages, language of geometry and the language of algebra. And they are the same thing."

He describes this — two unrelated-looking languages capturing the same reality — as the pattern that excited him for the rest of his career, and that later recurred in physics and in his own work connecting probability theory to graph theory.

### ~13:55–20:15 — RCA, superconductivity, and the "Pearl vortex"

After the Technion he studied at Brooklyn Polytechnic while working at RCA's David Sarnoff Research Laboratory in Princeton, New Jersey, on superconducting memory. He discovered permanent eddy currents (vortices) in thin superconducting films — now called the Pearl vortex — and won a prize for it.

> [15:36] "I discovered new phenomena there, and I got a prize. And it even has a name. It's called Pearl vortex."

He jokes that this was his footstep into immortality. Superconducting memory lost to semiconductors, and he is candid that the failure mode was obvious in hindsight.

> [18:10] "Who is going to trust memory to battery failure? What if you lose a battery? It was obvious it will never work."

### 20:15 — What people thought of AI in the 80s

Pearl says that even on primitive 1960s hardware, nobody in AI doubted the goal was achievable; the debate was only about method and timing.

> [18:59] "Everybody understood in AI as an inspiration ... That was not the question. The question was only how and when, but not whether."

Researchers in the 1960s predicted human-level machine intelligence within about twenty years — i.e. by roughly 1985 — which proved wildly optimistic. Asked about today's optimism, he says he is skeptical that LLM techniques alone get to AGI, while remaining confident that AGI is eventually achievable.

### 26:23 — Entering academia and researching AI

He joined UCLA around 1969–70, when the computer science department was being formed, hired initially to teach computer memory and hardware. He drifted toward pattern recognition and image compression (Fourier and Hadamard transforms), then into AI via game playing.

> [27:54] "At that time, AI was game playing, machine playing of chess and checkers and the puzzles, like the eight puzzles, ruby cubes, things like that."

What attracted him was the interplay between mathematical analysis and actual performance, and the balance between fast intuition and slow deliberate search — the Kahneman *Thinking, Fast and Slow* split, applied to heuristics. He proved mathematically that alpha-beta pruning is optimal.

> [32:34] "I proved that alpha-beta is optimal. Yes, mathematically ... Even Knuth was surprised that one can prove the optimality on alpha beta."

> [33:24] "I did mathematical work on the tradeoff between search and reasoning until I got sick and tired of search."

### 34:52 — The invention of Bayesian networks

The next problem was expert systems. Early systems tried to encode expert knowledge as logical rules, but real expertise is uncertain, and logic has nothing to say about combining uncertainties.

> [36:33] "Logic doesn't tell you how to combine uncertainties. Probability does, but not logic."

Textbook probability was intractable — the joint distribution blows up exponentially. Pearl's reaction was that humans nevertheless do this well, so the textbook route must not be what humans use. His insight was conditional independence: most facts are simply irrelevant to a given query.

> [38:43] "Not every fact in life is relevant to any query. Okay? The color of the eye of my uncle is irrelevant when I'm trying to find a diagnosis of a disease."

He found that a graph could encode exactly those independence relations without ever materializing the probability table: given the graph you can read off what is relevant to what. Working with Azaria Paz (Technion) he developed graphoid theory, and found that the axioms are shared between the two fields.

> [41:36] "The axioms of conditional probability, or conditional independence in probability theory, are the same axiom that you have in graph separation."

> [42:25] "I really know the excitement we had in the 1970s when we discovered all these connections between two seemingly unrelated perspectives on science, probability theory, and graph theory."

### 46:28 — Pioneering work in causality

Pearl says he initially believed probability captured all of human reasoning, and was wrong. The tell was that when experts drew their networks, the arrows always ran from cause to effect.

> [47:42] "Always the arrows went from what we believe to be cause into the effect. It never went the other way around."

The property probability lacks is *invariance*: causal relations stay stable across interventions and modifications of the system, while purely correlational ones do not. Disease→fever transfers; the reverse direction does not. A machine reasoning only with symmetric equations will happily conclude that fiddling with the instrument changes the world.

> [52:55] "Fiddling around with the barometer will change the weather tomorrow."

The fix required new mathematics: algebra plus the *assignment* operation from computer science, which is directional in a way the equality sign is not.

> [54:18] "You put the logic of assignment on top of the algebra, on top of physics, you get causal science."

### 55:38 — The causal hierarchy

Pearl lays out his three-level ladder:

**Level 1 — Association.** Passive observation; classical statistics.
> [55:41] "If you see X, what can you tell me about Y?"
He notes this is what is taught from Statistics 101 all the way up.

**Level 2 — Intervention (do-calculus).** What happens if I *force* X?
> [57:16] "The intervention is forcing you to do something that you're not inclined to do naturally."
Answering these generally requires experiments.

**Level 3 — Counterfactuals / explanation.** Retrospective reasoning from an observed outcome to what would have happened otherwise — the hardest level, needing the most assumptions and different algebraic tools.
> [58:42] "Given that I observe that I am 80 years old and I am still alive ... what if I didn't smoke?"

The load-bearing constraint:
> [59:36] "You cannot go from level I to level I plus 1 unless you have assumptions here."

### 59:34 — LLMs and predictions

Asked where LLMs sit on the ladder, Pearl gives a subtle answer: they do not violate the hierarchy, because they are not consuming raw data from the environment at all. They are consuming text that human beings already interpreted causally.

> [01:01:04] "They are not looking directly at the data in the environment. They're looking at interpreted data, data interpreted already by physicians and interpreters."

So an LLM can appear to answer level-2 and level-3 questions while doing level-1 work over an assumption-laden world model authored by humans.

> [01:02:22] "It's not really doing the introspection. It's taking the introspection that already was done and summarizing it. How it summarizes is a mystery that no one has yet been able to decode."

On whether LLMs alone reach AGI:
> [01:02:54] "I don't think so, but not without the element. They need to have some understanding of causality."

His proposed path is a hybrid he calls causal AI:
> [01:10:35] "Both the ability of LLMs to go from finite samples to property of distribution ... plus ability to reason in higher levels of the ladder ... I call causal AI."

He also raises how babies learn — through built-in curiosity and a drive to control their environment — as a model for what is missing, while flagging the obvious danger: a robot with that drive treats us as part of the environment it wants to control.

On timelines and on the AGI-in-three-to-five-years claims, he is unconvinced, and cites Hinton's more pessimistic read:
> [01:14:05] "[Hinton] said, no, we are on a dead end. ... I don't find the consensus here in terms of the capabilities of LLMs."

On claims that LLMs are conscious, he demands the same rigor he demands of himself, and says he does not even read the anthropomorphic marketing:
> [01:14:20] "Define what you mean by consciousness. What is the Turing Test for consciousness?"
> [01:14:51] "I don't buy this, and I don't read them even."

### 01:20:12 — A restless mind pays

Pearl argues that rebellion is the engine of scientific progress, and that the institutions nominally built for progress are the worst offenders.

> [01:20:23] "The scientific community and academic community is the most dogmatic, conservative, anti-progress that we have invented."

> [01:21:31] "I can see what difficulty the theory and the science of cause and effect are facing today in getting ... penetrating the thinking of disciplines like statistics, like economics."

He says those fields are still thinking as they did a century ago, and tells students explicitly to rebel:
> [01:21:31] "Don't take your professor's word as authority. Rebel against your professors. I rebelled against my professors, and I want to see my students rebel against me."

And he means it in both directions:
> [01:22:44] "Several students told me, 'You don't know anything about AI.' After a while, I told them, 'You're right.'"

> [01:22:54] "My work was controversial or mischievous before it was accepted."

He mentions holding correspondence with eminent philosophers of the era that shows how badly great minds can be trapped by a few basic molds, and says he may publish it someday.

### 01:24:36 — Advice for his younger self

He says he might have spent more time on chemistry, which he avoided because it demanded memorization rather than derivation.

> [01:24:44] "Maybe I should have spent more time on learning chemistry. I hated chemistry because it required so much memory."

> [01:25:15] "It's a choice one has to make ... Some people have the greatness of mind to be polyglots. I admire them."

He closes on the principle that unifies his taste in physics, his advice, and his research program — the superiority of a compact world model over stored answers:

> [01:26:21] "You don't store the questions and the answers explicitly. You derive them when you need them from a very parsimonious code."
