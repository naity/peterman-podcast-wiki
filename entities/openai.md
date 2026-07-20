---
type: entity
entity_kind: org
updated: 2026-07-19
sources: [harvard-professor-cs50-what-matters.md, meta-hiring-lead-on-behind-the-scenes.md, meta-senior-manager-m2-on-manager.md, openai-and-meta-distinguished-engineer.md, openai-codex-tech-lead-on-how-his.md, openai-eng-and-dev-tools-founder.md, the-creator-of-kubernetes-on-building.md]
---

# OpenAI

OpenAI appears in seven episodes as the frontier lab that senior Meta engineers and dev-tools founders migrate to, and as the maker of Codex — the direct competitor to Anthropic's Claude Code in the show's recurring AI-coding-tools thread.

## What the episodes reveal

- **Why senior people join.** Michael Bolin (ex-Meta E9) joined because at Meta he was building LLM dev tools on Llama 2 while users asked "why isn't this GPT-4?" — he wanted the best model, proximity to the researchers who make it, Meta-E8/E9-caliber colleagues, and consumer-scale reach; he compares 2024 OpenAI to joining [Google](google.md) in 2000 ([Codex tech lead](../sources/openai-codex-tech-lead-on-how-his.md)). Philip Su (Meta IC9) joined before the major growth phase ([Philip Su](../sources/openai-and-meta-distinguished-engineer.md)); Charlie Marsh arrived via acquisition when OpenAI bought Astral (Ruff, uv, Ty) ([Charlie Marsh](../sources/openai-eng-and-dev-tools-founder.md)).
- **Culture: research-led.** Bolin's crisp formulation of where power sits: "If the model weren't very good, it wouldn't really matter what we did on the harness" ([Codex tech lead](../sources/openai-codex-tech-lead-on-how-his.md)).
- **Codex.** The CLI launched rushed in April 2025 (10–20k GitHub stars in ~2 weeks); Codex Web launched with ~7 engineers but was "ahead of its time" — local agents had stronger product-market fit; the August 2025 confluence (GPT-5, new TUI, open-weights support, VS Code extension) produced "vertical line" growth past 1M users. The CLI is open source largely for trust — an agent running on your machine should be inspectable ([Codex tech lead](../sources/openai-codex-tech-lead-on-how-his.md)). Bolin writes 80–90% of his code with the model but hand-writes the security-critical sandboxing code ([same](../sources/openai-codex-tech-lead-on-how-his.md)).
- **Hiring and interviews.** OpenAI's "Feel the AGI" value wants genuine optimism about what AI can do — interviewers listen for it ([Meta hiring lead](../sources/meta-hiring-lead-on-behind-the-scenes.md)). Stefan Mai adds that OpenAI/Anthropic loops notoriously reuse question areas and their behavioral rounds want raw technical achievement — the classic staff-engineer "I wrote seven docs and aligned six teams" story lands poorly ([Stefan Mai](../sources/meta-senior-manager-m2-on-manager.md)).
- **Elsewhere in the ecosystem.** OpenAI ran 7,500-node Kubernetes clusters for training, stress-testing a system designed for ~100 nodes ([Kubernetes creator](../sources/the-creator-of-kubernetes-on-building.md)); Harvard's CS50 built its sanctioned CS50.ai tutor on OpenAI APIs — deliberately "less helpful" than Copilot, which would autocomplete an entire problem set from a filename ([David Malan](../sources/harvard-professor-cs50-what-matters.md)).

## People

- [Michael Bolin](michael-bolin.md) — Codex CLI tech lead; ex-[Meta](meta.md) Distinguished Engineer
- [Philip Su](philip-su.md) — Distinguished Engineer, ex-Meta IC9 and [Microsoft](microsoft.md)
- [Charlie Marsh](charlie-marsh.md) — founder of Astral, acquired by OpenAI

## Related

- [ai-coding-tools](../concepts/ai-coding-tools.md), [ai-era-engineering](../concepts/ai-era-engineering.md)
- [developer-tools](../concepts/developer-tools.md) — the Astral/Codex lineage
- [Anthropic](anthropic.md) — the rival lab and Claude Code
- [hiring-and-interviews](../concepts/hiring-and-interviews.md) — "Feel the AGI"
