---
type: entity
entity_kind: person
updated: 2026-07-19
sources: [dropboxs-former-most-senior-eng-building.md]
---

# James Cowling

Co-founder and CTO of Convex, formerly [Dropbox](dropbox.md)'s most senior engineer and an [MIT](mit.md) PhD in [distributed systems](../concepts/distributed-systems.md) ([episode](../sources/dropboxs-former-most-senior-eng-building.md)).

## Career arc

His MIT PhD produced Granola (distributed transactions via "independent transactions" avoiding two-phase commit), cited by Google's Spanner, and Viewstamped Replication Revisited, which influenced companies like TigerBeetle ([episode](../sources/dropboxs-former-most-senior-eng-building.md)). At Dropbox he led Magic Pocket, the exabyte-scale storage system with a modeled ~24 nines of durability via erasure coding, and the migration off [AWS](aws.md) S3 — peak bandwidth 764 Gbps, then the largest data migration in history — motivated by strategic control and massive pre-IPO savings, though he advises nearly everyone else to stay on the cloud ([episode](../sources/dropboxs-former-most-senior-eng-building.md)). The storage stack went Python to Go to Rust after Go runtime OOMs mimicked disk failures and could 7x load into congestion collapse ([episode](../sources/dropboxs-former-most-senior-eng-building.md)). Frustration with [promotion](../concepts/promotions.md) systems that reward complexity partly drove him to found Convex ([episode](../sources/dropboxs-former-most-senior-eng-building.md)).

## Key views & advice

- Simplicity is the hardest and most scalable property in [systems design](../concepts/systems-design.md): "simple systems are way harder to design than complex systems... If after the fact people think it's obvious, then you really nailed it"; design for validation and for what happens when the system doesn't work. He says AI/agentic development is bad at simplicity, which remains a human domain ([episode](../sources/dropboxs-former-most-senior-eng-building.md)).
- Migration discipline: dark-launch double-writes with six months of required zero-incident operation before deleting from S3; when a bug slipped through, he voluntarily reset the clock at double-digit-million cost — and leadership thanked him ([episode](../sources/dropboxs-former-most-senior-eng-building.md)).
- Orient teams around missions (Storage) not systems (Magic Pocket) so nobody's identity depends on defending an obsolete system ([episode](../sources/dropboxs-former-most-senior-eng-building.md)).
- [Career](../concepts/career-growth.md): choose working with the best people over 20% more pay; stay 3+ years to own the consequences of your decisions; don't enter [management](../concepts/management.md) before staff level or you'll lack the technical depth to influence strategy — and wanting management too much is a red flag ([episode](../sources/dropboxs-former-most-senior-eng-building.md)).
- Don't lead by example — it's passive; his team assumed on-call heroics were "James's job." Teach explicitly, delegate ownership, and fix conflict by demanding 100% alignment on "why," then trusting the team on "how" ([episode](../sources/dropboxs-former-most-senior-eng-building.md)).
- A PhD is training to sit with uncertainty on problems nobody can answer for you — an experience he's glad predated LLMs as a crutch ([episode](../sources/dropboxs-former-most-senior-eng-building.md)).

## Related

- [Episode: Dropbox's Former Most Senior Eng: Building Great Systems and Advice for the AI Era](../sources/dropboxs-former-most-senior-eng-building.md) — his interview
- [John Myles White](john-myles-white.md) — the same complexity-rewarding promo pathology seen from inside Meta
- [Charlie Marsh](charlie-marsh.md) — fellow infra-minded founder on AI-era engineering rigor
- [distributed-systems](../concepts/distributed-systems.md), [systems-design](../concepts/systems-design.md), [promotions](../concepts/promotions.md), [influence-and-leadership](../concepts/influence-and-leadership.md)
