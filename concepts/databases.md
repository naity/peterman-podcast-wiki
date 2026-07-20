---
type: concept
updated: 2026-07-19
sources: [turing-award-winner-postgres-disagreeing.md, aws-distinguished-eng-learnings-from.md, turing-award-winner-data-abstraction.md, uber-distinguished-eng-on-unfair.md]
---

# Databases

Database systems as told by the field's founder ([Mike Stonebraker](../entities/mike-stonebraker.md), creator of Ingres and Postgres), one of its biggest industrial builders ([Marc Brooker](../entities/marc-brooker.md), AWS databases), and the people who imported its ideas into distributed computing and platform operations.

## What the guests say

### One size fits none — or twelve too many?

Stonebraker's standing thesis: stream engines, column stores, and vector stores each beat a general RDBMS by an order of magnitude in their domain; Postgres is the right "one size fits all" only at the low end ([episode](../sources/turing-award-winner-postgres-disagreeing.md)). Yet he told [Amazon](../entities/amazon.md) directly that supporting ~15 database systems is "about 12 too many" — graph databases, for instance, are almost never the performant option and should be layers over a relational engine. This lands as a direct, named disagreement with Brooker, who builds that AWS portfolio ([episode](../sources/aws-distinguished-eng-learnings-from.md)) — the source pages themselves flag the pairing as a counterpoint. Operational evidence cuts Stonebraker's way from an unexpected quarter: [Joakim Recht](../entities/joakim-recht.md) found Uber running ~52 database technologies with per-technology team toolchains, and the fix was consolidation onto one platform (Odin: ~500,000 databases operated by ~20 people) ([episode](../sources/uber-distinguished-eng-on-unfair.md)).

### Consistency and transactions keep winning

Stonebraker recounts his two public fights with [Google](../entities/google.md): the 2011 paper showing distributed databases "beat the heck out of Hadoop," and the database community's rejection of eventual consistency because it breaks integrity constraints — both, he claims, vindicated when Spanner returned to conventional transactions ([episode](../sources/turing-award-winner-postgres-disagreeing.md)). [Barbara Liskov](../entities/barbara-liskov.md) shows the traffic flowing the other way decades earlier: her language Argus borrowed atomic transactions *from* the database field so distributed computations complete entirely or not at all — work that led to Viewstamped Replication, "the beginning of cloud storage" ([episode](../sources/turing-award-winner-data-abstraction.md)). Brooker's Aurora DSQL is the modern synthesis: MVCC plus optimistic commit-time checks (readers never block writers, ~<10% storage overhead), designed explicitly against outage patterns like a stalled client holding locks — and his problem-finding formula (serverless developers stuck with serverful relational databases × object storage as durability layer) produced Aurora Serverless and DSQL ([episode](../sources/aws-distinguished-eng-learnings-from.md)).

### Where databases came from and where they're going

Stonebraker started Ingres at [UC Berkeley](../entities/uc-berkeley.md) in 1972, one year after Codd's relational paper, knowing nothing about databases; it spread because it was a free database on Unix, and commercialization was forced by a concrete adoption failure (no COBOL on Unix for Arizona State's 40,000 student records). Postgres's defining innovation — the extendable type system — came from two concrete Ingres failures (GIS types; a bond trader's "bond time" date arithmetic) ([episode](../sources/turing-award-winner-postgres-disagreeing.md)). His current bet, DBOS, treats OS state as a database problem (a DBMS-backed file system beating the Linux file system), with ~2/3 of customers doing agentic AI — he predicts read-write agents will make workflows a distributed-database/atomicity problem. He is bearish on LLM text-to-SQL for real warehouses: ~85% on academic benchmarks, 0% on his real-world Beaver benchmark (~10% with RAG), because warehouse schemas are non-mnemonic, queries run ~100 lines, and the data isn't in the training pile ([episode](../sources/turing-award-winner-postgres-disagreeing.md)).

**Tension worth watching:** Brooker's portfolio-building and Stonebraker's consolidationism are both anti-hype positions — Brooker warns against bolting caches onto databases (metastable failures) and levels postmortem patterns up into whole-class fixes ([episode](../sources/aws-distinguished-eng-learnings-from.md)); Stonebraker wants unperformant engines retired outright ([episode](../sources/turing-award-winner-postgres-disagreeing.md)). The unresolved question between them is whether specialized engines are product surface or maintenance debt.

## Practical takeaways

- Match the engine to the workload — specialized stores win their domains by ~10x — but audit how many engines your org can actually operate; Uber's answer was "far fewer than 52" ([Stonebraker](../sources/turing-award-winner-postgres-disagreeing.md), [Recht](../sources/uber-distinguished-eng-on-unfair.md)).
- Don't bet against transactions: eventual consistency keeps losing to integrity constraints, even at Google scale ([Stonebraker](../sources/turing-award-winner-postgres-disagreeing.md)).
- Design database systems against known outage patterns (lock-holding stalls, cold caches), not just benchmarks ([Brooker](../sources/aws-distinguished-eng-learnings-from.md)).
- Extensibility is a durable moat — Postgres's type system outlived every rival feature ([Stonebraker](../sources/turing-award-winner-postgres-disagreeing.md)).
- Treat LLM text-to-SQL demos with suspicion until they're tested on your warehouse's real schemas ([Stonebraker](../sources/turing-award-winner-postgres-disagreeing.md)).

## Related

- [distributed-systems](distributed-systems.md) — consensus, replication, and the transaction bridge; [systems-design](systems-design.md) — Brooker's problem-finding method; [incident-management](incident-management.md) — postmortems as database-design input; [ai-era-engineering](ai-era-engineering.md) — agents as a database workload.
- Key people: [Mike Stonebraker](../entities/mike-stonebraker.md), [Marc Brooker](../entities/marc-brooker.md), [Barbara Liskov](../entities/barbara-liskov.md), [Joakim Recht](../entities/joakim-recht.md).
- Most relevant episodes: [Stonebraker](../sources/turing-award-winner-postgres-disagreeing.md), [Brooker](../sources/aws-distinguished-eng-learnings-from.md).
