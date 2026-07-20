---
type: source
updated: 2026-07-19
raw: ../raw/dropboxs-former-most-senior-eng-building.md
guest: "James Cowling"
guest_role: "CTO and co-founder of Convex, former most senior engineer at Dropbox, MIT PhD in distributed systems"
date: 2026-05-25
url: https://www.developing.dev/p/dropboxs-former-most-senior-eng-building
---

# Dropbox's Former Most Senior Eng: Building Great Systems and Advice for the AI Era | James Cowling

[James Cowling](../entities/james-cowling.md) is the CTO of Convex and was previously the most senior engineer at [Dropbox](../entities/dropbox.md), where he led Magic Pocket — the multi-exabyte storage system that migrated Dropbox off [AWS](../entities/aws.md) S3 in what was then the largest data migration in history. The episode is a masterclass in [systems design](../concepts/systems-design.md) (erasure coding, congestion collapse, multi-homing) fused with unusually direct opinions on [career growth](../concepts/career-growth.md): why simplicity beats complexity, why promo-driven engineering angers him, and why you shouldn't lead by example.

## Key takeaways

- Cowling's MIT PhD work (Granola, on distributed transaction coordination with "independent transactions" avoiding two-phase commit) predated and was cited by Google's Spanner paper; his Viewstamped Replication Revisited paper influenced companies like TigerBeetle. His core performance insight: what matters at scale is not raw hardware speed but eliminating points of coordination.
- On PhDs: a PhD is training to be a researcher, not more college — most aspiring engineers shouldn't do one. Its real value is the formative experience of facing a problem no one on earth (not even your advisor) can answer, which teaches you to sit with uncertainty; he feels lucky he went through it before LLMs existed as a crutch.
- Dropbox's Magic Pocket stored data at a modeled ~24 nines of durability using erasure coding (~27 fragments spread across racks, power feeds, drive manufacturers and regions), with reads racing e.g. 9 fragments and completing on the first 6 — making erasure-coded reads faster than unreplicated ones.
- Why Dropbox left S3: strategic control of the file system, huge cost savings pre-IPO, first-at-scale use of Shingled Magnetic Recording disks, and a tight understanding of its own workload (hot-then-decaying access patterns split across an access-efficient warm cluster and a bulk-written cold cluster) that a general-purpose service like S3 could not match. He still tells almost everyone else not to build their own [infrastructure](../concepts/distributed-systems.md): "most people should focus on their applications."
- The stack evolved Python → Go → Rust (pre-GA for both Go and Rust): Go's runtime memory unpredictability caused OOMs that looked like disk failures and could 7x load into congestion collapse (e.g. when a band released an album on Dropbox), so storage nodes were rewritten in Rust with the filesystem removed entirely, addressing disks directly via draft ZBC specs ("Discotech").
- Migration discipline: a "dark launch" double-writing to S3 and Magic Pocket, with a founder-mandated six months of zero incidents before deleting anything from S3 — and when one bug slipped to production, Cowling voluntarily reset the launch clock at a cost of double-digit millions, and leadership thanked him. Peak migration bandwidth hit 764 Gbps out of AWS.
- Simplicity is the hardest and most scalable property: Magic Pocket's block index was "just" 1,000 MySQL nodes, which academics scoffed at, but it was trivially walkable for continuous validation — "It's not about getting a system to work. It's what do you do when it doesn't work." He warns that agentic/AI development is bad at simplicity, which "is still the domain of human beings for now."
- On [promotions](../concepts/promotions.md) incentivizing complexity: it "almost angers" him and is partly why he founded his own company; teams should be named and oriented around missions ("Storage team"), not systems ("Magic Pocket team"), so no one's identity depends on defending an obsolete system — and one of his most impactful Dropbox jobs was shutting down projects that inertia kept alive.
- Career advice: pick working with the best people over 20% more pay; stay in jobs at least ~3 years or you never see the consequences of your decisions ("like playing a basketball game and leaving before the game's over"); don't go into [management](../concepts/management.md) too early (ideally reach staff first) or you'll lack the technical depth to influence strategy later; wanting to be a manager too much is a red flag.
- Don't lead by example — it's passive. When he jumped on every page to model ownership, his team concluded that was "James's job"; real [leadership](../concepts/influence-and-leadership.md) is explicitly teaching, delegating, and reframing on-call as empowering ownership. Organizational conflict is usually misalignment on "why," not "how" — demand 100% alignment on why, then trust the team.

## Notable quotes

- "Simple systems are way harder to design than complex systems. Simplicity is so hard... If after the fact people think it's obvious, then you really nailed it." — James (42:49)
- "It's not about getting a system to work. It's what do you do when it doesn't work." — James (42:19)
- "If you have two choices — making 20% more money now or working with the best people in the world — just be around the best people because that's going to set you on the ship to success." — James (1:02:20)
- "The luxury is you don't get up and have to do a terrible job. You get up and go to a place where you like your coworkers, and you solve cool problems, and you go home and feel proud of yourself." — James (1:07:49)

## Connections

- [AWS Distinguished Eng: Learnings From 3000 Incidents And How Engineering Is Changing | Marc Brooker](aws-distinguished-eng-learnings-from.md) — the other side of the S3 story: AWS-scale systems, incident management and how engineering is changing.
- [Turing Award Winner: Data Abstraction, Dijkstra, Distributed Systems | Barbara Liskov](turing-award-winner-data-abstraction.md) — Cowling's PhD was in Liskov's field (his Viewstamped Replication Revisited revisits Liskov's protocol) and both center on abstraction and distributed systems.
- [Turing Award Winner On Thinking Clearly, Paxos vs Raft, Working with Dijkstra | Leslie Lamport](turing-award-winner-on-working-with.md) — Cowling discusses Paxos/Raft/Viewstamped Replication equivalence; Lamport invented Paxos.
- [Distinguished Eng On Stack Ranking, Competing with Bezos, Regrets | Bryan Cantrill](distinguished-eng-on-stack-ranking.md) — kindred strong opinions on engineering culture, incentives and doing the right thing over promo games.
- [OpenAI Eng & Dev Tools Founder: How Software Engineering Is Changing | Charlie Marsh](openai-eng-and-dev-tools-founder.md) — fellow infrastructure-minded founder discussing how AI is changing engineering practice.
