---
type: entity
entity_kind: org
updated: 2026-07-19
sources: [dropboxs-former-most-senior-eng-building.md]
---

# Dropbox

File-storage company that appears in the podcast through [James Cowling](james-cowling.md), its former most senior engineer, who led Magic Pocket — the multi-exabyte storage system behind what was then the largest data migration in history, off [AWS](aws.md) S3 ([Dropbox's most senior eng](../sources/dropboxs-former-most-senior-eng-building.md)).

The episode makes Dropbox a case study in [systems design](../concepts/systems-design.md) discipline. Magic Pocket hit a modeled ~24 nines of durability via erasure coding spread across racks, power feeds, drive manufacturers and regions; the stack evolved Python → Go → Rust after Go's memory unpredictability caused congestion collapse, ending with storage nodes that bypassed the filesystem entirely ([episode](../sources/dropboxs-former-most-senior-eng-building.md)). The migration ran as a dark launch double-writing to S3 and Magic Pocket with a founder-mandated six months of zero incidents before deleting anything — and when one bug slipped to production, Cowling voluntarily reset the clock at a cost of double-digit millions, and leadership thanked him ([episode](../sources/dropboxs-former-most-senior-eng-building.md)). The counter-intuitive lesson he draws: simplicity scales — the block index was "just" 1,000 MySQL nodes, trivially walkable for continuous validation — and despite Dropbox's success he tells almost everyone else *not* to build their own infrastructure ([episode](../sources/dropboxs-former-most-senior-eng-building.md)).

## People

- [James Cowling](james-cowling.md) — most senior engineer, Magic Pocket lead; [MIT](mit.md) PhD, now CTO of Convex

## Related

- [systems-design](../concepts/systems-design.md), [distributed-systems](../concepts/distributed-systems.md) — Magic Pocket as the podcast's flagship infrastructure story
- [AWS](aws.md) — the other side of the S3 migration
- [Episode: Dropbox's Former Most Senior Eng: Building Great Systems](../sources/dropboxs-former-most-senior-eng-building.md)
