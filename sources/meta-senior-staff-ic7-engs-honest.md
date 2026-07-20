---
type: source
updated: 2026-07-19
raw: ../raw/meta-senior-staff-ic7-engs-honest.md
guest: "Igor"
guest_role: "Senior staff engineer (IC7/L7) at Meta, Google, and Cruise; 14.5 years at Google"
date: 2026-01-23
url: https://www.developing.dev/p/meta-senior-staff-ic7-engs-honest
---

# Meta Senior Staff (IC7) Eng's Honest Demotion Story

Igor spent 14.5 years at [Google](../entities/google.md) rising from L3 to senior staff (L7), then went to Cruise, then joined [Meta](../entities/meta.md) as an E7 — where after 14 months he concluded he had only ramped to roughly E6 performance and, more importantly, that he simply didn't enjoy the E7 job. Meta had no process to demote him at his request, so he boomeranged back to Google, deliberately negotiating a downlevel to L6 with a large [compensation](../concepts/compensation-and-equity.md) cut. It's a strikingly honest counterpoint to the show's usual [promotion](../concepts/promotions.md) stories: a senior engineer voluntarily stepping down because he loves coding, debugging, and [mentoring](../concepts/mentorship-and-sponsorship.md) more than meetings and design docs.

## Key takeaways

- Joining a big company at senior staff means racing an internal clock: in the [PSC](../concepts/calibrations-and-ratings.md) you're calibrated against tenured E7s, and with Meta's Amazon-style "cut the bottom 10%" [layoffs](../concepts/layoffs.md), you have roughly a year to match old-timers who deeply know the code, infra, surrounding teams, and people. Igor's model of ramping: you effectively start below an intern and re-climb every level (E3→E4→E5...) internally; in 14 months he generously self-assessed reaching ~E6, not E7.
- The deeper reason he wanted a demotion wasn't just ramp-up: he discovered he loves E5/E6 work — coding, debugging, designing, mentoring juniors — while senior staff is a leader role of meetings and design docs that "touches much less code."
- Meta (per HR) has no process for dropping a level within the same job category (they can convert titles, e.g. director→IC, but not E7→E6), so his request was simply refused; he suspects escalating to a VP might have worked but chose the "easy way out" — a recruiter who kept pinging him about returning to Google.
- Why the Meta ramp failed where Cruise succeeded: Cruise was smaller with less infrastructure to learn and uncrowded scope you could just claim; Meta felt "crowded," with too many senior ICs competing for scope in his org. Meta also doesn't know how to onboard senior external hires because nearly all its senior people grew up internally; neither he nor his managers had a recipe.
- His onboarding [regret](../concepts/regrets-and-advice.md): he spent too much time reading docs building foundational knowledge instead of getting hands dirty and learning by building in parallel. His last Meta project — estimated at two weeks — ballooned in complexity, and even finished it would never justify an E7 level.
- [Meta vs Google culture](../concepts/big-tech-culture.md): Meta sets deliberately aggressive, arbitrary deadlines with constant leadership status updates; deadlines slip and "everybody is fine with that," so after a few cycles people learn the pressure is artificial and go home at 5pm — "like elementary school, where the teacher is yelling but kids are still playing." Google (at least 10 years ago) applied pressure only in genuinely exceptional cases.
- Google had no process for boomeranging at a *lower* level either, but made it work; he had to reassure the recruiter he'd genuinely accept the lower comp. Amusingly, returning as L7 would have required no interview, but returning as L6 nearly required a coding interview ("who knows if you wrote code while you were out") — he got an exception. No re-interview after 3.5 years away; he picked a team via conversations with hiring managers, engineers, and the skip manager.
- On transparency: he can share because he's privileged — no work visa dependency, spouse's health insurance, kids through college, no mortgage, can afford not to work for years. His advice to others: don't post about your work challenges unless you're equally safe.
- Best quality-of-life level in his view: senior engineer (E5/L5) — shielded from upward reporting by the TL and managers, still doing the enjoyable work. Also: below-senior engineers can't actually see what principal-level life is like, so people chase promos blind. His marathon line to peers pressuring him to try E7 elsewhere: "I'm capable of running a marathon, but I don't like running."
- On [imposter syndrome](../concepts/imposter-syndrome.md): comparing yourself to a *group* of peers is a mistake — one is great at presenting, another at leading — you're comparing yourself against a composite team no individual matches. "I'm sure Elon Musk has imposter syndrome."
- His L7 promo project at Google: porting ads' ML training infrastructure (a 10-year-polished CPU-based online-training system, pre-TensorFlow-era rigor) to brand-new TPUs — starting as a two-person exploratory prototype, needing credibility with TPU, compiler, and TensorFlow teams, ordering expensive chips 18 months ahead of delivery. Testing trick: strip all computation from models to simulate an infinitely fast TPU and hunt bottlenecks. War story: data on spinning disks means you need disks for *throughput*, not storage — cheap but ungettable, like COVID toilet paper. Ads under-ordered chips conservatively because a mature business must actually make money, unlike today's LLM buildouts; TPUs' specialization made sparse embedding lookups painful.
- Mentorship story: an intern he hosted as an ~L4 later converted and became the manager of the very team he interned on — "don't underestimate your interns."
- His disillusionment: young-idealist Igor joined Google for its values; the Atlanta office shutdown (a few hundred people cut because one senior VP sponsor pulled out and nobody would take the headcount) taught him "at the end of the day, I'm just a cell in the spreadsheet" — years before post-COVID layoffs normalized this.
- Advice to younger self: ask whether your company really benefits from what you're building — he worked on projects that leadership later killed for the exact pointlessness he'd already sensed. Escape hatch depends on company: switching projects was fluid at Google and Meta, near-impossible at Intel and (reputedly) IBM.

## Notable quotes

- "I'm capable of running a marathon, but I don't like running a marathon. I don't like running. Why would I do that?" — Igor, ~00:30
- "It almost feels like an elementary school, like where the teacher is yelling but kids are still playing... if you constantly put pressure on your people, it just doesn't work anymore." — Igor, ~00:18
- "You feel like, yeah, at the end of the day, I'm just a cell in the spreadsheet." — Igor, ~00:45
- "Don't underestimate your interns. They can be really, really good." — Igor, ~00:43

## Connections

- [Airbnb Staff Eng on How To Not Get Stuck at Senior and Untold Rules of Calibrations](airbnb-staff-eng-on-how-to-not-get.md) — the calibration/ratings machinery Igor was judged by, from the opposite (promo-seeking) direction.
- [Meta Hiring Lead On Behind The Scenes of Senior+ Eng Hiring](meta-hiring-lead-on-behind-the-scenes.md) — how Meta hires the senior external ICs whose onboarding Igor found broken.
- [Honest Big Tech Layoff Story After 25 Years](laid-off-from-big-tech-after-25-years.md) — companion honest career-setback episode from the same early-2026 run; both discuss layoff-era pressure and stepping off the ladder.
- [Instagram Senior Staff Eng (IC7) On 3 Promos Through Redefining Expectations (Career Story)](instagram-senior-staff-eng-ic7-on.md) — contrasting IC7 story: succeeding and thriving at the level Igor chose to leave.
- [Turing Award Winner: TPUs vs GPUs vs CPUs, Computer Architecture, RISC vs CISC | David Patterson](turing-award-winner-tpu-vs-gpu-vs.md) — Patterson worked on the TPU itself; Igor built Google ads' training infrastructure on those first-generation TPUs.
