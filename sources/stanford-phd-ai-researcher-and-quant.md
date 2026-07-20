---
type: source
updated: 2026-07-19
raw: ../raw/stanford-phd-ai-researcher-and-quant.md
guest: "Nimit Sohani"
guest_role: "Stanford PhD, AI researcher at Cartesia, ex-Citadel Securities quantitative researcher"
date: 2026-01-26
url: https://www.developing.dev/p/stanford-phd-ai-researcher-and-quant
---

# Stanford PhD, AI Researcher and Ex-Citadel Quant Shares His Experience

Nimit Sohani did his PhD at [Stanford](../entities/stanford.md) in Chris Ré's lab, went to Citadel Securities as a quantitative researcher after graduating (just before ChatGPT launched), then returned to AI by joining Cartesia — the voice AI startup founded by his labmates, including Mamba creator Albert Gu. The episode is a rare side-by-side comparison of the two most lucrative "math + computation" career tracks — quant finance and [AI research](../concepts/ai-era-engineering.md) — covering PhD value, quant firm culture and comp, voice AI competition with ElevenLabs, and state space models vs transformers.

## Key takeaways

- A PhD is rarely strictly required outside academia, but it opens doors in AI research and quant finance and shapes the role you get: engineering-heavy AI work (training/eval infra, data processing) doesn't need one, while "pie in the sky" architecture-design research benefits from it. Its core skill: 90% of research is finding the right problem — interesting, meaningful, convincing to others, and tractably scoped.
- Building research taste: keep abreast of the literature (skim abstracts constantly — his main feed is a curated X/Twitter follow list grown organically from Stanford contacts and lab authors), and mature gradually — start with small sub-problems extending existing methods before attempting wholly new ideas; skipping that maturation is "generally inadvisable."
- He chose quant after his PhD out of curiosity and risk aversion — a stable, lucrative option among the three "math + computation" careers (ML research, quant finance, quantum computing) — and, contrary to reputation, had great work-life balance at Citadel because trader schedules anchored around US market hours trickle down to the whole culture. He thinks quant now has better work-life balance than AI, where competitors gain edge by "outworking" each other.
- Quant work is diverse (alpha generation, monetization, risk, data analysis; hedge fund vs market maker; front vs back office), unified by strong math — stochastic calculus is the backbone, plus numerical optimization, numerical linear algebra, and increasingly deep learning; he coded mostly C++ with some Python.
- Quant [compensation](../concepts/compensation-and-equity.md) has no standardized levels like tech's IC bands; it's opaque and driven by firm/team/strategy performance and seniority. Top 1% in either field make "NBA player salaries." Non-competes with paid garden leave of six months to two years are the norm, decided by the company at departure.
- Finance is radically more secretive than tech — even within a firm, pods may unknowingly work on the same strategies because sharing is forbidden (partly to keep returns uncorrelated). Returning to tech, he was jarred that people "just tell you that for free."
- Quant job security is U-shaped in an unusual way: senior quants get expensive relative to market rate and can stop being "worth it" even when good, while cheaper early-career quants are safer; the culture is up-or-out with regular trimming of low performers — easiest to enforce where P&L makes performance unambiguous. Insider-trading workarounds (WhatsApp groups tipping friends) get people fired, sued, and jailed.
- His quant firm tier list: Rentech is the mythical gold standard; Jane Street, Citadel, Jump Trading, Hudson River are the well-regarded big names; elite smaller/secretive shops include TGS, XTX, and Radix.
- He left Citadel for Cartesia — a [startup](../concepts/startups-and-founding.md) founded by his Chris Ré-lab colleagues — for growth and to re-enter AI as it took off, deliberately taking risk after establishing financial stability. Cartesia builds voice AI (text-to-speech flagship, speech-to-text, voice agents), where main rival ElevenLabs had an ~18-month head start; Cartesia differentiates on latency, cost, and voice cloning, pushing toward end-to-end speech models instead of the lossy STT→LLM→TTS pipeline.
- Startups vs big labs: big labs have all the compute but are more prone to groupthink and averse to out-of-the-box ideas; startups can strategically "challenge the orthodoxy" — e.g., Albert Gu's Mamba disproving that sequence modeling was solved by transformer scaling, and Cartesia's H-Nets learning tokenization boundaries directly from raw characters.
- SSMs vs transformers: transformers' KV cache grows linearly with sequence length (a "database" that recalls everything); SSMs compress context into a fixed-size state (like a human brain). Pure SSMs lag on recall-heavy tasks, so hybrids interleaving SSM and transformer layers are the text-modality cutting edge (Nvidia, recent Qwen models) — but for audio, where adjacent frames are highly redundant, SSM compression is "almost a free lunch," improving both quality and inference cost.
- On lab strategy, he's skeptical of both research-only startups (all-or-nothing against resource-rich big labs) and product-only wrapper companies (no moat — base model improvements made many obsolete); the durable position is the intersection, where a real product drives research and model control protects the product.
- Advice for SWEs wanting AI research: build fundamentals (coding, math intuition, reading tons of papers) until opportunities come to you; at big companies you get siloed, so a master's credential or moving to a flexible startup helps — Cartesia has successfully converted SWEs to research roles internally, but you need evidence of the skill set either way.
- His biggest [regret](../concepts/regrets-and-advice.md) is meta: he regrets the time spent regretting decisions that didn't matter. Advice to his younger self: focus on deep technical skills and don't spread yourself thin — "a simple recipe that's very hard to follow," like diet and exercise.

## Notable quotes

- "I would say 90% of the battle in research is actually finding the right problems." — Nimit, ~00:05
- "Even the firms that have a reputation for being more open are actually quite secretive versus in tech... It was like, wow, you're just going to tell me that for free." — Nimit, ~00:22
- "SSMs are kind of like a brain... whereas transformers are more like a database where you can kind of recall anything in the context." — Nimit, ~00:44
- "If your fundamentals are good enough, at some point the opportunities will just come to you rather than the other way around." — Nimit, ~00:53

## Connections

- [Google DeepMind Pre-Training Lead: How To Get a Job at a Frontier Lab | Vlad Feinberg](google-deepmind-pre-training-lead.md) — directly complementary advice on breaking into AI research/frontier labs.
- [OpenAI Eng & Dev Tools Founder: How Software Engineering Is Changing | Charlie Marsh](openai-eng-and-dev-tools-founder.md) — another researcher/engineer at the AI startup vs big lab boundary discussing how the field is shifting.
- [OpenAI Codex Tech Lead On How His Career Grew And How He Uses Codex | Michael Bolin](openai-codex-tech-lead-on-how-his.md) — the big-lab counterpart perspective on AI product-plus-research work.
- [Robinhood SWE Turned $1B+ Founder on Non-Linear Careers, Being Jaded About Promos, Startup Learnings](quitting-robinhood-and-raising-35m.md) — shared theme of leaving a lucrative, stable track to take startup risk after building a cushion.
- [MIT Complexity Theorist: Why You Can Do Better Than 'Optimal' On Leetcode & SAT | Ryan Williams](mit-complexity-theorist-on-leetcode.md) — shared thread of deep math fundamentals and research problem selection as career leverage.
