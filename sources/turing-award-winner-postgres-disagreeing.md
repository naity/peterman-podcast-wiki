---
type: source
updated: 2026-07-19
raw: ../raw/turing-award-winner-postgres-disagreeing.md
guest: "Mike Stonebraker"
guest_role: "Turing Award winner, creator of Ingres and Postgres, MIT/Berkeley professor, serial founder"
date: 2026-04-20
url: https://www.developing.dev/p/turing-award-winner-postgres-disagreeing
---

# Turing Award Winner: Postgres, Disagreeing with Google, Future Problems | Mike Stonebraker

[Mike Stonebraker](../entities/mike-stonebraker.md) is a Turing Award winner and the creator of Ingres and Postgres, arguably the most influential figure in database systems history. From [UC Berkeley](../entities/uc-berkeley.md) and later [MIT](../entities/mit.md), he shaped the relational database industry through both academic research and a string of startups (Ingres Corp, Streambase, Vertica, DBOS). The episode covers the origin stories of Ingres and Postgres, competing with Larry Ellison's Oracle, his famous public disagreements with [Google](../entities/google.md) over MapReduce and eventual consistency, why he stayed in academia over big tech, his current company DBOS (replacing OS state with a database), and why he thinks LLM text-to-SQL is far from ready on real-world data warehouses.

## Key takeaways

- Stonebraker started building Ingres at [UC Berkeley](../entities/uc-berkeley.md) in 1972 — one year after Ted Codd's relational paper — knowing nothing about [databases](../concepts/databases.md) or implementations; it earned him tenure in 1976 and spread to ~100 universities because it was a free database on Unix. His advice from this: "think crazy thoughts and try and do them" ([regrets-and-advice](../concepts/regrets-and-advice.md)).
- The push to commercialize Ingres came from a concrete failure: Arizona State could not adopt it for 40,000 student records because there was no COBOL on Unix — an unsupported OS plus unsupported DBMS doomed academic adoption, so he raised VC and founded Ingres Corporation in 1980 ([startups-and-founding](../concepts/startups-and-founding.md)).
- On competing with Oracle: Larry Ellison "made present tense and future tense indistinguishable" — Oracle documented referential integrity in its manual with a footnote "not yet implemented" while Ingres actually shipped it; Stonebraker considers Ellison's sales tactics unconscionable.
- Postgres's defining innovation was an extendable type system, motivated by two failures of Ingres: it couldn't support GIS types (points, lines, polygons) and couldn't let a bond trader overload date subtraction with "bond time" (every month = 30 days). Postgres also had inheritance and (a poorly implemented, later removed) time travel.
- "One size fits none" still holds: stream engines, column stores (Vertica, ClickHouse) and vector stores (Pinecone) each beat a general RDBMS by an order of magnitude in their domain. Postgres is the right "one size fits all" at the low end, but with no column store and no multi-node support it is not competitive for million-TPS workloads or petabyte warehouses.
- He publicly disagreed with [Google](../entities/google.md) twice and says he was vindicated both times: the 2011 paper (with Dave DeWitt) showed distributed databases "beat the heck out of Hadoop," and database people rejected eventual consistency because it breaks integrity constraints (e.g. stock > -1); Google later "completely abandoned" both with Spanner's conventional transactions. Google declined a partnership offer before the 2011 paper.
- He told [Amazon](../entities/amazon.md)/[AWS](../entities/aws.md) directly that supporting ~15 database systems is "about 12 too many" — e.g. graph databases are almost never the performant option and should be a layer over a relational system; retire anything not performant in a market big enough to justify maintenance.
- He chose academia and [startups](../concepts/startups-and-founding.md) over [big tech](../concepts/big-tech-culture.md) because a big company "gives you a boss and company rules," limits publishing, and he is "not cut out for politicking"; part-time work at 2000-person Informix felt bureaucratic and impact-free.
- DBOS (founded 2023, with Databricks co-founder Matei Zaharia) grew out of an academic project to replace the upper half of Linux with a database — a DBMS-backed file system is faster than the Linux file system. VCs rejected the OS pitch but funded the durable-workflow programming layer (TypeScript, Java, Go, Python); ~2/3 of customers are doing agentic AI, and he predicts read-write agents will make workflows a distributed-database/atomicity problem ([ai-era-engineering](../concepts/ai-era-engineering.md)).
- On LLM text-to-SQL: models score ~85% on academic benchmarks (Spider, Bird) but 0% on his real-world data-warehouse benchmark (Beaver) — ~10% with RAG, ~35% even given the FROM clause and join terms — because warehouse data isn't in the training pile, real queries run ~100 lines of SQL, schemas are non-mnemonic and redundant, and data is idiosyncratic.
- Career advice: he's not sure he'd recommend 18-year-olds major in CS anymore (healthcare and building trades look safer); PhD grads should take the most prestigious job available, find a [mentor](../concepts/mentorship-and-sponsorship.md), and pick an area that isn't going with the flow. He tells kids "follow your passion" while admitting he doesn't believe the money works out — but passion beats treating life as "what happens between 5pm and 8am."

## Notable quotes

- "Larry Ellison is a fabulous salesman and... he made present tense and future tense indistinguishable. And so he basically lied to customers." — Mike Stonebraker (~6:43)
- "All the database people said, you know, you're out of your friggin mind... And so Google completely abandoned eventual consistency and completely abandoned MapReduce." — Mike Stonebraker (~21:37–27:00)
- "I think Amazon's problem is that they are supporting, you know, 15 different database systems and that's about 12 too many." — Mike Stonebraker (~27:30)
- "On our benchmarks, large language models get 0% and if you enhance them with rag and all the tricks goes to 10%." — Mike Stonebraker (~44:30)

## Connections

- [Turing Award Winner: Data Abstraction, Dijkstra, Distributed Systems | Barbara Liskov](turing-award-winner-data-abstraction.md) — fellow Turing laureate; abstraction and systems foundations, adjacent era of CS history.
- [Turing Award Winner: TPUs vs GPUs vs CPUs, Computer Architecture, RISC vs CISC | David Patterson](turing-award-winner-tpu-vs-gpu-vs.md) — fellow Berkeley Turing laureate; Stonebraker's GPU/SIMD-vs-indexing discussion complements Patterson's hardware focus.
- [AWS Distinguished Eng: Learnings From 3000 Incidents And How Engineering Is Changing | Marc Brooker](aws-distinguished-eng-learnings-from.md) — the industry counterpoint: Brooker works on the AWS database portfolio Stonebraker criticizes as "12 too many," and chose the distinguished-engineer path Stonebraker rejected.
- [Turing Award Winner On Thinking Clearly, Paxos vs Raft, Working with Dijkstra | Leslie Lamport](turing-award-winner-on-working-with.md) — distributed consistency and transactions from the theory side; directly relevant to the eventual-consistency debate.
- [Dropbox's Former Most Senior Eng: Building Great Systems and Advice for the AI Era | James Cowling](dropboxs-former-most-senior-eng-building.md) — building storage/database-adjacent systems and AI-era advice.
